<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from data/AI4biology.yaml in https://github.com/1nslyn/biomedical-ai-pipeline -->
<!-- Edits made here are overwritten by the next build. -->

# AI for Biology

Genomics, transcriptomics, proteomics, omics and biological modeling.

**Maintainer:** [Keishi Suzuki](https://github.com/Kappapapa123)

**16 entries** · [Paper cards](paper_cards/AI4biology/) · [Back to index](README.md)

## Genomics

| Date | Model | Venue | Model size | Training scale | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.03 | [Evo 2](#model-evo-2-202603) | Nature | 40B (larger of 7B / 40B) | 9.3T tokens (40B) | autoregressive, 8K → 1M context | variant effect prediction, classification, generation |
| 2026.01 | [AlphaGenome](#model-alphagenome-202601) | Nature | _unchecked_ | 7,058 functional tracks | read-coverage pred. + distillation | variant effect prediction, gene expression prediction, regression |
| 2026.01 | [P-CARE](#model-p-care-202601) | Nat. Cancer | _n/a_ | — | supervised | risk prediction |

## Transcriptomics

| Date | Model | Venue | Model size | Training scale | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.07 | [Path2Space](#model-path2space-202607) | Cell | _unchecked_ | 56.6K spot pairs | CTransPath SSL → supervised reg. | gene expression prediction, cell type annotation, survival prediction +1 |

## Proteomics & Protein Design

| Date | Model | Venue | Model size | Training scale | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.06 | [LASErMPNN](#model-lasermpnn-202606) | Nature | _unchecked_ | PDB protein–ligand complexes | supervised, atom-level properties | generation, protein structure prediction |
| 2026.03 | [ProtAIDe-Dx](#model-protaide-dx-202603) | Nat. Med. | _unchecked_ | 17.2K participants | multi-task joint learning, scratch | diagnosis, classification, prognosis |
| 2026.03 | [CAR-T Response Biomarkers](#model-car-t-response-biomarkers-202603) | Nat. Biomed. Eng. | _n/a_ | 256 patients, 13 trials | supervised | treatment response, biomarker prediction |
| 2026.01 | [HEX](#model-hex-202601) | Nat. Med. | _unchecked_ | 755K tiles, 10 WSI (10 pts) | MUSK masked modeling (50M images) | biomarker prediction, prognosis, treatment response |
| 2026.01 | [GigaTIME](#model-gigatime-202601) | Cell | _unchecked_ | 21 paired H&E/mIF slides | supervised H&E → mIF translation | generation, biomarker prediction |

## Multi-omics & Spatial

| Date | Model | Venue | Model size | Training scale | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.06 | [AURORA](#model-aurora-202606) | Cell Metab. | _unchecked_ | 21.7K physiome records | — | diagnosis, generation |
| 2026.02 | [OMICmAge](#model-omicmage-202602) | Nat. Aging | _n/a_ | ~31K participants | supervised | risk prediction, survival prediction, regression |
| 2026.01 | [DBiTplus](#model-dbitplus-202601) | Nat. Methods | _unchecked_ | mouse embryo, lymph node | pretrained Mesmer + MaxFuse | segmentation, cell type annotation, clustering |
| 2025.12 | [SpatialEx](#model-spatialex-202512) | Nat. Methods | _unchecked_ | breast, colon, skin, brain | UNI (DINOv2) + hypergraph GNN | gene expression prediction, clustering |

## Other

| Date | Model | Venue | Model size | Training scale | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026.03 | [Exposome-Phenome Atlas](#model-exposome-phenome-atlas-202603) | Nat. Med. | _n/a_ | NHANES, ten waves 1999–2018 | none | association study, risk prediction |
| 2026.03 | [Antibiotic-Microbiome Links](#model-antibiotic-microbiome-links-202603) | Nat. Med. | _n/a_ | 15.0K adults | none | association study |
| 2026.02 | [Compact V4 models](#model-compact-v4-models-202602) | Nature | _unchecked_ | 44 sessions, 3 macaques | ImageNet supervised → neural fit | regression |

<sub><b>Model size</b> is the count the authors publish, with the component it covers in brackets — a slide encoder and a tile encoder are not comparable. <i>not published</i> means the access routes were worked and no author source states one; <i>n/a</i> means the paper does not introduce a model. <b>Training scale</b> is what the model was actually trained on, written per entry rather than derived from the record, because the unit differs from paper to paper.</sub>

## Details

Click a model to expand its record.

<a id="model-path2space-202607"></a>
<details>
<summary><b>Path2Space</b> — AI-predicted spatial transcriptomics unlocks breast cancer biomarkers from pathology <i>(Cell 2026-07)</i></summary>

**[AI-predicted spatial transcriptomics unlocks breast cancer biomarkers from pathology](https://www.cell.com/cell/fulltext/S0092-8674%2826%2900458-7)**

*Cell* · 2026-07 · [Eldad D. Shulman](https://scholar.google.com/citations?hl=en&user=fOGpHIsAAAAJ) & [Eytan Ruppin](https://scholar.google.com/citations?hl=en&user=L3KXa3cAAAAJ) · [doi:10.1016/j.cell.2026.04.023](https://doi.org/10.1016/j.cell.2026.04.023)

| | |
| --- | --- |
| **Backbone** | CTransPath feature extractor with an MLP regressor |
| **Pre-training** | `self-supervised`, `supervised`<br>CTransPath self-supervised pathology foundation model features, with Path2Space itself trained by supervised regression on paired H&E and spatial transcriptomics data. |
| **Training data** | 10x Genomics Visium breast cancer spatial transcriptomics with matched H&E images, plus the Bassiouni et al. cohort. Predicts 14,068 genes.<br>**56,567** matched image–expression spot pairs · **14,068** genes predicted |
| **Downstream tasks** | `gene expression prediction`, `cell type annotation`, `survival prediction`, `treatment response`<br>Spatial gene expression prediction, cell-type abundance inference, tumour microenvironment characterization, SpatioType survival stratification, and chemotherapy and trastuzumab response prediction. |
| **Modalities** | `histopathology`, `transcriptomics` |
| **Weights** | [zenodo.org/records/14729337](https://zenodo.org/records/14729337) |

</details>

<a id="model-lasermpnn-202606"></a>
<details>
<summary><b>LASErMPNN</b> — Zero-shot design of drug-binding proteins via neural iterative selection−expansion <i>(Nature 2026-06)</i></summary>

**[Zero-shot design of drug-binding proteins via neural iterative selection−expansion](https://www.nature.com/articles/s41586-026-10670-w)**

*Nature* · 2026-06 · [Benjamin Fry](https://scholar.google.com/citations?user=2TE2_OkAAAAJ&hl=en) & [Nicholas F. Polizzi](https://scholar.google.com/citations?hl=en&user=CgZvDJkAAAAJ&view_op=list_works&sortby=pubdate) · [doi:10.1038/s41586-026-10670-w](https://doi.org/10.1038/s41586-026-10670-w)

| | |
| --- | --- |
| **Backbone** | Ligand-aware message-passing heterograph neural network, paired with a protein–ligand structure predictor in a closed-loop iterative design algorithm (neural iterative selection−expansion, NISE) |
| **Pre-training** | `supervised`<br>Trained to predict atom-level properties of protein–ligand complexes. |
| **Training data** | Protein–ligand co-crystal structures from the Protein Data Bank. |
| **Downstream tasks** | `generation`, `protein structure prediction`<br>Zero-shot de novo design of high-affinity small-molecule binding proteins, side-chain packing and dihedral-angle prediction, neural proofreading, and designing proteins that protect labile ligands from hydrolysis. |
| **Modalities** | `molecular`, `proteomics` |
| **Code** | [github.com/polizzilab/LASErMPNN](https://github.com/polizzilab/LASErMPNN) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Zero-shot design of exatecan binders | design success rate | 100% | NISE loop; designs use different folds; denominator 4/4 |
| Zero-shot design of apixaban binders | design success rate | 83% | NISE loop; designs use different folds; denominator 5/6 |
| EPIC, exatecan binding | dissociation constant | 0.12 µM | first-round design |
| EPIC (Q51N/M97L), exatecan binding | dissociation constant | 1.2 nM | after two point mutations |
| APEX, apixaban binding | dissociation constant | 80 pM (95% CI 54–122 pM) | Prior best by competing methods on comparable targets: 680 nM (LigandMPNN+Rosetta), 8 µM (COMBS) |

</details>

<a id="model-aurora-202606"></a>
<details>
<summary><b>AURORA</b> — A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response <i>(Cell Metab. 2026-06)</i></summary>

**[A generative AI framework unifies human multi-omics to model aging, metabolic health, and intervention response](https://www.sciencedirect.com/science/article/pii/S1550413126001087)**

*Cell Metab.* · 2026-06 · [Jiawei Chen](https://scholar.google.com.hk/citations?user=9HNbgn8AAAAJ) & [Jing-Dong J. Han](https://scholar.google.com/citations?user=x7GzFRAAAAAJ&hl=en) · [doi:10.1016/j.cmet.2026.03.014](https://doi.org/10.1016/j.cmet.2026.03.014)

| | |
| --- | --- |
| **Backbone** | Multi-layer perceptron with self-attention |
| **Training data** | Jidong cohort -- 3D facial images, physiome measurements and lifestyle questionnaires.<br>**8,386** 3D facial images · **21,660** physiome records · **3,226** lifestyle questionnaires |
| **Downstream tasks** | `diagnosis`, `generation`<br>Disease prediction and generative modelling of intervention response. |
| **Modalities** | `multimodal`, `molecular` |
| **Code** | [github.com/JackieHanLab/Aurora](https://github.com/JackieHanLab/Aurora) |

</details>

<a id="model-evo-2-202603"></a>
<details>
<summary><b>Evo 2</b> — Genome modelling and design across all domains of life with Evo 2 <i>(Nature 2026-03)</i></summary>

**[Genome modelling and design across all domains of life with Evo 2](https://www.nature.com/articles/s41586-026-10176-5)**

*Nature* · 2026-03 · [Garyk Brixi](https://scholar.google.com/citations?user=U71t6aYAAAAJ&hl=en) & [Brian L. Hie](https://scholar.google.com/citations?user=qT3feHIAAAAJ&hl=en) · [doi:10.1038/s41586-026-10176-5](https://doi.org/10.1038/s41586-026-10176-5)

| | |
| --- | --- |
| **Parameters** | 40B |
| **Backbone** | StripedHyena 2 |
| **Pre-training** | `next-token prediction`, `self-supervised`<br>Two-stage genomic sequence pretraining: 8,192-token pretraining on genic-window-weighted data, followed by multi-stage midtraining and context extension up to 1M tokens. |
| **Training data** | OpenGenome2 -- curated non-redundant nucleotide sequences from bacteria, archaea, eukarya and bacteriophage.<br>**8.8T** nucleotides · **2.4T** tokens (Evo 2 7B) · **9.3T** tokens (Evo 2 40B) |
| **Downstream tasks** | `variant effect prediction`, `classification`, `generation`<br>Variant effect prediction, exon classification, gene essentiality prediction, protein and ncRNA mutational scanning, regulatory element and secondary-structure feature identification, genome-scale generation, and chromatin-accessibility controlled generation. |
| **Modalities** | `genomics` |
| **Code** | [github.com/arcinstitute/evo2](https://github.com/arcinstitute/evo2) |

</details>

<a id="model-protaide-dx-202603"></a>
<details>
<summary><b>ProtAIDe-Dx</b> — A deep joint-learning proteomics model for diagnosis of six conditions associated with dementia <i>(Nat. Med. 2026-03)</i></summary>

**[A deep joint-learning proteomics model for diagnosis of six conditions associated with dementia](https://www.nature.com/articles/s41591-026-04303-y)**

*Nat. Med.* · 2026-03 · [Lijun An](https://scholar.google.co.uk/citations?user=La_luGsAAAAJ&hl=en&oi=ao) & [Jacob W. Vogel](https://scholar.google.co.uk/citations?user=1m6yqlwAAAAJ&hl=en&oi=sra) · [doi:10.1038/s41591-026-04303-y](https://doi.org/10.1038/s41591-026-04303-y)

| | |
| --- | --- |
| **Backbone** | Multi-layer perceptron |
| **Pre-training** | `supervised`<br>Deep multi-task joint-learning framework trained from scratch with binary cross-entropy and a multi-class rank loss. |
| **Training data** | Global Neurodegenerative Proteomics Consortium (GNPC) v1.3MS dataset, SomaLogic 7k proteomics.<br>**17,187** participants · **7,595** proteins |
| **Downstream tasks** | `diagnosis`, `classification`, `prognosis`<br>Diagnostic prediction across six conditions -- control, Alzheimer's disease, Parkinson's disease, frontotemporal dementia, amyotrophic lateral sclerosis and stroke/TIA -- plus prediction of longitudinal clinical progression. |
| **Modalities** | `proteomics` |
| **Code** | [github.com/DeMONLab-BioFINDER/An_ProtAIDe-Dx](https://github.com/DeMONLab-BioFINDER/An_ProtAIDe-Dx) |
| **Note** | The accuracies above are within-GNPC cross-validation. Leave-one-site-out validation drops substantially for every model, and the authors state the model cannot replace existing clinical markers. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| GNPC cross-validation, amyotrophic lateral sclerosis | balanced classification accuracy | 95% | best of the six classes |
| GNPC cross-validation, stroke/TIA | balanced classification accuracy | 70% | worst of the six classes |

</details>

<a id="model-car-t-response-biomarkers-202603"></a>
<details>
<summary><b>CAR-T Response Biomarkers</b> — Predictive biomarkers of response to chimeric antigen receptor (CAR) T-cell therapy for pan-haematologic cancer <i>(Nat. Biomed. Eng. 2026-03)</i></summary>

**[Predictive biomarkers of response to chimeric antigen receptor (CAR) T-cell therapy for pan-haematologic cancer](https://www.nature.com/articles/s41551-026-01633-7)**

*Nat. Biomed. Eng.* · 2026-03 · [Gregory M. Chen](https://scholar.google.co.uk/citations?user=St_vpusAAAAJ&hl=en&oi=sra) & [Joseph A. Fraietta](https://scholar.google.co.uk/citations?user=sZYwTj8AAAAJ&hl=en&oi=ao) · [doi:10.1038/s41551-026-01633-7](https://doi.org/10.1038/s41551-026-01633-7)

| | |
| --- | --- |
| **Backbone** | Machine-learning biomarker analysis over a harmonized multi-assay data resource rather than a new model architecture. |
| **Pre-training** | `supervised` |
| **Training data** | Pre-infusion clinical features, apheresis T cells profiled by 17-marker flow cytometry, ex vivo T-cell expansion during manufacture, serum marker panels, and serial qPCR tracking of circulating CAR T cells.<br>**256** patients · **13** clinical trials · **2,000,000** apheresis T cells (flow cytometry) · **90,000** serum marker measurements |
| **Downstream tasks** | `treatment response`, `biomarker prediction`<br>Pan-cancer prediction of favourable versus non-favourable response to CAR T-cell therapy from pre-infusion and manufacturing measurements. |
| **Modalities** | `proteomics` |
| **Note** | Three cohort numbers, all real and all different: 256 patients in the data resource, 179 with apheresis flow cytometry, 141 with both flow and serial cytokines (model training and 10-fold CV), and 53 later-processed patients held out. `training_slides` describes the resource; the model itself saw 141. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 10-fold cross-validation (random forest) | AUROC | 0.875 | n = 141 -- patients with both flow cytometry and serial cytokines |
| Prospective hold-out of later-processed patients | AUROC | 0.74 | n = 53 |
| Pre-infusion measurements only | AUROC | 0.77 | the ceiling available before treatment starts |
| Post-infusion measurements only | AUROC | 0.85 |  |
| Leave-one-cancer-type-out | AUROC | 0.82 |  |

</details>

<a id="model-exposome-phenome-atlas-202603"></a>
<details>
<summary><b>Exposome-Phenome Atlas</b> — An atlas of exposome–phenome associations in health and disease risk <i>(Nat. Med. 2026-03)</i></summary>

**[An atlas of exposome–phenome associations in health and disease risk](https://www.nature.com/articles/s41591-026-04266-0)**

*Nat. Med.* · 2026-03 · [Chirag J. Patel](https://scholar.google.co.uk/citations?user=Ecjx73cAAAAJ&hl=en&oi=ao) & Arjun K. Manrai · [doi:10.1038/s41591-026-04266-0](https://doi.org/10.1038/s41591-026-04266-0)

| | |
| --- | --- |
| **Backbone** | Exposome-wide association study over survey waves rather than a new model architecture. |
| **Pre-training** | `none` |
| **Training data** | US CDC National Health and Nutrition Examination Survey (NHANES), ten independent waves 1999–2018: 305 phenotypes against 619 exposures, giving 123,774 estimable pairs.<br>**305** phenotypes · **619** exposures · **123,774** estimable pairs |
| **Downstream tasks** | `association study`, `risk prediction`<br>Exposome-wide association study (EWAS) against health and disease risk. |
| **Modalities** | `molecular` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Exposome-phenome pairs passing Bonferroni correction | count (share) | 5,674 (5%) | of 123,774 estimable pairs |
| Single-exposure incremental variance explained | median R² | 0.14% |  |
| Poly-exposomic model (≤20 exposures) | median R² | 3.5% | Maximum 43% (triglycerides). Across the 29 phenotypes with both, exposomic and genomic median R² are both 7.9% |

</details>

<a id="model-antibiotic-microbiome-links-202603"></a>
<details>
<summary><b>Antibiotic-Microbiome Links</b> — Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals <i>(Nat. Med. 2026-03)</i></summary>

**[Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals](https://www.nature.com/articles/s41591-026-04284-y)**

*Nat. Med.* · 2026-03 · [Gabriel Baldanzi](https://scholar.google.co.uk/citations?user=Q8bWon0AAAAJ&hl=en&oi=ao) & [Tove Fall](https://scholar.google.co.uk/citations?user=W5ZIq_oAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41591-026-04284-y](https://doi.org/10.1038/s41591-026-04284-y)

| | |
| --- | --- |
| **Backbone** | Population-scale association analysis rather than a new model architecture. |
| **Pre-training** | `none` |
| **Training data** | 14,979 adults from the Swedish Prescribed Drug Register and three Swedish population-based cohorts: SCAPIS (n = 8,488), SIMPLER (n = 4,784) and MOS (n = 1,707), with deep shotgun metagenomics over 1,340 species.<br>**14,979** adults · **1,340** species |
| **Downstream tasks** | `association study`<br>Association between eight years of oral antibiotic use and gut microbiome composition. |
| **Modalities** | `microbiome` |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Clindamycin, courses within the past year | change in species count | −47 species per course | q = 2.1e-17; the largest single effect in the study |
| Share of all FDR<5% species associations | proportion by drug | clindamycin 37.9%, flucloxacillin 25.8%, fluoroquinolones 17.9% | Penicillin V, the most prescribed antibiotic in the cohort, is associated with only 29 species |

</details>

<a id="model-omicmage-202602"></a>
<details>
<summary><b>OMICmAge</b> — OMICmAge quantifies biological age by integrating multi-omics with electronic medical records <i>(Nat. Aging 2026-02)</i></summary>

**[OMICmAge quantifies biological age by integrating multi-omics with electronic medical records](https://doi.org/10.1038/s43587-026-01073-7)**

*Nat. Aging* · 2026-02 · [Qingwen Chen](https://scholar.google.com/citations?user=Djf7l7AAAAAJ&hl=en&oi=ao) & [Jessica Lasky-Su](https://scholar.google.co.uk/citations?user=MijM6lwAAAAJ&hl=en&oi=ao) · [doi:10.1038/s43587-026-01073-7](https://doi.org/10.1038/s43587-026-01073-7)

| | |
| --- | --- |
| **Backbone** | Elastic net regression with a Cox proportional-hazards model |
| **Pre-training** | `supervised` |
| **Training data** | Mass General Brigham Biobank participants with multi-omics and EMR data.<br>**31,000** participants · **990** CpGs (OMICmAge) · **40** epigenetic biomarker proxies · **1,097** CpGs (DNAmEMRAge) |
| **Downstream tasks** | `risk prediction`, `survival prediction`, `regression`<br>Biological age estimation, mortality risk and aging-related chronic disease prediction. |
| **Modalities** | `molecular`, `EHR` |
| **Code** | [github.com/LaskySuLab/OMICmAge](https://github.com/LaskySuLab/OMICmAge) |
| **Note** | The 40 epigenetic biomarker proxies require a further 10,315 CpGs, 50.8% of which are on the 450K array -- the deployed measurement footprint is much larger than the headline 990 CpGs suggests. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Agreement with EMRAge (OMICmAge) | mean absolute error | 4.97 years | DNAmEMRAge is 8.50 years on the same target |
| 5-year mortality (DNAmEMRAge) | AUC | 0.898 | OMICmAge is 0.892 -- the worse surrogate fit predicts mortality slightly better |
| 10-year mortality (DNAmEMRAge) | AUC | 0.890 | OMICmAge is 0.873 |

</details>

<a id="model-compact-v4-models-202602"></a>
<details>
<summary><b>Compact V4 models</b> — Compact deep neural network models of the visual cortex <i>(Nature 2026-02)</i></summary>

**[Compact deep neural network models of the visual cortex](https://www.nature.com/articles/s41586-026-10150-1)**

*Nature* · 2026-02 · [Benjamin R. Cowley](https://scholar.google.com/citations?user=KPhO_2gAAAAJ&hl=en) & [Matthew A. Smith](https://scholar.google.com/citations?user=mhi9LhkAAAAJ&hl=en) · [doi:10.1038/s41586-026-10150-1](https://doi.org/10.1038/s41586-026-10150-1)

| | |
| --- | --- |
| **Backbone** | ResNet50 for the large model and custom compact CNNs for the compressed models; MobileNet, DenseNet, VGG, Xception, InceptionV4, NASNetMobile, InceptionV3 and CORnet were also evaluated |
| **Pre-training** | `supervised`<br>Supervised ImageNet classification for the backbone, then fitted to neural data through closed-loop adaptive experiments. |
| **Training data** | Extracellular spike responses from chronic multi-electrode arrays in macaque V4 (44 sessions, 3 macaques, ~50 units per session), plus V1 and IT recordings from public datasets, with images drawn from YFCC100M and ImageNet.<br>**44** sessions · **3** macaques · **78,000** unique images |
| **Downstream tasks** | `regression`<br>Predicting neural responses to arbitrary images in macaque visual cortex, stimulus preference characterization and circuit hypothesis generation. |
| **Code** | [github.com/cowleygroup/V4_compact_models](https://github.com/cowleygroup/V4_compact_models) |

</details>

<a id="model-alphagenome-202601"></a>
<details>
<summary><b>AlphaGenome</b> — Advancing regulatory variant effect prediction with AlphaGenome <i>(Nature 2026-01)</i></summary>

**[Advancing regulatory variant effect prediction with AlphaGenome](https://www.nature.com/articles/s41586-025-10014-0)**

*Nature* · 2026-01 · [Žiga Avsec](https://scholar.google.com/citations?user=gojWHbQAAAAJ) & [Pushmeet Kohli](https://scholar.google.com/citations?user=3pyzQQ8AAAAJ) · [doi:10.1038/s41586-025-10014-0](https://doi.org/10.1038/s41586-025-10014-0)

| | |
| --- | --- |
| **Backbone** | CNN + Transformer |
| **Pre-training** | `supervised`, `distillation`<br>Read-coverage prediction with student knowledge distillation. |
| **Training data** | Functional genomics datasets spanning regulatory assays.<br>**7,058** functional genomics tracks |
| **Downstream tasks** | `variant effect prediction`, `gene expression prediction`, `regression`<br>Regulatory variant effect prediction across functional genomics tracks. |
| **Modalities** | `genomics` |
| **Code** | [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome) |

</details>

<a id="model-p-care-202601"></a>
<details>
<summary><b>P-CARE</b> — Genomic risk model to implement precision prostate cancer screening in clinical care: the ProGRESS study <i>(Nat. Cancer 2026-01)</i></summary>

**[Genomic risk model to implement precision prostate cancer screening in clinical care: the ProGRESS study](https://www.nature.com/articles/s43018-025-01103-0)**

*Nat. Cancer* · 2026-01 · [Jason L. Vassy](https://scholar.google.co.uk/citations?user=sjSOUxgAAAAJ&hl=en&oi=sra) & [Tyler M. Seibert](https://scholar.google.co.uk/citations?hl=en&user=0WsaQZkAAAAJ&view_op=list_works&sortby=pubdate) · [doi:10.1038/s43018-025-01103-0](https://doi.org/10.1038/s43018-025-01103-0)

| | |
| --- | --- |
| **Backbone** | Two-stage Cox proportional hazards: LASSO-Cox variant selection (601 of 707 candidates) producing the PHS601 polygenic hazard score, then a Cox model combining PHS601 with genetic principal components and family history (P-CARE) |
| **Pre-training** | `supervised` |
| **Training data** | 585,418 male Million Veteran Program participants, genotyped on a custom Affymetrix Axiom biobank array of 723,305 variants enriched for low-frequency variants in African and Hispanic populations, with outcomes from the VA Corporate Data Warehouse, the VA Central Cancer Registry and the National Death Index. External validation in four PRACTICAL Consortium datasets (African ancestry, Asian ancestry, Cohort of Swedish Men and ProtecT) and in All of Us v7.<br>**585,418** MVP participants · **18,457** PRACTICAL participants · **74,331** All of Us participants · **601** variants retained |
| **Downstream tasks** | `risk prediction`<br>Time-to-event risk stratification for any, clinically significant, metastatic and fatal prostate cancer; three-tier clinical risk categorization; risk-equivalent-age calculation to set screening start age; positive-predictive-value enrichment of a PSA >= 3 ng/mL result; and paired monogenic reporting across 12 NCCN-guideline prostate cancer genes on the same blended genome-exome assay. |
| **Modalities** | `genomics` |
| **Code** | [github.com/precimed/MVP-PCa-PHS](https://github.com/precimed/MVP-PCa-PHS) |
| **Note** | Discrimination only -- no calibration curve is reported in any cohort. ProGRESS (NCT05926102, 5,000 VA patients) is ongoing, so no screening outcome exists yet. Family history is not one construct: paternal history in MVP, any first-degree relative in PRACTICAL and All of Us. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MVP, metastatic prostate cancer (PHS601 alone) | hazard ratio per s.d. | 2.07 (1.95–2.17) | n = 585,418; 10 x 10-fold cross-validation within the development cohort |
| MVP, metastatic prostate cancer (full P-CARE model) | hazard ratio per s.d. | 2.05 (1.93–2.16) | Statistically indistinguishable from PHS601 alone; the Discussion states family history and genetic ancestry add less here than in the authors' prior model |
| ProtecT, PSA ≥ 3 ng/mL for clinically significant cancer | positive predictive value | 0.13 → 0.19 (top 20%) → 0.23 (top 5%) | n = 6,411; external; the top-20% and top-5% confidence intervals overlap |
| All of Us v7, prostate cancer case-control | odds ratio per s.d. (age-adjusted) | 1.91 (1.85–1.98) | 4,473 cases / 69,858 controls; an odds ratio on case-control status, not a hazard ratio, so not directly comparable with the rows above |

</details>

<a id="model-hex-202601"></a>
<details>
<summary><b>HEX</b> — AI-enabled virtual spatial proteomics from histopathology for interpretable biomarker discovery in lung cancer <i>(Nat. Med. 2026-01)</i></summary>

**[AI-enabled virtual spatial proteomics from histopathology for interpretable biomarker discovery in lung cancer](https://www.nature.com/articles/s41591-025-04060-4)**

*Nat. Med.* · 2026-01 · [Zhe Li](https://scholar.google.com/citations?user=DfBEFMgAAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1038/s41591-025-04060-4](https://doi.org/10.1038/s41591-025-04060-4)

| | |
| --- | --- |
| **Backbone** | MUSK pathology foundation model |
| **Pre-training** | `MIM`<br>Unified masked modeling (MUSK) pretrained on 50M pathology images. |
| **Training data** | Same-section CODEX/PhenoCycler and H&E from non-small-cell lung cancer for training, plus pan-cancer (Bern) and colorectal external validation; six NSCLC clinical cohorts and 12 further TCGA cancer types for outcome prediction.<br>**819,532** image tiles · **10** WSI · **10** training patients · **578** TMA cores · **34** tissue types · **40** protein markers · **2,298** NSCLC clinical patients · **5,019** pan-cancer patients |
| **Downstream tasks** | `biomarker prediction`, `prognosis`, `treatment response`<br>Virtual spatial proteomics from H&E (HEX); prognosis and immunotherapy response prediction by MICA, a separate co-attention model that fuses real H&E features with HEX-generated virtual proteomics. |
| **Modalities** | `histopathology`, `proteomics` |
| **Code** | [github.com/lilab-stanford/HEX](https://github.com/lilab-stanford/HEX) |
| **Note** | Two models, and the headline clinical numbers belong to the second. HEX predicts 40 protein values per H&E tile; MICA fuses real H&E features with HEX-generated virtual proteomics and produces every prognosis and immunotherapy result. HEX predicts a tile mean (~50 µm), not single cells. Training is 754,836 tiles from 10 WSIs -- ten NSCLC patients at one hospital; the abstract's 819,532 tiles across 382 samples adds the two technical-validation TMA sets. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Stanford-WSI, 40-marker protein prediction (fivefold CV) | mean Pearson r | 0.790 | n = 10 WSIs; folds are patient splits of the ten training patients |
| Bern pan-cancer, external protein prediction | mean Pearson r | 0.658 | n = 206 cores, 24 overlapping markers only, no fine-tuning; the Stanford comparator on the same 24-marker subset is 0.718 |
| ANHIR lung, orthogonal IHC validation | Pearson r | 0.479 (CD31) / 0.606 (Ki-67) | n = 3 tumours; the only assay-independent check, and far below the headline |
| NSCLC prognosis, four external cohorts (MICA) | C-index | 0.68 | Trained on NLST with cutoffs fixed in advance; H&E-only 0.56 and virtual-CODEX-only 0.59, so the gain is in the fusion |
| Stanford-IO, immunotherapy objective response (MICA) | AUC | 0.82 (0.73–0.90) | n = 148, fivefold CV within a single cohort, no external validation; PD-L1 0.66 and TMB 0.59 (CI 0.37–0.80, which includes chance) |
| 12 further TCGA cancer types, prognosis (MICA) | study design | fivefold cross-validation | n = 5,019; cross-validated, not externally validated |

</details>

<a id="model-gigatime-202601"></a>
<details>
<summary><b>GigaTIME</b> — Multimodal AI generates virtual population for tumor microenvironment modeling <i>(Cell 2026-01)</i></summary>

**[Multimodal AI generates virtual population for tumor microenvironment modeling](https://doi.org/10.1016/j.cell.2025.11.016)**

*Cell* · 2026-01 · [Jeya Maria Jose Valanarasu](https://scholar.google.com/citations?user=vphpzPYAAAAJ&hl=en) & [Hoifung Poon](https://scholar.google.ca/citations?user=yqqmVbkAAAAJ&hl=en) · [doi:10.1016/j.cell.2025.11.016](https://doi.org/10.1016/j.cell.2025.11.016)

| | |
| --- | --- |
| **Backbone** | NestedUNet (UNet++) |
| **Pre-training** | `supervised`<br>Supervised cross-modal translation trained on 40 million cells with paired H&E and multiplex immunofluorescence. |
| **Training data** | Paired H&E and multiplex immunofluorescence slides.<br>**40,000,000** cells · **21** paired H&E/mIF slides |
| **Downstream tasks** | `generation`, `biomarker prediction`<br>Virtual mIF generation, population-scale tumour-immune microenvironment analysis and biomarker discovery. |
| **Modalities** | `histopathology`, `proteomics` |
| **Code** | [github.com/prov-gigatime/GigaTIME](https://github.com/prov-gigatime/GigaTIME) |

</details>

<a id="model-dbitplus-202601"></a>
<details>
<summary><b>DBiTplus</b> — Integration of imaging-based and sequencing-based spatial omics mapping on the same tissue section via DBiTplus <i>(Nat. Methods 2026-01)</i></summary>

**[Integration of imaging-based and sequencing-based spatial omics mapping on the same tissue section via DBiTplus](https://www.nature.com/articles/s41592-025-02948-0)**

*Nat. Methods* · 2026-01 · [Archibald Enninful](https://www.researchgate.net/profile/Archibald-Enninful) & [Rong Fan](https://scholar.google.com/citations?user=3FgAMAgAAAAJ&hl=en) · [doi:10.1038/s41592-025-02948-0](https://doi.org/10.1038/s41592-025-02948-0)

| | |
| --- | --- |
| **Backbone** | Mesmer for segmentation with MaxFuse for cross-modal integration |
| **Pre-training** | `supervised`<br>Uses pretrained Mesmer weights for segmentation. |
| **Training data** | FFPE and frozen mouse embryo, human lymph node and lymphoma tissue sections. |
| **Downstream tasks** | `segmentation`, `cell type annotation`, `clustering`<br>Spatial multi-omics integration, cell-type deconvolution and single-cell mapping on the same tissue section. |
| **Modalities** | `microscopy`, `transcriptomics`, `proteomics` |
| **Code** | [github.com/Janezjz/DBiT-plus](https://github.com/Janezjz/DBiT-plus) |

</details>

<a id="model-spatialex-202512"></a>
<details>
<summary><b>SpatialEx</b> — High-parameter spatial multi-omics through histology-anchored integration <i>(Nat. Methods 2025-12)</i></summary>

**[High-parameter spatial multi-omics through histology-anchored integration](https://www.nature.com/articles/s41592-025-02926-6)**

*Nat. Methods* · 2025-12 · [Yonghao Liu](https://scholar.google.com/citations?user=wCqFrjoAAAAJ&hl=zh-CN) & [Zhiyuan Yuan](https://scholar.google.com/citations?user=dycmzbgAAAAJ&hl=en) · [doi:10.1038/s41592-025-02926-6](https://doi.org/10.1038/s41592-025-02926-6)

| | |
| --- | --- |
| **Backbone** | UNI H&E foundation model with a hypergraph neural network |
| **Pre-training** | `self-supervised`<br>Uses the UNI self-supervised pathology foundation model as the histology encoder. |
| **Training data** | Human breast cancer, colon and skin, and mouse brain, profiled with Xenium and Visium. |
| **Downstream tasks** | `gene expression prediction`, `clustering`<br>H&E-to-omics prediction, panel diagonal integration and omics diagonal integration. |
| **Modalities** | `histopathology`, `transcriptomics`, `proteomics` |
| **Code** | [github.com/KEAML-JLU/SpatialEx](https://github.com/KEAML-JLU/SpatialEx) |

</details>

---

This page is generated. Add a paper by editing [`data/AI4biology.yaml`](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/data/AI4biology.yaml) in the [pipeline repository](https://github.com/1nslyn/biomedical-ai-pipeline) and rebuilding — edits made here are overwritten. The schema and house rules are in [CONTRIBUTING.md](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/CONTRIBUTING.md).
