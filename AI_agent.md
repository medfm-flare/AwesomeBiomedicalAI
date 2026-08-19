# AI Agents

Agentic, autonomous and tool-using AI systems.

**Maintainer:** @[Meng Wei](https://weimengmeng1999.github.io/meng-wei.github.io/)

**Notebook:** [NotebookLM](https://notebook.google.com/notebook/b25c668a-4926-45b8-bca3-329885628a36)

**14 entries** · [Back to index](README.md)

| Date | Model | Venue | Pre-training | Data usage | Downstream tasks |
| --- | --- | --- | --- | --- | --- |
| 2026-07 | [Multi-Agent Architectures](#model-multi-agent-architectures-202607) | Nat. Mach. Intell. | N/A | 6 benchmarks (eval) | benchmarking, agent coordination |
| 2026-07 | [Biomni](#model-biomni-202607) | Science | RL fine-tuning, training-free tool use | agent trajectories (train); 433 instances (eval) | CRISPR planning, scRNA-seq annotation, ADMET prediction +2 |
| 2026-06 | [MIRA](#model-mira-202606) | Nature | training-free | 500+ ED cases (eval) | history-taking, diagnosis, treatment planning +2 |
| 2026-05 | [Co-Scientist](#model-co-scientist-202605) | Nature | test-time compute scaling | — | hypothesis generation, research proposals |
| 2026-05 | [Robin](#model-robin-202605) | Nature | training-free | — | hypothesis generation, assay selection, candidate proposal +1 |
| 2026-05 | [ERA](#model-era-202605) | Nature | tree search | — | bioinformatics method discovery, epidemiological forecasting |
| 2026-04 | [AlphaLab](#model-alphalab-202604) | Preprint | N/A | — | general research automation |
| 2026-04 | [SPARK](#model-spark-202604) | Nat. Med. | training-free (agent); pretrained preprocessing models | 5.4K patients (eval) | biomarker discovery, risk stratification, spatial biology +2 |
| 2026-03 | [BioMedAgent](#model-biomedagent-202603) | Nat. Biomed. Eng. | N/A | — | bioinformatics analysis |
| 2026-03 | [AI Scientist](#model-ai-scientist-202603) | Nature | N/A | — | general research automation |
| 2026-02 | [PantheonOS](#model-pantheonos-202602) | bioRxiv | RL; integrated scFM pretraining (generative, masked gene prediction) | CELLxGENE subset (train) | gene panel design, signaling pathway mapping |
| 2026-01 | [PHIA](#model-phia-202601) | Nat. Commun. | N/A | 30K users, synthetic (eval) | wearable-data QA, anomaly detection |
| 2026-01 | [BioDSA](#model-biodsa-202601) | Nat. Biomed. Eng. | N/A | — | biomedical data science analysis |
| 2025-10 | [AILA](#model-aila-202510) | Nat. Commun. | N/A | 100 AFM tasks (eval) | AFM calibration, mechanical property measurement +2 |

## Details

Click a model to expand its record.

<a id="model-multi-agent-architectures-202607"></a>
<details>
<summary><b>Multi-Agent Architectures</b> — Capable language models can outgrow the benefits of collaboration <i>(Nat. Mach. Intell. 2026-07)</i></summary>

**[Capable language models can outgrow the benefits of collaboration](https://www.nature.com/articles/s42256-026-01268-y)**

*Nat. Mach. Intell.* · 2026-07 · [Yubin Kim](https://scholar.google.com/citations?user=tYK2WmQAAAAJ&hl=en) & [Xin Liu](https://scholar.google.com/citations?user=p9F83HoAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Single-agent vs. multi-agent architectures (independent, centralized, decentralized and hybrid coordination), instantiated with OpenAI, Google Gemini and Anthropic frontier LLMs across capability tiers |
| **Pre-training** | `N/A`<br>No new models trained; a comparative study of coordination architectures across LLM capability tiers. |
| **Data usage** | N/A; evaluated on six agentic benchmarks: BrowseComp-Plus, Finance Agent, PlanCraft, WorkBench, SWE-bench Verified, Terminal-Bench. |
| **Downstream tasks** | `benchmarking`, `agent coordination`<br>Shows that multi-agent collaboration's benefit is task-contingent and shrinks as base-model capability grows: large gains on parallelizable tasks (e.g., finance) but degraded performance on sequential tasks (e.g., planning) once models are sufficiently capable. |
| **Modalities** | `text` |

</details>

<a id="model-biomni-202607"></a>
<details>
<summary><b>Biomni</b> — Autonomous biomedical research with an artificial intelligence agent <i>(Science 2026-07)</i></summary>

**[Autonomous biomedical research with an artificial intelligence agent](https://www.science.org/doi/10.1126/science.adz4351)**

*Science* · 2026-07 · [Kexin Huang](https://scholar.google.com/citations?user=ogEXTOgAAAAJ&hl=en) & [Jure Leskovec](https://scholar.google.com/citations?hl=en&user=Q_kKkIUAAAAJ)

| | |
| --- | --- |
| **Backbone** | Configurable LLM agent (supports Claude, GPT, Gemini and other providers); Biomni-R0, a dedicated reasoning model for biology, is built on Qwen-32B |
| **Pre-training** | `RL fine-tuning`, `training-free tool use`<br>Biomni-R0 is fine-tuned via reinforcement learning from agent interaction data; the base Biomni agent is training-free tool use over a configurable LLM backbone. |
| **Data usage** | RL training data from agent interaction trajectories; evaluated on Biomni-Eval1 (433 instances spanning 10 biological reasoning tasks). |
| **Downstream tasks** | `CRISPR screen planning`, `scRNA-seq annotation`, `ADMET prediction`, `GWAS analysis`, `rare disease diagnosis`, `lab-bench QA`<br>CRISPR screen planning and gene identification, scRNA-seq annotation and hypothesis generation, ADMET property prediction, GWAS analysis and variant prioritization, rare disease diagnosis, and lab-bench Q&A. |
| **Modalities** | `text`, `omics data` |
| **Code** | [github.com/snap-stanford/biomni](https://github.com/snap-stanford/biomni) |

</details>

<a id="model-mira-202606"></a>
<details>
<summary><b>MIRA</b> — Towards autonomous medical artificial intelligence agents <i>(Nature 2026-06)</i></summary>

**[Towards autonomous medical artificial intelligence agents](https://www.nature.com/articles/s41586-026-10675-5)**

*Nature* · 2026-06 · [Dyke Ferber](https://scholar.google.com/citations?user=r7JtdUcAAAAJ&hl=en) & [Jakob Nikolas Kather](https://scholar.google.com/citations?user=w6-uFdEAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM-based autonomous agent with 11 tools, operating in a sandboxed, FHIR-compliant EHR environment (ICD, LOINC, ATC, NDC, RxNorm, SNOMED-CT coding) |
| **Pre-training** | `training-free`<br>No new model trained; MIRA (Medical Intelligence for Reasoning and Action) is an agent framework over an existing LLM backbone. |
| **Data usage** | N/A; evaluated on >500 MIMIC-IV emergency department cases spanning 8 diagnoses. |
| **Downstream tasks** | `history-taking`, `diagnosis`, `treatment planning`, `medication prescribing`, `admission decisions`<br>Autonomous EHR-integrated clinical decision-making: history-taking via patient-agent dialogue, ordering/interpreting labs, imaging and microbiology tests, differential diagnosis generation, treatment planning, medication prescribing, procedure scheduling and admission decisions. |
| **Modalities** | `text`, `EHR data` |
| **Code** | [github.com/Dyke-F/MIRA](https://github.com/Dyke-F/MIRA/tree/main/src) |
| **Replication** | [github.com/weimengmeng1999/MIRA](https://github.com/weimengmeng1999/MIRA) |

</details>

<a id="model-co-scientist-202605"></a>
<details>
<summary><b>Co-Scientist</b> — Accelerating scientific discovery with Co-Scientist <i>(Nature 2026-05)</i></summary>

**[Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)**

*Nature* · 2026-05 · [Juraj Gottweis](https://scholar.google.com/citations?user=jVRSR5AAAAAJ&hl=en) & [Vivek Natarajan](https://scholar.google.com/citations?user=gZiW7IAAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Multi-agent system built on Gemini; specialized agents (Generation, Reflection, Ranking, Evolution, Proximity, Meta-review) coordinated by a Supervisor agent with an asynchronous task-execution framework |
| **Pre-training** | `test-time compute scaling`<br>Built on pretrained Gemini; uses tournament-based self-improving hypothesis evolution rather than additional model training. |
| **Data usage** | N/A; grounded via literature search, simulation review and web/tool use — no fine-tuning dataset. |
| **Downstream tasks** | `hypothesis generation`, `research proposals`<br>Automated scientific hypothesis generation and research-proposal formulation; validated with in vitro experiments in drug-repurposing candidate discovery for AML, synergistic combination-therapy discovery, epigenetic target identification for liver fibrosis, and explaining bacterial gene-transfer mechanisms relevant to antimicrobial resistance. |
| **Modalities** | `text` |

</details>

<a id="model-robin-202605"></a>
<details>
<summary><b>Robin</b> — A multi-agent system for automating scientific discovery <i>(Nature 2026-05)</i></summary>

**[A multi-agent system for automating scientific discovery](https://www.nature.com/articles/s41586-026-10652-y)**

*Nature* · 2026-05 · [Ali E. Ghareeb](https://scholar.google.com/citations?hl=en&user=dlWmbncAAAAJ) & [Samuel G. Rodriques](https://scholar.google.com/citations?user=yGKwWGEAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Multi-agent LLM system orchestrating Crow (concise literature review), Falcon (deep literature synthesis for candidate evaluation) and Finch (autonomous bioinformatic data analysis) sub-agents |
| **Pre-training** | `training-free`<br>Agents use LLM reasoning and tool use rather than new model training. |
| **Data usage** | N/A; validated via a lab-in-the-loop experimental workflow on dry age-related macular degeneration (dAMD). |
| **Downstream tasks** | `hypothesis generation`, `assay selection`, `candidate proposal`, `data interpretation`<br>Autonomous hypothesis generation, experimental assay selection, therapeutic candidate proposal, interpretation of experimental (RNA-seq) data, and iterative hypothesis refinement; identified and validated ripasudil and KL001 as RPE-phagocytosis-enhancing dAMD candidates and discovered ABCA1 upregulation as a follow-on target. |
| **Modalities** | `text`, `omics data` |
| **Code** | [github.com/Future-House/robin](https://github.com/Future-House/robin) |

</details>

<a id="model-era-202605"></a>
<details>
<summary><b>ERA</b> — An AI system to help scientists write expert-level empirical software <i>(Nature 2026-05)</i></summary>

**[An AI system to help scientists write expert-level empirical software](https://www.nature.com/articles/s41586-026-10658-6)**

*Nature* · 2026-05 · [Eser Aygün (Google DeepMind)](https://scholar.google.com/citations?user=mogd5nkAAAAJ&hl=en) & [Michael Brenner (Google DeepMind)](https://scholar.google.com/citations?user=ZDL6ITwAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM agent (ERA, Empirical Research Assistance) |
| **Pre-training** | `tree search`<br>Uses tree search over generated programs rather than additional model training. |
| **Data usage** | N/A |
| **Downstream tasks** | `bioinformatics method discovery`, `epidemiological forecasting`<br>In bioinformatics, ERA discovered 40 novel methods for single-cell data analysis that outperformed the top human-developed methods on a public leaderboard. In epidemiology, ERA generated 14 models that outperformed the CDC ensemble and all other individual models for forecasting COVID-19 hospitalizations. |
| **Modalities** | `text`, `code` |
| **Code** | [github.com/google-research/era](https://github.com/google-research/era) |

</details>

<a id="model-alphalab-202604"></a>
<details>
<summary><b>AlphaLab</b> — AlphaLab: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs <i>(Preprint 2026-04)</i></summary>

**[AlphaLab: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs](https://brendanhogan.github.io/alphalab-paper/)**

*Preprint* · 2026-04 · [Brendan R. Hogan](https://scholar.google.com/citations?user=7Ha1788AAAAJ&hl=en) & [Yuriy Nevmyvaka](https://scholar.google.com/citations?user=Hui4EIcAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Multiagent LLM |
| **Pre-training** | `N/A` |
| **Data usage** | N/A |
| **Downstream tasks** | `general research automation`<br>General research across optimization domains. |
| **Modalities** | `text` |
| **Code** | [github.com/morganstanley/MSML](https://github.com/morganstanley/MSML/tree/main/projects/alpha-lab) |

</details>

<a id="model-spark-202604"></a>
<details>
<summary><b>SPARK</b> — An agentic framework for autonomous scientific discovery in cancer pathology <i>(Nat. Med. 2026-04)</i></summary>

**[An agentic framework for autonomous scientific discovery in cancer pathology](https://www.nature.com/articles/s41591-026-04357-y)**

*Nat. Med.* · 2026-04 · [Florian Trost](https://scholar.google.com/citations?user=GQnzSMoAAAAJ&hl=de), co-first with Bide Zhang & [Yuri Tolkach](https://scholar.google.com/citations?hl=en&user=bshxyrcAAAAJ&utm_source=chatgpt.com)

| | |
| --- | --- |
| **Backbone** | Agentic LLM workflow using OpenAI o1 for idea generation, OpenAI o3-mini for review / duplicate detection, and Claude Sonnet 3.5 for coding. WSI preprocessing uses GrandQC, organ-specific UNet++ / EfficientNet tissue segmentation, and HoverNext with convnextv2_large for single-cell detection and classification. |
| **Pre-training** | `training-free` (agent), `pretrained preprocessing models`<br>SPARK (System of Pathology Agents for Research and Knowledge) itself is training-free for pathology concept generation and parameter coding, using LLM reasoning and tool-building rather than training a new image model. The preprocessing models were previously trained, including a single-cell model trained on 1,272,506 manually annotated cells. |
| **Data usage** | No SPARK-specific image training set. Evaluation used >5,400 patients across 18 H&E histopathology cohorts and a METABRIC spatial biology breast cancer dataset with 625 primary tumors. |
| **Downstream tasks** | `biomarker discovery`, `risk stratification`, `spatial biology analysis`, `hypothesis generation`<br>Autonomous pathology concept generation, coded parameter generation, prognostic biomarker discovery, predictive biomarker analysis, risk stratification, PD-L1 / MSI / HPV / ER-related analyses, spatial biology analysis, tumor progression / temporal evolution hypothesis generation. |
| **Modalities** | `histopathology`, `text` |
| **Code** | [github.com/cpath-ukk/SPARK](https://github.com/cpath-ukk/SPARK) |

</details>

<a id="model-biomedagent-202603"></a>
<details>
<summary><b>BioMedAgent</b> — Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses <i>(Nat. Biomed. Eng. 2026-03)</i></summary>

**[Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses](https://www.nature.com/articles/s41551-026-01634-6)**

*Nat. Biomed. Eng.* · 2026-03 · [Dechao Bu](https://orcid.org/0000-0002-8833-5432) & [Yi Zhao](https://orcid.org/0000-0001-6046-8420)

| | |
| --- | --- |
| **Backbone** | Multiagent LLM |
| **Pre-training** | `N/A` |
| **Data usage** | N/A |
| **Downstream tasks** | `bioinformatics analysis`<br>Self-evolving, tool-aware biomedical data analysis. |
| **Modalities** | `text`, `omics data` |
| **Code** | [github.com/BOBQWERA/BioMedAgent](https://github.com/BOBQWERA/BioMedAgent) |

</details>

<a id="model-ai-scientist-202603"></a>
<details>
<summary><b>AI Scientist</b> — Towards end-to-end automation of AI research <i>(Nature 2026-03)</i></summary>

**[Towards end-to-end automation of AI research](https://www.nature.com/articles/s41586-026-10265-5)**

*Nature* · 2026-03 · [Chris Lu](https://scholar.google.com/citations?user=4WLoIRsAAAAJ&hl=en) & [Jeff Clune](https://scholar.google.com/citations?hl=en&user=5TZ7f5wAAAAJ&view_op=list_works&sortby=pubdate)

| | |
| --- | --- |
| **Backbone** | Multiagent LLM |
| **Pre-training** | `N/A` |
| **Data usage** | N/A |
| **Downstream tasks** | `general research automation`<br>End-to-end automation of the AI research pipeline. |
| **Modalities** | `text`, `code` |
| **Code** | [github.com/SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist?tab=readme-ov-file) |

</details>

<a id="model-pantheonos-202602"></a>
<details>
<summary><b>PantheonOS</b> — PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery <i>(bioRxiv 2026-02)</i></summary>

**[PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery](https://www.biorxiv.org/content/10.64898/2026.02.26.707870v1.full.pdf)**

*bioRxiv* · 2026-02 · [Weize Xu](https://scholar.google.com/citations?user=rHdkQ-cAAAAJ&hl=en) & [Xiaojie Qiu](https://scholar.google.com/citations?user=XlMd8TAAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM with a reinforcement-learning module routing to 22 integrated single-cell foundation models (scFMs) |
| **Pre-training** | `RL`, `generative pre-training (scGPT)`, `masked gene prediction (scBERT)`<br>The router's LLM/RL layer is trained via reinforcement learning; the 22 integrated scFMs use diverse pretraining methods, including generative pre-training (scGPT), BERT-style masked gene prediction (scBERT), and tabular self-supervised learning. |
| **Data usage** | Subsets of the CELLxGENE dataset. |
| **Downstream tasks** | `gene panel design`, `signaling pathway mapping`<br>Gene panel design, mapping molecular and signaling events, such as Cer1–Nodal inhibition, in embryonic development. |
| **Modalities** | `omics data`, `text` |
| **Code** | [github.com/aristoteleo/PantheonOS](https://github.com/aristoteleo/PantheonOS) |

</details>

<a id="model-phia-202601"></a>
<details>
<summary><b>PHIA</b> — Transforming wearable data into personal health insights using large language model agents <i>(Nat. Commun. 2026-01)</i></summary>

**[Transforming wearable data into personal health insights using large language model agents](https://www.nature.com/articles/s41467-025-67922-y)**

*Nat. Commun.* · 2026-01 · [Mike A. Merrill](https://scholar.google.com/citations?user=UtBcznsAAAAJ&hl=en) & [Xin Liu](https://scholar.google.com/citations?user=p9F83HoAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | PHIA (Personal Health Insights Agent) built on Gemini 1.0 Ultra |
| **Pre-training** | `N/A`<br>No fine-tuning; agent framework uses code generation plus information retrieval over the base model. |
| **Data usage** | 4,000 objective health queries, 172 open-ended queries, synthetic wearable data from 30,000 real Fitbit/Pixel Watch users. |
| **Downstream tasks** | `wearable-data QA`, `anomaly detection`<br>Answers questions on physical activity, sleep patterns, health correlations, anomaly detection, and population comparisons from wearable data; 84% accuracy on objective queries, 83% favorable rating on open-ended queries. |
| **Modalities** | `wearable sensor data`, `text` |

</details>

<a id="model-biodsa-202601"></a>
<details>
<summary><b>BioDSA</b> — Making large language models reliable data science programming copilots for biomedical research <i>(Nat. Biomed. Eng. 2026-01)</i></summary>

**[Making large language models reliable data science programming copilots for biomedical research](https://www.nature.com/articles/s41551-025-01587-2)**

*Nat. Biomed. Eng.* · 2026-01 · [Zifeng Wang](https://scholar.google.co.uk/citations?user=kMlWwTAAAAAJ&hl=en&oi=sra) & [Jimeng Sun](https://scholar.google.co.uk/citations?user=9jmmp5sAAAAJ&hl=en&oi=ao)

| | |
| --- | --- |
| **Backbone** | Model-agnostic agent framework |
| **Pre-training** | `N/A` |
| **Data usage** | N/A |
| **Downstream tasks** | `biomedical data science analysis`<br>Reliable data science programming copilot for biomedical research. |
| **Modalities** | `text`, `code` |
| **Code** | [github.com/RyanWangZf/BioDSA](https://github.com/RyanWangZf/BioDSA) |

</details>

<a id="model-aila-202510"></a>
<details>
<summary><b>AILA</b> — Evaluating large language model agents for automation of atomic force microscopy <i>(Nat. Commun. 2025-10)</i></summary>

**[Evaluating large language model agents for automation of atomic force microscopy](https://www.nature.com/articles/s41467-025-64105-7)**

*Nat. Commun.* · 2025-10 · [Indrajeet Mandal](https://scholar.google.com/citations?user=v_747TcAAAAJ&hl=en) & [N. M. Anoop Krishnan](https://scholar.google.com/citations?user=fGnjHcEAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | AILA (Artificially Intelligent Lab Assistant), evaluated with GPT-4o, GPT-3.5-turbo, Claude-3.5-Sonnet and Llama-3.3-70B |
| **Pre-training** | `N/A`<br>No new models trained. |
| **Data usage** | AFMBench: 100 expertly curated atomic force microscopy experimental tasks. |
| **Downstream tasks** | `AFM calibration`, `graphene layer analysis`, `mechanical property measurement`, `friction characterization`<br>Autonomous AFM calibration, graphene layer analysis, mechanical property measurement, indentation-mark detection, and load-dependent friction characterization. |
| **Modalities** | `text`, `instrument control` |
| **Code** | [github.com/M3RG-IITD/AILA](https://github.com/M3RG-IITD/AILA) |

</details>
