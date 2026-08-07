#!/usr/bin/env python3
"""Render the catalogue markdown from data/*.yaml.

    python scripts/build.py            # write the markdown files
    python scripts/build.py --check    # fail if anything on disk is stale (CI)

Pages migrate one at a time. A domain with a `data/<slug>.yaml` is generated;
a domain without one stays hand-maintained and we only count its table rows for
the README. That way nobody is blocked on a big-bang conversion.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.schema import (  # noqa: E402
    DATA_DIR,
    REPO_ROOT,
    Vocab,
    load_domain,
    load_domains,
    notebooklm_stem,
)

GENERATED_BANNER = (
    "<!-- GENERATED FILE - DO NOT EDIT BY HAND -->\n"
    "<!-- Source: {source} | Regenerate: python scripts/build.py -->\n"
)

# Compact labels for the index table's data column.
SCALE_LABELS = {
    "whole_slide_images": "WSI",
    "evaluation_wsi": "WSI (eval)",
    "image_text_pairs": "pairs",
    "image_caption_pairs": "pairs",
    "qa_pairs": "QA pairs",
    "semantic_groups": "groups",
    "synthetic_captions": "captions",
    "patients": "patients",
    "specimens": "specimens",
}
# Priority order when picking the one number that goes in the index table.
SCALE_PRIORITY = [
    "whole_slide_images",
    "image_text_pairs",
    "image_caption_pairs",
    "patients",
    "evaluation_wsi",
    "semantic_groups",
]


def human_number(n: int) -> str:
    for size, suffix in ((1_000_000_000, "B"), (1_000_000, "M"), (1_000, "K")):
        if n >= size:
            value = n / size
            return f"{value:.1f}".rstrip("0").rstrip(".") + suffix
    return str(n)


def escape_cell(text: str) -> str:
    """Make a value safe inside a markdown table cell."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def safe_url(url: str) -> str:
    """Percent-encode the parentheses markdown link targets cannot carry.

    Elsevier PIIs are full of them: .../PIIS1470-2045(25)00661-8/abstract would
    otherwise terminate the link at the first `)`.
    """
    return str(url).replace("(", "%28").replace(")", "%29")


def link(url: str, text: str | None = None) -> str:
    """A markdown link whose label defaults to the host + path, not the raw URL."""
    if not text:
        text = re.sub(r"^https?://(www\.)?", "", str(url)).rstrip("/")
        if len(text) > 60:
            text = text[:57] + "…"
    return f"[{text}]({safe_url(url)})"


def anchor_id(entry: dict) -> str:
    name = (entry.get("model") or {}).get("name") or entry.get("title", "")
    slug = re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")
    return f"model-{slug}-{str(entry.get('date', '')).replace('-', '')}"


def headline_scale(entry: dict) -> str:
    scale = (entry.get("data") or {}).get("scale") or {}
    if not scale:
        return "—"
    key = next((k for k in SCALE_PRIORITY if k in scale), None) or next(iter(scale))
    value = scale[key]
    if not isinstance(value, int):
        return escape_cell(value)
    label = SCALE_LABELS.get(key, key.replace("_", " "))
    return f"{human_number(value)} {label}"


def person_link(person: dict | None) -> str:
    if not person or not person.get("name"):
        return "—"
    name = person["name"]
    url = person.get("scholar") or person.get("homepage")
    return link(url, name) if url else name


def code_cell(entry: dict) -> str:
    model = entry.get("model") or {}
    links = []
    if model.get("repo"):
        links.append(link(model["repo"], "code"))
    if model.get("weights"):
        links.append(link(model["weights"], "weights"))
    return " · ".join(links) if links else "—"


def maintainer_line(maintainers: list[dict]) -> str:
    """Render maintainers with whatever profile links they have supplied."""
    parts = []
    for m in maintainers or []:
        name = m.get("name", "unknown")
        primary = m.get("homepage") or m.get("scholar") or (
            f"https://github.com/{m['github']}" if m.get("github") else None
        )
        label = f"[{name}]({primary})" if primary else name

        extras = []
        for key, text in (
            ("homepage", "homepage"),
            ("scholar", "Scholar"),
            ("linkedin", "LinkedIn"),
            ("twitter", "X"),
            ("github", "GitHub"),
        ):
            value = m.get(key)
            if not value:
                continue
            if key == "github":
                value = f"https://github.com/{value}"
            if value == primary:
                continue
            extras.append(f"[{text}]({value})")
        if extras:
            label += " (" + " · ".join(extras) + ")"
        parts.append(label)
    return ", ".join(parts) if parts else "_unassigned_"


# ---------------------------------------------------------------------------
# Domain page
# ---------------------------------------------------------------------------

def render_index_table(entries: list[dict]) -> list[str]:
    lines = [
        "| Date | Model | Paper | Venue | Size | Training data | Resources |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for entry in entries:
        model = entry.get("model") or {}
        name = model.get("name", "—")
        lines.append(
            "| {date} | [{name}](#{anchor}) | [{title}]({url}) | {venue} | {params} "
            "| {scale} | {code} |".format(
                date=entry.get("date", "—"),
                name=escape_cell(name),
                anchor=anchor_id(entry),
                title=escape_cell(entry.get("title", "—")),
                url=safe_url(entry.get("url", "")),
                venue=escape_cell(entry.get("venue", "—")),
                params=entry.get("params") or "—",
                scale=headline_scale(entry),
                code=code_cell(entry),
            )
        )
    return lines


def render_detail(entry: dict, vocab: Vocab) -> list[str]:
    model = entry.get("model") or {}
    authors = entry.get("authors") or {}
    out: list[str] = []

    out.append(f'<a id="{anchor_id(entry)}"></a>')
    out.append("")
    out.append(f"### {model.get('name', entry.get('title', 'Untitled'))}")
    out.append("")
    out.append(f"**{link(entry.get('url', ''), entry.get('title', ''))}**")
    out.append("")

    byline = [f"*{entry.get('venue', '')}* · {entry.get('date', '')}"]
    first, last = person_link(authors.get("first")), person_link(authors.get("last"))
    if first != "—" or last != "—":
        byline.append(f"{first} & {last}")
    if entry.get("doi"):
        byline.append(link(f"https://doi.org/{entry['doi']}", f"doi:{entry['doi']}"))
    out.append(" · ".join(byline))
    out.append("")

    rows: list[tuple[str, str]] = []
    if entry.get("params"):
        rows.append(("Parameters", entry["params"]))
    if model.get("params_note"):
        rows.append(("Parameter note", model["params_note"]))
    if entry.get("backbone"):
        rows.append(("Backbone", entry["backbone"]))

    pretraining = entry.get("pretraining") or []
    detail = entry.get("pretraining_detail")
    if pretraining or detail:
        value = ", ".join(f"`{p}`" for p in pretraining)
        if detail:
            value = f"{value}<br>{detail}" if value else detail
        rows.append(("Pre-training", value))

    data = entry.get("data") or {}
    if data:
        value = data.get("description", "")
        scale = data.get("scale") or {}
        if scale:
            chips = " · ".join(
                f"**{v:,}** {SCALE_LABELS.get(k, k.replace('_', ' '))}"
                if isinstance(v, int)
                else f"**{v}** {k.replace('_', ' ')}"
                for k, v in scale.items()
            )
            value = f"{value}<br>{chips}" if value else chips
        rows.append(("Training data", value))

    tasks = entry.get("tasks") or []
    tasks_detail = entry.get("tasks_detail")
    if tasks or tasks_detail:
        value = ", ".join(f"`{t}`" for t in tasks)
        if tasks_detail:
            value = f"{value}<br>{tasks_detail}" if value else tasks_detail
        rows.append(("Downstream tasks", value))

    if entry.get("modalities"):
        rows.append(("Modalities", ", ".join(f"`{m}`" for m in entry["modalities"])))
    if model.get("repo"):
        rows.append(("Code", link(model["repo"])))
    if model.get("weights"):
        rows.append(("Weights", link(model["weights"])))
    if model.get("license"):
        rows.append(("License", model["license"]))
    if entry.get("notebooklm"):
        rows.append(("NotebookLM", link(entry["notebooklm"], "open notebook")))
    rows.append(("PDF name", f"`{notebooklm_stem(entry, vocab)}.pdf`"))
    if entry.get("note"):
        rows.append(("Note", entry["note"]))

    out.append("| | |")
    out.append("| --- | --- |")
    for label, value in rows:
        out.append(f"| **{label}** | {escape_cell(value)} |")
    out.append("")

    perf = entry.get("performance") or []
    if perf:
        out.append("**Reported performance**")
        out.append("")
        out.append("| Benchmark | Metric | Value | Note |")
        out.append("| --- | --- | --- | --- |")
        for row in perf:
            out.append(
                "| {b} | {m} | {v} | {n} |".format(
                    b=escape_cell(row.get("benchmark", "")),
                    m=escape_cell(row.get("metric", "")),
                    v=escape_cell(row.get("value", "")),
                    n=escape_cell(row.get("note", "") or ""),
                )
            )
        out.append("")

    if entry.get("verify"):
        out.append("> [!NOTE]")
        out.append("> Needs checking before this entry is considered final:")
        for item in entry["verify"]:
            out.append(f"> - {str(item).strip()}")
        out.append("")

    return out


def render_domain_page(domain: dict, entries: list[dict], vocab: Vocab) -> str:
    slug = domain["slug"]
    out = [GENERATED_BANNER.format(source=f"data/{slug}.yaml")]
    out.append(f"# {domain['name']}")
    out.append("")
    out.append(f"{domain['scope']}.")
    out.append("")
    out.append(f"**Maintainer:** {maintainer_line(domain.get('maintainers'))}")
    out.append("")

    summary = [f"**{len(entries)} entries**"]
    if domain.get("notebooklm"):
        summary.append(f"[NotebookLM]({domain['notebooklm']})")
    summary.append("[Back to index](README.md)")
    out.append(" · ".join(summary))
    out.append("")

    if not entries:
        out.append("_No entries yet._")
        return "\n".join(out) + "\n"

    out.extend(render_index_table(entries))
    out.append("")
    out.append("## Details")
    out.append("")
    for entry in entries:
        out.extend(render_detail(entry, vocab))

    out.append("---")
    out.append("")
    out.append(
        f"Add a paper by editing [`data/{slug}.yaml`](data/{slug}.yaml) and running "
        "`python scripts/build.py`. See [CONTRIBUTING.md](CONTRIBUTING.md)."
    )
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------

LEGACY_ROW_RE = re.compile(r"^\|\s*(\d{6}|\d{4}-\d{2})\s*\|")


def count_legacy_rows(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text().splitlines() if LEGACY_ROW_RE.match(line))


def render_readme(domains: list[dict], counts: dict[str, int]) -> str:
    total = sum(counts.values())
    migrated = sum(1 for d in domains if (DATA_DIR / f"{d['slug']}.yaml").exists())

    out = [GENERATED_BANNER.format(source="data/domains.yaml")]
    out.append("# Awesome Biomedical AI Models")
    out.append("")
    out.append(
        "A curated catalogue of biomedical AI models and systems published in leading "
        "journals, with the architecture, pre-training recipe, training data and "
        "downstream tasks recorded for each one."
    )
    out.append("")
    out.append(f"**{total} models** across {len(domains)} domains.")
    out.append("")
    out.append("## Browse by domain")
    out.append("")
    out.append("| Domain | Scope | Models | Maintainer | NotebookLM |")
    out.append("| --- | --- | ---: | --- | --- |")
    for domain in domains:
        notebook = domain.get("notebooklm")
        out.append(
            "| [{name}]({file}) | {scope} | {count} | {maint} | {nb} |".format(
                name=domain["name"],
                file=domain["file"],
                scope=escape_cell(domain["scope"]),
                count=counts.get(domain["slug"], 0),
                maint=escape_cell(maintainer_line(domain.get("maintainers"))),
                nb=f"[NotebookLM]({notebook})" if notebook else "—",
            )
        )
    out.append("")
    out.append("## Contributing")
    out.append("")
    out.append(
        "Entries live in `data/*.yaml` and the markdown pages are generated from them, "
        "so a pull request should edit the YAML rather than the tables. "
        "[CONTRIBUTING.md](CONTRIBUTING.md) covers the schema, how to pick a domain, "
        "and the one-command way to turn a paper link into an entry."
    )
    out.append("")
    out.append("```bash")
    out.append("pip install -r requirements.txt")
    out.append("python scripts/build.py       # regenerate the markdown")
    out.append("python scripts/validate.py    # check the data before pushing")
    out.append("```")
    out.append("")
    verb = "is" if migrated == 1 else "are"
    out.append(
        f"{migrated} of {len(domains)} pages {verb} on the structured format so far; "
        "the rest are still hand-maintained markdown and can migrate one at a time."
    )
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit non-zero if any generated file is out of date",
    )
    args = parser.parse_args()

    vocab = Vocab.load()
    domains = load_domains()

    rendered: dict[Path, str] = {}
    counts: dict[str, int] = {}

    for domain in domains:
        slug = domain["slug"]
        page = REPO_ROOT / domain["file"]
        if (DATA_DIR / f"{slug}.yaml").exists():
            entries = load_domain(slug)
            counts[slug] = len(entries)
            rendered[page] = render_domain_page(domain, entries, vocab)
        else:
            counts[slug] = count_legacy_rows(page)

    rendered[REPO_ROOT / "README.md"] = render_readme(domains, counts)

    stale: list[Path] = []
    for path, content in rendered.items():
        current = path.read_text() if path.exists() else None
        if current == content:
            continue
        stale.append(path)
        if not args.check:
            path.write_text(content)

    rel = lambda p: p.relative_to(REPO_ROOT)  # noqa: E731

    if args.check:
        if stale:
            print("Generated files are out of date:")
            for path in stale:
                print(f"  - {rel(path)}")
            print("\nRun `python scripts/build.py` and commit the result.")
            return 1
        print(f"All {len(rendered)} generated files are up to date.")
        return 0

    if stale:
        for path in stale:
            print(f"wrote {rel(path)}")
    else:
        print("No changes.")
    print(f"{sum(counts.values())} models across {len(domains)} domains.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
