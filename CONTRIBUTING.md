# Contributing

Entries live in `data/*.yaml`. The markdown pages are generated from them, so a
pull request edits YAML and never a `.md` file — anything you type into a
generated page is overwritten on the next build.

```bash
pip install -r requirements.txt
python scripts/build.py            # regenerate the markdown
python scripts/validate.py --report
```

## Adding a paper

```bash
python scripts/fetch_meta.py "10.1038/s41591-024-02857-3" --added-by "Your Name"
```

That prints a YAML stub with the bibliographic fields already filled from
Crossref (or arXiv). Paste it into the right `data/<domain>.yaml`, fill the
TODOs from the paper, then build and validate.

`.claude/commands/add-paper.md` is the same workflow written as a prompt: run
`/add-paper <link>` in Claude Code, or paste the file into ChatGPT with your
link. It exists so nine maintainers produce byte-identical records instead of
nine private conventions.

### Which page?

One paper, one page. When a paper spans several, apply the first rule that fits:

1. Built for one imaging modality → that modality's page (`pathology`,
   `radiology`, `biomedical_images`), even if the model itself is multimodal.
2. Primary data is longitudinal clinical records → `longitudinal`.
3. Primary data is molecular or omics → `AI4biology`.
4. Mainly an agentic or tool-using system → `AI_agent`.
5. Mainly a language model or text benchmark → `LLM`.
6. Scientific discovery outside medicine → `AI4Science`.
7. None of the above → `multimodal`.

Say which rule you used in the PR. The order is arguable — argue with it in an
issue rather than routing by feel.

## The schema

Required: `date`, `title`, `url`, `venue`, `model`.
Expected (a warning if missing): `doi`, `authors`, `backbone`, `data`, `tasks`,
`modalities`.

| Field | Notes |
| --- | --- |
| `date` | `YYYY-MM`. Publication month, not the month you added it. |
| `title` | As published. |
| `url` | Canonical publisher or preprint link. |
| `doi` | Bare DOI (`10.1038/...`), no `https://doi.org/` prefix. This is the dedup key — without it, dedup falls back to title matching, which is weaker. |
| `venue` | Must be in `data/vocab.yaml`. Add new ones there with a `short`. |
| `authors` | `first` and `last` only, each `{name, scholar}`. |
| `model` | `{name, repo, weights, license}`. Only `name` is required. |
| `params` | `632M`, `4.6B`. **Only if the paper states it** — see below. |
| `backbone` | One line of architecture. |
| `pretraining` | List, from the `pretraining` vocabulary. |
| `data.scale` | Integers, with keys naming what was counted. |
| `tasks` | List, from the `tasks` vocabulary. |
| `performance` | `[{benchmark, metric, value, note}]`. |
| `verify` | Free-text list of things you could not confirm. Renders on the page. |

The controlled vocabularies (`venues`, `tasks`, `modalities`, `pretraining`)
live in `data/vocab.yaml`. The validator rejects values outside them, which is
the point: nine people otherwise write "Nat Med", "Nat. Med." and "Nature
Medicine" for the same journal. If a term is genuinely missing, add it to the
vocabulary in the same PR.

### Two fields that are easy to get wrong

**`params`.** Leave it `null` unless the paper gives a number. A backbone name
is not a parameter count — "ViT-L" tells you the reference configuration, not
what these authors trained. Where an entry does carry an inferred count, it also
carries a `verify` note saying so.

**`performance`.** Only numbers you can point at in the paper. An empty list is
a fine answer and most entries currently have one. A wrong benchmark number in a
catalogue other people cite is worse than a missing one, and it is the field an
LLM is most likely to invent when it is working from an abstract.

When in doubt, write a `verify` note. It renders as a callout on the page and
`validate.py --report` lists every entry carrying one, so it becomes tracked
work instead of a silent hole.

## Migrating a page to the structured format

Pages convert one at a time — nothing is blocked on a big-bang cutover. A page
with a `data/<slug>.yaml` is generated; one without stays hand-maintained
markdown and the build only counts its rows for the README.

To migrate yours: create `data/<your-slug>.yaml`, move each table row across
using `scripts/fetch_meta.py` for the bibliographic half, then run the build.
The old markdown is overwritten on the first build, so check the generated page
before committing.

## Weekly discovery

`.github/workflows/weekly-discovery.yml` runs every Monday. It searches PubMed
across the high-impact journal allowlist in `data/vocab.yaml`, drops news and
editorials by publication type, drops anything already catalogued, and opens one
issue with a checklist grouped by domain page. A typical week is around 30
candidates.

bioRxiv, medRxiv and arXiv are off by default — they roughly quintuple the list
for a much lower hit rate. Turn them on per run from the Actions tab, or with
`--include-preprints` / `--include-arxiv` locally.

It proposes; it does not commit. Tick what is worth adding, then run the
add-paper pipeline on those links. The human gate is deliberate — a bot that
writes straight into the catalogue would fill it with near-misses, and the only
reason to trust this list is that someone vouched for every row.

Run it by hand from the Actions tab, or locally:

```bash
python scripts/discover.py --days 7 --dry-run
python scripts/discover.py --check-journals   # verify the PubMed abbreviations
```

`ANTHROPIC_API_KEY` in repo secrets is optional. With it, candidates arrive
grouped by domain with a one-line rationale; without it, they arrive unrouted
and the scan still works.

## PDFs and NotebookLM

Do not commit publisher PDFs to this repository, supplementary files included.
Most are under publisher copyright and this repo is public. Keep the PDFs in the
NotebookLM notebook or shared drive, and link the notebook from the README
column.

The PDF naming convention is generated, not typed — `build.py` derives
`202607-NatMed-PRISM2.pdf` from an entry's `date`, `venue` and `model.name`, and
prints it on the detail block. Use what the page shows.
