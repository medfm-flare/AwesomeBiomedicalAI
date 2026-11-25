# H&E Virtual Omics

Models that predict molecular readouts — biomarkers, bulk expression, spatial maps and single-cell profiles — from routine H&E slides alone.

**Maintainer:** [Dongqing Sun](https://github.com/DongqingSun96)

**78 entries** (54 methods, 19 foundation models, 5 benchmarks) · **Last updated: 2026-11** · [Back to index](README.md)

**Jump to:** [Discrete biomarkers](#discrete-biomarkers) · [Subtypes and signatures](#subtypes-and-signatures) · [Bulk molecular profiles](#bulk-molecular-profiles) · [Spatial molecular maps](#spatial-molecular-maps) · [Single-cell profiles](#single-cell-profiles) · [Cell composition](#cell-composition) · [Foundation models](#foundation-models-evaluated-on-molecular-tasks) · [Benchmarks](#benchmarks) · [Reviews and other benchmarks](#reviews-and-benchmarks-outside-the-list) · [Common datasets](#common-datasets)

## Scope

A paper is listed when a model takes **only an H&E image at inference** and outputs a **molecular readout** that is checked against a measured assay (sequencing, methylation arrays, IHC, spatial transcriptomics or multiplexed protein imaging). Methods that need measured omics at inference, such as spatial-transcriptomics super-resolution, are out of scope. Papers were found by a PubMed search of Nature, Cell and Cancer Cell family journals (2018 – Nov 2026) and screened by hand; foundation models are listed when their evaluation includes molecular tasks.

**Reading the tables.** *Output scale* is the unit the model predicts for. *Strongest validation* is the hardest test reported: Same section < Serial section < Held-out (new patients, same cohort) < External (a different cohort) < Prospective. *Headline result* quotes values checked against the full text; — means not yet extracted. AUROC is for binary labels; r is Pearson correlation per gene or marker unless stated. Values are not comparable across rows: cohorts, gene panels and metrics differ.

## Discrete biomarkers

A yes/no or class label per patient: a mutation, MSI, receptor status, HRD.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [HRDPath](https://doi.org/10.1038/s41467-026-78430-y) | Nat. Commun. | HRD status and HRDetect score (ovarian) | Slide | Held-out | — |
| 2026-08 | [PathPrism](https://doi.org/10.1016/j.ccell.2026.05.014) | Cancer Cell | MSI and gene mutations, with spatial maps | Slide | — | — |
| 2025-11 | [CryoAID](https://doi.org/10.1038/s41467-025-66853-y) | Nat. Commun. | Molecular alterations of diffuse midline glioma from cryosections | Slide | — | — |
| 2025-09 | [EAGLE (EGFR)](https://doi.org/10.1038/s41591-025-03780-x) | Nat. Med. | EGFR mutation (lung adenocarcinoma) | Slide | Prospective | AUROC 0.77–0.88 across external cohorts and scanners; 0.89 in a prospective silent trial |
| 2025-05 | [MMRNet](https://doi.org/10.1016/j.xcrm.2025.102099) | Cell Rep. Med. | Mismatch repair deficiency (endometrial) | Slide | — | — |
| 2024-06 | [FGFR prescreening](https://doi.org/10.1038/s41467-024-49153-9) | Nat. Commun. | FGFR2/FGFR3 alterations for trial prescreening | Slide | Prospective | — |
| 2024-04 | [PD-L1 teacher–student MIL](https://doi.org/10.1038/s41467-024-46764-0) | Nat. Commun. | PD-L1 expression, pan-cancer | Slide | — | — |
| 2023-11 | [MSIntuit](https://doi.org/10.1038/s41467-023-42453-6) | Nat. Commun. | MSI (colorectal), pre-screening | Slide | — | — |
| 2023-09 | [Wagner 2023 transformer](https://doi.org/10.1016/j.ccell.2023.08.002) | Cancer Cell | MSI, BRAF and KRAS (colorectal) | Slide | External | AUROC MSI 0.97, BRAF 0.88, KRAS 0.80 on external cohorts; MSI 0.86–0.92 on biopsies |
| 2023-09 | [Pan-cancer proteogenomics](https://doi.org/10.1016/j.xcrm.2023.101173) | Cell Rep. Med. | Mutations and proteogenomic features (CPTAC) | Slide | — | — |
| 2023-04 | [MOMA](https://doi.org/10.1038/s41467-023-37179-4) | Nat. Commun. | Mutations, CNV, RNA and MSI (colorectal) | Slide | — | — |
| 2023-02 | [WiseMSI](https://doi.org/10.1016/j.xcrm.2022.100914) | Cell Rep. Med. | MSI (colorectal) | Slide | — | — |
| 2022-12 | [HRD luminal breast](https://doi.org/10.1016/j.xcrm.2022.100872) | Cell Rep. Med. | HRD (luminal breast cancer) | Slide | Held-out | — |
| 2022-11 | [PD-L1 breast](https://doi.org/10.1038/s41467-022-34275-9) | Nat. Commun. | PD-L1 status (breast) | Slide | — | — |
| 2022-06 | [Swarm learning](https://doi.org/10.1038/s41591-022-01768-5) | Nat. Med. | BRAF mutation and MSI (colorectal) | Slide | — | — |
| 2021-03 | [HIFs](https://doi.org/10.1038/s41467-021-21896-9) | Nat. Commun. | Molecular phenotypes, e.g. immune checkpoint expression and HRD | Slide | — | — |
| 2020-11 | [ReceptorNet](https://doi.org/10.1038/s41467-020-19334-3) | Nat. Commun. | ER, PR and HER2 status (breast) | Slide | External | ER AUROC 0.92 held-out, 0.85 external (TCGA) |
| 2020-08 | [Kather 2020 pan-cancer](https://doi.org/10.1038/s43018-020-0087-6) | Nat. Cancer | Actionable mutations, MSI and CIMP, pan-cancer | Slide | External | AUROC on DACHS: MSI 0.89, BRAF 0.77, CIMP 0.66 |
| 2019-07 | [Kather 2019 MSI](https://doi.org/10.1038/s41591-019-0462-y) | Nat. Med. | MSI (colorectal and gastric) | Slide | External | AUROC MSI colorectal 0.84 (DACHS); gastric 0.69 (Japanese cohort) |
| 2018-10 | [Coudray 2018](https://doi.org/10.1038/s41591-018-0177-5) | Nat. Med. | Six driver mutations including STK11, EGFR and KRAS (lung) | Slide | Held-out | AUROC STK11 0.86, EGFR 0.83, KRAS 0.73 (TCGA held-out) |

## Subtypes and signatures

A class or score derived from many molecules: an RNA subtype, a multi-gene signature, a methylation class.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2025-07 | [DLVPM-Twins](https://doi.org/10.1038/s42256-025-01052-4) | Nat. Mach. Intell. | Mutations and molecular states via a multimodal latent model | Slide | — | — |
| 2025-03 | [H&E DL Angioscore](https://doi.org/10.1038/s41467-025-57717-6) | Nat. Commun. | RNA angiogenesis signature (clear-cell renal) | Slide / region | External | Spearman 0.77 and 0.73 vs RNA Angioscore on two external cohorts |
| 2024-12 | [Urothelial subtypes](https://doi.org/10.1016/j.ccell.2024.10.016) | Cancer Cell | Four transcriptomic subtypes (urothelial carcinoma) | Slide | Held-out | — |
| 2024-07 | [DEPLOY](https://doi.org/10.1038/s41591-024-02995-8) | Nat. Med. | DNA methylation classes and CpG beta values (CNS tumours) | Slide | External | Median r 0.44–0.47 per CpG on external cohorts; 0.95 class accuracy on high-confidence cases |
| 2024-02 | [CAMIL regression](https://doi.org/10.1038/s41467-024-45589-1) | Nat. Commun. | Continuous biomarkers: HRD score, immune and proliferation signatures | Slide | Held-out | — |
| 2023-12 | [SlideGraph∞](https://doi.org/10.1016/j.xcrm.2023.101313) | Cell Rep. Med. | 200 co-expression gene-group states; TP53 and receptor status (breast) | Slide | External | AUROC TP53 0.82 held-out, 0.76 external (CPTAC); ER 0.85 external |
| 2023-10 | [HR+/HER2− subtypes](https://doi.org/10.1038/s41588-023-01507-7) | Nat. Genet. | Four integrated molecular subtypes (HR+/HER2− breast) | Slide | Held-out | — |
| 2023-06 | [PACpAInt](https://doi.org/10.1038/s41467-023-39026-y) | Nat. Commun. | Basal-like vs classical subtype, with spatial maps (pancreatic) | Slide / region | External | AUROC 0.81–0.86 on external cohorts and biopsies |

## Bulk molecular profiles

Thousands of genes per sample, compared with bulk RNA-seq.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2025-12 | [PathGen](https://doi.org/10.1038/s41467-025-66961-9) | Nat. Commun. | Generated bulk transcriptomic features | Slide | External | — |
| 2024-11 | [SEQUOIA](https://doi.org/10.1038/s41467-024-54182-5) | Nat. Commun. | Bulk transcriptome (~20,000 genes), 16 cancer types | Slide | External | On average 7,159 genes per cancer type significant in both TCGA and CPTAC |
| 2024-09 | [DeepPT](https://doi.org/10.1038/s43018-024-00793-2) | Nat. Cancer | Bulk transcriptome, used to predict treatment response | Slide | External | 1,408 (TransNEO) and 1,753 (NCI brain) of ~18,000 genes with r > 0.4 externally |
| 2024-07 | [RNAPath](https://doi.org/10.1038/s41467-024-50317-w) | Nat. Commun. | Bulk and spatial RNA expression, 23 normal tissues | Slide / region | External | — |
| 2020-08 | [HE2RNA](https://doi.org/10.1038/s41467-020-17678-4) | Nat. Commun. | Bulk transcriptome, 28 cancer types | Slide / tile | External | — |
| 2020-08 | [PC-CHiP](https://doi.org/10.1038/s43018-020-0085-8) | Nat. Cancer | Mutations, CNAs, whole-genome doubling and bulk expression, pan-cancer | Slide | Held-out | TP53 predictable in 12 of 27 cancer types; whole-genome doubling mean AUROC 0.73 |

## Spatial molecular maps

Expression or copy number per spot, region or pixel, compared with spatial transcriptomics or multiplexed protein imaging.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | [HisToSpatialCNV](https://doi.org/10.1038/s41551-026-01754-z) | Nat. Biomed. Eng. | Spatial copy-number state per spot | Spot | External | Macro-AUROC 0.83 held-out; 0.65–0.68 on external Visium and Xenium samples |
| 2026-07 | [Path2Space](https://doi.org/10.1016/j.cell.2026.04.023) | Cell | Spatial transcriptomics (breast) | Spot | External | Median gene r 0.37 held-out, 0.35 on an external 10x cohort |
| 2026-01 | [HEX](https://doi.org/10.1038/s41591-025-04060-4) | Nat. Med. | 40-plex CODEX protein maps (lung) | Region | External | Mean r 0.79 held-out; 0.74 on external TMAs; 0.66 across 34 tissue types |
| 2026-01 | [GigaTIME](https://doi.org/10.1016/j.cell.2025.11.016) | Cell | 21-channel virtual multiplex immunofluorescence | Pixel | External | — |
| 2026-01 | [STimage](https://doi.org/10.1038/s41467-026-68487-0) | Nat. Commun. | Spatial gene markers and cell types (breast) | Spot | External | Top-10 genes r ≈ 0.4 on external FFPE samples |
| 2025-11 | [MISO](https://doi.org/10.1038/s41467-025-66691-y) | Nat. Commun. | Spatial gene expression, multiscale | Spot | External | Mean r 0.45 held-out (top 100 genes); 0.27 on HEST-1k |
| 2025-08 | [HistoPlexer](https://doi.org/10.1038/s42256-025-01074-y) | Nat. Mach. Intell. | Multiplexed protein (imaging mass cytometry, melanoma) | Pixel | Held-out | — |
| 2025-07 | [OmiCLIP](https://doi.org/10.1038/s41592-025-02707-1) | Nat. Methods | Spatial transcriptomics via a visual–omics foundation model | Spot | — | — |
| 2024-09 | [VirtualMultiplexer](https://doi.org/10.1038/s42256-024-00889-5) | Nat. Mach. Intell. | Virtual multiplexed IHC (prostate) | Pixel | External | — |
| 2024-05 | [IGI-DL](https://doi.org/10.1016/j.xcrm.2024.101536) | Cell Rep. Med. | Spatial gene expression of the tumour microenvironment | Spot | — | — |
| 2020-08 | [ST-Net](https://doi.org/10.1038/s41551-020-0578-x) | Nat. Biomed. Eng. | Spatial expression of 250 genes (breast, legacy ST) | Spot | External | Mean r 0.33 over 234 genes on an external 10x sample |

## Single-cell profiles

Expression per cell, compared with single-cell spatial assays such as Xenium or CODEX.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11 | [Hist2Prot](https://doi.org/10.1038/s43018-026-01270-8) | Nat. Cancer | Single-cell spatial proteomics | Cell | External | Mean r 0.45 held-out; 0.40–0.42 on external G4X cohorts; 0.57–0.69 cross-platform |
| 2026-02 | [SpatialEx](https://doi.org/10.1038/s41592-025-02926-6) | Nat. Methods | Single-cell spatial transcriptome, proteome and metabolome | Cell | Serial section | — |
| 2026-01 | [sCellST](https://doi.org/10.1038/s41467-025-67965-1) | Nat. Commun. | Single-cell gene expression | Cell | External | Per-gene median r 0.06–0.15 on external Xenium slides |
| 2025-09 | [GHIST](https://doi.org/10.1038/s41592-025-02795-z) | Nat. Methods | Single-cell spatial gene expression | Cell | Held-out | Median r 0.70 for top 20 spatially variable genes (same section); mean r 0.16 over 785 genes on HER2ST |
| 2025-08 | [ROSIE](https://doi.org/10.1038/s41467-025-62346-0) | Nat. Commun. | 50-plex protein (CODEX), virtual staining | Patch | External | Mean r 0.22–0.27 per patch on external cohorts |

## Cell composition

Cell types, states or neighbourhoods defined by molecular data.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [CANVAS](https://doi.org/10.1016/j.cell.2026.05.031) | Cell | CODEX-defined cellular neighbourhoods | Region | Held-out | — |
| 2026-03 | [Hist2Cell](https://doi.org/10.1016/j.xgen.2025.101137) | Cell Genom. | Fine-grained cell-type abundance from ST deconvolution | Spot | External | — |
| 2025-02 | [HistoCell](https://doi.org/10.1038/s41467-025-57072-6) | Nat. Commun. | Cell types and transcriptional cell states | Cell | Held-out | — |
| 2023-07 | [GBM-CNN](https://doi.org/10.1038/s41467-023-39933-0) | Nat. Commun. | Glioblastoma transcriptional cell states | Region | External | — |

## Foundation models evaluated on molecular tasks

General pathology encoders whose evaluation includes molecular endpoints. Architecture, size and pre-training are covered in [Pathology](pathology.md); this table lists only the molecular tasks.

| Date | Model | Venue | Molecular tasks | Output scale | Strongest validation |
| --- | --- | --- | --- | --- | --- |
| 2026-11 | [THREADS](https://doi.org/10.1038/s43018-026-01252-w) | Nat. Cancer | Mutations and IHC status | Slide | — |
| 2026-10 | [ELF](https://doi.org/10.1016/j.ccell.2026.08.008) | Cancer Cell | Mutations, MSI, TMB, whole-genome doubling, aneuploidy | Slide | External |
| 2026-09 | [PRISM2](https://doi.org/10.1038/s41591-026-04521-4) | Nat. Med. | Genomic alterations from MSK-IMPACT (10 biomarkers) | Slide | Held-out |
| 2026-09 | [SlideChat](https://doi.org/10.1038/s43018-026-01220-4) | Nat. Cancer | ER, PR, HER2 and molecular subtypes (slide QA) | Slide | — |
| 2026-08 | [nnMIL](https://doi.org/10.1038/s41551-026-01767-8) | Nat. Biomed. Eng. | Receptor status, mutations, TMB, WGD, aneuploidy | Slide | External |
| 2026-07 | [EAGLE (framework)](https://doi.org/10.1038/s41467-026-74918-9) | Nat. Commun. | CRC, gastric, lung and breast mutations, MSI, CIMP, EBV, expression | Slide | External |
| 2026-04 | [Meta-encoder](https://doi.org/10.1038/s41467-026-71558-x) | Nat. Commun. | Protein/IHC and RNA tasks | Slide | — |
| 2026-04 | [PathPT](https://doi.org/10.1038/s41467-026-71715-2) | Nat. Commun. | Rare-cancer subtypes and mutations | Slide | — |
| 2026-04 | [KEEP](https://doi.org/10.1016/j.ccell.2026.01.019) | Cancer Cell | Molecularly defined subtypes (no separate molecular endpoint) | Slide | — |
| 2026-03 | [GPFM](https://doi.org/10.1038/s41551-025-01488-4) | Nat. Biomed. Eng. | Mutation tasks | Slide | — |
| 2025-12 | [mSTAR](https://doi.org/10.1038/s41467-025-66220-x) | Nat. Commun. | 18-gene mutations, IHC biomarkers, molecular subtypes, IDH | Slide | External |
| 2025-12 | [FLEX](https://doi.org/10.1038/s41467-025-66300-y) | Nat. Commun. | Mutations, MSI, IHC and subtypes | Slide | — |
| 2025-11 | [TITAN](https://doi.org/10.1038/s41591-025-03982-3) | Nat. Med. | Mutations and molecular subtypes | Slide | — |
| 2025-02 | [MUSK](https://doi.org/10.1038/s41586-024-08378-w) | Nature | ER, PR, HER2 status; IDH mutation | Slide | Held-out |
| 2024-10 | [Virchow](https://doi.org/10.1038/s41591-024-03141-0) | Nat. Med. | Genomic alterations from MSK-IMPACT | Slide | Held-out |
| 2024-10 | [CHIEF](https://doi.org/10.1038/s41586-024-07894-z) | Nature | Mutations and MSI | Slide | — |
| 2024-06 | [Prov-GigaPath](https://doi.org/10.1038/s41586-024-07441-w) | Nature | Mutations, TMB and subtypes | Slide | — |
| 2024-03 | [UNI](https://doi.org/10.1038/s41591-024-02857-3) | Nat. Med. | Mutations and molecular subtypes | Slide | — |
| 2024-03 | [CONCH](https://doi.org/10.1038/s41591-024-02856-4) | Nat. Med. | Molecularly defined brain tumour subtypes | Slide | Held-out |

## Benchmarks

Studies that rerun many models on the same molecular tasks, in the journals above.

| Date | Model | Venue | Molecular output | Output scale | Strongest validation | Headline result |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [PathBench](https://doi.org/10.1038/s41467-026-76004-6) | Nat. Commun. | 32 FMs, 41 TCGA/CPTAC tasks incl. IDH, MSI, PAM50, pathways | Slide | Held-out | — |
| 2026-06 | [Neidlinger 2026 FM benchmark](https://doi.org/10.1038/s41551-025-01516-3) | Nat. Biomed. Eng. | 19 FMs, 31 tasks: mutations, MSI, CIMP, EBV, expression | Slide | External | Median of 15 encoders: MSI 0.82 (DACHS); KRAS 0.53–0.61; PIK3CA 0.59 |
| 2026-06 | [PathoROB](https://doi.org/10.1038/s41467-026-73923-2) | Nat. Commun. | Robustness of FMs across medical centres; HRD (TCGA-BRCA) | Slide | Held-out | — |
| 2025-04 | [Campanella 2025 clinical benchmark](https://doi.org/10.1038/s41467-025-58796-1) | Nat. Commun. | Public FMs on hospital biomarker tasks: ER, PR, HER2, EGFR, KRAS, BRAF | Slide | Held-out | — |
| 2023-04 | [Niehues 2023 SSL-MIL benchmark](https://doi.org/10.1016/j.xcrm.2023.100980) | Cell Rep. Med. | 6 architectures: MSI, BRAF, KRAS, NRAS, PIK3CA (colorectal) | Slide | External | AUROC MSI 0.94 → 0.92, BRAF 0.82 → 0.81 (QUASAR CV → DACHS); KRAS 0.67, PIK3CA 0.57 within QUASAR |

## Reviews and benchmarks outside the list

Found with a PubMed search restricted to reviews and a web search, Nov 2026; scope judged from abstracts. Reviews are not listed above by design.

| Year | Kind | Paper | Venue | Scope |
| --- | --- | --- | --- | --- |
| 2026 | Review | [Histopathology-centered computational evolution of spatial omics: integration, mapping, and foundation models](https://doi.org/10.1093/bib/bbag387) | Brief Bioinform | Histology-centred spatial omics: integration, mapping, FMs |
| 2026 | Review | [Foundation models in computational pathology: methods, applications and clinical implications](https://doi.org/10.1136/bmjonc-2026-001102) | BMJ Oncol | FM methods and applications |
| 2026 | Review | [Foundation Models in Cancer Pathology: Techniques, Applications, and Future Directions](https://doi.org/10.34133/research.1332) | Research (Wash D C) | FMs in cancer pathology |
| 2026 | Review | [The state of the art in artificial intelligence and digital pathology in prostate cancer](https://doi.org/10.1038/s41585-025-01070-2) | Nat Rev Urol | AI and digital pathology in prostate cancer |
| 2025 | Review | [Artificial intelligence in digital pathology - time for a reality check](https://doi.org/10.1038/s41571-025-00991-6) | Nat Rev Clin Oncol | Whole field; clinical reality check |
| 2025 | Review | [Combining spatial transcriptomics with tissue morphology](https://doi.org/10.1038/s41467-025-58989-8) | Nat Commun | Spatial transcriptomics combined with morphology |
| 2024 | Review | [Artificial intelligence in liver cancer - new tools for research and patient management](https://doi.org/10.1038/s41575-024-00919-y) | Nat Rev Gastroenterol Hepatol | AI in liver cancer |
| 2023 | Review | [Artificial intelligence for digital and computational pathology](https://doi.org/10.1038/s44222-023-00096-8) | Nat Rev Bioeng | Whole field; molecular prediction is one section |
| 2023 | Systematic review | [Recent application of artificial intelligence on histopathologic image-based prediction of gene mutation in solid cancers](https://doi.org/10.1093/bib/bbad151) | Brief Bioinform | Gene mutations from H&E in solid cancers; literature to about 2022 |
| 2022 | Review | [Artificial intelligence in histopathology: enhancing cancer research and clinical oncology](https://doi.org/10.1038/s43018-022-00436-4) | Nat Cancer | Whole field; molecular prediction is one section |
| 2022 | Systematic review | [Artificial intelligence to identify genetic alterations in conventional histopathology](https://doi.org/10.1002/path.5898) | J Pathol | Genetic alterations from H&E; literature to about 2021 |
| 2022 | Review | [Deep Learning-Based Prediction of Molecular Tumor Biomarkers from H&E: A Practical Review](https://doi.org/10.3390/jpm12122022) | J Pers Med | Practical review of slide-level biomarker prediction |
| 2019 | Review | [Artificial intelligence in digital pathology - new tools for diagnosis and precision oncology](https://doi.org/10.1038/s41571-019-0252-y) | Nat Rev Clin Oncol | Whole field; molecular prediction is one section |
| 2026 | Benchmark | [Benchmarking pathology foundation models for predicting microsatellite instability in colorectal cancer histopathology](https://doi.org/10.1016/j.compmedimag.2025.102680) | Comput Med Imaging Graph | 3 FMs for MSI in colorectal cancer, TCGA to PAIP |
| 2026 | Benchmark | [Benchmarking Open-Source Pathology Foundation Models for Breast Cancer Biomarker Prediction from H&E Whole-Slide Images](https://doi.org/10.3390/cancers18152475) | Cancers (Basel) | 2 FMs for ER, PR, HER2 in TCGA-BRCA |
| 2026 | Benchmark | [Performance of deep learning methods for spatial gene expression prediction from histology images: a comprehensive assessment](https://doi.org/10.1093/bioadv/vbag202) | Bioinform Adv | 7 methods, 6 Visium/ST datasets, out-of-domain tests |
| 2026 | Bias analysis | [Confounding factors and biases abound when predicting molecular biomarkers from histological images](https://doi.org/10.1038/s41551-026-01616-8) | Nat Biomed Eng | Confounding between biomarkers and clinicopathological factors |
| 2025 | Benchmark | [Completing spatial transcriptomics data for gene expression prediction benchmarking](https://doi.org/10.1016/j.media.2025.103754) | Med Image Anal | SpaRED: 8 models on 26 public Visium datasets |
| 2024 | Benchmark | [A systematic pan-cancer study on deep learning-based prediction of multi-omic biomarkers from routine pathology images](https://doi.org/10.1038/s43856-024-00471-5) | Commun Med (Lond) | 12,093 models, 4,031 biomarkers, 32 TCGA cancers, CPTAC external |
| 2024 | Dataset resource | HEST-1k: a dataset for spatial transcriptomics and histology image analysis | NeurIPS | Public ST collection used as a shared test set |
| 2021 | Bias analysis | [The impact of site-specific digital histology signatures on deep learning model accuracy and bias](https://doi.org/10.1038/s41467-021-24698-1) | Nat Commun | Site-specific signatures in TCGA bias models |

## Common datasets

Datasets reused across the papers above, as training sets or external tests.

| Dataset | Paired molecular data | Used for | Access |
| --- | --- | --- | --- |
| TCGA | Mutations, MSI, RNA-seq, methylation, CNV; 33 cancer types | Training in most slide-level papers; held-out tests | Public; raw sequencing controlled |
| CPTAC | Proteogenomics; lung, colorectal, breast, brain, uterine and others | The most common external test after TCGA training | Public |
| DACHS | MSI, BRAF, KRAS, CIMP; colorectal (Germany) | External colorectal test in 4 papers | On request |
| QUASAR | MSI, BRAF, KRAS, NRAS, PIK3CA; colorectal trial (UK) | Training and cross-validation | On request |
| HEST-1k | Visium, Xenium and legacy ST, pan-tissue | External spatial test; Xenium single-cell tests | Public |
| HER2ST | Legacy ST, HER2-positive breast | Spatial training and benchmark | Public |
| 10x Genomics public samples | Visium and Xenium | Small external spatial tests; Xenium training | Public |
| Orion CRC | Same-section multiplexed immunofluorescence | External single-cell protein test | Public |

<sub>Generated from the H&E virtual omics literature catalogue (paper list, task extraction and dataset sheets). Corrections are welcome by pull request.</sub>
