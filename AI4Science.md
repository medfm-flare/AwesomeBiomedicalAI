<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from pipeline/ai4science/data.json by pipeline/generate.py -->
<!-- Edits made here are overwritten by the next run of the generator. -->

# AI for Science

Scientific discovery, research assistance, chemistry and drug design.

**Maintainer:** [Ryan Khalloqi](https://github.com/ryanwangk)

**12 entries** across 3 categories · [Back to index](README.md)

## Catalogue

### Drug & Molecule Design

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202604 | [DeepDrugDiscovery](#model-deepdrugdiscovery-202604) | Nat. Biomed. Eng. | not stated (VAE+GRU) | ✓ | 2 lead BBB-permeable, mTOR-independent autophagy enhancers; restored memory in AD mouse models |
| 202603 | [AI-guided LNP design (unnamed in paper)](#model-lnp-spatial-ai-202603) | Nat. Biomed. Eng. | N/A — non-neural (SISSO symbolic regression) | — | Lead lipid P1: 14.8x mRNA delivery efficiency vs. clinical-standard ALC-0315 |
| 202606 | [LASErMPNN](#model-lasermpnn-202606) | Nature | not stated (GNN) | ✓ | 5x hit rate, 70x affinity vs. prior SOTA; zero-shot design reached Kd = 1.2 nM |

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
| **Note** | Also catalogued on AI4biology.md (Keishi's page) — kept here too since drug-binding protein design sits squarely in this page's chemistry/drug-design scope; duplicates across pages are fine for now per team discussion. |

**Key results**

- Hit rate and highest-affinity design each surpassed the prior state-of-the-art method by 5-fold and 70-fold respectively.
- Without any experimental input, LASErMPNN suggested two mutations that increased binding affinity by more than two orders of magnitude (Kd = 1.2 ± 0.2 nM).

</details>

### Materials & Physical Science

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202602 | [Discovery Learning](#model-discovery-learning-202602) | Nature | N/A — no single model (learner/interpreter/oracle loop) | ✓ | Predicts full cycle life from ~50 cycles: ~5% of the energy, ~2% of the time of full testing |
| 202501 | [MatterGen](#model-mattergen-202501) | Nature | 46.8M | ✓ | >2x more novel/stable structures than prior baselines; one design (TaCr₂O₆) synthesized |
| 202311 | [GNoME](#model-gnome-202311) | Nature | not stated (GNN) | ✓ | 2.2M candidate crystals, ~380K most stable; 736 independently synthesized externally |

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

### Research Agents & Literature Tools

| Date | Model | Venue | Model size | Open | Headline result |
| --- | --- | --- | --- | --- | --- |
| 202602 | [OpenScholar](#model-openscholar-202602) | Nature | 8B (generator) | ✓ | +5 pts vs. GPT-4o, +7 vs. PaperQA2 on ScholarQABench; preferred over experts 51-70% |
| 202512 | [SciSciGPT](#model-sciscigpt-202512) | Nat. Comput. Sci. | N/A — base LLM undisclosed | ✓ | Automates science-of-science analytical workflows; no benchmark numbers published |
| 202607 | [Co-Scientist](#model-co-scientist-202607) | Nature | N/A — built on Gemini, size undisclosed | — | AML candidate KIRA6 showed an 18x separation between malignant and control cell lines |
| 202603 | [The AI Scientist](#model-ai-scientist-202603) | Nature | N/A — multi-model orchestration | ✓ | Autonomously written manuscript passed peer review at a 70%-acceptance ML workshop |
| 202605 | [ERA (Empirical Research Assistance)](#model-era-202605) | Nature | N/A — base LLM undisclosed | ✓ | 40 SOTA single-cell methods; 14 models beat the CDC's COVID-forecast ensemble |
| 202603 | [BioMedAgent](#model-biomedagent-202603) | Nat. Biomed. Eng. | N/A — base model (GPT-4o-mini), size undisclosed by vendor | ✓ | 100% analysable scope on local tools, vs. a narrower scope for online ChatGPT-4o/GPT Assistants |

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
