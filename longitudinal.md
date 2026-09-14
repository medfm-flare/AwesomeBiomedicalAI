# Longitudinal Health Data

Longitudinal EHR, physiological signals, wearables, and temporal clinical records.

**Maintainer:** Evan Su ([GitHub](https://github.com/HACKERALERT))

**50 entries** · **Last reviewed: 2026-09-14** · [Back to index](README.md)

**Jump to:** [EHR models and patient representations](#ehr-models-and-patient-representations) · [Disease risk, subtyping, and survival](#disease-risk-subtyping-and-survival) · [Cardiac and physiological signals](#cardiac-and-physiological-signals) · [Wearables and continuous sensing](#wearables-and-continuous-sensing) · [Inpatient deterioration and critical care](#inpatient-deterioration-and-critical-care) · [Biological age clocks](#biological-age-clocks)

This catalogue includes reusable representations, temporal prediction models, and clinically evaluated systems. Selection follows the repository’s journal coverage, particularly Nature and its clinical/computational journals, npj Digital Medicine, NEJM AI, The Lancet Digital Health, and Cell. Selected preprints are explicitly marked. Dates use the journal’s first online publication month, or the preprint’s first posting month; this is a curated selection, not a systematic review.

**Reading the table:** Data scale distinguishes pretraining, development, evaluation, and study-wide cohorts where reported; patient, visit, and recording counts are not interchangeable. “Training” includes self-supervision, supervised fitting, and downstream adaptation. `—` means a parameter count was not verified in the cited sources; `N/A` denotes non-neural entries without a comparable parameter count. Partial, trainable-only, and computed counts identify their scope in the record. Metrics retain their original cohorts and definitions and should not be ranked across papers. Prospective prediction evaluation and trials of effects on patient outcomes are distinguished in the evidence notes.

| Date | Model | Venue | Modalities | Model size | Data scale | Training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 202609 | [Computable patient journeys](#model-computable-patient-journeys-202609) | Nat. Med. | EHR, clinical text | 4B open model; full system — | 100K tuning visits; 31.2K extraction patients | instruction tuning, distillation, verification | temporal patient graphs, GLP-1 treatment trajectories |
| 202609 | [MoChiFormer / MoChiAgent](#model-mochiformer-mochiagent-202609) | Nat. Med. | maternal and infant EHR | — | 1.46M development; 90.2K external participants | masked reconstruction, multitask adaptation | maternal and infant outcomes, transgenerational risk |
| 202609 | [ECG-CLIP](#model-ecg-clip-202609) | Lancet Digit. Health | ECG, clinical reports | — | >1.7M ECGs / 542K patients; >800K external ECGs | masked ECG reconstruction, ECG–text contrastive learning | cardiac diagnosis, AF, mortality, CKD, and diabetes risk |
| 202608 | [PULSE](#model-pulse-202608) | Nat. Comput. Sci. | longitudinal labs, omics, images, EHR | — | 7K training / 3K test in core UKB experiment | longitudinal reconstruction, variational, and adversarial losses | cross-modal imputation, disease risk, trajectory forecasting |
| 202608 | [oFM](#model-ofm-202608) | arXiv (preprint) | oncology EHR, pathology, DNA/RNA | 421M trained + 5.1B frozen | 1.67M total; 1.05M stage-I patients | episode reconstruction, future-state prediction | survival, response, exploratory treatment ranking |
| 202607 | [Oncoformer](#model-oncoformer-202607) | Cell | EHR, chest X-ray | — | 3.7M COMPASS individuals; 502.7K external UKB participants | multimodal reconstruction, domain-adversarial learning, alignment | pan-cancer diagnosis, 1-year cancer risk, tumor staging |
| 202607 | [ALADYNOULLI](#model-aladynoulli-202607) | Nature | EHR, genetics | N/A | 683K participants across three fitted cohorts | hierarchical Bayesian inference with temporal priors | 20 disease signatures + low-incidence state, risk, genetic discovery |
| 202607 | [RisQ](#model-risq-202607) | medRxiv (preprint) | EHR, multimodal features | 0.51M (official config) | 488K participants, 3.8M diagnosis events | horizon-conditioned multitask supervision with modality dropout | multi-disease risk at 1/2/5/10-year horizons, survival, zero-shot ICD-chapter transfer |
| 202607 | [LLM EHR encoders](#model-llm-ehr-encoders-202607) | npj Digit. Med. | EHR | 0.6B / 4B / 8B | 6.7K EHRSHOT / 387K UKB benchmark patients | frozen LLM embeddings with logistic-regression heads | 15 EHRSHOT tasks: operational outcomes, lab values, new diagnoses |
| 202607 | [ED-Foundation](#model-ed-foundation-202607) | npj Digit. Med. | clinical text, medical images | — | 166.8K SYSMH narratives + public multimodal corpora | masked multimodal modeling, contrastive alignment | emergency triage, prognosis, decision support |
| 202607 | [Transformer-DAPT](#model-transformer-dapt-202607) | npj Digit. Med. | EHR-derived clinical features | — | 29K development / 19.2K external patients | survival/classification supervision with triplet loss | 1–12-month ischemic and bleeding risk after PCI |
| 202606 | [ECG-SCD](#model-ecg-scd-202606) | Nature | ECG, linked outcomes | — | 262.6K training ECGs / 75.2K patients | supervised multitask residual CNN | sudden cardiac death risk, ECG morphology analysis |
| 202606 | [DeepHHF](#model-deephhf-202606) | npj Digit. Med. | 24-hour ECG | ~13M | 57.6K eligible recordings / 40.2K patients | supervised segment and temporal learning | five-year heart failure risk |
| 202606 | [ActiTect / RBDisco](#model-actitect-rbdisco-202606) | npj Digit. Med. | wrist actigraphy | N/A | 78 development participants; local and external tests | supervised gradient-boosted trees on harmonized features | REM sleep behavior disorder screening |
| 202606 | [FIRST-ICU](#model-first-icu-202606) | npj Digit. Med. | ICU physiology, interventions | 1.79M (discrete variant) | 23.9K development / 12.6K external ICU admissions | supervised graph and temporal intervention forecasting | seven intervention forecasts, risk stratification |
| 202606 | [Hypoglycemia LSTM](#model-hypoglycemia-lstm-202606) | npj Digit. Med. | EHR, glucose, medications, labs | — | 143.1K admissions across three hospitals | supervised temporal classification | 24-hour inpatient hypoglycemia risk, updated every four hours |
| 202605 | [SurvivEHR](#model-survivehr-202605) | npj Digit. Med. | EHR | 22M | 7.6B events, ~23M patients | competing-risk time-to-next-event prediction | next-event prediction, 5-year hypertension and CVD risk, multimorbidity progression |
| 202605 | [Dynamic VTE transformer](#model-dynamic-vte-transformer-202605) | npj Digit. Med. | EHR, labs, cancer treatment | — | 80.8K development / 9.8K external patients | supervised temporal risk learning | quarterly venous thromboembolism risk during cancer treatment |
| 202605 | [TCPM](#model-tcpm-202605) | Nat. Commun. | longitudinal physiology, treatments | — | four public and two private datasets | counterfactual representation learning, policy optimization | temporal treatment-response modeling, medication policies |
| 202605 | [GRU-DA](#model-gru-da-202605) | npj Digit. Med. | longitudinal EHR | — | 15.2K development cases with 1:10 matched controls | supervised recurrent risk prediction with missingness decay | dynamic Alzheimer’s and related dementia risk |
| 202604 | [ECG-LFM](#model-ecg-lfm-202604) | Nat. Commun. | ECG | — | 11.6M ECGs, 2.0M individuals | masked and contrastive signal modeling | 8 CVD classifications, 8 cardiac functional phenotypes, individual identification |
| 202604 | [Early-ADHD](#model-early-adhd-202604) | Nat. Ment. Health | EHR | 29.4K adaptation parameters | 721.9K pretraining; 142.3K fine-tuning cohort | masked event modeling, DoRA time-to-event adaptation | ADHD diagnosis and diagnosis timing, birth to age 9 |
| 202604 | [Young-onset T2D detection](#model-young-onset-t2d-202604) | Lancet Digit. Health | EHR, registries | — | 3.4M individuals | supervised registry-sequence learning | young-onset type 2 diabetes risk at 0-24 month horizons |
| 202604 | [APOLLO](#model-apollo-202604) | arXiv (preprint) | EHR, multimodal | 266.1M trunk (computed) | 7.2M-patient corpus, including 1.4M test patients | masked multimodal event modeling | 261 prognostic tasks + 61 retrieval cohorts |
| 202603 | [Sepsis trajectory ensemble](#model-sepsis-trajectory-202603) | npj Digit. Med. | vitals, labs | — | 2.8K development; 1.2K internal / 43.9K external validation | trajectory-derived labels, supervised ML ensemble | 3-class recovery trajectory, binary deterioration, deterioration timing |
| 202603 | [PANGEA-SMM](#model-pangea-smm-202603) | Nat. Med. | labs, clinical | N/A | 1,031 training / 1,313 validation patients | Cox regression on time-varying biomarkers | dynamic risk of smoldering-to-active myeloma progression |
| 202603 | [TRUE-HF](#model-true-hf-202603) | Nat. Med. | smartwatch | — | 217-patient study cohort | semi-supervised autoregression with clinical conditioning | daily pVO2 estimation, early warning for unplanned healthcare use |
| 202603 | [WEAR-ME / WFM](#model-wear-me-wfm-202603) | Nature | wearable signals, routine blood tests | — | 40M pretraining hours; 1,165 development participants | masked wearable pretraining, frozen embeddings + classifier | insulin resistance screening |
| 202602 | [AD/PD EHR subtyping](#model-ad-pd-subtyping-202602) | Nat. Aging | EHR | — | 159K CPRD / 7.4K UKB study cohorts | masked encounter modeling, contrastive learning, clustering | five reproducible subtypes each for Alzheimer's and Parkinson's disease |
| 202602 | [OMICmAge](#model-omicmage-202602) | Nat. Aging | EHR, multi-omics | N/A | 31.3K MGB Biobank / 3.5K MGB-ABC cohorts | elastic-net epigenetic clock with an upstream EHR survival clock | all-cause mortality, six incident and prevalent diseases, lifestyle associations |
| 202602 | [CSFM](#model-csfm-202602) | Nat. Mach. Intell. | ECG, PPG, text | 51M / 117M / 343M | ~1.7M individuals | masked generative signal–text modeling | diagnosis, demographics, vital signs, ICU false alarms |
| 202602 | [Brain Health Score](#model-brain-health-score-202602) | NEJM AI | sleep EEG | — | ~36K recordings / ~27K people across six cohorts | supervised multitask representation learning, score distillation | cognition, disease, mortality associations |
| 202601 | [GluFormer](#model-gluformer-202601) | Nature | CGM | 135.3M (computed) | >10M measurements, 10.8K adults | autoregressive next-glucose-token prediction | CGM trajectory generation, HbA1c and glycaemic forecasting, 11-year risk stratification |
| 202601 | [SleepFM](#model-sleepfm-202601) | Nat. Med. | PSG | ~4.4M | ~432K pretraining hours / ~48K participants | leave-one-out contrastive learning; frozen encoder + task heads | 130-condition risk from one night, sleep staging, age and sex estimation |
| 202601 | [SleepGPT](#model-sleepgpt-202601) | Nat. Commun. | multichannel PSG | — | 59.3K pretraining hours / 5.1K subjects | time–frequency contrastive learning, matching, masked reconstruction | sleep staging, pathology, signal generation, spindles |
| 202601 | [GaitDynamics](#model-gaitdynamics-202601) | Nat. Biomed. Eng. | motion trajectories, ground reaction forces | — | 169 training participants; 270 overall / 34.8 hours | diffusion denoising, supervised force refinement | gait generation, force estimation, missing-joint reconstruction |
| 202511 | [1dViT](#model-1dvit-202511) | NEJM AI | ECG | 92.7M | 800K unlabeled ECGs | masked ECG modeling, supervised PET/report adaptation | 12 tasks: LVEF, myocardial flow reserve, blood flow, perfusion deficit |
| 202511 | [Wearable deterioration model](#model-wearable-deterioration-202511) | Nat. Commun. | continuous vitals | — | 888-patient study cohort; 2,897 patient-days | supervised LSTM with patient-level cross-validation | MEWS clinical-alert prediction, 24-hour adverse outcomes |
| 202510 | [LifeClock](#model-lifeclock-202510) | Nat. Med. | EHR | — | 24.6M visits, 9.7M individuals | masked reconstruction, domain discrimination, next-visit prediction | biological age across the lifespan, age gap, current and future disease risk |
| 202510 | [PpgAge](#model-ppgage-202510) | Nat. Commun. | PPG | — | 20.0M segments, 172K participants | contrastive PPG pretraining, ridge-regression age head | chronological age, ASCVD and cardiometabolic risk, behavior associations |
| 202510 | [DT-GPT](#model-dt-gpt-202510) | npj Digit. Med. | EHR, text | 7B | 16.5K NSCLC / 35.1K ICU / 1.1K ADNI task cohorts | BioMistral pretraining, supervised trajectory adaptation | multivariate trajectory forecasting, zero-shot unseen variables, chatbot interpretability |
| 202509 | [Delphi-2M](#model-delphi-2m-202509) | Nature | EHR | 2.2M | 0.4M UK Biobank participants | autoregressive disease-event modeling with age encoding | rates for >1,000 diseases, 20-year synthetic trajectories, comorbidity structure |
| 202509 | [InfEHR](#model-infehr-202509) | Nat. Commun. | temporal EHR graphs | — | 8.1K neonatal patients; separate postoperative cohorts | self-supervised graph learning, semisupervised refinement | neonatal sepsis and postoperative AKI phenotyping |
| 202508 | [PatientEmbedding](#model-patientembedding-202508) | npj Digit. Med. | longitudinal EHR codes | — | 102.7K eMERGE patients / 1.05M patient-year events | code autoencoding, masked temporal modeling, patient-pair learning | disease onset, phenotyping, subtyping, and progression |
| 202507 | [EchoNext](#model-echonext-202507) | Nature | ECG, demographics, echo-derived labels | — | 796.8K training ECG–echo pairs / 149.8K patients | supervised multitask ECG learning | structural heart disease screening |
| 202506 | [ECGFounder](#model-ecgfounder-202506) | NEJM AI | ECG | 76.3M | 10.8M ECGs, 1.8M subjects | supervised ECG pretraining on 150 diagnostic labels | 150-way diagnosis, single- and reduced-lead ECG, demographics, wearable ECG |
| 202506 | [TRisk](#model-trisk-202506) | Lancet Digit. Health | EHR | — | 3M adults across development and validation | supervised EHR survival modeling | 10-year CVD risk in primary prevention and diabetes, treatment-eligibility triage |
| 202504 | [CONCERN](#model-concern-202504) | Nat. Med. | nursing documentation, EHR | — | 60.9K trial encounters | supervised deterioration prediction | hourly deterioration alerts and clinical surveillance |
| 202406 | [CLMBR-T-base](#model-clmbr-t-base-202406) | npj Digit. Med. | longitudinal EHR codes | 141M | 2.57M Stanford pretraining patients | autoregressive next-code prediction, local continued pretraining | eight clinical tasks, transfer, and label efficiency |
| 202403 | [Foresight](#model-foresight-202403) | Lancet Digit. Health | clinical text converted to temporal concepts | — | 811K patients across three source cohorts | autoregressive next-concept prediction | patient timeline generation, future disorder prediction |

## Details

Click a model to expand its record.

<a id="ehr-foundation-models"></a>

### EHR models and patient representations

<a id="model-computable-patient-journeys-202609"></a>
<details>
<summary><b>Computable patient journeys</b> — temporal patient graphs, GLP-1 treatment trajectories <i>(Nat. Med. 2026-09)</i></summary>

**[Computable longitudinal patient journeys from structured and unstructured EHR data](https://doi.org/10.1038/s41591-026-04695-x)**

*Nat. Med.* · 2026-09 · [Edward Kim](https://orcid.org/0000-0001-5345-3781) & [Vicki Seyfert-Margolis](https://orcid.org/0009-0003-6560-3507) · [doi:10.1038/s41591-026-04695-x](https://doi.org/10.1038/s41591-026-04695-x)

| | |
| --- | --- |
| **Parameters** | 4B for the open extraction model; proprietary models and the complete pipeline have no disclosed total. |
| **Backbone** | LLM extraction and verification followed by ontology normalization and temporal knowledge-graph construction. |
| **Training** | Instruction tuning and teacher-label distillation using a 100,000-visit cohort, with a 70%/30% training/validation split. |
| **Data / cohorts** | Source EHR covers 35M patients; extraction uses 1M visits from 31,235 patients. The 100,000-visit tuning cohort is drawn from this extraction sample. The GLP-1 receptor agonist analysis includes 25,092 patients. |
| **Downstream tasks** | Medication, diagnosis, and outcome extraction; computable treatment and disease trajectories. |
| **Modalities** | EHR, clinical text |
| **Evidence** | Retrospective cohort analysis and blinded physician adjudication of extractions; treatment associations are observational. |
| **Code / resources** | [Extraction and validation assets](https://github.com/MyOwnMed/glp1_nature2026_extraction_validation) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Medication extraction | precision | 95.5% | 221 physician-adjudicated extractions |

</details>

<a id="model-mochiformer-mochiagent-202609"></a>
<details>
<summary><b>MoChiFormer / MoChiAgent</b> — maternal and infant outcomes, transgenerational risk <i>(Nat. Med. 2026-09)</i></summary>

**[Prediction of maternal and infant outcomes from longitudinal electronic health records with a Mother-Child AI agent](https://doi.org/10.1038/s41591-026-04694-y)**

*Nat. Med.* · 2026-09 · Sian Liu & [Fanxin Zeng](https://orcid.org/0000-0002-7337-4463) · [doi:10.1038/s41591-026-04694-y](https://doi.org/10.1038/s41591-026-04694-y)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | MoChiFormer combines visit-level transformers with a causal temporal decoder; MoChiAgent adds an LLM interface. |
| **Training** | Masked categorical and numerical reconstruction with variational regularization, followed by supervised multitask adaptation. |
| **Data / cohorts** | Development: 1,064,733 mothers and 393,375 infants across 4.40M visits. External cohorts: 75,816 mothers and 14,418 infants. |
| **Downstream tasks** | Missing-data imputation, gestational and infant age estimation, maternal and infant disease prediction, and transgenerational risk. |
| **Modalities** | maternal and infant EHR |
| **Evidence** | Multicohort retrospective evaluations separate concurrent disease detection from forecasting using pre-diagnosis records. The agent interface was assessed in an offline 25-case pilot with six specialists. |
| **Code / resources** | [MoChiAgent](https://github.com/peterzheng98/mochiagent) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Gestational diabetes, future prediction | AUROC | 0.79 | Pre-diagnosis EHR inputs; Figure 4b. Concurrent detection: 0.91 (Figure 4a). |

</details>

<a id="model-pulse-202608"></a>
<details>
<summary><b>PULSE</b> — cross-modal imputation, disease risk, trajectory forecasting <i>(Nat. Comput. Sci. 2026-08)</i></summary>

**[Longitudinal alignments and syntheses of multimodal clinical data for personalized medicine with the PULSE framework](https://doi.org/10.1038/s43588-026-01026-5)**

*Nat. Comput. Sci.* · 2026-08 · [Wei Wu](https://orcid.org/0009-0008-1250-3998) & [Kang Zhang](https://orcid.org/0000-0002-4549-1697) · [doi:10.1038/s43588-026-01026-5](https://doi.org/10.1038/s43588-026-01026-5)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Modality-specific variational encoders and temporal propagation using recurrent or causal transformer modules. |
| **Training** | Reconstructs missing modalities using current observations and past patient states, with variational and missingness-adversarial objectives. |
| **Data / cohorts** | Core UK Biobank experiment: 10,000 participants with paired visits, split 7,000/3,000 for training/testing; 61 blood measures and 251 metabolites. Additional experiments use proteomics, retinal images, and clinical cohorts. |
| **Downstream tasks** | Longitudinal cross-modal imputation, disease prediction, ICU readmission, and myopia forecasting. |
| **Modalities** | longitudinal labs, omics, images, EHR |
| **Evidence** | Retrospective experiments with task-specific cohorts and splits; generated measurements are evaluated against observed data. |
| **Code / resources** | [LongitudinalGeneration](https://github.com/ww20hust/LongitudinalGeneration) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Six diseases using generated proteomic profiles | AUROC | 0.72–0.83 | Task-specific classifiers |

</details>

<a id="model-ofm-202608"></a>
<details>
<summary><b>oFM</b> — survival, response, exploratory treatment ranking <i>(arXiv (preprint) 2026-08)</i></summary>

**[A Multimodal Foundation Model for Longitudinal Patient Representation and Scalable Insight Generation in Oncology](https://arxiv.org/abs/2608.24688)**

*arXiv (preprint)* · 2026-08 · Eugene Vorontsov & Siqi Liu

| | |
| --- | --- |
| **Parameters** | 421M trained parameters plus the frozen 5.1B PRISM2 encoder (paper Table A4). |
| **Backbone** | GatorTron episode encoder, temporal transformer, and frozen PRISM2 pathology encoder, with molecular inputs. |
| **Training** | Episode denoising, masked-episode and future-state representation prediction, then joint multimodal adaptation. |
| **Data / cohorts** | 1,672,203 patients overall. Training stages use 1,045,011 patients for episode learning, 386,382 for trajectories, and 92,567 with molecular data; stages are overlapping subsets. |
| **Downstream tasks** | Survival and treatment-response prediction, patient representations, and exploratory treatment ranking. |
| **Modalities** | oncology EHR, pathology, DNA/RNA |
| **Evidence** | Preprint; retrospective observational evaluations. Treatment ranking does not establish treatment benefit. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Overall-survival prediction | mean AUROC | 0.774 | Across evaluated tasks |

</details>

<a id="model-oncoformer-202607"></a>
<details>
<summary><b>Oncoformer</b> — Advancing cancer detection and treatment using longitudinal routine clinical data <i>(Cell 2026-07)</i></summary>

**[Advancing cancer detection and treatment using longitudinal routine clinical data](https://doi.org/10.1016/j.cell.2026.07.009)**

*Cell* · 2026-07 · Fei Liu & Kang Zhang · [doi:10.1016/j.cell.2026.07.009](https://doi.org/10.1016/j.cell.2026.07.009)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Unified multimodal transformer; 24-layer examination encoder (d=1024) and 12-layer temporal decoder (d=768). Visit-level encoding uses a BERT-style transformer encoder; chest X-rays are embedded with a DINOv2-pretrained Vision Transformer backbone. |
| **Training** | `self-supervised`, `reconstruction`, `domain-adversarial`, `cross-modal alignment`<br>Self-supervised reconstruction with a VAE regularization term, combined with domain-adversarial losses against cohort-specific and missingness patterns to promote cohort-invariant and missing-invariant representations, plus a cross-modal alignment term between tabular and image latents. |
| **Data / cohorts** | COMPASS cohort, with external validation on UK Biobank<br>**3,672,989** individuals · **17,748,334** clinical visits · **502,665** UK Biobank participants |
| **Downstream tasks** | `diagnosis`, `risk prediction`, `staging`, `treatment response`, `survival prediction`, `patient clustering`<br>Pan-cancer diagnosis, future cancer prediction, tumor staging, treatment-response prediction, recurrence-free survival prediction, and patient clustering. |
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
<summary><b>RisQ</b> — Learning the shared structure of human health across diseases, modalities, and time <i>(medRxiv preprint 2026-07)</i></summary>

**[Learning the shared structure of human health across diseases, modalities, and time](https://www.medrxiv.org/content/10.64898/2026.07.07.26357373v1)**

*medRxiv (preprint)* · 2026-07 · [Paul Hager](https://scholar.google.com/citations?user=ESLUtGAAAAAJ) & [Francesco Paolo Casale](https://scholar.google.com/citations?user=AUFp6j4AAAAJ)

| | |
| --- | --- |
| **Parameters** | Not stated in the paper. **507,713 trainable parameters (0.51M)** for the published `hidden_dim=64` configuration, taken from the author-supplied count table in the official repository (`figures/scripts/supplementary/f_supp_scaling_val_loss.py`, `HIDDEN_DIM_TO_N_PARAMS`), whose stated conditions — RepQuery on UK Biobank variables at `icd_hierarchy_level=[3]` — match `TFM/configs/model/RepQuery.yaml`. |
| **Backbone** | Transformer encoder-decoder with FT-Transformer feature tokenizers, BioLORD concept embeddings, and a cross-attention query decoder conditioned on disease and time horizon; 1-layer encoder and 1-layer decoder (d=64, 4 heads, 64 health tokens, 4,463 input features — 1,370 baseline plus 588 ICD and 2,505 medication features) |
| **Training** | `horizon-conditional supervised`, `multi-task`<br>Single-stage horizon-conditional supervised multi-task training with 60% modality dropout; no self-supervised stage. |
| **Data / cohorts** | UK Biobank, with external validation on All of Us without retraining<br>**488,170** participants · **3,813,248** diagnosis events · **3,658** structured and unstructured features spanning medications, biomarkers, and physical measurements · **257,538** All of Us participants |
| **Downstream tasks** | `risk prediction`, `survival`, `zero-shot generalization`, `temporal extrapolation`, `genetic association`<br>Multi-disease risk at 1/2/5/10-year horizons, survival, zero-shot leave-one-ICD-chapter-out generalization, temporal extrapolation, and exome-wide burden association. |
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
| **Backbone** | Decoder-only LLM embedding models — Qwen3-Embedding, Qwen2-Emb-7B, and Llama3.1-LLM2Vec-8B — with logistic-regression heads |
| **Training** | `off-the-shelf LLM embeddings`<br>No task-specific pre-training. Structured EHR codes are serialized into natural-language descriptions and embedded with general-purpose LLM encoders. |
| **Data / cohorts** | Downstream benchmark cohorts, not LLM pretraining data: EHRSHOT and UK Biobank<br>**6,739** patients · **921,499** visits · **41,661,637** events (EHRSHOT) · **387,464** UK Biobank patients · **19,484,777** visits · **72,265,684** events ([Table 1](https://www.nature.com/articles/s41746-026-02915-9/tables/1)). The processed UK Biobank subset used in the study is 387,464 patients, drawn from the full 502,489-participant cohort. |
| **Downstream tasks** | `operational outcomes`, `lab value prediction`, `new diagnoses`, `chest X-ray findings`<br>15 clinical prediction tasks spanning operational outcomes, lab value prediction, new diagnoses, and chest X-ray findings. |
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
| **Training** | `self-supervised`, `competing-risk time-to-event`<br>Self-supervised competing-risk, time-to-next-event objective over 263 competing outcomes: 74 long-term conditions, 81 medication classes, and 108 test types. |
| **Data / cohorts** | CPRD Aurum, with a 90-5-5 split by practice site<br>**7,600,000,000** coded events · **~23,000,000** UK primary-care patients |
| **Downstream tasks** | `next-event prediction`, `risk prediction`, `multimorbidity progression`<br>Next-event prediction, 5-year incident hypertension, 5-year CVD under competing risks, and multimorbidity progression from age 50. |
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
<summary><b>APOLLO</b> — A multimodal and temporal foundation model for virtual patient representations <i>(arXiv preprint 2026-04)</i></summary>

**[A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/abs/2604.18570)**

*arXiv (preprint)* · 2026-04 · [Andrew Zhang](https://scholar.google.com/citations?user=WDiKxmcAAAAJ) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ) · [arXiv:2604.18570](https://arxiv.org/abs/2604.18570)

| | |
| --- | --- |
| **Parameters** | Not reported in the paper. **266,125,824 (266.1M), computed** for the transformer trunk: the 235,768 x 768 structured embedding table (181,069,824) plus 12 transformer blocks at E=768, 12 heads, and a 4E-width MLP (85,054,464) and the final LayerNorm. Decoder weights for discrete vocabularies are tied to the input embeddings, so the output head adds no weights. Excludes the learnable time encoding, per-modality mask vectors, the projectors onto the 28 frozen unimodal encoders, and the unstructured regression head. |
| **Backbone** | Transformer encoder-decoder over a single time-ordered heterogeneous event sequence, with learnable time encoding replacing positional embeddings and modality-specific adapters (GatorTron for text, vision foundation models for images); 12 layers, 12 heads, d=768, 1,536-event context, 235,768-token structured vocabulary |
| **Training** | `masked event modeling`<br>Masked event and token modeling at a 0.3 mask ratio with modality-specific mask tokens; cross-entropy for structured tokens and embedding regression for unstructured inputs. |
| **Data / cohorts** | MGB-7M study corpus: **7,155,044** patients and **25,296,943,893** medical events over 33 years and 28 modalities. These totals include a held-out test set of **1.4M** patients; they are not training-only counts. |
| **Downstream tasks** | `disease onset`, `disease progression`, `treatment response`, `adverse events`, `hospital operations`, `retrieval`<br>261 prognostic tasks plus 61 retrieval cohorts via frozen embeddings — new disease onset (95), disease progression (78), treatment response (59), adverse events (17), hospital operations (12), and 61 retrieval cohorts. |
| **Modalities** | `EHR`, `text`, `images`, `28 modalities` |
| **Evidence** | Preprint; retrospective evaluations using frozen patient embeddings. |

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
| **Training** | `biomedical LLM pretraining`, `supervised fine-tuning`<br>BioMistral biomedical pretraining followed by supervised fine-tuning on clinical trajectories. |
| **Data / cohorts** | NSCLC Flatiron Health, MIMIC-IV ICU, and ADNI Alzheimer's cohorts<br>**16,496** NSCLC patients · **35,131** ICU patients · **1,140** Alzheimer's patients |
| **Downstream tasks** | `trajectory forecasting`, `zero-shot forecasting`, `interpretability`<br>Multivariate clinical-variable trajectory forecasting, zero-shot forecasting of unseen variables, and chatbot-based patient-level interpretability. |
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
| **Training** | `autoregressive generative`<br>Autoregressive generative modeling of disease-event sequences with continuous age encoding. |
| **Data / cohorts** | UK Biobank for training, with validation on Danish national data<br>**~400,000** UK Biobank participants · **1,900,000** Danish individuals (validation) |
| **Downstream tasks** | `rate prediction`, `trajectory generation`, `burden estimation`, `comorbidity structure`<br>Predict rates of more than 1,000 diseases, generate future health trajectories, estimate disease burden, and interpret comorbidity structure. |
| **Modalities** | `EHR` |
| **Code** | [github.com/gerstung-lab/delphi](https://github.com/gerstung-lab/delphi) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| UK Biobank, >1,000 diseases | mean AUC | ~0.76 | |
| UK Biobank, death | AUC | 0.97 | |
| 1.9M Danish individuals, no retraining | mean AUC | 0.67 (s.d. 0.09) | |

</details>

<a id="model-infehr-202509"></a>
<details>
<summary><b>InfEHR</b> — neonatal sepsis and postoperative AKI phenotyping <i>(Nat. Commun. 2025-09)</i></summary>

**[InfEHR: Clinical phenotype resolution through deep geometric learning on electronic health records](https://doi.org/10.1038/s41467-025-63366-6)**

*Nat. Commun.* · 2025-09 · Justin Kauffman & [Girish N. Nadkarni](https://orcid.org/0000-0001-6319-4314) · [doi:10.1038/s41467-025-63366-6](https://doi.org/10.1038/s41467-025-63366-6)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Graph neural representations of temporal patient records with phenotype-prior and probability-refinement components. |
| **Training** | Self-supervised representation learning combined with rule-derived priors and semisupervised phenotype inference. |
| **Data / cohorts** | Mount Sinai neonatal cohort: 8,067 patients and 9,256 antibiotic courses. Separate postoperative AKI cohorts include external UC Irvine data. |
| **Downstream tasks** | Resolving uncertain clinical phenotypes, demonstrated in neonatal sepsis and postoperative acute kidney injury. |
| **Modalities** | temporal EHR graphs |
| **Evidence** | Retrospective adjudicated-label and external-cohort evaluations; phenotype resolution is distinct from prospective disease forecasting. |
| **Code / resources** | [InfEHR](https://github.com/Nadkarni-Lab/InfEHR) |

</details>

<a id="model-patientembedding-202508"></a>
<details>
<summary><b>PatientEmbedding</b> — disease onset, phenotyping, subtyping, and progression <i>(npj Digit. Med. 2025-08)</i></summary>

**[Transformer patient embedding using electronic health records enables patient stratification and progression analysis](https://doi.org/10.1038/s41746-025-01872-z)**

*npj Digit. Med.* · 2025-08 · Su Xian & David R. Crosslin · [doi:10.1038/s41746-025-01872-z](https://doi.org/10.1038/s41746-025-01872-z)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Medical-code autoencoder, six-layer transformer, and sentence-embedding model for patient similarity. |
| **Training** | Code reconstruction, temporal modeling with 20% code masking, and patient-pair representation learning. |
| **Data / cohorts** | 102,740 eMERGE patients; 1,046,649 longitudinal patient-year events and 34,851 medical codes. University of Washington records support external subtype analyses. |
| **Downstream tasks** | Next-year disease prediction, phenotyping, colorectal cancer and lupus subtyping, and progression analysis. |
| **Modalities** | longitudinal EHR codes |
| **Evidence** | Retrospective prediction and external subtype validation. |
| **Code / resources** | [Patient embedding implementation](https://github.com/suxian06/language-model-based-patient-embedding) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Next-year disease / bulk phenotyping | median AUROC | 0.87 / 0.84 | Logistic-regression models using embeddings |

</details>

<a id="model-clmbr-t-base-202406"></a>
<details>
<summary><b>CLMBR-T-base</b> — eight clinical tasks, transfer, and label efficiency <i>(npj Digit. Med. 2024-06)</i></summary>

**[A multi-center study on the adaptability of a shared foundation model for electronic health records](https://doi.org/10.1038/s41746-024-01166-w)**

*npj Digit. Med.* · 2024-06 · Lin Lawrence Guo & [Lillian Sung](https://orcid.org/0000-0003-0951-3091) · [doi:10.1038/s41746-024-01166-w](https://doi.org/10.1038/s41746-024-01166-w)

| | |
| --- | --- |
| **Parameters** | 141M for CLMBR-T-base. |
| **Backbone** | 12-layer decoder transformer with local attention and a 65,536-code vocabulary. |
| **Training** | Autoregressive next-clinical-code prediction, optionally continued on local records before task-specific prediction. |
| **Data / cohorts** | 2.57M Stanford patients for initial pretraining; SickKids and MIMIC-IV support local adaptation and evaluation. |
| **Downstream tasks** | Eight clinical prediction tasks, transfer across institutions, and label-efficiency assessment. |
| **Modalities** | longitudinal EHR codes |
| **Evidence** | Retrospective multicenter benchmarks comparing direct transfer and continued local pretraining. |
| **Code / resources** | [SickKids experiments](https://github.com/sungresearch/femr-on-sk) · [MIMIC experiments](https://github.com/sungresearch/femr-on-mimic) · [Base weights](https://huggingface.co/StanfordShahLab/clmbr-t-base) |

</details>

<a id="model-foresight-202403"></a>
<details>
<summary><b>Foresight</b> — patient timeline generation, future disorder prediction <i>(Lancet Digit. Health 2024-03)</i></summary>

**[Foresight—a generative pretrained transformer for modelling of patient timelines using electronic health records: a retrospective modelling study](https://doi.org/10.1016/S2589-7500(24)00025-6)**

*Lancet Digit. Health* · 2024-03 · Zeljko Kraljevic & Richard J. B. Dobson · [doi:10.1016/S2589-7500(24)00025-6](https://doi.org/10.1016/S2589-7500(24)00025-6)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | CogStack/MedCAT extracts timestamped concepts from notes; a 16-layer, 16-head causal transformer models the resulting timelines. |
| **Training** | Generative next-concept prediction on patient histories. |
| **Data / cohorts** | 811,336 patients overall across King’s College Hospital, South London and Maudsley, and MIMIC-III; models are trained separately by dataset. |
| **Downstream tasks** | Forecasting new disorders and other biomedical concepts, and generating synthetic patient timelines. |
| **Modalities** | clinical text converted to temporal concepts |
| **Evidence** | Retrospective evaluations and clinician-reviewed synthetic examples. The paper defines “precision@10” as at least one correct candidate among ten. |
| **Code / resources** | [Foresight](https://github.com/CogStack/Foresight) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Next new disorder, KCH / SLaM / MIMIC-III | authors’ precision@10 | 0.68 / 0.76 / 0.88 | Hit-based definition described above |

</details>

### Disease risk, subtyping, and survival

<a id="model-aladynoulli-202607"></a>
<details>
<summary><b>ALADYNOULLI</b> — A Bayesian framework for longitudinal EHR and genetic discovery <i>(Nature 2026-07)</i></summary>

**[A Bayesian framework for longitudinal EHR and genetic discovery](https://www.nature.com/articles/s41586-026-10780-5)**

*Nature* · 2026-07 · [Sarah M. Urbut](https://scholar.google.com/citations?user=iafjMbAAAAAJ) & [Giovanni Parmigiani](https://scholar.google.com/citations?user=OlpYP3UAAAAJ) · [doi:10.1038/s41586-026-10780-5](https://doi.org/10.1038/s41586-026-10780-5)

| | |
| --- | --- |
| **Parameters** | N/A — Bayesian generative model with K = 21 signatures: 20 disease signatures and one low-incidence signature |
| **Backbone** | Bayesian generative mixture model with Gaussian-process priors over time; 36 polygenic risk scores plus sex and 10 genetic PCs feed individual-specific signature loadings |
| **Training** | `Bayesian inference`<br>Hierarchical Bayesian inference jointly over longitudinal diagnoses, age, and polygenic risk; fitted separately in each biobank. |
| **Data / cohorts** | UK Biobank, Mass General Brigham, and All of Us, with up to 52 years of follow-up<br>**427,239** UK Biobank · **48,069** Mass General Brigham · **208,263** All of Us · **>683,000** individuals · **348** diseases |
| **Downstream tasks** | `signature discovery`, `risk prediction`, `genetic discovery`, `patient stratification`<br>Latent time-varying disease-signature discovery, 1-year and 10-year risk prediction, common- and rare-variant genetic discovery, and patient stratification. |
| **Modalities** | `EHR`, `genetics` |
| **Code** | [doi:10.5281/zenodo.20802505](https://doi.org/10.5281/zenodo.20802505) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 1-year ASCVD | AUC | 0.881 | |
| Cross-cohort signature preservation | median preservation | 80% | |
| Rare-variant analysis | genome-wide-significant loci | 151 loci, 18 unique genes | |

</details>

<a id="model-transformer-dapt-202607"></a>
<details>
<summary><b>Transformer-DAPT</b> — 1–12-month ischemic and bleeding risk after PCI <i>(npj Digit. Med. 2026-07)</i></summary>

**[Transformer-DAPT: AI-based dynamic assessment of ischemic and bleeding risks in patients on DAPT following PCI](https://doi.org/10.1038/s41746-026-02977-9)**

*npj Digit. Med.* · 2026-07 · Ahmed Abdelhameed & Cui Tao · [doi:10.1038/s41746-026-02977-9](https://doi.org/10.1038/s41746-026-02977-9)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Transformer over active feature indices from 3,445 clinical variables collected during the two years before PCI; survival and binary-classification heads. |
| **Training** | Joint piecewise-constant hazard loss, binary cross-entropy, and outcome-supervised triplet loss for representation learning. |
| **Data / cohorts** | 29,032 Mayo Clinic patients, split 70%/10%/20% for training/validation/testing; 19,173 OneFlorida patients for external validation. |
| **Downstream tasks** | Ischemic and bleeding risk at 1, 2, 3, 6, 9, and 12 months after PCI, using pre-PCI clinical features. |
| **Modalities** | EHR-derived clinical features |
| **Evidence** | Retrospective internal and external validation; proposed treatment applications have not been tested in an intervention trial. |
| **Code / resources** | [Transformer-DAPT](https://github.com/Tao-AI-group/Transformer-DAPT) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| External validation | time-dependent C-index | 0.74–0.84 ischemic; 0.75–0.83 bleeding | Across evaluated time points |

</details>

<a id="model-dynamic-vte-transformer-202605"></a>
<details>
<summary><b>Dynamic VTE transformer</b> — quarterly venous thromboembolism risk during cancer treatment <i>(npj Digit. Med. 2026-05)</i></summary>

**[A deep learning model to dynamically predict cancer-associated thromboembolism in large-scale healthcare systems](https://doi.org/10.1038/s41746-026-02730-2)**

*npj Digit. Med.* · 2026-05 · Tianshe He & Nathanael R. Fillmore · [doi:10.1038/s41746-026-02730-2](https://doi.org/10.1038/s41746-026-02730-2)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Transformer over diagnosis histories, laboratory results, and demographic features. |
| **Training** | Supervised dynamic risk prediction after systemic cancer treatment begins. |
| **Data / cohorts** | 80,808 Veterans Affairs patients for development; 9,752 Harris Health patients for external validation. |
| **Downstream tasks** | Updating cancer-associated venous thromboembolism risk in three-month intervals during the first treatment year. |
| **Modalities** | EHR, labs, cancer treatment |
| **Evidence** | Retrospective external validation; anticoagulant-prescribing benefit was not tested prospectively. |
| **Code / resources** | [VTERisk](https://github.com/thunder001/VTERisk) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| External quarterly predictions | AUROC | 0.68–0.74 | Across prediction intervals |

</details>

<a id="model-tcpm-202605"></a>
<details>
<summary><b>TCPM</b> — temporal treatment-response modeling, medication policies <i>(Nat. Commun. 2026-05)</i></summary>

**[A generalist precision medication framework using temporal causal inference based on treatment-free physiological profiles](https://doi.org/10.1038/s41467-026-73238-2)**

*Nat. Commun.* · 2026-05 · [Zizhen Deng](https://orcid.org/0009-0003-4235-9345) & [Jinzhuo Wang](https://orcid.org/0000-0002-9464-4426) · [doi:10.1038/s41467-026-73238-2](https://doi.org/10.1038/s41467-026-73238-2)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Encoder–decoder with adversarial learning of treatment-free physiological representations and temporal policy optimization. |
| **Training** | Counterfactual outcome learning followed by medication-policy optimization under causal assumptions. |
| **Data / cohorts** | Six task-specific datasets spanning sepsis, diabetes, hypertension, coronary disease, pediatric burns, and macular degeneration; no single pooled training cohort. |
| **Downstream tasks** | Individualized longitudinal treatment-response estimation and medication-policy generation. |
| **Modalities** | longitudinal physiology, treatments |
| **Evidence** | Offline observational evaluation and physician simulation; causal identification assumptions and prospective clinical utility remain distinct questions. |
| **Code / resources** | [Precision-Medication](https://github.com/zizhendeng/Precision-Medication) |

</details>

<a id="model-gru-da-202605"></a>
<details>
<summary><b>GRU-DA</b> — dynamic Alzheimer’s and related dementia risk <i>(npj Digit. Med. 2026-05)</i></summary>

**[A dynamic risk prediction framework for Alzheimer's disease and related dementias with interpretability](https://doi.org/10.1038/s41746-026-02732-0)**

*npj Digit. Med.* · 2026-05 · Xiaoyang Ruan & Hongfang Liu · [doi:10.1038/s41746-026-02732-0](https://doi.org/10.1038/s41746-026-02732-0)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | GRU-D recurrent model with missingness decay and RETAIN-style attention. |
| **Training** | Supervised prediction using historical EHR sequences and varying follow-up start times. |
| **Data / cohorts** | UT Physicians development data include 15,172 ADRD cases with ten matched controls per case; external testing uses All of Us. |
| **Downstream tasks** | Dynamic Alzheimer’s disease and related dementia risk with interpretable temporal predictors. |
| **Modalities** | longitudinal EHR |
| **Evidence** | Retrospective matched-cohort and external evaluation; risk horizons depend on the prediction time relative to diagnosis. |
| **Code / resources** | [GRU-D-RETAIN](https://github.com/ruanxiaoyang-UT/GRU-D-RETAIN) |

</details>

<a id="model-early-adhd-202604"></a>
<details>
<summary><b>Early-ADHD</b> — Early ADHD prediction from longitudinal electronic health records <i>(Nat. Ment. Health 2026-04)</i></summary>

**[Early attention deficit hyperactivity disorder prediction from longitudinal electronic health records](https://www.nature.com/articles/s44220-026-00628-2)**

*Nat. Ment. Health* · 2026-04 · Elliot D. Hill & Matthew Engelhard · [doi:10.1038/s44220-026-00628-2](https://doi.org/10.1038/s44220-026-00628-2)

| | |
| --- | --- |
| **Parameters** | Not reported for the full pretrained transformer; DoRA fine-tuning reduces trainable parameters to **29,440** |
| **Backbone** | Discrete time-to-event transformer with axial rotary positional embeddings encoding age, encounter position, and continuous values; weight-decomposed low-rank adaptation (DoRA) applied to each linear layer for fine-tuning |
| **Training** | `masked modeling`, `self-supervised`<br>Self-supervised masked-modeling pretraining on longitudinal EHR. |
| **Data / cohorts** | Pretraining: **721,896** patients. Pediatric fine-tuning cohort: **142,270** patients, including **113,846** in the training split. |
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
| **Backbone** | Deep learning over routine-care event sequences combining hospital diagnoses, primary-care prescriptions, and primary-care service events across 0-24 month horizons |
| **Training** | `supervised`<br>Supervised end-to-end risk prediction on registry sequences. |
| **Data / cohorts** | Nationwide Danish registries, 1995-2018<br>**3,435,638** individuals · **16,828** developed young-onset type 2 diabetes (diagnosis before age 40) |
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
| **Training** | `supervised`<br>Cox regression fitted to clinical covariates and evolving biomarkers, including M-protein, serum free light chain ratio, creatinine, and hemoglobin. |
| **Data / cohorts** | Dana-Farber Cancer Institute training cohort plus six international validation institutions<br>**1,031** training patients · **1,313** validation patients |
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
| **Training** | `masked modeling`, `contrastive`<br>Masked encounter modeling and contrastive learning, followed by K-means clustering of patient embeddings. The largest number of clusters with prediction strength ≥0.95 is selected. |
| **Data / cohorts** | CPRD Aurum and UK Biobank cohorts for Alzheimer's disease (AD) and Parkinson's disease (PD)<br>**113,545** AD CPRD Aurum · **3,710** AD UK Biobank · **45,825** PD CPRD Aurum · **3,732** PD UK Biobank |
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
| **Training** | Supervised survival modeling on EHR sequences. The accessible abstract does not specify a separate self-supervised pretraining stage. |
| **Data / cohorts** | Open cohort of adults aged 25-84 with linked primary and secondary care EHR, 1998-2015<br>**3,000,000** adults · **291** English GP practices (development) · **98** practices (validation) |
| **Downstream tasks** | `risk prediction`, `treatment triage`<br>10-year CVD risk in the primary-prevention population and in diabetes cohorts, and treatment-eligibility triage. |
| **Modalities** | `EHR` |
| **Evidence** | Retrospective development and validation; treatment-eligibility comparisons are decision-curve analyses, not a treatment trial. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 10-year CVD risk | C-index | 0.910 (95% CI 0.906-0.913) | outperforms QRISK3 across age, sex, and deprivation strata |
| Treatment-eligibility triage, 10% threshold | reduction in high-risk classifications | 20.6% fewer | |
| Treatment-eligibility triage, 15% threshold | reduction in high-risk classifications | 34.6% fewer | |

</details>

### Cardiac and physiological signals

<a id="model-ecg-clip-202609"></a>
<details>
<summary><b>ECG-CLIP</b> — cardiac diagnosis, AF, mortality, CKD, and diabetes risk <i>(Lancet Digit. Health 2026-09)</i></summary>

**[Development and external validation of a contrastive learning foundation model for ECG-based prediction of cardiovascular diseases and outcomes](https://doi.org/10.1016/j.landig.2026.101092)**

*Lancet Digit. Health* · 2026-09 · Michael Ko & Giorgio Quer · [doi:10.1016/j.landig.2026.101092](https://doi.org/10.1016/j.landig.2026.101092)

| | |
| --- | --- |
| **Parameters** | Not specified in the published abstract. |
| **Backbone** | Paired ECG and text encoders for multimodal representation learning. |
| **Training** | Two stages: masked ECG reconstruction and contrastive alignment with clinician-overread reports. |
| **Data / cohorts** | Scripps pretraining corpus: >1.7M ECGs from 542,288 patients. MIMIC-IV supplies >800K ECGs for downstream training and evaluation. |
| **Downstream tasks** | Myocardial infarction, amyloidosis, and hypertrophic cardiomyopathy detection; atrial fibrillation, mortality, kidney disease, and diabetes prediction. |
| **Modalities** | ECG, clinical reports |
| **Evidence** | Retrospective external-dataset evaluation with five-fold downstream cross-validation and label-efficiency experiments; external performance includes task adaptation. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| AMI detection, ten positive training labels | AUROC | 0.910 (95% CI 0.903–0.916) | MIMIC-IV |

</details>

<a id="model-ecg-scd-202606"></a>
<details>
<summary><b>ECG-SCD</b> — sudden cardiac death risk, ECG morphology analysis <i>(Nature 2026-06)</i></summary>

**[An ECG biomarker for sudden cardiac death discovered with deep learning](https://doi.org/10.1038/s41586-026-10674-6)**

*Nature* · 2026-06 · [Ziad Obermeyer](https://orcid.org/0000-0002-4563-5849) & [Markus Lingman](https://orcid.org/0000-0002-4068-0341) · [doi:10.1038/s41586-026-10674-6](https://doi.org/10.1038/s41586-026-10674-6)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | 64-layer one-dimensional residual CNN; generative ECG analysis probes learned morphology. |
| **Training** | Supervised multitask learning, including sudden cardiac death within one year. |
| **Data / cohorts** | Swedish training set: 262,554 ECGs from 75,157 patients; held-out set: 179,060 ECGs from 51,481 patients. External evaluations include US and Taiwanese cohorts. |
| **Downstream tasks** | Sudden cardiac death risk stratification and analysis of associated ECG features. |
| **Modalities** | ECG, linked outcomes |
| **Evidence** | Retrospective external validation. Defibrillator-benefit analyses are observational. |
| **Code / resources** | [Analysis and ECG morphing code](https://github.com/alexmschubert/ECG-SCD); trained Swedish weights require a data-access agreement. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| High-risk group | annual sudden cardiac death rate | 7.0% | Group comprises 2.2% of the evaluated ECG sample |

</details>

<a id="model-deephhf-202606"></a>
<details>
<summary><b>DeepHHF</b> — five-year heart failure risk <i>(npj Digit. Med. 2026-06)</i></summary>

**[Modeling day-long ECG signals to predict heart failure risk with explainable AI](https://doi.org/10.1038/s41746-026-02835-8)**

*npj Digit. Med.* · 2026-06 · Eran Zvuloni & Joachim A. Behar · [doi:10.1038/s41746-026-02835-8](https://doi.org/10.1038/s41746-026-02835-8)

| | |
| --- | --- |
| **Parameters** | Approximately 13M, reported for DeepHHF. |
| **Backbone** | Residual CNN encodes ECG segments; a transformer combines them across a day-long recording. |
| **Training** | Two-stage supervised learning with weighted binary cross-entropy. |
| **Data / cohorts** | After exclusions, 57,575 recordings from 40,174 patients; the source dataset contains 69,663 recordings from 47,729 patients. |
| **Downstream tasks** | Five-year incident heart failure prediction from ambulatory ECG. |
| **Modalities** | 24-hour ECG |
| **Evidence** | Retrospective held-out evaluation; no independent external cohort reported. |
| **Code / resources** | The paper’s model-release URL remains a placeholder. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Five-year heart failure | AUROC | 0.80 | Clinical PCP-HF comparator: 0.74 |

</details>

<a id="model-ecg-lfm-202604"></a>
<details>
<summary><b>ECG-LFM</b> — Self-supervised ECG foundation model for CVD prediction and genetic discovery <i>(Nat. Commun. 2026-04)</i></summary>

**[A self-supervised electrocardiogram foundation model for empowering cardiovascular disease prediction and genetic factor discovery](https://www.nature.com/articles/s41467-026-72436-2)**

*Nat. Commun.* · 2026-04 · Siying Lin & [Huiying Zhao](https://scholar.google.com/citations?user=ei4g2_gAAAAJ) · [doi:10.1038/s41467-026-72436-2](https://doi.org/10.1038/s41467-026-72436-2)

| | |
| --- | --- |
| **Parameters** | Not reported; 1,024-d embeddings |
| **Backbone** | Convolutional feature encoder, Gumbel-softmax multi-codebook quantizer, and Conformer context blocks, in the style of wav2vec 2.0 |
| **Training** | `self-supervised`, `contrastive`, `masked modeling`, `multi-task`<br>Self-supervised multi-task learning combining contextual contrastive, masked-modeling, and multi-segment contrastive losses. |
| **Data / cohorts** | Harvard-Emory ECG Database plus MIMIC-IV-ECG<br>**11,571,587** 12-lead ECGs · **1,979,599** individuals. These are the reported combined pretraining totals. |
| **Downstream tasks** | `classification`, `phenotyping`, `identification`, `genetic discovery`<br>8 cardiovascular disease classifications, 8 cardiac functional phenotypes, individual identification, and genetic factor discovery. |
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
| **Backbone** | Vision Transformer variant in three sizes — CSFM-Tiny (6 encoder layers, hidden 1024, 8 attention heads), CSFM-Base (12 layers, hidden 3072, 12 heads), and CSFM-Large (16 layers, hidden 4096, 24 heads) |
| **Training** | `generative masked pretraining`<br>MAE-style generative masked pretraining with 75% of ECG tokens and 50% of text tokens masked; multimodal ECG/PPG signals paired with clinical and machine-generated text reports. |
| **Data / cohorts** | MIMIC-III-WDB (USA), MIMIC-IV-ECG (USA), and CODE-Full (Brazil)<br>**~1,700,000** individuals |
| **Downstream tasks** | `diagnosis`, `demographic recognition`, `vital sign estimation`, `outcome prediction`, `question answering`<br>Cardiac disease diagnosis, demographic recognition, vital sign measurement, clinical outcome prediction, and ECG question answering, evaluated on CinC17, PTB-XL, VTaC, CODE-15, SimBand, and ECG-QA. |
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
| **Training** | `masked signal modeling`, `self-supervised`<br>Self-supervised masked signal modeling at a 60% masking ratio. |
| **Data / cohorts** | Pretraining on MIMIC-IV-ECG, fine-tuning on PET-derived labels and clinical reports, with generalization assessed across five further cohorts including PTB-XL, UK Biobank cardiac MRI, and SPECT<br>**800,035** unlabeled ECGs · **3,126** PET-derived labels · **13,704** clinical reports |
| **Downstream tasks** | `regression`, `classification`, `cross-modality transfer`<br>12 clinical, demographic, and traditional ECG tasks including LVEF, myocardial flow reserve, rest and stress myocardial blood flow, and total perfusion deficit. |
| **Modalities** | `ECG` |
| **Code** | [github.com/4dm-labs/ecgflow](https://github.com/4dm-labs/ecgflow) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 12 internal tasks | AUROC range | 0.763-0.955 | 0.763 for impaired myocardial flow reserve <2, 0.955 for impaired LVEF <35% |
| External and cross-modality cohorts | AUROC range | 0.771-0.949 | |
| Self-supervised versus de novo supervised training | tasks improved | 11 of 12 | |

</details>

<a id="model-echonext-202507"></a>
<details>
<summary><b>EchoNext</b> — structural heart disease screening <i>(Nature 2025-07)</i></summary>

**[Detecting structural heart disease from electrocardiograms using AI](https://doi.org/10.1038/s41586-025-09227-0)**

*Nature* · 2025-07 · [Timothy J. Poterucha](https://orcid.org/0000-0001-7284-3937) & [Pierre Elias](https://orcid.org/0000-0002-9643-3024) · [doi:10.1038/s41586-025-09227-0](https://doi.org/10.1038/s41586-025-09227-0)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Convolutional ECG model with demographic and tabular ECG inputs, trained against echocardiography-derived targets. |
| **Training** | Supervised multitask prediction of structural abnormalities and a composite screening label. |
| **Data / cohorts** | Training: 796,816 paired ECG/echo records from 149,819 patients. External testing spans three systems; silent deployment includes 84,875 patients. |
| **Downstream tasks** | Screening for structural heart disease and identifying patients who may benefit from echocardiography. |
| **Modalities** | ECG, demographics, echo-derived labels |
| **Evidence** | External validation and silent deployment. The prospective DISCOVERY cohort was recruited using ValveNet, with EchoNext assessed subsequently. |
| **Code / resources** | [IntroECG dataset and smaller model](https://github.com/PierreElias/IntroECG); these are not the full clinical EchoNext weights. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Three external systems | AUROC | 0.78–0.80 | Structural heart disease screening |

</details>

<a id="model-ecgfounder-202506"></a>
<details>
<summary><b>ECGFounder</b> — An electrocardiogram foundation model built on over 10 million recordings <i>(NEJM AI 2025-06)</i></summary>

**[An Electrocardiogram Foundation Model Built on over 10 Million Recordings](https://ai.nejm.org/doi/full/10.1056/AIoa2401033)**

*NEJM AI* · 2025-06 · Jun Li & [Shenda Hong](https://scholar.google.com/citations?user=K95az5UAAAAJ) · [doi:10.1056/AIoa2401033](https://doi.org/10.1056/AIoa2401033)

| | |
| --- | --- |
| **Parameters** | 76.3M; ablation variants at 11.7M / 25.6M / 110M |
| **Backbone** | 1-D RegNet self-regulated CNN with group convolutions, channel attention, and skip connections |
| **Training** | `supervised pretraining`<br>Large-scale supervised pretraining on 150 cardiologist-annotated diagnostic labels. |
| **Data / cohorts** | Harvard-Emory ECG Database<br>**10,771,552** ECGs · **1,818,247** subjects · **150** label categories |
| **Downstream tasks** | `diagnosis`, `demographics`, `event detection`, `reduced-lead ECG`, `cross-modality transfer`, `wearable ECG`<br>150-way diagnosis, single- and reduced-lead ECG, demographics, clinical-event detection, cross-modality rhythm diagnosis, and wearable ECG. |
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

<a id="model-actitect-rbdisco-202606"></a>
<details>
<summary><b>ActiTect / RBDisco</b> — REM sleep behavior disorder screening <i>(npj Digit. Med. 2026-06)</i></summary>

**[ActiTect: a generalizable machine learning pipeline for REM sleep behavior disorder screening through standardized actigraphy](https://doi.org/10.1038/s41746-026-02738-8)**

*npj Digit. Med.* · 2026-06 · David Bertram & Katarzyna Bozek · [doi:10.1038/s41746-026-02738-8](https://doi.org/10.1038/s41746-026-02738-8)

| | |
| --- | --- |
| **Parameters** | N/A — feature-based boosted trees. |
| **Backbone** | ActiTect harmonizes device outputs and sleep–wake estimates; RBDisco uses XGBoost with interpretable motion features. |
| **Training** | Supervised feature-based classification with nested cross-validation; no neural pretraining. |
| **Data / cohorts** | 78 development participants, a blinded local test set of 31, and two independent external cohorts. Participant and recording counts differ. |
| **Downstream tasks** | Screening for REM sleep behavior disorder from nocturnal movement. |
| **Modalities** | wrist actigraphy |
| **Evidence** | Multicohort retrospective validation and device-robustness analyses; this predicts RBD rather than future Parkinson’s disease. |
| **Code / resources** | [ActiTect](https://github.com/bozeklab/actitect) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Independent external cohorts | AUROC | 0.84 / 0.94 | Cohort-specific screening results |

</details>

<a id="model-true-hf-202603"></a>
<details>
<summary><b>TRUE-HF</b> — Remote monitoring of heart failure exacerbations using a smartwatch <i>(Nat. Med. 2026-03)</i></summary>

**[Remote monitoring of heart failure exacerbations using a smartwatch](https://www.nature.com/articles/s41591-026-04247-3)**

*Nat. Med.* · 2026-03 · Yuan Gao & Heather J. Ross · [doi:10.1038/s41591-026-04247-3](https://doi.org/10.1038/s41591-026-04247-3)

| | |
| --- | --- |
| **Parameters** | Not reported; ~10 layers, d=512, 16 heads, deployed as a 10-model ensemble |
| **Backbone** | Autoregressive transformer with 1D-convolutional tokenization of HealthKit data at 90-1440 min resolutions, FiLM conditioning on clinical covariates, and rotary embeddings |
| **Training** | `semi-supervised`<br>Semi-supervised learning with daily target labels obtained by linearly interpolating outcomes between clinical assessments. |
| **Data / cohorts** | TRUE-HF study cohort, with external validation on an NIH All of Us Fitbit cohort<br>**217** patients with heart failure |
| **Downstream tasks** | `regression`, `early warning`<br>Predicting peak oxygen uptake (pVO2) and serving as an early warning signal for unplanned healthcare utilization from heart failure exacerbations. |
| **Modalities** | `smartwatch`, `clinical covariates` |
| **Code** | [github.com/mcintoshML/TRUEHF](https://github.com/mcintoshML/TRUEHF) |
| **Availability** | The official repository provides code; pretrained weights are not publicly released. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| pVO2 prediction | Pearson r | 0.85 | MAE 0.25 L/min |
| ≥10% pVO2 decline | AUROC | 0.82 (95% CI 0.69-0.92) | |
| Unplanned healthcare events | AUROC | 0.77 (0.62-0.90) | median lead time 7.4 days |

</details>

<a id="model-wear-me-wfm-202603"></a>
<details>
<summary><b>WEAR-ME / WFM</b> — insulin resistance screening <i>(Nature 2026-03)</i></summary>

**[Insulin resistance prediction from wearables and routine blood biomarkers](https://doi.org/10.1038/s41586-026-10179-2)**

*Nature* · 2026-03 · [Ahmed A. Metwally](https://orcid.org/0000-0002-0155-7412) & [Javier L. Prieto](https://orcid.org/0000-0003-3665-8114) · [doi:10.1038/s41586-026-10179-2](https://doi.org/10.1038/s41586-026-10179-2)

| | |
| --- | --- |
| **Parameters** | Not reported; the 384-dimensional embedding is not a parameter count. |
| **Backbone** | Wearable foundation model produces daily embeddings, which are pooled and reduced to five principal components for a nonlinear classifier. |
| **Training** | Masked reconstruction pretraining; the wearable encoder remains frozen during insulin-resistance classifier training. |
| **Data / cohorts** | 40M hours for pretraining. WEAR-ME: 932 training and 233 test participants; independent external cohort: 72 participants. |
| **Downstream tasks** | Insulin resistance prediction with wearable signals, demographics, and routine blood biomarkers. |
| **Modalities** | wearable signals, routine blood tests |
| **Evidence** | External validation against HOMA-IR-defined labels; no intervention trial. |
| **Code / resources** | [Insulin-resistance prediction code](https://github.com/Google-Health/consumer-health-research/tree/main/insulin_resistance_prediction) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| External validation | AUROC | 0.88 | Wearable embeddings plus demographics and blood markers; 0.76 without wearables |

</details>

<a id="model-brain-health-score-202602"></a>
<details>
<summary><b>Brain Health Score</b> — cognition, disease, mortality associations <i>(NEJM AI 2026-02)</i></summary>

**[Brain Health from Sleep EEG: A Multicohort, Deep Learning Biomarker for Cognition, Disease, and Mortality](https://doi.org/10.1056/AIoa2500487)**

*NEJM AI* · 2026-02 · Wolfgang Ganglberger & M. Brandon Westover · [doi:10.1056/AIoa2500487](https://doi.org/10.1056/AIoa2500487)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Deep networks process raw EEG or time–frequency spectrograms and learn a 1,024-dimensional latent representation. |
| **Training** | Joint prediction of cognition, disease, and sleep metrics, followed by distillation into a scalar Brain Health Score. |
| **Data / cohorts** | Approximately 36,000 polysomnography recordings from 27,000 people across six cohorts; these are study-wide totals. |
| **Downstream tasks** | Cognitive performance, disease status, and mortality association analysis. |
| **Modalities** | sleep EEG |
| **Evidence** | Multicohort observational validation; the score is a biomarker, not a demonstrated treatment target. |
| **Code / resources** | [Philosophers’ Stone](https://github.com/bdsp-core/philosophers-stone) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Mortality association | age-adjusted hazard ratio | 0.65–0.69 | Per standard-deviation higher score, across cohorts |

</details>

<a id="model-gluformer-202601"></a>
<details>
<summary><b>GluFormer</b> — A foundation model for continuous glucose monitoring data <i>(Nature 2026-01)</i></summary>

**[A foundation model for continuous glucose monitoring data](https://doi.org/10.1038/s41586-025-09925-9)**

*Nature* · 2026-01 · [Guy Lutsker](https://scholar.google.co.uk/citations?user=WBtGo0IAAAAJ&hl=en&oi=ao) & [Eran Segal](https://scholar.google.co.uk/citations?user=oAD8PrkAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41586-025-09925-9](https://doi.org/10.1038/s41586-025-09925-9)

| | |
| --- | --- |
| **Parameters** | Not reported in the paper. **135,341,516 (135.3M), computed** by instantiating the official `TransformerModel` from `train_model/train_GluFormer.py`: 16 `nn.TransformerEncoderLayer` blocks (d=1024, 16 heads, FFN 2048) contribute 134,397,952, the 461-row embedding table 472,064, and the untied 460-way output head 471,500. The sinusoidal positional encoding is a plain tensor, not a parameter, so it adds nothing. |
| **Backbone** | Autoregressive transformer |
| **Training** | `autoregressive`, `self-supervised`<br>Self-supervised autoregressive next-token prediction over a 461-token glucose vocabulary, using input sequences padded to 1,200 tokens. |
| **Data / cohorts** | Human Phenotype Project CGM data, validated on 19 external cohorts across 5 countries and 8 CGM devices<br>**>10,000,000** glucose measurements · **10,812** adults · **6,044** external participants |
| **Downstream tasks** | `trajectory generation`, `glycaemic prediction`, `risk stratification`, `multimodal extension`<br>Generate CGM trajectories, predict glycaemic measures such as HbA1c and fasting glucose plus long-term outcomes, risk stratification, and multimodal extension with diet. |
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
| **Parameters** | ~4.44M for the pretrained model; ~0.91M trainable in the downstream head, with the encoder frozen |
| **Backbone** | 1D CNN encoder (six conv layers, 128-d embeddings) with three transformer encoder layers and attention-based channel pooling; two LSTM layers in the downstream head |
| **Training** | `leave-one-out contrastive`<br>Leave-One-Out Contrastive Learning (LOO-CL). |
| **Data / cohorts** | Pretraining: **~432,000** hours of PSG from **~48,000** participants. The study-wide **~585,000** hours and **>65,000** participants include downstream and evaluation cohorts. |
| **Downstream tasks** | `disease prediction`, `sleep staging`, `phenotype estimation`<br>Disease prediction, sleep stage classification, and physiological and demographic estimation. |
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

<a id="model-sleepgpt-202601"></a>
<details>
<summary><b>SleepGPT</b> — sleep staging, pathology, signal generation, spindles <i>(Nat. Commun. 2026-01)</i></summary>

**[A unified time-frequency foundation model for sleep decoding](https://doi.org/10.1038/s41467-025-67970-4)**

*Nat. Commun.* · 2026-01 · Weixuan Huang & [Jia-Hong Gao](https://orcid.org/0000-0002-9311-0297) · [doi:10.1038/s41467-025-67970-4](https://doi.org/10.1038/s41467-025-67970-4)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Channel-adaptive transformer with time-domain and frequency-domain representations. |
| **Training** | Contrastive time–frequency alignment, hard-negative matching, and masked reconstruction. |
| **Data / cohorts** | Main-text pretraining set: 59,267 hours from 5,132 subjects. The larger 86,335-hour / 8,377-subject figure covers pretraining and evaluation. |
| **Downstream tasks** | Sleep staging, pathology classification, PSG generation, and spindle detection. |
| **Modalities** | multichannel PSG |
| **Evidence** | Retrospective evaluation across heterogeneous PSG datasets and channel configurations. |
| **Code / resources** | [SleepGPT](https://github.com/LordXX505/SleepGPT) |

</details>

<a id="model-gaitdynamics-202601"></a>
<details>
<summary><b>GaitDynamics</b> — gait generation, force estimation, missing-joint reconstruction <i>(Nat. Biomed. Eng. 2026-01)</i></summary>

**[GaitDynamics: a generative foundation model for analyzing human walking and running](https://doi.org/10.1038/s41551-025-01565-8)**

*Nat. Biomed. Eng.* · 2026-01 · [Tian Tan](https://orcid.org/0000-0003-4639-8301) & [Akshay S. Chaudhari](https://orcid.org/0000-0002-3667-6796) · [doi:10.1038/s41551-025-01565-8](https://doi.org/10.1038/s41551-025-01565-8)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Diffusion transformer generates kinematics and forces; a refinement model improves force estimates. |
| **Training** | Generative denoising and supervised force refinement. |
| **Data / cohorts** | 15 AddBiomechanics studies: 34.8 hours from 270 participants overall. Training uses 169 participants from eight studies; seven studies are held out entirely. |
| **Downstream tasks** | Walking and running synthesis, missing-joint reconstruction, ground-reaction-force estimation, and knee-loading analysis. |
| **Modalities** | motion trajectories, ground reaction forces |
| **Evidence** | Biomechanical validation on held-out movements and participants; no patient-outcome trial. |
| **Code / resources** | [Code, model, and demo](https://github.com/stanfordnmbl/GaitDynamics) |

</details>

### Inpatient deterioration and critical care

<a id="model-ed-foundation-202607"></a>
<details>
<summary><b>ED-Foundation</b> — emergency triage, prognosis, decision support <i>(npj Digit. Med. 2026-07)</i></summary>

**[A unified multi-modal foundation model for end-to-end emergency care](https://doi.org/10.1038/s41746-026-02981-z)**

*npj Digit. Med.* · 2026-07 · Zhenwei Huang & Tao Yu · [doi:10.1038/s41746-026-02981-z](https://doi.org/10.1038/s41746-026-02981-z)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | BEiT-3-based multimodal transformer with shared attention and modality-specific experts. |
| **Training** | Masked multimodal pretraining followed by contrastive alignment and downstream adaptation. |
| **Data / cohorts** | Includes 166,755 longitudinal narratives from SYSMH plus MIMIC-IV/ED, Quilt-1M, and RATIC resources; nine downstream datasets. |
| **Downstream tasks** | Emergency triage, prognosis, and decision support across stages of emergency care. |
| **Modalities** | clinical text, medical images |
| **Evidence** | Retrospective benchmarks across multiple datasets; no randomized deployment study reported. |
| **Code / resources** | [ED-Foundation implementation](https://github.com/AllminerLab/ED-Foundation) |

</details>

<a id="model-first-icu-202606"></a>
<details>
<summary><b>FIRST-ICU</b> — seven intervention forecasts, risk stratification <i>(npj Digit. Med. 2026-06)</i></summary>

**[FIRST-ICU: forecasting interventions and risk stratification in the ICU using graph neural network autoencoders](https://doi.org/10.1038/s41746-026-02890-1)**

*npj Digit. Med.* · 2026-06 · Nosa Aikodon & Sandra Ortega-Martorell · [doi:10.1038/s41746-026-02890-1](https://doi.org/10.1038/s41746-026-02890-1)

| | |
| --- | --- |
| **Parameters** | 1,792,015 for the discrete-decoder configuration; not a count for every variant. |
| **Backbone** | Graph encoder, LSTM, and intervention-interaction attention, with discrete or temporal decoders. |
| **Training** | Supervised intervention prediction with weighted cross-entropy for discrete states or focal loss for hourly probabilities. |
| **Data / cohorts** | 23,926 MIMIC-IV ICU admissions for development and internal testing; 12,603 AmsterdamUMCdb admissions for external evaluation without retraining. |
| **Downstream tasks** | Forecasting seven ICU interventions over a six-hour window, cold-start prediction, and patient stratification. |
| **Modalities** | ICU physiology, interventions |
| **Evidence** | Retrospective external validation. Targets are recorded clinician interventions; the model does not estimate counterfactual treatment benefit. |
| **Code / resources** | [Archived implementation](https://doi.org/10.5281/zenodo.19609882) |

</details>

<a id="model-hypoglycemia-lstm-202606"></a>
<details>
<summary><b>Hypoglycemia LSTM</b> — 24-hour inpatient hypoglycemia risk, updated every four hours <i>(npj Digit. Med. 2026-06)</i></summary>

**[Development and prospective evaluation of a real-time deep learning model for inpatient hypoglycemia prediction](https://doi.org/10.1038/s41746-026-02874-1)**

*npj Digit. Med.* · 2026-06 · Amanda Momenzadeh & Jesse G. Meyer · [doi:10.1038/s41746-026-02874-1](https://doi.org/10.1038/s41746-026-02874-1)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Parallel LSTM branches for longitudinal inputs plus a dense branch for static features. |
| **Training** | Supervised binary classification using five-day histories in four-hour bins. |
| **Data / cohorts** | 143,124 admissions across three hospitals, with retrospective development and prospective daily evaluation using live EHR extracts. |
| **Downstream tasks** | Hypoglycemia within 24 hours, with predictions refreshed every four hours. |
| **Modalities** | EHR, glucose, medications, labs |
| **Evidence** | Prospective prediction validation; no intervention effect on patient outcomes was tested. |
| **Code / resources** | [Hypoglycemia-DL](https://github.com/xomicsdatascience/Hypoglycemia-DL) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Hypoglycemia prediction | AUPRC; F1 | 0.23; 0.30 | F1 at threshold 0.7; precision 0.23, recall 0.44 |

</details>

<a id="model-sepsis-trajectory-202603"></a>
<details>
<summary><b>Sepsis trajectory ensemble</b> — Machine learning predicts sepsis deterioration trajectories <i>(npj Digit. Med. 2026-03)</i></summary>

**[Machine learning predicts sepsis deterioration trajectories](https://www.nature.com/articles/s41746-026-02565-x)**

*npj Digit. Med.* · 2026-03 · Rui Zhang & Hongping Qu · [doi:10.1038/s41746-026-02565-x](https://doi.org/10.1038/s41746-026-02565-x)

| | |
| --- | --- |
| **Parameters** | Not reported for the mixed ensemble, which includes a deep learning component |
| **Backbone** | Group-Based Trajectory Modeling for label derivation, combined with a random forest, gradient boosting, and deep learning ensemble |
| **Training** | `supervised`<br>Supervised ensemble learning after trajectory-based label derivation; no separate pretraining stage. |
| **Data / cohorts** | Ruijin Hospital development and internal validation cohorts plus external MIMIC-III and eICU<br>**2,843** development (2012-2019) · **1,213** internal validation (2020-2021) · **25,633** MIMIC-III · **18,247** eICU · **47,936** patients total |
| **Downstream tasks** | `trajectory classification`, `deterioration prediction`, `timing`<br>Three-class trajectory classification (rapid recovery, slow recovery, deterioration), binary deterioration, and deterioration timing. |
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
| **Training** | `supervised`<br>Supervised LSTM learning with 5-fold stratified patient-level cross-validation and class-balance resampling. |
| **Data / cohorts** | Non-ICU inpatients on VitalPatch biosensors at Northwell, Mar 2020-Nov 2022, plus prospective second-hospital and alternate-device external validation<br>**888** patients · **2,897** patient-days |
| **Downstream tasks** | `clinical alert prediction`, `deterioration prediction`<br>MEWS>6 clinical-alert prediction and 24-hour hard outcomes covering ICU transfer, rapid-response call, intubation, cardiac arrest, and death. |
| **Modalities** | `continuous vitals`, `demographics` |
| **Code** | [codeocean.com/capsule/9888403](https://codeocean.com/capsule/9888403/tree) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Deterioration prediction | ROC-AUC | 0.89 ± 0.03 | PR-AUC 0.58 ± 0.14 |
| Intubations, cardiac arrests, and deaths | detection rate | 100% | |
| Unplanned ICU transfers | detection rate | 83.6% | |
| Rapid-response calls | detection rate | 50% | lead time up to 17 h |

</details>

<a id="model-concern-202504"></a>
<details>
<summary><b>CONCERN</b> — hourly deterioration alerts and clinical surveillance <i>(Nat. Med. 2025-04)</i></summary>

**[Real-time surveillance system for patient deterioration: a pragmatic cluster-randomized controlled trial](https://doi.org/10.1038/s41591-025-03609-7)**

*Nat. Med.* · 2025-04 · [Sarah C. Rossetti](https://orcid.org/0000-0003-2632-8867) & Kenrick D. Cato · [doi:10.1038/s41591-025-03609-7](https://doi.org/10.1038/s41591-025-03609-7)

| | |
| --- | --- |
| **Parameters** | Not reported |
| **Backbone** | Ensemble early-warning system uses nursing-documentation patterns to update 24-hour deterioration risk hourly. |
| **Training** | Supervised ensemble learning on retrospective hospital encounters, followed by a separate clinical implementation trial. |
| **Data / cohorts** | Cluster-randomized trial: 60,893 encounters across 74 units in two health systems; 33,024 intervention and 27,869 usual-care encounters. |
| **Downstream tasks** | Clinical deterioration surveillance with risk displays for care teams. |
| **Modalities** | nursing documentation, EHR |
| **Evidence** | Pragmatic cluster-randomized trial of access to the system. |
| **Code / resources** | SAS trial-analysis code is available on request under the authors’ access conditions. The prediction algorithm is proprietary and is not shared. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| In-hospital mortality, intervention versus usual care | adjusted hazard ratio | 0.64 (95% CI 0.53–0.78) | Trial of the clinical workflow |

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
| **Training** | `supervised elastic net`<br>Supervised elastic net with 25-fold cross-validation for lambda selection. |
| **Data / cohorts** | MGB Biobank for EMRAge and MGB-ABC for the omics clocks, with validation in All of Us, TruDiagnostic Biobank, and Generation Scotland<br>**31,264** MGB Biobank · **3,451** MGB-ABC · **10,769** All of Us · **14,213** TruDiagnostic · **18,672** Generation Scotland |
| **Downstream tasks** | `mortality prediction`, `incident disease`, `prevalent disease`, `lifestyle association`<br>All-cause mortality, incident and prevalent stroke, type 2 diabetes, COPD, depression, CVD, and cancer, and lifestyle-factor associations. |
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
| **Training** | `self-supervised`<br>Self-supervised learning combining mask reconstruction, cohort discrimination, missing-data discrimination, and next-visit prediction. |
| **Data / cohorts** | Longitudinal clinical visits, with external validation on UK Biobank<br>**24,633,025** clinical visits · **9,680,764** individuals |
| **Downstream tasks** | `biological age`, `age gap`, `disease risk`<br>Biological age prediction across the lifespan, age-gap estimation, and current plus future disease risk prediction. |
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
| **Training** | `self-supervised contrastive`<br>Self-supervised contrastive learning on unlabeled wearable PPG. |
| **Data / cohorts** | Apple Heart & Movement Study<br>**19,993,427** PPG segments · **172,318** pretraining participants · **6,728** healthy participants for the age head · **120,235** validation participants |
| **Downstream tasks** | `age regression`, `disease risk`, `behavior association`, `longitudinal change detection`<br>Chronological-age prediction, age-gap to disease risk for ASCVD, hypertension, diabetes, and hyperlipidemia, behavior associations, and longitudinal change detection. |
| **Modalities** | `PPG` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Chronological age, healthy participants | MAE | 2.42-2.45 years | |
| Chronological age, general population | MAE | 3.13-3.26 years | |
| ASCVD | hazard ratio per 6-year age gap | 1.464 (1.36-1.57) | |
| Hypertension | hazard ratio per 6-year age gap | 1.620 (1.51-1.74) | |

</details>
