<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from data/pathology.yaml in https://github.com/1nslyn/biomedical-ai-pipeline -->
<!-- Edits made here are overwritten by the next build. -->

# Pathology

Histopathology, whole-slide imaging and computational pathology.

**Maintainer:** [Leo Yin](https://shuolinyin.com) ([GitHub](https://github.com/1nslyn))

**21 entries** · [Back to index](README.md)

| Date | Model | Venue | Model size | Training slides | Pre-training objective | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 202609 | [ELF](#model-elf-202609) | Cancer Cell | 14.3M (ensemble slide enc.) | 53.7K (90/10 train/val) | MoCo v3 contrastive + weak supervision | classification, subtyping, biomarker prediction +4 |
| 202609 | [SlideChat](#model-slidechat-202609) | Nat. Cancer | _not published_ | 8,583 (TCGA) | cross-domain alignment → instruction tuning | visual question answering, report generation, captioning +5 |
| 202608 | [Tissue Clocks](#model-tissue-clocks-202608) | Nat. Med. | _not published_ | 25.7K (cross-validated) | none — ImageNet ConvNeXt, fine-tuned | regression, risk prediction, benchmarking |
| 202608 | [TRICARE](#model-tricare-202608) | Nat. Biomed. Eng. | _not published_ | none (121+334 2D levels) | none — frozen CONCH | classification, grading, risk prediction +1 |
| 202608 | [nnMIL](#model-nnmil-202608) | Nat. Biomed. Eng. | _not published_ | not stated (40K WSIs pooled) | none — frozen UNI/GigaPath/H0/Virchow2 | classification, subtyping, grading +5 |
| 202607 | [PRISM2](#model-prism2-202607) | Nat. Med. | 4.6B | 2.35M | contrastive → next-token | detection, subtyping, grading +4 |
| 202604 | [PRET](#model-pret-202604) | Nat. Cancer | _not published_ | none (training-free) | none — frozen DINO ViT-S/8 | detection, subtyping, segmentation +1 |
| 202603 | [HistBiases](#model-histbiases-202603) | Nat. Biomed. Eng. | _n/a_ | not stated (8.2K patients) | none — frozen CTransPath / ShuffleNet | biomarker prediction, mutation prediction, benchmarking |
| 202602 | [Neuropath-AI](#model-neuropath-ai-202602) | Lancet Oncol. | _not published_ | 5.8K samples (not slides) | not disclosed | classification, mutation prediction, gene expression prediction |
| 202602 | [KEEP](#model-keep-202602) | Cancer Cell | 414M | none (tile–text pairs) | knowledge-enhanced contrastive | segmentation, detection, subtyping +2 |
| 202602 | [CHAI](#model-chai-202602) | J. Clin. Oncol. | _not published_ | not stated (178 patients) | not disclosed | biomarker prediction, treatment response |
| 202511 | [TITAN](#model-titan-202511) | Nat. Med. | 48.5M (slide enc.) | 336K | iBOT → CoCa | classification, subtyping, retrieval +2 |
| 202511 | [SMMILe](#model-smmile-202511) | Nat. Cancer | 1.2M (MIL head) | 3.9K (cross-validated) | none — frozen ResNet-50 / CONCH | classification, detection, subtyping +1 |
| 202507 | [EAGLE](#model-eagle-202507) | Nat. Med. | 1.1B (tile enc.) | 5.17K | none — Prov-GigaPath, fine-tuned | biomarker prediction, mutation prediction |
| 202501 | [MUSK](#model-musk-202501) | Nature | 675M | ~33K | BEiT-3 MIM → contrastive | retrieval, visual question answering, classification +4 |
| 202409 | [CHIEF](#model-chief-202409) | Nature | _not published_ | 60.5K | unsupervised tiles → weak slide labels | classification, detection, subtyping +2 |
| 202407 | [Virchow](#model-virchow-202407) | Nat. Med. | 632M | ~1.5M | DINOv2 | detection, biomarker prediction, classification |
| 202405 | [Prov-GigaPath](#model-prov-gigapath-202405) | Nature | 1B (tile enc.) | 171K | DINOv2 → LongNet MAE | classification, subtyping, mutation prediction +1 |
| 202403 | [UNI](#model-uni-202403) | Nat. Med. | 307M | 100K | DINOv2 | segmentation, detection, grading +3 |
| 202403 | [CONCH](#model-conch-202403) | Nat. Med. | _not published_ | none (1.17M image–caption) | iBOT → CoCa | classification, retrieval, segmentation +1 |
| 202308 | [PLIP](#model-plip-202308) | Nat. Med. | _not published_ | none (208K image–text) | CLIP contrastive | classification, retrieval |

<sub><b>Model size</b> is the count the authors publish, with the component it covers in brackets — a slide encoder and a tile encoder are not comparable. <i>not published</i> means the access routes were worked and no author source states one; <i>n/a</i> means the paper does not introduce a model. <b>Training slides</b> counts whole slides used for training, so a model trained on tiles or image–text pairs shows what it used instead. <b>Pre-training objective</b> names the objective the authors trained with. <i>none</i> means the work does no pre-training of its own and reuses the frozen encoder named after it; <i>not disclosed</i> means no reachable source states one.</sub>

## Details

Click a model to expand its record.

<a id="model-elf-202609"></a>
<details>
<summary><b>ELF</b> — Ensemble learning of pathology foundation models for precision oncology <i>(Cancer Cell 2026-09)</i></summary>

**[Ensemble learning of pathology foundation models for precision oncology](https://www.cell.com/cancer-cell/fulltext/S1535-6108%2826%2900385-5)**

*Cancer Cell* · 2026-09 · [Xiangde Luo](https://scholar.google.com/citations?user=dD4HLS4AAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1016/j.ccell.2026.08.008](https://doi.org/10.1016/j.ccell.2026.08.008)

<table>
<tr><td><strong>Parameters</strong></td><td>14.3M</td></tr>
<tr><td><strong>Backbone</strong></td><td>An 8-head gated ABMIL slide encoder of 14.3M parameters sitting on top of five frozen tile-level pathology foundation models -- UNI, CONCH v1.5, Prov-GigaPath, Virchow2 and H-optimus-0. Their 768- to 1,536-dimensional patch embeddings are linearly interpolated to a common 768 dimensions and LayerNormed; attention is averaged across the eight heads and applied to both the unified and the native-width features, and the five per-model slide embeddings are concatenated into the final slide representation.</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>MoCo</code>, <code>contrastive</code>, <code>weakly supervised</code><br>No tile encoder is trained here: the five foundation models stay frozen and only the slide-level ensemble module is pre-trained. MoCo v3 momentum contrastive learning aligns slide embeddings under a dual positive-sampling scheme -- the same tissue region embedded by two different foundation models, giving model invariance, and two spatially overlapping regions embedded by the same model, giving view consistency -- with non-overlapping regions, both across and within models, as negatives. InfoNCE loss at temperature 0.2. Two auxiliary weakly supervised heads predict cancer versus normal and the anatomical site among 20 organs, weighted equally with the contrastive loss. 300 epochs on 8 NVIDIA H100 GPUs at an effective batch size of 768 slides and up to 4,096 patch embeddings per sample.</td></tr>
<tr><td><strong>Training data</strong></td><td>Formalin-fixed paraffin-embedded H&amp;E whole-slide images from 11 public datasets (ACROBAT, BCNB, COBRA, DHMC, GTEx, IMP-CRS, IPD-Brain, NMI-Bladder, PAIP, PANDA and four TCGA cohorts) across 20 anatomic sites, carrying only coarse clinical labels -- tissue of origin, and cancer versus normal. Downstream evaluation uses separate public benchmarks plus retrospective Stanford and MSKCC treatment cohorts that are not publicly available.<br><strong>53,699</strong> pretraining whole slide images · <strong>11</strong> pretraining datasets · <strong>20</strong> anatomical sites · <strong>4,697</strong> evaluation subtyping slides · <strong>11,530</strong> evaluation biomarker patients · <strong>1,736</strong> evaluation response patients</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>subtyping</code>, <code>biomarker prediction</code>, <code>mutation prediction</code>, <code>treatment response</code>, <code>regression</code>, <code>risk prediction</code><br>Everything is linear probing on the frozen ELF slide embedding -- logistic regression, or XGBoost for the regression task. Disease classification and subtyping on BCCC skin (2/3/5 classes), BRACS breast (7 classes) and EBRAINS brain (12/30 classes). Molecular biomarker detection over 84 TCGA biomarker-indication combinations spanning 28 clinically actionable alterations and 14 cancer types, plus BRAF, KRAS and MSI status across four colorectal cohorts, pan-cancer aneuploidy-score regression, whole-genome doubling and tumour mutational burden classification. Response prediction for platinum chemotherapy, trastuzumab and bevacizumab, and durable response to immune checkpoint inhibitors across 13 cohorts and 8 cancer types, with Kaplan-Meier stratification of progression-free and recurrence-free survival from the ELF risk score.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/lilab-stanford/ELF">github.com/lilab-stanford/ELF</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/luoxd96/ELF">huggingface.co/luoxd96/ELF</a></td></tr>
<tr><td><strong>License</strong></td><td>GPL-3.0</td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| BRACS 7-class breast and EBRAINS 30-class brain subtyping (held-out test sets) | balanced accuracy | 0.457 / 0.757 | BRACS (n = 87) 0.457 against TITAN 0.393, CHIEF 0.384 and Prov-GigaPath 0.323; EBRAINS 30-class (n = 573) 0.757 against 0.702 for Virchow2, the best single foundation model. Across all six subtyping tasks ELF beats TITAN by 2.2% on average. |
| TCGA pan-cancer biomarker detection, 84 biomarker-indication combinations | mean AUC | 0.719 | standard deviation 0.142, over 28 actionable alterations in 14 cancer types (6,510 patients, 7,721 WSIs); TITAN 0.701, Prov-GigaPath 0.678, CHIEF 0.676 (P < 0.05) |
| Colorectal cancer MSI and BRAF status, four cohorts (SR386, SR1482, MCO, TCGA-CRC) | mean AUC | 0.886 / 0.806 | MSI 0.886 and BRAF 0.806 averaged over the four cohorts, three of which are external; up to 7% (MSI) and 13% (BRAF) above the second-best model, CHIEF |
| Anticancer therapy response, four cohorts (platinum, trastuzumab, bevacizumab) | mean AUC | 0.759 | metastatic breast/platinum 0.710 (n = 77), ovary/platinum 0.761 (n = 158), breast/trastuzumab 0.749 (n = 85), ovary/bevacizumab 0.817 (n = 36); 7-9% above Prov-GigaPath and CHIEF |
| Immune checkpoint inhibitor durable response, 13 cohorts across 8 cancer types | mean AUC | 0.724 | n = 1,057 patients; baselines 0.612-0.664 for Prov-GigaPath, CHIEF and TITAN (P < 0.05). Durable response is PFS >= 6 months in advanced disease, PFS >= 24 months otherwise, and pCR in the breast neoadjuvant cohort. |

</details>

<a id="model-slidechat-202609"></a>
<details>
<summary><b>SlideChat</b> — SlideChat is a multimodal generative artificial intelligence assistant for whole-slide computational pathology across cancer types <i>(Nat. Cancer 2026-09)</i></summary>

**[SlideChat is a multimodal generative artificial intelligence assistant for whole-slide computational pathology across cancer types](https://www.nature.com/articles/s43018-026-01220-4)**

*Nat. Cancer* · 2026-09 · Ying Chen & Yuanfeng Ji · [doi:10.1038/s43018-026-01220-4](https://doi.org/10.1038/s43018-026-01220-4)

<table>
<tr><td><strong>Backbone</strong></td><td>Frozen CONCH patch-level encoder over 224x224 tiles, a LongNet slide-level encoder with sparse dilated attention that contextualises the tile tokens, and a multimodal projector ("connector") mapping slide tokens into the embedding space of a Qwen2.5-7B-Instruct LLM</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>next-token prediction</code>, <code>instruction tuning</code><br>No pathology pre-training of its own: the CONCH tile encoder is reused frozen and the work trains the slide encoder, connector and LLM in two supervised generative stages. Stage 1, Cross-Domain Alignment, fits 8,583 WSI-caption pairs with only the LongNet slide encoder and the LLM connector unfrozen (3 epochs, AdamW, lr 1e-3, ~3 h). Stage 2, Visual Instruction Learning, tunes the slide encoder, connector and LLM jointly on 265,650 instruction/QA pairs (1 epoch, AdamW, lr 2e-5, ~24 h). Both stages ran on 8 x A100 80GB with a per-GPU batch size of 1.</td></tr>
<tr><td><strong>Training data</strong></td><td>SlideInstruction, built by prompting GPT-4 over TCGA whole-slide images and their paired pathology reports across 31 cancer types, giving one caption per slide for stage 1 and open-ended plus multiple-choice instruction pairs for stage 2. Evaluation uses SlideBench, the accompanying benchmark, over five cohorts: TCGA, BCNB, CPTAC, the public HISTAI set and MOP, a private Eastern Hepatobiliary Surgery Hospital cohort.<br><strong>8,583</strong> WSI · <strong>8,583</strong> captions · <strong>265,650</strong> vqa pairs · <strong>274,233</strong> instruction samples · <strong>31</strong> cancer types · <strong>8,836</strong> benchmark closed questions · <strong>129</strong> benchmark open questions · <strong>3,149</strong> benchmark reports</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>visual question answering</code>, <code>report generation</code>, <code>captioning</code>, <code>classification</code>, <code>subtyping</code>, <code>grading</code>, <code>biomarker prediction</code>, <code>benchmarking</code><br>Slide-level multiple-choice visual question answering across microscopy, diagnosis and clinical question categories (disease detection and classification, staging, grading, differential diagnosis, biomarker analysis, treatment guidance, prognostic assessment); free-text open-ended question answering scored by pathologists on five dimensions; free-text pathology report generation; and WSI captioning as the stage-1 objective. The work also releases SlideBench, a five-cohort WSI benchmark, and evaluates GPT-4o, MedDr, Quilt-LLaVA, LLaVA-Med, HistoGPT and PRISM on it.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/uni-medical/SlideChat">github.com/uni-medical/SlideChat</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/General-Medical-AI/SlideChat_Weight">huggingface.co/General-Medical-AI/SlideChat_Weight</a></td></tr>
<tr><td><strong>License</strong></td><td>Apache-2.0</td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| SlideBench, five cohorts (8,836 closed questions, 129 open questions, 3,149 reports) | margin over leading baselines | +19.1% accuracy / +7.7% METEOR | the abstract's headline margins, for closed-ended accuracy and report-generation METEOR respectively; SlideChat also took the highest expert ratings on all five open-ended scoring dimensions |
| SlideBench-Closed (TCGA, N = 3,176) | accuracy | 0.741 | versus GPT-4o 0.557, MedDr 0.490, LLaVA-Med 0.298 and Quilt-LLaVA 0.256. Averaged over five conversational turns rather than turn 1, Supplementary Table 20 reports 0.720 +/- 0.011. |
| SlideBench-Closed external cohorts (BCNB / CPTAC / HISTAI) | accuracy | 0.789 / 0.517 / 0.761 | N = 4,232 / 240 / 769; best baseline per cohort 0.602 (GPT-4o), 0.358 (MedDr) and 0.505 (GPT-4o). The private MOP cohort (N = 419) is evaluated in the paper but no per-cohort figure is quotable from a reachable source. |
| SlideBench-Report (TCGA, N = 1,547) | METEOR | 0.214 | versus HistoGPT 0.097 and PRISM 0.025. On the external sets SlideChat scores 0.140 on CPTAC (HistoGPT 0.139, PRISM 0.059) and 0.106 on HISTAI (0.065, 0.018). |

</details>

<a id="model-tissue-clocks-202608"></a>
<details>
<summary><b>Tissue Clocks</b> — Histological aging signatures for monitoring tissue-specific aging and disease <i>(Nat. Med. 2026-08)</i></summary>

**[Histological aging signatures for monitoring tissue-specific aging and disease](https://www.nature.com/articles/s41591-026-04566-5)**

*Nat. Med.* · 2026-08 · [Ernesto Abila](https://scholar.google.com/citations?user=EaXz-AIAAAAJ&hl=en) & [André F. Rendeiro](https://scholar.google.at/citations?user=lj17pqEAAAAJ&hl=en) · [doi:10.1038/s41591-026-04566-5](https://doi.org/10.1038/s41591-026-04566-5)

<table>
<tr><td><strong>Backbone</strong></td><td>ImageNet-pretrained ConvNeXt base, fine-tuned as a tissue-type classifier and then frozen as a feature extractor; a slide is represented by its mean tile embedding at three magnifications, and regularised linear or ensemble regressors map that to age</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>supervised</code><br>Supervised transfer learning rather than pathology-specific pretraining. ImageNet architectures (AlexNet, VGG16, ResNet50, ResNet152, ConvNeXt tiny and ConvNeXt base) were fine-tuned to classify tissue type on a dataset balanced across tissue, age bracket and sex -- one epoch with the backbone frozen, then up to 100 epochs of fine-tuning -- and the fine-tuned ConvNeXt base was carried forward. Tiles of 224, 448 and 896 pixels at roughly 0.5 microns per pixel are embedded and averaged per slide, and the age regressor is fitted on those features.</td></tr>
<tr><td><strong>Training data</strong></td><td>GTEx post-mortem H&amp;E whole-slide images spanning 40 tissue types and 29 organs, paired with the cohort's transcriptomic, methylation and phenotypic records. Validated on separate brain, lung and skin cohorts.<br><strong>25,712</strong> WSI · <strong>983</strong> individuals · <strong>40</strong> tissue types · <strong>480,000,000</strong> image tiles</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>regression</code>, <code>risk prediction</code>, <code>benchmarking</code><br>Predicts chronological age from tissue morphology and treats the residual -- the "age gap" -- as a measure of biological aging; relates tissue-specific age acceleration to telomere length, subclinical pathology, comorbidities and lifestyle factors; predicts tissue-specific age gaps from blood gene expression via ridge regression; and benchmarks 7 classical vision models and 18 pathology foundation models as feature extractors for the same task.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>transcriptomics</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/rendeirolab/tissue-clocks">github.com/rendeirolab/tissue-clocks</a></td></tr>
<tr><td><strong>License</strong></td><td>PolyForm-Noncommercial-1.0.0</td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| GTEx, biological age from histology (cross-validated, all tissues) | mean absolute error | 4.88 years | coefficient of determination 0.69 |
| Feature-extractor comparison, 7 classical vision and 18 pathology foundation models | mean MAE across organs and models | 8.67 vs 5.74 | classical ImageNet models 8.67, pathology foundation models 5.74, against 4.88 for this paper's fine-tuned model. The authors caution that some foundation models were pretrained on data that includes GTEx, which may flatter them here. |
| External cohorts, GTEx-trained clocks applied unchanged | Pearson correlation with chronological age | 0.56 / 0.76 / 0.46 | brain (n = 70), lung (n = 40) and skin (n = 185) |

</details>

<a id="model-tricare-202608"></a>
<details>
<summary><b>TRICARE</b> — Deep-learning triage of three-dimensional pathology datasets for comprehensive and efficient pathologist assessments <i>(Nat. Biomed. Eng. 2026-08)</i></summary>

**[Deep-learning triage of three-dimensional pathology datasets for comprehensive and efficient pathologist assessments](https://www.nature.com/articles/s41551-026-01760-1)**

*Nat. Biomed. Eng.* · 2026-08 · Gan Gao & [Jonathan T. C. Liu](https://scholar.google.com/citations?user=p-JSi6IAAAAJ&hl=en) · [doi:10.1038/s41551-026-01760-1](https://doi.org/10.1038/s41551-026-01760-1)

<table>
<tr><td><strong>Backbone</strong></td><td>2.5D multiple-instance learning on a frozen CONCH patch encoder (512-d embeddings), adapted by a trained fully-connected ReLU layer; gated-attention ABMIL pools patches laterally within each 2D level, then a non-gated attention module fuses the target level with one neighbouring level above and below into a context-aware feature for a two-class linear head</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>none</code>, <code>weakly supervised</code><br>No pre-training of its own. A frozen CONCH pathology foundation model supplies 512-d patch embeddings, chosen over UNI and CTransPath in an ablation and preferred partly for its lower dimensionality in a low-data regime; only a small domain-adaptation layer, the lateral and depth attention modules and a two-class head are trained, using pathologist labels attached to whole 2D levels rather than to patches. Training is leave-one-out cross-validation by patient, separately per organ, with class-weighted sampling to offset the imbalance between high- and low-risk levels.</td></tr>
<tr><td><strong>Training data</strong></td><td>Non-destructive open-top light-sheet (OTLS) 3D pathology volumes of intact biopsies, fluorescence-stained with TO-PRO-3 and eosin, optically cleared, and false-coloured to mimic H&amp;E. Two cohorts: simulated core-needle prostate biopsies from UW prostatectomies (with an independent UPenn punch-biopsy cohort imaged on a different OTLS generation and a modified staining protocol) and endoscopic biopsy / EMR specimens of Barrett's esophagus from UW. Pathologist panels label individual 2D depth levels low- versus high-risk; images and annotations are released on Zenodo and the full prostate development volumes on TCIA.<br><strong>54</strong> prostate patients · <strong>112</strong> prostate biopsies · <strong>121</strong> prostate 2d levels labelled · <strong>81</strong> prostate 2d levels test · <strong>59</strong> prostate biopsies reader study · <strong>24</strong> esophagus patients · <strong>95</strong> esophagus specimens · <strong>334</strong> esophagus 2d levels labelled · <strong>77</strong> esophagus 2d levels test · <strong>30</strong> esophagus specimens reader study</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>grading</code>, <code>risk prediction</code>, <code>detection</code><br>Binary risk classification of every 2D depth level inside a 3D biopsy volume, yielding a risk-versus-depth profile from which the highest-risk levels are triaged for pathologist review. Two use cases: prostate cancer grading (Grade Group 1 versus &gt; 1) and screening for dysplasia/cancer in Barrett's esophagus. The model triages rather than diagnoses -- pathologists render the final diagnosis on the selected levels -- and patch attention heatmaps localise the morphology driving each score.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>microscopy</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/alecgao066/TRICARE">github.com/alecgao066/TRICARE</a></td></tr>
<tr><td><strong>License</strong></td><td>CC-BY-NC-4.0</td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Prostate development cohort, higher-grade vs low-grade (leave-one-out CV, 121 levels) | AUC | 0.939 vs 0.871 | TRICARE L→D versus the 2D single-level ABMIL baseline, p < 0.005; balanced accuracy 0.826 vs 0.750 and F2 0.882 vs 0.862. Preprint (CARP3D) figure, not yet checked against the published Results. |
| Esophagus development cohort, dysplasia/cancer screening (leave-one-out CV, 334 levels) | AUC | 0.921 vs 0.895 | TRICARE L→D versus the 2D baseline, p < 0.005; balanced accuracy 0.833 vs 0.779 and F2 0.765 vs 0.711. Preprint (CARP3D) figure, not yet checked against the published Results. |
| Prostate independent test cohort (UPenn, different OTLS system and staining protocol) | AUC | 0.847 vs 0.779 | TRICARE L→D versus the 2D baseline, p < 0.005, on 81 levels from 29 patients. The authors attribute the drop from 0.939 to staining-protocol and microscope differences between cohorts. Preprint (CARP3D) figure, not yet checked against the published Results. |
| Esophagus independent test cohort (held-out patients, same site and microscope) | AUC | 0.917 vs 0.882 | TRICARE L→D versus the 2D baseline, p < 0.01, on 77 levels from 30 specimens. Preprint (CARP3D) figure, not yet checked against the published Results. |
| Prostate reader study, 5-year biochemical recurrence predicted from pathologist diagnoses | balanced accuracy | 0.633 vs 0.614 | AI-triaged 3D pathology versus conventional 2D histopathology, 59 biopsies read by five pathologists with a one-month washout; F2 0.654 vs 0.588. Eight prostate cases were upgraded and five esophageal cases upgraded with none downgraded. Preprint (CARP3D) figure, not yet checked against the published Results. |

</details>

<a id="model-nnmil-202608"></a>
<details>
<summary><b>nnMIL</b> — nnMIL: a generalizable multiple instance learning framework for computational pathology <i>(Nat. Biomed. Eng. 2026-08)</i></summary>

**[nnMIL: a generalizable multiple instance learning framework for computational pathology](https://www.nature.com/articles/s41551-026-01767-8)**

*Nat. Biomed. Eng.* · 2026-08 · [Xiangde Luo](https://scholar.google.com/citations?user=dD4HLS4AAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1038/s41551-026-01767-8](https://doi.org/10.1038/s41551-026-01767-8)

<table>
<tr><td><strong>Backbone</strong></td><td>Gated-attention MIL aggregator over frozen foundation-model patch embeddings: attention is computed in a randomly sampled 256-dimensional feature subspace while aggregation stays in the encoder's full D-dimensional embedding space, followed by a linear head. At inference the full feature space is tiled by overlapping subspaces (stride H/4) whose predictions are ensembled, which also yields the uncertainty score</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>none</code><br>nnMIL pre-trains nothing of its own. Patch features come from four public pathology foundation models used frozen -- GigaPath, H-optimus-0, UNI and Virchow2 -- extracted through the CLAM pipeline; only the lightweight gated-attention aggregator and its linear head are trained, from slide-level labels alone, with cross-entropy for classification, Cox loss for survival and MSE for regression. AdamW at 3e-4 (1e-4 for prognosis), cosine schedule with a 5-epoch warm-up, batch size 32 and up to 100 epochs with early stopping, on 8 x 48 GB NVIDIA L40 GPUs. Following nnU-Net, every setting -- bag size (half the median patch count per slide), hidden dimension, dropout, sampler, optimizer and inference stride -- is derived by rule from a per-dataset fingerprint rather than searched.</td></tr>
<tr><td><strong>Training data</strong></td><td>Public H&amp;E whole-slide benchmarks only, grouped into 35 clinical tasks over 40 cohorts: BCCC, BRACS, EBRAINS, IMP-CRC2024 and PANDA for diagnosis and subtyping; BCNB, SURGEN, MCO, TCGA-CRC, MUV, TCGA-GBM/LGG and pan-cancer TCGA for molecular biomarkers; TCGA pan-cancer plus PLCO, NLST, MCO, SURGEN and TCGA-CRC for prognosis; CAMELYON16/17 for cross-institution generalization. No private cohort.<br><strong>40,000</strong> WSI · <strong>35</strong> clinical tasks · <strong>40</strong> evaluation cohorts · <strong>4</strong> foundation models · <strong>7</strong> baseline mil methods</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>subtyping</code>, <code>grading</code>, <code>biomarker prediction</code>, <code>mutation prediction</code>, <code>survival prediction</code>, <code>regression</code>, <code>benchmarking</code><br>A slide-level aggregator trained per task on frozen patch features: multi-class disease diagnosis and subtyping, Gleason grading, protein-expression and mutation prediction (ER/PR/HER2, BRAF/KRAS/IDH), pan-cancer genomic biomarkers (WGD, TMB, and aneuploidy as regression), and disease-specific survival across 16 TCGA cancer types plus four external colorectal and lung cohorts. Every task is also a benchmark of seven prior MIL methods under identical splits and hyperparameters, and the subspace-ensemble inference adds an uncertainty score used for selective prediction and for sub-stratifying the high-risk survival group.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/Luoxd1996/nnMIL">github.com/Luoxd1996/nnMIL</a></td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| All 35 tasks / 40 cohorts, per frozen foundation model (Supplementary Tables 22-25) | mean pooled score across 40 cohorts | 0.722 / 0.728 / 0.727 / 0.741 | GigaPath / H-optimus-0 / UNI / Virchow2, all P < 0.01 against the baselines. Best competing method per encoder, already given nnMIL's batch size of 32 by gradient accumulation, reaches 0.703, 0.715, 0.710 and 0.718 respectively. |
| Disease diagnosis and subtyping, 8 cohorts (BCCC, BRACS, EBRAINS, IMP-CRC2024, PANDA) | mean balanced accuracy | 0.807 - 0.820 | 0.807 GigaPath, 0.818 H-optimus-0, 0.820 UNI, 0.818 Virchow2, against 0.786, 0.798, 0.789 and 0.799 for the second-best method ABMIL. PANDA is scored with Cohen's kappa, where nnMIL is slightly behind ABMIL. |
| Molecular biomarker detection, 12 cohorts, Virchow2 features | mean AUC | 0.794 | nine biomarkers; P < 0.01. ABMIL reaches 0.767 and DSMIL 0.762 at their best setting. Aneuploidy is scored by Pearson's r, where nnMIL is second best (0.630 vs 0.637 for TransMIL). |
| TCGA pan-cancer prognosis, 16 cancer types, five-fold cross-validation, Virchow2 features | mean C-index | 0.670 | disease-specific survival over 7,927 WSIs from 6,602 patients; second-best DSMIL 0.626, P < 0.001. |
| Cross-encoder transfer to a fifth foundation model, CONCHv1.5, all 40 cohorts | mean pooled score across 40 cohorts | 0.721 | P < 0.001; best competing method DTFD 0.698. Held out from the four encoders the framework was developed on. |

</details>

<a id="model-prism2-202607"></a>
<details>
<summary><b>PRISM2</b> — End-to-end multimodal pathology foundation model with clinical dialogue <i>(Nat. Med. 2026-07)</i></summary>

**[End-to-end multimodal pathology foundation model with clinical dialogue](https://www.nature.com/articles/s41591-026-04521-4)**

*Nat. Med.* · 2026-07 · [Eugene Vorontsov](https://scholar.google.com/citations?user=5o1gS_sAAAAJ&hl=en) & [Siqi Liu](https://scholar.google.com/citations?hl=en&user=ADyo_cAAAAAJ) · [doi:10.1038/s41591-026-04521-4](https://doi.org/10.1038/s41591-026-04521-4)

<table>
<tr><td><strong>Parameters</strong></td><td>4.6B</td></tr>
<tr><td><strong>Backbone</strong></td><td>Virchow2 tile encoder, Perceiver slide encoder (541M, plus a 79M attention pooler), BioGPT language encoder and a Phi-3 Mini 3.8B decoder-only LLM reached through a 29M-parameter MLP adapter</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>contrastive</code>, <code>next-token prediction</code><br>Two-stage language-supervised multimodal pre-training: contrastive slide-report alignment against BioGPT text embeddings plus an autoregressive dialogue objective, then a second stage in which the contrastive objective is dropped, the slide encoder is frozen and Phi-3 Mini is fine-tuned. Trained on 56 A100 40GB GPUs in bf16.</td></tr>
<tr><td><strong>Training data</strong></td><td>H&amp;E whole-slide images with paired clinical reports, converted into question-answer pairs<br><strong>2,350,518</strong> WSI · <strong>685,507</strong> specimens · <strong>200,692</strong> patients · <strong>14,000,000</strong> QA pairs</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>detection</code>, <code>subtyping</code>, <code>grading</code>, <code>biomarker prediction</code>, <code>survival prediction</code>, <code>question answering</code>, <code>report generation</code><br>Prompt-based cancer detection and subtyping via yes/no and multiple-choice question answering; diagnostic, biomarker and survival prediction by linear probing on the base and diagnostic embeddings; staging and grading on external public data; pathology report completion following CAP guidelines.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/paige-ai/Prism2">huggingface.co/paige-ai/Prism2</a></td></tr>
<tr><td><strong>License</strong></td><td>CC-BY-NC-ND-4.0</td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>Default feature extractor is a DINO-pretrained ViT-S/8 pathology encoder; PRET adds an in-context tagger, in-context classifier, instance miner, attention aggregator and postprocessor</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>DINO</code>, <code>self-supervised</code><br>Training-free for downstream tasks; the feature extractor holds all model parameters and is never fine-tuned. The default encoder was pretrained self-supervised with DINO on unlabelled TCGA pathology images, and the framework also runs on UNI, GPFM, CONCH, TITAN, mSTAR and Prov-GigaPath.</td></tr>
<tr><td><strong>Training data</strong></td><td>No task-specific training images for PRET itself. Evaluated on 4,484 WSIs across 23 benchmarks. The paper does not state a numeric TCGA pretraining image count for the default encoder.<br><strong>4,484</strong> WSI (eval) · <strong>23</strong> benchmarks</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>detection</code>, <code>subtyping</code>, <code>segmentation</code>, <code>classification</code><br>Cancer screening, cancer subtyping, tumour segmentation, lymph node metastasis detection.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/xmed-lab/PRET">github.com/xmed-lab/PRET</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/yili7eli/PRET">huggingface.co/yili7eli/PRET</a></td></tr>
<tr><td><strong>License</strong></td><td>Apache-2.0</td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>Benchmarking study rather than a new model. Evaluates CLAM, SlideGraph-infinity and TITAN, with CTransPath and ShuffleNet patch encoders.</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>self-supervised</code>, <code>weakly supervised</code><br>CTransPath pretrained on histology via self-supervised learning, giving 768-dimensional patch features; ShuffleNet pretrained on ImageNet, giving 1,024-dimensional patch features; TITAN trained on 330,000 image-text pairs.</td></tr>
<tr><td><strong>Training data</strong></td><td>H&amp;E WSIs from TCGA, METABRIC, MSK and DFCI. Weakly supervised models trained on TCGA and validated on CPTAC and ABCTB.<br><strong>8,221</strong> patients</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>biomarker prediction</code>, <code>mutation prediction</code>, <code>benchmarking</code><br>Molecular biomarker and gene mutation prediction from WSIs, plus a confounding/stratification analysis against biomarker interdependency, grade and TMB.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/imuhdawood/HistBiases">github.com/imuhdawood/HistBiases</a></td></tr>
<tr><td><strong>Note</strong></td><td>Benchmarking and bias study, not a new foundation model.</td></tr>
</table>

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

*Lancet Oncol.* · 2026-02 · H. Lalchungnunga & [Kenneth Aldape](https://scholar.google.com/citations?user=vZM9E_AAAAAJ&hl=en) · [doi:10.1016/S1470-2045(25)00661-8](https://doi.org/10.1016/S1470-2045%2825%2900661-8)

<table>
<tr><td><strong>Backbone</strong></td><td>Hierarchical molecular inference: deep-learning models predict DNA methylation and gene expression from H&amp;E whole-slide images, and a hierarchical classifier maps those predictions to nine tumour families and 52 terminal CNS tumour types</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>self-supervised</code><br>WSI-pretrained encoder followed by molecular inference-based hierarchical classification.</td></tr>
<tr><td><strong>Training data</strong></td><td>Multi-institutional retrospective CNS tumour cohort. Training data from the NCI, the Children's Brain Tumor Network and the Digital Brain Tumour Atlas; test data from the NCI, Northwestern Medicine, UPMC and University College London, drawn from laboratory archives between May 17, 2024 and May 13, 2025.<br><strong>5,835</strong> training samples · <strong>5,516</strong> test samples · <strong>52</strong> tumour types</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>mutation prediction</code>, <code>gene expression prediction</code><br>CNS tumour family-level classification, 52 terminal CNS tumour types, IDH mutation prediction, inferred gene expression and DNA methylation.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://methylscape.ccr.cancer.gov/">methylscape.ccr.cancer.gov</a></td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>414M</td></tr>
<tr><td><strong>Parameter note</strong></td><td>414M is the released checkpoint's own total, not a figure from the paper: the HuggingFace API reports safetensors total 414,210,816 for Astaxanthin/KEEP and the model page renders "Model size 0.4B params". It covers both towers (ViT-L/16 vision encoder plus the BERT-family text encoder) at F32. Neither the Cancer Cell abstract nor the arXiv preprint states a parameter count anywhere.</td></tr>
<tr><td><strong>Backbone</strong></td><td>ViT-L/16 vision encoder initialised from UNI, paired with a PubMedBERT text encoder initialised from a disease-knowledge encoder</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>contrastive</code><br>Knowledge-enhanced vision-language pretraining. A BERT-family knowledge encoder is first trained by metric learning over a disease knowledge graph, then used to align visual and textual representations within hierarchical semantic spaces, so alignment happens at the level of a semantic group rather than a single noisy image-text pair.</td></tr>
<tr><td><strong>Training data</strong></td><td>Pathology image-text pairs from OpenPath and Quilt-1M, reorganized into semantically structured groups aligned with disease ontology hierarchies<br><strong>143,000</strong> groups · <strong>11,454</strong> diseases · <strong>139,143</strong> disease attributes</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>segmentation</code>, <code>detection</code>, <code>subtyping</code>, <code>retrieval</code>, <code>classification</code><br>Zero-shot slide-level cancer region segmentation, cancer detection and subtyping; tile-level cross-modal retrieval and zero-shot image classification.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/MAGIC-AI4Med/KEEP">github.com/MAGIC-AI4Med/KEEP</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/Astaxanthin/KEEP">huggingface.co/Astaxanthin/KEEP</a></td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>Not described in any reachable source; the abstract says only that the CHAI platform extracts quantitative histomorphologic features from whole-slide images</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>supervised</code><br>Histomorphologic features extracted from H&amp;E whole-slide images of diagnostic biopsies were screened in a development cohort for association with differential time to next treatment or death between F-chemo- and G-chemo-treated patients; the resulting continuous score was dichotomised and the threshold locked before validation.</td></tr>
<tr><td><strong>Training data</strong></td><td>H&amp;E-stained diagnostic biopsy whole-slide images from patients with advanced pancreatic ductal adenocarcinoma<br><strong>477</strong> patients · <strong>178</strong> development patients · <strong>299</strong> validation patients</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>biomarker prediction</code>, <code>treatment response</code><br>Predicts which of two first-line chemotherapy backbones -- fluoropyrimidine-based (F-chemo) or gemcitabine-based (G-chemo) -- a patient will benefit from, reported as a binary F-pref or G-pref result.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>48.5M</td></tr>
<tr><td><strong>Parameter note</strong></td><td>48.5M is the slide encoder and excludes the frozen CONCH v1.5 patch encoder, so it is not comparable with tile-encoder counts such as Virchow's 632M. The released checkpoint on HuggingFace reports a safetensors total of 158,866,176, which is a different scope -- that file also carries the text encoder and multimodal decoder used for zero-shot and report generation, and ships the patch encoder separately as conch_v1_5_pytorch_model.bin. The repo is gated, so its config.json and model card could not be read to confirm the split.</td></tr>
<tr><td><strong>Backbone</strong></td><td>ViT slide encoder (Transformer-based Image and Text Alignment Network) over CONCH v1.5 patch features</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>self-supervised</code>, <code>iBOT</code>, <code>CoCa</code>, <code>contrastive</code><br>Three stages: iBOT self-supervised pretraining on a 2D grid of patch features, then CoCa alignment against synthetic ROI captions generated by the PathChat pathology copilot, then alignment against whole-slide pathology reports.</td></tr>
<tr><td><strong>Training data</strong></td><td>Whole-slide images with paired pathology reports and synthetic captions<br><strong>335,645</strong> WSI · <strong>182,862</strong> pathology reports · <strong>423,122</strong> captions</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>subtyping</code>, <code>retrieval</code>, <code>report generation</code>, <code>survival prediction</code><br>Slide-level representation without fine-tuning, rare disease recognition, cancer outcome prediction and pathology report generation.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/mahmoodlab/TITAN">github.com/mahmoodlab/TITAN</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/MahmoodLab/TITAN">huggingface.co/MahmoodLab/TITAN</a></td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>1.2M</td></tr>
<tr><td><strong>Parameter note</strong></td><td>The paper reports SMMILe's own cost as "1.50 GFLOPS, 1.20 M parameters" for 1,024-dimension patch embeddings; the frozen ResNet-50/CONCH patch encoder is not counted, so this is not comparable to a tile-encoder parameter count.</td></tr>
<tr><td><strong>Backbone</strong></td><td>ResNet-50 and CONCH patch encoders with an instance-based multiple-instance-learning architecture using superpatch and refinement modules</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>weakly supervised</code><br>Feature extraction with pretrained encoders (ImageNet ResNet-50, pathology foundation model CONCH), then weakly supervised MIL training with slide-level labels.</td></tr>
<tr><td><strong>Training data</strong></td><td>8 datasets covering 6 cancer types<br><strong>3,850</strong> WSI · <strong>8</strong> datasets · <strong>6</strong> cancer types</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>detection</code>, <code>subtyping</code>, <code>grading</code><br>WSI-level classification and patch-level spatial quantification, including metastasis detection, subtype prediction and grading.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/ZeyuGaoAi/SMMILe">github.com/ZeyuGaoAi/SMMILe</a></td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Ovarian (UBC-OCEAN) | macro AUC | 94.11% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 1.13, second-best +2.20 |
| Prostate | macro AUC | 90.92% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 2.68, second-best +2.90 |
| Gastric Endoscopy (IH-ESD) | macro AUC | 92.75% | WSI classification with ImageNet ResNet-50 patch embeddings; +/- 3.59, second-best +11.18 |
| Breast (Camelyon16), spatial quantification | spatial macro F1 | 66.47% | ImageNet ResNet-50 patch embeddings; +/- 10.21, second-best method DSMIL 42.91%, the 23.56-point gap quoted in the running text |

</details>

<a id="model-eagle-202507"></a>
<details>
<summary><b>EAGLE</b> — Real-world deployment of a fine-tuned pathology foundation model for lung cancer biomarker detection <i>(Nat. Med. 2025-07)</i></summary>

**[Real-world deployment of a fine-tuned pathology foundation model for lung cancer biomarker detection](https://www.nature.com/articles/s41591-025-03780-x)**

*Nat. Med.* · 2025-07 · Gabriele Campanella & Chad Vanderbilt · [doi:10.1038/s41591-025-03780-x](https://doi.org/10.1038/s41591-025-03780-x)

<table>
<tr><td><strong>Parameters</strong></td><td>1.1B</td></tr>
<tr><td><strong>Backbone</strong></td><td>Prov-GigaPath ViT-g tile encoder (1.1B), fine-tuned end to end rather than frozen, embedding 224-pixel patches at 20x / 0.5 microns per pixel into 1,536 features; a gated multiple-instance-learning attention aggregator pools every patch in a slide into one slide-level representation, and a linear classifier outputs the probability of an EGFR mutation</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>weakly supervised</code><br>This work pre-trains nothing of its own. The tile encoder is initialized from the public Prov-GigaPath pathology foundation model, and the whole stack -- encoder, gated MIL attention aggregator and linear classifier -- is then trained end to end from slide-level EGFR mutation labels alone, with no patch-level annotation. Encoding is sharded across 23 GPUs in 16-bit precision so the encoder can be optimized jointly with the aggregator; 6,624 patches are sampled per slide per step, 20 epochs on 24 NVIDIA H100-80GB GPUs in about 9.28 h. Inference runs on a single GPU.</td></tr>
<tr><td><strong>Training data</strong></td><td>H&amp;E whole-slide images of lung adenocarcinoma from four clinical cohorts -- MSKCC (training, validation, threshold calibration and the prospective silent trial), Mount Sinai Health System, Sahlgrenska University Hospital and the Technical University of Munich -- plus public TCGA-LUAD for external testing. Every slide is paired with targeted-NGS ground truth for EGFR: MSK-IMPACT at MSKCC, Oncomine Comprehensive v3 at MSHS, Oncomine Focus at SUH, TruSight Oncology 500 at TUM, and TCGA whole-exome calls clinically annotated through OncoKB. Slides were digitized on Aperio AT2 and GT450, Philips Ultrafast, Pramana and Hamamatsu NanoZoomer S210 scanners, so scanner variability is part of the evaluation.<br><strong>8,461</strong> WSI · <strong>5,174</strong> training slides · <strong>4,867</strong> training patients · <strong>1,742</strong> internal validation slides · <strong>1,484</strong> external validation slides · <strong>765</strong> threshold calibration slides · <strong>315</strong> prospective silent trial slides · <strong>197</strong> prospective silent trial primary slides</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>biomarker prediction</code>, <code>mutation prediction</code><br>Binary prediction of EGFR mutation status in lung adenocarcinoma directly from an H&amp;E whole-slide image, against targeted sequencing as ground truth. Validated retrospectively at MSKCC, then externally across three hospitals, five scanner models and TCGA, with stratifications by primary versus metastatic site, tissue area, EGFR variant class and slide artifact. Deployed in a 4-month prospective silent trial at MSKCC (May-August 2024) in which slides were picked up automatically on an hourly cadence and scored in real time beside the Idylla PCR rapid test. The score drives an AI-assisted screening workflow: below a tuned NPV threshold or above a tuned PPV threshold the sample skips rapid testing, otherwise the rapid test confirms it.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/chadvanderbilt/EAGLE">github.com/chadvanderbilt/EAGLE</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/MCCPBR/EAGLE">huggingface.co/MCCPBR/EAGLE</a></td></tr>
<tr><td><strong>License</strong></td><td>CC-BY-NC-SA-4.0</td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MSKCC internal retrospective validation (1,742 slides) | AUC | 0.847 | 0.90 on primary samples against 0.75 on metastatic specimens |
| External retrospective validation, three hospitals plus TCGA (1,484 slides) | AUC | 0.870 | MSHS 0.870 / 0.877 / 0.884 on Philips Ultrafast, Aperio GT450 and Pramana scans of the same slides; SUH 0.772; TUM 0.808; TCGA-LUAD 0.860, rising to 0.918 once slides with morphology-obscuring artifacts are dropped |
| Prospective silent trial, MSKCC primary samples, May-August 2024 (N = 197) | AUC | 0.890 | MSK-IMPACT as ground truth; the retrospective pretrial primary cohort (N = 374) gave 0.896, and the full pretrial cohort (N = 765) 0.853 |
| AI-assisted EGFR screening workflow, silent trial (least stringent thresholds) | rapid-test reduction / NPV / PPV | 43% / 0.963 / 0.984 | the most stringent operating point gives 18% / 0.971 / 1.000; both threshold pairs were fixed on the pretrial cohort, not on the trial cohort, and both sit inside the non-inferiority region for the Idylla rapid test |
| Median turnaround time from molecular accession, silent trial | hours | 0.74 vs 48.78 vs 435.26 | EAGLE 0.74 h (44 min), Idylla PCR rapid test 48.78 h, MSK-IMPACT NGS 435.26 h. Methods report a median 68 s to process one slide on a single RTX 3090. |

</details>

<a id="model-musk-202501"></a>
<details>
<summary><b>MUSK</b> — A vision-language foundation model for precision oncology <i>(Nature 2025-01)</i></summary>

**[A vision-language foundation model for precision oncology](https://www.nature.com/articles/s41586-024-08378-w)**

*Nature* · 2025-01 · [Jinxi Xiang](https://scholar.google.com/citations?user=Zn-0LioAAAAJ&hl=en) & [Ruijiang Li](https://scholar.google.com/citations?user=Y89JnCYAAAAJ&hl=en) · [doi:10.1038/s41586-024-08378-w](https://doi.org/10.1038/s41586-024-08378-w)

<table>
<tr><td><strong>Parameters</strong></td><td>675M</td></tr>
<tr><td><strong>Backbone</strong></td><td>BEiT-3-style multimodal transformer -- shared self-attention blocks with two independent vision and language experts; 24 layers, hidden size 1024, FFN 4096, 16 attention heads, 384x384 input at 16x16 patches</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>MIM</code>, <code>contrastive</code><br>Masked image modelling followed by vision-language contrastive alignment.</td></tr>
<tr><td><strong>Training data</strong></td><td>50 million TCGA H&amp;E image patches from ~33,000 WSIs and 1 billion text tokens from PubMed Central OA articles for masked pretraining, then ~1 million image-text pairs from Quilt1M (802k) and PathAsst (207k) for contrastive alignment<br><strong>50,000,000</strong> image patches · <strong>33,000</strong> WSI · <strong>11,577</strong> patients · <strong>1,000,000,000</strong> text tokens · <strong>1,001,800</strong> articles · <strong>1,000,000</strong> pairs</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>retrieval</code>, <code>visual question answering</code>, <code>classification</code>, <code>biomarker prediction</code>, <code>prognosis</code>, <code>survival prediction</code>, <code>treatment response</code><br>Cross-modal retrieval, visual question answering, histopathology image classification and molecular biomarker prediction, plus clinical outcome prediction -- melanoma relapse, pan-cancer prognosis and immunotherapy response.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/lilab-stanford/MUSK">github.com/lilab-stanford/MUSK</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/xiangjx/musk">huggingface.co/xiangjx/musk</a></td></tr>
<tr><td><strong>License</strong></td><td>CC-BY-NC-ND-4.0</td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>CTransPath tile encoder with a weakly supervised whole-slide aggregation module</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>self-supervised</code>, <code>weakly supervised</code><br>Two complementary pretraining strategies: unsupervised pretraining for tile-level features and weakly supervised pretraining for whole-slide pattern recognition.</td></tr>
<tr><td><strong>Training data</strong></td><td>Unsupervised tile-level pretraining then weakly supervised slide-level pretraining, across 14 cohorts and 19 anatomical sites<br><strong>15,000,000</strong> image tiles · <strong>60,530</strong> WSI · <strong>19</strong> anatomical sites</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>detection</code>, <code>subtyping</code>, <code>prognosis</code>, <code>mutation prediction</code><br>Cancer cell detection, tumour origin identification, molecular profile prediction and survival outcome prediction across cancer types.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/hms-dbmi/CHIEF">github.com/hms-dbmi/CHIEF</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://hub.docker.com/r/chiefcontainer/chief/">hub.docker.com/r/chiefcontainer/chief</a></td></tr>
<tr><td><strong>License</strong></td><td>GPLv3</td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>632M</td></tr>
<tr><td><strong>Backbone</strong></td><td>ViT-H/14</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>DINOv2</code><br>Self-supervised DINOv2 pretraining on H&amp;E whole-slide images.</td></tr>
<tr><td><strong>Training data</strong></td><td>H&amp;E-stained whole-slide images from a clinical archive<br><strong>1,500,000</strong> WSI · <strong>100,000</strong> patients · <strong>2,000,000,000</strong> training tiles</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>detection</code>, <code>biomarker prediction</code>, <code>classification</code><br>Pan-cancer detection including rare cancers, and biomarker prediction.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/Paige-AI/paige-ml-sdk">github.com/Paige-AI/paige-ml-sdk</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/paige-ai/Virchow">huggingface.co/paige-ai/Virchow</a></td></tr>
<tr><td><strong>License</strong></td><td>Apache-2.0</td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>1B</td></tr>
<tr><td><strong>Parameter note</strong></td><td>Two components, counted separately. The Nature paper and its Supplementary Information give no count for the released model; both figures come from the same team's follow-up paper (GigaPath-Flash, arXiv:2607.18218), whose Table 1 lists "GigaPath | Whole-Slide FM | ViT-g (1B) + LongNet (86M) | Apache-2.0 | Nature, 2024" and whose section 2.1 calls it "the frozen GigaPath ViT-g (1B) teacher". The 1B is the tile encoder; the 86M is the LongNet slide encoder. Not comparable with a tile-encoder-only count such as UNI's 307M without saying which half you mean.</td></tr>
<tr><td><strong>Backbone</strong></td><td>ViT-g tile encoder with a 12-layer, 768-dim LongNet slide encoder over 1,536-dim tile embeddings</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>DINOv2</code>, <code>MAE</code><br>DINOv2 tile-level pretraining followed by masked autoencoder pretraining with LongNet over whole slides.</td></tr>
<tr><td><strong>Training data</strong></td><td>Real-world H&amp;E slides from the Providence health network<br><strong>171,189</strong> WSI · <strong>1,384,860,229</strong> image tiles</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>subtyping</code>, <code>mutation prediction</code>, <code>biomarker prediction</code><br>26 prediction tasks spanning pathomics and cancer subtyping.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/prov-gigapath/prov-gigapath">github.com/prov-gigapath/prov-gigapath</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/prov-gigapath/prov-gigapath">huggingface.co/prov-gigapath/prov-gigapath</a></td></tr>
</table>

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

<table>
<tr><td><strong>Parameters</strong></td><td>307M</td></tr>
<tr><td><strong>Backbone</strong></td><td>ViT-L/16</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>DINOv2</code><br>Self-supervised DINOv2 pretraining on the Mass-100K slide corpus.</td></tr>
<tr><td><strong>Training data</strong></td><td>Mass-100K, H&amp;E whole-slide images from Massachusetts General Brigham<br><strong>100,426</strong> WSI · <strong>100,130,900</strong> tissue patches</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>segmentation</code>, <code>detection</code>, <code>grading</code>, <code>subtyping</code>, <code>biomarker prediction</code>, <code>classification</code><br>34 tasks including nuclear segmentation, primary and metastatic cancer detection, cancer grading and subtyping, biomarker screening, molecular subtyping, organ transplant assessment and pan-cancer classification.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/mahmoodlab/UNI">github.com/mahmoodlab/UNI</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/MahmoodLab/UNI">huggingface.co/MahmoodLab/UNI</a></td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>ViT-B/16 image encoder, 12-layer text encoder and 12-layer multimodal decoder</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>iBOT</code>, <code>CoCa</code><br>iBOT visual pretraining followed by CoCa image-text pretraining.</td></tr>
<tr><td><strong>Training data</strong></td><td>Pathology image-caption pairs curated from educational sources and PubMed<br><strong>1,170,647</strong> pairs</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>retrieval</code>, <code>segmentation</code>, <code>captioning</code><br>Tile- and slide-level classification, cross-modal image-to-text and text-to-image retrieval, image segmentation and captioning.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/mahmoodlab/CONCH">github.com/mahmoodlab/CONCH</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/MahmoodLab/CONCH">huggingface.co/MahmoodLab/CONCH</a></td></tr>
</table>

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

<table>
<tr><td><strong>Backbone</strong></td><td>CLIP ViT-B/32 image encoder with a 12-layer, 512-dim Transformer text encoder</td></tr>
<tr><td><strong>Pre-training</strong></td><td><code>CLIP</code>, <code>contrastive</code><br>CLIP fine-tuned on the OpenPath image-text corpus.</td></tr>
<tr><td><strong>Training data</strong></td><td>OpenPath, pathology images paired with natural-language descriptions sourced from medical Twitter<br><strong>208,414</strong> pairs</td></tr>
<tr><td><strong>Downstream tasks</strong></td><td><code>classification</code>, <code>retrieval</code><br>Zero-shot and transfer-learning classification of pathology images, and cross-modal image-to-text retrieval.</td></tr>
<tr><td><strong>Modalities</strong></td><td><code>histopathology</code>, <code>text</code></td></tr>
<tr><td><strong>Code</strong></td><td><a href="https://github.com/PathologyFoundation/plip">github.com/PathologyFoundation/plip</a></td></tr>
<tr><td><strong>Weights</strong></td><td><a href="https://huggingface.co/vinid/plip">huggingface.co/vinid/plip</a></td></tr>
</table>

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Zero-shot classification on four external datasets | F1 | 0.565-0.832 | range across Kather colon (0.565), PanNuke (0.656), WSSS4LUAD (0.734) and DigestPath (0.832); prior CLIP model scores 0.030-0.481 |
| Supervised classifier on PLIP embeddings | F1 improvement | 2.5% | versus other supervised model embeddings |

</details>

---

This page is generated. Add a paper by editing [`data/pathology.yaml`](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/data/pathology.yaml) in the [pipeline repository](https://github.com/1nslyn/biomedical-ai-pipeline) and rebuilding — edits made here are overwritten. The schema and house rules are in [CONTRIBUTING.md](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/CONTRIBUTING.md).
