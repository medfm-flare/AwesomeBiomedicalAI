# Biomedical Images — Other

Ultrasound, microscopy, retinal imaging, optical coherence tomography (OCT), dermatology, endoscopy, cytology, and other biomedical imaging modalities.

**Maintainers:** @Terry Fu · [Zaiyou He](https://github.com/zaiyouzy) ([LinkedIn](https://www.linkedin.com/in/zaiyouhe))

**15 papers** · **Last updated: 2026-08** · [Back to index](README.md)

## Paper overview

Click a model name to jump to its expandable record. `Not reported` means that no parameter count was found in the paper or supplementary information; `not publicly verifiable` means that public code or weights were also unavailable. Counts marked `computed` were reproduced from the cited official implementation, configuration, or released weights.

| Date | Model | Venue | Modality | Training data | Model size | Training / adaptation | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 202608 | [VirTues](#model-virtues-202608) | Nature | Spatial proteomics, multiplex tissue imaging | 3,102 patients in 15 IMC cohorts (core pretraining); extended evaluation across >5,100 patients | 43.4M (official weights) | masked marker-space reconstruction with marker and spatial attention; ESM-2 marker embeddings | virtual staining, cell and niche analysis, retrieval, biomarker discovery, patient stratification |
| 202608 | [ULTRA](#model-ultra-202608) | Cell | SRS, virtual H&E, 3D histology | component-specific paired/unpaired datasets; 17-patient clinical validation | 29.8M diffusion U-Net; 2.0M virtual-stain G; 11.4M protein G; 28.3M 3D CNN (computed) | diffusion restoration, paired cGAN translation, semi-supervised CycleGAN staining, supervised 3D classification | restoration, virtual staining, protein prediction, 3D tumor mapping |
| 202607 | [Retina4IRD](#model-retina4ird-202607) | Nat. Med. | CFP, OCT | 1,137 development patients / 2,197 eyes; 1,843 patients / 3,376 eyes overall | 303.3M per CFP/OCT ViT-L model (computed); stacking model not included | separate RETFound-initialized CFP and OCT models fine-tuned for 17 genotypes; prediction stacking with clinical metadata | genotype ranking, clinician decision support, management planning |
| 202607 | [MLLM-EDR](#model-mllm-edr-202607) | Nat. Commun. | Endoscopy, text | 203,838 images and 4,461 reports; 1,839 patients in primary training split | ≥2.7B decoder; exact full-system total not reported | trainable CLIP vision encoder, frozen CLIP text encoder, multitask contrastive/classification losses; rank-16 LoRA on OPT-2.7B decoder | anatomical and mucosal recognition, 19-disease diagnosis, report generation |
| 202606 | [AIOC](#model-aioc-202606) | Nat. Commun. | Fetal ultrasound | 28,994-image internal cohort plus 16,145 external/early images; 9,215 fetuses total | 12.7M detector + 20.6M classifier (official ONNX weights) | joint rotated-box YOLOX structure detection and MILA/LSTM four-view classification; no external pretraining reported | structure detection, standard-view classification, case-level cleft diagnosis, education |
| 202605 | [MouseMapper](#model-mousemapper-202605) | Nature | 3D light-sheet microscopy | module-specific nerve, immune-cell, organ and tissue annotations | 31.4M VesselFM/DynUNet (computed); tissue nnU-Nets configuration dependent | VesselFM transfer with distillation or encoder freezing; supervised nnU-Net tissue models | nerve, immune-cell, organ and tissue mapping across whole bodies |
| 202605 | [MicroSplit](#model-microsplit-202605) | Nat. Methods | Fluorescence microscopy | 14 named datasets; 24 2D + 6 3D primary tasks | Task/configuration dependent; not reported | dedicated variational splitting encoder-decoder per task; supervised semantic separation with co-learned denoising | 2–4-way semantic unmixing, denoising, uncertainty maps, artifact removal |
| 202604 | [BUSGen](#model-busgen-202604) | Nat. Biomed. Eng. | Breast ultrasound | BUS-3.5M: >3.5M images from 5,907 examinations and 4,636 patients | Not publicly verifiable | conditional DDPM pretraining; frozen backbone with LoRA adapters for downstream BUS-DMs | screening, diagnosis, prognosis |
| 202604 | [Reti-Pioneer](#model-reti-pioneer-202604) | Nat. Med. | Color fundus photography, clinical variables | 107,730 images from 53,865 individuals | 303.3M RETFound + 86.9M Swin V2-B (computed); ViM-S and fusion heads additional | bilateral features from RETFound, Swin V2-B and ViM-S fused with image-quality and clinical metadata | six-disease screening and 5-/10-year risk prediction |
| 202603 | [FluoResFM](#model-fluoresfm-202603) | Nat. Commun. | Fluorescence microscopy, text prompts | 4,303,086 paired patches across 3 restoration tasks and >20 structures | 683.7M U-Net; 6,721 parameters adapted for new tasks (computed; text encoder excluded) | paired L1 restoration with frozen BiomedCLIP prompt embeddings; new-task tuning limited to input/output blocks | denoising, deconvolution, multi-scale super-resolution and four additional restoration settings |
| 202603 | [OVFM](#model-ovfm-202603) | Nat. Biomed. Eng. | Ophthalmic surgical video | 1.1M clips across 144 surgery types | Base 121.3M; Small 36.2M; Tiny 7.8M (computed) | DINO-style self-distillation with spatiotemporal transformers; Base checkpoint used in released downstream scripts | step/tool recognition, complications, skills, segmentation, nucleus localization |
| 202602 | [Autonomous cytopathology pipeline](#model-cytopathology-202602) | Nature | Whole-slide cytology, single cells | detector: 242,669 nuclei / 348 images; classifier: 168,569 augmented training images from 354 slides | MaxViT classifier 118.7M (computed); YOLOX variant/count not specified | supervised YOLOX nucleus detection and ImageNet-initialized MaxViT-base 10-class cell classification | single-cell classification, LSIL+/HSIL+ detection, HPV abnormality stratification, triage |
| 202506 | [PanDerm](#model-panderm-202506) | Nat. Med. | Dermoscopy, clinical, TBP, dermatopathology | ~2.1M unlabeled images across four modalities | 303.3M paper ViT-L/16; 85.8M later Base release (computed) | CAEv2-style masked-image pretraining; downstream linear probing, full fine-tuning or segmentation heads | cancer screening, differential diagnosis, segmentation, longitudinal monitoring, prognosis |
| 202412 | [FMUE](#model-fmue-202412) | Cell Rep. Med. | OCT | 102,468 OCT images | 303.7M total; 0.393M rank-4 LoRA parameters plus task head (computed) | RETFound ViT-L initialization; frozen backbone with query/value LoRA in every attention block | retinal-disease diagnosis, calibrated uncertainty, OOD detection |
| 202309 | [RETFound](#model-retfound-202309) | Nature | CFP, OCT | 1.6M unlabeled retinal images | 303.3M ViT-L/16 encoder (computed) | modality-specific masked autoencoder pretraining followed by supervised task fine-tuning | ocular disease detection and systemic-disease prediction |

## Details

### 2026 additions

<a id="model-virtues-202608"></a>
<details>
<summary><b>VirTues</b> — A virtual-tissue foundation model for spatial proteomics <i>(Nature 2026-08)</i></summary>

**[The Virtual Tissues foundation model resolves spatial proteomics across scales](https://www.nature.com/articles/s41586-026-10884-y)**

*Nature* · 2026-08 · [Bunne Lab](https://github.com/bunnelab) · [doi:10.1038/s41586-026-10884-y](https://doi.org/10.1038/s41586-026-10884-y)

| | |
| --- | --- |
| **Model** | VirTues |
| **Model type** | Foundation model for highly multiplexed tissue imaging and spatial proteomics |
| **Backbone** | Purpose-built Vision Transformer with factorized marker and spatial attention; ESM-2 protein representations encode marker identity |
| **Model size** | **43,374,656 parameters (43.4M)**, verified from the official Hugging Face safetensors metadata |
| **Training / adaptation** | Masked-autoencoding objective over marker-by-space tissue tensors. Pretraining masks individual measurements and larger marker/niche structures, then reconstructs the missing marker intensities. Downstream use includes prompting, retrieval, linear/readout models and task-specific analyses rather than one universal fine-tuning recipe. |
| **Training data** | Core pretraining corpus: **15 imaging mass cytometry cohorts, 3,102 patients and 146 markers**. The extended study covers 32 cohorts across IMC, CODEX, Orion and MIBI, representing **more than 5,100 patients and 239 markers**. |
| **Downstream tasks** | Missing-marker reconstruction and virtual staining; cell segmentation and typing; tissue-niche annotation; cross-cohort tissue and patient retrieval; survival and treatment-response biomarker discovery; patient stratification |
| **Modalities** | `IMC`, `CODEX`, `Orion`, `MIBI`, `multiplex tissue imaging`, `spatial proteomics` |
| **Code** | [github.com/bunnelab/virtues](https://github.com/bunnelab/virtues) |
| **Weights** | [huggingface.co/bunnelab/virtues](https://huggingface.co/bunnelab/virtues) |

> **Scope note:** VirTues overlaps computational pathology, but it fits this page because its primary inputs are multiplex biomedical tissue images and spatial-proteomic marker maps, and its core tasks include image reconstruction, segmentation and spatial image analysis.

</details>

<a id="model-retina4ird-202607"></a>
<details>
<summary><b>Retina4IRD</b> — Inherited retinal disease diagnosis and clinician decision support <i>(Nat. Med. 2026-07)</i></summary>

**[AI-based clinician decision support system for diagnosis of inherited retinal diseases: a multicenter, randomized trial](https://www.nature.com/articles/s41591-026-04545-w)**

*Nature Medicine* · 2026-07 · [Huixun Jia](https://orcid.org/0000-0001-9341-5587) & [Xiaodong Sun](https://orcid.org/0000-0001-5015-0945) · [doi:10.1038/s41591-026-04545-w](https://doi.org/10.1038/s41591-026-04545-w)

| | |
| --- | --- |
| **Model** | Retina4IRD |
| **Model type** | Clinical AI decision-support system |
| **Backbone** | ViT-L/16 image models for color fundus photography and OCT; the released implementation combines image predictions with clinical metadata using an ensemble/stacking model |
| **Model size** | **303,319,057 parameters (303.3M) per CFP or OCT image model**, computed from the official `vit_large_patch16` definition and 17-class configuration. The separate stacking model is not included because its serialized estimator was not independently counted. |
| **Training / adaptation** | Vision Transformer initialized from RETFound and fine-tuned for 17 genotype categories; CFP and OCT image predictions can be combined with patient metadata |
| **Training data** | Development stage: **1,137 patients and 2,197 eyes** across training, validation and internal testing. The complete development-plus-external evaluation population contains **1,843 genetically confirmed patients and 3,376 eyes** across China, South Korea and Poland; that larger number is not a training-only count. |
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

> **Verification note:** The parameter count is reproduced from the official released architecture/configuration, not stated by the paper. The cohort totals are separated so the full evaluation population is not mislabeled as training data.

</details>

<a id="model-mllm-edr-202607"></a>
<details>
<summary><b>MLLM-EDR</b> — Automatic esophagogastroduodenoscopy diagnosis and reporting <i>(Nat. Commun. 2026-07)</i></summary>

**[Bootstrapping multimodal large language model with medical knowledge for automatic esophagogastroduodenoscopy diagnosis and reporting](https://www.nature.com/articles/s41467-026-75377-y)**

*Nature Communications* · 2026-07 · Miaojing Shi & [Shuchang Xu](https://orcid.org/0000-0003-3170-2278) · [doi:10.1038/s41467-026-75377-y](https://doi.org/10.1038/s41467-026-75377-y)

| | |
| --- | --- |
| **Model** | MLLM-EDR |
| **Model type** | Medical multimodal large-language-model system |
| **Backbone** | CLIP/MedCLIP vision and text encoders; temporal adaptive pooling; one self-attention layer and three visual–text cross-attention blocks; an OPT-2.7B language decoder in the official software implementation; linear mucosa and disease heads |
| **Model size** | **At least 2.7B parameters** from the named OPT-2.7B decoder alone. The exact full-system total, including CLIP encoders, fusion blocks and heads, is not reported and cannot be reproduced without the authors' private local checkpoints. |
| **Training / adaptation** | Multitask learning with expert-verified GPT-4-assisted medical descriptions, diagnostic classification and vision–text alignment objectives. The official code trains the vision encoder, freezes the CLIP text encoder, and adapts the frozen OPT-2.7B decoder with rank-16 LoRA on attention and feed-forward projections. |
| **Training data** | **4,461 participants**, **203,838 EGD images**, and **4,461 reports** from four hospitals. The primary TJ-EGD dataset contains 118,802 images and 2,631 participants, including 1,839 training participants. |
| **Downstream tasks** | Eight-site anatomical recognition; six-type gastric-mucosa classification; diagnosis of 19 gastrointestinal diseases; EGD report generation; video-level clinical assistance |
| **Modalities** | `endoscopy images`, `clinical reports`, `medical text` |
| **Code** | [Zenodo software record](https://doi.org/10.5281/zenodo.21023152) |
| **Weights** | Not publicly released |
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
| **Model** | AIOC |
| **Model type** | Clinical ultrasound diagnostic and educational AI system |
| **Backbone** | Dual-branch system: YOLOX structure-detection branch plus a Mamba-Inspired Linear Attention (MILA) classification branch; an LSTM models relationships between global and local structural features |
| **Model size** | **12,659,177 parameters** in the released detector and **20,598,244 parameters** in the released four-view classifier, counted from the official ONNX initializers on Zenodo. |
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
| **Model** | MouseMapper |
| **Model type** | Modular whole-body 3D image-analysis framework |
| **Backbone** | Nerve-Module and Immune-Module based on VesselFM; Tissue-Module uses 3D U-Net models trained through nnU-Net; graph extraction follows segmentation |
| **Model size** | **31,420,554 parameters (31.4M)** for the published VesselFM-style MONAI DynUNet configuration, computed from the official code. Tissue/organ nnU-Net models are generated from dataset-specific plans, so no single additional count is valid. |
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
| **Model** | MicroSplit |
| **Model type** | Task-specific computational microscopy model; not a foundation model |
| **Backbone** | Variational Splitting Encoder–Decoder using lateral context; architecture resembles a hierarchical VAE / Ladder-VAE but predicts separated structures rather than reconstructing its input |
| **Model size** | **Task/configuration dependent; not reported.** Each 2D/3D task has a dedicated model whose target-channel count, input size, multiscale context and convolution strides can differ. |
| **Training / adaptation** | Supervised semantic unmixing from target channels with co-learned denoising; variational posterior sampling enables calibrated uncertainty/error maps. Each unmixing task requires a dedicated model; no external pretraining is reported. |
| **Training data** | Fourteen publicly downloadable named microscopy datasets. Evaluated on **24 2D** and **6 3D** semantic-unmixing tasks, plus six additional tasks in the supplementary material. The paper does not report one aggregate training-image count. |
| **Downstream tasks** | Separation of two, three, or four superimposed fluorescence structures; denoising; uncertainty estimation; structured-artifact removal; reduced channel count, acquisition time, and light exposure |
| **Modalities** | `2D fluorescence microscopy`, `3D fluorescence microscopy` |
| **Implementation** | [CAREamics MicroSplit API](https://careamics.github.io/latest/reference/careamics/config/algorithms/microsplit_algorithm_config/) |
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
| **Model** | FluoResFM |
| **Model type** | Fluorescence-microscopy image-restoration foundation model |
| **Backbone** | Text-conditioned U-Net with residual blocks and text–image fusion blocks at every scale; cross-attention injects task, structure, and imaging-condition prompts encoded by BiomedCLIP |
| **Model size** | **683,650,561 parameters (683.7M)** in the restoration U-Net, computed from the official training configuration. The frozen external BiomedCLIP text encoder is excluded. The released `in-out` adaptation strategy updates **6,721 parameters**. |
| **Training / adaptation** | Supervised training on paired low/high-quality patches using L1 loss for 700,000 iterations. BiomedCLIP supplies the pretrained text encoder. Adaptation to new tasks uses the official `in-out` strategy, which updates the input block and final output block while freezing the rest of the U-Net. |
| **Training data** | **4,303,086 paired patches**, three restoration tasks, and more than 20 biological structures. Evaluation includes 302 internal and 51 external unseen datasets. |
| **Downstream tasks** | Denoising; deconvolution; ×2 super-resolution; adaptation to 3D restoration, surface projection, isotropic reconstruction, and ×3/×4/×8 super-resolution; preprocessing for cell/organelle segmentation |
| **Modalities** | `fluorescence microscopy`, `text prompts` |
| **Code** | [github.com/qiqi-lu/fluoresfm](https://github.com/qiqi-lu/fluoresfm) · [Zenodo](https://doi.org/10.5281/zenodo.18383925) |
| **Weights / example data** | [Zenodo](https://doi.org/10.5281/zenodo.18382702) |
| **Interactive tool** | [napari-fluoresfm](https://github.com/qiqi-lu/napari-fluoresfm) |

> **Verification note:** Counts are reproduced from the official released code/configuration rather than reported in the article. The 6,721 adapted parameters include the input block and output normalization/convolution block selected by the official `finetune(strategy="in-out")` method.

</details>

### Additional catalogue entries

These earlier records are retained from the existing catalogue and updated here where the paper, supplementary information, official code, configurations, or released weights support a more specific statement.

<a id="model-ultra-202608"></a>
<details>
<summary><b>ULTRA</b> — Ultrarapid deep 3D histology for intraoperative glioma mapping <i>(Cell 2026-08)</i></summary>

**[Ultrarapid deep 3D histology enables intraoperative mapping of glioma infiltration](https://doi.org/10.1016/j.cell.2026.07.026)**

*Cell* · 2026-08 · [Zhijie Liu](https://github.com/Zhijie-Liu) & [Lixue Shi](https://ibs.fudan.edu.cn/ibsen/42/73/c39095a475763/page.htm) · [doi:10.1016/j.cell.2026.07.026](https://doi.org/10.1016/j.cell.2026.07.026)

| | |
| --- | --- |
| **Model** | ULTRA |
| **Model type** | Multistage image-to-image translation and 3D histology analysis pipeline |
| **Backbone** | U-Net-based Poisson diffusion model (PBDM); U-Net-based conditional GAN; modified Stimulated Raman CycleGAN (SRC-GAN); six-layer 3D CNN for tumor segmentation |
| **Model size** | Multi-component pipeline: **29,763,329** parameters in the diffusion U-Net; **1,965,059** in the virtual-staining generator; **11,370,881** in the released lipid-to-protein generator; **28,269,826** in the 3D CNN. Counts are computed from the official default configurations; they must not be summed as one simultaneously executed model. |
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
| **Model** | BUSGen |
| **Model type** | Breast-ultrasound generative foundation model |
| **Backbone** | U-Net denoiser inside a DDPM |
| **Model size** | **Not publicly verifiable.** No parameter count was found in the article material reviewed here, and public code or weights are not available. |
| **Training / adaptation** | Conditional DDPM pretraining for breast-ultrasound generation, conditioned on pathology, lesion location and device type. For downstream BUS-DMs, the pretrained backbone is frozen and LoRA adapters are fine-tuned for task-specific generation. |
| **Training data** | BUS-3.5M: **more than 3.5 million images** from **5,907 examinations**, **4,636 patients** and **3,749 lesions**. |
| **Downstream tasks** | Breast-cancer screening, diagnosis, and prognosis |
| **Modalities** | `breast ultrasound` |
| **Code / weights** | Not publicly released; pretraining code, adaptation code and an online API are available from the authors upon reasonable request |
| **Project page / demo** | [aibus.bio](https://aibus.bio/) |

> **Verification note:** The previous catalogue entry listed approximately 50M parameters, but this count was not found on the official article page reviewed for this draft, so it is omitted pending a citable source. The official aibus.bio site is listed as a project/demo, not as a model repository.

</details>

<a id="model-reti-pioneer-202604"></a>
<details>
<summary><b>Reti-Pioneer</b> — Multidisease detection and risk prediction from retinal imaging <i>(Nat. Med. 2026-04)</i></summary>

**[AI framework for multidisease detection via retinal imaging](https://www.nature.com/articles/s41591-026-04359-w)**

*Nature Medicine* · 2026-04 · Xiayin Zhang & Honghua Yu

| | |
| --- | --- |
| **Model** | Reti-Pioneer |
| **Model type** | Retinal-image multidisease screening and risk-stratification framework |
| **Backbone** | Ensemble of RETFound ViT-L/16, torchvision Swin V2-B and ViM-S/Visual Mamba feature extractors; bilateral-eye features are fused with image-quality scores and ten clinical metadata variables |
| **Model size** | **303,301,632** parameters for the RETFound encoder and **86,905,848** for the Swin V2-B encoder (computed from the official definitions). The ViM-S encoder and disease-specific fusion heads are additional; an exact complete-system total is not reported. |
| **Training / adaptation** | The three pretrained image encoders produce left/right-eye features. Disease-specific quality-aware fusion heads combine those features with fundus-image quality and clinical metadata for binary cross-sectional prediction and 5-/10-year risk prediction. The public training path uses cached encoder features and trains the fusion heads with AdamW. |
| **Training data** | 107,730 color fundus photographs from 53,865 individuals |
| **Downstream tasks** | Cross-sectional detection plus five- and ten-year risk prediction for type 2 diabetes, hypertension, hyperlipidemia, gout, osteoporosis, and thyroid disease |
| **Modalities** | `color fundus photography` |
| **Code** | [github.com/lyhyl/Reti-Pioneer](https://github.com/lyhyl/Reti-Pioneer) |

</details>

<a id="model-ovfm-202603"></a>
<details>
<summary><b>OVFM</b> — Ophthalmic surgical video recognition and navigation <i>(Nat. Biomed. Eng. 2026-03)</i></summary>

**[An ophthalmic video foundation model for surgical recognition and navigation with wet-lab porcine eye validation](https://www.nature.com/articles/s41551-026-01622-w)**

*Nature Biomedical Engineering* · 2026-03 · [Puxun Tu](https://scholar.google.com/citations?user=eluE08oAAAAJ&hl=zh-CN) & Xiaojun Chen

| | |
| --- | --- |
| **Model** | OVFM |
| **Model type** | Ophthalmic surgical-video foundation model |
| **Backbone** | Spatiotemporal Vision Transformer with divided space–time attention; the official repository provides Tiny, Small and Base encoders |
| **Model size** | **121,258,752 (Base)**, **36,233,728 (Small)** and **7,753,920 (Tiny)** encoder parameters, computed from the official no-head inference definitions. |
| **Training / adaptation** | DINO-style teacher–student self-distillation on ophthalmic surgical clips using spatiotemporal encoders. The released downstream fine-tuning scripts load the Base pretraining checkpoint and attach task-specific heads. |
| **Training data** | 1.1 million clips across 144 surgical types |
| **Downstream tasks** | Surgical-step and tool recognition; complication detection; skill assessment; scene and limbus segmentation; nucleus localization |
| **Modalities** | `ophthalmic surgical video` |
| **Code** | [github.com/puxuntu/OVFM](https://github.com/puxuntu/OVFM) |

</details>

<a id="model-cytopathology-202602"></a>
<details>
<summary><b>Autonomous cytopathology pipeline</b> — Whole-slide edge tomography for cervical cytology <i>(Nature 2026-02)</i></summary>

**[Clinical-grade autonomous cytopathology through whole-slide edge tomography](https://www.nature.com/articles/s41586-025-10094-y)**

*Nature* · 2026-02 · [Nao Nitta](https://scholar.google.com/citations?user=T13gRB0AAAAJ&hl=ja) & [Keisuke Goda](https://scholar.google.com/citations?user=gnB9CVgAAAAJ&hl=en)

| | |
| --- | --- |
| **Model** | No single model name stated; multistage autonomous cytopathology pipeline |
| **Model type** | Autonomous cytopathology pipeline using whole-slide edge tomography and CMD-based population analysis |
| **Backbone** | YOLOX nucleus detector; maxvit_base_tf_224 single-cell classifier; CMD-based slide/population analysis |
| **Model size** | **118,706,398 parameters (118.7M)** for the released 10-class MaxViT-base classifier configuration. The YOLOX variant and its parameter count are not specified in the public release, so no detector value is inferred. |
| **Training / adaptation** | Supervised YOLOX training on expert nucleus annotations. The MaxViT-base classifier is initialized with ImageNet-pretrained weights and fully optimized for ten cell classes using weighted cross-entropy and AdamW. |
| **Training data** | YOLOX: **348 images with 242,669 annotated nuclei**. MaxViT: **168,569 augmented training images** derived from **354 whole-slide images**, with 50,222 validation images. Multicentre evaluation involved **1,124 slides**; these evaluation slides are not training data. |
| **Downstream tasks** | Single-cell classification; slide-level LSIL+/HSIL+ detection; HPV-associated abnormality stratification; autonomous cervical-cytology triage |
| **Modalities** | `whole-slide cytology`, `single-cell imaging` |
| **Code** | [Zenodo code record](https://zenodo.org/records/17808303) |

</details>

<a id="model-panderm-202506"></a>
<details>
<summary><b>PanDerm</b> — Multimodal vision foundation model for clinical dermatology <i>(Nat. Med. 2025-06)</i></summary>

**[A multimodal vision foundation model for clinical dermatology](https://www.nature.com/articles/s41591-025-03747-y)**

*Nature Medicine* · 2025-06 · [Siyuan Yan](https://scholar.google.co.uk/citations?user=LGcOLREAAAAJ&hl=en&oi=ao) & [Zongyuan Ge](https://scholar.google.co.uk/citations?user=Q0gUrcIAAAAJ&hl=en&oi=ao)

| | |
| --- | --- |
| **Model** | PanDerm |
| **Model type** | Dermatology vision foundation model |
| **Backbone** | Paper model: ViT-L/16; the later public release also provides a ViT-B/16 checkpoint |
| **Model size** | **303,326,208 parameters (303.3M)** for the paper ViT-L/16 encoder; **85,807,872 (85.8M)** for the later Base release, computed from the official implementation. |
| **Training / adaptation** | CAEv2-style masked-image representation learning across dermoscopy, clinical photography, total-body photography and dermatopathology. Downstream protocols include linear probing, full supervised fine-tuning and task-specific segmentation heads. |
| **Training data** | Approximately 2.1 million unlabelled real-world skin-disease images |
| **Downstream tasks** | Skin-cancer screening; differential diagnosis across many skin conditions; lesion segmentation; longitudinal change monitoring; total-body-photography applications; prognosis prediction |
| **Modalities** | `dermoscopy`, `clinical photography`, `total-body photography`, `dermatopathology` |
| **Code** | [github.com/SiyuanYan1/PanDerm](https://github.com/SiyuanYan1/PanDerm) |

</details>

<a id="model-fmue-202412"></a>
<details>
<summary><b>FMUE</b> — Uncertainty-aware OCT retinal-disease diagnosis <i>(Cell Rep. Med. 2024-12)</i></summary>

**[Enhancing AI reliability: A foundation model with uncertainty estimation for optical coherence tomography-based retinal disease diagnosis](https://doi.org/10.1016/j.xcrm.2024.101876)**

*Cell Reports Medicine* · 2024-12 · [Yuanyuan Peng](https://scholar.google.ca/citations?user=UZGX1XkAAAAJ&hl=ko&oi=sra) & [Haoyu Chen](https://scholar.google.com/citations?hl=en&user=KWbcBucAAAAJ&view_op=list_works&sortby=pubdate)

| | |
| --- | --- |
| **Model** | FMUE |
| **Model type** | OCT foundation model with uncertainty estimation |
| **Backbone** | RETFound ViT-L/16 with rank-4 LoRA matrices inserted into the query and value projections of all 24 attention blocks |
| **Model size** | **303.7M total parameters** (exact count varies slightly with the task head). The LoRA matrices contribute **393,216 trainable parameters**; the classification head is also trainable (for example, 2,050 parameters for a binary head). Counts are computed from the official implementation. |
| **Training / adaptation** | Initialize from RETFound OCT masked-autoencoder weights; freeze pretrained parameters; train rank-4 query/value LoRA adapters and the task-specific classification head. Uncertainty and OOD decisions are derived from the resulting predictive outputs. |
| **Training data** | 102,468 OCT images |
| **Downstream tasks** | Retinal-disease diagnosis and out-of-distribution detection |
| **Modalities** | `OCT` |
| **Code** | [github.com/yuanyuanpeng0129/FMUE](https://github.com/yuanyuanpeng0129/FMUE) |

</details>

<a id="model-retfound-202309"></a>
<details>
<summary><b>RETFound</b> — Generalizable disease detection from retinal images <i>(Nature 2023-09)</i></summary>

**[A foundation model for generalizable disease detection from retinal images](https://www.nature.com/articles/s41586-023-06555-x)**

*Nature* · 2023-09 · [Yukun Zhou](https://scholar.google.com/citations?user=ALDx-VUAAAAJ&hl=zh-CN) & [Pearse Keane](https://scholar.google.co.uk/citations?user=-7KS8pYAAAAJ&hl=en)

| | |
| --- | --- |
| **Model** | RETFound |
| **Model type** | Retinal-image foundation model |
| **Backbone** | ViT-L/16 retinal encoder with separate CFP and OCT pretrained checkpoints |
| **Model size** | **303,301,632 parameters (303.3M)** for the no-head encoder used by the official downstream implementation, computed from the released model definition. |
| **Training / adaptation** | Modality-specific masked autoencoder pretraining on unlabeled CFP and OCT images, followed by supervised fine-tuning on ocular-disease and systemic-disease prediction tasks. |
| **Training data** | 1.6 million unlabelled retinal images |
| **Downstream tasks** | Ocular-disease detection and prognosis; prediction of systemic conditions including heart failure and myocardial infarction |
| **Modalities** | `color fundus photography`, `OCT` |
| **Code** | [github.com/rmaphoh/RETFound](https://github.com/rmaphoh/RETFound) |

</details>

---

## Curation notes

- Dates use the first online publication month, and overview entries are ordered by that date.
- Parameter counts are included only when reported by the paper, exposed by official weights, or reproducible from an official architecture/configuration. Each computed count is labeled; unknown or configuration-dependent totals remain explicit.
- The compact overview is intended for discovery. The expandable records hold architecture, data, resources, and representative reported results.
- Publisher PDFs and supplementary PDFs should not be committed to this public repository.
