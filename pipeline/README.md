# Catalogue pipeline

Domain pages generated from structured data instead of hand-edited tables.

Each domain has a `pipeline/<domain>/data.json` holding one record per paper, grouped into
categories. `generate.py` renders that into the domain's markdown page (summary table +
collapsible per-model detail with a "Key results" list). The rendered page carries a
`GENERATED FILE - DO NOT EDIT BY HAND` banner — edit the JSON and regenerate instead.

```bash
python3 pipeline/generate.py pipeline/ai4science/data.json AI4Science.md
```

`generate.py` has no third-party dependencies (stdlib `json` only), so it runs anywhere
without a pip install step — including inside a CI job.

Only quote numbers a fetched source actually states. Where a paper is paywalled or a figure
isn't reported, leave the field blank or add a `note` explaining what was checked, rather than
estimating.

## Ingesting a new paper

`ingest.py` automates the "paste a link, get a catalogue entry" step: it calls the Claude API
with the server-side `web_fetch` tool on the given URL, extracts a JSON entry against the same
schema `generate.py` reads (Claude also picks the category), inserts it into `data.json`, and
regenerates `AI4Science.md`.

```bash
export ANTHROPIC_API_KEY=...       # or another credential the SDK resolves automatically
pip install anthropic              # if not already installed
python3 pipeline/ingest.py https://www.nature.com/articles/...
```

Pass `--dry-run` to see the extracted JSON without writing anything. The script enforces the
same honesty rules used to build the catalogue by hand — a missing model size becomes an
explicit "N/A — <reason>", never a guess — and refuses MICCAI/IEEE-conference entries (flags
them in `note` instead of silently dropping them, so a human can double-check the call).

Always review the diff before committing — this fills in the tedious first draft, it doesn't
replace the manual read the mentor asked for.
