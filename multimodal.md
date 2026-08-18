# Multimodal AI

Cross-modal health models without a single dominant biomedical domain.

**Maintainer:** @Yeonwoo Seo ([Homepage](https://yws0322.github.io/) / [LinkedIn](https://www.linkedin.com/in/yeonwoo-seo-8950372bb/) / [GitHub](https://github.com/yws0322))

**19 entries** · **Last updated: 202608** · [Back to index](README.md)

## Paper overview

Click a model name to jump to its expandable record. A dash (—) means the value has not been confirmed from the paper or an official release.

| Date | Model | Venue | Model Size | Modalities | Pre-training | Downstream Tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 202608 | [VirTues](#model-virtues-202608) | Nature | — | Multiplex spatial proteomics + protein sequence | self-supervised, masked autoencoding | reconstruction, cell typing, niche annotation, biomarker discovery +1 |
| 202607 | [PRISM2](#model-prism2-202607) | Nat. Med. | 4.6B | Histopathology + clinical text | contrastive, next-token prediction | detection, subtyping, grading +4 |
| 202607 | [RisQ](#model-risq-202607) | medRxiv | — | EHR/diagnoses + labs + lifestyle + genetics | N/A (supervised, no separate pretraining) | zero-shot disease risk prediction |
| 202604 | [APOLLO](#model-apollo-202604) | arXiv | — | EHR (diagnoses, meds, labs, notes) + pathology images | masked modeling | patient retrieval, disease onset, progression +3 |
| 202602 | [MAOSS](#model-maoss-202602) | Nat. Commun. | — | Non-contrast CT + demographics + labs | — | steatosis grading, fibrosis detection, cirrhosis risk |
| 202601 | [Emu3](#model-emu3-202601) | Nature | 8.49B | Text + image + video | next-token prediction, autoregressive | image gen, video gen, vision-language understanding |
| 202512 | [GigaTIME](#model-gigatime-202512) | Cell | — | H&E histopathology → multiplex immunofluorescence | supervised, cross-modal translation | H&E-to-mIF translation, biomarker discovery, stratification |
| 202512 | [SurvPGC](#model-survpgc-202512) | npj Digit. Med. | — | Histopathology + transcriptomics + clinical text | frozen foundation encoders, supervised fusion | pan-cancer survival prediction |
| 202512 | [PathGen](#model-pathgen-202512) | Nat. Commun. | — | Histopathology to gene-expression generation | diffusion-based generative, conditioned on WSI embeddings | grading, subtyping, survival prediction |
| 202511 | [GlioSurv](#model-gliosurv-202511) | npj Digit. Med. | — | Multiparametric MRI + clinical + molecular markers | self-supervised (imaging), frozen (clinical) | survival prediction, risk stratification |
| 202510 | [MRI-PTPCa](#model-mri-ptpca-202510) | Nat. Cancer | — | Multiparametric MRI + histopathology | contrastive | diagnosis, Gleason grading |
| 202509 | [PROGPath](#model-progpath-202509) | Signal Transduct. Target. Ther. | — | Histopathology + clinical variables | self-supervised (patch encoder), weakly supervised (fusion) | pan-cancer survival prediction |
| 202508 | [AD Biomarker Fusion](#model-ad-biomarker-fusion-202508) | Nat. Commun. | — | Demographics + history + biomarkers + structural MRI | supervised, two-stage | amyloid/tau PET-status classification |
| 202507 | [LUCID](#model-lucid-202507) | Cell Rep. Med. | ~632M | CT + chief complaints (text) + labs + demographics | supervised, two-stage | EGFR mutation prediction, survival prediction |
| 202507 | [TRIBE](#model-tribe-202507) | arXiv | ~1B | Video + audio + text | frozen encoders, supervised fusion | whole-brain fMRI response prediction |
| 202505 | [MDLM](#model-mdlm-202505) | npj Digit. Med. | — | CT + histopathology + clinical features | supervised (ImageNet), supervised fusion | survival prediction, radiotherapy stratification |
| 202503 | [Orpheus](#model-orpheus-202503) | Nat. Commun. | — | Histopathology + pathology text reports | self-supervised (tiles), supervised regression | recurrence-score regression, risk stratification |
| 202502 | [Renal CT-Pathology AI](#model-renal-ct-pathology-202502) | Nat. Commun. | — | Pre-operative CT + linked pathology/outcome labels | supervised, segmentation pretraining | malignancy prediction, aggressiveness prediction |
| 202408 | [MuMo](#model-mumo-202408) | Signal Transduct. Target. Ther. | — | CT + histopathology (HER2 IHC) + clinical reports | supervised, pretrained segmentation preprocessing | treatment response prediction |

## Details

Click a model to expand its record.

<a id="model-virtues-202608"></a>
<details>
<summary><b>VirTues</b> — The Virtual Tissues foundation model resolves spatial proteomics across scales <i>(Nature 202608)</i></summary>

**[The Virtual Tissues foundation model resolves spatial proteomics across scales](https://doi.org/10.1038/s41586-026-10884-y)**

*Nature* · 202608 · [Johann Wenckstern](https://scholar.google.com/citations?user=3FAQWrAAAAAJ&hl=de) & [Charlotte Bunne](https://scholar.google.com/citations?user=U80atIAAAAAJ&hl=en) · [doi:10.1038/s41586-026-10884-y](https://doi.org/10.1038/s41586-026-10884-y)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Vision Transformer variant with a tokenization scheme fusing spatial image-patch tokens and marker tokens (marker identity embedded via the ESM-2 protein language model, esm2_t30_150M_UR50D), plus patch/cell/niche/tissue summary tokens |
| **Pre-training** | self-supervised, masked autoencoding<br>Random per-marker-channel and per-patch token masking with a reconstruction objective; marker identity is injected by adding ESM-2 protein-language-model embeddings to the corresponding image tokens, letting one model generalize across different antibody panels. |
| **Training data** | The "spora" dataset — described as the largest open spatial-proteomics dataset to date<br>**12,000+** multiplex images · **5,000+** patients · **31** clinical cohorts |
| **Downstream tasks** | reconstruction, cell typing, niche annotation, biomarker discovery, patient stratification<br>Marker reconstruction/inpainting, cell typing and segmentation, niche annotation, zero-shot cross-panel annotation (generalizing to marker panels not seen in training), spatial biomarker discovery, and patient stratification. |
| **Modalities** | multiplex spatial proteomics imaging (imaging mass cytometry-type, multi-channel protein marker maps), protein sequence |
| **Code** | [github.com/bunnelab/virtues](https://github.com/bunnelab/virtues) |
| **Weights** | [huggingface.co/bunnelab/virtues](https://huggingface.co/bunnelab/virtues) (variants virtues-sp32, virtues-sp31, virtues-imc14) |
| **License** | Mixed MIT / CC-BY-NC-4.0, depending on weight variant |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| NeoTRIP cohort (TNBC), anti-PD-L1 immunotherapy response | AUROC | 0.817 |  |
| Disease-free survival stratification | C-index | 0.628 | vs. 0.606 for the comparison baseline |
| Held-out marker channel reconstruction | Pearson r | 0.723 ± 0.157 |  |

</details>

<a id="model-prism2-202607"></a>
<details>
<summary><b>PRISM2</b> — End-to-end multimodal pathology foundation model with clinical dialogue <i>(Nat. Med. 202607)</i></summary>

**[End-to-end multimodal pathology foundation model with clinical dialogue](https://doi.org/10.1038/s41591-026-04521-4)**

*Nat. Med.* · 202607 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ) & [Siqi Liu](https://scholar.google.com/citations?user=ADyo_cAAAAAJ) · [doi:10.1038/s41591-026-04521-4](https://doi.org/10.1038/s41591-026-04521-4)

| | |
| --- | --- |
| **Parameters** | 4.6B |
| **Backbone** | Virchow2 tile encoder, Perceiver slide encoder (541M, plus a 79M attention pooler), BioGPT language encoder and a Phi-3 Mini 3.8B decoder-only LLM reached through a 29M-parameter MLP adapter |
| **Pre-training** | contrastive, next-token prediction<br>Two-stage language-supervised multimodal pre-training: contrastive slide-report alignment against BioGPT text embeddings plus an autoregressive dialogue objective, then a second stage in which the contrastive objective is dropped, the slide encoder is frozen and Phi-3 Mini is fine-tuned end-to-end on the dialogue objective alone. |
| **Training data** | H&E whole-slide images with paired clinical reports, converted into question-answer pairs<br>**2,350,518** WSI · **685,507** specimens · **200,692** patients · **14,000,000** QA pairs |
| **Downstream tasks** | detection, subtyping, grading, biomarker prediction, survival prediction, question answering, report generation<br>Prompt-based cancer detection and subtyping via yes/no and multiple-choice question answering; diagnostic, biomarker and survival prediction by linear probing on the base and diagnostic embeddings; staging and grading on external public data; pathology report completion following CAP guidelines. |
| **Modalities** | histopathology, text |
| **Weights** | [huggingface.co/paige-ai/Prism2](https://huggingface.co/paige-ai/Prism2) |
| **License** | CC-BY-NC-ND-4.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MSK pan-cancer detection (linear probing) | AUC | 0.967 | diagnostic embedding; 0.956 with the base embedding, 0.947 with PRISM and 0.931 with TITAN. Drop on rare cancers is modest, 0.967 to 0.957. |
| MSK colorectal cancer recurrence-free survival | C-index | 0.809 | PRISM2 survival embeddings, versus 0.773 for a survival specialist model trained from scratch on the same 225,597-case dataset |
| CAMELYON17 tumour staging (external, five-fold) | quadratic weighted kappa | 0.888 / 0.881 | base / diagnostic embeddings, versus 0.852 for PRISM and 0.641 for TITAN |
| PANDA-SI prostate cancer grading (external) | quadratic weighted kappa | 0.862 | diagnostic embedding; 0.836 base, 0.841 PRISM, 0.750 TITAN |
| Biomarker prediction, 10 MSK datasets (linear probing) | mean AUC | 0.854 | PRISM2 base embedding; next best is COBRA at 0.846. On overlapping TCGA biomarkers PRISM2 reaches 0.784 against 0.781 for TITAN. |

</details>

<a id="model-risq-202607"></a>
<details>
<summary><b>RisQ</b> — Learning the shared structure of human health across diseases, modalities, and time <i>(medRxiv 202607)</i></summary>

**[Learning the shared structure of human health across diseases, modalities, and time](https://doi.org/10.64898/2026.07.07.26357373)**

*medRxiv* · 202607 · [Paul Hager](https://scholar.google.com/citations?user=LeI7UOYAAAAJ&hl=en&oi=ao) & [Francesco Paolo Casale](https://scholar.google.com/citations?user=AUFp6j4AAAAJ&hl=en&oi=ao) · [doi:10.64898/2026.07.07.26357373](https://doi.org/10.64898/2026.07.07.26357373)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Transformer encoder producing a shared health representation, queried by a cross-attention decoder at chosen time horizons |
| **Pre-training** | N/A<br>Not built via self-supervised pretraining — the encoder-decoder is trained end-to-end via direct supervised disease-risk prediction across the full UK Biobank multimodal feature set, then evaluated zero-shot on disease chapters withheld from training. |
| **Training data** | UK Biobank participant records; external validation on All of Us<br>**488,170** UK Biobank participants · **257,538** All of Us participants |
| **Downstream tasks** | zero-shot risk prediction<br>Zero-shot disease-risk prediction across disease chapters not seen during training, benchmarked against demographic, disease-specific, multi-disease, and tabular foundation-model (XGBoost, TabPFN v3) baselines. |
| **Modalities** | diagnostic/EHR history, medications, labs/biomarkers, physical measurements, lifestyle, environmental exposures, genetics |
| **Code** | [github.com/RisQ-Lab/RisQ](https://github.com/RisQ-Lab/RisQ) (no pretrained weights released; using the pipeline requires a separate UK Biobank data-access agreement) |
| **License** | MIT |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Zero-shot, out-of-disease-chapter | C-index | 0.667 (95% CI 0.660–0.673) | vs. 0.632 (95% CI 0.625–0.639) demographic-only baseline; outperformed disease-specific models, multi-disease frameworks and tabular foundation models on both UK Biobank and the external All of Us cohort |

</details>

<a id="model-apollo-202604"></a>
<details>
<summary><b>APOLLO</b> — A multimodal and temporal foundation model for virtual patient representations at healthcare system scale <i>(arXiv 202604)</i></summary>

**[A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/pdf/2604.18570)**

*arXiv* · 202604 · [Andrew Zhang](https://scholar.google.com/citations?user=WDiKxmcAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Transformer |
| **Pre-training** | masked modeling<br>Masking-and-reconstruction (temporal masked-event modeling) over structured EHR events and clinical notes spanning 28 modalities, learning a shared patient representation without task-specific labels. |
| **Training data** | MGB-7M, a health-system-scale longitudinal EHR corpus<br>**7,155,044** patient records · **25,296,943,893** distinct medical events · 33 years · 17 institutions |
| **Downstream tasks** | patient retrieval, disease onset, disease progression, treatment response, adverse events, hospital operations<br>322 downstream tasks: patient retrieval (61 cohorts), new disease onset (95 tasks), disease progression (78 tasks), treatment response (59 tasks), drug adverse events (17 tasks), hospital operations endpoints (12 tasks). |
| **Modalities** | diagnoses (ICD-10), medications (RxNorm), labs (LOINC), vitals/flowsheets, clinical notes, pathology images (28 modalities total) |
| **Code** | Not found; MGB-7M is proprietary patient EHR data, so the model is likely closed |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| All-cause mortality | AUROC | 0.92 |  |
| Heart failure onset | AUROC | 0.88 | vs. 0.77 baseline |
| Type 2 diabetes onset | AUROC | 0.85 | vs. 0.61 baseline |
| Trastuzumab response, HER2+ breast cancer | AUROC | 0.93 | vs. 0.66 baseline |
| Disease-onset tasks (95 total) | tasks beating baseline | 74/95 | p < 0.05 |

</details>

<a id="model-maoss-202602"></a>
<details>
<summary><b>MAOSS</b> — Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease <i>(Nat. Commun. 202602)</i></summary>

**[Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease](https://doi.org/10.1038/s41467-026-68414-3)**

*Nature Communications* · 202602 · Yuan Gao & Yu Shi · [doi:10.1038/s41467-026-68414-3](https://doi.org/10.1038/s41467-026-68414-3)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Not disclosed in the paper or repository README |
| **Pre-training** | Not disclosed — the README and accessible text do not describe an architecture or training scheme in enough detail to characterize it. |
| **Training data** | Multi-cohort steatotic liver disease dataset with histology and radiology confirmation<br>**968** histology-confirmed cases · **1,103** radiology-confirmed cases · **660** histology validation · **375** MRI-PDFF validation · **1,192** deployment cohort |
| **Downstream tasks** | steatosis grading, fibrosis detection, cirrhosis risk<br>Steatosis detection/grading, clinically significant fibrosis detection, and cirrhosis progression risk stratification, deployed prospectively inside a clinical workflow. |
| **Modalities** | non-contrast CT (image features + liver/spleen volume and density biomarkers), demographics, labs |
| **Code** | [github.com/YGOX/MAOSS](https://github.com/YGOX/MAOSS) (no pretrained-weight download found; the repo's --model_path flag is a placeholder for a user's own checkpoints) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Steatosis grading | AUC | 0.904–0.929 |  |
| Clinically significant fibrosis | AUC | 0.824–0.888 |  |
| Deployment cohort (n=1,192) | additional at-risk patients identified | +36% | vs. standard workflow |

</details>

<a id="model-emu3-202601"></a>
<details>
<summary><b>Emu3</b> — Multimodal learning with next-token prediction for large multimodal models <i>(Nature 202601)</i></summary>

**[Multimodal learning with next-token prediction for large multimodal models](https://www.nature.com/articles/s41586-025-10041-x)**

*Nature* · 202601 · [Xinlong Wang](https://scholar.google.com/citations?user=DPz0DjYAAAAJ) & [Tiejun Huang](https://scholar.google.com/citations?user=knvEK4AAAAAJ)

| | |
| --- | --- |
| **Parameters** | 8.49B (32 layers, hidden size 4096); 1.5B ablation variant |
| **Backbone** | Transformer, decoder-only |
| **Pre-training** | next-token prediction, autoregressive<br>A single decoder-only transformer trained purely by next-token prediction over text, image and video tokens unified into one discrete vocabulary — no separate contrastive or diffusion stage is used. |
| **Training data** | Large-scale multimodal corpus (~3PB) spanning text, images and video |
| **Downstream tasks** | image generation, video generation, vision-language understanding |
| **Modalities** | text, image, video |
| **Code** | [github.com/baaivision/Emu3](https://github.com/baaivision/Emu3) |
| **Weights** | Hugging Face / ModelScope |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Text-to-image (GenEval) | score | 70.0 | vs. SDXL 66.9 |
| Vision-language understanding (12 benchmarks) | average accuracy | 62.1 | vs. LLaVA-1.6 61.8 |
| Text-to-video (VBench) | score | 81.0 | vs. Open-Sora-1.2 79.8 |
| Robotic manipulation (CALVIN) | success rate | 87.0% (5-step) / 98.5% (1-step) |  |

</details>

<a id="model-gigatime-202512"></a>
<details>
<summary><b>GigaTIME</b> — Multimodal AI generates virtual population for tumor microenvironment modeling <i>(Cell 202512)</i></summary>

**[Multimodal AI generates virtual population for tumor microenvironment modeling](https://doi.org/10.1016/j.cell.2025.11.016)**

*Cell* · 202512 · [Jeya Maria Jose Valanarasu](https://scholar.google.com/citations?user=vphpzPYAAAAJ&hl=en) & [Hoifung Poon](https://scholar.google.com/citations?user=yqqmVbkAAAAJ&hl=en) · [doi:10.1016/j.cell.2025.11.016](https://doi.org/10.1016/j.cell.2025.11.016)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Built on the GigaPath / GigaPath-Flash pathology foundation model (transformer/ViT-based cross-modal translator) |
| **Pre-training** | supervised, cross-modal translation<br>Supervised image-to-image translation trained to predict 21-channel multiplex immunofluorescence (mIF) protein-activation maps directly from H&E whole-slide images, benchmarked against a CycleGAN baseline — not a self-supervised or contrastive scheme. |
| **Training data** | Paired H&E/mIF data from Providence Health, applied at scale to generate a large virtual mIF cohort<br>**~40,000,000** paired cells (21 protein channels) · **14,256** patients / 51 hospitals · **299,376** virtual mIF slides generated across 24 cancer types · external validation on **10,200** TCGA patients |
| **Downstream tasks** | H&E-to-mIF translation, biomarker discovery, patient stratification<br>H&E-to-mIF image translation, protein-biomarker discovery, patient stratification by stage/survival, and cross-cohort (TCGA) validation. |
| **Modalities** | H&E whole-slide pathology imaging → multiplex immunofluorescence (spatial protein data) |
| **Code** | [github.com/prov-gigatime/GigaTIME](https://github.com/prov-gigatime/GigaTIME) |
| **Weights** | Hugging Face (research-use only) |
| **License** | Apache-2.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Virtual protein prediction | vs. CycleGAN baseline | Outperformed on Dice/Pearson | exact values not confirmed in accessible text |
| Protein–biomarker–staging–survival associations | count | 1,234 significant associations |  |
| Cross-cohort validation (TCGA) | Spearman correlation | ≈0.88 |  |

</details>

<a id="model-survpgc-202512"></a>
<details>
<summary><b>SurvPGC</b> — Multimodal deep learning for cancer prognosis prediction with clinical information prompts integration <i>(npj Digit. Med. 202512)</i></summary>

**[Multimodal deep learning for cancer prognosis prediction with clinical information prompts integration](https://doi.org/10.1038/s41746-025-02257-y)**

*npj Digital Medicine* · 202512 · Jiaxin Hou & [Wenjian Qin](https://scholar.google.com/citations?user=QulpzUAAAAAJ&hl=en) · [doi:10.1038/s41746-025-02257-y](https://doi.org/10.1038/s41746-025-02257-y)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Per-modality foundation-model encoders (CONCH for clinical-text prompts, scFoundation for transcriptomics, UNI for WSI patches) combined through a dual-path cross-attention fusion module (clinical–pathology and genomic–pathology) |
| **Pre-training** | frozen foundation encoders, supervised fusion<br>The three per-modality encoders are used frozen from their own external pretraining (CONCH, scFoundation, UNI); only the dual cross-attention fusion module is trained, via a supervised survival loss on labeled TCGA cohorts — this paper performs no new self-supervised pretraining of its own. |
| **Training data** | TCGA cohorts, 5-fold cross-validation<br>TCGA-LIHC (n=354) · TCGA-BRCA (n=1,035) · TCGA-COADREAD (n=298) |
| **Downstream tasks** | survival prediction<br>Pan-cancer prognosis/survival prediction across three cancer types. |
| **Modalities** | histopathology (WSI), bulk transcriptomics, clinical data (converted to text prompts) |
| **Code** | [github.com/Houjiaxin123/SurvPGC](https://github.com/Houjiaxin123/SurvPGC) (no pretrained-weight download found; only a Baidu Pan link for visualization outputs) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| TCGA-LIHC | C-index | 0.701 |  |
| TCGA-BRCA | C-index | 0.701 |  |
| TCGA-COADREAD | C-index | 0.676 |  |

</details>

<a id="model-pathgen-202512"></a>
<details>
<summary><b>PathGen</b> — Generating crossmodal gene expression from cancer histopathology improves multimodal AI predictions <i>(Nat. Commun. 202512)</i></summary>

**[Generating crossmodal gene expression from cancer histopathology improves multimodal AI predictions](https://doi.org/10.1038/s41467-025-66961-9)**

*Nature Communications* · 202512 · Samiran Dey & [Tapabrata Chakraborti](https://scholar.google.com/citations?user=ZIBre_IAAAAJ&hl=en) · [doi:10.1038/s41467-025-66961-9](https://doi.org/10.1038/s41467-025-66961-9)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Diffusion model conditioned on patch-level whole-slide-image embeddings, built on the UNI pathology foundation-model encoder with an MCAT-style co-attention framework linking synthesized transcriptomic features back to spatial WSI regions |
| **Pre-training** | Diffusion-based generative training, conditioned on histopathology patch embeddings, to synthesize gene-expression values across biologically meaningful gene groups — a one-directional generation (histopathology to transcriptomics), not a bidirectional alignment; the pipeline adds conformal prediction for uncertainty/coverage guarantees on the generated expression values. |
| **Training data** | Public multimodal cancer cohorts spanning four cancer types<br>TCGA-GBM (glioblastoma) · TCGA-LGG (low-grade glioma) · TCGA-KIRC (renal) · CPTAC (uterine, breast) — exact patient/slide counts not disclosed in accessible sources |
| **Downstream tasks** | Cancer grading/subtyping and patient survival-risk prediction, using the synthesized transcriptomic features alongside WSIs, with conformal coverage guarantees and co-attention-based interpretability. |
| **Modalities** | histopathology (WSI) — generates gene expression/transcriptomics as an output modality |
| **Code** | [github.com/Samiran-Dey/PathGen](https://github.com/Samiran-Dey/PathGen) |
| **Weights** | Trained checkpoints linked via Google Drive in the repository README |
| **License** | CC-BY-NC-ND-4.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Grading/survival prediction, WSI + synthesized transcriptomics vs. WSI-only | significance | p < 0.05 | statistically significant improvement across all four cohorts |
| Synthesized vs. real transcriptomic-data predictions | significance | p > 0.05 | statistically indistinguishable across all four cohorts; exact AUC/C-index values not confirmed in accessible text |

</details>

<a id="model-gliosurv-202511"></a>
<details>
<summary><b>GlioSurv</b> — interpretable transformer for multimodal, individualized survival prediction in diffuse glioma <i>(npj Digit. Med. 202511)</i></summary>

**[GlioSurv: interpretable transformer for multimodal, individualized survival prediction in diffuse glioma](https://doi.org/10.1038/s41746-025-02018-x)**

*npj Digital Medicine* · 202511 · Junhyeok Lee & [Kyu Sung Choi](https://scholar.google.co.kr/citations?user=XYh6Z0gAAAAJ) · [doi:10.1038/s41746-025-02018-x](https://doi.org/10.1038/s41746-025-02018-x)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | ViT for imaging, BERT-style encoder for clinical/molecular data, modality-specific adaptors, cross-attention fusion, Weibull accelerated-failure-time survival head |
| **Pre-training** | self-supervised (imaging), frozen (clinical)<br>The ViT imaging encoder is self-supervised-pretrained on the internal development-cohort MRI volumes; the BERT-style clinical/molecular encoder is kept frozen; only the cross-attention fusion module and survival head are trained on labeled outcomes. |
| **Training data** | Internal and multi-institutional external glioma cohorts<br>**1,944** patients total: 713 internal dev · 178 internal val · 84 external (SNUH) · 470 (UCSF) · 499 (UPenn) |
| **Downstream tasks** | survival prediction, risk stratification, prognostic factor attribution<br>Individualized survival prediction, risk stratification, and attribution of prognostic factors. |
| **Modalities** | multiparametric MRI (T1, post-contrast T1, T2, FLAIR), clinical variables, molecular markers (IDH, 1p/19q, MGMTp), treatment data |
| **Code** | [github.com/snuh-rad-aicon/GlioSurv](https://github.com/snuh-rad-aicon/GlioSurv) |
| **Weights** | [Official pretrained checkpoints](https://github.com/snuh-rad-aicon/GlioSurv/releases) released publicly as GitHub Release v1.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Internal/external cohorts | C-index | 0.61–0.80 |  |
| Internal/external cohorts | IAUC | 0.68–0.86 |  |
| Internal/external cohorts | IBS | 0.10–0.21 |  |
| vs. CNN / ViT / non-imaging multimodal transformer baselines | significance | p < 0.01 | GlioSurv outperformed all baselines |

</details>

<a id="model-mri-ptpca-202510"></a>
<details>
<summary><b>MRI-PTPCa</b> — An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer <i>(Nat. Cancer 202510)</i></summary>

**[An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer](https://doi.org/10.1038/s43018-025-01041-x)**

*Nature Cancer* · 202510 · Lizhi Shao & Shancheng Ren · [doi:10.1038/s43018-025-01041-x](https://doi.org/10.1038/s43018-025-01041-x)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Contrastive multiparametric-MRI encoder plus a multi-input Vision Transformer under multi-task supervision |
| **Pre-training** | contrastive<br>Contrastive learning directly on ~1.3M paired MRI–pathology images, aligning MRI regions with their corresponding histopathology, followed by multi-task supervised fine-tuning for diagnosis and grading. |
| **Training data** | Discovery, modeling, external and prospective cohorts<br>**~1,300,000** image–pathology pairs · **>5,500** patients |
| **Downstream tasks** | diagnosis, grading<br>Prostate cancer diagnosis (non-PCa / PCa / non-clinically-significant / clinically-significant) and Gleason Grade Group grading. |
| **Modalities** | multiparametric MRI, histopathology |
| **Code** | [github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer](https://github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer) (README states pretrained-weight release as a goal; no download link or release exists yet) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Diagnosis | AUC | >0.978 |  |
| Gleason Grade Group grading | accuracy | 89.1% |  |

</details>

<a id="model-progpath-202509"></a>
<details>
<summary><b>PROGPath</b> — Pancancer outcome prediction via a unified weakly supervised deep learning model <i>(Signal Transduct. Target. Ther. 202509)</i></summary>

**[Pancancer outcome prediction via a unified weakly supervised deep learning model](https://doi.org/10.1038/s41392-025-02374-w)**

*Signal Transduction and Targeted Therapy* · 202509 · Wei Yuan & [Anant Madabhushi](https://scholar.google.com/citations?user=deMrrCkAAAAJ) · [doi:10.1038/s41392-025-02374-w](https://doi.org/10.1038/s41392-025-02374-w)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Virchow2 (ViT) patch features aggregated via attention-guided multiple-instance learning (AMIL), fused with clinical data through a cross-attention transformer and a mixture-of-experts cancer-aware router |
| **Pre-training** | self-supervised (patch encoder), weakly supervised (fusion)<br>The Virchow2 patch encoder is used via its own externally pretrained self-supervised weights, frozen; PROGPath's own AMIL fusion module and MoE router are trained via a weakly supervised survival loss using only slide-level outcome labels, with no patch-level annotation. |
| **Training data** | TCGA plus a large external validation panel<br>**7,999** WSIs / **6,670** patients (TCGA, 15 cancer types) · external: **7,374** WSIs / **4,441** patients across 17 cohorts |
| **Downstream tasks** | survival prediction<br>Pan-cancer overall survival prediction. |
| **Modalities** | histopathology (WSI), structured clinical variables |
| **Code** | [github.com/Valeyards/ProgPath](https://github.com/Valeyards/ProgPath) |
| **Weights** | Released via linked Google Drive |
| **License** | CC-BY-NC-SA-4.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| TCGA | C-index | 0.731 | +5.3% over a histology-only variant |
| External cohorts | vs. MCAT, MOTCAT, SurvPath | Outperformed |  |

</details>

<a id="model-ad-biomarker-fusion-202508"></a>
<details>
<summary><b>AD Biomarker Fusion</b> — AI-driven fusion of multimodal data for Alzheimer's disease biomarker assessment <i>(Nat. Commun. 202508)</i></summary>

**[AI-driven fusion of multimodal data for Alzheimer's disease biomarker assessment](https://doi.org/10.1038/s41467-025-62590-4)**

*Nature Communications* · 202508 · [Varuna H. Jasodanand](https://scholar.google.com/citations?user=VZwxdNQAAAAJ&hl=en) & [Vijaya B. Kolachalama](https://scholar.google.com/citations?user=YgjYrrcAAAAJ&hl=en) · [doi:10.1038/s41467-025-62590-4](https://doi.org/10.1038/s41467-025-62590-4)

| | |
| --- | --- |
| **Model** | No single model name stated |
| **Parameters** | Not disclosed |
| **Backbone** | Transformer with attention-based fusion and random feature masking for missing modalities; Swin UNETR for structural-MRI feature extraction |
| **Pre-training** | supervised, two-stage<br>Stage 1 classifies amyloid-β / meta-tau PET-positivity directly from demographics, medical history, medications, fluid biomarkers, neuropsychological scores and structural MRI; stage 2 predicts regional tau status. Random feature masking during training lets the model handle missing modalities at inference. |
| **Training data** | 7 cohorts spanning training and external test sets<br>**12,185** patients (NACC, OASIS3, A4, AIBL, FHS for training; ADNI, HABS, NACC-subset for testing) |
| **Downstream tasks** | PET-status classification<br>Amyloid-β / tau PET-positivity classification from non-PET data. |
| **Modalities** | demographics, medical history, medications, fluid biomarkers, neuropsychological assessments, structural MRI |
| **Code** | [github.com/vkola-lab/ncomms2025](https://github.com/vkola-lab/ncomms2025) (interactive demo on Hugging Face Spaces; no downloadable checkpoint file confirmed) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Amyloid-β status | AUROC | 0.79 |  |
| Tau meta-temporal status | AUROC | 0.84 |  |

</details>

<a id="model-lucid-202507"></a>
<details>
<summary><b>LUCID</b> — AI-enabled molecular phenotyping and prognostic predictions in lung cancer through multimodal clinical information integration <i>(Cell Rep. Med. 202507)</i></summary>

**[AI-enabled molecular phenotyping and prognostic predictions in lung cancer through multimodal clinical information integration](https://doi.org/10.1016/j.xcrm.2025.102216)**

*Cell Reports Medicine* · 202507 · Yuxing Lu & Xiaoying Huang · [doi:10.1016/j.xcrm.2025.102216](https://doi.org/10.1016/j.xcrm.2025.102216)

| | |
| --- | --- |
| **Parameters** | ~632M (ViT-h stage) |
| **Backbone** | Two-stage: ViT-h image encoder (Stage 1) plus a cross-attention transformer fusing CT, text, labs and demographics (Stage 2) |
| **Pre-training** | supervised, two-stage<br>Stage 1 fine-tunes ViT-h on CT images directly against EGFR-mutation and survival labels; Stage 2 adds the cross-attention transformer that fuses the Stage-1 CT embedding with free-text chief complaints, lab results and demographics, trained end-to-end with AdamW over 50 epochs with cosine-annealing LR across 5 random seeds. Fully supervised throughout, with no self-supervised or contrastive stage. |
| **Training data** | West China Hospital cohort with external validation<br>**5,175** patients (West China Hospital) · **1,285** patients (external, Sun Yat-sen Memorial Hospital) |
| **Downstream tasks** | EGFR mutation prediction, survival prediction |
| **Modalities** | CT images, free-text chief complaints, laboratory results, demographics |
| **Code** | [github.com/YuxingLu613/LUCID](https://github.com/YuxingLu613/LUCID) (README is a stub; no weights released, data available on reasonable request only) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| EGFR mutation prediction | AUC | 0.851–0.881 |  |
| Survival prediction | AUC | 0.821–0.912 | varying time horizons |
| External validation | AUC | 0.876 |  |

</details>

<a id="model-tribe-202507"></a>
<details>
<summary><b>TRIBE</b> — TRImodal Brain Encoder for whole-brain fMRI response prediction <i>(arXiv 202507)</i></summary>

**[TRIBE: TRImodal Brain Encoder for whole-brain fMRI response prediction](https://arxiv.org/abs/2507.22229)**

*arXiv* · 202507 · Stéphane d'Ascoli & [Jean-Rémi King](https://scholar.google.com/citations?user=XZOgIwEAAAAJ)

| | |
| --- | --- |
| **Parameters** | ~1B (unconfirmed) |
| **Backbone** | Transformer fusing three frozen pretrained foundation encoders — Llama-3.2 (text), V-JEPA 2 (video), Wav2Vec-BERT (audio) |
| **Pre-training** | frozen encoders, supervised fusion<br>The three backbone encoders (Llama-3.2, V-JEPA 2, Wav2Vec-BERT) are used frozen from their own independent pretraining; only TRIBE's fusion transformer is trained, via supervised regression against recorded whole-brain (1000-parcel) fMRI BOLD signal — this paper performs no new self-supervised pretraining. |
| **Training data** | Courtois NeuroMod dataset<br>fMRI recordings across ~700 individuals |
| **Downstream tasks** | fMRI response prediction<br>Whole-brain (1000-parcel) fMRI response prediction to naturalistic video/audio/text stimuli — the Algonauts 2025 competition benchmark. |
| **Modalities** | video, audio, text (dialogue transcript) |
| **Code** | [github.com/facebookresearch/algonauts-2025](https://github.com/facebookresearch/algonauts-2025) (no weights released for TRIBE's own fusion transformer; only its external Llama-3.2 dependency is on Hugging Face) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Algonauts 2025 competition | rank | 1st place |  |
| Whole-brain response prediction | mean Pearson r | ≈0.215 | averaged across subjects |

</details>

<a id="model-mdlm-202505"></a>
<details>
<summary><b>MDLM</b> — Multimodal fusion model for prognostic prediction and radiotherapy response assessment in head and neck squamous cell carcinoma <i>(npj Digit. Med. 202505)</i></summary>

**[Multimodal fusion model for prognostic prediction and radiotherapy response assessment in head and neck squamous cell carcinoma](https://doi.org/10.1038/s41746-025-01712-0)**

*npj Digital Medicine* · 202505 · Ruxian Tian & Xicheng Song · [doi:10.1038/s41746-025-01712-0](https://doi.org/10.1038/s41746-025-01712-0)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | 3D-ResNet50 for CT, ResNet50 with attention-based multiple-instance learning for WSI |
| **Pre-training** | supervised (ImageNet), supervised fusion<br>Both ResNet50 branches are ImageNet-pretrained (standard supervised image classification, not self-supervised); the CT+WSI fusion head is then trained end-to-end via a supervised overall-survival / disease-free-survival loss on the labeled HNSCC cohort. |
| **Training data** | Multi-center China cohort plus a public external set<br>**1,087** HNSCC patients (multi-center China) · **56** patients (TCIA, external) |
| **Downstream tasks** | survival prediction, radiotherapy benefit stratification |
| **Modalities** | contrast-enhanced CT, histopathology (WSI), clinical features |
| **Code** | [github.com/yyyhd/MDLM](https://github.com/yyyhd/MDLM) (bare repo, no README/documentation as of check; no weights found) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Internal test, overall survival | C-index | 0.745 |  |
| Internal test, disease-free survival | C-index | 0.741 |  |
| External cohorts | C-index | 0.674–0.747 |  |
| High-risk group | postoperative radiotherapy benefit | Prolonged OS | vs. no significant benefit in the low-risk group |

</details>

<a id="model-orpheus-202503"></a>
<details>
<summary><b>Orpheus</b> — Multimodal histopathologic models stratify hormone receptor-positive early breast cancer <i>(Nat. Commun. 202503)</i></summary>

**[Multimodal histopathologic models stratify hormone receptor-positive early breast cancer](https://doi.org/10.1038/s41467-025-57283-x)**

*Nature Communications* · 202503 · [Kevin M. Boehm](https://scholar.google.com/citations?user=3t7ftQwAAAAJ&hl=en) & [Jakob Nikolas Kather](https://scholar.google.com/citations?user=w6-uFdEAAAAJ&hl=en) · [doi:10.1038/s41467-025-57283-x](https://doi.org/10.1038/s41467-025-57283-x)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | CTransPath (Swin Transformer) tile encoder plus a transformer text encoder, combined via tensor fusion into a transformer regression head |
| **Pre-training** | self-supervised (tiles), supervised regression<br>The CTransPath tile encoder is used via its own externally self-supervised pretraining; Orpheus's own tensor-fusion and regression head are trained supervised, directly regressing the Oncotype DX Recurrence Score from paired WSI tiles and synoptic pathology-report text. |
| **Training data** | Three-institution cohort with two external validation sets<br>**6,172–6,203** cases across 3 institutions · external: **452** and **575** cases |
| **Downstream tasks** | recurrence-score regression, high-risk classification, recurrence risk stratification |
| **Modalities** | histopathology (WSI), synoptic pathology text reports |
| **Code** | [github.com/kmboehm/orpheus](https://github.com/kmboehm/orpheus) (checkpoints saved during training are local training outputs only; no pretrained weights released) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Recurrence-score regression, combined modality | Pearson r | 0.68 | vs. 0.63 WSI-only, 0.58 text-only |
| High-risk detection (RS > 25) | AUROC | 0.89 | vs. 0.73 clinicopathologic nomogram; AUPRC 0.64 |
| RS ≤ 25 patients, metastatic recurrence | time-dependent AUC | 0.75 | vs. 0.49 for RS alone |

</details>

<a id="model-renal-ct-pathology-202502"></a>
<details>
<summary><b>Renal CT-Pathology AI</b> — Artificial intelligence links CT images to pathologic features and survival outcomes of renal masses <i>(Nat. Commun. 202502)</i></summary>

**[Artificial intelligence links CT images to pathologic features and survival outcomes of renal masses](https://doi.org/10.1038/s41467-025-56784-z)**

*Nature Communications* · 202502 · Ying Xiong & [Shuo Wang](https://scholar.google.com/citations?user=mAhTSxcAAAAJ&hl=en) · [doi:10.1038/s41467-025-56784-z](https://doi.org/10.1038/s41467-025-56784-z)

| | |
| --- | --- |
| **Model** | No single model name stated |
| **Parameters** | Not disclosed |
| **Backbone** | Multi-view CNN (ResNet18) with intermediate feature fusion; nnU-Net for tumor segmentation |
| **Pre-training** | supervised, segmentation pretraining<br>The nnU-Net segmentation stage is pretrained supervised on the public KiTS renal-tumor segmentation dataset; the downstream malignancy and aggressiveness CNN classifiers are then trained supervised end-to-end on labeled CT–pathology–outcome triples, with no self-supervised or foundation-model-style pretraining. |
| **Training data** | Pre-operative CT cohort linked to pathology and outcome<br>**13,261** CT volumes · **4,557** patients |
| **Downstream tasks** | malignancy prediction, aggressiveness prediction |
| **Modalities** | multi-phase pre-operative CT, linked to pathology and survival/outcome labels |
| **Code** | [github.com/shuowang26/renal-mass-ai](https://github.com/shuowang26/renal-mass-ai) |
| **Weights** | Available on request, subject to a non-commercial research agreement (not a public download) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Malignancy prediction (prospective set) | AUC | 0.871 | beat the average of 7 radiologists |
| Aggressiveness prediction | AUC | 0.783 |  |

</details>

<a id="model-mumo-202408"></a>
<details>
<summary><b>MuMo</b> — Predicting gastric cancer response to anti-HER2 therapy or anti-HER2 combined immunotherapy based on multi-modal data <i>(Signal Transduct. Target. Ther. 202408)</i></summary>

**[Predicting gastric cancer response to anti-HER2 therapy or anti-HER2 combined immunotherapy based on multi-modal data](https://doi.org/10.1038/s41392-024-01932-y)**

*Signal Transduction and Targeted Therapy* · 202408 · Zifan Chen & Lin Shen · [doi:10.1038/s41392-024-01932-y](https://doi.org/10.1038/s41392-024-01932-y)

| | |
| --- | --- |
| **Parameters** | Not disclosed |
| **Backbone** | Transformer-based multimodal fusion; MnasNet for CT feature extraction |
| **Pre-training** | supervised, pretrained segmentation preprocessing<br>A pretrained lesion-segmentation model preprocesses the CT scans; the MnasNet CT encoder and transformer fusion model are then trained supervised end-to-end against treatment-response labels, with no self-supervised pretraining stage of their own. |
| **Training data** | Two treatment cohorts plus external validation<br>**429** HER2+ gastric cancer patients (2 cohorts) · **39** patients (external validation) |
| **Downstream tasks** | treatment response prediction, PFS/OS risk stratification |
| **Modalities** | CT (lesion-annotated), histopathology (HER2 IHC score), clinical/radiology/pathology reports |
| **Code** | [github.com/czifan/MuMo](https://github.com/czifan/MuMo) (bare repo, no README/documentation as of check; no weights found) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Anti-HER2 therapy response | AUC | 0.821 |  |
| Anti-HER2 + immunotherapy response | AUC | 0.914 |  |
| External validation | AUC | 0.884 |  |

</details>

---

## Curation notes

- Entries are ordered by publication month, newest first.
- Parameter counts are shown only when the paper or an official release states a value; architecture names are never converted into inferred parameter counts.
- The compact overview table is for discovery; expandable records hold full architecture, training, and reported-performance detail. Pre-training descriptions always spell out the actual training procedure — a bare "supervised" or "self-supervised" tag in the overview table is expanded to specifics in the corresponding record.
- Papers from conference proceedings (e.g. MICCAI) or IEEE venues are out of scope for this file — entries here are restricted to journal publications (Nature-family, Cell-family, npj, JCO, STTT, etc.) or their arXiv/medRxiv/bioRxiv preprints.
