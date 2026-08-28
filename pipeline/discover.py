#!/usr/bin/env python3
"""Find candidate AI4Science papers via PubMed and OpenAlex.

This only searches and dedupes -- it never extracts or writes an entry.
Candidates get handed to ingest.fetch_entry() (same as a manually-pasted
URL) by whoever reviews them, so fit_score/review_gate do the real
filtering; this step just needs to cast a reasonably wide net.

Usage:
    python3 pipeline/discover.py [--days 7] [--max 40]

Stdlib only (urllib) -- no new dependency. Neither API requires a key for
this volume of use; set NCBI_API_KEY in .env to raise PubMed's rate limit
if that starts getting throttled.
"""
import argparse
import datetime
import json
import os
import sys
import urllib.parse
import urllib.request

import ingest

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OPENALEX = "https://api.openalex.org/works"

# Deliberately a loose net -- fit_score in ingest.py does the real
# scope judgment once a candidate is actually fetched.
JOURNALS = [
    "Nature", "Science", "Cell", "Nat Biomed Eng", "Nat Comput Sci",
    "Nat Chem", "Nat Mater", "Nat Methods", "Nat Mach Intell",
]
AI_KEYWORDS = [
    "artificial intelligence", "machine learning", "deep learning",
    "neural network", "large language model", "generative model",
    "foundation model", "agentic",
]
EXCLUDED_TYPES = ["Review", "Editorial", "Comment", "News"]

# OpenAlex Source IDs for the same journal list, resolved once via
# https://api.openalex.org/sources?search=<name> -- OpenAlex has no
# "search by journal name" filter on /works itself, so these need to be
# looked up ahead of time rather than passed as names.
OPENALEX_SOURCE_IDS = {
    "Nature": "S137773608",
    "Science": "S3880285",
    "Cell": "S110447773",
    "Nat Biomed Eng": "S2764624792",
    "Nat Comput Sci": "S4210228084",
    "Nat Chem": "S202193212",
    "Nat Mater": "S103895331",
    "Nat Methods": "S127827428",
    "Nat Mach Intell": "S2912241403",
}
OPENALEX_EXCLUDED_TYPES = ["review", "editorial", "book-review", "letter"]


def _build_term() -> str:
    journals = " OR ".join(f'"{j}"[Journal]' for j in JOURNALS)
    keywords = " OR ".join(f'"{k}"[Title/Abstract]' for k in AI_KEYWORDS)
    excluded = " OR ".join(f"{t}[Publication Type]" for t in EXCLUDED_TYPES)
    return f"({journals}) AND ({keywords}) NOT ({excluded})"


def _get(path: str, params: dict) -> dict:
    params = {**params, "tool": "ai4science-catalogue", "retmode": "json"}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    url = f"{EUTILS}/{path}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=20) as resp:
        return json.loads(resp.read())


def _doi_from_summary(summary: dict) -> str | None:
    for aid in summary.get("articleids", []):
        if aid.get("idtype") == "doi" and aid.get("value"):
            return aid["value"]
    return None


def search_pubmed(days: int = 7, max_results: int = 40) -> list[dict]:
    """Return candidates: [{title, journal, pubdate, doi, url, pmid}, ...]."""
    search = _get("esearch.fcgi", {
        "db": "pubmed",
        "term": _build_term(),
        "datetype": "pdat",
        "reldate": days,
        "retmax": max_results,
    })
    pmids = search.get("esearchresult", {}).get("idlist", [])
    if not pmids:
        return []

    summaries = _get("esummary.fcgi", {"db": "pubmed", "id": ",".join(pmids)})
    result = summaries.get("result", {})

    candidates = []
    for pmid in pmids:
        summary = result.get(pmid)
        if not summary:
            continue
        doi = _doi_from_summary(summary)
        url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        candidates.append({
            "pmid": pmid,
            "title": summary.get("title", "").rstrip("."),
            "journal": summary.get("fulljournalname") or summary.get("source", ""),
            "pubdate": summary.get("pubdate", ""),
            "doi": doi,
            "url": url,
            "source": "pubmed",
        })
    return candidates


def search_openalex(days: int = 7, max_results: int = 40) -> list[dict]:
    """Return candidates: [{title, journal, pubdate, doi, url, source}, ...]."""
    today = datetime.date.today()
    from_date = today - datetime.timedelta(days=days)

    source_filter = "|".join(OPENALEX_SOURCE_IDS.values())
    keyword_filter = "|".join(urllib.parse.quote(k) for k in AI_KEYWORDS)
    type_filter = ",".join(f"type:!{t}" for t in OPENALEX_EXCLUDED_TYPES)
    filt = (
        f"primary_location.source.id:{source_filter}"
        f",from_publication_date:{from_date.isoformat()}"
        f",to_publication_date:{today.isoformat()}"
        f",title_and_abstract.search:{keyword_filter}"
        f",{type_filter}"
    )
    url = (
        f"{OPENALEX}?filter={filt}&per-page={max_results}"
        "&select=title,doi,publication_date,primary_location"
        "&mailto=ai4science-catalogue@example.invalid"
    )
    with urllib.request.urlopen(url, timeout=20) as resp:
        data = json.loads(resp.read())

    candidates = []
    for work in data.get("results", []):
        doi = (work.get("doi") or "").removeprefix("https://doi.org/") or None
        source = (work.get("primary_location") or {}).get("source") or {}
        candidates.append({
            "title": (work.get("title") or "").rstrip("."),
            "journal": source.get("display_name", ""),
            "pubdate": work.get("publication_date", ""),
            "doi": doi,
            "url": f"https://doi.org/{doi}" if doi else work.get("id", ""),
            "source": "openalex",
        })
    return candidates


def search_all(days: int = 7, max_results: int = 40) -> list[dict]:
    """Query PubMed and OpenAlex, merging and deduping by DOI/URL."""
    combined = search_pubmed(days=days, max_results=max_results)
    combined += search_openalex(days=days, max_results=max_results)

    seen_dois, seen_urls, deduped = set(), set(), []
    for c in combined:
        if c["doi"] and c["doi"] in seen_dois:
            continue
        if c["url"] in seen_urls:
            continue
        if c["doi"]:
            seen_dois.add(c["doi"])
        seen_urls.add(c["url"])
        deduped.append(c)
    return deduped


def filter_new(candidates: list[dict], data: dict) -> list[dict]:
    """Drop candidates already in the catalogue, matched by DOI or URL."""
    known_urls = ingest.existing_urls(data)
    known_dois = {
        e.get("doi") for cat in data["categories"] for e in cat["entries"] if e.get("doi")
    }
    return [
        c for c in candidates
        if c["url"] not in known_urls and (not c["doi"] or c["doi"] not in known_dois)
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--max", type=int, default=40)
    args = parser.parse_args()

    candidates = search_all(days=args.days, max_results=args.max)
    data = ingest.load_data()
    new_candidates = filter_new(candidates, data)

    print(f"{len(candidates)} matched, {len(new_candidates)} not already catalogued:", file=sys.stderr)
    for c in new_candidates:
        print(f"- [{c['source']}, {c['journal']}, {c['pubdate']}] {c['title']}\n  {c['url']}")


if __name__ == "__main__":
    main()
