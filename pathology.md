<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Source: data/pathology.yaml | Regenerate: python scripts/build.py -->

# Pathology

Histopathology, whole-slide imaging and computational pathology.

**Maintainer:** [Leo Yin](https://shuolinyin.com) ([GitHub](https://github.com/leoyin1127))

**15 entries** · [Back to index](README.md)

| Date | Model | Paper | Venue | Size | Training data | Resources |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [PRISM2](#model-prism2-202607) | [End-to-end multimodal pathology foundation model with clinical dialogue](https://www.nature.com/articles/s41591-026-04521-4) | Nat. Med. | 4.6B | 2.4M WSI | [weights](https://huggingface.co/paige-ai/Prism2) |
| 2026-04 | [PRET](#model-pret-202604) | [PRET is a few-shot system for pan-cancer recognition without example training](https://www.nature.com/articles/s43018-026-01141-2) | Nat. Cancer | — | 4.5K WSI (eval) | [code](https://github.com/xmed-lab/PRET) |
| 2026-03 | [HistBiases](#model-histbiases-202603) | [Confounding factors and biases abound when predicting molecular biomarkers from histological images](https://www.nature.com/articles/s41551-026-01616-8) | Nat. Biomed. Eng. | — | 8.2K patients | [code](https://github.com/imuhdawood/HistBiases) |
| 2026-02 | [Neuropath-AI](#model-neuropath-ai-202602) | [Classification accuracy of a hierarchical molecular inference-based deep-learning system for CNS tumour diagnosis: a multi-institutional, retrospective study](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045%2825%2900661-8/abstract) | Lancet Oncol. | — | 5.8K WSI | [weights](https://methylscape.ccr.cancer.gov/) |
| 2026-02 | [CHAI](#model-chai-202602) | [Development and validation of a computational histology artificial intelligence-powered predictive biomarker for selection of chemotherapy in advanced pancreatic cancer](https://ascopubs.org/doi/10.1200/JCO-25-02199) | J. Clin. Oncol. | — | 25K WSI | — |
| 2026-02 | [KEEP](#model-keep-202602) | [Knowledge-enhanced pretraining for vision-language pathology foundation model on cancer diagnosis](https://www.cell.com/cancer-cell/fulltext/S1535-6108%2826%2900058-9) | Cancer Cell | — | 143K groups | [code](https://github.com/MAGIC-AI4Med/KEEP) |
| 2025-11 | [SMMILe](#model-smmile-202511) | [SMMILe enables accurate spatial quantification in digital pathology using multiple-instance learning](https://www.nature.com/articles/s43018-025-01060-8) | Nat. Cancer | — | 3.9K WSI | [code](https://github.com/ZeyuGaoAi/SMMILe) |
| 2025-11 | [TITAN](#model-titan-202511) | [A multimodal whole-slide foundation model for pathology](https://www.nature.com/articles/s41591-025-03982-3) | Nat. Med. | — | 335.6K WSI | [code](https://github.com/mahmoodlab/TITAN) · [weights](https://huggingface.co/MahmoodLab/TITAN) |
| 2025-01 | [MUSK](#model-musk-202501) | [A vision-language foundation model for precision oncology](https://www.nature.com/articles/s41586-024-08378-w) | Nature | — | 33K WSI | [code](https://github.com/lilab-stanford/MUSK) |
| 2024-09 | [CHIEF](#model-chief-202409) | [A pathology foundation model for cancer diagnosis and prognosis prediction](https://www.nature.com/articles/s41586-024-07894-z) | Nature | — | — | [code](https://github.com/hms-dbmi/CHIEF) |
| 2024-07 | [Virchow](#model-virchow-202407) | [A foundation model for clinical-grade computational pathology and rare cancers detection](https://www.nature.com/articles/s41591-024-03141-0) | Nat. Med. | 632M | 1.5M WSI | [code](https://github.com/Paige-AI/paige-ml-sdk) · [weights](https://huggingface.co/paige-ai/Virchow) |
| 2024-05 | [Prov-GigaPath](#model-prov-gigapath-202405) | [A whole-slide foundation model for digital pathology from real-world data](https://www.nature.com/articles/s41586-024-07441-w) | Nature | — | 171.2K WSI | [code](https://github.com/prov-gigapath/prov-gigapath) · [weights](https://huggingface.co/prov-gigapath/prov-gigapath) |
| 2024-03 | [CONCH](#model-conch-202403) | [A visual-language foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02856-4) | Nat. Med. | 86M | 1.2M pairs | [code](https://github.com/mahmoodlab/CONCH) · [weights](https://huggingface.co/MahmoodLab/CONCH) |
| 2024-03 | [UNI](#model-uni-202403) | [Towards a general-purpose foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02857-3) | Nat. Med. | 307M | 100.4K WSI | [code](https://github.com/mahmoodlab/UNI) · [weights](https://huggingface.co/MahmoodLab/UNI2-h) |
| 2023-08 | [PLIP](#model-plip-202308) | [A visual-language foundation model for pathology image analysis using medical Twitter](https://www.nature.com/articles/s41591-023-02504-3) | Nat. Med. | — | 208.4K pairs | [code](https://github.com/PathologyFoundation/plip) · [weights](https://huggingface.co/vinid/plip) |

## Details

<a id="model-prism2-202607"></a>

### PRISM2

**[End-to-end multimodal pathology foundation model with clinical dialogue](https://www.nature.com/articles/s41591-026-04521-4)**

*Nat. Med.* · 2026-07 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ&hl=en) & [Siqi Liu](https://scholar.google.com/citations?hl=en&user=ADyo_cAAAAAJ) · [doi:10.1038/s41591-026-04521-4](https://doi.org/10.1038/s41591-026-04521-4)

| | |
| --- | --- |
| **Parameters** | 4.6B |
| **Backbone** | Virchow2 tile encoder, Perceiver slide encoder, BioGPT language encoder and a Phi-3 Mini 3.8B decoder-only LLM |
| **Pre-training** | `contrastive`, `next-token prediction`<br>Two-stage language-supervised multimodal pre-training: contrastive slide-report alignment, then autoregressive clinical-dialogue learning. The slide encoder is frozen while Phi-3 Mini is fine-tuned in stage 2. |
| **Training data** | H&E whole-slide images with paired clinical reports, converted into question-answer pairs<br>**2,350,518** WSI · **685,507** specimens · **200,692** patients · **14,000,000** QA pairs |
| **Downstream tasks** | `detection`, `subtyping`, `biomarker prediction`, `survival prediction`, `report generation`<br>Prompt-based cancer detection and subtyping; diagnostic, biomarker and survival prediction; pathology report completion. |
| **Modalities** | `histopathology`, `text` |
| **Weights** | [huggingface.co/paige-ai/Prism2](https://huggingface.co/paige-ai/Prism2) |
| **PDF name** | `202607-NatMed-PRISM2.pdf` |

<a id="model-pret-202604"></a>

### PRET

**[PRET is a few-shot system for pan-cancer recognition without example training](https://www.nature.com/articles/s43018-026-01141-2)**

*Nat. Cancer* · 2026-04 · [Yi Li](https://scholar.google.com/citations?user=qGsK180AAAAJ&hl=en) & [Xiaomeng Li](https://scholar.google.com/citations?user=uVTzPpoAAAAJ&hl=en) · [doi:10.1038/s43018-026-01141-2](https://doi.org/10.1038/s43018-026-01141-2)

| | |
| --- | --- |
| **Backbone** | Default feature extractor is a DINO-pretrained ViT-S/8 pathology encoder; PRET adds an in-context tagger, in-context classifier, instance miner, attention aggregator and postprocessor |
| **Pre-training** | `DINO`, `self-supervised`<br>Training-free for downstream tasks. The default encoder was pretrained self-supervised on unlabeled TCGA pathology images. |
| **Training data** | No task-specific training images for PRET itself. Evaluated on 4,484 WSIs across 23 benchmarks. The paper does not state a numeric TCGA pretraining image count for the default encoder.<br>**4,484** WSI (eval) · **23** benchmarks |
| **Downstream tasks** | `detection`, `subtyping`, `segmentation`, `classification`<br>Cancer screening, cancer subtyping, tumour segmentation, lymph node metastasis detection. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/xmed-lab/PRET](https://github.com/xmed-lab/PRET) |
| **PDF name** | `202604-NatCancer-PRET.pdf` |

<a id="model-histbiases-202603"></a>

### HistBiases

**[Confounding factors and biases abound when predicting molecular biomarkers from histological images](https://www.nature.com/articles/s41551-026-01616-8)**

*Nat. Biomed. Eng.* · 2026-03 · [Muhammad Dawood](https://scholar.google.com/citations?hl=en&user=a-szm64AAAAJ) & [Fayyaz ul Amir Afsar Minhas](https://scholar.google.com/citations?hl=en&user=cQ6eO_kAAAAJ) · [doi:10.1038/s41551-026-01616-8](https://doi.org/10.1038/s41551-026-01616-8)

| | |
| --- | --- |
| **Backbone** | Benchmarking study rather than a new model. Evaluates CLAM, SlideGraph-infinity and TITAN, with CTransPath and ShuffleNet patch encoders. |
| **Pre-training** | `self-supervised`, `weakly supervised`<br>CTransPath pretrained on histology via self-supervised learning; ShuffleNet pretrained on ImageNet; TITAN trained on 330,000 image-text pairs. |
| **Training data** | H&E WSIs from TCGA, METABRIC, MSK and DFCI. Weakly supervised models trained on TCGA and validated on CPTAC and ABCTB.<br>**8,221** patients |
| **Downstream tasks** | `biomarker prediction`, `mutation prediction`, `benchmarking`<br>Molecular biomarker and gene mutation prediction from WSIs, plus a confounding/stratification analysis against biomarker interdependency, grade and TMB. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/imuhdawood/HistBiases](https://github.com/imuhdawood/HistBiases) |
| **PDF name** | `202603-NatBME-HistBiases.pdf` |
| **Note** | Benchmarking and bias study, not a new foundation model. |

<a id="model-neuropath-ai-202602"></a>

### Neuropath-AI

**[Classification accuracy of a hierarchical molecular inference-based deep-learning system for CNS tumour diagnosis: a multi-institutional, retrospective study](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045%2825%2900661-8/abstract)**

*Lancet Oncol.* · 2026-02 · H. Lalchungnunga & Kenneth Aldape · [doi:10.1016/S1470-2045(25)00661-8](https://doi.org/10.1016/S1470-2045%2825%2900661-8)

| | |
| --- | --- |
| **Backbone** | UNI large vision transformer plus hierarchical submodules using MLPs and ensemble classifiers (random forest, SVM, KNN, logistic regression) |
| **Pre-training** | `self-supervised`<br>WSI-pretrained UNI encoder followed by molecular inference-based hierarchical classification. |
| **Training data** | Multi-institutional retrospective CNS tumour cohort<br>**5,835** WSI |
| **Downstream tasks** | `classification`, `mutation prediction`, `gene expression prediction`<br>CNS tumour family-level classification, 52 terminal CNS tumour types, IDH mutation prediction, inferred gene expression and DNA methylation. |
| **Modalities** | `histopathology` |
| **Weights** | [methylscape.ccr.cancer.gov](https://methylscape.ccr.cancer.gov/) |
| **PDF name** | `202602-LancetOnc-Neuropath-AI.pdf` |

<a id="model-chai-202602"></a>

### CHAI

**[Development and validation of a computational histology artificial intelligence-powered predictive biomarker for selection of chemotherapy in advanced pancreatic cancer](https://ascopubs.org/doi/10.1200/JCO-25-02199)**

*J. Clin. Oncol.* · 2026-02 · [Andrew Hendifar](https://scholar.google.com/citations?hl=en&user=XwWT-TMAAAAJ) & [Jennifer J. Knox](https://scholar.google.com/citations?user=6aEaHzcAAAAJ&hl=en) · [doi:10.1200/JCO-25-02199](https://doi.org/10.1200/JCO-25-02199)

| | |
| --- | --- |
| **Backbone** | Not stated in the paper |
| **Pre-training** | `supervised`<br>Pan-cancer H&E slides are patched and merged with indication labels to form a base model for cell and tissue classification. |
| **Training data** | Pan-cancer H&E-stained slides<br>**25,000** WSI |
| **Downstream tasks** | `biomarker prediction`, `treatment response`<br>Quantifies histomorphologic features of the cancer and its microenvironment along dimensions defined by the hallmarks of cancer, used to select chemotherapy. |
| **Modalities** | `histopathology` |
| **PDF name** | `202602-JCO-CHAI.pdf` |

<a id="model-keep-202602"></a>

### KEEP

**[Knowledge-enhanced pretraining for vision-language pathology foundation model on cancer diagnosis](https://www.cell.com/cancer-cell/fulltext/S1535-6108%2826%2900058-9)**

*Cancer Cell* · 2026-02 · Xiao Zhou & [Weidi Xie](https://scholar.google.com/citations?user=Vtrqj4gAAAAJ&hl=zh-CN)

| | |
| --- | --- |
| **Backbone** | ViT-L/16 vision encoder with a BERT text encoder |
| **Pre-training** | `contrastive`, `CLIP`<br>Knowledge-enhanced vision-language pretraining using semantic-level alignment via metric learning within semantic groups guided by a disease knowledge graph. |
| **Training data** | Pathology image-text pairs from OpenPath and Quilt-1M, reorganized into semantically structured groups<br>**143,000** groups |
| **Downstream tasks** | `segmentation`, `detection`, `subtyping`, `retrieval`, `classification`<br>Zero-shot slide-level cancer region segmentation, cancer detection and subtyping; tile-level cross-modal retrieval and zero-shot image classification. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/MAGIC-AI4Med/KEEP](https://github.com/MAGIC-AI4Med/KEEP) |
| **PDF name** | `202602-CancerCell-KEEP.pdf` |

> [!NOTE]
> Needs checking before this entry is considered final:
> - Cell Press DOI not yet recorded -- add it so dedup keys on DOI rather than title.

<a id="model-smmile-202511"></a>

### SMMILe

**[SMMILe enables accurate spatial quantification in digital pathology using multiple-instance learning](https://www.nature.com/articles/s43018-025-01060-8)**

*Nat. Cancer* · 2025-11 · [Zeyu Gao](https://scholar.google.com/citations?hl=zh-CN&user=CeP6dkcAAAAJ) & [Mireia Crispin-Ortuzar](https://scholar.google.com/citations?hl=en&user=TRZzLJgAAAAJ) · [doi:10.1038/s43018-025-01060-8](https://doi.org/10.1038/s43018-025-01060-8)

| | |
| --- | --- |
| **Backbone** | ResNet-50 and CONCH patch encoders with an instance-based multiple-instance-learning architecture using superpatch and refinement modules |
| **Pre-training** | `weakly supervised`<br>Feature extraction with pretrained encoders (ImageNet ResNet-50, pathology foundation model CONCH), then weakly supervised MIL training with slide-level labels. |
| **Training data** | 8 datasets covering 6 cancer types<br>**3,850** WSI · **8** datasets · **6** cancer types |
| **Downstream tasks** | `classification`, `detection`, `subtyping`, `grading`<br>WSI-level classification and patch-level spatial quantification, including metastasis detection, subtype prediction and grading. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/ZeyuGaoAi/SMMILe](https://github.com/ZeyuGaoAi/SMMILe) |
| **PDF name** | `202511-NatCancer-SMMILe.pdf` |

<a id="model-titan-202511"></a>

### TITAN

**[A multimodal whole-slide foundation model for pathology](https://www.nature.com/articles/s41591-025-03982-3)**

*Nat. Med.* · 2025-11 · [Tong Ding](https://scholar.google.com/citations?user=Vwt2ZVYAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-025-03982-3](https://doi.org/10.1038/s41591-025-03982-3)

| | |
| --- | --- |
| **Backbone** | ViT slide encoder (Transformer-based Image and Text Alignment Network) over CONCH v1.5 patch features |
| **Pre-training** | `self-supervised`, `contrastive`, `CLIP`<br>Visual self-supervised pretraining followed by vision-language alignment against pathology reports and synthetic captions generated by a pathology multimodal copilot. |
| **Training data** | Whole-slide images with paired pathology reports and synthetic captions<br>**335,645** WSI · **423,122** captions |
| **Downstream tasks** | `classification`, `subtyping`, `retrieval`, `report generation`, `survival prediction`<br>Slide-level representation without fine-tuning, rare disease recognition, cancer outcome prediction and pathology report generation. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/mahmoodlab/TITAN](https://github.com/mahmoodlab/TITAN) |
| **Weights** | [huggingface.co/MahmoodLab/TITAN](https://huggingface.co/MahmoodLab/TITAN) |
| **PDF name** | `202511-NatMed-TITAN.pdf` |

<a id="model-musk-202501"></a>

### MUSK

**[A vision-language foundation model for precision oncology](https://www.nature.com/articles/s41586-024-08378-w)**

*Nature* · 2025-01 · [Jinxi Xiang](https://scholar.google.com/citations?user=Zn-0LioAAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1038/s41586-024-08378-w](https://doi.org/10.1038/s41586-024-08378-w)

| | |
| --- | --- |
| **Backbone** | BEiT-3 |
| **Pre-training** | `MIM`, `contrastive`<br>Masked image modelling followed by vision-language contrastive alignment. |
| **Training data** | WSIs plus the QUILT-1M and PathAsst image-text corpora<br>**33,000** WSI |
| **Downstream tasks** | `prognosis`, `treatment response`, `survival prediction`<br>Predicting clinical outcomes -- melanoma relapse, pan-cancer prognosis and immunotherapy response. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/lilab-stanford/MUSK](https://github.com/lilab-stanford/MUSK) |
| **PDF name** | `202501-Nat-MUSK.pdf` |

<a id="model-chief-202409"></a>

### CHIEF

**[A pathology foundation model for cancer diagnosis and prognosis prediction](https://www.nature.com/articles/s41586-024-07894-z)**

*Nature* · 2024-09 · [Xiyue Wang](https://scholar.google.com/citations?user=NHt3fUcAAAAJ&hl=en) & [Kun-Hsing Yu](https://scholar.google.com/citations?user=1ZCJvkgAAAAJ&hl=en) · [doi:10.1038/s41586-024-07894-z](https://doi.org/10.1038/s41586-024-07894-z)

| | |
| --- | --- |
| **Backbone** | CTransPath tile encoder with a weakly supervised whole-slide aggregation module |
| **Pre-training** | `self-supervised`, `weakly supervised`<br>Two complementary pretraining strategies: unsupervised pretraining for tile-level features and weakly supervised pretraining for whole-slide pattern recognition. |
| **Training data** | Tile-level and slide-level pretraining across many cancer types and institutions |
| **Downstream tasks** | `classification`, `detection`, `subtyping`, `prognosis`, `mutation prediction`<br>Cancer cell detection, tumour origin identification, molecular profile prediction and survival outcome prediction across cancer types. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/hms-dbmi/CHIEF](https://github.com/hms-dbmi/CHIEF) |
| **PDF name** | `202409-Nat-CHIEF.pdf` |

> [!NOTE]
> Needs checking before this entry is considered final:
> - Pretraining data scale (tiles / WSIs) not yet filled in from the paper.

<a id="model-virchow-202407"></a>

### Virchow

**[A foundation model for clinical-grade computational pathology and rare cancers detection](https://www.nature.com/articles/s41591-024-03141-0)**

*Nat. Med.* · 2024-07 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ&hl=en) & [Thomas J. Fuchs](https://scholar.google.ch/citations?user=zh0Raz8AAAAJ&hl=en) · [doi:10.1038/s41591-024-03141-0](https://doi.org/10.1038/s41591-024-03141-0)

| | |
| --- | --- |
| **Parameters** | 632M |
| **Backbone** | ViT-H/14 |
| **Pre-training** | `DINOv2`<br>Self-supervised DINOv2 pretraining on H&E whole-slide images. |
| **Training data** | H&E-stained whole-slide images from a clinical archive<br>**1,500,000** WSI |
| **Downstream tasks** | `detection`, `biomarker prediction`, `classification`<br>Pan-cancer detection including rare cancers, and biomarker prediction. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/Paige-AI/paige-ml-sdk](https://github.com/Paige-AI/paige-ml-sdk) |
| **Weights** | [huggingface.co/paige-ai/Virchow](https://huggingface.co/paige-ai/Virchow) |
| **PDF name** | `202407-NatMed-Virchow.pdf` |

> [!NOTE]
> Needs checking before this entry is considered final:
> - Previously catalogued as "Virchow2". This Nat. Med. paper introduces Virchow; Virchow2 is the separate arXiv follow-up (2408.00738). Confirm and, if the team wants Virchow2 listed too, add it as its own entry.
> - params 632M is the standard ViT-H/14 configuration, not a figure quoted in the paper.

<a id="model-prov-gigapath-202405"></a>

### Prov-GigaPath

**[A whole-slide foundation model for digital pathology from real-world data](https://www.nature.com/articles/s41586-024-07441-w)**

*Nature* · 2024-05 · [Hanwen Xu](https://scholar.google.com/citations?user=HwO7L5sAAAAJ&hl=zh-CN) & [Hoifung Poon](https://scholar.google.com/citations?user=yqqmVbkAAAAJ&hl=en) · [doi:10.1038/s41586-024-07441-w](https://doi.org/10.1038/s41586-024-07441-w)

| | |
| --- | --- |
| **Backbone** | ViT tile encoder with a LongNet slide-level encoder |
| **Pre-training** | `DINOv2`, `MAE`<br>DINOv2 tile-level pretraining followed by masked autoencoder pretraining with LongNet over whole slides. |
| **Training data** | Real-world H&E slides from the Providence health network<br>**171,189** WSI |
| **Downstream tasks** | `classification`, `subtyping`, `mutation prediction`, `biomarker prediction`<br>26 prediction tasks spanning pathomics and cancer subtyping. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/prov-gigapath/prov-gigapath](https://github.com/prov-gigapath/prov-gigapath) |
| **Weights** | [huggingface.co/prov-gigapath/prov-gigapath](https://huggingface.co/prov-gigapath/prov-gigapath) |
| **PDF name** | `202405-Nat-Prov-GigaPath.pdf` |

<a id="model-conch-202403"></a>

### CONCH

**[A visual-language foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02856-4)**

*Nat. Med.* · 2024-03 · [Ming Y. Lu](https://scholar.google.com/citations?user=GhzAXmIAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-024-02856-4](https://doi.org/10.1038/s41591-024-02856-4)

| | |
| --- | --- |
| **Parameters** | 86M |
| **Backbone** | ViT-B/16 |
| **Pre-training** | `iBOT`, `CoCa`<br>iBOT visual pretraining followed by CoCa image-text pretraining. |
| **Training data** | Pathology image-caption pairs curated from educational sources and PubMed<br>**1,170,000** pairs |
| **Downstream tasks** | `classification`, `retrieval`, `segmentation`, `captioning`<br>Tile- and slide-level classification, cross-modal image-to-text and text-to-image retrieval, image segmentation and captioning. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/mahmoodlab/CONCH](https://github.com/mahmoodlab/CONCH) |
| **Weights** | [huggingface.co/MahmoodLab/CONCH](https://huggingface.co/MahmoodLab/CONCH) |
| **PDF name** | `202403-NatMed-CONCH.pdf` |

> [!NOTE]
> Needs checking before this entry is considered final:
> - params 86M is the standard ViT-B/16 configuration, not a figure quoted in the paper.

<a id="model-uni-202403"></a>

### UNI

**[Towards a general-purpose foundation model for computational pathology](https://www.nature.com/articles/s41591-024-02857-3)**

*Nat. Med.* · 2024-03 · [Richard J. Chen](https://scholar.google.com/citations?user=yhGqdMgAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) · [doi:10.1038/s41591-024-02857-3](https://doi.org/10.1038/s41591-024-02857-3)

| | |
| --- | --- |
| **Parameters** | 307M |
| **Backbone** | ViT-L/16 |
| **Pre-training** | `DINOv2`<br>Self-supervised DINOv2 pretraining on the Mass-100K slide corpus. |
| **Training data** | Mass-100K, H&E whole-slide images from Massachusetts General Brigham<br>**100,426** WSI |
| **Downstream tasks** | `segmentation`, `detection`, `grading`, `subtyping`, `biomarker prediction`, `classification`<br>34 tasks including nuclear segmentation, primary and metastatic cancer detection, cancer grading and subtyping, biomarker screening, molecular subtyping, organ transplant assessment and pan-cancer classification. |
| **Modalities** | `histopathology` |
| **Code** | [github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI) |
| **Weights** | [huggingface.co/MahmoodLab/UNI2-h](https://huggingface.co/MahmoodLab/UNI2-h) |
| **PDF name** | `202403-NatMed-UNI.pdf` |

> [!NOTE]
> Needs checking before this entry is considered final:
> - params 307M is the standard ViT-L/16 configuration, not a figure quoted in the paper.

<a id="model-plip-202308"></a>

### PLIP

**[A visual-language foundation model for pathology image analysis using medical Twitter](https://www.nature.com/articles/s41591-023-02504-3)**

*Nat. Med.* · 2023-08 · [Zhi Huang](https://scholar.google.com/citations?user=Sh6TgyQAAAAJ&hl=en) & [James Zou](https://scholar.google.com/citations?user=23ZXZvEAAAAJ&hl=en) · [doi:10.1038/s41591-023-02504-3](https://doi.org/10.1038/s41591-023-02504-3)

| | |
| --- | --- |
| **Backbone** | CLIP ViT-B/32 with a Transformer text encoder |
| **Pre-training** | `CLIP`, `contrastive`<br>CLIP fine-tuned on the OpenPath image-text corpus. |
| **Training data** | OpenPath, pathology images paired with natural-language descriptions sourced from medical Twitter<br>**208,414** pairs |
| **Downstream tasks** | `classification`, `retrieval`<br>Zero-shot and transfer-learning classification of pathology images, and cross-modal image-to-text retrieval. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/PathologyFoundation/plip](https://github.com/PathologyFoundation/plip) |
| **Weights** | [huggingface.co/vinid/plip](https://huggingface.co/vinid/plip) |
| **PDF name** | `202308-NatMed-PLIP.pdf` |

---

Add a paper by editing [`data/pathology.yaml`](data/pathology.yaml) and running `python scripts/build.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).
