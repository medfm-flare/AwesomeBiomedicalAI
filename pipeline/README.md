# Catalogue pipeline

Domain pages generated from structured data instead of hand-edited tables.

Each domain has a `pipeline/<domain>/data.json` holding one record per paper, grouped into
categories. `generate.py` renders that into the domain's markdown page (summary table +
collapsible per-model detail with a "Key results" list). The rendered page carries a
`GENERATED FILE - DO NOT EDIT BY HAND` banner — edit the JSON and regenerate instead.

```bash
python3 pipeline/generate.py pipeline/ai4science/data.json AI4Science.md
```

No third-party dependencies (stdlib `json` only), so it runs anywhere without a pip install
step — including inside a CI job.

Only quote numbers a fetched source actually states. Where a paper is paywalled or a figure
isn't reported, leave the field blank or add a `note` explaining what was checked, rather than
estimating.
