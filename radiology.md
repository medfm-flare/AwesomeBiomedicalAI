# Radiology

CT, MRI, X-ray and fMRI foundation models.

**Maintainer:** @Sumin Kim · [Judy Lyu](https://github.com/judylyu) 

**49 entries** · **Last updated: 202610** · [Back to index](README.md)

## CT

Click a model to expand its record.

| Date | Model | Venue | Model size | Training data | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 202610 | [CAPTOR](#model-captor-202610) | arXiv | _not published_ | none (25.5K volume–report pairs) | contrastive, vision-language | classification, prognosis, retrieval |
| 202609 | [nnFoundation](#model-nnfoundation-202609) | arXiv | 102M (CNN) | 2.1M volumes | MAE | segmentation, classification, report generation +2 |
| 202609 | [RADAR](#model-radar-202609) | Science | _not published_ | none (15M anatomy–text pairs) | contrastive, vision-language | classification |
| 202608 | [LiON](#model-lion-202608) | Nat. Med. | _n/a_ | 6.4K patients | _n/a_ | classification, segmentation |
| 202607 | [OrganLens](#model-organlens-202607) | arXiv | _not published_ | not stated (organ-conditioned CT) | self-supervised | classification, retrieval, prognosis |
| 202607 | [NeuroVFM](#model-neurovfm-202607) | Nat. Med. | 85.8M | 5.24M volumes | JEPA | classification, report generation, retrieval +2 |
| 202606 | [TAMP](#model-tamp-202606) | Nat. Commun. | _not published_ | none (10.8M simulated CT images) | self-supervised | enhancement |
| 202605 | [FlexiCT](#model-flexict-202605) | arXiv | _not published_ | 266K volumes | agglomerative, DINOv3, contrastive | segmentation, classification, registration +1 |
| 202605 | [MultiMedVision](#model-multimedvision-202605) | arXiv | _not published_ | none (CXR + CT-RATE) | self-supervised | classification |
| 202604 | [Curia-2](#model-curia-2-202604) | arXiv | 86M (ViT-B) | none (228M DICOM slices) | DINOv2 | classification, detection, regression |
| 202604 | [VoxelFM](#model-voxelfm-202604) | arXiv | _not published_ | 137K studies | DINO | classification, segmentation, retrieval +4 |
| 202604 | [FM-HCT](#model-fm-hct-202604) | Nat. Biomed. Eng. | 86M (ViT-B) | 362K volumes | DINO | classification, retrieval |
| 202603 | [Merlin](#model-merlin-202603) | Nature | 121M | none (25.5K volume–report pairs) | CLIP | classification, segmentation, retrieval +2 |
| 202603 | [Thymus-IO](#model-thymus-io-202603) | Nature | _n/a_ | 5.7K CT volumes | SwAV | classification, prognosis |
| 202603 | [Thymus-Adult](#model-thymus-adult-202603) | Nature | _n/a_ | 5.7K CT volumes | SwAV | classification |
| 202603 | [SegAnyPET](#model-seganypet-202603) | arXiv | _not published_ | 11K PET volumes | _n/a_ | segmentation |
| 202602 | [OMAFound](#model-omafound-202602) | Nat. Health | _not published_ | 325.2K CT volumes | self-supervised | classification |
| 202602 | [CT-CLIP / CT-CHAT](#model-ct-clip-ct-chat-202602) | Nat. Biomed. Eng. | _not published_ | none (25.7K volume–text pairs) | CLIP | classification, retrieval, VQA |
| 202602 | [MAOSS](#model-maoss-202602) | Nat. Commun. | _not published_ | not stated (multisite CT + literature) | _n/a_ | classification, prognosis |
| 202602 | [TANGERINE](#model-tangerine-202602) | Commun. Med. | 307M (ViT-L) | 98K volumes | MAE | classification |
| 202601 | [SDF-HOLO](#model-sdf-holo-202601) | arXiv | _not published_ | 10K patients | vision-language | segmentation, detection, report generation |
| 202512 | [VoCo](#model-voco-202512) | IEEE TPAMI | 53M (SwinUNETR-B) | 160K volumes | VoCo, contrastive learning | segmentation, classification, regression +1 |
| 202512 | [TAP-CT](#model-tap-ct-202512) | arXiv | 86M (ViT-B 3D) | 105K volumes | DINOv2 | segmentation, classification |
| 202512 | [AnyMC3D](#model-anymc3d-202512) | arXiv | _n/a_ | none (frozen DINOv2/3) | DINOv2, DINOv3 | classification |
| 202511 | [Pillar-0](#model-pillar-0-202511) | arXiv | 79M (Atlas enc.) | none (~155K volume–report pairs) | contrastive, vision-language | classification, prognosis |
| 202511 | [SPECTRE](#model-spectre-202511) | CVPR 2026 | 339M (local enc.) | 230K CT volumes | DINOv3, SigLIP | classification, segmentation, retrieval |
| 202508 | [RadFM](#model-radfm-202508) | Nat. Commun. | 14B | none (16M 2D/3D image–text) | vision-language | classification, VQA, report generation |
| 202508 | [Curia](#model-curia-202508) | arXiv | 86M | none (228M DICOM slices) | DINOv2 | General-purpose multimodal radiology representation learning |
| 202507 | [Percival](#model-percival-202507) | medRxiv | 22M (DeiT-S enc.) | none (403K volume–report pairs) | InfoNCE, contrastive | retrieval, classification, prognosis |
| 202503 | [FratMAE](#model-fratmae-202503) | arXiv | 86M (ViT-B) | 1.3K PET/CT volumes | MAE | segmentation, classification |
| 202501 | [CT-FM](#model-ct-fm-202501) | arXiv | 77.8M | 148K CT volumes | SimCLR | segmentation, triage, retrieval |
| 202501 | [3DINO](#model-3dino-202501) | arXiv | 307M (ViT-L) | ~100K volumes | 3DINO, self-supervised | classification, segmentation |

<a id="model-captor-202610"></a>
<details>
<summary><b>CAPTOR</b> — CAPTOR: a vision-language foundation model for Chest-Abdomen-Pelvis Oncologic CT <i>(arXiv 202610)</i></summary>

**[CAPTOR: a vision-language foundation model for Chest-Abdomen-Pelvis Oncologic CT](https://arxiv.org/abs/2610.14226)**

*arXiv* · 202610 · [arXiv:2610.14226](https://arxiv.org/abs/2610.14226)

| | |
| --- | --- |
| **Backbone** | 3D-inflated ResNet-152 (I3ResNet) and Clinical-Longformer |
| **Pre-training** | `contrastive`, `vision-language`<br>CLIP-style alignment of 3D CAP CT regions with corresponding radiology-report text; architecture based on Merlin. |
| **Training data** | Oncologic chest–abdomen–pelvis CT with paired reports<br>**25,512** volume–report pairs for the paper model; a 100K-study checkpoint is also released |
| **Downstream tasks** | `classification`, `prognosis`, `retrieval`<br>Disease detection, TumorImagingBench survival prediction and image retrieval on CAP and oncologic subsets. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/Guerbet-AI/CAPTOR](https://github.com/Guerbet-AI/CAPTOR) |
| **Weights** | [huggingface.co/Guerbet-AI/CAPTOR](https://huggingface.co/Guerbet-AI/CAPTOR) |

</details>

<a id="model-nnfoundation-202609"></a>
<details>
<summary><b>nnFoundation</b> — nnFoundation: 3D foundation models for radiology <i>(arXiv 202609)</i></summary>

**[nnFoundation: 3D Foundation Models for Radiology](https://arxiv.org/abs/2609.26924)**

*arXiv* · 202609 · [arXiv:2609.26924](https://arxiv.org/abs/2609.26924)

| | |
| --- | --- |
| **Parameters** | 102M (CNN) |
| **Parameter note** | 102M is the released nnFoundation CNN (ResEnc-L). The complementary nnFoundation ViT (Primus, depth 40, dim 1056) has 674M parameters. |
| **Backbone** | Residual encoder CNN and Primus vision transformer |
| **Pre-training** | `MAE`<br>Masked autoencoding on the full 2.1M-volume corpus; DINOv2 and contrastive objectives were compared on a 630K-volume proxy set. |
| **Training data** | CT, MRI and PET<br>**2,100,000** volumes |
| **Downstream tasks** | `segmentation`, `classification`, `report generation`, `retrieval`, `detection`<br>Evaluated on 108 tasks spanning CT, MRI and PET. |
| **Modalities** | `CT`, `MRI`, `PET` |
| **Code** | [github.com/MIC-DKFZ/nnssl](https://github.com/MIC-DKFZ/nnssl) |
| **Weights** | [huggingface.co/MIC-DKFZ/nnFoundationCNN](https://huggingface.co/MIC-DKFZ/nnFoundationCNN) |

</details>

<a id="model-radar-202609"></a>
<details>
<summary><b>RADAR</b> — An expert-level generalist AI for abdominal CT diagnosis <i>(Science 202609)</i></summary>

**[An expert-level generalist AI for abdominal CT diagnosis](https://www.science.org/doi/10.1126/science.aec6129)**

*Science* · 202609 · [doi:10.1126/science.aec6129](https://doi.org/10.1126/science.aec6129)

| | |
| --- | --- |
| **Backbone** | U-Net vision encoder and BERT text encoder |
| **Pre-training** | `contrastive`, `vision-language`<br>Anatomy-level image–text alignment of abdominal CT structures with radiology-report descriptions. |
| **Training data** | Contrast-enhanced abdominal CT<br>**424,911** examinations · **15,000,000** anatomy-wise image–text pairs |
| **Downstream tasks** | `classification`<br>Generalist diagnosis across 18 anatomical structures and 146 imaging findings. |
| **Modalities** | `CT`, `text` |
| **Code** | [doi.org/10.5281/zenodo.21271172](https://doi.org/10.5281/zenodo.21271172) |
| **Weights** | [huggingface.co/radar-generalist/RADAR](https://huggingface.co/radar-generalist/RADAR) |

</details>

<a id="model-lion-202608"></a>
<details>
<summary><b>LiON</b> — Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial <i>(Nat. Med. 202608)</i></summary>

**[Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial](https://www.nature.com/articles/s41591-026-04589-y)**

*Nat. Med.* · 202608 · [doi:10.1038/s41591-026-04589-y](https://doi.org/10.1038/s41591-026-04589-y)

| | |
| --- | --- |
| **Backbone** | Feature pyramid network with query-based classifier and segmentator |
| **Pre-training** | `_n/a_`<br>Supervised end-to-end training for liver malignancy diagnosis; not a self-supervised foundation-model pre-training recipe. |
| **Training data** | Contrast-enhanced CT<br>**6,443** patients |
| **Downstream tasks** | `classification`, `segmentation`<br>Patient-level liver malignancy diagnosis and eight-type lesion segmentation. |
| **Modalities** | `CT` |
| **Code** | [github.com/alibaba-damo-academy/pixel-lesion-patient-network](https://github.com/alibaba-damo-academy/pixel-lesion-patient-network) |

</details>

<a id="model-organlens-202607"></a>
<details>
<summary><b>OrganLens</b> — Organ-specific representation learning for CT foundation models <i>(arXiv 202607)</i></summary>

**[OrganLens: Organ-Specific Representation Learning for CT Foundation Models](https://arxiv.org/abs/2607.25164)**

*arXiv* · 202607 · [arXiv:2607.25164](https://arxiv.org/abs/2607.25164)

| | |
| --- | --- |
| **Backbone** | Shared CT encoder with organ-identity conditioning |
| **Pre-training** | `self-supervised`<br>Organ-specific distillation and anatomy-mask supervision, with anatomy-weighted pooling into 11 organ-specific representations. |
| **Training data** | Organ-conditioned CT; numeric pretraining scale not stated<br>Evaluated on CT-RATE, RAD-ChestCT, INSPECT and NLST. |
| **Downstream tasks** | `classification`, `retrieval`, `prognosis`<br>Organ-matched findings, image–text retrieval and lung-cancer mortality. |
| **Modalities** | `CT` |

</details>

<a id="model-neurovfm-202607"></a>
<details>
<summary><b>NeuroVFM</b> — Health system learning enables generalist neuroimaging models <i>(Nat. Med. 202607)</i></summary>

**[Health system learning enables generalist neuroimaging models](https://www.nature.com/articles/s41591-026-04497-1)**

*Nat. Med.* · 202607 · [doi:10.1038/s41591-026-04497-1](https://doi.org/10.1038/s41591-026-04497-1)

| | |
| --- | --- |
| **Parameters** | 85.8M |
| **Parameter note** | 85.8M is the released ViT-Base encoder; the paper also reports a ViT-Small variant with 21.7M parameters. Diagnostic heads and the findings LLM are separate. |
| **Backbone** | 3D vision transformer |
| **Pre-training** | `JEPA`<br>Volumetric joint-embedding predictive pretraining. |
| **Training data** | CT and MRI neuroimaging<br>**5,240,000** volumes |
| **Downstream tasks** | `classification`, `report generation`, `retrieval`, `triage`, `registration`<br>Generalist health-system neuroimaging. |
| **Modalities** | `CT`, `MRI` |
| **Code** | [github.com/MLNeurosurg/neurovfm](https://github.com/MLNeurosurg/neurovfm) |

</details>

<a id="model-tamp-202606"></a>
<details>
<summary><b>TAMP</b> — Imaging foundation model for universal enhancement of non-ideal measurement CT <i>(Nat. Commun. 202606)</i></summary>

**[Imaging foundation model for universal enhancement of non-ideal measurement CT](https://www.nature.com/articles/s41467-026-73943-y)**

*Nat. Commun.* · 202606 · [doi:10.1038/s41467-026-73943-y](https://doi.org/10.1038/s41467-026-73943-y)

| | |
| --- | --- |
| **Backbone** | Multi-scale integrated Transformer Amplifier |
| **Pre-training** | `self-supervised`<br>Pretrained on physics-driven simulated non-ideal measurement CT (low-dose, sparse-view and limited-angle) for universal enhancement. |
| **Training data** | Simulated non-ideal measurement CT<br>**10,800,000** images |
| **Downstream tasks** | `enhancement`<br>Universal NICT enhancement with optional LoRA adaptation to specific clinical protocols. |
| **Modalities** | `CT` |
| **Code** | [github.com/YutingHe-list/TAMP](https://github.com/YutingHe-list/TAMP) |

</details>

<a id="model-flexict-202605"></a>
<details>
<summary><b>FlexiCT</b> — Universal CT representations from anatomy to disease phenotype through agglomerative pretraining <i>(arXiv 202605)</i></summary>

**[Universal CT Representations from Anatomy to Disease Phenotype through Agglomerative Pretraining](https://arxiv.org/abs/2605.21906)**

*arXiv* · 202605 · [arXiv:2605.21906](https://arxiv.org/abs/2605.21906)

| | |
| --- | --- |
| **Backbone** | 2D and 3D vision transformers |
| **Pre-training** | `agglomerative`, `DINOv3`, `contrastive`<br>Continual pretraining in three stages: 2D axial DINOv3, 3D volumetric teacher–student and report-guided CLIP alignment. |
| **Training data** | Public CT datasets<br>**266,227** volumes from 56 datasets |
| **Downstream tasks** | `segmentation`, `classification`, `registration`, `retrieval`<br>Also report-aligned zero-shot classification; five evaluation families in the paper. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/ricklisz/FlexiCT](https://github.com/ricklisz/FlexiCT) |

</details>

<a id="model-multimedvision-202605"></a>
<details>
<summary><b>MultiMedVision</b> — Multi-modal medical vision framework <i>(arXiv 202605)</i></summary>

**[MultiMedVision: Multi-Modal Medical Vision Framework](https://arxiv.org/abs/2605.09151)**

*arXiv* · 202605 · [arXiv:2605.09151](https://arxiv.org/abs/2605.09151)

| | |
| --- | --- |
| **Backbone** | Sparse vision transformer with 3D rotary positional embeddings |
| **Pre-training** | `self-supervised`<br>Joint 2D/3D representation learning on mixed-modality batches in a shared latent space, without modality-specific adapters. |
| **Training data** | Chest X-ray (MIMIC-CXR) and CT (CT-RATE) |
| **Downstream tasks** | `classification`<br>2D chest X-ray benchmarks and 3D CT-RATE tasks with a single shared encoder. |
| **Modalities** | `CT`, `X-ray` |

</details>

<a id="model-curia-2-202604"></a>
<details>
<summary><b>Curia-2</b> — Scaling self-supervised learning for radiology foundation models <i>(arXiv 202604)</i></summary>

**[Curia-2: Scaling Self-Supervised Learning for Radiology Foundation Models](https://arxiv.org/abs/2604.01987)**

*arXiv* · 202604 · [arXiv:2604.01987](https://arxiv.org/abs/2604.01987)

| | |
| --- | --- |
| **Parameters** | 86M (ViT-B) |
| **Parameter note** | 86M is Curia-2 B (ViT-B). The paper also reports Curia-2 L (303M) and Curia-2 g (1.3B). |
| **Backbone** | Vision transformer |
| **Pre-training** | `DINOv2`<br>Radiology-adapted DINOv2 with content-aware cropping, anatomically guided iBOT masking and SigReg; trained on 400M images from the Curia corpus. |
| **Training data** | **164,000,000** CT and **64,000,000** MRI DICOM images |
| **Downstream tasks** | `classification`, `detection`, `regression`<br>CuriaBench 2D (slice) and 3D (volumetric) tracks, including findings detection. |
| **Modalities** | `CT`, `MRI` |

</details>

<a id="model-voxelfm-202604"></a>
<details>
<summary><b>VoxelFM</b> — Learning robust visual features in computed tomography enables efficient transfer learning for clinical tasks <i>(arXiv 202604)</i></summary>

**[Learning Robust Visual Features in Computed Tomography Enables Efficient Transfer Learning for Clinical Tasks](https://arxiv.org/abs/2604.04133)**

*arXiv* · 202604 · [arXiv:2604.04133](https://arxiv.org/abs/2604.04133)

| | |
| --- | --- |
| **Backbone** | 3D vision transformer (ViT-B) |
| **Pre-training** | `DINO`<br>3D self-distillation without language supervision; frozen-backbone transfer with lightweight probes. |
| **Training data** | Multi-institution CT<br>**137,000** studies |
| **Downstream tasks** | `classification`, `segmentation`, `retrieval`, `regression`, `localization`, `report generation`, `prognosis`<br>Seven frozen-probe task families, including survival analysis. |
| **Modalities** | `CT` |
| **Code** | [github.com/rmaguado/VoxelFM](https://github.com/rmaguado/VoxelFM) |
| **Weights** | [huggingface.co/rmaguado/VoxelFM](https://huggingface.co/rmaguado/VoxelFM) |

</details>

<a id="model-fm-hct-202604"></a>
<details>
<summary><b>FM-HCT</b> — 3D foundation model for generalizable disease detection in head computed tomography <i>(Nat. Biomed. Eng. 202604)</i></summary>

**[3D foundation model for generalizable disease detection in head computed tomography](https://www.nature.com/articles/s41551-026-01668-w)**

*Nat. Biomed. Eng.* · 202604 · [doi:10.1038/s41551-026-01668-w](https://doi.org/10.1038/s41551-026-01668-w)

| | |
| --- | --- |
| **Parameters** | 86M (ViT-B) |
| **Parameter note** | The paper specifies a ViT-Base configuration (768-dim, 12 layers, 12 heads) on 512 patches of 12×12×12 voxels but does not print a parameter total; 86M follows the standard ViT-Base count. |
| **Backbone** | Vision transformer |
| **Pre-training** | `DINO` |
| **Training data** | Head CT<br>**362,000** volumes |
| **Downstream tasks** | `classification`, `retrieval`<br>Generalizable disease detection in head CT. |
| **Modalities** | `CT` |
| **Code** | [github.com/NYUMedML/headCT_foundation](https://github.com/NYUMedML/headCT_foundation) |

</details>

<a id="model-merlin-202603"></a>
<details>
<summary><b>Merlin</b> — Merlin: a computed tomography vision–language foundation model and dataset <i>(Nature 202603)</i></summary>

**[Merlin: a computed tomography vision–language foundation model and dataset](https://www.nature.com/articles/s41586-026-10181-8)**

*Nature* · 202603 · [doi:10.1038/s41586-026-10181-8](https://doi.org/10.1038/s41586-026-10181-8)

| | |
| --- | --- |
| **Parameters** | 121M |
| **Parameter note** | 121M is the full vision–language model total from third-party benchmark tables (e.g. Pillar-0); the primary image encoder is an inflated 3D ResNet-152, paired with a Clinical Longformer text encoder. Not comparable with a vision-encoder-only count such as Curia-B's 86M. |
| **Backbone** | ResNet vision encoder and Longformer text encoder |
| **Pre-training** | `CLIP` |
| **Training data** | CT volumes paired with clinical text<br>**25,500** CT volumes |
| **Downstream tasks** | `classification`, `segmentation`, `retrieval`, `report generation`, `prognosis` |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/StanfordMIMI/Merlin](https://github.com/StanfordMIMI/Merlin) |
| **Dataset** | [github.com/StanfordMIMI/Merlin](https://github.com/StanfordMIMI/Merlin) |

</details>

<a id="model-thymus-io-202603"></a>
<details>
<summary><b>Thymus-IO</b> — Thymic health and immunotherapy outcomes in patients with cancer <i>(Nature 202603)</i></summary>

**[Thymic health and immunotherapy outcomes in patients with cancer](https://www.nature.com/articles/s41586-026-10243-x)**

*Nature* · 202603 · [doi:10.1038/s41586-026-10243-x](https://doi.org/10.1038/s41586-026-10243-x)

| | |
| --- | --- |
| **Backbone** | U-Net and 3D ResNet-50 |
| **Pre-training** | `SwAV` |
| **Training data** | **5,700** CT volumes |
| **Downstream tasks** | `classification`, `prognosis`<br>Associates thymic health with immunotherapy outcomes. |
| **Modalities** | `CT` |

</details>

<a id="model-thymus-adult-202603"></a>
<details>
<summary><b>Thymus-Adult</b> — Thymic health consequences in adults <i>(Nature 202603)</i></summary>

**[Thymic health consequences in adults](https://www.nature.com/articles/s41586-026-10242-y)**

*Nature* · 202603 · [doi:10.1038/s41586-026-10242-y](https://doi.org/10.1038/s41586-026-10242-y)

| | |
| --- | --- |
| **Backbone** | U-Net and 3D ResNet-50 |
| **Pre-training** | `SwAV` |
| **Training data** | **5,700** CT volumes |
| **Downstream tasks** | `classification`<br>Assesses thymic health in adults. |
| **Modalities** | `CT` |

</details>

<a id="model-seganypet-202603"></a>
<details>
<summary><b>SegAnyPET</b> — Developing foundation models for universal segmentation from 3D whole-body positron emission tomography <i>(arXiv 202603)</i></summary>

**[Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)**

*arXiv* · 202603 · [arXiv:2603.11627](https://arxiv.org/abs/2603.11627)

| | |
| --- | --- |
| **Backbone** | 3D promptable segmentation network adapted from SAM-Med3D |
| **Pre-training** | `_n/a_`<br>Supervised promptable segmentation on whole-body PET; not a self-supervised encoder pre-training recipe. |
| **Training data** | Multi-center, multi-tracer, multi-disease whole-body PET<br>**11,041** 3D scans · **59,831** segmentation masks |
| **Downstream tasks** | `segmentation`<br>Zero-shot organ and lesion segmentation with a human-in-the-loop prompt workflow. |
| **Modalities** | `PET` |
| **Code** | [github.com/YichiZhang98/SegAnyPET](https://github.com/YichiZhang98/SegAnyPET) |

</details>

<a id="model-omafound-202602"></a>
<details>
<summary><b>OMAFound</b> — A foundation model for breast and lung cancer screening using non-contrast computed tomography <i>(Nat. Health 202602)</i></summary>

**[A foundation model for breast and lung cancer screening using non-contrast computed tomography](https://doi.org/10.1038/s44360-026-00055-8)**

*Nat. Health* · 202602 · [doi:10.1038/s44360-026-00055-8](https://doi.org/10.1038/s44360-026-00055-8)

| | |
| --- | --- |
| **Backbone** | SwinUNETR-V2 encoder |
| **Pre-training** | `self-supervised`<br>Rotation, reconstruction and contrastive objectives. |
| **Training data** | Ten CT datasets<br>**325,197** CT volumes · **151,386** patients |
| **Downstream tasks** | `classification`<br>Breast and lung cancer screening from non-contrast CT. |
| **Modalities** | `CT` |
| **Code** | [github.com/Qian-IMMULab/OMAFound](https://github.com/Qian-IMMULab/OMAFound) |

</details>

<a id="model-ct-clip-ct-chat-202602"></a>
<details>
<summary><b>CT-CLIP / CT-CHAT</b> — Generalist foundation models from a multimodal dataset for 3D computed tomography <i>(Nat. Biomed. Eng. 202602)</i></summary>

**[Generalist foundation models from a multimodal dataset for 3D computed tomography](https://www.nature.com/articles/s41551-025-01599-y)**

*Nat. Biomed. Eng.* · 202602 · [doi:10.1038/s41551-025-01599-y](https://doi.org/10.1038/s41551-025-01599-y)

| | |
| --- | --- |
| **Backbone** | CT-ViT |
| **Pre-training** | `CLIP`<br>Contrastive alignment of CT volumes and radiology reports. |
| **Training data** | CT-RATE<br>**25,692** CT volumes |
| **Downstream tasks** | `classification`, `retrieval`, `VQA`<br>Generalist 3D CT vision-language analysis and dialogue. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/ibrahimethemhamamci/CT-CLIP](https://github.com/ibrahimethemhamamci/CT-CLIP) |

</details>

<a id="model-maoss-202602"></a>
<details>
<summary><b>MAOSS</b> — Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease <i>(Nat. Commun. 202602)</i></summary>

**[Multi-modal AI for opportunistic screening, staging and progression risk stratification of steatotic liver disease](https://www.nature.com/articles/s41467-026-68414-3)**

*Nat. Commun.* · 202602 · [doi:10.1038/s41467-026-68414-3](https://doi.org/10.1038/s41467-026-68414-3)

| | |
| --- | --- |
| **Backbone** | 3D ResNet-34 and ViLT |
| **Pre-training** | `_n/a_`<br>Supervised multimodal training with a missing-aware alignment module; not a self-supervised foundation-model pre-training recipe. |
| **Training data** | Multisite imaging data and information from 226 publications |
| **Downstream tasks** | `classification`, `prognosis`<br>Screening, staging and progression-risk stratification of steatotic liver disease. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/YGOX/MAOSS](https://github.com/YGOX/MAOSS) |

</details>

<a id="model-tangerine-202602"></a>
<details>
<summary><b>TANGERINE</b> — A computationally frugal, open-source chest CT foundation model for thoracic disease detection in lung cancer screening programmes <i>(Commun. Med. 202602)</i></summary>

**[A computationally frugal, open-source chest CT foundation model for thoracic disease detection in lung cancer screening programmes](https://www.nature.com/articles/s43856-025-01328-1)**

*Commun. Med.* · 202602 · [doi:10.1038/s43856-025-01328-1](https://doi.org/10.1038/s43856-025-01328-1)

| | |
| --- | --- |
| **Parameters** | 307M (ViT-L) |
| **Parameter note** | The paper specifies a ViT-Large encoder (24 blocks, 1024-dim embeddings) but does not print a parameter total; 307M follows the standard ViT-Large count. |
| **Backbone** | 3D ViT-Large masked autoencoder |
| **Pre-training** | `MAE`<br>3D masked autoencoding on volumetric thoracic low-dose CT (75% masking). |
| **Training data** | Public and private thoracic LDCT, including SUMMIT<br>**98,000** volumes |
| **Downstream tasks** | `classification`<br>Fourteen thoracic disease-detection tasks, including lung cancer and interstitial lung abnormality. |
| **Modalities** | `CT` |
| **Code** | [github.com/niccolo246/3D-MAE-MedImaging](https://github.com/niccolo246/3D-MAE-MedImaging) |
| **Weights** | [doi.org/10.5281/zenodo.18835750](https://doi.org/10.5281/zenodo.18835750) |

</details>

<a id="model-sdf-holo-202601"></a>
<details>
<summary><b>SDF-HOLO</b> — A generalist foundation model for total-body PET/CT enables diagnostic reporting and system-wide metabolic profiling <i>(arXiv 202601)</i></summary>

**[A Generalist Foundation Model for Total-body PET/CT Enables Diagnostic Reporting and System-wide Metabolic Profiling](https://arxiv.org/abs/2601.12820)**

*arXiv* · 202601 · [arXiv:2601.12820](https://arxiv.org/abs/2601.12820)

| | |
| --- | --- |
| **Backbone** | Dual-stream PET and CT encoders with cross-modal interaction |
| **Pre-training** | `vision-language`<br>Voxel–mask–text alignment with hierarchical local-window and global attention across total-body PET/CT. |
| **Training data** | Total-body PET/CT<br>More than **10,000** patients |
| **Downstream tasks** | `segmentation`, `detection`, `report generation`<br>Tumor segmentation, low-dose lesion detection and multilingual diagnostic reporting, plus system-wide metabolic profiling. |
| **Modalities** | `PET`, `CT`, `text` |

</details>

<a id="model-voco-202512"></a>
<details>
<summary><b>VoCo</b> — Large-scale 3D medical image pre-training with geometric context priors <i>(IEEE TPAMI 202512)</i></summary>

**[Large-scale 3D medical image pre-training with geometric context priors](https://doi.org/10.1109/tpami.2025.3639593)**

*IEEE TPAMI* · 202512 · [doi:10.1109/TPAMI.2025.3639593](https://doi.org/10.1109/tpami.2025.3639593)

| | |
| --- | --- |
| **Parameters** | 53M |
| **Parameter note** | 53M matches the released VoCo_B_SSL_head checkpoint (SwinUNETR Base, feature_size=48); the repository also lists 31M–1.2B variants. |
| **Backbone** | SwinUNETR |
| **Pre-training** | `VoCo`, `contrastive learning`<br>Volume contrastive learning with geometric context priors. |
| **Training data** | PreCT-160K<br>**160,000** CT volumes |
| **Downstream tasks** | `segmentation`, `classification`, `regression`, `vision-language modeling`<br>Evaluated on more than 50 tasks. |
| **Modalities** | `CT` |
| **Code** | [github.com/Luffy03/Large-Scale-Medical](https://github.com/Luffy03/Large-Scale-Medical) |
| **Dataset** | [huggingface.co/datasets/Luffy503/PreCT-160K](https://huggingface.co/datasets/Luffy503/PreCT-160K) |
| **PDF name** | `VoCo - Large-Scale 3D Medical Image Pre-Training With Geometric Context Priors.pdf` |

</details>

<a id="model-tap-ct-202512"></a>
<details>
<summary><b>TAP-CT</b> — TAP-CT: 3D task-agnostic pretraining of computed tomography foundation models <i>(arXiv 202512)</i></summary>

**[TAP-CT: 3D task-agnostic pretraining of computed tomography foundation models](https://arxiv.org/abs/2512.00872)**

*arXiv* · 202512 · [arXiv:2512.00872](https://arxiv.org/abs/2512.00872)

| | |
| --- | --- |
| **Parameters** | 86M |
| **Parameter note** | Table 1 in the TAP-CT paper lists 86.0M for TAP-B-3D (ViT-Base 3D); the HuggingFace checkpoint reports 87.1M safetensors total. |
| **Backbone** | 3D vision transformer |
| **Pre-training** | `DINOv2` |
| **Training data** | **105,000** CT volumes |
| **Downstream tasks** | `segmentation`, `classification`<br>Task-agnostic 3D CT foundation-model suite. |
| **Modalities** | `CT` |
| **Weights** | [huggingface.co/fomofo/tap-ct-b-3d](https://huggingface.co/fomofo/tap-ct-b-3d) |
| **PDF name** | `TAP-CT - 3D Task-Agnostic Pretraining of CT Foundation Models.pdf` |

</details>

<a id="model-anymc3d-202512"></a>
<details>
<summary><b>AnyMC3D</b> — Revisiting 2D foundation models for scalable 3D medical image classification <i>(arXiv 202512)</i></summary>

**[Revisiting 2D foundation models for scalable 3D medical image classification](https://arxiv.org/abs/2512.12887)**

*arXiv* · 202512 · [arXiv:2512.12887](https://arxiv.org/abs/2512.12887)

| | |
| --- | --- |
| **Backbone** | DINOv2 and DINOv3 backbones with lightweight task plugins |
| **Pre-training** | `DINOv2`, `DINOv3` |
| **Training data** | none (frozen DINOv2/3)<br>Uses frozen 2D foundation-model backbones with lightweight task plugins; no native 3D pre-training corpus. |
| **Downstream tasks** | `classification`<br>Scalable evaluation across 12 three-dimensional classification tasks. |
| **Modalities** | `CT`, `MRI` |

</details>

<a id="model-pillar-0-202511"></a>
<details>
<summary><b>Pillar-0</b> — Pillar-0: a new frontier for radiology foundation models <i>(arXiv 202511)</i></summary>

**[Pillar-0: a new frontier for radiology foundation models](https://arxiv.org/abs/2511.17803)**

*arXiv* · 202511 · [arXiv:2511.17803](https://arxiv.org/abs/2511.17803)

| | |
| --- | --- |
| **Parameters** | 79M |
| **Parameter note** | 79M is the Atlas vision encoder only; pretraining aligns it with a frozen Qwen3-Embedding-8B text encoder, which is not included. |
| **Backbone** | Atlas |
| **Pre-training** | `contrastive`, `vision-language`<br>CLIP-like radiology pretraining. |
| **Training data** | Abdomen-pelvis, chest and head CT plus breast MRI<br>**155,292** volumes |
| **Downstream tasks** | `classification`, `prognosis`<br>Best-performing model on 319 of 366 RATE findings. |
| **Modalities** | `CT`, `MRI`, `text` |
| **Code** | [github.com/YalaLab/pillar-pretrain](https://github.com/YalaLab/pillar-pretrain) |
| **PDF name** | `Pillar-0 - A New Frontier for Radiology Foundation Models.pdf` |

</details>

<a id="model-spectre-202511"></a>
<details>
<summary><b>SPECTRE</b> — Scaling self-supervised and cross-modal pretraining for volumetric CT transformers <i>(CVPR 2026 202511)</i></summary>

**[Scaling self-supervised and cross-modal pretraining for volumetric CT transformers](https://arxiv.org/abs/2511.17209)**

*CVPR 2026* · 202511 · [arXiv:2511.17209](https://arxiv.org/abs/2511.17209)

| | |
| --- | --- |
| **Parameters** | 339M |
| **Parameter note** | 339M is the local ViT-L backbone (d=1080, 24 layers); the full SPECTRE release also includes a global transformer and cross-modal components. |
| **Backbone** | Local and global 3D vision transformers |
| **Pre-training** | `DINOv3`, `SigLIP`<br>Self-supervised and cross-modal pretraining. |
| **Training data** | **230,000** CT volumes |
| **Downstream tasks** | `classification`, `segmentation`, `retrieval`<br>Scaling study for volumetric CT. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/cclaess/SPECTRE](https://github.com/cclaess/SPECTRE) |

</details>

<a id="model-radfm-202508"></a>
<details>
<summary><b>RadFM</b> — Towards generalist foundation model for radiology by leveraging web-scale 2D&3D medical data <i>(Nat. Commun. 202508)</i></summary>

**[Towards generalist foundation model for radiology by leveraging web-scale 2D&3D medical data](https://www.nature.com/articles/s41467-025-62385-7)**

*Nat. Commun.* · 202508 · [doi:10.1038/s41467-025-62385-7](https://doi.org/10.1038/s41467-025-62385-7)

| | |
| --- | --- |
| **Parameters** | 14B |
| **Parameter note** | 14B is the full visually conditioned generative model stated in the paper, not a vision-encoder-only count. |
| **Backbone** | 3D vision transformer with Perceiver and LLaMA language decoder |
| **Pre-training** | `vision-language`<br>Generative multimodal pretraining on interleaved 2D/3D scans and text (MedMD), then radiology instruction tuning on RadMD. |
| **Training data** | 2D and 3D radiology scans with paired text<br>**16,000,000** images |
| **Downstream tasks** | `classification`, `VQA`, `report generation`<br>Diagnosis, visual question answering, report generation and rationale diagnosis on RadBench and public benchmarks. |
| **Modalities** | `CT`, `MRI`, `X-ray`, `PET`, `text` |
| **Code** | [github.com/chaoyi-wu/RadFM](https://github.com/chaoyi-wu/RadFM) |
| **Weights** | [huggingface.co/chaoyi-wu/RadFM](https://huggingface.co/chaoyi-wu/RadFM) |

</details>

<a id="model-curia-202508"></a>
<details>
<summary><b>Curia</b> — Curia: a multi-modal foundation model for radiology <i>(arXiv 202508)</i></summary>

**[Curia: a multi-modal foundation model for radiology](https://arxiv.org/abs/2509.06830)**

*arXiv* · 202508 · [arXiv:2509.06830](https://arxiv.org/abs/2509.06830)

| | |
| --- | --- |
| **Parameters** | 86M |
| **Parameter note** | Curia-B (ViT-B) released for downstream use; the paper also trains Curia-L at 300M on the full 200M-image corpus. |
| **Backbone** | ViT-B |
| **Pre-training** | `DINOv2` |
| **Training data** | **164,000,000** CT and **64,000,000** MRI DICOM images |
| **Downstream tasks** | General-purpose multimodal radiology representation learning |
| **Modalities** | `CT`, `MRI` |
| **Code** | [github.com/raidium-med/curia](https://github.com/raidium-med/curia) |

</details>

<a id="model-percival-202507"></a>
<details>
<summary><b>Percival</b> — A pan-organ vision–language model for generalizable 3D CT representations <i>(medRxiv 202507)</i></summary>

**[A pan-organ vision–language model for generalizable 3D CT representations](https://pmc.ncbi.nlm.nih.gov/articles/PMC12236870/)**

*medRxiv* · 202507

| | |
| --- | --- |
| **Parameters** | 22M |
| **Parameter note** | DeiT-Small Patch16 vision encoder adapted for 3D patches; the Clinical Longformer text encoder is excluded. Standard DeiT-S count. |
| **Backbone** | 3D DeiT |
| **Pre-training** | `InfoNCE`, `contrastive`<br>Vision-language pretraining with CT volumes and reports. |
| **Training data** | More than<br>**403,000** CT volumes |
| **Downstream tasks** | `retrieval`, `classification`, `prognosis`<br>Pan-organ CT representation learning. |
| **Modalities** | `CT`, `text` |
| **Code** | [github.com/cams2b/percival](https://github.com/cams2b/percival) |

</details>

<a id="model-fratmae-202503"></a>
<details>
<summary><b>FratMAE</b> — Developing a PET/CT foundation model for cross-modal anatomical and functional imaging <i>(arXiv 202503)</i></summary>

**[Developing a PET/CT Foundation Model for Cross-Modal Anatomical and Functional Imaging](https://arxiv.org/abs/2503.02824)**

*arXiv* · 202503 · [arXiv:2503.02824](https://arxiv.org/abs/2503.02824)

| | |
| --- | --- |
| **Parameters** | 86M (ViT-B) |
| **Parameter note** | Each PET and CT encoder is a standard ViT-B; the paper does not print a combined parameter total. |
| **Backbone** | Twin ViT-B encoders for PET and CT with cross-attention decoders |
| **Pre-training** | `MAE`<br>Cross-fraternal twin masked autoencoding with asymmetric PET/CT masking, plus InfoNCE alignment of PET features to radiotracer and demographic text. |
| **Training data** | AutoPET III whole-body PET/CT<br>**1,292** volumes |
| **Downstream tasks** | `segmentation`, `classification`<br>Lesion segmentation and Hodgkin lymphoma staging on GHSG PET/CT. |
| **Modalities** | `PET`, `CT`, `text` |

</details>

<a id="model-ct-fm-202501"></a>
<details>
<summary><b>CT-FM</b> — Vision foundation models for computed tomography <i>(arXiv 202501)</i></summary>

**[Vision foundation models for computed tomography](https://arxiv.org/abs/2501.09001)**

*arXiv* · 202501 · [arXiv:2501.09001](https://arxiv.org/abs/2501.09001)

| | |
| --- | --- |
| **Parameters** | 77.8M |
| **Parameter note** | SegResNet encoder; stated in the GitHub repository and HuggingFace model card. |
| **Backbone** | SegResEncoder |
| **Pre-training** | `SimCLR` |
| **Training data** | IDC corpus<br>**148,000** CT volumes |
| **Downstream tasks** | `segmentation`, `triage`, `retrieval`<br>General-purpose computed-tomography representations. |
| **Modalities** | `CT` |
| **Code** | [github.com/project-lighter/CT-FM](https://github.com/project-lighter/CT-FM) |
| **Weights** | [huggingface.co/project-lighter/ct_fm_feature_extractor](https://huggingface.co/project-lighter/ct_fm_feature_extractor) |
| **PDF name** | `CT-FM - Vision Foundation Models for Computed Tomography.pdf` |

</details>

<a id="model-3dino-202501"></a>
<details>
<summary><b>3DINO</b> — A generalizable 3D framework and model for self-supervised learning in medical imaging <i>(arXiv 202501)</i></summary>

**[A generalizable 3D framework and model for self-supervised learning in medical imaging](https://arxiv.org/abs/2501.11755)**

*arXiv* · 202501 · [arXiv:2501.11755](https://arxiv.org/abs/2501.11755)

| | |
| --- | --- |
| **Parameters** | 307M |
| **Parameter note** | 3DINO-ViT uses a ViT-Large backbone with a 3D ViT-Adapter module for dense downstream tasks. |
| **Backbone** | Vision transformer |
| **Pre-training** | `3DINO`, `self-supervised` |
| **Training data** | **1,300** patients |
| **Downstream tasks** | `classification`, `segmentation`<br>Generalizable three-dimensional self-supervised medical imaging. |
| **Modalities** | `CT`, `MRI` |
| **Code** | [github.com/AICONSlab/3DINO](https://github.com/AICONSlab/3DINO) |

</details>

## MRI & fMRI

Click a model to expand its record. Cross-modality models link to details under CT.

| Date | Model | Venue | Model size | Training data | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 202610 | [A4-MR](#model-a4-mr-202610) | arXiv | _not published_ | 50K MRI studies | vision-language | classification, segmentation, localization |
| 202609 | [nnFoundation](#model-nnfoundation-202609) | arXiv | 102M (CNN) | 2.1M volumes | MAE | segmentation, classification, report generation +2 |
| 202607 | [NeuroVFM](#model-neurovfm-202607) | Nat. Med. | 85.8M | 5.24M volumes | JEPA | classification, report generation, retrieval +2 |
| 202607 | [MARS](#model-mars-202607) | Nat. Biomed. Eng. | _not published_ | 336K volumes | MAE, contrastive learning | classification, segmentation, registration +2 |
| 202605 | [MultitaskCognition](#model-multitaskcognition-202605) | Nat. Aging | _n/a_ | not stated (~3K studies) | supervised, transfer learning | classification, segmentation, regression +1 |
| 202604 | [Curia-2](#model-curia-2-202604) | arXiv | 86M (ViT-B) | none (228M DICOM slices) | DINOv2 | classification, detection, regression |
| 202604 | [NeuroFM](#model-neurofm-202604) | Nat. Biomed. Eng. | _not published_ | none (8.65M fMRI frames) | MAE | regression, classification, prognosis |
| 202603 | [TRIBEv2](#model-tribev2-202603) | arXiv | _not published_ | not stated (multimodal) | Multimodal representation learning | regression |
| 202602 | [CMR Transformer](#model-cmr-transformer-202602) | Nat. Biomed. Eng. | _not published_ | none (~21K scan–text pairs) | InfoNCE, contrastive | regression, classification |
| 202602 | [BrainIAC](#model-brainiac-202602) | Nat. Neurosci. | 88.4M | 32K scans | SimCLR | classification, regression, segmentation +1 |
| 202602 | [PRIMA](#model-prima-202602) | Nat. Biomed. Eng. | 56.6M (vis. enc.) | none (221K study–report pairs) | CLIP | classification, triage, regression |
| 202601 | [deepmriprep](#model-deepmriprep-202601) | Nat. Comput. Sci. | _n/a_ | not stated (685 MRI scans) | _n/a_ | preprocessing |
| 202601 | [FOMO25](#model-fomo25-202601) | arXiv | _not published_ | 176K volumes | MAE | segmentation, classification, regression |
| 202512 | [AnyMC3D](#model-anymc3d-202512) | arXiv | _n/a_ | none (frozen DINOv2/3) | DINOv2, DINOv3 | classification |
| 202511 | [Pillar-0](#model-pillar-0-202511) | arXiv | 79M (Atlas enc.) | none (~155K volume–report pairs) | contrastive, vision-language | classification, prognosis |
| 202510 | [BrainFound](#model-brainfound-202510) | arXiv | 307M (ViT-L) | 10K volumes | DINOv2 | classification |
| 202509 | [MRI-PTPCa](#model-mri-ptpca-202509) | Nat. Cancer | _not published_ | none (1.3M image–pathology pairs) | BYOL | classification, grading |
| 202508 | [RadFM](#model-radfm-202508) | Nat. Commun. | 14B | none (16M 2D/3D image–text) | vision-language | classification, VQA, report generation |
| 202508 | [Curia](#model-curia-202508) | arXiv | 86M | none (228M DICOM slices) | DINOv2 | General-purpose multimodal radiology representation learning |
| 202504 | [Spark3D](#model-spark3d-202504) | CVPR 2025 | _not published_ | 44K MRI volumes | MAE | segmentation |
| 202501 | [3DINO](#model-3dino-202501) | arXiv | 307M (ViT-L) | ~100K volumes | 3DINO, self-supervised | classification, segmentation |
| 202412 | [BME-X](#model-bme-x-202412) | Nat. Biomed. Eng. | _not published_ | not stated (516 participants) | supervised | segmentation, registration, classification |

<a id="model-a4-mr-202610"></a>
<details>
<summary><b>A4-MR</b> — Abnormality-aware anatomical alignment for MR <i>(arXiv 202610)</i></summary>

**[A4-MR: Abnormality-aware Anatomical Alignment for MR](https://arxiv.org/abs/2610.13056)**

*arXiv* · 202610 · [arXiv:2610.13056](https://arxiv.org/abs/2610.13056)

| | |
| --- | --- |
| **Backbone** | 3D vision-language MRI encoder |
| **Pre-training** | `vision-language`<br>Anatomy-level image–text alignment with noisy localization labels and distinct representations of healthy versus abnormal anatomy. |
| **Training data** | Multi-anatomy MRI, about half paired with radiology reports<br>**50,000** studies · **491,000** series |
| **Downstream tasks** | `classification`, `segmentation`, `localization`<br>Abnormality detection, frozen-encoder knee and abdominal organ segmentation, and 3D anatomy localization. |
| **Modalities** | `MRI`, `text` |

</details>

<a id="model-mars-202607"></a>
<details>
<summary><b>MARS</b> — Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications <i>(Nat. Biomed. Eng. 202607)</i></summary>

**[Large-scale multi-sequence pretraining for generalizable MRI analysis in versatile clinical applications](https://www.nature.com/articles/s41551-026-01740-5)**

*Nat. Biomed. Eng.* · 202607 · [doi:10.1038/s41551-026-01740-5](https://doi.org/10.1038/s41551-026-01740-5)

| | |
| --- | --- |
| **Backbone** | 3D Swin Transformer |
| **Pre-training** | `MAE`, `contrastive learning` |
| **Training data** | Multi-sequence MRI<br>**336,000** volumes |
| **Downstream tasks** | `classification`, `segmentation`, `registration`, `report generation`, `prognosis`<br>Evaluated across 44 clinical tasks. |
| **Modalities** | `MRI` |
| **Code** | [github.com/zqiuak/MARS](https://github.com/zqiuak/MARS) |

</details>

<a id="model-multitaskcognition-202605"></a>
<details>
<summary><b>MultitaskCognition</b> — Predicting categorical and continuous Alzheimer’s disease outcomes from a single MRI scan <i>(Nat. Aging 202605)</i></summary>

**[Predicting categorical and continuous Alzheimer’s disease outcomes from a single MRI scan](https://doi.org/10.1038/s43587-026-01121-2)**

*Nat. Aging* · 202605 · [doi:10.1038/s43587-026-01121-2](https://doi.org/10.1038/s43587-026-01121-2)

| | |
| --- | --- |
| **Backbone** | 3D U-Net, ResNet-50 and XGBoost |
| **Pre-training** | `supervised`, `transfer learning` |
| **Training data** | Approximately<br>**3,000** MRI studies |
| **Downstream tasks** | `classification`, `segmentation`, `regression`, `prognosis`<br>Alzheimer’s disease outcomes from a single MRI scan. |
| **Modalities** | `MRI` |
| **Code** | [github.com/darenma/MultitaskCognition](https://github.com/darenma/MultitaskCognition) |

</details>

<a id="model-neurofm-202604"></a>
<details>
<summary><b>NeuroFM</b> — Towards a general-purpose foundation model for functional MRI analysis <i>(Nat. Biomed. Eng. 202604)</i></summary>

**[Towards a general-purpose foundation model for functional MRI analysis](https://www.nature.com/articles/s41551-026-01666-y)**

*Nat. Biomed. Eng.* · 202604 · [doi:10.1038/s41551-026-01666-y](https://doi.org/10.1038/s41551-026-01666-y)

| | |
| --- | --- |
| **Backbone** | Spatiotemporal waveform Mamba |
| **Pre-training** | `MAE` |
| **Training data** | More than<br>**50,000** subjects and **8,650,000** fMRI frames |
| **Downstream tasks** | `regression`, `classification`, `prognosis`<br>General-purpose functional MRI analysis. |
| **Modalities** | `fMRI` |
| **Code** | [github.com/CUHK-AIM-Group/NeuroSTORM](https://github.com/CUHK-AIM-Group/NeuroSTORM) |

</details>

<a id="model-tribev2-202603"></a>
<details>
<summary><b>TRIBEv2</b> — A foundation model of vision, audition, and language for in-silico neuroscience <i>(arXiv 202603)</i></summary>

**[A foundation model of vision, audition, and language for in-silico neuroscience](https://ai.meta.com/research/publications/a-foundation-model-of-vision-audition-and-language-for-in-silico-neuroscience/)**

*arXiv* · 202603

| | |
| --- | --- |
| **Backbone** | V-JEPA 2, wav2vec and Llama |
| **Pre-training** | Multimodal representation learning |
| **Training data** | Multiple datasets; numeric scale not recorded |
| **Downstream tasks** | `regression`<br>Maps vision, audio and language stimuli to predicted brain voxels. |
| **Modalities** | `fMRI`, `vision`, `audio`, `text` |
| **Code** | [github.com/facebookresearch/tribev2](https://github.com/facebookresearch/tribev2) |

</details>

<a id="model-cmr-transformer-202602"></a>
<details>
<summary><b>CMR Transformer</b> — A generalizable deep learning system for cardiac MRI <i>(Nat. Biomed. Eng. 202602)</i></summary>

**[A generalizable deep learning system for cardiac MRI](https://www.nature.com/articles/s41551-026-01637-3)**

*Nat. Biomed. Eng.* · 202602 · [doi:10.1038/s41551-026-01637-3](https://doi.org/10.1038/s41551-026-01637-3)

| | |
| --- | --- |
| **Backbone** | Multiscale vision transformer and BERT text encoder |
| **Pre-training** | `InfoNCE`, `contrastive`<br>Image-report contrastive learning. |
| **Training data** | Cardiac MRI with paired reports Approximately<br>**21,000** scans |
| **Downstream tasks** | `regression`, `classification`<br>Left-ventricular ejection fraction and 39 cardiovascular conditions. |
| **Modalities** | `MRI`, `text` |
| **Code** | [github.com/rohanshad/cmr_transformer](https://github.com/rohanshad/cmr_transformer) |

</details>

<a id="model-brainiac-202602"></a>
<details>
<summary><b>BrainIAC</b> — A generalizable foundation model for analysis of human brain MRI <i>(Nat. Neurosci. 202602)</i></summary>

**[A generalizable foundation model for analysis of human brain MRI](https://www.nature.com/articles/s41593-026-02202-6)**

*Nat. Neurosci.* · 202602 · [doi:10.1038/s41593-026-02202-6](https://doi.org/10.1038/s41593-026-02202-6)

| | |
| --- | --- |
| **Parameters** | 88.4M |
| **Parameter note** | MONAI ViT-B/16³ (96×96×96 input, 16³ patches); figure from the released checkpoint configuration. |
| **Backbone** | ViT-B |
| **Pre-training** | `SimCLR` |
| **Training data** | **32,000** MRI scans |
| **Downstream tasks** | `classification`, `regression`, `segmentation`, `prognosis`<br>Generalizable analysis of brain MRI. |
| **Modalities** | `MRI` |
| **Code** | [github.com/AIM-KannLab/BrainIAC](https://github.com/AIM-KannLab/BrainIAC) |

</details>

<a id="model-prima-202602"></a>
<details>
<summary><b>PRIMA</b> — Learning neuroimaging models from health system-scale data <i>(Nat. Biomed. Eng. 202602)</i></summary>

**[Learning neuroimaging models from health system-scale data](https://www.nature.com/articles/s41551-025-01608-0)**

*Nat. Biomed. Eng.* · 202602 · [doi:10.1038/s41551-025-01608-0](https://doi.org/10.1038/s41551-025-01608-0)

| | |
| --- | --- |
| **Parameters** | 56.6M |
| **Parameter note** | 56.584M is the combined sequence and study hierarchical ViT visual encoder; the VQ-VAE volume tokenizer and text tower are excluded. |
| **Backbone** | Hierarchical vision transformer |
| **Pre-training** | `CLIP` |
| **Training data** | **221,000** MRI studies · **5,600,000** sequences |
| **Downstream tasks** | `classification`, `triage`, `regression`<br>Prediction of 52 radiologic diagnoses. |
| **Modalities** | `MRI`, `text` |

</details>

<a id="model-deepmriprep-202601"></a>
<details>
<summary><b>deepmriprep</b> — deepmriprep: voxel-based morphometry preprocessing via deep neural networks <i>(Nat. Comput. Sci. 202601)</i></summary>

**[deepmriprep: voxel-based morphometry preprocessing via deep neural networks](https://www.nature.com/articles/s43588-026-00953-7)**

*Nat. Comput. Sci.* · 202601 · [doi:10.1038/s43588-026-00953-7](https://doi.org/10.1038/s43588-026-00953-7)

| | |
| --- | --- |
| **Backbone** | 3D U-Net |
| **Pre-training** | `_n/a_`<br>Supervised voxel-based morphometry preprocessing; the paper does not introduce a foundation-model pre-training objective. |
| **Training data** | **685** MRI scans |
| **Downstream tasks** | `preprocessing`<br>Deep-learning voxel-based morphometry preprocessing. |
| **Modalities** | `MRI` |
| **Code** | [github.com/wwu-mmll/deepmriprep-train](https://github.com/wwu-mmll/deepmriprep-train) |

</details>

<a id="model-fomo25-202601"></a>
<details>
<summary><b>FOMO25</b> — From 100,000+ images to winning the first brain MRI foundation model challenges: sharing lessons and models <i>(arXiv 202601)</i></summary>

**[From 100,000+ images to winning the first brain MRI foundation model challenges: sharing lessons and models](https://arxiv.org/abs/2601.13166)**

*arXiv* · 202601 · [arXiv:2601.13166](https://arxiv.org/abs/2601.13166)

| | |
| --- | --- |
| **Backbone** | CNN U-Net |
| **Pre-training** | `MAE` |
| **Training data** | **115,000 + 61,000** MRI volumes |
| **Downstream tasks** | `segmentation`, `classification`, `regression`<br>SSL3D and FOMO25 challenge tasks. |
| **Modalities** | `MRI` |
| **Code** | [github.com/jbanusco/BrainFM4Challenges](https://github.com/jbanusco/BrainFM4Challenges) |

</details>

<a id="model-brainfound-202510"></a>
<details>
<summary><b>BrainFound</b> — Towards generalisable foundation models for brain MRI <i>(arXiv 202510)</i></summary>

**[Towards generalisable foundation models for brain MRI](https://arxiv.org/abs/2510.23415)**

*arXiv* · 202510 · [arXiv:2510.23415](https://arxiv.org/abs/2510.23415)

| | |
| --- | --- |
| **Parameters** | 307M |
| **Parameter note** | ViT-Large/14 DINOv2 backbone; each axial slice is processed independently at 224×224. |
| **Backbone** | ViT-L |
| **Pre-training** | `DINOv2` |
| **Training data** | **10,000** MRI volumes |
| **Downstream tasks** | `classification`<br>Neurodegeneration classification and tumour grading. |
| **Modalities** | `MRI` |
| **Code** | [github.com/Moona-Mazher/BrainFound](https://github.com/Moona-Mazher/BrainFound) |

</details>

<a id="model-mri-ptpca-202509"></a>
<details>
<summary><b>MRI-PTPCa</b> — An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer <i>(Nat. Cancer 202509)</i></summary>

**[An MRI–pathology foundation model for noninvasive diagnosis and grading of prostate cancer](https://www.nature.com/articles/s43018-025-01041-x)**

*Nat. Cancer* · 202509 · [doi:10.1038/s43018-025-01041-x](https://doi.org/10.1038/s43018-025-01041-x)

| | |
| --- | --- |
| **Backbone** | CNN and vision transformer |
| **Pre-training** | `BYOL` |
| **Training data** | Nearly **1,300,000** image–pathology pairs from more than **5,500** patients |
| **Downstream tasks** | `classification`, `grading`<br>Non-invasive prostate-cancer diagnosis and grading. |
| **Modalities** | `MRI`, `histopathology` |
| **Code** | [github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer](https://github.com/StandWisdom/MRI-based-Predicted-Transformer-for-Prostate-cancer) |

</details>

<a id="model-spark3d-202504"></a>
<details>
<summary><b>Spark3D</b> — Revisiting MAE pre-training for 3D medical image segmentation <i>(CVPR 2025 202504)</i></summary>

**[Revisiting MAE pre-training for 3D medical image segmentation](https://doi.org/10.1109/CVPR52734.2025.00489)**

*CVPR 2025* · 202504 · [doi:10.1109/CVPR52734.2025.00489](https://doi.org/10.1109/CVPR52734.2025.00489)

| | |
| --- | --- |
| **Backbone** | CNN U-Net |
| **Pre-training** | `MAE` |
| **Training data** | **44,000** MRI volumes from **9,000** patients |
| **Downstream tasks** | `segmentation`<br>Masked-autoencoder pretraining for three-dimensional medical segmentation. |
| **Modalities** | `MRI` |
| **Code** | [github.com/MIC-DKFZ/nnssl](https://github.com/MIC-DKFZ/nnssl) |

</details>

<a id="model-bme-x-202412"></a>
<details>
<summary><b>BME-X</b> — A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks <i>(Nat. Biomed. Eng. 202412)</i></summary>

**[A foundation model for enhancing magnetic resonance images and downstream segmentation, registration and diagnostic tasks](https://www.nature.com/articles/s41551-024-01283-7)**

*Nat. Biomed. Eng.* · 202412 · [doi:10.1038/s41551-024-01283-7](https://doi.org/10.1038/s41551-024-01283-7)

| | |
| --- | --- |
| **Backbone** | U-Net CNN |
| **Pre-training** | `supervised`<br>Tissue-classification then tissue-aware enhancement; not a self-supervised encoder. |
| **Training data** | 52 foetal participants and 464 Baby Connectome Project participants (0–6 years)<br>**516** participants |
| **Downstream tasks** | `segmentation`, `registration`, `classification`<br>MRI enhancement and downstream image-analysis tasks. |
| **Modalities** | `MRI` |
| **Code** | [github.com/DBC-Lab/Brain_MRI_Enhancement](https://github.com/DBC-Lab/Brain_MRI_Enhancement) |

</details>

## X-Ray

Click a model to expand its record. Cross-modality models link to details under CT.

| Date | Model | Venue | Model size | Training data | Pre-training | Downstream tasks |
| --- | --- | --- | --- | --- | --- | --- |
| 202607 | [CLEAR](#model-clear-202607) | Nat. Biomed. Eng. | 86M (ViT-B) | none (0.87M image–report pairs) | contrastive, vision-language | classification |
| 202605 | [MultiMedVision](#model-multimedvision-202605) | arXiv | _not published_ | none (CXR + CT-RATE) | self-supervised | classification |
| 202602 | [CheXficient](#model-chexficient-202602) | arXiv | _not published_ | none (22.7% of 1.24M CXR–report pairs) | CLIP | classification, retrieval, segmentation +1 |
| 202601 | [AFLoc](#model-afloc-202601) | Nat. Biomed. Eng. | _not published_ | none (MIMIC-CXR image–text) | CLIP | localization, classification |
| 202508 | [RadFM](#model-radfm-202508) | Nat. Commun. | 14B | none (16M 2D/3D image–text) | vision-language | classification, VQA, report generation |

<a id="model-clear-202607"></a>
<details>
<summary><b>CLEAR</b> — An auditable foundation model for radiology grounded in clinical concepts <i>(Nat. Biomed. Eng. 202607)</i></summary>

**[CLEAR: an auditable foundation model for radiology grounded in clinical concepts](https://www.nature.com/articles/s41551-026-01741-4)**

*Nat. Biomed. Eng.* · 202607 · [doi:10.1038/s41551-026-01741-4](https://doi.org/10.1038/s41551-026-01741-4)

| | |
| --- | --- |
| **Parameters** | 86M (ViT-B) |
| **Parameter note** | 86M is the DINOv2 ViT-B/14 image encoder. The 12-layer GPT-2-style text encoder and LLM concept embeddings are separate. |
| **Backbone** | DINOv2 ViT-B/14 image encoder and GPT-2-style text encoder |
| **Pre-training** | `contrastive`, `vision-language`<br>Task-agnostic contrastive pretraining; concept scores are projected through LLM embeddings of 368,294 radiological observations. |
| **Training data** | MIMIC-CXR, CheXpert-Plus and ReXGradient chest X-ray–report pairs<br>**873,342** pairs · **239,391** patients |
| **Downstream tasks** | `classification`<br>Auditable zero-shot and linearly probed CXR finding classification, plus concept-bottleneck models. |
| **Modalities** | `X-ray`, `text` |
| **Code** | [github.com/peterhan91/CLEAR](https://github.com/peterhan91/CLEAR) |
| **Weights** | [huggingface.co/peterhan91/CLEAR](https://huggingface.co/peterhan91/CLEAR) |

</details>

<a id="model-chexficient-202602"></a>
<details>
<summary><b>CheXficient</b> — A data- and compute-efficient chest X-ray foundation model beyond aggressive scaling <i>(arXiv 202602)</i></summary>

**[A data- and compute-efficient chest X-ray foundation model beyond aggressive scaling](https://arxiv.org/abs/2602.22843)**

*arXiv* · 202602 · [arXiv:2602.22843](https://arxiv.org/abs/2602.22843)

| | |
| --- | --- |
| **Backbone** | Chest X-ray vision-language encoder |
| **Pre-training** | `CLIP`<br>Active data curation during CLIP-style pretraining; trained on 22.7% of the 1,235,004-pair corpus. |
| **Training data** | Paired chest X-rays and reports<br>22.7% of **1,235,004** pairs |
| **Downstream tasks** | `classification`, `retrieval`, `segmentation`, `report generation`<br>Zero-shot findings classification, cross-modal retrieval, disease prediction, semantic segmentation and radiology report generation. |
| **Modalities** | `X-ray`, `text` |
| **Code** | [github.com/cwangrun/CheXficient](https://github.com/cwangrun/CheXficient) |

</details>

<a id="model-afloc-202601"></a>
<details>
<summary><b>AFLoc</b> — A multimodal vision–language model for generalizable annotation-free pathology localization <i>(Nat. Biomed. Eng. 202601)</i></summary>

**[A multimodal vision–language model for generalizable annotation-free pathology localization](https://www.nature.com/articles/s41551-025-01574-7)**

*Nat. Biomed. Eng.* · 202601 · [doi:10.1038/s41551-025-01574-7](https://doi.org/10.1038/s41551-025-01574-7)

| | |
| --- | --- |
| **Backbone** | ResNet and BioClinicalBERT |
| **Pre-training** | `CLIP` |
| **Training data** | MIMIC-CXR |
| **Downstream tasks** | `localization`, `classification`<br>Annotation-free pathology localization. |
| **Modalities** | `X-ray`, `text` |
| **Code** | [github.com/YH0517/AFLoc](https://github.com/YH0517/AFLoc) |
| **Dataset** | [physionet.org/content/mimic-cxr](https://physionet.org/content/mimic-cxr/) |

</details>

