#!/usr/bin/env python3
"""Ingest one paper into pipeline/ai4science/data.json via the Claude API.

Fetches a paper URL with the server-side web_fetch tool, extracts a
catalogue entry matching the existing schema (Claude picks the category
itself, from drug-design / materials-science / research-agents), and
inserts it. Regenerates AI4Science.md afterwards.

Usage:
    python3 pipeline/ingest.py <paper_url> [--model claude-sonnet-5] [--dry-run]

Requires ANTHROPIC_API_KEY (or another credential the SDK resolves
automatically) in the environment.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import anthropic

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "pipeline" / "ai4science" / "data.json"
MD_PATH = REPO_ROOT / "AI4Science.md"
GENERATE_SCRIPT = REPO_ROOT / "pipeline" / "generate.py"

CATEGORY_IDS = ["drug-design", "materials-science", "research-agents"]

ENTRY_SCHEMA = {
    "type": "object",
    "properties": {
        "fit_score": {
            "type": "integer",
            "description": (
                "An integer from 0 to 100. How well this paper fits THIS catalogue's own "
                "scope: AI for Science (scientific discovery, research assistance, "
                "chemistry, drug design). Judge only against that scope — the same paper "
                "being a good fit for another page elsewhere in the repo too is fine and "
                "not a reason to lower this score. "
                "90-100: squarely scientific discovery / research assistance / chemistry / "
                "drug design, in a high-impact venue. 60-89: reasonably in scope but "
                "somewhat mixed (e.g. partly clinical, partly discovery-oriented). 30-59: "
                "weak connection to this scope — mostly about something else with only "
                "tangential AI-for-science framing. 0-29: not this domain at all, or not "
                "high-impact-journal caliber."
            ),
        },
        "fit_rationale": {
            "type": "string",
            "description": "One or two sentences justifying fit_score, judged only against this page's own scope.",
        },
        "source_access": {
            "type": "string",
            "enum": ["full_text", "open_mirror", "press_release_only", "abstract_only"],
            "description": (
                "How much of the paper you could actually verify. full_text: read the "
                "paper itself (or a complete open preprint/HTML version). open_mirror: "
                "original was paywalled but you found and read a complete open version "
                "(arXiv/bioRxiv preprint, etc). press_release_only: original is "
                "paywalled and all you found was press/news coverage, not the paper. "
                "abstract_only: only the title/abstract were accessible anywhere."
            ),
        },
        "category": {
            "type": "string",
            "enum": CATEGORY_IDS,
            "description": "Which of the three existing categories this paper best fits.",
        },
        "id": {"type": "string", "description": "Short kebab-case slug, e.g. 'mattergen'."},
        "date": {"type": "string", "description": "Publication date as YYYYMM, e.g. '202604'."},
        "model": {"type": "string", "description": "The model/system name. If the paper names none, describe it briefly, e.g. 'AI-guided LNP design (unnamed in paper)'."},
        "title": {"type": "string"},
        "url": {"type": "string"},
        "doi": {"type": ["string", "null"]},
        "venue": {"type": "string", "description": "Short venue form, e.g. 'Nat. Biomed. Eng.', 'Nature', 'Cell'."},
        "authors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": ["string", "null"], "description": "Google Scholar / ORCID profile if findable, else null."},
                },
                "required": ["name", "url"],
                "additionalProperties": False,
            },
            "description": "First and last author only, matching the rest of the catalogue.",
        },
        "params": {
            "type": "string",
            "description": "Model size if the paper states one (e.g. '46.8M'). If not a single neural net or the size isn't published, say why instead of guessing, e.g. 'N/A — non-neural (symbolic regression)' or 'not stated (VAE+GRU)'.",
        },
        "backbone": {"type": "string", "description": "Specific architecture detail — real layer counts/dims when the paper states them, not just a category word."},
        "pretraining": {
            "type": "object",
            "properties": {
                "tags": {"type": "array", "items": {"type": "string"}},
                "text": {"type": "string"},
            },
            "required": ["tags", "text"],
            "additionalProperties": False,
        },
        "training_data": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "stat": {"type": ["string", "null"], "description": "A concrete number/count if stated, else null."},
            },
            "required": ["text", "stat"],
            "additionalProperties": False,
        },
        "downstream_tasks": {
            "type": "object",
            "properties": {
                "tags": {"type": "array", "items": {"type": "string"}},
                "text": {"type": "string"},
            },
            "required": ["tags", "text"],
            "additionalProperties": False,
        },
        "modalities": {"type": "array", "items": {"type": "string"}},
        "code": {"type": ["string", "null"]},
        "weights": {"type": ["string", "null"]},
        "license": {"type": ["string", "null"]},
        "open": {"type": "boolean", "description": "True if code and/or weights are publicly available."},
        "key_results": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Concrete, numeric findings quoted or closely paraphrased from the fetched source. Empty array if nothing is fetchable — never invent one.",
        },
        "note": {
            "type": ["string", "null"],
            "description": "Caveats: paywalled, numbers from a press release rather than the paper, disputed claims, etc. Null if nothing to flag.",
        },
        "headline": {
            "type": "string",
            "maxLength": 140,
            "description": "ONE short, specific, numeric-if-possible clause for the summary table (roughly 12-20 words) — not a generic category phrase, and not a full multi-clause sentence with caveats (those belong in 'note').",
        },
    },
    "required": [
        "fit_score", "fit_rationale", "source_access",
        "category", "id", "date", "model", "title", "url", "doi", "venue", "authors",
        "params", "backbone", "pretraining", "training_data", "downstream_tasks",
        "modalities", "code", "weights", "license", "open", "key_results", "note", "headline",
    ],
    "additionalProperties": False,
}

SYSTEM_PROMPT = """You extract structured catalogue entries for a curated list of \
high-impact biomedical/scientific AI papers ("AI for Science": scientific discovery, \
research assistance, chemistry and drug design).

Rules, non-negotiable:
- Fetch the given URL with web_fetch first. If it redirects to a login/paywall page, \
  use web_search to find a complete open version — the arXiv/bioRxiv/medRxiv preprint, \
  a university press office writeup, or a PMC/open-repository copy — then web_fetch \
  that. Search by title + author, not just the URL. Only fall back to press-release-only \
  coverage if no complete open text exists anywhere; set "source_access" honestly to \
  reflect whatever you actually ended up reading (see its schema description).
- Every number in "key_results", "headline", "training_data.stat", and "params" must \
  come from something you actually fetched. Never estimate, round from memory, or \
  reuse a number from a similar-sounding paper.
- If a field genuinely is not stated anywhere you could fetch, say so explicitly \
  (e.g. "not stated in the paper", "N/A — non-neural (symbolic regression)", \
  "N/A — base LLM undisclosed") rather than leaving it vague or guessing. A wrong \
  number in a catalogue other people cite is worse than an honest blank.
- Score "fit_score" and write "fit_rationale" honestly per their schema descriptions — \
  this gates whether the entry gets inserted automatically, so do not inflate it to \
  make the paper look like a better fit than it is. Judge fit only against this page's \
  own scope (scientific discovery, research assistance, chemistry, drug design); this \
  catalogue deliberately allows papers that also belong on another page in the repo, so \
  that overlap is not itself a reason to lower the score.
- "headline" is what a reader sees in the summary table before opening the record — \
  ONE short, concrete, numeric-if-possible clause (see its maxLength/description), not \
  a category label like "candidate screening" or "self-supervised", and not a full \
  sentence with caveats piled on (caveats go in "note").
- Pick the single best-fitting category from the three given. If none fits well, \
  still pick the closest and say so in "note" (and reflect it in a lower fit_score).
- venue should be the short form already used in this catalogue (e.g. "Nat. Biomed. \
  Eng.", "Nature", "Cell", "Nat. Comput. Sci."), not the full journal name.
- Do not include entries from MICCAI, IEEE conference venues, or similar conference \
  proceedings — this catalogue only tracks Nature/Cell/Science-family journals and \
  arXiv/bioRxiv/medRxiv preprints of that caliber. If the fetched paper turns out to \
  be from an excluded venue, still return the JSON but set "note" to say so plainly \
  and drop "fit_score" accordingly.
"""


def load_data() -> dict:
    return json.loads(DATA_PATH.read_text())


def existing_urls(data: dict) -> set[str]:
    return {e["url"] for cat in data["categories"] for e in cat["entries"]}


def _describe_tool_start(block) -> str | None:
    if block.type != "server_tool_use":
        return None
    if block.name == "web_search":
        return "Searching the web for an accessible copy..."
    if block.name == "web_fetch":
        return "Fetching a page..."
    return f"Calling {block.name}..."


def fetch_entry(url: str, model: str, on_progress=None) -> dict:
    """Fetch and extract a catalogue entry. on_progress(str), if given, is
    called with human-readable status lines as the agentic turn runs."""
    notify = on_progress or (lambda _msg: None)
    client = anthropic.Anthropic()
    messages = [{"role": "user", "content": f"Extract a catalogue entry for this paper: {url}"}]
    tools = [
        {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 6},
        {"type": "web_search_20260209", "name": "web_search", "max_uses": 4},
    ]
    output_config = {"format": {"type": "json_schema", "schema": ENTRY_SCHEMA}, "effort": "medium"}

    restarts, max_restarts = 0, 5
    response = None
    while True:
        # Streaming avoids request-timeout risk on a turn with several
        # server-tool (web_search/web_fetch) round-trips under the hood.
        with client.messages.stream(
            model=model,
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            tools=tools,
            output_config=output_config,
            messages=messages,
        ) as stream:
            block_types: dict[int, str] = {}
            for event in stream:
                if event.type == "content_block_start":
                    block_types[event.index] = event.content_block.type
                    message = _describe_tool_start(event.content_block)
                    if message:
                        notify(message)
                    elif event.content_block.type == "text":
                        notify("Writing the extracted entry...")
                elif event.type == "content_block_stop":
                    kind = block_types.get(event.index, "")
                    if kind in ("web_search_tool_result", "web_fetch_tool_result"):
                        notify(f"{kind.replace('_tool_result', '')} finished.")
            response = stream.get_final_message()
        if response.stop_reason == "refusal":
            detail = getattr(response, "stop_details", None)
            raise RuntimeError(f"Claude refused the request: {detail}")
        if response.stop_reason != "pause_turn":
            break
        restarts += 1
        if restarts > max_restarts:
            raise RuntimeError("giving up: turn still paused after max_restarts")
        notify("Turn paused mid-way (long tool chain) — resuming...")
        messages.append({"role": "assistant", "content": response.content})

    notify("Parsing the extracted entry...")
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)


WEAK_ACCESS = {"press_release_only", "abstract_only"}


def review_gate(entry: dict, fit_threshold: int) -> list[str]:
    """Return a list of reasons this entry needs a human/--force before insertion."""
    reasons = []
    if entry["fit_score"] < fit_threshold:
        reasons.append(f"fit_score {entry['fit_score']}/100 is below the threshold ({fit_threshold}): {entry['fit_rationale']}")
    if entry["source_access"] in WEAK_ACCESS:
        reasons.append(f"source_access is '{entry['source_access']}' — extraction may be thin or sourced from press coverage only, not the paper itself.")
    return reasons


def insert_entry(data: dict, entry: dict) -> str:
    category = entry.pop("category")
    cat = next((c for c in data["categories"] if c["id"] == category), None)
    if cat is None:
        raise ValueError(f"Unknown category '{category}', expected one of {CATEGORY_IDS}")
    if any(e["id"] == entry["id"] for e in cat["entries"]):
        raise ValueError(f"Entry id '{entry['id']}' already exists in category '{category}'")
    cat["entries"].append(entry)
    cat["entries"].sort(key=lambda e: e["date"], reverse=True)
    return category


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Paper URL to ingest")
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and print the entry, don't write files")
    parser.add_argument("--fit-threshold", type=int, default=60, help="Minimum fit_score (0-100) to insert without --force")
    parser.add_argument("--force", action="store_true", help="Insert even if the review gate flags a low fit_score or weak source_access")
    args = parser.parse_args()

    data = load_data()
    if args.url in existing_urls(data):
        print(f"Already in the catalogue: {args.url}", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching and extracting: {args.url}", file=sys.stderr)
    print("(can take a few minutes — web_search/web_fetch may run several rounds server-side)", file=sys.stderr)
    entry = fetch_entry(args.url, args.model, on_progress=lambda msg: print(f"  {msg}", file=sys.stderr))

    print(
        f"fit_score={entry['fit_score']}/100  source_access={entry['source_access']}  category={entry['category']}",
        file=sys.stderr,
    )
    print(json.dumps(entry, indent=2, ensure_ascii=False))

    gate_reasons = review_gate(entry, args.fit_threshold)
    if gate_reasons:
        print("\nReview gate flagged this entry:", file=sys.stderr)
        for reason in gate_reasons:
            print(f"  - {reason}", file=sys.stderr)

    if args.dry_run:
        return

    if gate_reasons and not args.force:
        print("Not inserted. Re-run with --force to insert anyway.", file=sys.stderr)
        sys.exit(2)

    category = insert_entry(data, dict(entry))
    DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"\nInserted into category '{category}'. Regenerating {MD_PATH.name}...", file=sys.stderr)
    subprocess.run([sys.executable, str(GENERATE_SCRIPT), str(DATA_PATH), str(MD_PATH)], check=True)
    print("Done. Review the diff before committing.", file=sys.stderr)


if __name__ == "__main__":
    main()
