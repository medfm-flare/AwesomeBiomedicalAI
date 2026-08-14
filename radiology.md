# Radiology

CT, MRI, PET, X-ray and fMRI foundation models.

**Maintainer:** [Judy Lyu](https://github.com/judylyu)

**31 papers** · **Last updated: 2026-08** · [Back to index](README.md)

## Paper overview

Click a model name to jump to its expandable record. A dash (`—`) means that the corresponding value has not been confirmed from the paper or an official release.


| Date    | Model                                                  | Venue             | Modality                  | Training data                     | Training / adaptation              | Downstream tasks                                                         |
| ------- | ------------------------------------------------------ | ----------------- | ------------------------- | --------------------------------- | ---------------------------------- | ------------------------------------------------------------------------ |
| 2026-07 | [NeuroVFM](#model-neurovfm-202607)                     | Nat. Med.         | CT, MRI                   | 5.24M volumes                     | JEPA                               | classification, report generation, retrieval, triage, registration       |
| 2026-07 | [MARS](#model-mars-202607)                             | Nat. Biomed. Eng. | MRI                       | 336K volumes                      | MAE, contrastive learning          | classification, segmentation, registration, report generation, prognosis |
| 2026-05 | [MultitaskCognition](#model-multitaskcognition-202605) | Nat. Aging        | MRI                       | ~3K studies                       | supervised, transfer learning      | classification, segmentation, regression, prognosis                      |
| 2026-04 | [FM-HCT](#model-fm-hct-202604)                         | Nat. Biomed. Eng. | CT                        | 362K volumes                      | DINO                               | classification, retrieval                                                |
| 2026-04 | [NeuroFM](#model-neurofm-202604)                       | Nat. Biomed. Eng. | fMRI                      | 8.65M frames                      | MAE                                | regression, classification, prognosis                                    |
| 2026-03 | [TRIBEv2](#model-tribev2-202603)                       | arXiv             | fMRI, vision, audio, text | Multiple datasets                 | Multimodal representation learning | regression                                                               |
| 2026-03 | [Merlin](#model-merlin-202603)                         | Nature            | CT, text                  | 25.5K CT volumes                  | CLIP                               | classification, segmentation, retrieval, report generation, prognosis    |
| 2026-03 | [Thymus-IO](#model-thymus-io-202603)                   | Nature            | CT                        | 5.7K CT volumes                   | SwAV                               | classification, prognosis                                                |
| 2026-03 | [Thymus-Adult](#model-thymus-adult-202603)             | Nature            | CT                        | 5.7K CT volumes                   | SwAV                               | classification                                                           |
| 2026-02 | [OMAFound](#model-omafound-202602)                     | Nat. Health       | CT                        | 325.2K CT volumes                 | self-supervised                    | classification                                                           |
| 2026-02 | [CMR Transformer](#model-cmr-transformer-202602)       | Nat. Biomed. Eng. | MRI, text                 | ~21K scans                        | InfoNCE, contrastive               | regression, classification                                               |
| 2026-02 | [BrainIAC](#model-brainiac-202602)                     | Nat. Neurosci.    | MRI                       | 32K scans                         | SimCLR                             | classification, regression, segmentation, prognosis                      |
| 2026-02 | [CT-CLIP / CT-CHAT](#model-ct-clip-ct-chat-202602)     | Nat. Biomed. Eng. | CT, text                  | 25.7K CT volumes                  | CLIP                               | classification, retrieval, VQA                                           |
| 2026-02 | [PRIMA](#model-prima-202602)                           | Nat. Biomed. Eng. | MRI, text                 | 221K studies                      | CLIP                               | classification, triage, regression                                       |
| 2026-02 | [MAOSS](#model-maoss-202602)                           | Nat. Commun.      | CT, text                  | Multisite data + 226 publications | —                                  | classification, prognosis                                                |
| 2026-01 | [AFLoc](#model-afloc-202601)                           | Nat. Biomed. Eng. | X-ray, text               | MIMIC-CXR                         | CLIP                               | localization, classification                                             |
| 2026-01 | [deepmriprep](#model-deepmriprep-202601)               | Nat. Comput. Sci. | MRI                       | 685 MRI scans                     | —                                  | preprocessing                                                            |
| 2026-01 | [FOMO25](#model-fomo25-202601)                         | arXiv             | MRI                       | 176K volumes                      | MAE                                | segmentation, classification, regression                                 |
| 2025-12 | [VoCo](#model-voco-202512)                             | IEEE TPAMI        | CT                        | 160K volumes                      | VoCo, contrastive learning         | segmentation, classification, regression, vision-language modeling       |
| 2025-12 | [TAP-CT](#model-tap-ct-202512)                         | arXiv             | CT                        | 105K volumes                      | DINOv2                             | segmentation, classification                                             |
| 2025-12 | [AnyMC3D](#model-anymc3d-202512)                       | arXiv             | CT, MRI                   | —                                 | DINOv2, DINOv3                     | classification                                                           |
| 2025-11 | [Pillar-0](#model-pillar-0-202511)                     | arXiv             | CT, MRI, text             | ~155K volumes                     | contrastive, vision-language       | classification, prognosis                                                |
| 2025-11 | [SPECTRE](#model-spectre-202511)                       | CVPR 2026         | CT, text                  | 230K CT volumes                   | DINOv3, SigLIP                     | classification, segmentation, retrieval                                  |
| 2025-10 | [BrainFound](#model-brainfound-202510)                 | arXiv             | MRI                       | 10K volumes                       | DINOv2                             | classification                                                           |
| 2025-09 | [MRI-PTPCa](#model-mri-ptpca-202509)                   | Nat. Cancer       | MRI, histopathology       | —                                 | BYOL                               | classification, grading                                                  |
| 2025-08 | [Curia](#model-curia-202508)                           | arXiv             | CT, MRI                   | 228M DICOM images                 | DINOv2                             | General-purpose multimodal radiology representation learning             |
| 2025-07 | [Percival](#model-percival-202507)                     | medRxiv           | CT, text                  | 403K CT volumes                   | InfoNCE, contrastive               | retrieval, classification, prognosis                                     |
| 2025-04 | [Spark3D](#model-spark3d-202504)                       | CVPR 2025         | MRI                       | 44K MRI volumes                   | MAE                                | segmentation                                                             |
| 2025-01 | [CT-FM](#model-ct-fm-202501)                           | arXiv             | CT                        | 148K CT volumes                   | SimCLR                             | segmentation, triage, retrieval                                          |
| 2025-01 | [3DINO](#model-3dino-202501)                           | arXiv             | CT, MRI                   | 1.3K patients                     | 3DINO, self-supervised             | classification, segmentation                                             |
| 2024-12 | [BME-X](#model-bme-x-202412)                           | Nat. Biomed. Eng. | MRI                       | —                                 | —                                  | segmentation, registration, classification                               |




## Details

Click a model to expand its record.



**NeuroVFM** — Health system learning enables generalist neuroimaging models *(Nat. Med. 2026-07)*

**[Health system learning enables generalist neuroimaging models](https://www.nature.com/articles/s41591-026-04497-1)**

*Nat. Med.* · 2026-07 · Published · [doi:10.1038/s41591-026-04497-1](https://doi.org/10.1038/s41591-026-04497-1)


|                      |                                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Backbone**         | 3D vision transformer                                                                                               |
| **Pre-training**     | `JEPA` Volumetric joint-embedding predictive pretraining.                                                           |
| **Training data**    | CT and MRI neuroimaging **5,240,000** volumes                                                                       |
| **Downstream tasks** | `classification`, `report generation`, `retrieval`, `triage`, `registration` Generalist health-system neuroimaging. |
| **Modalities**       | `CT`, `MRI`                                                                                                         |
| **Code**             | [github.com/MLNeurosurg/neurovfm](https://github.com/MLNeurosurg/neurovfm)                                          |






**MARS** — Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications *(Nat. Biomed. Eng. 2026-07)*

**[Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications](https://www.nature.com/articles/s41551-026-01740-5)**

*Nat. Biomed. Eng.* · 2026-07 · Published · [doi:10.1038/s41551-026-01740-5](https://doi.org/10.1038/s41551-026-01740-5)


|                      |                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Backbone**         | 3D Swin Transformer                                                                                                    |
| **Pre-training**     | `MAE`, `contrastive learning`                                                                                          |
| **Training data**    | Multi-sequence MRI **336,000** volumes                                                                                 |
| **Downstream tasks** | `classification`, `segmentation`, `registration`, `report generation`, `prognosis` Evaluated across 44 clinical tasks. |
| **Modalities**       | `MRI`                                                                                                                  |
| **Code**             | [github.com/zqiuak/MARS](https://github.com/zqiuak/MARS)                                                               |






**MultitaskCognition** — Predicting categorical and continuous Alzheimer’s disease outcomes from a single MRI scan *(Nat. Aging 2026-05)*

**[Predicting categorical and continuous Alzheimer’s disease outcomes from a single MRI scan](https://doi.org/10.1038/s43587-026-01121-2)**

*Nat. Aging* · 2026-05 · Published · [doi:10.1038/s43587-026-01121-2](https://doi.org/10.1038/s43587-026-01121-2)


|                      |                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Backbone**         | 3D U-Net, ResNet-50 and XGBoost                                                                                  |
| **Pre-training**     | `supervised`, `transfer learning`                                                                                |
| **Training data**    | Approximately **3,000** MRI studies                                                                              |
| **Downstream tasks** | `classification`, `segmentation`, `regression`, `prognosis` Alzheimer’s disease outcomes from a single MRI scan. |
| **Modalities**       | `MRI`                                                                                                            |
| **Code**             | [github.com/darenma/MultitaskCognition](https://github.com/darenma/MultitaskCognition)                           |






**FM-HCT** — 3D foundation model for generalizable disease detection in head computed tomography *(Nat. Biomed. Eng. 2026-04)*

**[3D foundation model for generalizable disease detection in head computed tomography](https://www.nature.com/articles/s41551-026-01668-w)**

*Nat. Biomed. Eng.* · 2026-04 · Published · [doi:10.1038/s41551-026-01668-w](https://doi.org/10.1038/s41551-026-01668-w)


|                      |                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Backbone**         | Vision transformer                                                                     |
| **Pre-training**     | `DINO`                                                                                 |
| **Training data**    | Head CT **362,000** volumes                                                            |
| **Downstream tasks** | `classification`, `retrieval` Generalizable disease detection in head CT.              |
| **Modalities**       | `CT`                                                                                   |
| **Code**             | [github.com/NYUMedML/headCT_foundation](https://github.com/NYUMedML/headCT_foundation) |






**NeuroFM** — Towards a general-purpose foundation model for functional MRI analysis *(Nat. Biomed. Eng. 2026-04)*

**[Towards a general-purpose foundation model for functional MRI analysis](https://www.nature.com/articles/s41551-026-01666-y)**

*Nat. Biomed. Eng.* · 2026-04 · Published · [doi:10.1038/s41551-026-01666-y](https://doi.org/10.1038/s41551-026-01666-y)


|                      |                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------ |
| **Backbone**         | Spatiotemporal waveform Mamba                                                        |
| **Pre-training**     | `MAE`                                                                                |
| **Training data**    | More than **50,000** subjects and **8,650,000** fMRI frames                          |
| **Downstream tasks** | `regression`, `classification`, `prognosis` General-purpose functional MRI analysis. |
| **Modalities**       | `fMRI`                                                                               |
| **Code**             | [github.com/CUHK-AIM-Group/NeuroSTORM](https://github.com/CUHK-AIM-Group/NeuroSTORM) |






**TRIBEv2** — A foundation model of vision, audition, and language for in-silico neuroscience *(arXiv 2026-03)*

**[A foundation model of vision, audition, and language for in-silico neuroscience](https://ai.meta.com/research/publications/a-foundation-model-of-vision-audition-and-language-for-in-silico-neuroscience/)**

*arXiv* · 2026-03 · Preprint


|                      |                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Backbone**         | V-JEPA 2, wav2vec and Llama                                                        |
| **Pre-training**     | Multimodal representation learning                                                 |
| **Training data**    | Multiple datasets; numeric scale not recorded                                      |
| **Downstream tasks** | `regression` Maps vision, audio and language stimuli to predicted brain voxels.    |
| **Modalities**       | `fMRI`, `vision`, `audio`, `text`                                                  |
| **Code**             | [github.com/facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) |






**Merlin** — Merlin: a computed tomography vision–language foundation model and dataset *(Nature 2026-03)*

**[Merlin: a computed tomography vision–language foundation model and dataset](https://www.nature.com/articles/s41586-026-10181-8)**

*Nature* · 2026-03 · Updated · [doi:10.1038/s41586-026-10181-8](https://doi.org/10.1038/s41586-026-10181-8)


|                      |                                                                                 |
| -------------------- | ------------------------------------------------------------------------------- |
| **Backbone**         | ResNet vision encoder and Longformer text encoder                               |
| **Pre-training**     | `CLIP`                                                                          |
| **Training data**    | CT volumes paired with clinical text **25,500** CT volumes                      |
| **Downstream tasks** | `classification`, `segmentation`, `retrieval`, `report generation`, `prognosis` |
| **Modalities**       | `CT`, `text`                                                                    |
| **Code**             | [github.com/StanfordMIMI/Merlin](https://github.com/StanfordMIMI/Merlin)        |
| **Dataset**          | [github.com/StanfordMIMI/Merlin](https://github.com/StanfordMIMI/Merlin)        |






**Thymus-IO** — Thymic health and immunotherapy outcomes in patients with cancer *(Nature 2026-03)*

**[Thymic health and immunotherapy outcomes in patients with cancer](https://www.nature.com/articles/s41586-026-10243-x)**

*Nature* · 2026-03 · Published · [doi:10.1038/s41586-026-10243-x](https://doi.org/10.1038/s41586-026-10243-x)


|                      |                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------- |
| **Backbone**         | U-Net and 3D ResNet-50                                                              |
| **Pre-training**     | `SwAV`                                                                              |
| **Training data**    | **5,700** CT volumes                                                                |
| **Downstream tasks** | `classification`, `prognosis` Associates thymic health with immunotherapy outcomes. |
| **Modalities**       | `CT`                                                                                |






**Thymus-Adult** — Thymic health consequences in adults *(Nature 2026-03)*

**[Thymic health consequences in adults](https://www.nature.com/articles/s41586-026-10242-y)**

*Nature* · 2026-03 · Published · [doi:10.1038/s41586-026-10242-y](https://doi.org/10.1038/s41586-026-10242-y)


|                      |                                                    |
| -------------------- | -------------------------------------------------- |
| **Backbone**         | U-Net and 3D ResNet-50                             |
| **Pre-training**     | `SwAV`                                             |
| **Training data**    | **5,700** CT volumes                               |
| **Downstream tasks** | `classification` Assesses thymic health in adults. |
| **Modalities**       | `CT`                                               |






**OMAFound** — A foundation model for breast and lung cancer screening using non-contrast computed tomography *(Nat. Health 2026-02)*

**[A foundation model for breast and lung cancer screening using non-contrast computed tomography](https://doi.org/10.1038/s44360-026-00055-8)**

*Nat. Health* · 2026-02 · Published · [doi:10.1038/s44360-026-00055-8](https://doi.org/10.1038/s44360-026-00055-8)


|                      |                                                                              |
| -------------------- | ---------------------------------------------------------------------------- |
| **Backbone**         | SwinUNETR-V2 encoder                                                         |
| **Pre-training**     | `self-supervised` Rotation, reconstruction and contrastive objectives.       |
| **Training data**    | Ten CT datasets **325,197** CT volumes · **151,386** patients                |
| **Downstream tasks** | `classification` Breast and lung cancer screening from non-contrast CT.      |
| **Modalities**       | `CT`                                                                         |
| **Code**             | [github.com/Qian-IMMULab/OMAFound](https://github.com/Qian-IMMULab/OMAFound) |






**CMR Transformer** — A generalizable deep learning system for cardiac MRI *(Nat. Biomed. Eng. 2026-02)*

**[A generalizable deep learning system for cardiac MRI](https://www.nature.com/articles/s41551-026-01637-3)**

*Nat. Biomed. Eng.* · 2026-02 · Published · [doi:10.1038/s41551-026-01637-3](https://doi.org/10.1038/s41551-026-01637-3)


|                      |                                                                                                     |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| **Backbone**         | Multiscale vision transformer and BERT text encoder                                                 |
| **Pre-training**     | `InfoNCE`, `contrastive` Image-report contrastive learning.                                         |
| **Training data**    | Cardiac MRI with paired reports Approximately **21,000** scans                                      |
| **Downstream tasks** | `regression`, `classification` Left-ventricular ejection fraction and 39 cardiovascular conditions. |
| **Modalities**       | `MRI`, `text`                                                                                       |
| **Code**             | [github.com/rohanshad/cmr_transformer](https://github.com/rohanshad/cmr_transformer)                |






**BrainIAC** — A generalizable foundation model for analysis of human brain MRI *(Nat. Neurosci. 2026-02)*

**[A generalizable foundation model for analysis of human brain MRI](https://www.nature.com/articles/s41593-026-02202-6)**

*Nat. Neurosci.* · 2026-02 · Published · [doi:10.1038/s41593-026-02202-6](https://doi.org/10.1038/s41593-026-02202-6)


|                      |                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------ |
| **Backbone**         | ViT-B                                                                                            |
| **Pre-training**     | `SimCLR`                                                                                         |
| **Training data**    | **32,000** MRI scans                                                                             |
| **Downstream tasks** | `classification`, `regression`, `segmentation`, `prognosis` Generalizable analysis of brain MRI. |
| **Modalities**       | `MRI`                                                                                            |
| **Code**             | [github.com/AIM-KannLab/BrainIAC](https://github.com/AIM-KannLab/BrainIAC)                       |






**CT-CLIP / CT-CHAT** — Generalist foundation models from a multimodal dataset for 3D computed tomography *(Nat. Biomed. Eng. 2026-02)*

**[Generalist foundation models from a multimodal dataset for 3D computed tomography](https://www.nature.com/articles/s41551-025-01599-y)**

*Nat. Biomed. Eng.* · 2026-02 · Published · [doi:10.1038/s41551-025-01599-y](https://doi.org/10.1038/s41551-025-01599-y)


|                      |                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------- |
| **Backbone**         | CT-ViT                                                                                       |
| **Pre-training**     | `CLIP` Contrastive alignment of CT volumes and radiology reports.                            |
| **Training data**    | CT-RATE **25,692** CT volumes                                                                |
| **Downstream tasks** | `classification`, `retrieval`, `VQA` Generalist 3D CT vision-language analysis and dialogue. |
| **Modalities**       | `CT`, `text`                                                                                 |
| **Code**             | [github.com/ibrahimethemhamamci/CT-CLIP](https://github.com/ibrahimethemhamamci/CT-CLIP)     |






**PRIMA** — Learning neuroimaging models from health system-scale data *(Nat. Biomed. Eng. 2026-02)*

**[Learning neuroimaging models from health system-scale data](https://www.nature.com/articles/s41551-025-01608-0)**

*Nat. Biomed. Eng.* · 2026-02 · Published · [doi:10.1038/s41551-025-01608-0](https://doi.org/10.1038/s41551-025-01608-0)


|                      |                                                                                 |
| -------------------- | ------------------------------------------------------------------------------- |
| **Backbone**         | Hierarchical vision transformer                                                 |
| **Pre-training**     | `CLIP`                                                                          |
| **Training data**    | **221,000** MRI studies · **5,600,000** sequences                               |
| **Downstream tasks** | `classification`, `triage`, `regression` Prediction of 52 radiologic diagnoses. |
| **Modalities**       | `MRI`, `text`                                                                   |






**MAOSS** — Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease *(Nat. Commun. 2026-02)*

**[Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease](https://www.nature.com/articles/s41467-026-68414-3)**

*Nat. Commun.* · 2026-02 · Published · [doi:10.1038/s41467-026-68414-3](https://doi.org/10.1038/s41467-026-68414-3)


|                      |                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Backbone**         | 3D ResNet-34 and ViLT                                                                                            |
| **Pre-training**     | Not recorded                                                                                                     |
| **Training data**    | Multisite imaging data and information from 226 publications                                                     |
| **Downstream tasks** | `classification`, `prognosis` Screening, staging and progression-risk stratification of steatotic liver disease. |
| **Modalities**       | `CT`, `text`                                                                                                     |
| **Code**             | [github.com/YGOX/MAOSS](https://github.com/YGOX/MAOSS)                                                           |






**AFLoc** — A multimodal vision–language model for generalizable annotation-free pathology localization *(Nat. Biomed. Eng. 2026-01)*

**[A multimodal vision–language model for generalizable annotation-free pathology localization](https://www.nature.com/articles/s41551-025-01574-7)**

*Nat. Biomed. Eng.* · 2026-01 · Published · [doi:10.1038/s41551-025-01574-7](https://doi.org/10.1038/s41551-025-01574-7)


|                      |                                                                             |
| -------------------- | --------------------------------------------------------------------------- |
| **Backbone**         | ResNet and BioClinicalBERT                                                  |
| **Pre-training**     | `CLIP`                                                                      |
| **Training data**    | MIMIC-CXR                                                                   |
| **Downstream tasks** | `localization`, `classification` Annotation-free pathology localization.    |
| **Modalities**       | `X-ray`, `text`                                                             |
| **Code**             | [github.com/YH0517/AFLoc](https://github.com/YH0517/AFLoc)                  |
| **Dataset**          | [physionet.org/content/mimic-cxr](https://physionet.org/content/mimic-cxr/) |






**deepmriprep** — deepmriprep: voxel-based morphometry preprocessing via deep neural networks *(Nat. Comput. Sci. 2026-01)*

**[deepmriprep: voxel-based morphometry preprocessing via deep neural networks](https://www.nature.com/articles/s43588-026-00953-7)**

*Nat. Comput. Sci.* · 2026-01 · Published · [doi:10.1038/s43588-026-00953-7](https://doi.org/10.1038/s43588-026-00953-7)


|                      |                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Backbone**         | 3D U-Net                                                                               |
| **Pre-training**     | Not recorded                                                                           |
| **Training data**    | **685** MRI scans                                                                      |
| **Downstream tasks** | `preprocessing` Deep-learning voxel-based morphometry preprocessing.                   |
| **Modalities**       | `MRI`                                                                                  |
| **Code**             | [github.com/wwu-mmll/deepmriprep-train](https://github.com/wwu-mmll/deepmriprep-train) |






**FOMO25** — From 100,000+ images to winning the first brain MRI foundation model challenges: sharing lessons and models *(arXiv 2026-01)*

**[From 100,000+ images to winning the first brain MRI foundation model challenges: sharing lessons and models](https://arxiv.org/abs/2601.13166)**

*arXiv* · 2026-01 · Preprint · [arXiv:2601.13166](https://arxiv.org/abs/2601.13166)


|                      |                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Backbone**         | CNN U-Net                                                                                |
| **Pre-training**     | `MAE`                                                                                    |
| **Training data**    | **115,000 + 61,000** MRI volumes                                                         |
| **Downstream tasks** | `segmentation`, `classification`, `regression` SSL3D and FOMO25 challenge tasks.         |
| **Modalities**       | `MRI`                                                                                    |
| **Code**             | [github.com/jbanusco/BrainFM4Challenges](https://github.com/jbanusco/BrainFM4Challenges) |






**VoCo** — Large-scale 3D medical image pre-training with geometric context priors *(IEEE TPAMI 2025-12)*

**[Large-scale 3D medical image pre-training with geometric context priors](https://doi.org/10.1109/tpami.2025.3639593)**

*IEEE TPAMI* · 2025-12 · Published · [doi:10.1109/TPAMI.2025.3639593](https://doi.org/10.1109/tpami.2025.3639593)


|                      |                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Backbone**         | SwinUNETR                                                                                                   |
| **Pre-training**     | `VoCo`, `contrastive learning` Volume contrastive learning with geometric context priors.                   |
| **Training data**    | PreCT-160K **160,000** CT volumes                                                                           |
| **Downstream tasks** | `segmentation`, `classification`, `regression`, `vision-language modeling` Evaluated on more than 50 tasks. |
| **Modalities**       | `CT`                                                                                                        |
| **Code**             | [github.com/Luffy03/Large-Scale-Medical](https://github.com/Luffy03/Large-Scale-Medical)                    |
| **Dataset**          | [huggingface.co/datasets/Luffy503/PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K)          |
| **PDF name**         | `VoCo - Large-Scale 3D Medical Image Pre-Training With Geometric Context Priors.pdf`                        |






**TAP-CT** — TAP-CT: 3D task-agnostic pretraining of computed tomography foundation models *(arXiv 2025-12)*

**[TAP-CT: 3D task-agnostic pretraining of computed tomography foundation models](https://arxiv.org/abs/2512.00872)**

*arXiv* · 2025-12 · Preprint · [arXiv:2512.00872](https://arxiv.org/abs/2512.00872)


|                      |                                                                                |
| -------------------- | ------------------------------------------------------------------------------ |
| **Backbone**         | 3D vision transformer                                                          |
| **Pre-training**     | `DINOv2`                                                                       |
| **Training data**    | **105,000** CT volumes                                                         |
| **Downstream tasks** | `segmentation`, `classification` Task-agnostic 3D CT foundation-model suite.   |
| **Modalities**       | `CT`                                                                           |
| **Weights**          | [huggingface.co/fomofo/tap-ct-b-3d](https://huggingface.co/fomofo/tap-ct-b-3d) |
| **PDF name**         | `TAP-CT - 3D Task-Agnostic Pretraining of CT Foundation Models.pdf`            |






**AnyMC3D** — Revisiting 2D foundation models for scalable 3D medical image classification *(arXiv 2025-12)*

**[Revisiting 2D foundation models for scalable 3D medical image classification](https://arxiv.org/abs/2512.12887)**

*arXiv* · 2025-12 · Preprint · [arXiv:2512.12887](https://arxiv.org/abs/2512.12887)


|                      |                                                                                        |
| -------------------- | -------------------------------------------------------------------------------------- |
| **Backbone**         | DINOv2 and DINOv3 backbones with lightweight task plugins                              |
| **Pre-training**     | `DINOv2`, `DINOv3`                                                                     |
| **Training data**    | Numeric scale not recorded                                                             |
| **Downstream tasks** | `classification` Scalable evaluation across 12 three-dimensional classification tasks. |
| **Modalities**       | `CT`, `MRI`                                                                            |






**Pillar-0** — Pillar-0: a new frontier for radiology foundation models *(arXiv 2025-11)*

**[Pillar-0: a new frontier for radiology foundation models](https://arxiv.org/abs/2511.17803)**

*arXiv* · 2025-11 · Preprint · [arXiv:2511.17803](https://arxiv.org/abs/2511.17803)


|                      |                                                                                  |
| -------------------- | -------------------------------------------------------------------------------- |
| **Backbone**         | Atlas                                                                            |
| **Pre-training**     | `contrastive`, `vision-language` CLIP-like radiology pretraining.                |
| **Training data**    | Abdomen-pelvis, chest and head CT plus breast MRI **155,292** volumes            |
| **Downstream tasks** | `classification`, `prognosis` Best-performing model on 319 of 366 RATE findings. |
| **Modalities**       | `CT`, `MRI`, `text`                                                              |
| **Code**             | [github.com/YalaLab/pillar-pretrain](https://github.com/YalaLab/pillar-pretrain) |
| **PDF name**         | `Pillar-0 - A New Frontier for Radiology Foundation Models.pdf`                  |






**SPECTRE** — Scaling self-supervised and cross-modal pretraining for volumetric CT transformers *(CVPR 2026 2025-11)*

**[Scaling self-supervised and cross-modal pretraining for volumetric CT transformers](https://arxiv.org/abs/2511.17209)**

*CVPR 2026* · 2025-11 · Accepted · [arXiv:2511.17209](https://arxiv.org/abs/2511.17209)


|                      |                                                                                |
| -------------------- | ------------------------------------------------------------------------------ |
| **Backbone**         | Local and global 3D vision transformers                                        |
| **Pre-training**     | `DINOv3`, `SigLIP` Self-supervised and cross-modal pretraining.                |
| **Training data**    | **230,000** CT volumes                                                         |
| **Downstream tasks** | `classification`, `segmentation`, `retrieval` Scaling study for volumetric CT. |
| **Modalities**       | `CT`, `text`                                                                   |
| **Code**             | [github.com/cclaess/SPECTRE](https://github.com/cclaess/SPECTRE)               |






**BrainFound** — Towards generalisable foundation models for brain MRI *(arXiv 2025-10)*

**[Towards generalisable foundation models for brain MRI](https://arxiv.org/abs/2510.23415)**

*arXiv* · 2025-10 · Preprint · [arXiv:2510.23415](https://arxiv.org/abs/2510.23415)


|                      |                                                                                  |
| -------------------- | -------------------------------------------------------------------------------- |
| **Backbone**         | ViT-L                                                                            |
| **Pre-training**     | `DINOv2`                                                                         |
| **Training data**    | **10,000** MRI volumes                                                           |
| **Downstream tasks** | `classification` Neurodegeneration classification and tumour grading.            |
| **Modalities**       | `MRI`                                                                            |
| **Code**             | [github.com/Moona-Mazher/BrainFound](https://github.com/Moona-Mazher/BrainFound) |






**MRI-PTPCa** — An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer *(Nat. Cancer 2025-09)*

**[An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer](https://www.nature.com/articles/s43018-025-01041-x)**

*Nat. Cancer* · 2025-09 · Published · [doi:10.1038/s43018-025-01041-x](https://doi.org/10.1038/s43018-025-01041-x)


|                      |                                                                                                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backbone**         | CNN and vision transformer                                                                                                                                       |
| **Pre-training**     | `BYOL`                                                                                                                                                           |
| **Training data**    | Numeric scale not recorded                                                                                                                                       |
| **Downstream tasks** | `classification`, `grading` Non-invasive prostate-cancer diagnosis and grading.                                                                                  |
| **Modalities**       | `MRI`, `histopathology`                                                                                                                                          |
| **Code**             | [github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer](https://github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer) |






**Curia** — Curia: a multi-modal foundation model for radiology *(arXiv 2025-08)*

**[Curia: a multi-modal foundation model for radiology](https://arxiv.org/abs/2509.06830)**

*arXiv* · 2025-08 · Preprint · [arXiv:2509.06830](https://arxiv.org/abs/2509.06830)


|                      |                                                                      |
| -------------------- | -------------------------------------------------------------------- |
| **Backbone**         | ViT-B                                                                |
| **Pre-training**     | `DINOv2`                                                             |
| **Training data**    | **164,000,000** CT and **64,000,000** MRI DICOM images               |
| **Downstream tasks** | General-purpose multimodal radiology representation learning         |
| **Modalities**       | `CT`, `MRI`                                                          |
| **Code**             | [github.com/raidium-med/curia](https://github.com/raidium-med/curia) |






**Percival** — A pan-organ vision–language model for generalizable 3D CT representations *(medRxiv 2025-07)*

**[A pan-organ vision–language model for generalizable 3D CT representations](https://pmc.ncbi.nlm.nih.gov/articles/PMC12236870/)**

*medRxiv* · 2025-07 · Preprint


|                      |                                                                                   |
| -------------------- | --------------------------------------------------------------------------------- |
| **Backbone**         | 3D DeiT                                                                           |
| **Pre-training**     | `InfoNCE`, `contrastive` Vision-language pretraining with CT volumes and reports. |
| **Training data**    | More than **403,000** CT volumes                                                  |
| **Downstream tasks** | `retrieval`, `classification`, `prognosis` Pan-organ CT representation learning.  |
| **Modalities**       | `CT`, `text`                                                                      |
| **Code**             | [github.com/cams2b/percival](https://github.com/cams2b/percival)                  |






**Spark3D** — Revisiting MAE pre-training for 3D medical image segmentation *(CVPR 2025 2025-04)*

**[Revisiting MAE pre-training for 3D medical image segmentation](https://doi.org/10.1109/CVPR52734.2025.00489)**

*CVPR 2025* · 2025-04 · Published · [doi:10.1109/CVPR52734.2025.00489](https://doi.org/10.1109/CVPR52734.2025.00489)


|                      |                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Backbone**         | CNN U-Net                                                                                 |
| **Pre-training**     | `MAE`                                                                                     |
| **Training data**    | **44,000** MRI volumes from **9,000** patients                                            |
| **Downstream tasks** | `segmentation` Masked-autoencoder pretraining for three-dimensional medical segmentation. |
| **Modalities**       | `MRI`                                                                                     |
| **Code**             | [github.com/MIC-DKFZ/nnssl](https://github.com/MIC-DKFZ/nnssl)                            |








**CT-FM** — Vision foundation models for computed tomography *(arXiv 2025-01)*

**[Vision foundation models for computed tomography](https://arxiv.org/abs/2501.09001)**

*arXiv* · 2025-01 · Preprint · [arXiv:2501.09001](https://arxiv.org/abs/2501.09001)


|                      |                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Backbone**         | SegResEncoder                                                                                                            |
| **Pre-training**     | `SimCLR`                                                                                                                 |
| **Training data**    | IDC corpus **148,000** CT volumes                                                                                        |
| **Downstream tasks** | `segmentation`, `triage`, `retrieval` General-purpose computed-tomography representations.                               |
| **Modalities**       | `CT`                                                                                                                     |
| **Code**             | [github.com/project-lighter/CT-FM](https://github.com/project-lighter/CT-FM)                                             |
| **Weights**          | [huggingface.co/project-lighter/ct_fm_feature_extractor](https://huggingface.co/project-lighter/ct_fm_feature_extractor) |
| **PDF name**         | `CT-FM - Vision Foundation Models for Computed Tomography.pdf`                                                           |






**3DINO** — A generalizable 3D framework and model for self-supervised learning in medical imaging *(arXiv 2025-01)*

**[A generalizable 3D framework and model for self-supervised learning in medical imaging](https://arxiv.org/abs/2501.11755)**

*arXiv* · 2025-01 · Preprint · [arXiv:2501.11755](https://arxiv.org/abs/2501.11755)


|                      |                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **Backbone**         | Vision transformer                                                                                |
| **Pre-training**     | `3DINO`, `self-supervised`                                                                        |
| **Training data**    | **1,300** patients                                                                                |
| **Downstream tasks** | `classification`, `segmentation` Generalizable three-dimensional self-supervised medical imaging. |
| **Modalities**       | `CT`, `MRI`                                                                                       |
| **Code**             | [github.com/AICONSlab/3DINO](https://github.com/AICONSlab/3DINO)                                  |






**BME-X** — A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks *(Nat. Biomed. Eng. 2024-12)*

**[A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks](https://www.nature.com/articles/s41551-024-01283-7)**

*Nat. Biomed. Eng.* · 2024-12 · Published · [doi:10.1038/s41551-024-01283-7](https://doi.org/10.1038/s41551-024-01283-7)


|                      |                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| **Backbone**         | U-Net CNN                                                                                             |
| **Pre-training**     | Not recorded                                                                                          |
| **Training data**    | Numeric scale not recorded                                                                            |
| **Downstream tasks** | `segmentation`, `registration`, `classification` MRI enhancement and downstream image-analysis tasks. |
| **Modalities**       | `MRI`                                                                                                 |
| **Code**             | [github.com/DBC-Lab/Brain_MRI_Enhancement](https://github.com/DBC-Lab/Brain_MRI_Enhancement)          |


