"""The paper record schema, and validation against it.

One module owns what a catalogue entry looks like. `build.py`, `validate.py`
and `discover.py` all import from here so the three can never disagree.

Deliberately dependency-free apart from PyYAML: CI should not need a resolver
step to check a pull request.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"

DATE_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
URL_RE = re.compile(r"^https?://\S+$")
# "4.6B", "632M", "7B", "110M" -- a number and a magnitude, nothing else.
PARAMS_RE = re.compile(r"^\d+(\.\d+)?[KMBT]$")


@dataclass
class Issue:
    """A single validation problem, addressed to whoever edited the YAML."""

    level: str  # "error" blocks the merge, "warn" does not
    where: str
    message: str

    def __str__(self) -> str:
        mark = "ERROR" if self.level == "error" else "warn "
        return f"  {mark}  {self.where}: {self.message}"


@dataclass
class Vocab:
    venues: dict
    tasks: list
    modalities: list
    pretraining: list
    discovery_keywords: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path | None = None) -> "Vocab":
        raw = yaml.safe_load((path or DATA_DIR / "vocab.yaml").read_text())
        return cls(
            venues=raw["venues"],
            tasks=raw["tasks"],
            modalities=raw["modalities"],
            pretraining=raw["pretraining"],
            discovery_keywords=raw.get("discovery_keywords", {}),
        )

    def venue_by_pubmed(self, abbrev: str) -> str | None:
        """Map an NLM abbreviation (or a known alias) to our canonical venue name."""
        target = (abbrev or "").strip().rstrip(".").lower()
        if not target:
            return None
        for name, meta in self.venues.items():
            known = [name, meta.get("pubmed"), *(meta.get("aliases") or [])]
            if any(k and k.strip().rstrip(".").lower() == target for k in known):
                return name
        return None

    def venue_short(self, venue: str) -> str:
        entry = self.venues.get(venue)
        return entry["short"] if entry else re.sub(r"[^A-Za-z0-9]", "", venue)

    def high_impact_venues(self) -> list[str]:
        return [v for v, meta in self.venues.items() if meta.get("high_impact")]


# ---------------------------------------------------------------------------
# Field specification
#
#   required  -- absent or null is an error
#   expected  -- absent or null is a warning; we want it, papers vary
#   optional  -- silence
# ---------------------------------------------------------------------------
REQUIRED = ["date", "title", "url", "venue", "model"]
EXPECTED = ["doi", "authors", "backbone", "data", "tasks", "modalities"]
KNOWN_FIELDS = set(REQUIRED) | set(EXPECTED) | {
    "params",
    "pretraining",
    "pretraining_detail",
    "tasks_detail",
    "performance",
    "notebooklm",
    "added",
    "verify",
    "note",
}


def normalize_doi(value: str | None) -> str | None:
    """Reduce a DOI or a publisher URL to a bare lowercase DOI.

    This is the dedup key. `10.1038/S41586-024-07441-W`,
    `https://doi.org/10.1038/s41586-024-07441-w` and
    `https://www.nature.com/articles/s41586-024-07441-w` must all collapse to
    the same string or the weekly bot will re-propose papers we already have.
    """
    if not value:
        return None
    text = str(value).strip()
    text = re.sub(r"^https?://(dx\.)?doi\.org/", "", text, flags=re.I)
    text = re.sub(r"^doi:\s*", "", text, flags=re.I)

    if not text.lower().startswith("10."):
        # Try to recover a DOI from a known publisher URL shape.
        m = re.search(r"nature\.com/articles/([a-z0-9\-.]+)", text, re.I)
        if m:
            text = f"10.1038/{m.group(1)}"
        else:
            m = re.search(r"(10\.\d{4,9}/[^\s?#]+)", text)
            if not m:
                return None
            text = m.group(1)

    text = text.rstrip(").,;")
    text = re.sub(r"[?#].*$", "", text)
    return text.lower()


def entry_key(entry: dict) -> str:
    """Dedup identity: DOI when we have one, else normalized title."""
    doi = normalize_doi(entry.get("doi") or entry.get("url"))
    if doi:
        return f"doi:{doi}"
    title = re.sub(r"[^a-z0-9]+", " ", str(entry.get("title", "")).lower()).strip()
    return f"title:{title}"


def notebooklm_stem(entry: dict, vocab: Vocab) -> str:
    """Filename stem for the NotebookLM upload, e.g. `202607-NatMed-PRISM2`.

    Generated rather than typed so nine maintainers cannot drift apart on it.
    """
    date = str(entry.get("date", "")).replace("-", "")
    short = vocab.venue_short(entry.get("venue", ""))
    model = (entry.get("model") or {}).get("name") or entry.get("title", "")
    model = re.sub(r"[^A-Za-z0-9.+-]", "", str(model).split("(")[0].strip())
    return f"{date}-{short}-{model}"


def _check_str_list(value, allowed, where, label, issues, vocab_name):
    if value is None:
        return
    if not isinstance(value, list):
        issues.append(Issue("error", where, f"{label} must be a list"))
        return
    for item in value:
        if item not in allowed:
            issues.append(
                Issue(
                    "error",
                    where,
                    f"{label} value {item!r} is not in the {vocab_name} vocabulary "
                    f"(add it to data/vocab.yaml if it is genuinely new)",
                )
            )


def validate_entry(entry: dict, where: str, vocab: Vocab) -> list[Issue]:
    """Validate one paper record. Returns every problem, not just the first."""
    issues: list[Issue] = []

    if not isinstance(entry, dict):
        return [Issue("error", where, "entry is not a mapping")]

    for key in entry:
        if key not in KNOWN_FIELDS:
            issues.append(
                Issue("error", where, f"unknown field {key!r} (typo? see CONTRIBUTING.md)")
            )

    for name in REQUIRED:
        if entry.get(name) in (None, "", []):
            issues.append(Issue("error", where, f"missing required field {name!r}"))
    for name in EXPECTED:
        if entry.get(name) in (None, "", []):
            issues.append(Issue("warn", where, f"missing {name!r}"))

    date = entry.get("date")
    if date is not None and not DATE_RE.match(str(date)):
        issues.append(
            Issue("error", where, f"date {date!r} must be YYYY-MM (e.g. 2026-07)")
        )

    url = entry.get("url")
    if url and not URL_RE.match(str(url)):
        issues.append(Issue("error", where, f"url {url!r} is not an http(s) URL"))

    doi = entry.get("doi")
    if doi and not DOI_RE.match(str(doi)):
        issues.append(
            Issue("error", where, f"doi {doi!r} should be a bare DOI, e.g. 10.1038/s41586-024-07441-w")
        )

    venue = entry.get("venue")
    if venue and venue not in vocab.venues:
        issues.append(
            Issue(
                "error",
                where,
                f"venue {venue!r} is not in the vocabulary "
                f"(add it to data/vocab.yaml, with a `short` for the NotebookLM filename)",
            )
        )

    params = entry.get("params")
    if params is not None and not PARAMS_RE.match(str(params)):
        issues.append(
            Issue("error", where, f"params {params!r} must look like 632M / 4.6B / 7B")
        )

    model = entry.get("model")
    if isinstance(model, dict):
        if not model.get("name"):
            issues.append(Issue("error", where, "model.name is required"))
        for link_field in ("repo", "weights"):
            link = model.get(link_field)
            if link and not URL_RE.match(str(link)):
                issues.append(
                    Issue("error", where, f"model.{link_field} {link!r} is not a URL")
                )
    elif model is not None:
        issues.append(Issue("error", where, "model must be a mapping with a `name`"))

    authors = entry.get("authors")
    if isinstance(authors, dict):
        for role in ("first", "last"):
            person = authors.get(role)
            if person is None:
                issues.append(Issue("warn", where, f"authors.{role} is missing"))
            elif not isinstance(person, dict) or not person.get("name"):
                issues.append(Issue("error", where, f"authors.{role} needs a `name`"))
    elif authors is not None:
        issues.append(Issue("error", where, "authors must be a mapping with first/last"))

    _check_str_list(entry.get("tasks"), vocab.tasks, where, "tasks", issues, "task")
    _check_str_list(
        entry.get("modalities"), vocab.modalities, where, "modalities", issues, "modality"
    )
    _check_str_list(
        entry.get("pretraining"),
        vocab.pretraining,
        where,
        "pretraining",
        issues,
        "pretraining",
    )

    perf = entry.get("performance")
    if perf is not None:
        if not isinstance(perf, list):
            issues.append(Issue("error", where, "performance must be a list"))
        else:
            for i, row in enumerate(perf):
                if not isinstance(row, dict):
                    issues.append(Issue("error", where, f"performance[{i}] is not a mapping"))
                    continue
                for name in ("benchmark", "metric", "value"):
                    if row.get(name) in (None, ""):
                        issues.append(
                            Issue("error", where, f"performance[{i}] is missing {name!r}")
                        )

    nlm = entry.get("notebooklm")
    if nlm and not URL_RE.match(str(nlm)):
        issues.append(Issue("error", where, f"notebooklm {nlm!r} is not a URL"))

    return issues


def load_domain(slug: str) -> list[dict]:
    """Load one domain's papers, newest first. Missing file -> empty list."""
    path = DATA_DIR / f"{slug}.yaml"
    if not path.exists():
        return []
    raw = yaml.safe_load(path.read_text()) or []
    if not isinstance(raw, list):
        raise ValueError(f"{path} must contain a list of papers")
    return sorted(raw, key=lambda e: str(e.get("date", "")), reverse=True)


def load_domains() -> list[dict]:
    return yaml.safe_load((DATA_DIR / "domains.yaml").read_text())
