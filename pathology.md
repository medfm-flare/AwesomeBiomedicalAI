<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from data/pathology.yaml in https://github.com/1nslyn/biomedical-ai-pipeline -->
<!-- Edits made here are overwritten by the next build. -->

# Pathology

Histopathology, whole-slide imaging and computational pathology.

**Maintainer:** [Leo Yin](https://shuolinyin.com) ([GitHub](https://github.com/1nslyn))

**15 entries** · [Back to index](README.md)

| Date | Model | Venue | Model size | Training slides | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.07 | [PRISM2](#model-prism2-202607) | Nat. Med. | 4.6B | 2.35M | contrastive → dialogue next-token | detection, subtyping, grading +4 |
| 2026.04 | [PRET](#model-pret-202604) | Nat. Cancer | _not published_ | none (training-free) | DINO ViT-S/8 encoder, then frozen | detection, subtyping, segmentation +1 |
| 2026.03 | [HistBiases](#model-histbiases-202603) | Nat. Biomed. Eng. | _n/a_ | not stated (8.2K patients) | frozen CTransPath + CLAM/SlideGraph | biomarker prediction, mutation prediction, benchmarking |
| 2026.02 | [Neuropath-AI](#model-neuropath-ai-202602) | Lancet Oncol. | _not published_ | 5.8K samples (not slides) | WSI → molecular inference → hierarchy | classification, mutation prediction, gene expression prediction |
| 2026.02 | [KEEP](#model-keep-202602) | Cancer Cell | 414M | none (tile–text pairs) | knowledge-graph metric + contrastive | segmentation, detection, subtyping +2 |
| 2026.02 | [CHAI](#model-chai-202602) | J. Clin. Oncol. | _not published_ | not stated (178 patients) | supervised histomorphologic screening | biomarker prediction, treatment response |
| 2025.11 | [TITAN](#model-titan-202511) | Nat. Med. | 48.5M (slide enc.) | 336K | iBOT → CoCa (3 stages) | classification, subtyping, retrieval +2 |
| 2025.11 | [SMMILe](#model-smmile-202511) | Nat. Cancer | 1.2M (MIL head) | 3.9K (cross-validated) | weakly supervised MIL, frozen encoder | classification, detection, subtyping +1 |
| 2025.01 | [MUSK](#model-musk-202501) | Nature | 675M | 33K | BEiT-3 MIM → contrastive | retrieval, visual question answering, classification +4 |
| 2024.09 | [CHIEF](#model-chief-202409) | Nature | _not published_ | 60.5K | CTransPath tiles → weakly supervised | classification, detection, subtyping +2 |
| 2024.07 | [Virchow](#model-virchow-202407) | Nat. Med. | 632M | 1.5M | DINOv2 | detection, biomarker prediction, classification |
| 2024.05 | [Prov-GigaPath](#model-prov-gigapath-202405) | Nature | 1B (tile enc.) | 171K | DINOv2 tiles → LongNet MAE slides | classification, subtyping, mutation prediction +1 |
| 2024.03 | [UNI](#model-uni-202403) | Nat. Med. | 307M | 100K | DINOv2 | segmentation, detection, grading +3 |
| 2024.03 | [CONCH](#model-conch-202403) | Nat. Med. | _not published_ | none (1.17M image–caption) | iBOT → CoCa | classification, retrieval, segmentation +1 |
| 2023.08 | [PLIP](#model-plip-202308) | Nat. Med. | _not published_ | none (208K image–text) | CLIP contrastive fine-tune | classification, retrieval |

<sub><b>Model size</b> is the count the authors publish, with the component it covers in brackets — a slide encoder and a tile encoder are not comparable. <i>not published</i> means the access routes were worked and no author source states one; <i>n/a</i> means the paper does not introduce a model. <b>Training slides</b> counts whole slides used for training, so a model trained on tiles or image–text pairs shows what it used instead.</sub>

## Details

Click a model to expand its record.

<a id="model-prism2-202607"></a>
<details>
<summary><b>PRISM2</b> — End-to-end multimodal pathology foundation model with clinical dialogue <i>(Nat. Med. 2026-07)</i></summary>

**[End-to-end multimodal pathology foundation model with clinical dialogue](https://www.nature.com/articles/s41591-026-04521-4)**

*Nat. Med.* · 2026-07 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ&hl=en) & [Siqi Liu](https://scholar.google.com/citations?hl=en&user=ADyo_cAAAAAJ) · [doi:10.1038/s41591-026-04521-4](https://doi.org/10.1038/s41591-026-04521-4)

| | |
| --- | --- |
| **Parameters** | 4.6B |
| **Backbone** | Virchow2 tile encoder, Perceiver slide encoder (541M, plus a 79M attention pooler), BioGPT language encoder and a Phi-3 Mini 3.8B decoder-only LLM reached through a 29M-parameter MLP adapter |
| **Pre-training** | `contrastive`, `next-token prediction`<br>Two-stage language-supervised multimodal pre-training: contrastive slide-report alignment against BioGPT text embeddings plus an autoregressive dialogue objective, then a second stage in which the contrastive objective is dropped, the slide encoder is frozen and Phi-3 Mini is fine-tuned. Trained on 56 A100 40GB GPUs in bf16. |
| **Training data** | H&E whole-slide images with paired clinical reports, converted into question-answer pairs<br>**2,350,518** WSI · **685,507** specimens · **200,692** patients · **14,000,000** QA pairs |
| **Downstream tasks** | `detection`, `subtyping`, `grading`, `biomarker prediction`, `survival prediction`, `question answering`, `report generation`<br>Prompt-based cancer detection and subtyping via yes/no and multiple-choice question answering; diagnostic, biomarker and survival prediction by linear probing on the base and diagnostic embeddings; staging and grading on external public data; pathology report completion following CAP guidelines. |
| **Modalities** | `histopathology`, `text` |
| **Weights** | [huggingface.co/paige-ai/Prism2](https://huggingface.co/paige-ai/Prism2) |
| **License** | CC-BY-NC-ND-4.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MSK pan-cancer detection (linear probing) | AUC | 0.967 | diagnostic embedding; 0.956 with the base embedding, 0.947 with PRISM and 0.931 with TITAN. Drop on rare cancers is modest, 0.967 to 0.957. |
| MSK colorectal cancer recurrence-free survival | C-index | 0.809 | PRISM2 survival embeddings, versus 0.773 for a survival specialist model trained from scratch on the same 225,597-case survival dataset |
| CAMELYON17 tumour staging (external, five-fold across source institutions) | quadratic weighted kappa | 0.888 / 0.881 | base / diagnostic embeddings, versus 0.852 for PRISM and 0.641 for TITAN |
| PANDA-SI prostate cancer grading (external, cross-institution transfer) | quadratic weighted kappa | 0.862 | diagnostic embedding; 0.836 base, 0.841 PRISM, 0.750 TITAN |
| Biomarker prediction, 10 tissue-specific MSK datasets (linear probing) | mean AUC | 0.854 | PRISM2 base embedding; next best is COBRA at 0.846. On the seven overlapping TCGA biomarkers PRISM2 base reaches 0.784 against 0.781 for TITAN. |

</details>

<a id="model-pret-202604"></a>
<details>
<summary><b>PRET</b> — PRET is a few-shot system for pan-cancer recognition without example training <i>(Nat. Cancer 2026-04)</i></summary>

**[PRET is a few-shot system for pan-cancer recognition without example training](https://www.nature.com/articles/s43018-026-01141-2)**

*Nat. Cancer* · 2026-04 · [Yi Li](https://scholar.google.com/citations?user=qGsK180AAAAJ&hl=en) & [Xiaomeng Li](https://scholar.google.com/citations?user=uVTzPpoAAAAJ&hl=en) · [doi:10.1038/s43018-026-01141-2](https://doi.org/10.1038/s43018-026-01141-2)

| | |
| --- | --- |
| **Backbone** | Default feature extractor is a DINO-pretrained ViT-S/8 pathology encoder; PRET adds an in-context tagger, in-context classifier, instance miner, attention aggregator and postprocessor |
| **Pre-training** | `DINO`, `self-supervised`<br>Training-free for downstream tasks; the feature extractor holds all model parameters and is never fine-tuned. The default encoder was pretrained self-supervised with DINO on unlabelled TCGA pathology images, and the framework also runs on UNI, GPFM, CONCH, TITAN, mSTAR and Prov-GigaPath. |
| **Training data** | No task-specific training images for PRET itself. Evaluated on 4,484 WSIs across 23 benchmarks. The paper does not state a numeric TCGA pretraining image count for the default encoder.<br>**4,484** WSI (eval) · **23** benchmarks |
| **Downstream tasks** | `detection`, `subtyping`, `segmentation`, `classification`<br>Cancer screening, cancer subtyping, tumour segmentation, lymph node metastasis detection. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/xmed-lab/PRET](https://github.com/xmed-lab/PRET) |
| **Weights** | [huggingface.co/yili7eli/PRET](https://huggingface.co/yili7eli/PRET) |
| **License** | Apache-2.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 23 international benchmarks (4,484 WSIs) | AUC | >97% | reached on 15 of the 23 benchmarks; PRET outperforms existing approaches across 20 tasks |
| 23 international benchmarks (4,484 WSIs) | maximum improvement over existing approaches | 36.76% | abstract does not state which metric the improvement is measured in |
| Lymph node metastasis detection, 8 slide examples | comparison against pathologists | outperforms 11 pathologists | abstract calls this clinical-grade diagnostic performance but gives no underlying AUC; the per-benchmark figures live in Figs. 4 and 5, which are behind the paywall |
| Pan-cancer screening and subtyping, 11 datasets, slide-label prompt, 8-shot | mean AUC | 93.8% (+-1.9) | Supplementary Table 2, mean over ESCC, PTC, CRC, GC, LC, BC, lymphoma, ESCA, SARC, RCC and NSCLC; best baselines MI-SimpleShot and KNN-Mean both reach 90.9% |

</details>

<a id="model-histbiases-202603"></a>
<details>
<summary><b>HistBiases</b> — Confounding factors and biases abound when predicting molecular biomarkers from histological images <i>(Nat. Biomed. Eng. 2026-03)</i></summary>

**[Confounding factors and biases abound when predicting molecular biomarkers from histological images](https://www.nature.com/articles/s41551-026-01616-8)**

*Nat. Biomed. Eng.* · 2026-03 · [Muhammad Dawood](https://scholar.google.com/citations?hl=en&user=a-szm64AAAAJ) & [Fayyaz ul Amir Afsar Minhas](https://scholar.google.com/citations?hl=en&user=cQ6eO_kAAAAJ) · [doi:10.1038/s41551-026-01616-8](https://doi.org/10.1038/s41551-026-01616-8)

| | |
| --- | --- |
| **Backbone** | Benchmarking study rather than a new model. Evaluates CLAM, SlideGraph-infinity and TITAN, with CTransPath and ShuffleNet patch encoders. |
| **Pre-training** | `self-supervised`, `weakly supervised`<br>CTransPath pretrained on histology via self-supervised learning, giving 768-dimensional patch features; ShuffleNet pretrained on ImageNet, giving 1,024-dimensional patch features; TITAN trained on 330,000 image-text pairs. |
| **Training data** | H&E WSIs from TCGA, METABRIC, MSK and DFCI. Weakly supervised models trained on TCGA and validated on CPTAC and ABCTB.<br>**8,221** patients |
| **Downstream tasks** | `biomarker prediction`, `mutation prediction`, `benchmarking`<br>Molecular biomarker and gene mutation prediction from WSIs, plus a confounding/stratification analysis against biomarker interdependency, grade and TMB. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/imuhdawood/HistBiases](https://github.com/imuhdawood/HistBiases) |
| **Note** | Benchmarking and bias study, not a new foundation model. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| TCGA-BRCA (cross-validation) and ABCTB (independent validation) | AUROC, ER status | 0.87 / 0.90 | CLAM with CTransPath features; the same models reach 0.79 / 0.78 for PR |
| TCGA-CRC, MSI status | AUROC, whole cohort vs stratified subgroups | 0.88 -> 0.72 | SlideGraph-infinity; 0.88 (0.873-0.886) over the whole cohort falls to 0.72 within both the hypermutated and the non-hypermutated subgroup |
| TCGA-BRCA, grade-only baseline | AUROC | ER 0.76, PR 0.70, TP53 0.75 | SVM on one-hot pathologist-assigned grade; the weakly supervised TP53 predictor reaches only 0.81, so the added value of the ML model is modest. ABCTB gives 0.79 for ER and 0.71 for PR. |
| TCGA-CRC, TP53 mutation stratified by tumour mutational burden | AUROC, whole cohort vs high-TMB subgroup | 0.717 -> 0.50 | 0.717 (0.711-0.722) over the cohort falls to chance in high-TMB cases; the BRAF predictor falls from 0.774 (0.764-0.785) to 0.65 in low-TMB cases |

</details>

<a id="model-neuropath-ai-202602"></a>
<details>
<summary><b>Neuropath-AI</b> — Classification accuracy of a hierarchical molecular inference-based deep-learning system for CNS tumour diagnosis: a multi-institutional, retrospective study <i>(Lancet Oncol. 2026-02)</i></summary>

**[Classification accuracy of a hierarchical molecular inference-based deep-learning system for CNS tumour diagnosis: a multi-institutional, retrospective study](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045%2825%2900661-8/abstract)**

*Lancet Oncol.* · 2026-02 · H. Lalchungnunga & Kenneth Aldape · [doi:10.1016/S1470-2045(25)00661-8](https://doi.org/10.1016/S1470-2045%2825%2900661-8)

| | |
| --- | --- |
| **Backbone** | Hierarchical molecular inference: deep-learning models predict DNA methylation and gene expression from H&E whole-slide images, and a hierarchical classifier maps those predictions to nine tumour families and 52 terminal CNS tumour types |
| **Pre-training** | `self-supervised`<br>WSI-pretrained encoder followed by molecular inference-based hierarchical classification. |
| **Training data** | Multi-institutional retrospective CNS tumour cohort. Training data from the NCI, the Children's Brain Tumor Network and the Digital Brain Tumour Atlas; test data from the NCI, Northwestern Medicine, UPMC and University College London, drawn from laboratory archives between May 17, 2024 and May 13, 2025.<br>**5,835** training samples · **5,516** test samples · **52** tumour types |
| **Downstream tasks** | `classification`, `mutation prediction`, `gene expression prediction`<br>CNS tumour family-level classification, 52 terminal CNS tumour types, IDH mutation prediction, inferred gene expression and DNA methylation. |
| **Modalities** | `histopathology` |
| **Weights** | [methylscape.ccr.cancer.gov](https://methylscape.ccr.cancer.gov/) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Multi-institutional CNS tumour test cohort (5,516 samples) | family-level sample coverage | 96% | family-level classifications reached in 5,299 of 5,516 samples |
| Multi-institutional CNS tumour test cohort (5,516 samples) | terminal-classification sample coverage | 87% | 4,772 samples reached a terminal classification at moderate confidence or better |
| Multi-institutional CNS tumour test cohort (4,772 covered samples) | top-1 prediction accuracy | 80% | 3,817 of 4,772 samples, 95% CI 79-81; balanced accuracy 66% (95% CI 63-70) |
| Multi-institutional CNS tumour test cohort (4,772 covered samples) | top-2 prediction accuracy | 86% | 4,103 of 4,772 samples, 95% CI 85-87; balanced accuracy 75% (95% CI 71-78) |

</details>

<a id="model-keep-202602"></a>
<details>
<summary><b>KEEP</b> — Knowledge-enhanced pretraining for vision-language pathology foundation model on cancer diagnosis <i>(Cancer Cell 2026-02)</i></summary>

**[Knowledge-enhanced pretraining for vision-language pathology foundation model on cancer diagnosis](https://www.cell.com/cancer-cell/fulltext/S1535-6108%2826%2900058-9)**

*Cancer Cell* · 2026-02 · Xiao Zhou & [Weidi Xie](https://scholar.google.com/citations?user=Vtrqj4gAAAAJ&hl=zh-CN) · [doi:10.1016/j.ccell.2026.01.019](https://doi.org/10.1016/j.ccell.2026.01.019)

| | |
| --- | --- |
| **Parameters** | 414M |
| **Parameter note** | 414M is the released checkpoint's own total, not a figure from the paper: the HuggingFace API reports safetensors total 414,210,816 for Astaxanthin/KEEP and the model page renders "Model size 0.4B params". It covers both towers (ViT-L/16 vision encoder plus the BERT-family text encoder) at F32. Neither the Cancer Cell abstract nor the arXiv preprint states a parameter count anywhere. |
| **Backbone** | ViT-L/16 vision encoder initialised from UNI, paired with a PubMedBERT text encoder initialised from a disease-knowledge encoder |
| **Pre-training** | `contrastive`<br>Knowledge-enhanced vision-language pretraining. A BERT-family knowledge encoder is first trained by metric learning over a disease knowledge graph, then used to align visual and textual representations within hierarchical semantic spaces, so alignment happens at the level of a semantic group rather than a single noisy image-text pair. |
| **Training data** | Pathology image-text pairs from OpenPath and Quilt-1M, reorganized into semantically structured groups aligned with disease ontology hierarchies<br>**143,000** groups · **11,454** diseases · **139,143** disease attributes |
| **Downstream tasks** | `segmentation`, `detection`, `subtyping`, `retrieval`, `classification`<br>Zero-shot slide-level cancer region segmentation, cancer detection and subtyping; tile-level cross-modal retrieval and zero-shot image classification. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/MAGIC-AI4Med/KEEP](https://github.com/MAGIC-AI4Med/KEEP) |
| **Weights** | [huggingface.co/Astaxanthin/KEEP](https://huggingface.co/Astaxanthin/KEEP) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Zero-shot cancer detection, 7 CPTAC cohorts | average sensitivity at 0.95 specificity | 0.898 | reported by the authors as 89.8% in the repository README |
| EBRAINS, zero-shot subtyping (30 rare brain cancer types) | balanced accuracy | 0.456 | next-best model CONCH 0.371 |
| AGGC22, zero-shot cancer region segmentation | DICE | 0.530 | next-best model CONCH 0.449; before post-processing |
| CAMELYON16, zero-shot cancer region segmentation | DICE | 0.361 | next-best model CONCH 0.292, a 6.9-point gap; the preprint states 6.8 points, so one of the two is rounded differently |

</details>

<a id="model-chai-202602"></a>
<details>
<summary><b>CHAI</b> — Development and validation of a computational histology artificial intelligence-powered predictive biomarker for selection of chemotherapy in advanced pancreatic cancer <i>(J. Clin. Oncol. 2026-02)</i></summary>

**[Development and validation of a computational histology artificial intelligence-powered predictive biomarker for selection of chemotherapy in advanced pancreatic cancer](https://ascopubs.org/doi/10.1200/JCO-25-02199)**

*J. Clin. Oncol.* · 2026-02 · [Andrew Hendifar](https://scholar.google.com/citations?hl=en&user=XwWT-TMAAAAJ) & [Jennifer J. Knox](https://scholar.google.com/citations?user=6aEaHzcAAAAJ&hl=en) · [doi:10.1200/JCO-25-02199](https://doi.org/10.1200/JCO-25-02199)

| | |
| --- | --- |
| **Backbone** | Not described in any reachable source; the abstract says only that the CHAI platform extracts quantitative histomorphologic features from whole-slide images |
| **Pre-training** | `supervised`<br>Histomorphologic features extracted from H&E whole-slide images of diagnostic biopsies were screened in a development cohort for association with differential time to next treatment or death between F-chemo- and G-chemo-treated patients; the resulting continuous score was dichotomised and the threshold locked before validation. |
| **Training data** | H&E-stained diagnostic biopsy whole-slide images from patients with advanced pancreatic ductal adenocarcinoma<br>**477** patients · **178** development patients · **299** validation patients |
| **Downstream tasks** | `biomarker prediction`, `treatment response`<br>Predicts which of two first-line chemotherapy backbones -- fluoropyrimidine-based (F-chemo) or gemcitabine-based (G-chemo) -- a patient will benefit from, reported as a binary F-pref or G-pref result. |
| **Modalities** | `histopathology` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Validation cohort (COMPASS + Know Your Tumor), F-pref patients | median overall survival | 14.4 vs 11.7 months | F-chemo vs G-chemo, n = 173, P = .003 |
| Validation cohort (COMPASS + Know Your Tumor), F-pref patients | median time to next treatment or death | 8.6 vs 7.5 months | F-chemo vs G-chemo, n = 173, P = .035 |
| Validation cohort (COMPASS + Know Your Tumor), G-pref patients | median time to next treatment or death | 9.6 vs 7.2 months | G-chemo vs F-chemo, n = 126, P = .038; OS showed no difference (14.3 vs 12.4 months, P = .5) |
| Validation cohort, propensity score-weighted | biomarker-treatment interaction | TNTD P < .001, OS P = .005 |  |

</details>

<a id="model-titan-202511"></a>
<details>
<summary><b>TITAN</b> — A multimodal whole-slide foundation model for pathology <i>(Nat. Med. 2025-11)</i></summary>

**[A multimodal whole-slide foundation model for pathology](https://www.nature.com/articles/s41591-025-03982-3)**

*Nat. Med.* · 2025-11 · [Tong Ding](https://scholar.google.com/citations?user=Vwt2ZVYAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-025-03982-3](https://doi.org/10.1038/s41591-025-03982-3)

| | |
| --- | --- |
| **Parameters** | 48.5M |
| **Parameter note** | 48.5M is the slide encoder and excludes the frozen CONCH v1.5 patch encoder, so it is not comparable with tile-encoder counts such as Virchow's 632M. The released checkpoint on HuggingFace reports a safetensors total of 158,866,176, which is a different scope -- that file also carries the text encoder and multimodal decoder used for zero-shot and report generation, and ships the patch encoder separately as conch_v1_5_pytorch_model.bin. The repo is gated, so its config.json and model card could not be read to confirm the split. |
| **Backbone** | ViT slide encoder (Transformer-based Image and Text Alignment Network) over CONCH v1.5 patch features |
| **Pre-training** | `self-supervised`, `iBOT`, `CoCa`, `contrastive`<br>Three stages: iBOT self-supervised pretraining on a 2D grid of patch features, then CoCa alignment against synthetic ROI captions generated by the PathChat pathology copilot, then alignment against whole-slide pathology reports. |
| **Training data** | Whole-slide images with paired pathology reports and synthetic captions<br>**335,645** WSI · **182,862** pathology reports · **423,122** captions |
| **Downstream tasks** | `classification`, `subtyping`, `retrieval`, `report generation`, `survival prediction`<br>Slide-level representation without fine-tuning, rare disease recognition, cancer outcome prediction and pathology report generation. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/mahmoodlab/TITAN](https://github.com/mahmoodlab/TITAN) |
| **Weights** | [huggingface.co/MahmoodLab/TITAN](https://huggingface.co/MahmoodLab/TITAN) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| TCGA-UT-8K, linear probe tumour subtyping (32 classes) | balanced accuracy | 0.832 | logistic regression, +/- 0.0056; next-best slide encoder PRISM 0.774 |
| OT108, linear probe OncoTree classification (108 classes) | balanced accuracy | 0.587 | logistic regression, +/- 0.0103; next-best slide encoder PRISM 0.508 |
| TCGA-UT-8K, zero-shot tumour subtyping (32 classes) | balanced accuracy | 0.761 | +/- 0.0063; AUROC 0.989; PRISM 0.536 |
| Rare-Cancer slide retrieval (43 rare types in a 186-class database) | Top-1 accuracy | 0.539 | +/- 0.0100; Top-5 0.804; next-best slide encoder PRISM 0.449 |
| Disease-specific survival, six TCGA cohorts | concordance index (mean over cohorts) | 0.716 | next-best model CHIEF 0.691, the +3.62% quoted in the running text |

</details>

<a id="model-smmile-202511"></a>
<details>
<summary><b>SMMILe</b> — SMMILe enables accurate spatial quantification in digital pathology using multiple-instance learning <i>(Nat. Cancer 2025-11)</i></summary>

**[SMMILe enables accurate spatial quantification in digital pathology using multiple-instance learning](https://www.nature.com/articles/s43018-025-01060-8)**

*Nat. Cancer* · 2025-11 · [Zeyu Gao](https://scholar.google.com/citations?hl=zh-CN&user=CeP6dkcAAAAJ) & [Mireia Crispin-Ortuzar](https://scholar.google.com/citations?hl=en&user=TRZzLJgAAAAJ) · [doi:10.1038/s43018-025-01060-8](https://doi.org/10.1038/s43018-025-01060-8)

| | |
| --- | --- |
| **Parameters** | 1.2M |
| **Parameter note** | The paper reports SMMILe's own cost as "1.50 GFLOPS, 1.20 M parameters" for 1,024-dimension patch embeddings; the frozen ResNet-50/CONCH patch encoder is not counted, so this is not comparable to a tile-encoder parameter count. |
| **Backbone** | ResNet-50 and CONCH patch encoders with an instance-based multiple-instance-learning architecture using superpatch and refinement modules |
| **Pre-training** | `weakly supervised`<br>Feature extraction with pretrained encoders (ImageNet ResNet-50, pathology foundation model CONCH), then weakly supervised MIL training with slide-level labels. |
| **Training data** | 8 datasets covering 6 cancer types<br>**3,850** WSI · **8** datasets · **6** cancer types |
| **Downstream tasks** | `classification`, `detection`, `subtyping`, `grading`<br>WSI-level classification and patch-level spatial quantification, including metastasis detection, subtype prediction and grading. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/ZeyuGaoAi/SMMILe](https://github.com/ZeyuGaoAi/SMMILe) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Ovarian (UBC-OCEAN) | macro AUC | 94.11% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 1.13, second-best +2.20 |
| Prostate | macro AUC | 90.92% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 2.68, second-best +2.90 |
| Gastric Endoscopy (IH-ESD) | macro AUC | 92.75% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 3.59, second-best +11.18 |
| Breast (Camelyon16), spatial quantification | spatial macro F1 | 66.47% | ImageNet ResNet-50 patch embeddings; +/- 10.21, second-best method DSMIL 42.91%, the 23.56-point gap quoted in the running text |

</details>

<a id="model-musk-202501"></a>
<details>
<summary><b>MUSK</b> — A vision-language foundation model for precision oncology <i>(Nature 2025-01)</i></summary>

**[A vision-language foundation model for precision oncology](https://www.nature.com/articles/s41586-024-08378-w)**

*Nature* · 2025-01 · [Jinxi Xiang](https://scholar.google.com/citations?user=Zn-0LioAAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1038/s41586-024-08378-w](https://doi.org/10.1038/s41586-024-08378-w)

| | |
| --- | --- |
| **Parameters** | 675M |
| **Backbone** | BEiT-3-style multimodal transformer -- shared self-attention blocks with two independent vision and language experts; 24 layers, hidden size 1024, FFN 4096, 16 attention heads, 384x384 input at 16x16 patches |
| **Pre-training** | `MIM`, `contrastive`<br>Masked image modelling followed by vision-language contrastive alignment. |
| **Training data** | 50 million TCGA H&E image patches from ~33,000 WSIs and 1 billion text tokens from PubMed Central OA articles for masked pretraining, then ~1 million image-text pairs from Quilt1M (802k) and PathAsst (207k) for contrastive alignment<br>**50,000,000** image patches · **33,000** WSI · **11,577** patients · **1,000,000,000** text tokens · **1,001,800** articles · **1,000,000** pairs |
| **Downstream tasks** | `retrieval`, `visual question answering`, `classification`, `biomarker prediction`, `prognosis`, `survival prediction`, `treatment response`<br>Cross-modal retrieval, visual question answering, histopathology image classification and molecular biomarker prediction, plus clinical outcome prediction -- melanoma relapse, pan-cancer prognosis and immunotherapy response. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/lilab-stanford/MUSK](https://github.com/lilab-stanford/MUSK) |
| **Weights** | [huggingface.co/xiangjx/musk](https://huggingface.co/xiangjx/musk) |
| **License** | CC-BY-NC-ND-4.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| PathVQA visual question answering | accuracy | 73.2% | 95% CI 72.1-74.4 |
| HER2 status prediction | AUC | 0.826 | 95% CI 0.813-0.839 |
| Melanoma 5-year relapse prediction | AUC | 0.833 | 95% CI 0.818-0.847 |
| Pan-cancer prognosis, 16 cancer types | c-index | 0.746 | average; overall stage baseline reported as 0.645 |
| Immunotherapy response prediction, lung cancer | AUC | 0.768 | 95% CI 0.724-0.812 |

</details>

<a id="model-chief-202409"></a>
<details>
<summary><b>CHIEF</b> — A pathology foundation model for cancer diagnosis and prognosis prediction <i>(Nature 2024-09)</i></summary>

**[A pathology foundation model for cancer diagnosis and prognosis prediction](https://www.nature.com/articles/s41586-024-07894-z)**

*Nature* · 2024-09 · [Xiyue Wang](https://scholar.google.com/citations?user=NHt3fUcAAAAJ&hl=en) & [Kun-Hsing Yu](https://scholar.google.com/citations?user=1ZCJvkgAAAAJ&hl=en) · [doi:10.1038/s41586-024-07894-z](https://doi.org/10.1038/s41586-024-07894-z)

| | |
| --- | --- |
| **Backbone** | CTransPath tile encoder with a weakly supervised whole-slide aggregation module |
| **Pre-training** | `self-supervised`, `weakly supervised`<br>Two complementary pretraining strategies: unsupervised pretraining for tile-level features and weakly supervised pretraining for whole-slide pattern recognition. |
| **Training data** | Unsupervised tile-level pretraining then weakly supervised slide-level pretraining, across 14 cohorts and 19 anatomical sites<br>**15,000,000** image tiles · **60,530** WSI · **19** anatomical sites |
| **Downstream tasks** | `classification`, `detection`, `subtyping`, `prognosis`, `mutation prediction`<br>Cancer cell detection, tumour origin identification, molecular profile prediction and survival outcome prediction across cancer types. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/hms-dbmi/CHIEF](https://github.com/hms-dbmi/CHIEF) |
| **Weights** | [hub.docker.com/r/chiefcontainer/chief](https://hub.docker.com/r/chiefcontainer/chief/) |
| **License** | GPLv3 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Cancer cell detection, 15 datasets spanning 11 cancer types | macro-average AUROC | 0.9397 |  |
| Tumour origin prediction, held-out test sets | macro-averaged accuracy | 0.895 |  |
| Tumour origin prediction, independent cohorts | AUROC | 0.9853 | paper reports 0.9853 +/- 0.0245 |
| MSI-high identification in colorectal cancer | AUROC | 0.869-0.875 | range across the evaluated cohorts |
| Survival prediction, held-out test set | c-index | 0.74 | average across cancer types |

</details>

<a id="model-virchow-202407"></a>
<details>
<summary><b>Virchow</b> — A foundation model for clinical-grade computational pathology and rare cancers detection <i>(Nat. Med. 2024-07)</i></summary>

**[A foundation model for clinical-grade computational pathology and rare cancers detection](https://www.nature.com/articles/s41591-024-03141-0)**

*Nat. Med.* · 2024-07 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ&hl=en) & [Thomas J. Fuchs](https://scholar.google.ch/citations?user=zh0Raz8AAAAJ&hl=en) · [doi:10.1038/s41591-024-03141-0](https://doi.org/10.1038/s41591-024-03141-0)

| | |
| --- | --- |
| **Parameters** | 632M |
| **Backbone** | ViT-H/14 |
| **Pre-training** | `DINOv2`<br>Self-supervised DINOv2 pretraining on H&E whole-slide images. |
| **Training data** | H&E-stained whole-slide images from a clinical archive<br>**1,500,000** WSI · **100,000** patients · **2,000,000,000** training tiles |
| **Downstream tasks** | `detection`, `biomarker prediction`, `classification`<br>Pan-cancer detection including rare cancers, and biomarker prediction. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/Paige-AI/paige-ml-sdk](https://github.com/Paige-AI/paige-ml-sdk) |
| **Weights** | [huggingface.co/paige-ai/Virchow](https://huggingface.co/paige-ai/Virchow) |
| **License** | Apache-2.0 |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Pan-cancer detection across nine common and seven rare cancers | AUC | 0.950 | specimen level; aggregator trained on Virchow embeddings |
| Rare cancer detection | AUC | 0.937 | seven rare cancer types |
| Pan-cancer detection at 95% sensitivity | specificity | 72.5% | UNI 68.9%, Phikon 62.9%, CTransPath 52.3% |
| Prostate cancer detection versus the Paige Prostate clinical product | AUC | 0.980 | pan-cancer model on Virchow embeddings; surpassed by the FDA-approved Paige Prostate specialist model at 0.995 (P < 0.05) |

</details>

<a id="model-prov-gigapath-202405"></a>
<details>
<summary><b>Prov-GigaPath</b> — A whole-slide foundation model for digital pathology from real-world data <i>(Nature 2024-05)</i></summary>

**[A whole-slide foundation model for digital pathology from real-world data](https://www.nature.com/articles/s41586-024-07441-w)**

*Nature* · 2024-05 · [Hanwen Xu](https://scholar.google.com/citations?user=HwO7L5sAAAAJ&hl=zh-CN) & [Hoifung Poon](https://scholar.google.com/citations?user=yqqmVbkAAAAJ&hl=en) · [doi:10.1038/s41586-024-07441-w](https://doi.org/10.1038/s41586-024-07441-w)

| | |
| --- | --- |
| **Parameters** | 1B |
| **Parameter note** | Two components, counted separately. The Nature paper and its Supplementary Information give no count for the released model; both figures come from the same team's follow-up paper (GigaPath-Flash, arXiv:2607.18218), whose Table 1 lists "GigaPath \| Whole-Slide FM \| ViT-g (1B) + LongNet (86M) \| Apache-2.0 \| Nature, 2024" and whose section 2.1 calls it "the frozen GigaPath ViT-g (1B) teacher". The 1B is the tile encoder; the 86M is the LongNet slide encoder. Not comparable with a tile-encoder-only count such as UNI's 307M without saying which half you mean. |
| **Backbone** | ViT-g tile encoder with a 12-layer, 768-dim LongNet slide encoder over 1,536-dim tile embeddings |
| **Pre-training** | `DINOv2`, `MAE`<br>DINOv2 tile-level pretraining followed by masked autoencoder pretraining with LongNet over whole slides. |
| **Training data** | Real-world H&E slides from the Providence health network<br>**171,189** WSI · **1,384,860,229** image tiles |
| **Downstream tasks** | `classification`, `subtyping`, `mutation prediction`, `biomarker prediction`<br>26 prediction tasks spanning pathomics and cancer subtyping. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/prov-gigapath/prov-gigapath](https://github.com/prov-gigapath/prov-gigapath) |
| **Weights** | [huggingface.co/prov-gigapath/prov-gigapath](https://huggingface.co/prov-gigapath/prov-gigapath) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Digital pathology benchmark (26 tasks) | tasks at state of the art | 25/26 | significant improvement over the second-best method in 18 tasks |
| Cancer subtyping across nine cancer types | AUROC | 0.903 | average; falls to 0.886 with a randomly initialised LongNet |
| LUAD five-gene mutation prediction | macro-AUROC | 0.626 | average over EGFR, FAT1, KRAS, TP53, LRP1B on Prov-Path |
| Pan-cancer tumour mutation burden prediction | AUROC | 0.708 | average |

</details>

<a id="model-uni-202403"></a>
<details>
<summary><b>UNI</b> — Towards a general-purpose foundation model for computational pathology <i>(Nat. Med. 2024-03)</i></summary>

**[Towards a general-purpose foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02857-3)**

*Nat. Med.* · 2024-03 · [Richard J. Chen](https://scholar.google.com/citations?user=yhGqdMgAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-024-02857-3](https://doi.org/10.1038/s41591-024-02857-3)

| | |
| --- | --- |
| **Parameters** | 307M |
| **Backbone** | ViT-L/16 |
| **Pre-training** | `DINOv2`<br>Self-supervised DINOv2 pretraining on the Mass-100K slide corpus. |
| **Training data** | Mass-100K, H&E whole-slide images from Massachusetts General Brigham<br>**100,426** WSI · **100,130,900** tissue patches |
| **Downstream tasks** | `segmentation`, `detection`, `grading`, `subtyping`, `biomarker prediction`, `classification`<br>34 tasks including nuclear segmentation, primary and metastatic cancer detection, cancer grading and subtyping, biomarker screening, molecular subtyping, organ transplant assessment and pan-cancer classification. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI) |
| **Weights** | [huggingface.co/MahmoodLab/UNI](https://huggingface.co/MahmoodLab/UNI) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Prostate ISUP grading (PANDA) | quadratic weighted Cohen's kappa | 0.946 | ABMIL on pre-extracted UNI features; +0.014 over REMEDIS |
| 32-class pan-cancer tissue classification (TCGA Uniform Tumor) | balanced accuracy | 65.7% | linear probing on pre-extracted features; +4.7% over REMEDIS |
| 32-class pan-cancer tissue classification (TCGA Uniform Tumor) | AUROC | 0.975 | linear probing on pre-extracted features; +0.017 over REMEDIS |
| Tumor-immune lymphocyte detection (ChampKit) | AUROC | 0.978 | without stain normalisation; UNI FNR 0.193 vs best ChampKit model 0.974 AUROC / 0.246 FNR |
| CAMELYON17-WILDS out-of-domain test set | accuracy | 98.3% | 97.4% on the OOD validation set; best leaderboard model 95.2% / 96.5% |

</details>

<a id="model-conch-202403"></a>
<details>
<summary><b>CONCH</b> — A visual-language foundation model for computational pathology <i>(Nat. Med. 2024-03)</i></summary>

**[A visual-language foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02856-4)**

*Nat. Med.* · 2024-03 · [Ming Y. Lu](https://scholar.google.com/citations?user=GhzAXmIAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-024-02856-4](https://doi.org/10.1038/s41591-024-02856-4)

| | |
| --- | --- |
| **Backbone** | ViT-B/16 image encoder, 12-layer text encoder and 12-layer multimodal decoder |
| **Pre-training** | `iBOT`, `CoCa`<br>iBOT visual pretraining followed by CoCa image-text pretraining. |
| **Training data** | Pathology image-caption pairs curated from educational sources and PubMed<br>**1,170,647** pairs |
| **Downstream tasks** | `classification`, `retrieval`, `segmentation`, `captioning`<br>Tile- and slide-level classification, cross-modal image-to-text and text-to-image retrieval, image segmentation and captioning. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/mahmoodlab/CONCH](https://github.com/mahmoodlab/CONCH) |
| **Weights** | [huggingface.co/MahmoodLab/CONCH](https://huggingface.co/MahmoodLab/CONCH) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| TCGA BRCA subtyping | balanced accuracy | 91.3% | zero-shot with prompt ensembling; 95% CI 86.6-96.0%, n = 150 |
| TCGA NSCLC subtyping | balanced accuracy | 90.7% | zero-shot with prompt ensembling; 95% CI 85.9-94.8%, n = 150 |
| TCGA RCC subtyping | balanced accuracy | 90.2% | zero-shot with prompt ensembling; 95% CI 86.0-93.8%, n = 225 |
| Text-to-image retrieval | mean recall | 44.0% | zero-shot; paper's average over source A (68.8%), source B (39.0%) and TCGA LUAD (24.0%) |
| SICAP zero-shot segmentation | Dice | 0.601 | macro-averaged over images; 95% CI 0.530-0.675, n = 31 WSIs |

</details>

<a id="model-plip-202308"></a>
<details>
<summary><b>PLIP</b> — A visual-language foundation model for pathology image analysis using medical Twitter <i>(Nat. Med. 2023-08)</i></summary>

**[A visual-language foundation model for pathology image analysis using medical Twitter](https://www.nature.com/articles/s41591-023-02504-3)**

*Nat. Med.* · 2023-08 · [Zhi Huang](https://scholar.google.com/citations?user=Sh6TgyQAAAAJ&hl=en) & [James Zou](https://scholar.google.com/citations?user=23ZXZvEAAAAJ&hl=en) · [doi:10.1038/s41591-023-02504-3](https://doi.org/10.1038/s41591-023-02504-3)

| | |
| --- | --- |
| **Backbone** | CLIP ViT-B/32 image encoder with a 12-layer, 512-dim Transformer text encoder |
| **Pre-training** | `CLIP`, `contrastive`<br>CLIP fine-tuned on the OpenPath image-text corpus. |
| **Training data** | OpenPath, pathology images paired with natural-language descriptions sourced from medical Twitter<br>**208,414** pairs |
| **Downstream tasks** | `classification`, `retrieval`<br>Zero-shot and transfer-learning classification of pathology images, and cross-modal image-to-text retrieval. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/PathologyFoundation/plip](https://github.com/PathologyFoundation/plip) |
| **Weights** | [huggingface.co/vinid/plip](https://huggingface.co/vinid/plip) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Zero-shot classification on four external datasets | F1 | 0.565-0.832 | range across Kather colon (0.565), PanNuke (0.656), WSSS4LUAD (0.734) and DigestPath (0.832); prior CLIP model scores 0.030-0.481 |
| Supervised classifier on PLIP embeddings | F1 improvement | 2.5% | versus other supervised model embeddings |

</details>

---

This page is generated. Add a paper by editing [`data/pathology.yaml`](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/data/pathology.yaml) in the [pipeline repository](https://github.com/1nslyn/biomedical-ai-pipeline) and rebuilding — edits made here are overwritten. The schema and house rules are in [CONTRIBUTING.md](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/CONTRIBUTING.md).
