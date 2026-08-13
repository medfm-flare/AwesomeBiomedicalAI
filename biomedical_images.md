# Biomedical Images — Other

Ultrasound, microscopy, retinal imaging, optical coherence tomography (OCT), dermatology, endoscopy, cytology, and other biomedical imaging modalities.

**Maintainers:** @Terry Fu · [Zaiyou He](https://github.com/zaiyouzy)

**16 papers** · **Last updated: 2026-08** · [Back to index](README.md)

## Paper overview

Click a model name to jump to its expandable record. A dash (`—`) means that the corresponding value has not been confirmed from the paper or an official release.

| Date | Model | Venue | Modality | Training data | Training / adaptation | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [Retina4IRD](#model-retina4ird-202607) | Nat. Med. | CFP, OCT | 1,843 patients; 3,376 eyes | RETFound pretraining; supervised fine-tuning | genotype prediction, clinical decision support |
| 2026-07 | [MLLM-EDR](#model-mllm-edr-202607) | Nat. Commun. | Endoscopy, text | 203,838 images; 4,461 reports | MedCLIP + BLIP-2; multitask learning; LoRA | diagnosis, report generation |
| 2026-07 | [ULTRA](#model-ultra-202607) | Cell | SRS, virtual H&E, 3D histology | pipeline-specific datasets; 17-patient validation | self-, semi-, and supervised multistage learning | image restoration, virtual staining, tumor mapping |
| 2026-06 | [AIOC](#model-aioc-202606) | Nat. Commun. | Fetal ultrasound | 45,139 images; 9,215 fetuses | supervised multitask learning | structure detection, view classification, diagnosis |
| 2026-05 | [MouseMapper](#model-mousemapper-202605) | Nature | 3D light-sheet microscopy | module-specific 3D annotations | VesselFM transfer; LwF; supervised 3D U-Net | nerve, immune-cell, organ and tissue segmentation |
| 2026-05 | [MicroSplit](#model-microsplit-202605) | Nat. Methods | Fluorescence microscopy | 24 2D + 6 3D tasks | task-specific supervised unmixing and denoising | semantic unmixing, uncertainty estimation |
| 2026-04 | [BUSGen](#model-busgen-202604) | Nat. Biomed. Eng. | Breast ultrasound | 3.5M images | DDPM | screening, diagnosis, prognosis |
| 2026-04 | [Reti-Pioneer](#model-reti-pioneer-202604) | Nat. Med. | Color fundus photography | 107,730 images; 53,865 individuals | not stated in current entry | multidisease screening, longitudinal risk prediction |
| 2026-03 | [FluoResFM](#model-fluoresfm-202603) | Nat. Commun. | Fluorescence microscopy | 4,303,086 paired patches | supervised paired restoration; BiomedCLIP text encoder | denoising, deconvolution, super-resolution +4 |
| 2026-03 | [OVFM](#model-ovfm-202603) | Nat. Biomed. Eng. | Ophthalmic surgical video | 1.1M clips; 144 surgery types | self-supervised video pretraining | recognition, detection, assessment, segmentation |
| 2026-02 | [Autonomous cytopathology pipeline](#model-cytopathology-202602) | Nature | Whole-slide cytology | 242,669 annotated nuclei + multicentre slides | supervised detection and classification | cervical cytology classification and triage |
| 2025-06 | [PanDerm](#model-panderm-202506) | Nat. Med. | Dermatology | ~2.1M images | self-supervised learning | skin-cancer diagnosis and screening |
| 2025-01 | [FMUE](#model-fmue-202501) | Cell Rep. Med. | OCT | 102,468 OCT images | RETFound SSL + LoRA | diagnosis, OOD detection |
| 2024-08 | [RET-CLIP](#model-ret-clip-202408) | MICCAI | Retinal imaging, text | 193,865 patients' CFP-report pairs | contrastive learning; tripartite optimization | diagnosis, multilabel classification |
| 2024-05 | [EndoFM-LV](#model-endofm-lv-202405) | IEEE entry (verify) | Endoscopy video | 6,469 videos; >13M frames | masked video modeling; teacher–student learning | classification, segmentation, detection, workflow recognition |
| 2023-09 | [RETFound](#model-retfound-202309) | Nature | CFP, OCT | 1.6M unlabelled images | self-supervised learning | retinal disease detection |

## Details

### 2026 additions

<a id="model-retina4ird-202607"></a>
<details>
<summary><b>Retina4IRD</b> — Inherited retinal disease diagnosis and clinician decision support <i>(Nat. Med. 2026-07)</i></summary>

**[AI-based clinician decision support system for diagnosis of inherited retinal diseases: a multicenter, randomized trial](https://www.nature.com/articles/s41591-026-04545-w)**

*Nature Medicine* · 2026-07 · [Huixun Jia](https://orcid.org/0000-0001-9341-5587) & [Xiaodong Sun](https://orcid.org/0000-0001-5015-0945) · [doi:10.1038/s41591-026-04545-w](https://doi.org/10.1038/s41591-026-04545-w)

| | |
| --- | --- |
| **Model type** | Clinical AI decision-support system |
| **Backbone** | ViT-L/16 image models for color fundus photography and OCT; the released implementation combines image predictions with clinical metadata using an ensemble/stacking model |
| **Training / adaptation** | Vision Transformer initialized from RETFound and fine-tuned for 17 genotype categories; CFP and OCT image predictions can be combined with patient metadata |
| **Training data** | Multimodal CFP and OCT data from **1,843 genetically confirmed patients** and **3,376 eyes** across China, South Korea, and Poland. This is the reported development-and-validation cohort, not a training-only count. |
| **Downstream tasks** | Prediction of 17 genotype categories; top-k genetic diagnosis before genetic testing; clinician decision support; downstream management planning |
| **Modalities** | `color fundus photography`, `OCT`, `clinical metadata` |
| **Code** | [github.com/zycl2001/Retina4IRD](https://github.com/zycl2001/Retina4IRD) |
| **Weights** | [huggingface.co/zycl2001/Retina4IRD](https://huggingface.co/zycl2001/Retina4IRD) |
| **Data** | [Zenodo minimum dataset](https://zenodo.org/records/20489924); full clinical data require a material transfer agreement |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Internal validation | top-5 prediction accuracy | 90.4% | 95% CI 89.6–91.2% |
| External validation | top-5 prediction accuracy | 85.6% | 95% CI 85.0–86.3% |
| Randomized trial | top-5 genetic accuracy | 88.5% vs 67.3% | Retina4IRD-assisted specialist vs specialist alone; 295 participants in final analysis |

> **Verification note:** The paper does not report a total parameter count in the publicly accessible article information. The cohort count above must not be described as training-only data.

</details>

<a id="model-mllm-edr-202607"></a>
<details>
<summary><b>MLLM-EDR</b> — Automatic esophagogastroduodenoscopy diagnosis and reporting <i>(Nat. Commun. 2026-07)</i></summary>

**[Bootstrapping multimodal large language model with medical knowledge for automatic esophagogastroduodenoscopy diagnosis and reporting](https://www.nature.com/articles/s41467-026-75377-y)**

*Nature Communications* · 2026-07 · Miaojing Shi & [Shuchang Xu](https://orcid.org/0000-0003-3170-2278) · [doi:10.1038/s41467-026-75377-y](https://doi.org/10.1038/s41467-026-75377-y)

| | |
| --- | --- |
| **Model type** | Medical multimodal large-language-model system |
| **Backbone** | MedCLIP ViT visual encoder and text encoder; temporal adaptive pooling; self-attention and three visual–text interaction blocks; BLIP-2 multimodal decoder; linear classification heads |
| **Training / adaptation** | End-to-end multitask learning using expert-verified medical descriptions generated with GPT-4; cross-entropy and vision–text contrastive objectives; BLIP-2 decoder adapted with LoRA (rank 16) while its original pretrained weights are frozen |
| **Training data** | **4,461 participants**, **203,838 EGD images**, and **4,461 reports** from four hospitals. The primary TJ-EGD dataset contains 118,802 images and 2,631 participants, including 1,839 training participants. |
| **Downstream tasks** | Eight-site anatomical recognition; six-type gastric-mucosa classification; diagnosis of 19 gastrointestinal diseases; EGD report generation; video-level clinical assistance |
| **Modalities** | `endoscopy images`, `clinical reports`, `medical text` |
| **Code** | [Zenodo software record](https://doi.org/10.5281/zenodo.21023152) |
| **Data** | Available by request under the restrictions described in the paper |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Nineteen GI diseases | average diagnostic accuracy | 0.882 | compared with 0.720 for evaluated AI baselines and 0.784 for junior endoscopists |
| Report generation | completeness and facticity | senior-endoscopist level | reported by the authors; no single aggregate number is stated in the abstract |
| Clinical workflow | reporting time | 13.48 seconds | compared with approximately 7 minutes for endoscopists |

> **Verification note:** Nature currently labels this as an unedited early-access version. Small details may change when the version of record is fully edited.

</details>

<a id="model-aioc-202606"></a>
<details>
<summary><b>AIOC</b> — Fetal orofacial-cleft detection and medical education <i>(Nat. Commun. 2026-06)</i></summary>

**[Artificial intelligence for detecting fetal orofacial clefts and advancing medical education](https://www.nature.com/articles/s41467-026-74119-4)**

*Nature Communications* · 2026-06 · [Yuanji Zhang](https://orcid.org/0000-0002-5398-7588) & [Dong Ni](https://orcid.org/0000-0002-9146-6003) · [doi:10.1038/s41467-026-74119-4](https://doi.org/10.1038/s41467-026-74119-4)

| | |
| --- | --- |
| **Model type** | Clinical ultrasound diagnostic and educational AI system |
| **Backbone** | Dual-branch system: YOLOX structure-detection branch plus a Mamba-Inspired Linear Attention (MILA) classification branch; an LSTM models relationships between global and local structural features |
| **Training / adaptation** | Supervised multitask training for rotated-box structure detection and four-view classification, followed by expert-knowledge-based case-level diagnosis. No external pretraining is reported. |
| **Training data** | **45,139 ultrasound images** from **9,215 fetuses** across **22 hospitals**. Internal OC-6000: 28,994 images from 6,010 fetuses, split 80/10/10 by case. External OC-3000: 15,848 images from 3,168 fetuses. OC-Early: 297 images from 37 fetuses. |
| **Downstream tasks** | Detection of five key structures; classification of four ultrasound views; Control/cleft lip/cleft lip-and-palate diagnosis; assistance for junior radiologists; AI-supported clinical education |
| **Modalities** | `fetal ultrasound` |
| **Code / models** | [Zenodo](https://doi.org/10.5281/zenodo.18805366) |
| **Data** | Patient data are restricted; access requests are reviewed by participating institutions |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| OC-6000 internal test | sensitivity / specificity | 93.67% / 98.59% | average AUC 95.57% |
| OC-3000 external test | sensitivity / specificity | 98.33% / 98.99% | average AUC 98.52% |
| Junior radiologists with AIOC | sensitivity | 96.09% | improvement of 6.18 percentage points over unassisted junior radiologists |

</details>

<a id="model-mousemapper-202605"></a>
<details>
<summary><b>MouseMapper</b> — Whole-body cellular and structural mapping with 3D microscopy <i>(Nature 2026-05)</i></summary>

**[A deep-learning framework reveals whole-body perturbations at cell level](https://www.nature.com/articles/s41586-026-10535-2)**

*Nature* · 2026-05 · Doris Kaltenecker & Ali Ertürk · [doi:10.1038/s41586-026-10535-2](https://doi.org/10.1038/s41586-026-10535-2)

| | |
| --- | --- |
| **Model type** | Modular whole-body 3D image-analysis framework |
| **Backbone** | Nerve-Module and Immune-Module based on VesselFM; Tissue-Module uses 3D U-Net models trained through nnU-Net; graph extraction follows segmentation |
| **Training / adaptation** | Supervised learning from VR annotations. Nerve-Module fine-tunes VesselFM with Learning without Forgetting and KL-divergence distillation. Immune-Module freezes the VesselFM encoder and fine-tunes its decoder. Organ and tissue models are supervised 3D U-Nets. |
| **Training data** | Nerves: 84 annotated 300³ subvolumes plus 8 approximately 1,000³ subvolumes. Immune cells: five 256³ annotated volumes cropped into forty 128³ training patches. Organs: 27 organs in 12 whole-body scans (8 train, 4 test). Tissues: 387 final samples with about 2B adipose and 2B muscle voxels. |
| **Downstream tasks** | Peripheral-nerve segmentation and quantification; immune-cell and cluster segmentation; mapping of 31 organs and tissues; whole-body disease-perturbation analysis |
| **Modalities** | `3D light-sheet fluorescence microscopy`, `vDISCO`, `whole-body mouse imaging` |
| **Code** | [github.com/erturklab/mouseMapper](https://github.com/erturklab/mouseMapper) |
| **Interactive data** | [MouseMapper atlas](https://discotechnologies.org/MouseMapper/) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Nerve segmentation | voxel Dice | 0.7494 | fine-tuned VesselFM |
| Cross-condition nerve segmentation | voxel Dice | 0.6916–0.7143 | different labels, imaging conditions, scales, and species |
| Immune-cell segmentation | voxel Dice | 0.7878 | compared with 0.2140–0.5468 for evaluated alternatives |

</details>

<a id="model-microsplit-202605"></a>
<details>
<summary><b>MicroSplit</b> — Semantic unmixing of fluorescence microscopy data <i>(Nat. Methods 2026-05)</i></summary>

**[MicroSplit: semantic unmixing of fluorescent microscopy data](https://www.nature.com/articles/s41592-026-03082-1)**

*Nature Methods* · 2026-05 · [Ashesh Ashesh](https://orcid.org/0000-0003-3778-0576) & Florian Jug · [doi:10.1038/s41592-026-03082-1](https://doi.org/10.1038/s41592-026-03082-1)

| | |
| --- | --- |
| **Model type** | Task-specific computational microscopy model; not a foundation model |
| **Backbone** | Variational Splitting Encoder–Decoder using lateral context; architecture resembles a hierarchical VAE / Ladder-VAE but predicts separated structures rather than reconstructing its input |
| **Training / adaptation** | Supervised semantic unmixing from target channels with co-learned denoising; variational posterior sampling enables calibrated uncertainty/error maps. Each unmixing task requires a dedicated model; no external pretraining is reported. |
| **Training data** | Fourteen publicly downloadable named microscopy datasets. Evaluated on **24 2D** and **6 3D** semantic-unmixing tasks, plus six additional tasks in the supplementary material. The paper does not report one aggregate training-image count. |
| **Downstream tasks** | Separation of two, three, or four superimposed fluorescence structures; denoising; uncertainty estimation; structured-artifact removal; reduced channel count, acquisition time, and light exposure |
| **Modalities** | `2D fluorescence microscopy`, `3D fluorescence microscopy` |
| **Implementation** | [CAREamics](https://careamics.github.io/) |
| **Reproducibility code** | [github.com/CAREamics/MicroSplit-reproducibility](https://github.com/CAREamics/MicroSplit-reproducibility) |
| **Original research code** | [github.com/juglab/MicroSplit](https://github.com/juglab/MicroSplit) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| All evaluated unmixing tasks | average PSNR | 32.53 | aggregate reported by the authors |
| All evaluated unmixing tasks | average MicroMS-SSIM | 0.886 | microscopy-adapted structural similarity metric |
| Task coverage | evaluated tasks | 24 2D + 6 3D | six further tasks are reported in the supplementary material |

</details>

<a id="model-fluoresfm-202603"></a>
<details>
<summary><b>FluoResFM</b> — Multi-task fluorescence microscopy image restoration <i>(Nat. Commun. 2026-03)</i></summary>

**[A foundation model for multi-task cross-distribution restoration of fluorescence microscopy images](https://www.nature.com/articles/s41467-026-70307-4)**

*Nature Communications* · 2026-03 · [Qiqi Lu](https://orcid.org/0000-0001-6066-0690) & [Shenghua Cheng](https://orcid.org/0000-0003-3527-3845) · [doi:10.1038/s41467-026-70307-4](https://doi.org/10.1038/s41467-026-70307-4)

| | |
| --- | --- |
| **Model type** | Fluorescence-microscopy image-restoration foundation model |
| **Backbone** | Text-conditioned U-Net with residual blocks and text–image fusion blocks at every scale; cross-attention injects task, structure, and imaging-condition prompts encoded by BiomedCLIP |
| **Training / adaptation** | Supervised training on paired low/high-quality patches using L1 loss for 700,000 iterations. BiomedCLIP supplies the pretrained text encoder. Adaptation to new tasks updates only the first and last U-Net convolution layers. |
| **Training data** | **4,303,086 paired patches**, three restoration tasks, and more than 20 biological structures. Evaluation includes 302 internal and 51 external unseen datasets. |
| **Downstream tasks** | Denoising; deconvolution; ×2 super-resolution; adaptation to 3D restoration, surface projection, isotropic reconstruction, and ×3/×4/×8 super-resolution; preprocessing for cell/organelle segmentation |
| **Modalities** | `fluorescence microscopy`, `text prompts` |
| **Code** | [github.com/qiqi-lu/fluoresfm](https://github.com/qiqi-lu/fluoresfm) · [Zenodo](https://doi.org/10.5281/zenodo.18383925) |
| **Weights / example data** | [Zenodo](https://doi.org/10.5281/zenodo.18382702) |
| **Interactive tool** | [napari-fluoresfm](https://github.com/qiqi-lu/napari-fluoresfm) |

> **Verification note:** A reliable total parameter count is not stated in the paper or official model documentation reviewed for this entry.

</details>

### Existing catalogue entries

The records below preserve the information already present on this page. They have been reformatted but have not yet undergone the same full-paper verification pass as the 2026 additions above.

<a id="model-ultra-202607"></a>
<details>
<summary><b>ULTRA</b> — Ultrarapid deep 3D histology for intraoperative glioma mapping <i>(Cell 2026-07)</i></summary>

**[Ultrarapid deep 3D histology enables intraoperative mapping of glioma infiltration](https://doi.org/10.1016/j.cell.2026.07.026)**

*Cell* · 2026-07 · [Zhijie Liu](https://github.com/Zhijie-Liu) & [Lixue Shi](https://ibs.fudan.edu.cn/ibsen/42/73/c39095a475763/page.htm) · [doi:10.1016/j.cell.2026.07.026](https://doi.org/10.1016/j.cell.2026.07.026)

| | |
| --- | --- |
| **Model** | [ULTRA](https://github.com/Zhijie-Liu/Ultrarapid-Deep-3D-Histology) |
| **Model type** | Multistage image-to-image translation and 3D histology analysis pipeline |
| **Backbone** | U-Net-based Poisson diffusion model (PBDM); U-Net-based conditional GAN; modified Stimulated Raman CycleGAN (SRC-GAN); six-layer 3D CNN for tumor segmentation |
| **Training / adaptation** | Self-supervised PBDM; supervised paired conditional GAN; semi-supervised SRC-GAN using paired and unpaired SRH–H&E data; supervised 3D CNN |
| **Training data** | PBDM: high-quality SRS images (count not reported); conditional GAN: 6,000 paired lipid–protein image fields; SRC-GAN: paired and unpaired SRH–H&E images (count not reported); 3D CNN: 20,064 paired histology blocks and labels; clinical validation on brain-tumor tissue from 17 patients |
| **Downstream tasks** | SRS image restoration; lipid-to-protein channel synthesis; virtual H&E staining; 3D nuclear morphometry; glioma subtype characterization; tumor segmentation; intraoperative infiltration-margin mapping |
| **Modalities** | stimulated Raman histology; virtual H&E; 3D histology |
| **Code** | [github.com/Zhijie-Liu/Ultrarapid-Deep-3D-Histology](https://github.com/Zhijie-Liu/Ultrarapid-Deep-3D-Histology) |

</details>
<a id="model-busgen-202604"></a>
<details>
<summary><b>BUSGen</b> — Generative foundation model for breast ultrasound <i>(Nat. Biomed. Eng. 2026-04)</i></summary>

**[A foundation generative model for breast ultrasound image analysis](https://www.nature.com/articles/s41551-026-01639-1)**

*Nature Biomedical Engineering* · 2026-04 · [Haojun Yu](https://scholar.google.com/citations?user=KpnMXvMAAAAJ&hl=en&oi=sra) & [Liwei Wang](https://scholar.google.com/citations?hl=en&user=VZHxoh8AAAAJ)

| | |
| --- | --- |
| **Model** | [BUSGen](https://aibus.bio) |
| **Model type** | Breast-ultrasound generative foundation model |
| **Backbone** | U-Net |
| **Training / adaptation** | Denoising Diffusion Probabilistic Model (DDPM) |
| **Training data** | BUS-3.5M: 3.5 million breast-ultrasound images |
| **Downstream tasks** | Breast-cancer screening, diagnosis, and prognosis |
| **Modalities** | `breast ultrasound` |

> **Verification note:** The previous catalogue entry listed approximately 50M parameters, but this count was not found on the official article page reviewed for this draft, so it is omitted pending a citable source.

</details>

<a id="model-reti-pioneer-202604"></a>
<details>
<summary><b>Reti-Pioneer</b> — Multidisease detection and risk prediction from retinal imaging <i>(Nat. Med. 2026-04)</i></summary>

**[AI framework for multidisease detection via retinal imaging](https://www.nature.com/articles/s41591-026-04359-w)**

*Nature Medicine* · 2026-04 · Xiayin Zhang & Honghua Yu

| | |
| --- | --- |
| **Model** | [Reti-Pioneer](https://github.com/lyhyl/Reti-Pioneer) |
| **Model type** | Retinal-image multidisease screening and risk-stratification framework |
| **Backbone** | Swin Transformer, Vision Mamba, and RETFound |
| **Training / adaptation** | Not specified in the current catalogue entry |
| **Training data** | 107,730 color fundus photographs from 53,865 individuals |
| **Downstream tasks** | Cross-sectional detection plus five- and ten-year risk prediction for type 2 diabetes, hypertension, hyperlipidemia, gout, osteoporosis, and thyroid disease |
| **Modalities** | `color fundus photography` |

</details>

<a id="model-ovfm-202603"></a>
<details>
<summary><b>OVFM</b> — Ophthalmic surgical video recognition and navigation <i>(Nat. Biomed. Eng. 2026-03)</i></summary>

**[An ophthalmic video foundation model for surgical recognition and navigation with wet-lab porcine eye validation](https://www.nature.com/articles/s41551-026-01622-w)**

*Nature Biomedical Engineering* · 2026-03 · [Puxun Tu](https://scholar.google.com/citations?user=eluE08oAAAAJ&hl=zh-CN) & Xiaojun Chen

| | |
| --- | --- |
| **Model** | [OVFM](https://github.com/puxuntu/OVFM) |
| **Model type** | Ophthalmic surgical-video foundation model |
| **Backbone** | Self-supervised video transformer; released repository provides ViT Tiny, Small, and Base variants |
| **Training / adaptation** | Self-supervised pretraining on ophthalmic surgical videos; current entry notes DINO-style heads and an SVT base |
| **Training data** | 1.1 million clips across 144 surgical types |
| **Downstream tasks** | Surgical-step and tool recognition; complication detection; skill assessment; scene and limbus segmentation; nucleus localization |
| **Modalities** | `ophthalmic surgical video` |

</details>

<a id="model-cytopathology-202602"></a>
<details>
<summary><b>Autonomous cytopathology pipeline</b> — Whole-slide edge tomography for cervical cytology <i>(Nature 2026-02)</i></summary>

**[Clinical-grade autonomous cytopathology through whole-slide edge tomography](https://www.nature.com/articles/s41586-025-10094-y)**

*Nature* · 2026-02 · [Nao Nitta](https://scholar.google.com/citations?user=T13gRB0AAAAJ&hl=ja) & [Keisuke Goda](https://scholar.google.com/citations?user=gnB9CVgAAAAJ&hl=en)

| | |
| --- | --- |
| **Model** | No single model name stated; [code/data record](https://zenodo.org/records/17808303) |
| **Model type** | Autonomous cytopathology pipeline using whole-slide edge tomography and CMD-based population analysis |
| **Backbone** | YOLOX nucleus detector; MaxViT-base single-cell classifier; CMD-based population analysis |
| **Training / adaptation** | Supervised learning from expert-annotated single-cell images; no external pretraining is stated in the current entry |
| **Training data** | YOLOX: 348 images with 242,669 annotated nuclei. MaxViT: cell images from 354 donor-derived whole slides. Multicentre refinement added 14 whole-slide samples. |
| **Downstream tasks** | Single-cell classification; slide-level LSIL+/HSIL+ detection; HPV-associated abnormality stratification; autonomous cervical-cytology triage |
| **Modalities** | `whole-slide cytology`, `single-cell imaging` |

</details>

<a id="model-panderm-202506"></a>
<details>
<summary><b>PanDerm</b> — Multimodal vision foundation model for clinical dermatology <i>(Nat. Med. 2025-06)</i></summary>

**[A multimodal vision foundation model for clinical dermatology](https://www.nature.com/articles/s41591-025-03747-y)**

*Nature Medicine* · 2025-06 · [Siyuan Yan](https://scholar.google.co.uk/citations?user=LGcOLREAAAAJ&hl=en&oi=ao) & [Zongyuan Ge](https://scholar.google.co.uk/citations?user=Q0gUrcIAAAAJ&hl=en&oi=ao)

| | |
| --- | --- |
| **Model** | [PanDerm](https://github.com/SiyuanYan1/PanDerm) |
| **Model type** | Dermatology vision foundation model |
| **Backbone** | Vision Transformer |
| **Training / adaptation** | Self-supervised learning |
| **Training data** | Approximately 2.1 million unlabelled real-world skin-disease images |
| **Downstream tasks** | Skin-cancer diagnosis and screening |
| **Modalities** | `clinical dermatology imaging` |

</details>

<a id="model-fmue-202501"></a>
<details>
<summary><b>FMUE</b> — Uncertainty-aware OCT retinal-disease diagnosis <i>(Cell Rep. Med. 2025-01)</i></summary>

**[Enhancing AI reliability: A foundation model with uncertainty estimation for optical coherence tomography-based retinal disease diagnosis](https://doi.org/10.1016/j.xcrm.2024.101876)**

*Cell Reports Medicine* · 2025-01 · [Yuanyuan Peng](https://scholar.google.ca/citations?user=UZGX1XkAAAAJ&hl=ko&oi=sra) & [Haoyu Chen](https://scholar.google.com/citations?hl=en&user=KWbcBucAAAAJ&view_op=list_works&sortby=pubdate)

| | |
| --- | --- |
| **Model** | [FMUE](https://github.com/yuanyuanpeng0129/FMUE) |
| **Model type** | OCT foundation model with uncertainty estimation |
| **Backbone** | RETFound encoder |
| **Training / adaptation** | RETFound self-supervised pretraining plus LoRA adaptation |
| **Training data** | 102,468 OCT images |
| **Downstream tasks** | Retinal-disease diagnosis and out-of-distribution detection |
| **Modalities** | `OCT` |

</details>

<a id="model-ret-clip-202408"></a>
<details>
<summary><b>RET-CLIP</b> — Retinal image–report foundation model <i>(MICCAI 2024-08)</i></summary>

**[RET-CLIP: A Retinal Image Foundation Model Pre-trained with Clinical Diagnostic Reports](https://papers.miccai.org/miccai-2024/paper/1812_paper.pdf)**

*MICCAI* · 2024-08 · [Jiawei Du](https://scholar.google.ca/citations?user=SACHmJwAAAAJ&hl=ko&oi=sra) & [Ningli Wang](https://scholar.google.com.sg/citations?user=MIO-cxgAAAAJ&hl=zh-CN)

| | |
| --- | --- |
| **Model** | [RET-CLIP](https://github.com/sStonemason/RET-CLIP) |
| **Model type** | Retinal vision–language foundation model |
| **Backbone** | ViT vision encoder plus RoBERTa language encoder |
| **Training / adaptation** | Contrastive learning with tripartite optimization |
| **Training data** | CFPs and clinical diagnostic reports from 193,865 patients |
| **Downstream tasks** | Retinal diagnosis and multilabel classification |
| **Modalities** | `color fundus photography`, `clinical reports` |

</details>

<a id="model-endofm-lv-202405"></a>
<details>
<summary><b>EndoFM-LV</b> — Long-video endoscopy foundation model <i>(2024-05; publication metadata needs verification)</i></summary>

**[Instability of periodic waves for the Korteweg-de Vries-Burgers equation with monostable source](https://ieeexplore.ieee.org/document/10885043)** *(title and paper link preserved from the current catalogue entry)*

*IEEE entry* · 2024-05 · [Zhao Wang](https://scholar.google.com/citations?user=1kEufdwAAAAJ&hl=zh-CN) & [Qi Dou](https://scholar.google.com.hk/citations?user=iHh7IJQAAAAJ)

| | |
| --- | --- |
| **Model** | [EndoFM-LV](https://github.com/med-air/EndoFM-LV) |
| **Model type** | Long-video endoscopy foundation model |
| **Backbone** | ViT-Base initialized from VideoMAE V2 |
| **Training / adaptation** | Self-supervised masked-token modeling over video patches in a teacher–student framework |
| **Training data** | 6,469 long endoscopy videos (>1 minute each), totaling more than 13 million frames |
| **Downstream tasks** | Classification, segmentation, detection, and workflow recognition |
| **Modalities** | `endoscopy video` |

> **Verification note:** The existing paper title concerns a mathematical wave equation and appears unrelated to EndoFM-LV. The original entry has been preserved rather than silently corrected; its canonical publication title and link must be verified before this draft is used to update the repository.

</details>

<a id="model-retfound-202309"></a>
<details>
<summary><b>RETFound</b> — Generalizable disease detection from retinal images <i>(Nature 2023-09)</i></summary>

**[A foundation model for generalizable disease detection from retinal images](https://www.nature.com/articles/s41586-023-06555-x)**

*Nature* · 2023-09 · [Yukun Zhou](https://scholar.google.com/citations?user=ALDx-VUAAAAJ&hl=zh-CN) & [Pearse Keane](https://scholar.google.co.uk/citations?user=-7KS8pYAAAAJ&hl=en)

| | |
| --- | --- |
| **Model** | [RETFound](https://github.com/rmaphoh/RETFound_MAE) |
| **Model type** | Retinal-image foundation model |
| **Backbone** | Vision Transformer |
| **Training / adaptation** | Self-supervised learning |
| **Training data** | 1.6 million unlabelled retinal images |
| **Downstream tasks** | Generalizable retinal-disease detection |
| **Modalities** | `color fundus photography`, `OCT` |

</details>

---

## Curation notes

- Entries are ordered by publication month.
- Parameter counts are shown only inside a detailed record when the paper or an official release provides a value; architecture names are never converted into inferred parameter counts.
- The compact overview is intended for discovery. The expandable records hold architecture, data, resources, and representative reported results.
- Publisher PDFs and supplementary PDFs should not be committed to this public repository.
