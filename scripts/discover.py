#!/usr/bin/env python3
"""Find biomedical AI papers published since last week that we do not have yet.

    python scripts/discover.py --days 7 --dry-run     # print to stdout
    python scripts/discover.py --days 7 --out out.md  # issue body for the bot

Design note: this proposes, it does not commit. Output is a checklist a
maintainer ticks. An auto-committing bot would quietly fill the catalogue with
near-misses, and the whole value of the list is that a human vouched for every
row.

Sources
  PubMed          the high-impact journal allowlist in data/vocab.yaml (default)
  bioRxiv/medRxiv opt-in via --include-preprints
  arXiv           opt-in via --include-arxiv

Preprints are off by default on purpose. A week of the journal allowlist is
~40 candidates; adding bioRxiv and medRxiv takes it past 170, and a checklist
that long is one nobody works through.

Only PyYAML is required; everything else is stdlib so CI stays fast.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.schema import (  # noqa: E402
    DATA_DIR,
    REPO_ROOT,
    Vocab,
    load_domain,
    load_domains,
    normalize_doi,
)

USER_AGENT = "AwesomeBiomedicalAI-discovery (+https://github.com/medfm-flare/AwesomeBiomedicalAI)"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5")


@dataclass
class Candidate:
    title: str
    url: str
    venue: str
    date: str
    source: str
    doi: str | None = None
    authors: list[str] = field(default_factory=list)
    abstract: str = ""
    domain: str | None = None
    rationale: str = ""

    def key(self) -> str:
        doi = normalize_doi(self.doi or self.url)
        if doi:
            return f"doi:{doi}"
        return "title:" + re.sub(r"[^a-z0-9]+", " ", self.title.lower()).strip()


# ---------------------------------------------------------------------------
# What we already have
# ---------------------------------------------------------------------------

DOI_IN_TEXT = re.compile(r"10\.\d{4,9}/[^\s)\]|<>\"']+")
NATURE_ARTICLE = re.compile(r"nature\.com/articles/([a-z0-9\-.]+)", re.I)


def known_keys() -> set[str]:
    """Every paper already in the repo -- structured YAML and legacy markdown.

    The legacy pages matter: without scanning them the first run would re-propose
    all ~80 papers that have not migrated yet.
    """
    keys: set[str] = set()

    for domain in load_domains():
        slug = domain["slug"]
        if (DATA_DIR / f"{slug}.yaml").exists():
            for entry in load_domain(slug):
                doi = normalize_doi(entry.get("doi") or entry.get("url"))
                if doi:
                    keys.add(f"doi:{doi}")
                title = re.sub(r"[^a-z0-9]+", " ", str(entry.get("title", "")).lower())
                keys.add("title:" + title.strip())
            continue

        page = REPO_ROOT / domain["file"]
        if not page.exists():
            continue
        text = page.read_text()
        for match in DOI_IN_TEXT.findall(text):
            doi = normalize_doi(match)
            if doi:
                keys.add(f"doi:{doi}")
        for match in NATURE_ARTICLE.findall(text):
            keys.add(f"doi:10.1038/{match.lower()}")
        # Markdown link labels double as titles in the legacy tables.
        for label in re.findall(r"\|\s*\d{6}\s*\|\s*\[([^\]]+)\]", text):
            keys.add("title:" + re.sub(r"[^a-z0-9]+", " ", label.lower()).strip())

    return keys


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def get(url: str, params: dict | None = None, retries: int = 3) -> bytes:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=45) as response:
                return response.read()
        except Exception as exc:  # noqa: BLE001 - any transport failure is retryable
            last = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"GET failed after {retries} attempts: {url}") from last


# ---------------------------------------------------------------------------
# PubMed
# ---------------------------------------------------------------------------

# These journals publish a lot of journalism and opinion alongside research, and
# it all matches an "artificial intelligence" keyword search. Excluding by
# publication type is deterministic and free, so do it here rather than paying a
# model to reject "How should India approach AI?" every week.
EXCLUDED_PUBLICATION_TYPES = [
    "news",
    "editorial",
    "comment",
    "newspaper article",
    "historical article",
    "biography",
    "retracted publication",
    "retraction of publication",
]


def build_pubmed_query(vocab: Vocab, since: date, until: date) -> str:
    journals = [
        meta["pubmed"]
        for meta in vocab.venues.values()
        if meta.get("high_impact") and meta.get("pubmed")
    ]
    journal_clause = " OR ".join(f'"{j}"[ta]' for j in journals)
    ai_terms = vocab.discovery_keywords.get("ai", [])
    ai_clause = " OR ".join(f'"{t}"[tiab]' for t in ai_terms)
    excluded = " OR ".join(f'"{t}"[pt]' for t in EXCLUDED_PUBLICATION_TYPES)
    window = f'("{since:%Y/%m/%d}"[dp] : "{until:%Y/%m/%d}"[dp])'
    return f"(({journal_clause}) AND ({ai_clause})) AND {window} NOT ({excluded})"


def fetch_pubmed(vocab: Vocab, since: date, until: date, limit: int = 200) -> list[Candidate]:
    query = build_pubmed_query(vocab, since, until)
    payload = json.loads(
        get(
            f"{EUTILS}/esearch.fcgi",
            {"db": "pubmed", "term": query, "retmax": limit, "retmode": "json"},
        )
    )
    ids = payload.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []

    out: list[Candidate] = []
    for chunk_start in range(0, len(ids), 100):
        chunk = ids[chunk_start : chunk_start + 100]
        root = ET.fromstring(
            get(
                f"{EUTILS}/efetch.fcgi",
                {"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"},
            )
        )
        for article in root.findall(".//PubmedArticle"):
            out.append(parse_pubmed_article(article, vocab))
        time.sleep(0.4)  # NCBI asks for <= 3 requests/second without a key
    return [c for c in out if c]


def _text(node, path: str, default: str = "") -> str:
    found = node.find(path)
    if found is None:
        return default
    return "".join(found.itertext()).strip()


def parse_pubmed_article(article, vocab: Vocab) -> Candidate | None:
    title = _text(article, ".//ArticleTitle")
    if not title:
        return None

    journal_abbrev = _text(article, ".//Journal/ISOAbbreviation") or _text(
        article, ".//Journal/Title"
    )
    venue = vocab.venue_by_pubmed(journal_abbrev) or journal_abbrev

    doi = None
    for node in article.findall(".//ArticleId"):
        if node.get("IdType") == "doi":
            doi = (node.text or "").strip()
            break

    pubmed_id = _text(article, ".//PMID")
    url = f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"

    year = _text(article, ".//PubDate/Year") or _text(article, ".//DateRevised/Year")
    month = _text(article, ".//PubDate/Month") or "01"
    months = {
        m: f"{i:02d}"
        for i, m in enumerate(
            "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), start=1
        )
    }
    month = months.get(month, month if month.isdigit() else "01").zfill(2)

    authors = []
    for node in article.findall(".//Author"):
        last = _text(node, "LastName")
        fore = _text(node, "ForeName")
        if last:
            authors.append(f"{fore} {last}".strip())

    return Candidate(
        title=re.sub(r"\s+", " ", title).strip().rstrip("."),
        url=url,
        venue=venue,
        date=f"{year}-{month}" if year else "",
        source="pubmed",
        doi=doi,
        authors=authors,
        abstract=_text(article, ".//Abstract"),
    )


# ---------------------------------------------------------------------------
# bioRxiv / medRxiv
# ---------------------------------------------------------------------------

def matches_topic(text: str, vocab: Vocab, strict: bool) -> bool:
    lowered = text.lower()
    keywords = vocab.discovery_keywords
    has_ai = any(t.lower() in lowered for t in keywords.get("ai", []))
    if not strict:
        return has_ai
    has_bio = any(t.lower() in lowered for t in keywords.get("biomedical", []))
    return has_ai and has_bio


def fetch_rxiv(
    server: str, vocab: Vocab, since: date, until: date, cap: int = 1500
) -> list[Candidate]:
    """Page through a preprint server's feed for the window.

    The API returns every preprint in the range, not just matching ones, so the
    cost is proportional to the window. At the weekly cadence this is a few
    hundred records; `cap` stops a long --days backfill from running for ever.
    """
    out: list[Candidate] = []
    cursor = 0
    while True:
        payload = json.loads(
            get(f"https://api.biorxiv.org/details/{server}/{since}/{until}/{cursor}")
        )
        items = payload.get("collection", [])
        if not items:
            break
        for item in items:
            haystack = f"{item.get('title', '')} {item.get('abstract', '')}"
            if not matches_topic(haystack, vocab, strict=True):
                continue
            posted = str(item.get("date", ""))
            authors = [a.strip() for a in str(item.get("authors", "")).split(";") if a.strip()]
            out.append(
                Candidate(
                    title=re.sub(r"\s+", " ", item.get("title", "")).strip(),
                    url=f"https://doi.org/{item['doi']}" if item.get("doi") else "",
                    venue="bioRxiv" if server == "biorxiv" else "medRxiv",
                    date=posted[:7],
                    source=server,
                    doi=item.get("doi"),
                    authors=authors,
                    abstract=item.get("abstract", ""),
                )
            )
        total = int(payload.get("messages", [{}])[0].get("total", 0) or 0)
        cursor += len(items)
        if cursor >= total or cursor >= cap:
            if cursor < total:
                print(
                    f"  {server}: stopped at {cursor}/{total} records (cap={cap}); "
                    "narrow --days or raise the cap to cover the rest",
                    file=sys.stderr,
                )
            break
        time.sleep(0.3)
    return out


# ---------------------------------------------------------------------------
# arXiv (opt-in)
# ---------------------------------------------------------------------------

ATOM = "{http://www.w3.org/2005/Atom}"


def fetch_arxiv(vocab: Vocab, since: date, until: date, limit: int = 150) -> list[Candidate]:
    query = (
        '(cat:cs.CV OR cat:cs.CL OR cat:cs.LG OR cat:q-bio.QM) '
        'AND (abs:"foundation model" OR abs:"large language model" OR abs:"vision-language")'
    )
    raw = get(
        "http://export.arxiv.org/api/query",
        {
            "search_query": query,
            "start": 0,
            "max_results": limit,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
    )
    root = ET.fromstring(raw)
    out: list[Candidate] = []
    for entry in root.findall(f"{ATOM}entry"):
        published = (entry.findtext(f"{ATOM}published") or "")[:10]
        if not published:
            continue
        posted = datetime.strptime(published, "%Y-%m-%d").date()
        if posted < since or posted > until:
            continue
        title = re.sub(r"\s+", " ", entry.findtext(f"{ATOM}title") or "").strip()
        summary = re.sub(r"\s+", " ", entry.findtext(f"{ATOM}summary") or "").strip()
        if not matches_topic(f"{title} {summary}", vocab, strict=True):
            continue
        out.append(
            Candidate(
                title=title,
                url=entry.findtext(f"{ATOM}id") or "",
                venue="arXiv",
                date=published[:7],
                source="arxiv",
                authors=[
                    (a.findtext(f"{ATOM}name") or "").strip()
                    for a in entry.findall(f"{ATOM}author")
                ],
                abstract=summary,
            )
        )
    return out


# ---------------------------------------------------------------------------
# Domain routing via Claude (optional)
# ---------------------------------------------------------------------------

def classify(candidates: list[Candidate], domains: list[dict]) -> None:
    """Ask Claude which page each candidate belongs on. No key -> leave unrouted."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key or not candidates:
        return

    catalogue = "\n".join(f"- {d['slug']}: {d['scope']}" for d in domains)
    listing = "\n".join(
        f"{i}. {c.title}\n   venue: {c.venue}\n   abstract: {c.abstract[:600]}"
        for i, c in enumerate(candidates)
    )
    prompt = (
        "You are triaging papers for a curated biomedical AI catalogue.\n\n"
        f"Pages:\n{catalogue}\n\n"
        "For each paper below, pick the single best page and give a one-sentence "
        "reason it does or does not belong in a curated high-impact list. If a "
        "paper is not a biomedical AI model, system or benchmark, set domain to "
        '"skip".\n\n'
        f"Papers:\n{listing}\n\n"
        'Reply with JSON only: {"results":[{"index":0,"domain":"pathology",'
        '"rationale":"..."}]}'
    )

    body = json.dumps(
        {
            "model": CLAUDE_MODEL,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}],
        }
    ).encode()
    request = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = json.load(response)
        text = "".join(block.get("text", "") for block in payload.get("content", []))
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return
        for row in json.loads(match.group(0)).get("results", []):
            index = row.get("index")
            if isinstance(index, int) and 0 <= index < len(candidates):
                candidates[index].domain = row.get("domain")
                candidates[index].rationale = row.get("rationale", "")
    except Exception as exc:  # noqa: BLE001 - classification is a nicety, not a gate
        print(f"note: classification skipped ({type(exc).__name__}: {exc})", file=sys.stderr)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def render_issue(
    candidates: list[Candidate], domains: list[dict], since: date, until: date, scanned: int
) -> str:
    by_slug = {d["slug"]: d for d in domains}
    maintainers = {
        d["slug"]: ", ".join(m.get("name", "") for m in d.get("maintainers") or [])
        for d in domains
    }

    lines = [
        f"Scan window **{since} → {until}**. "
        f"{scanned} results retrieved, {len(candidates)} not already in the catalogue.",
        "",
        "Tick the ones worth adding, then run the add-paper prompt on each link "
        "(`.claude/commands/add-paper.md`). Close this issue when triaged.",
        "",
    ]

    if not candidates:
        lines.append("Nothing new this week.")
        return "\n".join(lines)

    grouped: dict[str, list[Candidate]] = {}
    for candidate in candidates:
        grouped.setdefault(candidate.domain or "unrouted", []).append(candidate)

    order = [d["slug"] for d in domains] + ["unrouted", "skip"]
    for slug in sorted(grouped, key=lambda s: order.index(s) if s in order else 99):
        if slug == "skip":
            continue
        heading = by_slug.get(slug, {}).get("name", slug.replace("_", " ").title())
        owner = maintainers.get(slug)
        lines.append(f"### {heading}" + (f" — {owner}" if owner else ""))
        lines.append("")
        for candidate in grouped[slug]:
            authors = ""
            if candidate.authors:
                authors = candidate.authors[0]
                if len(candidate.authors) > 1:
                    authors += f" … {candidate.authors[-1]}"
            meta = " · ".join(x for x in (candidate.venue, candidate.date, authors) if x)
            lines.append(f"- [ ] [{candidate.title}]({candidate.url})")
            lines.append(f"      {meta}")
            if candidate.rationale:
                lines.append(f"      _{candidate.rationale}_")
        lines.append("")

    skipped = grouped.get("skip", [])
    if skipped:
        lines.append("<details><summary>")
        lines.append(f"{len(skipped)} result(s) judged out of scope</summary>")
        lines.append("")
        for candidate in skipped:
            lines.append(f"- [{candidate.title}]({candidate.url}) — {candidate.venue}")
        lines.append("")
        lines.append("</details>")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=7, help="how far back to scan")
    parser.add_argument("--out", type=Path, help="write the issue body here")
    parser.add_argument("--json", type=Path, help="also write raw candidates as JSON")
    parser.add_argument("--dry-run", action="store_true", help="print to stdout")
    parser.add_argument(
        "--include-preprints",
        action="store_true",
        help="also scan bioRxiv and medRxiv (high volume, lower precision)",
    )
    parser.add_argument("--include-arxiv", action="store_true", help="also scan arXiv")
    parser.add_argument(
        "--check-journals",
        action="store_true",
        help="verify every pubmed abbreviation in vocab.yaml resolves, then exit",
    )
    args = parser.parse_args()

    vocab = Vocab.load()
    domains = load_domains()

    if args.check_journals:
        bad = []
        for name, meta in vocab.venues.items():
            abbrev = meta.get("pubmed")
            if not abbrev:
                continue
            payload = json.loads(
                get(
                    f"{EUTILS}/esearch.fcgi",
                    {"db": "pubmed", "term": f'"{abbrev}"[ta]', "retmax": 0, "retmode": "json"},
                )
            )
            count = int(payload.get("esearchresult", {}).get("count", 0))
            status = "ok" if count else "NO MATCH"
            print(f"  {status:<8} {name:<24} -> {abbrev!r} ({count} records)")
            if not count:
                bad.append(name)
            time.sleep(0.4)
        if bad:
            print(f"\n{len(bad)} journal abbreviation(s) do not resolve: {', '.join(bad)}")
            return 1
        print("\nAll journal abbreviations resolve.")
        return 0

    until = datetime.now(timezone.utc).date()
    since = until - timedelta(days=args.days)

    sources: list[tuple[str, object]] = [
        ("pubmed", lambda: fetch_pubmed(vocab, since, until)),
    ]
    # Preprints are off by default. A week of bioRxiv + medRxiv is ~140 topic
    # matches against ~38 from the journal allowlist, and a 170-item checklist
    # is one nobody triages. Turn them on when you want breadth.
    if args.include_preprints:
        sources += [
            ("biorxiv", lambda: fetch_rxiv("biorxiv", vocab, since, until)),
            ("medrxiv", lambda: fetch_rxiv("medrxiv", vocab, since, until)),
        ]

    found: list[Candidate] = []
    for label, fn in sources:
        try:
            hits = fn()
            print(f"  {label}: {len(hits)} hit(s)", file=sys.stderr)
            found.extend(hits)
        except Exception as exc:  # noqa: BLE001 - one dead source must not kill the run
            print(f"  {label}: FAILED ({type(exc).__name__}: {exc})", file=sys.stderr)

    if args.include_arxiv:
        try:
            hits = fetch_arxiv(vocab, since, until)
            print(f"  arxiv: {len(hits)} hit(s)", file=sys.stderr)
            found.extend(hits)
        except Exception as exc:  # noqa: BLE001
            print(f"  arxiv: FAILED ({type(exc).__name__}: {exc})", file=sys.stderr)

    scanned = len(found)
    seen = known_keys()
    fresh: list[Candidate] = []
    for candidate in found:
        key = candidate.key()
        if key in seen:
            continue
        seen.add(key)
        fresh.append(candidate)

    print(f"  {scanned} scanned, {len(fresh)} new after dedup", file=sys.stderr)

    classify(fresh, domains)
    fresh = [c for c in fresh if c.domain != "skip"] + [c for c in fresh if c.domain == "skip"]

    body = render_issue(fresh, domains, since, until, scanned)

    if args.json:
        args.json.write_text(json.dumps([c.__dict__ for c in fresh], indent=2))
    if args.out:
        args.out.write_text(body)
        print(f"wrote {args.out}", file=sys.stderr)
    if args.dry_run or not args.out:
        print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
