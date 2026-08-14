# Longitudinal Health Data

Longitudinal EHR, physiological signals, wearables and temporal clinical records.

**Maintainer:** Evan Su ([GitHub](https://github.com/HACKERALERT))

**25 entries** · [Back to index](README.md)

**Jump to:** [EHR foundation models](#ehr-foundation-models) · [Disease risk, subtyping and survival](#disease-risk-subtyping-and-survival) · [Cardiac and physiological signals](#cardiac-and-physiological-signals) · [Wearables and continuous sensing](#wearables-and-continuous-sensing) · [Inpatient deterioration and critical care](#inpatient-deterioration-and-critical-care) · [Biological age clocks](#biological-age-clocks)

`—` in the model-size column means no parameter count was reported in the paper. `N/A` marks entries where a parameter count does not apply, such as Bayesian generative models and penalized regression clocks. Counts marked `computed` were reproduced from the cited official implementation or from the architecture the paper specifies; each record states exactly which components the figure covers.

| Date | Model | Venue | Data | Model size | Training data | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 202607 | [Oncoformer](#model-oncoformer-202607) | Cell | EHR, chest X-ray | — | 3.7M individuals, 17.7M visits | self-supervised reconstruction with domain-adversarial losses against cohort and missingness patterns, plus cross-modal alignment | pan-cancer diagnosis, 1-year cancer risk, tumor staging +3 |
| 202607 | [ALADYNOULLI](#model-aladynoulli-202607) | Nature | EHR, genetics | N/A | 683K individuals, 348 diseases | hierarchical Bayesian inference over diagnoses, age and 36 polygenic risk scores, with Gaussian-process time priors | 21 latent disease signatures, 1-/10-year risk, GWAS and rare-variant discovery +1 |
| 202607 | [RisQ](#model-risq-202607) | medRxiv | EHR, multimodal features | 0.51M (computed) | 488K participants, 3.8M diagnosis events | single-stage horizon-conditional multi-task supervision with 60% modality dropout, no self-supervised stage | multi-disease risk at 1/2/5/10-year horizons, survival, zero-shot ICD-chapter transfer +2 |
| 202607 | [LLM EHR encoders](#model-llm-ehr-encoders-202607) | npj Digit. Med. | EHR | 0.6B / 4B / 8B | 6.7K patients (EHRSHOT), 387K (UK Biobank) | none — frozen off-the-shelf LLM embeddings of codes serialized to natural language, with logistic-regression or gradient-boosting heads | 15 EHRSHOT tasks: operational outcomes, lab values, new diagnoses +1 |
| 202605 | [SurvivEHR](#model-survivehr-202605) | npj Digit. Med. | EHR | 22M | 7.6B events, ~23M patients | competing-risk time-to-next-event prediction over 263 outcomes (74 conditions, 81 drug classes, 108 tests) | next-event prediction, 5-year hypertension and CVD risk, multimorbidity progression |
| 202604 | [ECG-LFM](#model-ecg-lfm-202604) | Nat. Commun. | ECG | — | 11.6M ECGs, 2.0M individuals | wav2vec 2.0-style contrastive plus masked signal modeling with multi-segment contrastive loss | 8 CVD classifications, 8 cardiac functional phenotypes, individual identification +1 |
| 202604 | [Early-ADHD](#model-early-adhd-202604) | Nat. Ment. Health | EHR | 29.4K trainable | 720K pretraining, 140K fine-tuning patients | masked EHR-event modeling, then DoRA adaptation with a discrete time-to-event head | ADHD diagnosis and diagnosis timing, birth to age 9 |
| 202604 | [Young-onset T2D detection](#model-young-onset-t2d-202604) | Lancet Digit. Health | EHR, registries | — | 3.4M individuals | supervised end-to-end on registry event sequences across 0-24 month horizons, no pre-training | young-onset type 2 diabetes risk at 0-24 month horizons |
| 202604 | [APOLLO](#model-apollo-202604) | arXiv | EHR, multimodal | 266.1M (computed) | 7.2M patients, 25.3B events | masked event modeling at 0.3 mask ratio over 28 modalities, cross-entropy plus embedding regression | 322 frozen-embedding tasks: disease onset, progression, treatment response +3 |
| 202603 | [Sepsis trajectory ensemble](#model-sepsis-trajectory-202603) | npj Digit. Med. | vitals, labs | N/A | 47.9K patients | group-based trajectory modeling to derive labels, then a random forest, gradient boosting and deep learning ensemble | 3-class recovery trajectory, binary deterioration, deterioration timing |
| 202603 | [PANGEA-SMM](#model-pangea-smm-202603) | Nat. Med. | labs, clinical | N/A | 1,031 training / 1,313 validation patients | Cox regression on four time-varying biomarker trajectories (M-protein, sFLC ratio, creatinine, hemoglobin) | dynamic risk of smoldering-to-active myeloma progression |
| 202603 | [TRUE-HF](#model-true-hf-202603) | Nat. Med. | smartwatch | — | 217 patients | semi-supervised on linearly interpolated CPET labels, autoregressive with FiLM conditioning on clinical covariates | daily pVO2 estimation, early warning for unplanned healthcare use |
| 202602 | [AD/PD EHR subtyping](#model-ad-pd-subtyping-202602) | Nat. Aging | EHR | — | 159K CPRD, 7.4K UK Biobank patients | masked encounter modeling plus contrastive learning, then k-means at a 0.95 prediction-strength threshold | five reproducible subtypes each for Alzheimer's and Parkinson's disease |
| 202602 | [OMICmAge](#model-omicmage-202602) | Nat. Aging | EHR, multi-omics | N/A | 31.3K MGB Biobank, 3.5K MGB-ABC | elastic net over 990 CpGs and 40 epigenetic biomarker proxies, stacked on a Cox EMR clock | all-cause mortality, six incident and prevalent diseases, lifestyle associations |
| 202602 | [CSFM](#model-csfm-202602) | Nat. Mach. Intell. | ECG, PPG, text | 51M / 117M / 343M | ~1.7M individuals | MAE-style generative masking of 75% of ECG and 50% of text tokens, paired signals and reports | diagnosis, demographics, vital signs, ICU false alarms +1 |
| 202601 | [GluFormer](#model-gluformer-202601) | Nature | CGM | 135.3M (computed) | >10M measurements, 10.8K adults | autoregressive next-token prediction over a 461-token glucose vocabulary, 1,200-token context | CGM trajectory generation, HbA1c and glycaemic forecasting, 11-year risk stratification |
| 202601 | [SleepFM](#model-sleepfm-202601) | Nat. Med. | PSG | ~4.4M | ~585K hours, 65K+ participants | leave-one-out contrastive learning across heterogeneous PSG channel configurations | 130-condition risk from one night, sleep staging, age and sex estimation |
| 202511 | [1dViT](#model-1dvit-202511) | NEJM AI | ECG | 92.7M | 800K unlabeled ECGs | masked signal modeling at 60% mask ratio, then fine-tuning on PET-derived and report labels | 12 tasks: LVEF, myocardial flow reserve, blood flow, perfusion deficit |
| 202511 | [Wearable deterioration model](#model-wearable-deterioration-202511) | Nat. Commun. | continuous vitals | — | 888 patients, 2,897 patient-days | supervised LSTM on 9 continuous vital and demographic inputs, 5-fold patient-level CV with class rebalancing | MEWS clinical-alert prediction, 24-hour adverse outcomes |
| 202510 | [LifeClock](#model-lifeclock-202510) | Nat. Med. | EHR | — | 24.6M visits, 9.7M individuals | mask reconstruction plus cohort discrimination, missing-data discrimination and next-visit prediction | biological age across the lifespan, age gap, current and future disease risk |
| 202510 | [PpgAge](#model-ppgage-202510) | Nat. Commun. | PPG | — | 20.0M segments, 172K participants | contrastive pretraining on unlabeled wrist PPG, then a ridge-penalized linear age head | chronological age, ASCVD and cardiometabolic risk, behavior associations |
| 202510 | [DT-GPT](#model-dt-gpt-202510) | npj Digit. Med. | EHR, text | 7B | 16.5K NSCLC, 35.1K ICU, 1.1K ADNI patients | BioMistral biomedical pretraining, then supervised fine-tuning on text-serialized trajectories with no imputation | multivariate trajectory forecasting, zero-shot unseen variables, chatbot interpretability |
| 202509 | [Delphi-2M](#model-delphi-2m-202509) | Nature | EHR | 2.2M | 0.4M UK Biobank participants | autoregressive generative modeling of disease-event sequences with continuous age encoding | rates for >1,000 diseases, 20-year synthetic trajectories, comorbidity structure +1 |
| 202506 | [ECGFounder](#model-ecgfounder-202506) | NEJM AI | ECG | 76.3M | 10.8M ECGs, 1.8M subjects | large-scale supervised pretraining on 150 cardiologist-annotated diagnostic labels | 150-way diagnosis, single- and reduced-lead ECG, demographics, wearable ECG +2 |
| 202506 | [TRisk](#model-trisk-202506) | Lancet Digit. Health | EHR | — | 3M adults | no separate pre-training stage; supervised survival training over variable-length EHR sequences, then transfer-learned and fine-tuned for the diabetes cohort | 10-year CVD risk in primary prevention and diabetes, treatment-eligibility triage |

## Details

Click a model to expand its record.

### EHR foundation models

<a id="model-oncoformer-202607"></a>
<details>
<summary><b>Oncoformer</b> — Advancing cancer detection and treatment using longitudinal routine clinical data <i>(Cell 2026-07)</i></summary>

**[Advancing cancer detection and treatment using longitudinal routine clinical data](https://doi.org/10.1016/j.cell.2026.07.009)**

*Cell* · 2026-07 · Fei Liu & Kang Zhang · [doi:10.1016/j.cell.2026.07.009](https://doi.org/10.1016/j.cell.2026.07.009)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Unified multimodal transformer; 24-layer examination encoder (d=1024) and 12-layer temporal decoder (d=768). Visit-level encoding uses a BERT-style transformer encoder; chest X-rays are embedded with a DINOv2-pretrained Vision Transformer backbone. |
| **Pre-training** | `self-supervised`, `reconstruction`, `domain-adversarial`, `cross-modal alignment`<br>Self-supervised reconstruction with a VAE regularization term, combined with domain-adversarial losses against cohort-specific and missingness patterns to promote cohort-invariant and missing-invariant representations, plus a cross-modal alignment term between tabular and image latents. |
| **Training data** | COMPASS cohort, with external validation on UK Biobank<br>**3,672,989** individuals · **17,748,334** clinical visits · **502,665** UK Biobank participants |
| **Downstream tasks** | `diagnosis`, `risk prediction`, `staging`, `treatment response`, `survival prediction`, `patient clustering`<br>Pan-cancer diagnosis, future cancer prediction, tumor staging, treatment-response prediction, recurrence-free survival prediction and patient clustering. |
| **Modalities** | `EHR`, `laboratory tests`, `chest X-ray`, `longitudinal clinical records` |
| **Code** | [github.com/kaiwang13/Oncoformer](https://github.com/kaiwang13/Oncoformer) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Pan-cancer diagnosis | AUROC | 0.956 | |
| Cancer prediction up to 1 year before diagnosis | AUROC | 0.869 | |
| Tumor staging | mean AUROC | >0.90 | |

</details>

<a id="model-risq-202607"></a>
<details>
<summary><b>RisQ</b> — Learning the shared structure of human health across diseases, modalities, and time <i>(medRxiv 2026-07)</i></summary>

**[Learning the shared structure of human health across diseases, modalities, and time](https://www.medrxiv.org/content/10.64898/2026.07.07.26357373v1)**

*medRxiv* · 2026-07 · [Paul Hager](https://scholar.google.com/citations?user=ESLUtGAAAAAJ) & [Francesco Paolo Casale](https://scholar.google.com/citations?user=AUFp6j4AAAAJ)

| | |
| --- | --- |
| **Parameters** | Not stated in the paper. **507,713 trainable parameters (0.51M)** for the published `hidden_dim=64` configuration, taken from the author-supplied count table in the official repository (`figures/scripts/supplementary/f_supp_scaling_val_loss.py`, `HIDDEN_DIM_TO_N_PARAMS`), whose stated conditions — RepQuery on UK Biobank variables at `icd_hierarchy_level=[3]` — match `configs/model/RepQuery.yaml`. |
| **Backbone** | Transformer encoder-decoder with FT-Transformer feature tokenizers, BioLORD concept embeddings and a cross-attention query decoder conditioned on disease and time horizon; 1-layer encoder and 1-layer decoder (d=64, 4 heads, 64 health tokens, 4,463 input features — 1,370 baseline plus 588 ICD and 2,505 medication features) |
| **Pre-training** | `horizon-conditional supervised`, `multi-task`<br>Single-stage horizon-conditional supervised multi-task training with modality dropout; no self-supervised stage. |
| **Training data** | UK Biobank, with external validation on All of Us without retraining<br>**488,170** participants · **3,813,248** diagnosis events · **3,658** structured and unstructured features spanning medications, biomarkers and physical measurements · **257,538** All of Us participants |
| **Downstream tasks** | `risk prediction`, `survival`, `zero-shot generalization`, `temporal extrapolation`, `genetic association`<br>Multi-disease risk at 1/2/5/10-year horizons, survival, zero-shot leave-one-ICD-chapter-out generalization, temporal extrapolation and exome-wide burden association. |
| **Modalities** | `EHR`, `biomarkers`, `medications`, `physical measurements`, `genetics` |
| **Code** | [github.com/RisQ-Lab/RisQ](https://github.com/RisQ-Lab/RisQ) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| UK Biobank, 1-year horizon | macro AUC | 0.791 | |
| UK Biobank, 10-year horizon | macro AUC | 0.760 | |
| UK Biobank survival | macro C-index | 0.760 | |
| All of Us, 1-year horizon, zero-shot | AUC | 0.703 | versus 0.535 for Delphi-2M |

</details>

<a id="model-llm-ehr-encoders-202607"></a>
<details>
<summary><b>LLM EHR encoders</b> — Large language models are powerful electronic health record encoders <i>(npj Digit. Med. 2026-07)</i></summary>

**[Large language models are powerful electronic health record encoders](https://www.nature.com/articles/s41746-026-02915-9)**

*npj Digit. Med.* · 2026-07 · [Stefan Hegselmann](https://scholar.google.com/citations?user=-lnWdScAAAAJ) & [Benjamin Wild](https://scholar.google.com/citations?user=_aIyvUkAAAAJ) · [doi:10.1038/s41746-026-02915-9](https://doi.org/10.1038/s41746-026-02915-9)

| | |
| --- | --- |
| **Parameters** | Qwen3-Embedding at 0.6B / 4B / 8B |
| **Backbone** | Decoder-only LLM embedding models — Qwen3-Embedding, Qwen2-Emb-7B and Llama3.1-LLM2Vec-8B — with logistic-regression heads |
| **Pre-training** | `off-the-shelf LLM embeddings`<br>No task-specific pre-training. Structured EHR codes are serialized into natural-language descriptions and embedded with general-purpose LLM encoders. |
| **Training data** | EHRSHOT and UK Biobank<br>**6,739** patients · **921,499** visits · **41,661,637** events (EHRSHOT) · **387,464** UK Biobank patients · **20,354,932** visits · **72,265,684** events. The processed UK Biobank subset used in the study is 387,464 patients, drawn from the full 502,489-participant cohort. |
| **Downstream tasks** | `operational outcomes`, `lab value prediction`, `new diagnoses`, `chest X-ray findings`<br>15 clinical prediction tasks spanning operational outcomes, lab value prediction, new diagnoses and chest X-ray findings. |
| **Modalities** | `EHR` |
| **Code** | [github.com/stefanhgm/ehrshot-benchmark](https://github.com/stefanhgm/ehrshot-benchmark) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| EHRSHOT, 15 tasks | mean AUROC | 0.769 | matches the specialized CLMBR-T-Base EHR foundation model at 0.769 |
| UK Biobank | AUROC | 0.751 | |

</details>

<a id="model-survivehr-202605"></a>
<details>
<summary><b>SurvivEHR</b> — A competing risks, time-to-event foundation model for multiple long-term conditions <i>(npj Digit. Med. 2026-05)</i></summary>

**[SurvivEHR: a competing risks, time-to-event foundation model for multiple long-term conditions from primary care electronic health records](https://www.nature.com/articles/s41746-026-02709-z)**

*npj Digit. Med.* · 2026-05 · [Charles Gadd](https://scholar.google.com/citations?user=oWUNs6AAAAAJ) & [Christopher Yau](https://scholar.google.com/citations?user=5tyrt68AAAAJ) · [doi:10.1038/s41746-026-02709-z](https://doi.org/10.1038/s41746-026-02709-z)

| | |
| --- | --- |
| **Parameters** | 22M; weights withheld for data privacy |
| **Backbone** | Decoder-only transformer with a neural competing-risks survival head (DeSurv); 384-d latent embeddings |
| **Pre-training** | `self-supervised`, `competing-risk time-to-event`<br>Self-supervised competing-risk, time-to-next-event objective over 263 competing outcomes: 74 long-term conditions, 81 medication classes and 108 test types. |
| **Training data** | CPRD Aurum, with a 90-5-5 split by practice site<br>**7,600,000,000** coded events · **~23,000,000** UK primary-care patients |
| **Downstream tasks** | `next-event prediction`, `risk prediction`, `multimorbidity progression`<br>Next-event prediction, 5-year incident hypertension, 5-year CVD under competing risks and multimorbidity progression from age 50. |
| **Modalities** | `EHR` |
| **Code** | [github.com/cwlgadd/SurvivEHR](https://github.com/cwlgadd/SurvivEHR) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Pre-training test set | inter-event concordance | 0.994 | |
| Downstream prognostic tasks | comparison against standard survival baselines | improves over baselines | largest gains in low-resource settings |

</details>

<a id="model-apollo-202604"></a>
<details>
<summary><b>APOLLO</b> — A multimodal and temporal foundation model for virtual patient representations <i>(arXiv 2026-04)</i></summary>

**[A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/abs/2604.18570)**

*arXiv* · 2026-04 · [Andrew Zhang](https://scholar.google.com/citations?user=WDiKxmcAAAAJ) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ) · [arXiv:2604.18570](https://arxiv.org/abs/2604.18570)

| | |
| --- | --- |
| **Parameters** | Not reported in the paper. **266,125,824 (266.1M), computed** for the transformer trunk: the 235,768 x 768 structured embedding table (181,069,824) plus 12 transformer blocks at E=768, 12 heads and a 4E-width MLP (85,054,464) and the final LayerNorm. Decoder weights for discrete vocabularies are tied to the input embeddings, so the output head adds no weights. Excludes the learnable time encoding, per-modality mask vectors, the projectors onto the 28 frozen unimodal encoders and the unstructured regression head. |
| **Backbone** | Transformer encoder-decoder over a single time-ordered heterogeneous event sequence, with learnable time encoding replacing positional embeddings and modality-specific adapters (GatorTron for text, vision foundation models for images); 12 layers, 12 heads, d=768, 1,536-event context, 235,768-token structured vocabulary |
| **Pre-training** | `masked event modeling`<br>Masked event and token modeling at a 0.3 mask ratio with modality-specific mask tokens; cross-entropy for structured tokens and embedding regression for unstructured inputs. |
| **Training data** | MGB-7M — Mass General Brigham records over 33 years spanning 28 modalities, with a held-out test set of 1.4 million patients<br>**7,155,044** patients · **25,296,943,893** medical events |
| **Downstream tasks** | `disease onset`, `disease progression`, `treatment response`, `adverse events`, `hospital operations`, `retrieval`<br>322 tasks via frozen embeddings — new disease onset (95), disease progression (78), treatment response (59), adverse events (17), hospital operations (12) and 61 retrieval cohorts. |
| **Modalities** | `EHR`, `text`, `images`, `28 modalities` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 1-year all-cause mortality | AUROC | 0.92 | |
| 30 cancer-progression tasks | mean AUROC | 0.735 | versus 0.626 for a task-specific supervised transformer |
| 95 disease-onset tasks | tasks beating the age-sex baseline | 74 of 95 | |

</details>

<a id="model-dt-gpt-202510"></a>
<details>
<summary><b>DT-GPT</b> — Large language models forecast patient health trajectories enabling digital twins <i>(npj Digit. Med. 2025-10)</i></summary>

**[Large language models forecast patient health trajectories enabling digital twins](https://www.nature.com/articles/s41746-025-02004-3)**

*npj Digit. Med.* · 2025-10 · Nikita Makarov & [Michael P. Menden](https://scholar.google.com/citations?user=jBejY7cAAAAJ) · [doi:10.1038/s41746-025-02004-3](https://doi.org/10.1038/s41746-025-02004-3)

| | |
| --- | --- |
| **Parameters** | 7B (BioMistral-7B) |
| **Backbone** | BioMistral-7B fine-tuned on text-serialized longitudinal clinical variables, with no imputation or normalization |
| **Pre-training** | `biomedical LLM pretraining`, `supervised fine-tuning`<br>BioMistral biomedical pretraining followed by supervised fine-tuning on clinical trajectories. |
| **Training data** | NSCLC Flatiron Health, MIMIC-IV ICU and ADNI Alzheimer's cohorts<br>**16,496** NSCLC patients · **35,131** ICU patients · **1,140** Alzheimer's patients |
| **Downstream tasks** | `trajectory forecasting`, `zero-shot forecasting`, `interpretability`<br>Multivariate clinical-variable trajectory forecasting, zero-shot forecasting of unseen variables and chatbot-based patient-level interpretability. |
| **Modalities** | `EHR`, `text` |
| **Code** | [github.com/MendenLab/DT-GPT](https://github.com/MendenLab/DT-GPT) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| NSCLC (Flatiron Health) | scaled MAE | 0.55 ± 0.04 | 3.4% reduction versus state-of-the-art baselines |
| MIMIC-IV ICU | scaled MAE | 0.59 ± 0.03 | 1.3% reduction versus state-of-the-art baselines |
| ADNI Alzheimer's | scaled MAE | 0.47 ± 0.03 | 1.8% reduction versus state-of-the-art baselines |

</details>

<a id="model-delphi-2m-202509"></a>
<details>
<summary><b>Delphi-2M</b> — Learning the natural history of human disease with generative transformers <i>(Nature 2025-09)</i></summary>

**[Learning the natural history of human disease with generative transformers](https://doi.org/10.1038/s41586-025-09529-3)**

*Nature* · 2025-09 · [Artem Shmatko](https://scholar.google.co.uk/citations?user=UXQl-IwAAAAJ&hl=en&oi=ao) & [Moritz Gerstung](https://scholar.google.co.uk/citations?user=MJWR0R0AAAAJ&hl=en&oi=ao) · [doi:10.1038/s41586-025-09529-3](https://doi.org/10.1038/s41586-025-09529-3)

| | |
| --- | --- |
| **Parameters** | 2.2M (12 layers, 12 heads, d=120) |
| **Backbone** | Modified GPT-2 transformer |
| **Pre-training** | `autoregressive generative`<br>Autoregressive generative modeling of disease-event sequences with continuous age encoding. |
| **Training data** | UK Biobank for training, with validation on Danish national data<br>**~400,000** UK Biobank participants · **1,900,000** Danish individuals (validation) |
| **Downstream tasks** | `rate prediction`, `trajectory generation`, `burden estimation`, `comorbidity structure`<br>Predict rates of more than 1,000 diseases, generate future health trajectories, estimate disease burden and interpret comorbidity structure. |
| **Modalities** | `EHR` |
| **Code** | [github.com/gerstung-lab/delphi](https://github.com/gerstung-lab/delphi) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| UK Biobank, >1,000 diseases | mean AUC | ~0.76 | |
| UK Biobank, death | AUC | 0.97 | |
| 1.9M Danish individuals, no retraining | mean AUC | 0.67 (s.d. 0.09) | |

</details>

### Disease risk, subtyping and survival

<a id="model-aladynoulli-202607"></a>
<details>
<summary><b>ALADYNOULLI</b> — A Bayesian framework for longitudinal EHR and genetic discovery <i>(Nature 2026-07)</i></summary>

**[A Bayesian framework for longitudinal EHR and genetic discovery](https://www.nature.com/articles/s41586-026-10780-5)**

*Nature* · 2026-07 · [Sarah M. Urbut](https://scholar.google.com/citations?user=iafjMbAAAAAJ) & [Giovanni Parmigiani](https://scholar.google.com/citations?user=OlpYP3UAAAAJ) · [doi:10.1038/s41586-026-10780-5](https://doi.org/10.1038/s41586-026-10780-5)

| | |
| --- | --- |
| **Parameters** | N/A — Bayesian generative model with K = 21 latent disease signatures |
| **Backbone** | Bayesian generative mixture model with Gaussian-process priors over time; 36 polygenic risk scores plus sex and 10 genetic PCs feed individual-specific signature loadings |
| **Pre-training** | `Bayesian inference`<br>N/A — hierarchical Bayesian inference jointly over longitudinal diagnoses, age and polygenic risk. |
| **Training data** | UK Biobank, Mass General Brigham and All of Us, with up to 52 years of follow-up<br>**427,239** UK Biobank · **48,069** Mass General Brigham · **208,263** All of Us · **>683,000** individuals · **348** diseases |
| **Downstream tasks** | `signature discovery`, `risk prediction`, `genetic discovery`, `patient stratification`<br>Latent time-varying disease-signature discovery, 1-year and 10-year risk prediction, common- and rare-variant genetic discovery and patient stratification. |
| **Modalities** | `EHR`, `genetics` |
| **Code** | [doi:10.5281/zenodo.20802505](https://doi.org/10.5281/zenodo.20802505) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 1-year ASCVD | AUC | 0.881 | |
| Cross-cohort signature preservation | median preservation | 80% | |
| Rare-variant analysis | genome-wide-significant loci | 151 loci, 18 unique genes | |

</details>

<a id="model-early-adhd-202604"></a>
<details>
<summary><b>Early-ADHD</b> — Early ADHD prediction from longitudinal electronic health records <i>(Nat. Ment. Health 2026-04)</i></summary>

**[Early attention deficit hyperactivity disorder prediction from longitudinal electronic health records](https://www.nature.com/articles/s44220-026-00628-2)**

*Nat. Ment. Health* · 2026-04 · Elliot D. Hill & Matthew Engelhard · [doi:10.1038/s44220-026-00628-2](https://doi.org/10.1038/s44220-026-00628-2)

| | |
| --- | --- |
| **Parameters** | Not reported for the full pretrained transformer; DoRA fine-tuning reduces trainable parameters to **29,440** |
| **Backbone** | Discrete time-to-event transformer with axial rotary positional embeddings encoding age, encounter position and continuous values; weight-decomposed low-rank adaptation (DoRA) applied to each linear layer for fine-tuning |
| **Pre-training** | `masked modeling`, `self-supervised`<br>Self-supervised masked-modeling pretraining on longitudinal EHR. |
| **Training data** | Pretraining corpus plus a pediatric fine-tuning cohort<br>**>720,000** pretraining patients · **>140,000** fine-tuning patients |
| **Downstream tasks** | `diagnosis`, `diagnosis timing`<br>ADHD diagnosis and diagnosis timing from birth to age 9. |
| **Modalities** | `EHR` |
| **Code** | [github.com/Elliot-D-Hill/early-adhd](https://github.com/Elliot-D-Hill/early-adhd) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| ADHD diagnosis by age 5, 4-year horizon | time-dependent AUROC | 0.92 | |

</details>

<a id="model-young-onset-t2d-202604"></a>
<details>
<summary><b>Young-onset T2D detection</b> — Deep learning across primary and secondary care <i>(Lancet Digit. Health 2026-04)</i></summary>

**[Detection of young-onset type 2 diabetes using deep learning across primary and secondary care: a nationwide, retrospective cohort study](https://doi.org/10.1016/j.landig.2025.100968)**

*Lancet Digit. Health* · 2026-04 · Christian Holm Johansen & [Søren Brunak](https://scholar.google.com/citations?user=eNqd5xEAAAAJ) · [doi:10.1016/j.landig.2025.100968](https://doi.org/10.1016/j.landig.2025.100968)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Deep learning over routine-care event sequences combining hospital diagnoses, primary-care prescriptions and primary-care service events across 0-24 month horizons |
| **Pre-training** | `supervised`<br>N/A — supervised. |
| **Training data** | Nationwide Danish registries, 1995-2018<br>**3,435,638** individuals · **16,828** developed young-onset type 2 diabetes (diagnosis before age 40) |
| **Downstream tasks** | `risk prediction`<br>Future young-onset type 2 diabetes risk at 0-24 month horizons. |
| **Modalities** | `EHR`, `national registries` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Onset 3-15 months after assessment | relative risk, top 0.1% risk stratum | 118.1 (95% CI 113.1-122.5) | |
| Onset 12-24 months after assessment | relative risk, top 0.1% risk stratum | 74.6 (71.2-78.2) | |

</details>

<a id="model-pangea-smm-202603"></a>
<details>
<summary><b>PANGEA-SMM</b> — Enhanced dynamic risk stratification of smoldering multiple myeloma <i>(Nat. Med. 2026-03)</i></summary>

**[Enhanced dynamic risk stratification of smoldering multiple myeloma](https://www.nature.com/articles/s41591-026-04304-x)**

*Nat. Med.* · 2026-03 · [Floris Chabrun](https://scholar.google.co.uk/citations?user=2bicZOwAAAAJ&hl=en&oi=ao) & Irene M. Ghobrial · [doi:10.1038/s41591-026-04304-x](https://doi.org/10.1038/s41591-026-04304-x)

| | |
| --- | --- |
| **Parameters** | N/A — Cox regression |
| **Backbone** | Multivariate Cox regression with time-varying covariates; bone-marrow and no-bone-marrow variants |
| **Pre-training** | `supervised`<br>N/A. |
| **Training data** | Dana-Farber Cancer Institute training cohort plus six international validation institutions<br>**1,031** training patients · **1,313** validation patients |
| **Downstream tasks** | `progression risk`<br>Predicting risk of progression from smoldering multiple myeloma (SMM) to active multiple myeloma (MM). |
| **Modalities** | `labs`, `clinical variables` |
| **Code** | [github.com/pangea-study/pangea_2.0](https://github.com/pangea-study/pangea_2.0) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Overall | C-statistic | 0.79 | |
| Validation cohort 1 | C-statistic | 0.84 (95% CI 0.79-0.88) | versus 0.76 for the 20/2/20 model |

</details>

<a id="model-ad-pd-subtyping-202602"></a>
<details>
<summary><b>AD/PD EHR subtyping</b> — Subtyping Alzheimer's and Parkinson's disease from longitudinal EHR <i>(Nat. Aging 2026-02)</i></summary>

**[Subtyping Alzheimer's disease and Parkinson's disease using longitudinal electronic health records](https://www.nature.com/articles/s43587-026-01085-3)**

*Nat. Aging* · 2026-02 · [Jie Lian](https://scholar.google.co.uk/citations?user=b_9BSxsAAAAJ&hl=en&oi=ao) & [Kazem Rahimi](https://scholar.google.co.uk/citations?user=5u7TxAMAAAAJ&hl=en&oi=ao) · [doi:10.1038/s43587-026-01085-3](https://doi.org/10.1038/s43587-026-01085-3)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Transformer encoder over sequential clinical events |
| **Pre-training** | `masked modeling`, `contrastive`<br>Masked encounters modeling and contrastive learning. |
| **Training data** | CPRD Aurum and UK Biobank cohorts for Alzheimer's disease (AD) and Parkinson's disease (PD)<br>**113,545** AD CPRD Aurum · **3,710** AD UK Biobank · **45,825** PD CPRD Aurum · **3,732** PD UK Biobank |
| **Downstream tasks** | `subtyping`, `clustering`<br>Subtyping and clustering of Alzheimer's disease and Parkinson's disease. |
| **Modalities** | `EHR` |
| **Code** | [github.com/SereneLian/Subtyping_EHR_AD_PD](https://github.com/SereneLian/Subtyping_EHR_AD_PD) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| AD and PD subtypes | reproducible subtypes | five per condition | prediction strength ≥0.95 |
| AD survival separation | log-rank P | 2.7 × 10⁻⁵⁰ | |
| PD survival separation | log-rank P | 2.1 × 10⁻²⁴ | |

</details>

<a id="model-trisk-202506"></a>
<details>
<summary><b>TRisk</b> — Transformer-based risk model for preventive cardiovascular treatment selection <i>(Lancet Digit. Health 2025-06)</i></summary>

**[Refined selection of individuals for preventive cardiovascular disease treatment with a transformer-based risk model](https://doi.org/10.1016/j.landig.2025.03.005)**

*Lancet Digit. Health* · 2025-06 · [Shishir Rao](https://scholar.google.com/citations?user=pQHoibsAAAAJ) & [Kazem Rahimi](https://scholar.google.co.uk/citations?user=5u7TxAMAAAAJ&hl=en&oi=ao) · [doi:10.1016/j.landig.2025.03.005](https://doi.org/10.1016/j.landig.2025.03.005)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Transformer over variable-length longitudinal EHR sequences with a survival head |
| **Pre-training** | Not specified |
| **Training data** | Open cohort of adults aged 25-84 with linked primary and secondary care EHR, 1998-2015<br>**3,000,000** adults · **291** English GP practices (development) · **98** practices (validation) |
| **Downstream tasks** | `risk prediction`, `treatment triage`<br>10-year CVD risk in the primary-prevention population and in diabetes cohorts, and treatment-eligibility triage. |
| **Modalities** | `EHR` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 10-year CVD risk | C-index | 0.910 (95% CI 0.906-0.913) | outperforms QRISK3 across age, sex and deprivation strata |
| Treatment-eligibility triage, 10% threshold | reduction in high-risk classifications | 20.6% fewer | |
| Treatment-eligibility triage, 15% threshold | reduction in high-risk classifications | 34.6% fewer | |

</details>

### Cardiac and physiological signals

<a id="model-ecg-lfm-202604"></a>
<details>
<summary><b>ECG-LFM</b> — Self-supervised ECG foundation model for CVD prediction and genetic discovery <i>(Nat. Commun. 2026-04)</i></summary>

**[A self-supervised electrocardiogram foundation model for empowering cardiovascular disease prediction and genetic factor discovery](https://www.nature.com/articles/s41467-026-72436-2)**

*Nat. Commun.* · 2026-04 · Siying Lin & [Huiying Zhao](https://scholar.google.com/citations?user=ei4g2_gAAAAJ) · [doi:10.1038/s41467-026-72436-2](https://doi.org/10.1038/s41467-026-72436-2)

| | |
| --- | --- |
| **Parameters** | Not reported; 1,024-d embeddings |
| **Backbone** | Convolutional feature encoder, Gumbel-softmax multi-codebook quantizer and Conformer context blocks, in the style of wav2vec 2.0 |
| **Pre-training** | `self-supervised`, `contrastive`, `masked modeling`, `multi-task`<br>Self-supervised multi-task learning combining contextual contrastive, masked-modeling and multi-segment contrastive losses. |
| **Training data** | Harvard-Emory ECG Database plus MIMIC-IV-ECG<br>**11,571,587** 12-lead ECGs · **1,979,599** individuals · **10,600,000** Harvard-Emory · **800,035** MIMIC-IV-ECG |
| **Downstream tasks** | `classification`, `phenotyping`, `identification`, `genetic discovery`<br>8 cardiovascular disease classifications, 8 cardiac functional phenotypes, individual identification and genetic factor discovery. |
| **Modalities** | `ECG` |
| **Code** | [github.com/biomed-AI/ECG-LFM](https://github.com/biomed-AI/ECG-LFM) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Across datasets | mean AUROC | 0.930 | |
| PTB-XL | AUROC | 0.951 | |
| Chapman | AUROC | 0.993 | |
| CPSC-2018 | AUROC | 0.971 | |
| CODE-15 | AUROC | 0.925 | |
| UK Biobank | AUROC | 0.807 | |

</details>

<a id="model-csfm-202602"></a>
<details>
<summary><b>CSFM</b> — Cardiac Sensing Foundation Model across scenarios and devices <i>(Nat. Mach. Intell. 2026-02)</i></summary>

**[Cardiac health assessment across scenarios and devices using a multimodal foundation model pretrained on data from 1.7 million individuals](https://www.nature.com/articles/s42256-026-01180-5)**

*Nat. Mach. Intell.* · 2026-02 · [Xiao Gu](https://scholar.google.com/citations?user=xpXBs0gAAAAJ) & [David A. Clifton](https://scholar.google.com/citations?user=mFN2KJ4AAAAJ) · [doi:10.1038/s42256-026-01180-5](https://doi.org/10.1038/s42256-026-01180-5)

| | |
| --- | --- |
| **Parameters** | Tiny 51M / Base 117M / Large 343M |
| **Backbone** | Vision Transformer variant in three sizes — CSFM-Tiny (6 encoder layers, hidden 1024, 8 attention heads), CSFM-Base (12 layers, hidden 3072, 12 heads) and CSFM-Large (16 layers, hidden 4096, 24 heads) |
| **Pre-training** | `generative masked pretraining`<br>MAE-style generative masked pretraining with 75% of ECG tokens and 50% of text tokens masked; multimodal ECG/PPG signals paired with clinical and machine-generated text reports. |
| **Training data** | MIMIC-III-WDB (USA), MIMIC-IV-ECG (USA) and CODE-Full (Brazil)<br>**~1,700,000** individuals |
| **Downstream tasks** | `diagnosis`, `demographic recognition`, `vital sign estimation`, `outcome prediction`, `question answering`<br>Cardiac disease diagnosis, demographic recognition, vital sign measurement, clinical outcome prediction and ECG question answering, evaluated on CinC17, PTB-XL, VTaC, CODE-15, SimBand and ECG-QA. |
| **Modalities** | `ECG`, `PPG`, `text` |
| **Code** | [github.com/guxiao0822/Cardiac-Sensing-FM](https://github.com/guxiao0822/Cardiac-Sensing-FM) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| CinC17 | macro-F1 | 0.677 (95% CI 0.656-0.699) | versus 0.634 baseline |
| CODE-15, 1-year mortality | AUC | 0.844 | versus 0.816 baseline |
| VTaC, ICU false-alarm prediction (ventricular tachyarrhythmia) | AUC | 0.967 | versus 0.931 baseline; AUC stays above 0.7 five minutes before an event |

</details>

<a id="model-1dvit-202511"></a>
<details>
<summary><b>1dViT</b> — Foundation transformer for ECG-based cardiac and coronary function assessment <i>(NEJM AI 2025-11)</i></summary>

**[A Foundation Transformer Model with Self-Supervised Learning for ECG-Based Assessment of Cardiac and Coronary Function](https://ai.nejm.org/doi/full/10.1056/AIoa2500164)**

*NEJM AI* · 2025-11 · Jonathan B. Moody & [Venkatesh L. Murthy](https://scholar.google.com/citations?user=nNET6osAAAAJ) · [doi:10.1056/AIoa2500164](https://doi.org/10.1056/AIoa2500164)

| | |
| --- | --- |
| **Parameters** | 92.7M trainable |
| **Backbone** | 1-D Vision Transformer with a patch-embedding layer for multichannel 1-D waveforms |
| **Pre-training** | `masked signal modeling`, `self-supervised`<br>Self-supervised masked signal modeling at a 60% masking ratio. |
| **Training data** | Pretraining on MIMIC-IV-ECG, fine-tuning on PET-derived labels and clinical reports, with generalization assessed across five further cohorts including PTB-XL, UK Biobank cardiac MRI and SPECT<br>**800,035** unlabeled ECGs · **3,126** PET-derived labels · **13,704** clinical reports |
| **Downstream tasks** | `regression`, `classification`, `cross-modality transfer`<br>12 clinical, demographic and traditional ECG tasks including LVEF, myocardial flow reserve, rest and stress myocardial blood flow and total perfusion deficit. |
| **Modalities** | `ECG` |
| **Code** | [github.com/4dm-labs/ecgflow](https://github.com/4dm-labs/ecgflow) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 12 internal tasks | AUROC range | 0.763-0.955 | 0.763 for impaired myocardial flow reserve <2, 0.955 for impaired LVEF <35% |
| External and cross-modality cohorts | AUROC range | 0.771-0.949 | |
| Self-supervised versus de novo supervised training | tasks improved | 11 of 12 | |

</details>

<a id="model-ecgfounder-202506"></a>
<details>
<summary><b>ECGFounder</b> — An electrocardiogram foundation model built on over 10 million recordings <i>(NEJM AI 2025-06)</i></summary>

**[An Electrocardiogram Foundation Model Built on over 10 Million Recordings](https://ai.nejm.org/doi/full/10.1056/AIoa2401033)**

*NEJM AI* · 2025-06 · Jun Li & [Shenda Hong](https://scholar.google.com/citations?user=K95az5UAAAAJ) · [doi:10.1056/AIoa2401033](https://doi.org/10.1056/AIoa2401033)

| | |
| --- | --- |
| **Parameters** | 76.3M; ablation variants at 11.7M / 25.6M / 110M |
| **Backbone** | 1-D RegNet self-regulated CNN with group convolutions, channel attention and skip connections |
| **Pre-training** | `supervised pretraining`<br>Large-scale supervised pretraining on 150 cardiologist-annotated diagnostic labels. |
| **Training data** | Harvard-Emory ECG Database<br>**10,771,552** ECGs · **1,818,247** subjects · **150** label categories |
| **Downstream tasks** | `diagnosis`, `demographics`, `event detection`, `reduced-lead ECG`, `cross-modality transfer`, `wearable ECG`<br>150-way diagnosis, single- and reduced-lead ECG, demographics, clinical-event detection, cross-modality rhythm diagnosis and wearable ECG. |
| **Modalities** | `ECG` |
| **Weights** | [huggingface.co/PKUDigitalHealth/ECGFounder](https://huggingface.co/PKUDigitalHealth/ECGFounder) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Internal 12-lead, 20 classifications | average AUROC | 0.968 (0.955-0.982) | AUROC exceeds 0.95 for 80 diagnoses |
| CODE-test (external) | AUROC | 0.981 (0.979-0.984) | |
| PTB-XL (external) | AUROC | 0.924 (0.917-0.931) | |
| Single-lead, normal sinus rhythm | AUROC | 0.975 (0.972-0.977) | |
| Single-lead, atrial fibrillation | AUROC | 0.957 (0.955-0.959) | |

</details>

### Wearables and continuous sensing

<a id="model-true-hf-202603"></a>
<details>
<summary><b>TRUE-HF</b> — Remote monitoring of heart failure exacerbations using a smartwatch <i>(Nat. Med. 2026-03)</i></summary>

**[Remote monitoring of heart failure exacerbations using a smartwatch](https://www.nature.com/articles/s41591-026-04247-3)**

*Nat. Med.* · 2026-03 · Yuan Gao & Heather J. Ross · [doi:10.1038/s41591-026-04247-3](https://doi.org/10.1038/s41591-026-04247-3)

| | |
| --- | --- |
| **Parameters** | Not reported; ~10 layers, d=512, 16 heads, deployed as a 10-model ensemble |
| **Backbone** | Autoregressive transformer with 1D-convolutional tokenization of HealthKit data at 90-1440 min resolutions, FiLM conditioning on clinical covariates and rotary embeddings |
| **Pre-training** | `semi-supervised`<br>Semi-supervised learning. |
| **Training data** | TRUE-HF study cohort, with external validation on an NIH All of Us Fitbit cohort<br>**217** patients with heart failure |
| **Downstream tasks** | `regression`, `early warning`<br>Predicting peak oxygen uptake (pVO2) and serving as an early warning signal for unplanned healthcare utilization from heart failure exacerbations. |
| **Modalities** | `smartwatch`, `clinical covariates` |
| **Code** | [github.com/mcintoshML/TRUEHF](https://github.com/mcintoshML/TRUEHF) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| pVO2 prediction | Pearson r | 0.85 | MAE 0.25 L/min |
| ≥10% pVO2 decline | AUROC | 0.82 (95% CI 0.69-0.92) | |
| Unplanned healthcare events | AUROC | 0.77 (0.62-0.90) | median lead time 7.4 days |

</details>

<a id="model-gluformer-202601"></a>
<details>
<summary><b>GluFormer</b> — A foundation model for continuous glucose monitoring data <i>(Nature 2026-01)</i></summary>

**[A foundation model for continuous glucose monitoring data](https://doi.org/10.1038/s41586-025-09925-9)**

*Nature* · 2026-01 · [Guy Lutsker](https://scholar.google.co.uk/citations?user=WBtGo0IAAAAJ&hl=en&oi=ao) & [Eran Segal](https://scholar.google.co.uk/citations?user=oAD8PrkAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41586-025-09925-9](https://doi.org/10.1038/s41586-025-09925-9)

| | |
| --- | --- |
| **Parameters** | Not reported in the paper. **135,341,516 (135.3M), computed** by instantiating the official `TransformerModel` from `train_model/train_GluFormer.py`: 16 `nn.TransformerEncoderLayer` blocks (d=1024, 16 heads, FFN 2048) contribute 134,397,952, the 461-row embedding table 472,064 and the untied 460-way output head 471,500. The sinusoidal positional encoding is a plain tensor, not a parameter, so it adds nothing. |
| **Backbone** | Autoregressive transformer |
| **Pre-training** | `autoregressive`, `self-supervised`<br>Self-supervised autoregressive next-token prediction. |
| **Training data** | Human Phenotype Project CGM data, validated on 19 external cohorts across 5 countries and 8 CGM devices<br>**>10,000,000** glucose measurements · **10,812** adults · **6,044** external participants |
| **Downstream tasks** | `trajectory generation`, `glycaemic prediction`, `risk stratification`, `multimodal extension`<br>Generate CGM trajectories, predict glycaemic measures such as HbA1c and fasting glucose plus long-term outcomes, risk stratification and multimodal extension with diet. |
| **Modalities** | `CGM`, `diet` |
| **Code** | [github.com/Guylu/GluFormer](https://github.com/Guylu/GluFormer) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Incident diabetes, top versus bottom risk quartile | share of cases | 66% versus 7% | 580 adults, 11-year median follow-up |
| Cardiovascular deaths, top versus bottom risk quartile | share of deaths | 69% versus 0% | 580 adults, 11-year median follow-up |

</details>

<a id="model-sleepfm-202601"></a>
<details>
<summary><b>SleepFM</b> — A multimodal sleep foundation model for disease prediction <i>(Nat. Med. 2026-01)</i></summary>

**[A multimodal sleep foundation model for disease prediction](https://www.nature.com/articles/s41591-025-04133-4)**

*Nat. Med.* · 2026-01 · [Rahul Thapa](https://scholar.google.co.uk/citations?user=H9FNWVcAAAAJ&hl=en&oi=ao) & [James Zou](https://scholar.google.co.uk/citations?user=23ZXZvEAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41591-025-04133-4](https://doi.org/10.1038/s41591-025-04133-4)

| | |
| --- | --- |
| **Parameters** | ~4.44M for pre-training; ~0.91M trainable for fine-tuning |
| **Backbone** | 1D CNN encoder (six conv layers, 128-d embeddings) with three transformer encoder layers and attention-based channel pooling; two LSTM layers for fine-tuning |
| **Pre-training** | `leave-one-out contrastive`<br>Leave-One-Out Contrastive Learning (LOO-CL). |
| **Training data** | Polysomnography recordings<br>**~585,000** hours of PSG · **>65,000** participants |
| **Downstream tasks** | `disease prediction`, `sleep staging`, `phenotype estimation`<br>Disease prediction, sleep stage classification and physiological and demographic estimation. |
| **Modalities** | `PSG` |
| **Code** | [github.com/zou-group/sleepfm-clinical](https://github.com/zou-group/sleepfm-clinical) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 130 conditions from a single night of PSG | C-index | ≥0.75 | |
| All-cause mortality | C-index | 0.84 | |
| Dementia | C-index | 0.85 | |
| Myocardial infarction | C-index | 0.81 | |

</details>

### Inpatient deterioration and critical care

<a id="model-sepsis-trajectory-202603"></a>
<details>
<summary><b>Sepsis trajectory ensemble</b> — Machine learning predicts sepsis deterioration trajectories <i>(npj Digit. Med. 2026-03)</i></summary>

**[Machine learning predicts sepsis deterioration trajectories](https://www.nature.com/articles/s41746-026-02565-x)**

*npj Digit. Med.* · 2026-03 · Rui Zhang & Hongping Qu · [doi:10.1038/s41746-026-02565-x](https://doi.org/10.1038/s41746-026-02565-x)

| | |
| --- | --- |
| **Parameters** | N/A — trajectory model plus ML ensemble |
| **Backbone** | Group-Based Trajectory Modeling for label derivation, combined with a random forest, gradient boosting and deep learning ensemble |
| **Pre-training** | `supervised`<br>N/A — supervised. |
| **Training data** | Ruijin Hospital development and internal validation cohorts plus external MIMIC-III and eICU<br>**2,843** development (2012-2019) · **1,213** internal validation (2020-2021) · **25,633** MIMIC-III · **18,247** eICU · **47,936** patients total |
| **Downstream tasks** | `trajectory classification`, `deterioration prediction`, `timing`<br>Three-class trajectory classification (rapid recovery, slow recovery, deterioration), binary deterioration and deterioration timing. |
| **Modalities** | `vitals`, `labs` |
| **Code** | [github.com/ccmzhangrui/sepsis-trajectory-python-data](https://github.com/ccmzhangrui/sepsis-trajectory-python-data) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Development cohort | AUROC | 0.92 | |
| Internal validation | AUROC | 0.89 | |
| MIMIC-III (external) | AUROC | 0.84 | |
| eICU (external) | AUROC | 0.77 | |
| Deterioration warning | median lead time | 17.6 h | before deterioration |

</details>

<a id="model-wearable-deterioration-202511"></a>
<details>
<summary><b>Wearable deterioration model</b> — Continuous in-hospital deterioration prediction from a clinical wearable <i>(Nat. Commun. 2025-11)</i></summary>

**[Development and validation of a clinical wearable deep learning based continuous inhospital deterioration prediction model](https://www.nature.com/articles/s41467-025-65219-8)**

*Nat. Commun.* · 2025-11 · Michael R. Scheid & [Theodoros P. Zanos](https://scholar.google.com/citations?user=mEJCPeMAAAAJ) · [doi:10.1038/s41467-025-65219-8](https://doi.org/10.1038/s41467-025-65219-8)

| | |
| --- | --- |
| **Parameters** | Not reported; LSTM recurrent network with 9 inputs |
| **Backbone** | Recurrent neural network with LSTM units over continuous vitals plus demographics |
| **Pre-training** | `supervised`<br>N/A — supervised, with 5-fold stratified patient-level cross-validation and class-balance resampling. |
| **Training data** | Non-ICU inpatients on VitalPatch biosensors at Northwell, Mar 2020-Nov 2022, plus prospective second-hospital and alternate-device external validation<br>**888** patients · **2,897** patient-days |
| **Downstream tasks** | `clinical alert prediction`, `deterioration prediction`<br>MEWS>6 clinical-alert prediction and 24-hour hard outcomes covering ICU transfer, rapid-response call, intubation, cardiac arrest and death. |
| **Modalities** | `continuous vitals`, `demographics` |
| **Code** | [codeocean.com/capsule/9888403](https://codeocean.com/capsule/9888403/tree) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Deterioration prediction | ROC-AUC | 0.89 ± 0.03 | PR-AUC 0.58 ± 0.14 |
| Intubations, cardiac arrests and deaths | detection rate | 100% | |
| Unplanned ICU transfers | detection rate | 83.6% | |
| Rapid-response calls | detection rate | 50% | lead time up to 17 h |

</details>

### Biological age clocks

<a id="model-omicmage-202602"></a>
<details>
<summary><b>OMICmAge</b> — Biological age from multi-omics integrated with electronic medical records <i>(Nat. Aging 2026-02)</i></summary>

**[OMICmAge quantifies biological age by integrating multi-omics with electronic medical records](https://www.nature.com/articles/s43587-026-01073-7)**

*Nat. Aging* · 2026-02 · [Qingwen Chen](https://scholar.google.com/citations?user=Djf7l7AAAAAJ) & [Jessica Lasky-Su](https://scholar.google.com/citations?user=MijM6lwAAAAJ) · [doi:10.1038/s43587-026-01073-7](https://doi.org/10.1038/s43587-026-01073-7)

| | |
| --- | --- |
| **Parameters** | N/A — penalized regression over 990 CpGs plus 40 epigenetic biomarker proxies and age; upstream EMRAge uses 19 clinical variables |
| **Backbone** | Elastic-net regression stacked on a Cox proportional-hazards EMR clock (EMRAge → DNAmEMRAge → OMICmAge) |
| **Pre-training** | `supervised elastic net`<br>N/A — supervised elastic net with 25-fold cross-validation for lambda selection. |
| **Training data** | MGB Biobank for EMRAge and MGB-ABC for the omics clocks, with validation in All of Us, TruDiagnostic Biobank and Generation Scotland<br>**31,264** MGB Biobank · **3,451** MGB-ABC · **10,769** All of Us · **14,213** TruDiagnostic · **18,672** Generation Scotland |
| **Downstream tasks** | `mortality prediction`, `incident disease`, `prevalent disease`, `lifestyle association`<br>All-cause mortality, incident and prevalent stroke, type 2 diabetes, COPD, depression, CVD and cancer, and lifestyle-factor associations. |
| **Modalities** | `EHR`, `DNA methylation`, `multi-omics` |
| **Code** | [github.com/LaskySuLab/OMICmAge](https://github.com/LaskySuLab/OMICmAge) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 5-year mortality | AUC | 0.892 | versus 0.838 for PCGrimAge and 0.772 for chronological age |
| 10-year mortality | AUC | 0.873 | versus 0.816 for PCGrimAge and 0.749 for chronological age |
| All-cause mortality | hazard ratio per s.d. | 11.31 | |

</details>

<a id="model-lifeclock-202510"></a>
<details>
<summary><b>LifeClock</b> — A full life cycle biological clock based on routine clinical data <i>(Nat. Med. 2025-10)</i></summary>

**[A full life cycle biological clock based on routine clinical data and its impact in health and diseases](https://doi.org/10.1038/s41591-025-04006-w)**

*Nat. Med.* · 2025-10 · Kai Wang & [Kang Zhang](https://scholar.google.co.uk/citations?user=cdzVY_QAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41591-025-04006-w](https://doi.org/10.1038/s41591-025-04006-w)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | EHRFormer time-series transformer; 24-layer examination encoder (d=1024) and 12-layer temporal decoder (d=768) |
| **Pre-training** | `self-supervised`<br>Self-supervised learning combining mask reconstruction, cohort discrimination, missing-data discrimination and next-visit prediction. |
| **Training data** | Longitudinal clinical visits, with external validation on UK Biobank<br>**24,633,025** clinical visits · **9,680,764** individuals |
| **Downstream tasks** | `biological age`, `age gap`, `disease risk`<br>Biological age prediction across the lifespan, age-gap estimation and current plus future disease risk prediction. |
| **Modalities** | `EHR` |
| **Code** | [github.com/kaiwang13/EHRFormer](https://github.com/kaiwang13/EHRFormer) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| UK Biobank biological age (external) | MAE | 4.14 | |
| Coronary artery disease | AUC | 0.98 | |
| Atrial fibrillation and hypertension | AUC | 0.95 | |
| Future disease prediction | AUC | ≥0.8 | |

</details>

<a id="model-ppgage-202510"></a>
<details>
<summary><b>PpgAge</b> — A wearable-based aging clock associates with disease and behavior <i>(Nat. Commun. 2025-10)</i></summary>

**[A wearable-based aging clock associates with disease and behavior](https://www.nature.com/articles/s41467-025-64275-4)**

*Nat. Commun.* · 2025-10 · [Andrew C. Miller](https://scholar.google.com/citations?user=X3RNgQMAAAAJ) & [Guillermo Sapiro](https://scholar.google.com/citations?user=ISRNX3gAAAAJ) · [doi:10.1038/s41467-025-64275-4](https://doi.org/10.1038/s41467-025-64275-4)

| | |
| --- | --- |
| **Parameters** | Not reported; 256-d embeddings from 60-second PPG segments |
| **Backbone** | Deep PPG encoder with a linear age-regression head |
| **Pre-training** | `self-supervised contrastive`<br>Self-supervised contrastive learning on unlabeled wearable PPG. |
| **Training data** | Apple Heart & Movement Study<br>**19,993,427** PPG segments · **172,318** pretraining participants · **6,728** healthy participants for the age head · **120,235** validation participants |
| **Downstream tasks** | `age regression`, `disease risk`, `behavior association`, `longitudinal change detection`<br>Chronological-age prediction, age-gap to disease risk for ASCVD, hypertension, diabetes and hyperlipidemia, behavior associations and longitudinal change detection. |
| **Modalities** | `PPG` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Chronological age, healthy participants | MAE | 2.42-2.45 years | |
| Chronological age, general population | MAE | 3.13-3.26 years | |
| ASCVD | hazard ratio per 6-year age gap | 1.464 (1.36-1.57) | |
| Hypertension | hazard ratio per 6-year age gap | 1.620 (1.51-1.74) | |

</details>
