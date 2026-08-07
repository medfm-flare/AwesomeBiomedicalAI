---
description: Turn a paper link into a catalogue entry (input, paper link; output, a PR-ready YAML record)
argument-hint: <doi, publisher URL, or arXiv id>
---

Add the paper at `$ARGUMENTS` to this catalogue.

This file is also the team's shared prompt. If you are not running inside Claude
Code, paste the whole thing into ChatGPT or Claude with the link substituted for
`$ARGUMENTS` — the steps are the same, you just run the commands yourself.

## 1. Get the bibliographic metadata from an API, never from memory

```bash
python scripts/fetch_meta.py "$ARGUMENTS" --added-by "<your name>"
```

That returns a YAML stub with date, title, venue, DOI and first/last author
already correct — they come from Crossref or arXiv, not from a model. Do not
retype or "correct" these fields. If the command errors, the link is probably
not a DOI or arXiv id; find the DOI first.

If it warns that the venue is unknown, add the venue to `data/vocab.yaml` with a
`short` (used for the NotebookLM filename) and, for a journal, its `pubmed`
abbreviation. Then re-run.

## 2. Check it is not already catalogued

```bash
grep -ri "<the doi>" data/ *.md
```

Skip the paper if it is already there. If the existing entry is worse than what
you are about to write, improve that entry instead of adding a second one.

## 3. Pick the domain page

One paper, one page. `data/domains.yaml` lists the scope of each. When a paper
spans several, use this order:

1. If it is built for one imaging modality, that modality's page wins
   (pathology, radiology, biomedical_images) — even if the model is multimodal.
2. Otherwise, if its primary data is longitudinal clinical records, longitudinal.
3. Otherwise, if its primary data is molecular/omics, AI4biology.
4. Otherwise, if it is mainly an agentic or tool-using system, AI_agent.
5. Otherwise, if it is mainly a language model or a text benchmark, LLM.
6. Otherwise, if it targets scientific discovery outside medicine, AI4Science.
7. Only if none of the above fits, multimodal.

Say which rule you applied, so the choice can be argued with.

## 4. Fill in the fields that need the paper read

Read the paper (and its supplementary) for these. Every one has a house rule:

- `model.name` — the name the authors give it. No name, use the method acronym.
- `params` — total parameter count, format `632M` / `4.6B`. **Leave it `null`
  unless the paper states it.** Do not infer a count from the backbone name, and
  do not copy a number from a different paper about the same architecture.
- `backbone` — architecture in one line.
- `pretraining` — terms from the `pretraining` list in `data/vocab.yaml`.
  `pretraining_detail` — the recipe in one or two sentences.
- `data.description` and `data.scale` — real integers from the paper. Use keys
  that say what was counted (`whole_slide_images`, `patients`, `image_text_pairs`).
  Drop the placeholder keys you do not need.
- `tasks` — terms from the `tasks` list. `tasks_detail` — the specifics.
- `modalities` — terms from the `modalities` list.
- `performance` — headline benchmark results, as
  `{benchmark, metric, value, note}`. **Only numbers you can point to in the
  paper.** An empty list is correct and expected; a wrong number is not. This
  field is the one most likely to be silently fabricated, so if you are working
  from an abstract alone, leave it empty and say so.
- `verify` — a list of anything you could not confirm. Prefer writing an honest
  `verify` note over filling a field with a plausible guess; the note renders on
  the page and CI reports it, so it will get fixed.

Scholar links for `authors.first.scholar` / `authors.last.scholar` are nice but
optional. Do not invent a profile URL — leave `null` if you cannot find one.

## 5. Write, build, validate

Add the record to `data/<domain>.yaml` in date order (newest first), then:

```bash
python scripts/build.py
python scripts/validate.py --report
```

`build.py` regenerates the markdown — never edit `.md` files directly, they are
overwritten. `validate.py` must print `OK`. Fix any error it reports; warnings
are acceptable if you note why.

If the domain page has no `data/<slug>.yaml` yet, it is still hand-maintained
markdown. Either migrate the page first, or append a row to the existing table
in the same column order and say that you did.

## 6. Report back

Show a compact summary: model name, venue, date, target page, the routing rule
you used, anything in `verify`, and whether `performance` is empty and why.
