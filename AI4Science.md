<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from pipeline/ai4science/data.json by pipeline/generate.py -->
<!-- Edits made here are overwritten by the next run of the generator. -->

# AI for Science

Scientific discovery, research assistance, chemistry and drug design.

**Maintainer:** [Ryan Khalloqi](https://github.com/ryanwangk)

**28 entries** across 3 categories · [Back to index](README.md)

## Catalogue

### Drug & Molecule Design

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202610 | [EquiformerV2 (with coordinate-denoising auxiliary task), benchmarked against SchNet, DimeNet++, EGNN, PaiNN, Ponita, TFN, eSCN and T5Chem; XGBoost active-learning oracle](#model-active-geometric-chemical-reaction-prediction-202610) | Nat. Comput. Sci. | Not stated as a single number — the study benchmarks ten GNN architectures (SchNet, DimeNet++, EGNN, PaiNN, Ponita Point Cloud/Fiber, TFN, eSCN, EquiformerV2) plus XGBoost/CatBoost/Random Forest oracles; no parameter counts are reported for any. | ✓ | Active-learning-guided GNNs correctly predict borylation site for all 10 novel test substrates |
| 202610 | [Pinal](#model-pinal-202610) | Nature | 16 billion (T2struct scaled up to 15.5B parameters + SaProt-T sequence designer) | ✓ | 16B-parameter Pinal designs proteins from text prompts; H-protein design beats native E. coli enzyme 1.7-fold |
| 202610 | [RFdiffusion3 (RFD3)](#model-rfdiffusion3-202610) | Science | 168M trainable parameters (final network) | ✓ | 168M-parameter all-atom diffusion model designs functional enzymes and DNA binders, 10x faster than RFdiffusion2 |
| 202609 | [MutexaGPT](#model-mutexagpt-202609) | Nat. Comput. Sci. | not stated (multi-agent LLM orchestration platform, base LLM undisclosed) | — | LLM multi-agent platform (MutexaGPT) automates physics-based enzyme design, validated experimentally on two enzymes |
| 202609 | [CARPNN (chimaeric antigen receptor-protein-mpNN)](#model-carpnn-de-novo-car-binders-202609) | Nat. Biomed. Eng. | N/A — not a single neural network; a pipeline combining several pretrained models (RFdiffusion, BindCraft/AlphaFold2-hallucination, ProteinMPNN/SolubleMPNN, Boltz-2, AlphaFold2-multimer); no new model parameter count is reported | ✓ | 1,758 AI-designed CAR-T binders screened; evolved BCMA binder achieves near-complete tumour control in mice |
| 202609 | [SynCraft](#model-syncraft-202609) | Nat. Mach. Intell. | N/A — not a trained neural net; uses the pretrained Gemini-2.5-Pro LLM via API with retrieval-augmented few-shot prompting, no fine-tuning or disclosed parameter count | ✓ | LLM-guided molecular edits raise synthesizable-analog success rate to ~45% vs ~30-38% for prior methods |
| 202608 | [MAP (mechanism-aware perturbation response predictor)](#model-map-knowledge-driven-perturbation-202608) | Nat. Mach. Intell. | not stated as a single total parameter count (uses frozen ESM-2 and MoleculeSTM encoders + trainable adapter MLPs + 4-layer transformer + STATE SE-600M foundation model) | — | MAP predicts single-cell drug responses zero-shot, improving DEG correlation up to +12.3% over baselines |
| 202608 | [Dyna-1](#model-dyna-1-202608) | Nature | not stated (fine-tuned on top of frozen ESM-3 embeddings; full ESM-3 model size not specified in preprint) | ✓ | Dyna-1 predicts millisecond protein motions from missing NMR peaks, reaching AUROC 0.92 on BPTI dynamics |
| 202606 | [LASErMPNN](#model-lasermpnn-202606) | Nature | not stated (GNN) | ✓ | 5x hit rate, 70x affinity vs. prior SOTA; zero-shot design reached Kd = 1.2 nM |
| 202604 | [DeepDrugDiscovery](#model-deepdrugdiscovery-202604) | Nat. Biomed. Eng. | not stated (VAE+GRU) | ✓ | 2 lead BBB-permeable, mTOR-independent autophagy enhancers; restored memory in AD mouse models |
| 202603 | [AI-guided LNP design (unnamed in paper)](#model-lnp-spatial-ai-202603) | Nat. Biomed. Eng. | N/A — non-neural (SISSO symbolic regression) | — | Lead lipid P1: 14.8x mRNA delivery efficiency vs. clinical-standard ALC-0315 |
| 202412 | [RetroChimera](#model-retrochimera-202412) | Nature | Ensemble of two models; on the Pistachio dataset NeuralLoc has 165M parameters and R-SMILES 2 has 66.7M parameters (on USPTO-50K: 1.9M and 17.4M respectively) | ✓ | Ensembled retrosynthesis model preferred by chemists over reference reactions ~64% of the time |

<a id="model-active-geometric-chemical-reaction-prediction-202610"></a>
<details>
<summary><b>EquiformerV2 (with coordinate-denoising auxiliary task), benchmarked against SchNet, DimeNet++, EGNN, PaiNN, Ponita, TFN, eSCN and T5Chem; XGBoost active-learning oracle</b> — Advancing chemical reaction prediction in data-scarce drug discovery with active and geometric deep learning <i>(Nat. Comput. Sci. 202610)</i></summary>

**[Advancing chemical reaction prediction in data-scarce drug discovery with active and geometric deep learning](https://doi.org/10.1038/s43588-026-01063-0)**

*Nat. Comput. Sci.* · 202610 · [Mason Minot](https://orcid.org/0000-0003-0225-9107) & [Gisbert Schneider](https://orcid.org/0000-0001-6706-1084) · [doi:10.1038/s43588-026-01063-0](https://doi.org/10.1038/s43588-026-01063-0)

| | |
| --- | --- |
| **Parameters** | Not stated as a single number — the study benchmarks ten GNN architectures (SchNet, DimeNet++, EGNN, PaiNN, Ponita Point Cloud/Fiber, TFN, eSCN, EquiformerV2) plus XGBoost/CatBoost/Random Forest oracles; no parameter counts are reported for any. |
| **Backbone** | Tree-based ensemble (XGBoost/CatBoost/Random Forest on 512-bit ECFP4 fingerprints) used as active-learning oracle; geometric GNNs (invariant: SchNet, DimeNet++, invariant-EGNN; equivariant: PaiNN, Ponita, TFN, eSCN, EquiformerV2) augmented with coordinate-denoising and node-masking self-supervised auxiliary heads plus a reaction-condition mixer and two-layer MLP output head, operating on 3D RDKit-generated conformers. |
| **Pre-training** | `self-supervised` `coordinate-denoising` `node-masking` `online-auxiliary-tasks`<br>No offline pretraining on external corpora; instead, online self-supervised auxiliary objectives (coordinate denoising via Gaussian noise on xyz atom positions, sigma=0.03, and node masking/atom-type prediction) are applied jointly with the supervised task directly on the same labeled reaction data during training. |
| **Training data** | Data were generated through a three-round active-learning experimental campaign for C–H borylation, starting from an initial dataset of 626 regioselectivity and 2,044 HTE (yield/binary) data points across 518 substrates, with substrates for active learning drawn from a pool of 22,253 candidates filtered for known, purchasable, QC-verified compounds.<br>**Final dataset after 3 active-learning rounds: 812 substrates (incl. 106 negatives) and 920 borylated species for regioselectivity, plus 6,865 HTE data points across 568 substrates for yield/binary classification.** |
| **Downstream tasks** | `reaction-outcome-prediction` `regioselectivity-prediction` `active-learning` `yield-prediction` `late-stage-functionalization`<br>Binary reaction feasibility classification, regioselectivity (site-of-borylation) prediction, and yield prediction for C–H borylation (and a secondary Minisci C–H alkylation benchmark), with prospective experimental validation on ten previously unreported substrates. |
| **Modalities** | `molecular graphs`, `3D molecular conformers`, `chemical reaction conditions`, `ECFP/Morgan fingerprints` |
| **Code** | [github.com/minotm/active-drug-discovery](https://github.com/minotm/active-drug-discovery) |
| **Weights** | [doi.org/10.5281/zenodo.20783136](https://doi.org/10.5281/zenodo.20783136) |
| **License** | GNU GPLv3 |
| **Note** | This is primarily a methodology/benchmarking paper (active-learning oracle + benchmark of ten GNN architectures) rather than a single named model; no single parameter count or architecture is reported as 'the' model. |

**Key results**

- Active learning expanded the C–H borylation dataset from an initial 626 regioselectivity/2,044 HTE data points (518 substrates) to 812 substrates (106 negatives, 920 borylated species) and 6,865 HTE data points across 568 substrates over three rounds.
- On the Random split, T5Chem achieved 0.73±0.03 MCC versus 0.79±0.05 for PaiNN for condition-aware reaction outcome prediction; on the harder Scaffold and Butina splits T5Chem dropped to 0.38±0.08 and 0.36±0.08 while Ponita Fiber reached 0.59±0.05 and 0.47±0.1.
- Self-supervised coordinate-denoising and node-masking auxiliary tasks provided a consistent performance benefit across GNN architectures, especially on the challenging Scaffold split.
- Prospective validation with EquiformerV2 (plus coordinate denoising) on ten unreported borylation substrates: the most probable predicted borylation site matched the experimentally observed site for all ten substrates, including challenging N-heteroaryl and symmetric cases.

</details>

<a id="model-pinal-202610"></a>
<details>
<summary><b>Pinal</b> — Programmable design of functional proteins from natural language <i>(Nature 202610)</i></summary>

**[Programmable design of functional proteins from natural language](https://www.nature.com/articles/s41586-026-11205-z)**

*Nature* · 202610 · Fengyuan Dai & [Fajie Yuan](https://scholar.google.com/citations?user=yOiBwasAAAAJ&hl=en) · [doi:10.1038/s41586-026-11205-z](https://doi.org/10.1038/s41586-026-11205-z)

| | |
| --- | --- |
| **Parameters** | 16 billion (T2struct scaled up to 15.5B parameters + SaProt-T sequence designer) |
| **Backbone** | Two-stage encoder-decoder pipeline: T2struct (text-to-structure) uses a pre-trained T5 encoder plus a GPT-2-style decoder trained from scratch, linked via a text-3Di cross-attention module, autoregressively generating Foldseek 3Di structure tokens; SaProt-T (structure+text-to-sequence) is adapted from SaProt with text encoded by PubMedBERT and prepended to 3Di token embeddings, trained with a masked language modeling objective. |
| **Pre-training** | `synthetic data generation` `masked language modeling` `autoregressive` `LLM-generated annotations`<br>Trained on a synthetic corpus of 1.7 billion protein-text pairs built from UniProt/TrEMBL and Swiss-Prot entries annotated via the ProTrek multimodal protein language model and consolidated/paraphrased with LLMs, plus ~800 million keyword-protein pairs from InterPro; structures sourced from the AlphaFold Protein Structure Database (AFDB). |
| **Training data** | 1.7 billion synthetically annotated protein-text pairs spanning 135 million unique protein sequences and structures, encompassing over 100 billion word tokens; human-curated Swiss-Prot (545K proteins, 27M pairs) used for validation/ablation comparisons.<br>**1.7 billion protein-text pairs** |
| **Downstream tasks** | `de novo protein design` `enzyme engineering` `fluorescent protein design` `plastic-degrading enzyme design` `metabolic pathway engineering`<br>Natural-language-prompted generation and experimental validation of a GFP-like fluorescent protein, a PETase, an alcohol dehydrogenase, and a metabolic H-protein incorporated into a multi-enzyme CO2-fixation pathway. |
| **Modalities** | `protein sequence`, `protein structure (3Di tokens)`, `natural language text` |
| **Code** | [huggingface.co/westlake-repl/Pinal](https://huggingface.co/westlake-repl/Pinal) |
| **Weights** | [huggingface.co/westlake-repl/Pinal](https://huggingface.co/westlake-repl/Pinal) |
| **Note** | Original Nature article page was not directly accessible (paywall/fetch error); entry is based on the complete bioRxiv preprint (v9, 10.1101/2024.08.01.606258), which text matches the Nature abstract and appears to be the accepted version. License for the Hugging Face weights is not stated in the fetched text. |

**Key results**

- Pinal achieved a mean keyword recovery rate of 77% versus approximately 12% for ESM3 in a keyword-conditioned generation comparison.
- 17 of 20 (85%) structurally novel Pinal designs (TM-score < 0.5 to known PDB structures) were successfully expressed in soluble form in E. coli.
- Pinal-designed H-protein (pinalH02) drove glycine synthesis to a final titer of 11.1 mM, a 1.7-fold increase over the native E. coli H-protein.
- 14 of 20 (70%) H-protein candidates showed soluble expression, with 5 active in a reconstituted CO2-fixation assay.
- In an independent benchmark, Pinal achieved the best performance on 11 of 14 metrics for sequence plausibility, structural foldability, and language alignment.

</details>

<a id="model-rfdiffusion3-202610"></a>
<details>
<summary><b>RFdiffusion3 (RFD3)</b> — Atomic functional site scaffolding in biopolymers with RFdiffusion3 <i>(Science 202610)</i></summary>

**[Atomic functional site scaffolding in biopolymers with RFdiffusion3](https://doi.org/10.1126/science.aeh2982)**

*Science* · 202610 · Jasper Butcher & David Baker · [doi:10.1126/science.aeh2982](https://doi.org/10.1126/science.aeh2982)

| | |
| --- | --- |
| **Parameters** | 168M trainable parameters (final network) |
| **Backbone** | Transformer-based U-Net with atom-level diffusion: a downsampling module encoding atomic/residue features, a sparse transformer token module (Pairformer shrunk from 48 to 2 layers relative to AlphaFold3), and an upsampling module predicting coordinate updates; uses sparse cross-attention for atom\u2194token pooling instead of triangle attention/multiplication. |
| **Pre-training** | `diffusion` `self-supervised` `structure-denoising`<br>Hierarchical training: the network is pre-trained on a mix of AlphaFold2 distillation structures and deposited PDB structures, then fine-tuned on a larger fraction of DNA- and protein-protein-interaction examples, using structures by denoising native structures to varying noise levels and predicting backbone/side-chain atom positions conditioned on partial constraints. |
| **Training data** | All protein-protein, protein-small-molecule and protein-DNA complexes in the Protein Data Bank deposited through December 2024, plus a set of high-quality AlphaFold2 distillation structures, each annotated with potential design conditioning features (hydrogen bonds, binding partners, functional motifs).<br>**PDB entries through December 2024 + AF2 distillation structure set** |
| **Downstream tasks** | `protein-binder-design` `enzyme-design` `DNA-binding-protein-design` `small-molecule-binder-design` `RNA-structure-design`<br>Used for unconditional protein backbone generation, protein-protein binder design, protein-DNA and protein-small-molecule interface design, atomic active-site/enzyme scaffolding, and RNA structure design, with experimental validation of designed DNA-binding proteins and enzymes (plus, per the Science abstract, de novo phosphotriesterases and transthyretin-specific zinc proteases not covered in the bioRxiv preprint text obtained). |
| **Modalities** | `protein structure`, `small molecule`, `DNA`, `RNA` |
| **Code** | [github.com/RosettaCommons/foundry](https://github.com/RosettaCommons/foundry) |
| **Note** | Full Science text is paywalled; entry is based on the open bioRxiv preprint (2025.09.18.676967v2, same model/architecture) plus the Science abstract and a EurekAlert press release for the published version's phosphotriesterase/transthyretin-protease experiments, which go beyond what the fetched preprint describes. |

**Key results**

- Final network has 168M trainable parameters vs ~350M for AlphaFold3
- RFD3 is roughly an order of magnitude (~10x) faster than RFdiffusion2 for typical protein lengths
- 98% of unconditional designs (length 100-200) had at least one of 8 ProteinMPNN sequences predicted by AF3 to fold within 1.5 \u00c5 RMSD
- For protein-binder design across 5 targets, RFD3 found on average 8.2 unique successful clusters vs 1.4 for RFdiffusion1
- On the Atomic Motif Enzyme benchmark, RFD3 outperformed RFdiffusion2 on 37/41 (90%) cases, and on cases with >4 residue islands achieved 15% vs 4% passing designs
- Designed DNA-binding protein validated by yeast display bound with EC50 = 5.89 \u00b1 2.15 \u00c5\u03bcM
- Designed cysteine-hydrolase esterase achieved Kcat/Km = 3557 from 190 screened designs (35 multi-turnover hits)
- Per the Science abstract (not in the fetched preprint text): de novo phosphotriesterases with a carbamylated-lysine dual-metal active site and transthyretin-specific zinc proteases were obtained as active catalysts from zero-shot 96-construct design campaigns

</details>

<a id="model-mutexagpt-202609"></a>
<details>
<summary><b>MutexaGPT</b> — MutexaGPT: an intuition-to-design translator for physics-based enzyme engineering <i>(Nat. Comput. Sci. 202609)</i></summary>

**[MutexaGPT: an intuition-to-design translator for physics-based enzyme engineering](https://www.nature.com/articles/s43588-026-01049-y)**

*Nat. Comput. Sci.* · 202609 · Zhongyue J. Yang · [doi:10.1038/s43588-026-01049-y](https://doi.org/10.1038/s43588-026-01049-y)

| | |
| --- | --- |
| **Parameters** | not stated (multi-agent LLM orchestration platform, base LLM undisclosed) |
| **Backbone** | Multi-agent large language model system that elicits missing information via dialogue, constructs physics-based enzyme models, and configures/executes high-throughput molecular dynamics (Mutexa) workflows |
| **Pre-training** | `LLM-agents` `no-custom-pretraining`<br>Built on existing large language model agents (base LLM not disclosed in the accessible text) orchestrated to elicit user intuition, build physics-based simulation inputs, and interpret molecular dynamics outputs; not a newly pretrained model. |
| **Training data** | No dedicated training dataset described; the system operates via prompt-based agent orchestration and physics-based molecular dynamics simulations rather than supervised training on a curated dataset. |
| **Downstream tasks** | `enzyme-engineering` `molecular-dynamics` `mutation-library-design` `protein-design`<br>Applied to two protein engineering tasks: engineering halide methyltransferase toward bulkier substrates and engineering bidomain amylase for enhanced activity at lower temperature, producing smart mutation libraries validated experimentally. |
| **Modalities** | `natural language`, `protein structure/dynamics`, `molecular simulation trajectories` |
| **Note** | Full text metadata/abstract and article HTML were accessible; base LLM identity, model size, and detailed quantitative results (e.g., fold-improvement numbers) were not present in the fetched excerpt, so params and precise numeric gains are left unstated rather than guessed. The paper calls itself "open-access" (free to read), which is not the same as open-source; no code or weights repository was found, so "open" reflects that, not publication access. |

**Key results**

- MutexaGPT is described as an 'open-access, multi-agent large language model platform'
- Demonstrated on two tasks: engineering halide methyltransferase toward bulkier substrates and engineering bidomain amylase for enhanced activity at lower temperature
- System yields 'experimentally validated improvements in enzyme specificity and cold activity'

</details>

<a id="model-carpnn-de-novo-car-binders-202609"></a>
<details>
<summary><b>CARPNN (chimaeric antigen receptor-protein-mpNN)</b> — Sequence and structural determinants of efficacious de novo chimaeric antigen receptors <i>(Nat. Biomed. Eng. 202609)</i></summary>

**[Sequence and structural determinants of efficacious de novo chimaeric antigen receptors](https://www.nature.com/articles/s41551-026-01790-9)**

*Nat. Biomed. Eng.* · 202609 · Arthur Chow & [Caleb A. Lareau](https://orcid.org/0000-0003-4179-4807) · [doi:10.1038/s41551-026-01790-9](https://doi.org/10.1038/s41551-026-01790-9)

| | |
| --- | --- |
| **Parameters** | N/A — not a single neural network; a pipeline combining several pretrained models (RFdiffusion, BindCraft/AlphaFold2-hallucination, ProteinMPNN/SolubleMPNN, Boltz-2, AlphaFold2-multimer); no new model parameter count is reported |
| **Backbone** | Composite generative pipeline: RFdiffusion (diffusion backbone generation) + ProteinMPNN sequence design + AlphaFold2-multimer co-fold validation, or BindCraft (AlphaFold2-gradient hallucination); lead optimization via CARPNN, which mutates interface/non-interface residues with SolubleMPNN (temperature 0.4, 2,000–10,000 draws) and refolds/filters candidates with Boltz-2 |
| **Pre-training** | `structure-prediction` `protein-language-model` `diffusion-model` `no-new-pretraining`<br>No new model was pretrained; the authors chained existing pretrained tools (RFdiffusion, ProteinMPNN/SolubleMPNN, BindCraft's AlphaFold2-based hallucination, AlphaFold2-multimer, Boltz-2) into design and filtering pipelines for binder generation and sequence diversification. |
| **Training data** | No new training dataset for a model; instead the study generated and experimentally screened 1,758 de novo designed protein binders against three antigens (BCMA, CD19, CD22) using yeast surface display, biolayer interferometry, CAR-Jurkat/primary CAR-T assays, and in vivo xenograft models.<br>**1,758 designed protein binders screened across BCMA, CD19 and CD22 campaigns** |
| **Downstream tasks** | `CAR-T cell engineering` `protein binder design` `drug discovery` `cancer immunotherapy`<br>Downstream evaluation includes yeast-surface-display binding screens, CAR-Jurkat and primary CAR-T activation/cytokine assays, single-cell RNA-seq of CAR-T cells, in vitro tumour-killing assays, and in vivo xenograft tumour-control experiments in mice. |
| **Modalities** | `protein sequence`, `protein structure` |
| **Code** | [github.com/clareaulab/CARPNN](https://github.com/clareaulab/CARPNN) |
| **Note** | The DOI/URL originally supplied (10.1038/s41551-026-01792-7) is a short paywalled 'Research Briefing' summarizing this primary, fully open-access research article (10.1038/s41551-026-01790-9), which was used for all extracted details. |

**Key results**

- Screened 1,758 newly designed protein binders targeting BCMA, CD19 and CD22 for efficacy in protein-binding, T-cell activation and in vivo killing assays.
- BindCraft campaign yielded 10.7% yeast enrichment for BCMA binders versus a maximum of 2.4% for any RFdiffusion campaign.
- Evolved BCMA binder B5.I0 achieved near-complete tumour control in a high-tumour-burden (1:10 effector:target) xenograft model, whereas the clinical scFv C11D5.3 and biparatopic VHH1-VHH2 (CARVYKTI) binder failed to control tumours at that ratio.
- A single ipSAE ≥0.85 cutoff was the best-calibrated in silico metric predicting sub-1,000 nM binding success across YSD and CARPNN campaigns.
- CARPNN sequence evolution reduced off-target CD22 CAR activation from 42% (parental D1) to 19% (evolved D1.N0) in RPMI-8226 (CD22−) co-cultures while retaining on-target CD69 activation of 65–74%.

</details>

<a id="model-syncraft-202609"></a>
<details>
<summary><b>SynCraft</b> — Guiding large language models to predict edit sequences for molecular synthesizability optimization <i>(Nat. Mach. Intell. 202609)</i></summary>

**[Guiding large language models to predict edit sequences for molecular synthesizability optimization](https://doi.org/10.1038/s42256-026-01304-x)**

*Nat. Mach. Intell.* · 202609 · [Junren Li](https://orcid.org/0000-0003-1411-7288) & Luhua Lai · [doi:10.1038/s42256-026-01304-x](https://doi.org/10.1038/s42256-026-01304-x)

| | |
| --- | --- |
| **Parameters** | N/A — not a trained neural net; uses the pretrained Gemini-2.5-Pro LLM via API with retrieval-augmented few-shot prompting, no fine-tuning or disclosed parameter count |
| **Backbone** | Gemini-2.5-Pro LLM driven by Chain-of-Thought prompting and Retrieval-Augmented Generation (top-k=5 Morgan fingerprint retrieval), outputting a discrete atom-level edit action space (DEL_ATOM, MUTATE_ATOM, ADD_ATOM, ADD_BOND/DEL_BOND, CHANGE_BOND, SET_CHIRAL/SET_BOND_STEREO) deterministically executed by RDKit; optional interaction-aware module using AutoDock Vina docking + PLIP interaction profiling with graph alignment to inject 3D binding constraints into the prompt. |
| **Pre-training** | `frozen pretrained LLM` `no fine-tuning` `retrieval-augmented generation` `few-shot prompting`<br>No model pretraining/fine-tuning is performed; SynCraft uses the off-the-shelf Gemini-2.5-Pro model purely via in-context few-shot prompting, retrieving top-5 similar exemplars (reasoning + edit sequence) from a curated 'Synthesis Cliff' reference database at inference time. |
| **Training data** | A 'Synthesis Cliff Dataset' was constructed by taking unsynthesizable molecules generated by five structure-based 3D generative models (LiGAN, 3D-SBDD, Pocket2Mol, DiffSBDD, ResGen) from the GenBench3D benchmark, flagging unsynthesizable ones via the SimpRetro retrosynthesis model (USPTO-derived templates, Enamine building blocks), and pairing each with its nearest synthesizable neighbor (ECFP4 Tanimoto >0.5 and Pharm2D >0.5) from the ~23-million-compound eMolecules database; Gemini-2.5-Pro was used to generate chemical rationales for each pair, forming the few-shot reference corpus (not model training weights).<br>**3,332 unsynthesizable-to-synthesizable cliff pairs; eMolecules database of ~23 million compounds searched** |
| **Downstream tasks** | `synthesizability optimization` `molecular editing` `hit optimization` `structure-based drug design` `retrosynthesis-aware design`<br>Evaluated on restoring synthesizability of molecules generated by Pocket2Mol and ResGen (1,725 and 1,025 test molecules respectively) while preserving structural similarity; applied retrospectively to replicate human medicinal chemist edits on PLK1 inhibitors, and prospectively to rescue 42 high-scoring but previously discarded RIPK1 inhibitor candidates using interaction-aware (docking + PLIP) constraints. |
| **Modalities** | `SMILES/molecular graph (atom-mapped)`, `natural language reasoning text`, `3D protein-ligand docking poses` |
| **Code** | [github.com/catalystforyou/SynCraft-Core](https://github.com/catalystforyou/SynCraft-Core) |
| **Note** | Based on the arXiv preprint (2512.20333, posted Dec 2025) since the Nature Machine Intelligence version of record was paywalled/inaccessible; content, figures and numbers should match the published version but exact final wording may differ slightly. |

**Key results**

- On Pocket2Mol test set, SynCraft achieved 42.7% success rate at Tanimoto similarity >0.5 vs ~30% for best baseline (SynFormer/ReaSyn), and 28.4% at >0.6 vs 14.1–15.4% for baselines
- On ResGen test set, SynCraft achieved 44.7% success at >0.5 and 29.1% at >0.6, versus 37.5%/22.0% for the strongest baseline ReaSyn
- Ablation: 5-shot edit-based SynCraft reached 44.68% success at Sim>0.5 on ResGen vs only 26.44% for zero-shot direct-SMILES generation, despite the latter having a higher raw 'Total Solved' rate (72.39% vs 69.27%)
- Retrospective case study: SynCraft's reasoning to remove chiral dimethylpiperazine methyl groups converged with the actual human-expert-modified synthesized PLK1 inhibitor IIP0944
- Prospective RIPK1 case studies: an ether-bridge edit preserved Vina docking score (-10.7 to -10.2 kcal/mol) and a scaffold-hop edit preserved score (-10.2 to -9.9 kcal/mol) while restoring synthesizability
- Estimated operational cost of ~$3–5 USD per 100 optimization runs using the Gemini-2.5-Pro API

</details>

<a id="model-map-knowledge-driven-perturbation-202608"></a>
<details>
<summary><b>MAP (mechanism-aware perturbation response predictor)</b> — A knowledge-driven framework for predicting single-cell responses for unprofiled drugs <i>(Nat. Mach. Intell. 202608)</i></summary>

**[A knowledge-driven framework for predicting single-cell responses for unprofiled drugs](https://www.nature.com/articles/s42256-026-01286-w)**

*Nat. Mach. Intell.* · 202608 · Jinghao Feng & Weidi Xie · [doi:10.1038/s42256-026-01286-w](https://doi.org/10.1038/s42256-026-01286-w)

| | |
| --- | --- |
| **Parameters** | not stated as a single total parameter count (uses frozen ESM-2 and MoleculeSTM encoders + trainable adapter MLPs + 4-layer transformer + STATE SE-600M foundation model) |
| **Backbone** | Knowledge encoders: BioBERT (text), MoleculeSTM (SMILES, frozen + 4 trainable MLP layers), ESM-2 (protein sequence, frozen + 4 trainable MLP layers) aligned via contrastive InfoNCE pretraining on MAP-KG; perturbation predictor conditions a pretrained single-cell foundation model (STATE SE-600M) via a 4-self-attention-layer transformer encoder fusing drug, gene, and cell-state embeddings, followed by an MLP decoder. |
| **Pre-training** | `knowledge-graph` `contrastive-learning` `multimodal-alignment` `molecular-structure` `protein-language-model`<br>Knowledge-driven multimodal contrastive (InfoNCE) pretraining on MAP-KG, aligning drug SMILES, protein sequences, and free-text mechanism-of-action descriptions (via frozen MoleculeSTM/ESM-2 encoders plus BioBERT) into a unified mechanism-aware embedding space, using both intra-node attribute alignment and inter-node relation-conditioned alignment. |
| **Training data** | MAP-KG, a constructed knowledge graph unifying 14 public biomedical resources (including PrimeKG) linking drugs and genes via mechanistic relations; perturbation prediction trained/evaluated on Tahoe-100M, OP3, SciPlex3 and ComboSciPlex single-cell perturbation atlases.<br>**187,089 drugs, 22,924 genes, 694,246 mechanistic relations (428,192 drug-gene + 266,054 gene-gene edges) in MAP-KG** |
| **Downstream tasks** | `perturbation-response-prediction` `zero-shot-drug-generalization` `virtual-screening` `gene-set-enrichment-analysis` `drug-combination-prediction`<br>Zero-shot prediction of single-cell transcriptional response to unseen cell type-drug combinations and to entirely unprofiled drugs; extension to two-drug combination perturbation prediction; pathway-level GSEA-based in silico virtual screening for anti-cancer drug prioritization in A-549 lung cancer cells. |
| **Modalities** | `gene expression (scRNA-seq)`, `molecular structure (SMILES)`, `protein sequence`, `text (mechanism-of-action descriptions)`, `knowledge graph` |
| **Code** | [huggingface.co/datasets/RainGate/MAP-KG](https://huggingface.co/datasets/RainGate/MAP-KG) |
| **Note** | MAP-KG dataset is openly released on Hugging Face, but model code/weights for the perturbation predictor itself were not confirmed as released in the fetched text; params count not disclosed as a single number since it combines multiple frozen/pretrained backbones. |

**Key results**

- Improves top-50 DEG Pearson delta correlation by up to +12.3% (unseen cell type-drug combos) and +11.8% (unprofiled drugs) over strongest baselines across three benchmarks
- On Tahoe-100M unprofiled-drug regime: +17.5% top-50 DEG direction accuracy, +11.8% top-50 DEG Pearson delta correlation, +16.9% HVG perturbation discrimination score over baselines
- Prioritizes four out of five approved anti-cancer drugs among top-14 of 58 held-out compounds for A-549 (NSCLC) in silico screening; adagrasib and afatinib ranked 2nd and 4th
- MAP-KG comprises 187,089 drugs, 22,924 genes and 694,246 mechanistic relations from 14 public resources
- Per-compound top-50 DEG Pearson delta correlation on unprofiled drugs ranged from 0.942 (sildenafil) to 0.620 (ciclopirox), highest of all baselines on all 16 test compounds

</details>

<a id="model-dyna-1-202608"></a>
<details>
<summary><b>Dyna-1</b> — Learning millisecond protein dynamics from what is missing in NMR spectra <i>(Nature 202608)</i></summary>

**[Learning millisecond protein dynamics from what is missing in NMR spectra](https://doi.org/10.1038/s41586-026-10989-4)**

*Nature* · 202608 · Hannah K. Wayment-Steele & Dorothee Kern · [doi:10.1038/s41586-026-10989-4](https://doi.org/10.1038/s41586-026-10989-4)

| | |
| --- | --- |
| **Parameters** | not stated (fine-tuned on top of frozen ESM-3 embeddings; full ESM-3 model size not specified in preprint) |
| **Backbone** | Classifier head on layer-22 embeddings of ESM-3 (sequence+structure), compared against ESM-2 layers, AlphaFold2 pair representation, and one-hot-amino-acid transformer baselines; binary per-residue classification task |
| **Pre-training** | `ESM-3` `self-supervised protein language model` `transfer learning`<br>Built on frozen embeddings from a pretrained ESM-3 model (layer 22 selected as best-performing) and also tested ESM-2 and AlphaFold2 pair representations; the protein-dynamics classifier itself was trained from scratch on curated BMRB missing-assignment data. |
| **Training data** | Curated a 'missing assignment BMRB' (mBMRB) dataset from ~10,000 BMRB-deposited proteins, using ~5,906 proteins with usable structures (2,680 lacking X-ray/EM structures) to train a binary classifier predicting missing NMR peak assignments as a proxy for µs-ms exchange broadening; evaluated on RelaxDB, a hand-curated benchmark of 133 single-domain protein relaxation datasets (plus RelaxDB-CPMG) and a held-out mBMRB-Test split.<br>**~5,906 training proteins (mBMRB), 133 proteins in RelaxDB benchmark** |
| **Downstream tasks** | `protein dynamics prediction` `NMR data reinterpretation` `enzyme/ligand-binding site discovery` `structural biology`<br>Predicts per-residue probability of µs-ms conformational exchange from sequence/structure alone, used to reinterpret existing NMR relaxation datasets, flag likely mis-assignments, and highlight biologically relevant dynamic motifs (e.g., ligand-binding loops in flavodoxin, the mRNA-binding loop of ribonuclease toxin MqsR). |
| **Modalities** | `protein sequence`, `protein structure (ESMFold/AlphaFold2 predicted)`, `NMR relaxation data` |
| **Code** | [github.com/WaymentSteeleLab/Dyna-1](https://github.com/WaymentSteeleLab/Dyna-1) |
| **Weights** | [github.com/WaymentSteeleLab/Dyna-1](https://github.com/WaymentSteeleLab/Dyna-1) |
| **License** | noncommercial use license (per repo) |
| **Note** | Nature version is paywalled; all extracted text and numbers are from the complete open bioRxiv preprint (2025.03.19.642801), which may differ slightly from the final published version. Parameter count of underlying ESM-3 model not disclosed in the preprint. |

**Key results**

- Naïve secondary-structure-frequency baseline achieved AUROC 0.501 (near random) on the validation set
- AF2-pair-representation model achieved AUROC 0.71 and last-layer ESM-2 embeddings achieved AUROC 0.75 on the validation set; one-hot-amino-acid transformer baseline achieved AUROC 0.62
- Layer-22 ESM-3 embeddings (sequence+structure) achieved the best validation AUROC of 0.77, leading to selection as 'Dyna-1'
- Restricting training to 30% sequence identity / 0.5 TM-score split (~2,700 proteins) only reduced validation AUROC from 0.755 to 0.74 versus the full dataset, arguing against memorization
- Dyna-1 achieved AUROC of 0.92 predicting millisecond exchange in BPTI, matching known 5-state exchange kinetics from MD simulation
- Dyna-1 achieved AUROC of 0.60 (improving to 0.62 after reinterpreting mis-assigned/overlapping peaks) on the NtrC receiver domain, and is generally weakest at predicting exchange in beta-sheets

</details>

<a id="model-lasermpnn-202606"></a>
<details>
<summary><b>LASErMPNN</b> — Zero-shot design of drug-binding proteins via neural iterative selection−expansion <i>(Nature 202606)</i></summary>

**[Zero-shot design of drug-binding proteins via neural iterative selection−expansion](https://www.nature.com/articles/s41586-026-10670-w)**

*Nature* · 202606 · [Benjamin Fry](https://scholar.google.com/citations?user=2TE2_OkAAAAJ&hl=en) & [Nicholas F. Polizzi](https://scholar.google.com/citations?hl=en&user=CgZvDJkAAAAJ&view_op=list_works&sortby=pubdate) · [doi:10.1038/s41586-026-10670-w](https://doi.org/10.1038/s41586-026-10670-w)

| | |
| --- | --- |
| **Parameters** | not stated (GNN) |
| **Backbone** | Extends ProteinMPNN with SE(3)-equivariant Geometric Vector Perceptron (GVP) layers and a Hetero-GATv2 message-passing scheme handling ligand-to-protein and protein-to-protein messages; the ligand encoder runs 3 rounds of GATv2 message passing to build 256-dim per-atom embeddings, paired with a structure predictor for the 3D protein–ligand complex |
| **Pre-training** | `graph neural network` `structure-conditioned`<br>Trained to predict atom-level properties; used in an iterative selection-expansion design loop rather than single-shot generation. |
| **Training data** | Protein–ligand co-crystal structures from the Protein Data Bank (PDB). |
| **Downstream tasks** | `de novo binder design` `side-chain packing` `proofreading`<br>Zero-shot de novo design of high-affinity small-molecule binding proteins, side-chain packing and dihedral-angle prediction, neural proofreading, and designing proteins that protect labile ligands from hydrolysis. |
| **Modalities** | `protein structure`, `small molecules` |
| **Code** | [github.com/polizzilab/LASErMPNN](https://github.com/polizzilab/LASErMPNN) |
| **Note** | Originally cross-listed with AI4biology.md (Keishi's page); that page was later removed from the repo (2026-09-15), so this entry now lives only here, which fits the drug-design/protein-binder scope on its own merits. |

**Key results**

- Hit rate and highest-affinity design each surpassed the prior state-of-the-art method by 5-fold and 70-fold respectively.
- Without any experimental input, LASErMPNN suggested two mutations that increased binding affinity by more than two orders of magnitude (Kd = 1.2 ± 0.2 nM).

</details>

<a id="model-deepdrugdiscovery-202604"></a>
<details>
<summary><b>DeepDrugDiscovery</b> — DeepDrugDiscovery identifies blood–brain barrier permeable autophagy enhancers for Alzheimer’s disease <i>(Nat. Biomed. Eng. 202604)</i></summary>

**[DeepDrugDiscovery identifies blood–brain barrier permeable autophagy enhancers for Alzheimer’s disease](https://www.nature.com/articles/s41551-026-01667-x)**

*Nat. Biomed. Eng.* · 202604 · [Yu Dong](https://scholar.google.com/citations?hl=zh-CN&user=9lXsixYAAAAJ&view_op=list_works) & [Jia-Hong Lu](https://scholar.google.com/citations?hl=en&user=DluFD2sAAAAJ&view_op=list_works) · [doi:10.1038/s41551-026-01667-x](https://doi.org/10.1038/s41551-026-01667-x)

| | |
| --- | --- |
| **Parameters** | not stated (VAE+GRU) |
| **Backbone** | Hybrid variational autoencoder (VAE) fused with a Gated Recurrent Unit (GRU) that combines structural fingerprints with auxiliary molecular descriptors |
| **Pre-training** | `β-VAE` `unsupervised`<br>Unsupervised β-variational autoencoder with progressive Kullback–Leibler annealing, learning a latent compound space without labelled data. |
| **Training data** | A library of unique small-molecule compounds screened computationally for BBB permeability and ADMET properties.<br>**1,155,606 compounds** |
| **Downstream tasks** | `virtual screening` `ADMET prediction` `diversity analysis`<br>Ligand-based virtual screening, ADMET property prediction, diversity analysis, and identification of BBB-permeable, mTOR-independent autophagy enhancers. |
| **Modalities** | `small molecules` |
| **Code** | [github.com/XiangLuXiao/DeepDrugDiscovery](https://github.com/XiangLuXiao/DeepDrugDiscovery) |
| **Note** | Nature and the bioengineer.org writeup describe the validation qualitatively; neither states a numeric hit rate or screening funnel size, so none is given here. |

**Key results**

- Identified multiple novel autophagy enhancers acting outside the broad mTOR pathway; two lead compounds cross the blood–brain barrier.
- Lead compounds cleared amyloid-β and tau aggregates and restored memory function in worm and mouse Alzheimer's disease models.

</details>

<a id="model-lnp-spatial-ai-202603"></a>
<details>
<summary><b>AI-guided LNP design (unnamed in paper)</b> — Artificial intelligence-guided design of LNPs for in vivo targeted mRNA delivery via analysis of the spatial conformation of ionizable lipids <i>(Nat. Biomed. Eng. 202603)</i></summary>

**[Artificial intelligence-guided design of LNPs for in vivo targeted mRNA delivery via analysis of the spatial conformation of ionizable lipids](https://www.nature.com/articles/s41551-026-01640-8)**

*Nat. Biomed. Eng.* · 202603 · [Lin-Jia Su](https://scholar.google.co.uk/citations?user=omc7JboAAAAJ&hl=en&oi=sra) & [Yao-Xin Lin](https://scholar.google.co.uk/citations?user=KXEbGR0AAAAJ&hl=en&oi=ao) · [doi:10.1038/s41551-026-01640-8](https://doi.org/10.1038/s41551-026-01640-8)

| | |
| --- | --- |
| **Parameters** | N/A — non-neural (SISSO symbolic regression) |
| **Backbone** | Sure Independence Screening and Sparsifying Operator (SISSO) symbolic regression over 3D spatial-conformation descriptors, not a neural network |
| **Pre-training** | `symbolic regression` `compressed sensing`<br>No pretraining stage; molecular-dynamics simulations generate 3D conformation descriptors that SISSO regresses against measured delivery efficacy. |
| **Training data** | Representative ionizable lipids with spatial and chemical descriptors and matched experimental mRNA delivery efficacy.<br>**100 lipids · 28 features** |
| **Downstream tasks** | `property prediction` `candidate screening`<br>Predicting mRNA delivery efficiency of ionizable lipid nanoparticles and screening untested lipid candidates for organ-targeted delivery. |
| **Modalities** | `molecular structure` |
| **Note** | Numbers are from the CAS English-language press release (english.cas.cn); the full text is paywalled and was not independently checked. No code or model repository was found. |

**Key results**

- Lead lipid P1 gave a 14.8-fold improvement in mRNA delivery efficiency over the clinical-standard lipid ALC-0315.
- P1's 3D structure binds IgM, giving spleen-targeted delivery; in a mouse melanoma model this produced strong T-cell activation and tumour regression.

</details>

<a id="model-retrochimera-202412"></a>
<details>
<summary><b>RetroChimera</b> — Chemist-aligned retrosynthesis by ensembling diverse inductive bias models <i>(Nature 202412)</i></summary>

**[Chemist-aligned retrosynthesis by ensembling diverse inductive bias models](https://doi.org/10.1038/s41586-026-11160-9)**

*Nature* · 202412 · [Krzysztof Maziarz](https://orcid.org/0009-0007-0477-562X) & [Marwin H. S. Segler](https://orcid.org/0000-0001-8008-0546) · [doi:10.1038/s41586-026-11160-9](https://doi.org/10.1038/s41586-026-11160-9)

| | |
| --- | --- |
| **Parameters** | Ensemble of two models; on the Pistachio dataset NeuralLoc has 165M parameters and R-SMILES 2 has 66.7M parameters (on USPTO-50K: 1.9M and 17.4M respectively) |
| **Backbone** | NeuralLoc: GNN-based template-classification/localization model (GPS+PNA layers, 3-5 layers, hidden dim 64-1024); R-SMILES 2: Transformer encoder-decoder with Group-Query Attention, RMSNorm, SwiGLU (6-8 layers, hidden dim 256-512), combined via a learned pointwise ensembling/reranking scheme |
| **Pre-training** | `supervised` `reaction-prediction` `ensembling`<br>Both submodels are trained from scratch (no generic self-supervised pretraining) directly on reaction datasets to predict reactants from products; a separate learning-based ensembling module (with monotonic convex per-model scoring functions) is fit on a validation split to combine their outputs. |
| **Training data** | Trained and evaluated on USPTO-50K, USPTO-FULL, and the proprietary Pistachio reaction database (curated, larger and more diverse than USPTO-FULL), plus zero-shot/fine-tuning tests on internal Novartis and GSK reaction datasets.<br>**Pistachio training set is ~3.5x larger than USPTO-FULL; zero-shot test used 10,444 internal Novartis reactions** |
| **Downstream tasks** | `retrosynthesis-prediction` `multi-step-synthesis-planning` `reaction-feasibility-scoring`<br>Single-step retrosynthesis prediction (reactant recall accuracy at top-k), multi-step synthetic route search (SimpRetro and hard Pistachio targets), and chemist preference/alignment evaluation via pairwise AB-tests. |
| **Modalities** | `molecular-graphs`, `SMILES` |
| **Code** | [github.com/microsoft/retrochimera](https://github.com/microsoft/retrochimera) |
| **Weights** | [github.com/microsoft/retrochimera](https://github.com/microsoft/retrochimera) |
| **License** | MIT |
| **Note** | Nature version (2026, 'accepted article preview') is paywalled; extracted from the complete open arXiv preprint (2412.05269), which matches the abstract and appears to be the same study accepted at Nature. |

**Key results**

- RetroChimera improves top-10 accuracy over prior state of the art by 1.7% on USPTO-50K and 1.6% on USPTO-FULL
- On a held-out 2024 Pistachio time-split test set of 146,393 reactions, RetroChimera reaches with 10 candidates the accuracy that R-SMILES 2 needs 50 candidates to reach
- In double-blind pairwise chemist evaluations (599 comparisons, 9 experts), chemists preferred RetroChimera's top prediction over the published reference reaction with mean preference rate ≈64% (P<0.05)
- Zero-shot transfer to 10,444 internal Novartis reactions: RetroChimera outperformed both of its constituent submodels without any fine-tuning
- NeuralLoc submodel has 165M parameters and R-SMILES 2 submodel has 66.7M parameters when trained on Pistachio (1.9M / 17.4M respectively on USPTO-50K)

</details>

### Materials & Physical Science

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202610 | [CIF-based Random Forest ml-MXene classifier (unnamed in paper)](#model-mxene-treasure-chest-202610) | Science | N/A — non-neural (Random Forest ensemble classifier was the best-performing of the benchmarked models) | — | ML-guided database mining enabled rapid synthesis of 5 rediscovered and 11 new rare-earth MXenes |
| 202610 | [HIP (Hessian Interatomic Potentials)](#model-hip-hessian-interatomic-potentials-202610) | Nat. Comput. Sci. | not stated in the fetched text | ✓ | HIP predicts molecular Hessians directly, 10–70× faster than autodiff with 2–3× less peak memory |
| 202610 | [MatText (BERT- and Llama-based benchmarking framework)](#model-mattext-cc-cliff-202610) | Nat. Comput. Sci. | Multiple models benchmarked: a custom small BERT (hidden size 512, 4 layers, 8 attention heads; parameter count not stated) and Llama-2/Llama-3 models from 7B to 70B parameters fine-tuned with LoRA. | ✓ | LLMs show a 'geometric blindness': scaling to 70B params or 2M structures barely narrows the gap with GNNs |
| 202608 | [Self-supervised pretrained OAReactDiff/React-OT and AEFM generative transition-state models (RobustTSGen)](#model-robust-ts-gen-202608) | Nat. Comput. Sci. | not stated in the accessible text (diffusion/flow-matching generative models; size not disclosed) | ✓ | Pretraining cuts transition-state RMSD on unseen transition-metal reactions from 0.39 Å to 0.19 Å |
| 202602 | [Discovery Learning](#model-discovery-learning-202602) | Nature | N/A — no single model (learner/interpreter/oracle loop) | ✓ | Predicts full cycle life from ~50 cycles: ~5% of the energy, ~2% of the time of full testing |
| 202501 | [MatterGen](#model-mattergen-202501) | Nature | 46.8M | ✓ | >2x more novel/stable structures than prior baselines; one design (TaCr₂O₆) synthesized |
| 202311 | [GNoME](#model-gnome-202311) | Nature | not stated (GNN) | ✓ | 2.2M candidate crystals, ~380K most stable; 736 independently synthesized externally |
| 202311 | [A-Lab (with ARROWS3 active learning and XRD-AutoAnalyzer)](#model-a-lab-202311) | Nature | not stated \u2014 no single network; pipeline of an NLP similarity/precursor model, an XGBoost temperature regressor, a phase-ID CNN and an actor\u2013critic RL refinement agent, none with published parameter counts | ✓ | Self-driving lab synthesized 36 of 57 predicted inorganic targets in 17 days across 353 robotic recipes |

<a id="model-mxene-treasure-chest-202610"></a>
<details>
<summary><b>CIF-based Random Forest ml-MXene classifier (unnamed in paper)</b> — Data-driven discovery and rapid, direct synthesis of MXenes <i>(Science 202610)</i></summary>

**[Data-driven discovery and rapid, direct synthesis of MXenes](https://doi.org/10.1126/science.aeh5957)**

*Science* · 202610 · [Ali Saffar Shamshirgar](https://orcid.org/0000-0002-0762-8058) & [Johanna Rosen](https://orcid.org/0000-0002-5173-6726) · [doi:10.1126/science.aeh5957](https://doi.org/10.1126/science.aeh5957)

| | |
| --- | --- |
| **Parameters** | N/A — non-neural (Random Forest ensemble classifier was the best-performing of the benchmarked models) |
| **Backbone** | Random Forest classifier operating on structural descriptors parsed from CIF files (symmetry info, pair-distance statistics, density features, structural heterogeneity); benchmarked against SVM, a multilayer perceptron, and a simplified graph-based model, with Random Forest selected as best performer. |
| **Pre-training** | `supervised-classification` `materials-database-mining`<br>No pretraining in the neural-network sense; the classifier was trained from scratch in a supervised manner on a balanced, labeled dataset of ml-MXene vs. non-ml-MXene crystal structures drawn from the Materials Project and OQMD. |
| **Training data** | A balanced set of 1050 labeled crystal structures (525 ml-MXene, 525 non-ml-MXene) compiled from screening the Materials Project and Open Quantum Materials Database for 2:1:2 stoichiometry compounds chemically adjacent to known MXenes.<br>**1050 labeled structures (525 positive / 525 negative)** |
| **Downstream tasks** | `materials-discovery` `crystal-structure-classification` `synthesis-guidance`<br>The trained classifier triaged 541 candidate CIF structures down to 270 high-probability ml-MXene candidates, which were further curated (with literature cross-checking) to a list of 50 compounds; findings guided experimental rediscovery of 5 MXenes via rapid self-propagating high-temperature synthesis and the synthesis of 11 new rare-earth M2CT2 MXenes. |
| **Modalities** | `crystal structure (CIF)`, `tabular structural descriptors` |
| **Note** | Original Science article is paywalled; entry is based on the complete open arXiv preprint (2608.16644), which matches the Science abstract/metadata. No code or model release was found in the available text. |

**Key results**

- Screening Materials Project and OQMD yielded 541 candidate 2:1:2 compounds
- Random Forest outperformed SVM, MLP, and a simplified graph-based model on a balanced 1050-structure labeled dataset
- A probability threshold of P(ml-MXene) > 0.8 narrowed candidates to 270, further curated to a 50-material 'Treasure Chest'
- Guided by the ML screen, researchers experimentally rediscovered 5 MXenes using a self-propagating high-temperature synthesis completing within minutes without sustained external heating
- 11 previously unexplored rare-earth M2CT2 MXenes (M = Pr, Nd, Sm, Gd, Tb, Ho, Tm) were synthesized, showing semiconducting behavior and diverse magnetic states
- 26 additional hypothetical phases were theoretically predicted to be stable

</details>

<a id="model-hip-hessian-interatomic-potentials-202610"></a>
<details>
<summary><b>HIP (Hessian Interatomic Potentials)</b> — HIP: Hessian Interatomic Potentials without derivatives <i>(Nat. Comput. Sci. 202610)</i></summary>

**[HIP: Hessian Interatomic Potentials without derivatives](https://doi.org/10.1038/s43588-026-01066-x)**

*Nat. Comput. Sci.* · 202610 · Andreas Burger & Alán Aspuru-Guzik · [doi:10.1038/s43588-026-01066-x](https://doi.org/10.1038/s43588-026-01066-x)

| | |
| --- | --- |
| **Parameters** | not stated in the fetched text |
| **Backbone** | SE(3)-equivariant EquiformerV2 backbone (reused from the HORM model) with an added equivariant Hessian readout head combining node and pairwise message contributions (an extra EquiformerV2-style readout layer was added for expressivity) |
| **Pre-training** | `equivariant-GNN` `Hessian-supervised` `fixed-backbone-finetuning`<br>HIP keeps a fixed EquiformerV2 backbone (from the HORM molecular Hessian model) and trains only a new Hessian-prediction readout head on energies, forces and DFT Hessians, using a learning-rate warm-up over 15k steps from 0 to 5e-4 followed by cosine decay over 500k steps to 5e-5, trained on a single H100 GPU.' |
| **Training data** | Trained/evaluated using DFT reference Hessians (e.g. recomputed with GPU4PySCF v1.3.0 at ωB97X/6-31G* for a transition-state proposal subset) built on top of the HORM large-scale molecular Hessian database; model performance evaluated on a held-out validation set.<br>**10,000 validation structures** |
| **Downstream tasks** | `transition-state-search` `geometry-optimization` `vibrational-analysis`<br>Direct Hessian prediction is used to accelerate transition-state searches, geometry optimization and vibrational (normal-mode) analysis compared with Hessians obtained via automatic differentiation of a learned potential. |
| **Modalities** | `3D molecular structure`, `quantum-chemical Hessian/energy/force labels` |
| **Code** | [github.com/BurgerAndreas/hip](https://github.com/BurgerAndreas/hip) |
| **Weights** | [huggingface.co/andreasburger/hip](https://huggingface.co/andreasburger/hip) |
| **License** | Apache-2.0 (code repository) |
| **Note** | Original Nature Computational Science article (paywalled DOI) was not directly fetchable; entry is built from the openly available arXiv/OpenReview preprint 'Shoot from the HIP: Hessian Interatomic Potentials without derivatives' (arXiv:2509.21624), which appears to be the same work. Code and weights links were added after extraction by checking the repository directly: BurgerAndreas/hip is Apache-2.0, its README links this arXiv paper (2509.21624), and checkpoints are hosted on Hugging Face. |

**Key results**

- HIP accelerates Hessian predictions 10–70 times and reduces peak memory by a factor of 2–3 compared with automatic differentiation of the underlying potential.
- HIP maintains O(N) scaling with the number of atoms, versus worse scaling for automatic-differentiation-based Hessians.
- On the reported benchmark, HIP-EquiformerV2 achieves Hessian error 0.030, eigenvalue error 0.063, top-eigenvector cosine similarity 0.982 and lowest-eigenvalue error 0.031 at 38.5 (time units); an improved variant (HIP-EquiformerV2*) achieves 0.020, 0.041, 0.982 and 0.031 at 31.4.

</details>

<a id="model-mattext-cc-cliff-202610"></a>
<details>
<summary><b>MatText (BERT- and Llama-based benchmarking framework)</b> — Less can be more for predicting properties with large language models <i>(Nat. Comput. Sci. 202610)</i></summary>

**[Less can be more for predicting properties with large language models](https://doi.org/10.1038/s43588-026-01045-2)**

*Nat. Comput. Sci.* · 202610 · [Nawaf Alampara](https://scholar.google.com/citations?user=R7K3xFIAAAAJ&hl=en) & [Kevin Maik Jablonka](https://scholar.google.com/citations?user=R2ntI8IAAAAJ&hl=en) · [doi:10.1038/s43588-026-01045-2](https://doi.org/10.1038/s43588-026-01045-2)

| | |
| --- | --- |
| **Parameters** | Multiple models benchmarked: a custom small BERT (hidden size 512, 4 layers, 8 attention heads; parameter count not stated) and Llama-2/Llama-3 models from 7B to 70B parameters fine-tuned with LoRA. |
| **Backbone** | BERT-base-uncased-style encoder (hidden size 512, 4 hidden layers, 8 attention heads, max position embedding 1024, MLM pretraining) and decoder-only Llama-2/Llama-3 (7B–70B) fine-tuned via parameter-efficient LoRA; compared against GNN baselines (CoGN, SchNet, DimeNet) and descriptor-based MODNet. |
| **Pre-training** | `self-supervised` `masked-language-modeling` `text-representation-of-crystals` `LoRA-finetuning`<br>BERT variants were pretrained from scratch with masked language modeling (15% masking) on nine different text representations of crystal structures (e.g., CIF P1, SLICES, Z-matrix, composition, local environment) at dataset scales from 30K to 2M structures sourced from the NOMAD archive via the MatBench suite; Llama-2/Llama-3 models (7B–70B) were general-purpose pretrained LLMs subsequently parameter-efficiently fine-tuned (LoRA) on the same text representations for property regression. |
| **Training data** | Crystal structures converted into nine text representations using the authors' MatText package, drawn from the NOMAD open materials archive and benchmarked via the MatBench suite, at scales ranging from 30,000 up to 2 million structures.<br>**up to 2 x 10^6 crystal structures** |
| **Downstream tasks** | `materials-property-prediction` `benchmarking` `shear-modulus` `bulk-modulus` `formation-energy`<br>Regression of shear modulus, bulk modulus, and perovskite formation energy from text-encoded crystal structures, plus a synthetic coordinate-category probing task and comparison against the MatBench leaderboard (GNNs, descriptor-based MODNet, and other LLM-based approaches). |
| **Modalities** | `text`, `crystal structure (tabular/coordinate-category)` |
| **Code** | [github.com/lamalab-org/MatText](https://github.com/lamalab-org/MatText) |
| **Weights** | [huggingface.co/datasets/n0w0f/MatText (datasets); example pretrained model e.g. n0w0f/MatText-cifp1-2m](https://huggingface.co/datasets/n0w0f/MatText (datasets); example pretrained model e.g. n0w0f/MatText-cifp1-2m) |
| **License** | MIT |
| **Note** | Original Nature Computational Science article (paywalled) could not be fetched directly; entry is based on the complete arXiv preprint (2406.17295v3), the authors' official project/results page (lamalab-org.github.io/MatText), and search-engine-indexed snippets of the published abstract, which together closely match the published version's stated results (e.g., up to 70B parameters, 2M structures) though some published-version experimental details (e.g., exact Llama-2 7B/13B/70B table numbers) could not be independently verified beyond the arXiv v3 Llama-3-8B results. |

**Key results**

- Geometric blindness (LLMs failing to use coordinate information while excelling at categorical patterns) persists regardless of model size (up to 70B parameters), dataset scale (up to 2 million structures), or text representation strategy.
- Scaling dataset size (30K to 2M structures) or model size (7B to 70B parameters) changed RMSE by only single digits (percent), far from closing the gap with GNNs.
- On MatBench-style tasks, best BERT-based RMSE for perovskite formation energy was ~0.095 eV versus a GNN SOTA of 0.055 eV; fine-tuned Llama-3-8B-Instruct performed worse still (RMSE 0.181-0.716 eV depending on representation).
- Across the MatBench leaderboard, GNN-based and language-based approaches segregate almost perfectly into a 'GNN-LM wall', with language models consistently at the high-error end across six material-property tasks.

</details>

<a id="model-robust-ts-gen-202608"></a>
<details>
<summary><b>Self-supervised pretrained OAReactDiff/React-OT and AEFM generative transition-state models (RobustTSGen)</b> — Robust generative transition-state models for unseen chemistry <i>(Nat. Comput. Sci. 202608)</i></summary>

**[Robust generative transition-state models for unseen chemistry](https://doi.org/10.1038/s43588-026-01034-5)**

*Nat. Comput. Sci.* · 202608 · Samir Darouich & Heather J. Kulik · [doi:10.1038/s43588-026-01034-5](https://doi.org/10.1038/s43588-026-01034-5)

| | |
| --- | --- |
| **Parameters** | not stated in the accessible text (diffusion/flow-matching generative models; size not disclosed) |
| **Backbone** | Generative transition-state models built on OAReactDiff/React-OT (SE(3)-equivariant diffusion) and AEFM (equivariant flow-matching model), fine-tuned from equilibrium-conformer self-supervised pretraining |
| **Pre-training** | `self-supervised` `pseudo-reaction pretraining` `equilibrium conformers`<br>A self-supervised pretraining strategy constructs pseudo-reactions from abundant equilibrium conformer structures (independent of the Transition1x TS dataset), exposing the generative model to diverse chemical environments before supervised fine-tuning on transition-state data. |
| **Training data** | Fine-tuning data come from the Transition1x dataset of small-organic-molecule reactions, extended with curated benchmarks built via controlled elemental substitutions and a diverse transition-metal-complex (TMC) reaction set to probe generalization to unseen elements/chemistry. |
| **Downstream tasks** | `transition-state structure prediction` `reaction barrier estimation` `catalysis/transition-metal chemistry generalization`<br>Evaluated on predicting transition-state geometries and reaction energetics for reactions involving previously unseen elements and transition-metal complexes, including out-of-distribution Rh/Pt-catalyzed reactions and low-data fine-tuning regimes. |
| **Modalities** | `3D molecular geometry` |
| **Code** | [github.com/samirdarouich/RobustTSGen](https://github.com/samirdarouich/RobustTSGen) |
| **Weights** | [doi.org/10.5281/zenodo.18338076](https://doi.org/10.5281/zenodo.18338076) |
| **License** | MIT (code repository) |
| **Note** | Original Nature Computational Science article is paywalled; entry is based on the complete open arXiv preprint (arXiv:2601.16469, 'Beyond the Training Domain...') and the paper's public GitHub/Zenodo resources, which match the published title/DOI per cross-references. |

**Key results**

- Self-supervised pretraining lowers the median RMSD of predicted TS geometries on Transition1x-TMC reactions from 0.39 Å to 0.19 Å.
- Pretraining reduces the fine-tuning data required to reach comparable accuracy by up to 75%, enabling reliable performance in low-data regimes.
- Without pretraining, generative TS models produce unphysical geometries and large energetic errors on chemically novel (unseen-element/TMC) reactions despite good performance on organic reactions.

</details>

<a id="model-discovery-learning-202602"></a>
<details>
<summary><b>Discovery Learning</b> — Discovery Learning predicts battery cycle life from minimal experiments <i>(Nature 202602)</i></summary>

**[Discovery Learning predicts battery cycle life from minimal experiments](https://www.nature.com/articles/s41586-025-09951-7)**

*Nature* · 202602 · [Jiawei Zhang](https://scholar.google.com/citations?user=tbtanasAAAAJ) & [Ziyou Song](https://scholar.google.com/citations?user=CWEeVz4AAAAJ) · [doi:10.1038/s41586-025-09951-7](https://doi.org/10.1038/s41586-025-09951-7)

| | |
| --- | --- |
| **Parameters** | N/A — no single model (learner/interpreter/oracle loop) |
| **Backbone** | Closed reasoning loop of a “learner” (active-learning cycle-life predictor), an “interpreter” (physics-based battery simulator plus historical data) and an “oracle” (final prediction), not a single neural network |
| **Pre-training** | `active learning` `physics-guided` `zero-shot`<br>Active learning selects a few battery candidates to run for ~50 cycles; physics-guided simulation and zero-shot transfer extrapolate to full cycle life. |
| **Training data** | Large-format lithium-ion pouch cells; the model generalised to pouch cells after training only on cylindrical-cell data.<br>**123 pouch cells** |
| **Downstream tasks** | `cycle-life prediction`<br>Predicting the number of charge–discharge cycles before capacity drops below 90% of design capacity, from ~50 cycles of data. |
| **Modalities** | `battery cycling time series` |
| **Code** | [zenodo.org/records/17654407](https://zenodo.org/records/17654407) |
| **Note** | Coverage (EurekAlert, Newswise) gives resource savings, not a numeric prediction-error figure (e.g. MAPE); left blank rather than guessed. |

**Key results**

- Predicts cycle life from ~50 cycles using an estimated 5% of the energy and 2% of the time of conventional full-life testing (days–weeks vs. months–years).
- Generalised across cell geometry: trained on cylindrical cells, validated on larger pouch cells.

</details>

<a id="model-mattergen-202501"></a>
<details>
<summary><b>MatterGen</b> — A generative model for inorganic materials design <i>(Nature 202501)</i></summary>

**[A generative model for inorganic materials design](https://www.nature.com/articles/s41586-025-08628-5)**

*Nature* · 202501 · Claudio Zeni & Tian Xie · [doi:10.1038/s41586-025-08628-5](https://doi.org/10.1038/s41586-025-08628-5)

| | |
| --- | --- |
| **Parameters** | 46.8M |
| **Backbone** | SE(3)-equivariant graph neural network based on GemNet-dT (the non-conservative force-prediction variant of GemNet), 4 message-passing layers, 512-dim hidden node/edge features, 7Å neighbor cutoff; jointly denoises atomic positions, element types and lattice parameters under periodicity constraints |
| **Pre-training** | `diffusion`<br>Denoising diffusion trained end-to-end on crystal structures; can be fine-tuned toward property constraints (bulk modulus, band gap, chemical system, magnetic density). |
| **Training data** | Stable inorganic materials from the Materials Project and Alexandria databases.<br>**~608,000 structures** |
| **Downstream tasks** | `generative design` `property-guided generation`<br>Property-guided generation of novel, stable inorganic crystals across the periodic table; one generated structure (TaCr₂O₆) was synthesised experimentally. |
| **Modalities** | `crystal structure` |
| **Code** | [github.com/microsoft/mattergen](https://github.com/microsoft/mattergen) |
| **Weights** | [huggingface.co/microsoft/mattergen](https://huggingface.co/microsoft/mattergen) |
| **Note** | License not independently confirmed — check the repo before citing it as permissive. |

**Key results**

- Generated structures are reported as more than twice as likely to be novel and stable, and more than ten times closer to the local energy minimum, than prior generative baselines.

</details>

<a id="model-gnome-202311"></a>
<details>
<summary><b>GNoME</b> — Scaling deep learning for materials discovery <i>(Nature 202311)</i></summary>

**[Scaling deep learning for materials discovery](https://www.nature.com/articles/s41586-023-06735-9)**

*Nature* · 202311 · Amil Merchant & Ekin Dogus Cubuk · [doi:10.1038/s41586-023-06735-9](https://doi.org/10.1038/s41586-023-06735-9)

| | |
| --- | --- |
| **Parameters** | not stated (GNN) |
| **Backbone** | Graph neural network over crystal-structure graphs, paired with learned interatomic potentials for molecular-dynamics simulation |
| **Pre-training** | `active learning` `DFT-supervised`<br>Active-learning loop combining structural and compositional models, bootstrapped from ~48,000 known stable crystals and refined against hundreds of millions of first-principles (DFT) calculations. |
| **Training data** | Crystal structures and stability labels from the Materials Project, expanded through the active-learning loop.<br>**~48,000 seed crystals** |
| **Downstream tasks** | `stability prediction` `materials discovery`<br>Predicting the stability of candidate inorganic crystal structures to find new stable materials; interatomic potentials also support ionic-conductivity prediction. |
| **Modalities** | `crystal structure` |
| **Code** | [github.com/google-deepmind/materials_discovery](https://github.com/google-deepmind/materials_discovery) |
| **Note** | Flagged for balance: the discovery-count claims have drawn published pushback over duplicate/near-duplicate structures (see C&EN, “Duplicate structures haunt crystallography databases”, Dec. 2025, and The Register, Apr. 2024). Included as a landmark, heavily-cited result, with that dispute noted rather than omitted. |

**Key results**

- Identified 2.2 million candidate structures below the known stability threshold, of which ~380,000 are the most stable — roughly a ten-fold expansion of known stable materials.
- 736 of the predicted structures were independently synthesised and confirmed by external groups.

</details>

<a id="model-a-lab-202311"></a>
<details>
<summary><b>A-Lab (with ARROWS3 active learning and XRD-AutoAnalyzer)</b> — An autonomous laboratory for the accelerated synthesis of inorganic materials <i>(Nature 202311)</i></summary>

**[An autonomous laboratory for the accelerated synthesis of inorganic materials](https://www.nature.com/articles/s41586-023-06734-w)**

*Nature* · 202311 · [Nathan J. Szymanski](https://orcid.org/0000-0003-2255-9676) & [Gerbrand Ceder](https://orcid.org/0000-0001-9275-3605) · [doi:10.1038/s41586-023-06734-w](https://doi.org/10.1038/s41586-023-06734-w)

| | |
| --- | --- |
| **Parameters** | not stated \u2014 no single network; pipeline of an NLP similarity/precursor model, an XGBoost temperature regressor, a phase-ID CNN and an actor\u2013critic RL refinement agent, none with published parameter counts |
| **Backbone** | Modular: text-mined synthesis-similarity encoder + masked precursor-completion model for recipe proposal; XGBoost regressor for synthesis temperature; XRD phase ID by CNN with 6 convolutional layers (max pooling between each) and 3 fully connected ReLU layers, batch norm and 50% dropout, Monte Carlo dropout ensemble of 100 networks at inference; automated Rietveld refinement by PPO actor\u2013critic agent driving GSAS-II; ARROWS3 active learning over DFT reaction energies |
| **Pre-training** | `text-mined-literature` `supervised` `simulated-data` `reinforcement-learning` `active-learning`<br>Recipe models were trained on text-mined literature synthesis procedures; the XRD CNN is trained per-target on simulated diffraction patterns (200 per reference phase, augmented for strain, texture, impurity peaks and poor crystallinity) derived from ICSD/Materials Project structures; the Rietveld agent was trained by PPO reinforcement learning in a custom gym environment wrapping GSAS-II. |
| **Training data** | Knowledge base of 33,343 solid-state synthesis procedures extracted from 24,304 publications for recipe/temperature models; SynTERRA text-mined data from >24,000 publications used for novelty filtering; ICSD experimental structures plus Materials Project (v2022.10.28) DFT entries cross-referenced with a Google DeepMind database for target screening and XRD simulation.<br>**33,343 synthesis procedures from 24,304 publications** |
| **Downstream tasks** | `autonomous-experimentation` `materials-synthesis` `synthesis-planning` `XRD-phase-identification` `active-learning`<br>Closed-loop screening of novel air-stable inorganic targets, ML proposal of precursor sets and firing temperatures, robotic powder dosing/heating/XRD characterization, automated phase and weight-fraction analysis, and active-learning re-planning of failed syntheses via pairwise reaction pathways. |
| **Modalities** | `X-ray diffraction patterns`, `crystal structures / DFT thermodynamic data`, `scientific text (synthesis literature)` |
| **Code** | [github.com/mattmcdermott/novel-materials-screening](https://github.com/njszym/ARROWS ; https://github.com/njszym/XRD-AutoAnalyzer ; https://github.com/CederGroupHub/SynthesisSimilarity ; https://github.com/CederGroupHub/s4 ; https://github.com/mattmcdermott/novel-materials-screening) |
| **Note** | An Author Correction was published 19 January 2026 (10.1038/s41586-025-09992-y); the current article text reports 36/57 successes, while stale page metadata and the original abstract still cite 41/58 \u2014 the 36/57 and 63% figures used here are from the corrected main text. The paper drew public criticism from solid-state chemists over XRD-based phase assignments and novelty of some targets. |

**Key results**

- Synthesized 36 of 57 target compounds (63% success) in 17 days of continuous closed-loop operation, spanning 33 elements and 40 structural prototypes
- 353 synthesis recipes were tested; only 30% of individual recipes produced their target, and 30 of the 36 successes came from literature-trained ML recipes
- Active learning (ARROWS3) found improved routes for 9 targets, 6 of which had zero yield from the initial literature-inspired recipes
- Manual regrinding/higher-temperature follow-up added 2 targets (Y3Ga3In2O12, Mg3NiO4), raising success to 67%; excluding 3 computationally problematic compounds gives 70% (38/54)
- 88 unique pairwise reactions were catalogued, which can prune the recipe search space by up to 80%
- Rerouting CaFe2P2O9 synthesis through CaFe3P3O13 (77 vs 8 meV per atom driving force) raised target yield by about 70%
- Average hardware exception rate across stations was about 3.9% over 1.5 years of operation

</details>

### Research Agents & Literature Tools

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202609 | [Virtual Biotech](#model-virtual-biotech-202609) | Science | N/A — not a single neural net; orchestration of LLM agents (Claude via Anthropic's Agent SDK), underlying model size undisclosed | — | Multi-agent 'Virtual Biotech' analyzed 55,984 trials, finding cell-type-specific targets 48% more likely to reach market |
| 202609 | [Paper2Agent](#model-paper2agent-202609) | Nature | N/A — not a single trained neural network; a multi-agent orchestration framework built on an off-the-shelf LLM (claude-sonnet-4-20250514 used in evaluations) | ✓ | Turns papers into AI agents; AlphaGenome agent hits 98.7–100% accuracy vs 37–83% for Biomni/Claude+Repo |
| 202607 | [Co-Scientist](#model-co-scientist-202607) | Nature | N/A — built on Gemini, size undisclosed | — | AML candidate KIRA6 showed an 18x separation between malignant and control cell lines |
| 202605 | [ERA (Empirical Research Assistance)](#model-era-202605) | Nature | N/A — base LLM undisclosed | ✓ | 40 SOTA single-cell methods; 14 models beat the CDC's COVID-forecast ensemble |
| 202603 | [The AI Scientist](#model-ai-scientist-202603) | Nature | N/A — multi-model orchestration | ✓ | Autonomously written manuscript passed peer review at a 70%-acceptance ML workshop |
| 202603 | [BioMedAgent](#model-biomedagent-202603) | Nat. Biomed. Eng. | N/A — base model (GPT-4o-mini), size undisclosed by vendor | ✓ | 100% analysable scope on local tools, vs. a narrower scope for online ChatGPT-4o/GPT Assistants |
| 202602 | [OpenScholar](#model-openscholar-202602) | Nature | 8B (generator) | ✓ | +5 pts vs. GPT-4o, +7 vs. PaperQA2 on ScholarQABench; preferred over experts 51-70% |
| 202512 | [SciSciGPT](#model-sciscigpt-202512) | Nat. Comput. Sci. | N/A — base LLM undisclosed | ✓ | Automates science-of-science analytical workflows; no benchmark numbers published |

<a id="model-virtual-biotech-202609"></a>
<details>
<summary><b>Virtual Biotech</b> — The Virtual Biotech: A multi-agent AI framework for therapeutic discovery and development <i>(Science 202609)</i></summary>

**[The Virtual Biotech: A multi-agent AI framework for therapeutic discovery and development](https://doi.org/10.1126/science.aeg6779)**

*Science* · 202609 · [Harrison G. Zhang](https://scholar.google.com/citations?user=d2JMhbEAAAAJ&hl=en) & James Zou · [doi:10.1126/science.aeg6779](https://doi.org/10.1126/science.aeg6779)

| | |
| --- | --- |
| **Parameters** | N/A — not a single neural net; orchestration of LLM agents (Claude via Anthropic's Agent SDK), underlying model size undisclosed |
| **Backbone** | Multi-agent system with a virtual Chief Scientific Officer orchestrator, a chief-of-staff briefing agent, a scientific reviewer agent, and specialized scientist agents organized into four scientific divisions comprising eleven total agents, equipped with more than 100 custom MCPs/analytical tools; built on Anthropic's Agent SDK (Claude models) |
| **Pre-training** | `LLM-agent` `tool-use` `retrieval-augmented` `multi-agent-orchestration`<br>No custom pretraining is described; the system wraps general-purpose Claude LLM agents with domain-specific system prompts, tools, and MCPs rather than training new model weights. |
| **Training data** | Not a trained model in the conventional sense — agents query existing large-scale public biomedical resources at inference time, including Open Targets (targets/diseases/genetic evidence), CELLxGENE and Tabula Sapiens single-cell atlases, the Tahoe-100M drug-perturbation atlas, TCGA PanCancer LUAD cohort, GEO microarray datasets for five ulcerative colitis trials, and a curated set of 55,984 clinical trials.<br>**55,984 clinical trials; 78,726 targets; 39,530 diseases; >100 million single-cell profiles** |
| **Downstream tasks** | `clinical-trial-outcome-prediction` `target-discovery` `drug-safety-analysis` `trial-failure-mechanism-inference`<br>Applied to (1) large-scale annotation and statistical analysis of 55,984 clinical trials to link target genomic/single-cell features to trial success and safety, (2) proposing a B7-H3 antibody-drug conjugate strategy for lung cancer by integrating multimodal evidence, and (3) analyzing a terminated ulcerative colitis trial (anti-OSMRβ mAb) to infer failure mechanisms and propose biomarker-guided enrollment strategies. |
| **Modalities** | `text`, `genetics/genomics`, `single-cell transcriptomics`, `spatial transcriptomics`, `clinical trial records`, `chemoinformatics/pharmacology data` |
| **Note** | Original Science article is paywalled; entry is based on the complete open bioRxiv preprint (DOI 10.64898/2026.02.23.707551), which matches the same title/authors and reports the same key statistics as the journal press materials. No code or model weights repository was found in the preprint's data-availability statement. |

**Key results**

- Used >37,000 clinical-trialist agent instances to curate and analyze 55,984 clinical trials (Phase I n=14,237; Phase II n=22,164; Phase III n=14,911; Phase IV n=4,672).
- Drugs targeting cell-type-specific genes were 40% more likely to progress from Phase I to Phase II and 48% more likely to ever reach Phase IV.
- Cell-type-specific targets were associated with 32% lower adverse event rates on average across organ systems.
- Lower expression bimodality scores were significantly associated with trial termination (OR=0.81), withdrawal (OR=0.88), and suspension (OR=0.70).
- The full target identification/validation case study (statistical genetics, single-cell/spatial transcriptomics, clinicogenomics, modality assessment) cost $46.00 in Anthropic API credits.
- System integrates over 100 custom MCPs/tools spanning 78,726 targets, 39,530 diseases, 14.5 million protein-protein interactions, and >4 billion drug perturbation-response data points.

</details>

<a id="model-paper2agent-202609"></a>
<details>
<summary><b>Paper2Agent</b> — Reimagining research papers as interactive and reliable AI agents <i>(Nature 202609)</i></summary>

**[Reimagining research papers as interactive and reliable AI agents](https://doi.org/10.1038/s41586-026-11044-y)**

*Nature* · 202609 · [Jiacheng Miao](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Jiacheng%20Miao%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en) & [James Zou](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22James%20Zou%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en) · [doi:10.1038/s41586-026-11044-y](https://doi.org/10.1038/s41586-026-11044-y)

| | |
| --- | --- |
| **Parameters** | N/A — not a single trained neural network; a multi-agent orchestration framework built on an off-the-shelf LLM (claude-sonnet-4-20250514 used in evaluations) |
| **Backbone** | Multi-agent pipeline (environment agent, extraction agent, testing agent) that converts a paper's manuscript/code/data into a model context protocol (MCP) server of validated tools, then connects that MCP server to a chat agent (Claude Code, backed by claude-sonnet-4-20250514) for natural-language querying |
| **Pre-training** | `no additional pretraining` `relies on pretrained LLM`<br>No model pretraining is performed; Paper2Agent orchestrates an existing pretrained LLM (Claude Sonnet 4) plus sub-agents to read a paper's manuscript and codebase and auto-generate/validate MCP tools. |
| **Training data** | No training dataset is used to train a model; instead, each paper's own manuscript, supplementary materials, datasets and code repository serve as the knowledge source converted into MCP tools (case studies used AlphaGenome, Scanpy, and TISSUE papers/repos). |
| **Downstream tasks** | `genomic variant interpretation` `single-cell transcriptomics` `spatial transcriptomics` `causal gene prioritization` `multi-agent scientific reasoning`<br>Case studies convert AlphaGenome into an agent for genomic variant effect interpretation and GWAS locus analysis, Scanpy into an agent for single-cell preprocessing/clustering, and TISSUE into an agent for spatial transcriptomics uncertainty estimation; multiple paper-agents are then combined to prioritize GPR137 as a causal gene for a psoriasis-associated variant. |
| **Modalities** | `text`, `genomic sequence/variant data`, `single-cell/spatial transcriptomics data`, `code` |
| **Code** | [github.com/jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) |
| **Note** | The framework itself is not a trained model but an agent-orchestration system wrapping existing LLMs and papers' own code; 'params'/'pretraining'/'training_data' fields reflect that it is not a conventional neural network. |

**Key results**

- Paper2Agent generated 22 AlphaGenome MCP tools, all passing automated validation, in around 45 min at a cost of US $14 on a personal laptop.
- AlphaGenome agent achieved 98.7 ± 1.3% accuracy on 15 tutorial-derived queries and 100.0 ± 0.0% on 15 novel queries, versus 82.7 ± 3.4%/78.7 ± 4.4% for Claude + Repo and 37.3 ± 4.0%/56.0 ± 3.4% for Biomni.
- On 30 open-ended researcher-style queries, the AlphaGenome agent scored 82.7 ± 2.4% accuracy versus 56.7 ± 2.3% (Claude + Repo) and 72.2 ± 2.2% (Biomni).
- The AlphaGenome agent reduced median query runtime by 1.9× and 3.1× versus Claude + Repo and Biomni on tutorial queries, and by 2.9× and 3.8× on novel queries.
- A multi-agent collaboration across AlphaGenome, MPRA-scCRISPRi and Perturb-seq paper-agents identified GPR137 as the likely causal gene for a psoriasis-associated variant (rs887314), with knockdown signature correlating with the CRE perturbation signature (Spearman r = 0.613, P = 3.79×10⁻³ at Stim8hr; r = 0.630, P = 4.71×10⁻³ at Stim48hr, FDR < 0.05).

</details>

<a id="model-co-scientist-202607"></a>
<details>
<summary><b>Co-Scientist</b> — Accelerating scientific discovery with Co-Scientist <i>(Nature 202607)</i></summary>

**[Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)**

*Nature* · 202607 · Juraj Gottweis & Vivek Natarajan · [doi:10.1038/s41586-026-10644-y](https://doi.org/10.1038/s41586-026-10644-y)

| | |
| --- | --- |
| **Parameters** | N/A — built on Gemini, size undisclosed |
| **Backbone** | Multi-agent AI system built on Gemini; agents generate, critique and refine hypotheses in a tournament-style ranking loop, scaled with test-time compute |
| **Pre-training** | `multi-agent` `test-time compute scaling`<br>Orchestration layer over Gemini rather than a separately pretrained model; hypothesis quality improves with additional test-time compute. |
| **Training data** | Evaluated across 203 open-ended research objectives spanning AML drug repurposing, liver fibrosis and antimicrobial resistance, rather than trained on a fixed corpus.<br>**203 research objectives** |
| **Downstream tasks** | `hypothesis generation` `research prioritization`<br>Generating and prioritising scientific hypotheses for wet-lab validation. |
| **Modalities** | `text` |
| **Note** | Closed system — no public code or weights; access is via Google's Gemini for Science research registration, not open source. |

**Key results**

- Proposed AML drug-repurposing candidate KIRA6 showed an 18-fold separation between malignant and control cell lines in follow-up validation.
- Independently recapitulated a previously unpublished bacterial gene-transfer resistance mechanism.
- In expert evaluation across 203 objectives, hypothesis quality was rated above both human experts and leading LLM baselines.

</details>

<a id="model-era-202605"></a>
<details>
<summary><b>ERA (Empirical Research Assistance)</b> — An AI system to help scientists write expert-level empirical software <i>(Nature 202605)</i></summary>

**[An AI system to help scientists write expert-level empirical software](https://www.nature.com/articles/s41586-026-10658-6)**

*Nature* · 202605 · [Eser Aygün](https://scholar.google.com/citations?user=mogd5nkAAAAJ&hl=en) & [Michael Brenner](https://scholar.google.com/citations?user=ZDL6ITwAAAAJ&hl=en) · [doi:10.1038/s41586-026-10658-6](https://doi.org/10.1038/s41586-026-10658-6)

| | |
| --- | --- |
| **Parameters** | N/A — base LLM undisclosed |
| **Backbone** | LLM combined with tree search (TS), which systematically improves a quality metric and navigates the space of candidate programs; for some tasks combined with Gemini Deep Think |
| **Pre-training** | `tree search` `LLM-guided program search`<br>Search/optimization framework over an existing LLM rather than a newly pretrained model. |
| **Training data** | Applied per research task rather than trained on a fixed corpus (bioinformatics, epidemiology, geospatial, neuroscience, physics). |
| **Downstream tasks** | `scientific software generation` `method discovery`<br>Generating expert-level empirical software across domains: single-cell analysis, epidemiological forecasting, geospatial CO2 monitoring, zebrafish neural-activity prediction, numerical integration, and cosmic-string gravitational-wave theory. |
| **Modalities** | `text`, `code`, `scientific data` |
| **Code** | [github.com/google-research/era](https://github.com/google-research/era) |

**Key results**

- Discovered 40 novel single-cell data analysis methods that outperformed the top human-developed methods on a public leaderboard.
- Generated 14 COVID-19 hospitalization forecasting models that outperformed the CDC ensemble and every individual model on the public leaderboard.
- Reached state-of-the-art predictive performance on ZAPBench, predicting activity across more than 70,000 zebrafish neurons.
- Derived six new general solutions and a closed-form asymptotic formula for cosmic-string gravitational radiation, extending beyond the previously known simplest case.

</details>

<a id="model-ai-scientist-202603"></a>
<details>
<summary><b>The AI Scientist</b> — Towards end-to-end automation of AI research <i>(Nature 202603)</i></summary>

**[Towards end-to-end automation of AI research](https://www.nature.com/articles/s41586-026-10265-5)**

*Nature* · 202603 · Yutaro Yamada & [Jeff Clune](https://scholar.google.com/citations?hl=en&user=5TZ7f5wAAAAJ&view_op=list_works&sortby=pubdate) · [doi:10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5)

| | |
| --- | --- |
| **Parameters** | N/A — multi-model orchestration |
| **Backbone** | Multi-agent system orchestrating foundation models for idea generation, coding, experimentation, analysis and manuscript writing, run in both a template-based focused mode and a template-free open-ended mode |
| **Pre-training** | `multi-agent` `agentic search`<br>Orchestration over existing foundation models rather than a newly pretrained model. |
| **Training data** | Evaluated across machine-learning research tasks in both modes rather than trained on a fixed corpus. |
| **Downstream tasks** | `idea generation` `experimentation` `manuscript writing` `self-review`<br>Autonomous end-to-end research: generating ideas, writing code, running experiments, analysing and plotting results, writing the full manuscript, and performing its own peer review. |
| **Modalities** | `text`, `code` |
| **Code** | [github.com/SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) |
| **Note** | Also on AI_agent.md, listed there as Chris Lu & Jeff Clune. The Nature author list (Yamada, Lange, Cong Lu, Chris Lu, Hu, Foerster, Ha, Clune) puts Yutaro Yamada as first author, so that's used here — worth a correction on the AI_agent.md entry too. |

**Key results**

- A fully autonomously generated manuscript passed the first round of peer review for a top-tier ML conference workshop with a 70% acceptance rate.

</details>

<a id="model-biomedagent-202603"></a>
<details>
<summary><b>BioMedAgent</b> — Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses <i>(Nat. Biomed. Eng. 202603)</i></summary>

**[Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://www.nature.com/articles/s41551-026-01634-6)**

*Nat. Biomed. Eng.* · 202603 · [Dechao Bu](https://orcid.org/0000-0002-8833-5432) & [Yi Zhao](https://orcid.org/0000-0001-6046-8420) · [doi:10.1038/s41551-026-01634-6](https://doi.org/10.1038/s41551-026-01634-6)

| | |
| --- | --- |
| **Parameters** | N/A — base model (GPT-4o-mini), size undisclosed by vendor |
| **Backbone** | Self-evolving multi-agent LLM framework that chains bioinformatics tools into executable workflows via interactive exploration and memory retrieval; evaluated against other agents using the same underlying model (GPT-4o-mini) |
| **Pre-training** | `multi-agent` `self-evolving` `tool use`<br>Agentic orchestration and self-evolution over an existing LLM rather than a newly pretrained model. |
| **Training data** | Tool-use framework operating on user-supplied biomedical datasets rather than a fixed training corpus. |
| **Downstream tasks** | `biomedical data analysis` `workflow automation`<br>Autonomous biomedical data analysis from natural-language prompts, with tool chaining and workflow execution requiring no computational expertise from the user. |
| **Modalities** | `text`, `biomedical data` |
| **Code** | [github.com/BOBQWERA/BioMedAgent](https://github.com/BOBQWERA/BioMedAgent) |
| **Note** | Also on AI_agent.md (Meng/Lan's page). |

**Key results**

- Outperformed other LLM agents built on the same base model (GPT-4o-mini), with consistent success-rate improvements across multiple task types.
- Reached a 100% analysable scope using local workspace tools, versus a narrower scope for ChatGPT-4o and GPT Assistants run online.

</details>

<a id="model-openscholar-202602"></a>
<details>
<summary><b>OpenScholar</b> — Synthesizing scientific literature with retrieval-augmented language models <i>(Nature 202602)</i></summary>

**[Synthesizing scientific literature with retrieval-augmented language models](https://www.nature.com/articles/s41586-025-10072-4)**

*Nature* · 202602 · [Akari Asai](https://scholar.google.com/citations?user=gqB4u_wAAAAJ) & [Hannaneh Hajishirzi](https://scholar.google.com/citations?user=LOV6_WIAAAAJ) · [doi:10.1038/s41586-025-10072-4](https://doi.org/10.1038/s41586-025-10072-4)

| | |
| --- | --- |
| **Parameters** | 8B (generator) |
| **Backbone** | Llama-3.1-8B generator, fine-tuned; Contriever-based retriever continued-pretrained on peS2o; BGE-Large reranker; also runs with GPT-4o as the generator (OpenScholar-GPT4o) |
| **Pre-training** | `RAG` `self-feedback` `instruction tuning`<br>Retrieval-augmented generation with a self-feedback inference loop; the 8B generator was instruction-tuned on 13,000 examples (modified torchtune, 8×A100 GPUs). |
| **Training data** | peS2o open-access paper datastore (v2/v3), embedded for dense retrieval.<br>**45,000,000 papers · 200M+ passage embeddings** |
| **Downstream tasks** | `literature synthesis` `citation-grounded QA`<br>Long-form, citation-backed scientific literature synthesis; evaluated on ScholarQABench (2,967 expert queries, 208 long-form answers across 4 domains). |
| **Modalities** | `text` |
| **Code** | [github.com/AkariAsai/OpenScholar](https://github.com/AkariAsai/OpenScholar) |
| **Weights** | Hugging Face collection: OpenScholar-v1 |
| **License** | Apache-2.0 |

**Key results**

- OpenScholar-8B beats GPT-4o by 5 points and PaperQA2 by 7 points on ScholarQABench correctness.
- Citation accuracy on par with human experts, versus a 78–90% citation hallucination rate for GPT-4o.
- In blind evaluation, experts preferred OpenScholar-8B / OpenScholar-GPT4o answers over expert-written ones 51% / 70% of the time.

</details>

<a id="model-sciscigpt-202512"></a>
<details>
<summary><b>SciSciGPT</b> — SciSciGPT: advancing human–AI collaboration in the science of science <i>(Nat. Comput. Sci. 202512)</i></summary>

**[SciSciGPT: advancing human–AI collaboration in the science of science](https://www.nature.com/articles/s43588-025-00906-6)**

*Nat. Comput. Sci.* · 202512 · [Erzhuo Shao](https://orcid.org/0000-0003-2440-271X) & [Dashun Wang](https://orcid.org/0000-0002-7054-2206) · [doi:10.1038/s43588-025-00906-6](https://doi.org/10.1038/s43588-025-00906-6)

| | |
| --- | --- |
| **Parameters** | N/A — base LLM undisclosed |
| **Backbone** | Multi-agent LLM orchestration framework; the fetched abstract/arXiv page does not name the underlying base LLM(s), so it is left unconfirmed rather than guessed |
| **Pre-training** | `multi-agent` `tool use`<br>Agentic orchestration over an existing LLM — no new model is pretrained; agents plan and call bibliometric/analysis tools. |
| **Training data** | Operates over science-of-science bibliometric datasets at inference time rather than a fixed training corpus. |
| **Downstream tasks** | `bibliometric analysis` `research automation`<br>Automates science-of-science analytical workflows: bibliometric analysis, research prototyping/iteration, and reproducibility support. Proposes an LLM-agent capability maturity model for human–AI collaboration. |
| **Modalities** | `text`, `structured bibliometric data` |
| **Code** | [github.com/Northwestern-CSSI/SciSciGPT](https://github.com/Northwestern-CSSI/SciSciGPT) |
| **License** | CC BY-NC-SA 4.0 (arXiv preprint license) |
| **Note** | Nature Computational Science published this 2025-12-09; the arXiv preprint (2504.05559) predates it by several months, which is why the date here differs from the original catalogue entry. No numeric benchmark results were available in the fetched abstract; the full text is paywalled. |

</details>

## Tools

AI tools the team uses for research and literature work. Not papers/models — utilities.

| Name | Description | Links |
| --- | --- | --- |
| EvoScientist | Full-purpose AI research tool: conducts literature review, hypothesis generation and experimentation refinement, and outputs a full paper. | [code](https://github.com/EvoScientist/EvoScientist) |
| PaperOrchestra | Automated AI research-paper writer, implemented as a skill (benchmark + autoraters) that runs on top of any coding agent (Claude Code, Cursor, Antigravity, Cline, Aider). No API keys or LLM SDKs required. | [code](https://github.com/Ar9av/PaperOrchestra) |
| PaperBanana | Automatic figure generation from a method description and caption. | [code](https://github.com/dwzhu-pku/PaperBanana) · [homepage](https://dwzhu-pku.github.io/PaperBanana/) |
| Scite_ | Conversational AI over 280M full-text papers; good for finding and citing real papers, and for summarizing and learning about academic literature. | [homepage](https://scite.ai/home) |
| claude scholar | Agents and skills for tying a codebase to Zotero and Obsidian, for literature-review workflows. | [code](https://github.com/Galaxy-Dawn/claude-scholar) |

---
