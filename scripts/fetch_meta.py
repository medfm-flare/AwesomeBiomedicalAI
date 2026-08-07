#!/usr/bin/env python3
"""Turn a paper link into a pre-filled YAML stub.

    python scripts/fetch_meta.py https://www.nature.com/articles/s41591-024-02857-3
    python scripts/fetch_meta.py 10.1038/s41586-024-07894-z
    python scripts/fetch_meta.py 2411.19666            # arXiv id

Bibliographic fields (date, title, venue, DOI, first/last author) come from
Crossref or arXiv, so they are correct by construction. The fields that need
someone to actually read the paper -- backbone, pre-training, data scale,
tasks, performance -- come back as TODO markers for a human or an LLM to fill.

Splitting it this way is deliberate: an LLM asked for everything at once will
also hallucinate the publication month.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.schema import Vocab, normalize_doi  # noqa: E402

USER_AGENT = "AwesomeBiomedicalAI-fetchmeta (+https://github.com/medfm-flare/AwesomeBiomedicalAI)"
ARXIV_ID = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?$")


def get_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def match_venue(container: str, short: str, vocab: Vocab) -> tuple[str, list[str]]:
    """Map a Crossref container title onto our controlled venue vocabulary."""
    notes: list[str] = []
    for candidate in (short, container):
        if not candidate:
            continue
        normalized = candidate.strip().rstrip(".").lower()
        for name, meta in vocab.venues.items():
            known = [name, meta.get("pubmed"), *(meta.get("aliases") or [])]
            if any(
                k and k.strip().rstrip(".").lower() == normalized for k in known
            ):
                return name, notes
    guess = short or container or "UNKNOWN"
    notes.append(
        f"venue {guess!r} is not in data/vocab.yaml -- add it there (with a `short` "
        "for the NotebookLM filename) or map it to an existing entry"
    )
    return guess, notes


def from_crossref(doi: str, vocab: Vocab) -> tuple[dict, list[str]]:
    message = get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]

    parts = (
        message.get("published", {})
        or message.get("published-print", {})
        or message.get("published-online", {})
    ).get("date-parts", [[]])[0]
    year = parts[0] if parts else None
    month = parts[1] if len(parts) > 1 else 1

    container = (message.get("container-title") or [""])[0]
    short = (message.get("short-container-title") or [""])[0]
    venue, notes = match_venue(container, short, vocab)

    authors = message.get("author") or []

    def person(author: dict | None) -> dict:
        if not author:
            return {"name": "TODO"}
        name = f"{author.get('given', '')} {author.get('family', '')}".strip()
        return {"name": name or "TODO", "scholar": None}

    return (
        {
            "date": f"{year}-{month:02d}" if year else "TODO",
            "title": re.sub(r"\s+", " ", (message.get("title") or ["TODO"])[0]).strip(),
            "url": message.get("URL") or f"https://doi.org/{doi}",
            "doi": message.get("DOI", doi),
            "venue": venue,
            "authors": {"first": person(authors[0] if authors else None),
                        "last": person(authors[-1] if authors else None)},
        },
        notes,
    )


def from_arxiv(arxiv_id: str, vocab: Vocab) -> tuple[dict, list[str]]:
    request = urllib.request.Request(
        f"http://export.arxiv.org/api/query?id_list={arxiv_id}",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        root = ET.fromstring(response.read())

    ns = "{http://www.w3.org/2005/Atom}"
    entry = root.find(f"{ns}entry")
    if entry is None:
        raise SystemExit(f"arXiv returned nothing for {arxiv_id}")

    published = (entry.findtext(f"{ns}published") or "")[:7]
    names = [(a.findtext(f"{ns}name") or "").strip() for a in entry.findall(f"{ns}author")]
    notes = [
        "arXiv preprint -- check whether a journal version exists and prefer it; "
        "if it is published, use the journal DOI so dedup works"
    ]
    return (
        {
            "date": published or "TODO",
            "title": re.sub(r"\s+", " ", entry.findtext(f"{ns}title") or "").strip(),
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "doi": f"10.48550/arXiv.{arxiv_id}",
            "venue": "arXiv",
            "authors": {
                "first": {"name": names[0] if names else "TODO", "scholar": None},
                "last": {"name": names[-1] if names else "TODO", "scholar": None},
            },
        },
        notes,
    )


TEMPLATE = """\
# Paste this into data/<domain>.yaml, fill every TODO, then run:
#     python scripts/build.py && python scripts/validate.py
{notes}
- date: {date}
  title: {title}
  url: {url}
  doi: {doi}
  venue: {venue}
  authors:
    first:
      name: {first_name}
      scholar: null            # TODO Google Scholar profile
    last:
      name: {last_name}
      scholar: null            # TODO Google Scholar profile
  model:
    name: TODO                 # the model/system name, e.g. UNI
    repo: null                 # TODO GitHub URL if there is one
    weights: null              # TODO Hugging Face URL if weights are released
    license: null
  params: null                 # TODO e.g. 632M / 4.6B -- omit rather than guess
  backbone: TODO               # architecture in one line
  pretraining: []              # TODO from the `pretraining` list in data/vocab.yaml
  pretraining_detail: TODO
  data:
    description: TODO
    scale:
      whole_slide_images: 0    # TODO replace with the real counts, drop unused keys
  tasks: []                    # TODO from the `tasks` list in data/vocab.yaml
  tasks_detail: TODO
  modalities: []               # TODO from the `modalities` list in data/vocab.yaml
  performance: []              # TODO [{{benchmark: ..., metric: ..., value: ...}}]
  added: {{date: {added}, by: TODO}}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("link", help="DOI, publisher URL, or arXiv id")
    parser.add_argument("--added-by", default="TODO", help="your name, for the `added` field")
    parser.add_argument("--month", default=None, help="value for added.date (YYYY-MM)")
    args = parser.parse_args()

    vocab = Vocab.load()
    raw = args.link.strip()

    arxiv_match = ARXIV_ID.search(raw) if ("arxiv" in raw.lower() or "/" not in raw) else None
    if arxiv_match:
        fields, notes = from_arxiv(arxiv_match.group(1), vocab)
    else:
        doi = normalize_doi(raw)
        if not doi:
            raise SystemExit(
                f"Could not extract a DOI or arXiv id from {raw!r}.\n"
                "Pass the DOI directly, e.g. 10.1038/s41591-024-02857-3"
            )
        fields, notes = from_crossref(doi, vocab)

    banner = ""
    if notes:
        banner = "#\n" + "\n".join(f"# NOTE: {n}" for n in notes) + "\n"

    added = args.month or fields["date"]
    print(
        TEMPLATE.format(
            notes=banner,
            date=fields["date"],
            title=fields["title"],
            url=fields["url"],
            doi=fields["doi"],
            venue=fields["venue"],
            first_name=fields["authors"]["first"]["name"],
            last_name=fields["authors"]["last"]["name"],
            added=added,
        ).replace("by: TODO", f"by: {args.added_by}")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
