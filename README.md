<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Source: data/domains.yaml | Regenerate: python scripts/build.py -->

# Awesome Biomedical AI Models

A curated catalogue of biomedical AI models and systems published in leading journals, with the architecture, pre-training recipe, training data and downstream tasks recorded for each one.

**98 models** across 9 domains.

## Browse by domain

| Domain | Scope | Models | Maintainer | NotebookLM |
| --- | --- | ---: | --- | --- |
| [Pathology](pathology.md) | Histopathology, whole-slide imaging and computational pathology | 15 | [Leo Yin](https://shuolinyin.com) ([GitHub](https://github.com/leoyin1127)) | — |
| [Radiology](radiology.md) | CT, MRI, PET, X-ray and fMRI | 28 | Judy Lyu, Sumin Kim | — |
| [Biomedical Images — Other](biomedical_images.md) | Ultrasound, microscopy, retinal imaging, OCT, dermatology, endoscopy and other imaging | 9 | Terry Fu, Zaiyou He | — |
| [Longitudinal Health Data](longitudinal.md) | Longitudinal EHR, physiological signals, wearables and temporal clinical records | 9 | Evan Su | — |
| [Multimodal AI](multimodal.md) | Cross-modal health models without a single dominant biomedical domain | 3 | Yeonwoo Seo | — |
| [AI Agents](AI_agent.md) | Agentic, autonomous and tool-using AI systems | 7 | Meng Wei, Lan Feng | — |
| [AI for Biology](AI4biology.md) | Genomics, transcriptomics, proteomics, omics and biological modeling | 16 | Keishi Suzuki | — |
| [Large Language Models](LLM.md) | Benchmarks of LLMs, medical language models and clinical NLP | 6 | Leo Chen | — |
| [AI for Science](AI4Science.md) | Scientific discovery, research assistance, chemistry and drug design | 5 | Ryan Khalloqi | — |

## Contributing

Entries live in `data/*.yaml` and the markdown pages are generated from them, so a pull request should edit the YAML rather than the tables. [CONTRIBUTING.md](CONTRIBUTING.md) covers the schema, how to pick a domain, and the one-command way to turn a paper link into an entry.

```bash
pip install -r requirements.txt
python scripts/build.py       # regenerate the markdown
python scripts/validate.py    # check the data before pushing
```

1 of 9 pages is on the structured format so far; the rest are still hand-maintained markdown and can migrate one at a time.
