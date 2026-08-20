# AI Agents

Agentic, autonomous and tool-using AI systems.

**Maintainer:** @[Meng Wei](https://weimengmeng1999.github.io/meng-wei.github.io/) @[ Feng Lan](https://ai-healthcare-portfolio.hushed-dove-3131.chatgpt.site)

**Deep-read Paper Cards:** [Nature-style English cards for all 27 entries](https://github.com/Lan-Feng-1010/AwesomeBiomedicalAI/tree/add-ai-agent-paper-cards/paper_cards)

**27 entries** · [Back to index](README.md)

| Date | Model | Venue | Pre-training | Data usage | Downstream tasks |
| --- | --- | --- | --- | --- | --- |
| 2026-07 | [Multi-Agent Architectures](#model-multi-agent-architectures-202607) | Nat. Mach. Intell. | N/A | 6 benchmarks (eval) | benchmarking, agent coordination |
| 2026-07 | [Biomni](#model-biomni-202607) | Science | RL fine-tuning, training-free tool use | agent trajectories (train); 433 instances (eval) | CRISPR planning, scRNA-seq annotation, ADMET prediction +2 |
| 2026-07 | [AI X-ray Scientist](#model-ai-x-ray-scientist-202607) | Nat. Mach. Intell. | training-free | — | X-ray sample alignment, closed-loop experimentation |
| 2026-06 | [MIRA](#model-mira-202606) | Nature | training-free | 500+ ED cases (eval) | history-taking, diagnosis, treatment planning +2 |
| 2026-06 | [AMIE](#model-amie-202606) | Nature | training-free | RxQA + 100 cases (eval) | disease management reasoning, medication selection |
| 2026-05 | [Co-Scientist](#model-co-scientist-202605) | Nature | test-time compute scaling | — | hypothesis generation, research proposals |
| 2026-05 | [Robin](#model-robin-202605) | Nature | training-free | — | hypothesis generation, assay selection, candidate proposal +1 |
| 2026-05 | [ERA](#model-era-202605) | Nature | tree search | — | bioinformatics method discovery, epidemiological forecasting |
| 2026-05 | [CIPHER](#model-cipher-202605) | Nat. Commun. | N/A | — | process monitoring, autonomous machine control |
| 2026-05 | [Autonomous Interaction](#model-autonomous-interaction-202605) | Nat. Commun. | N/A | — | multi-robot task negotiation, dynamic team coordination |
| 2026-04 | [AlphaLab](#model-alphalab-202604) | Preprint | N/A | — | general research automation |
| 2026-04 | [SPARK](#model-spark-202604) | Nat. Med. | training-free (agent); pretrained preprocessing models | 5.4K patients (eval) | biomarker discovery, risk stratification, spatial biology +2 |
| 2026-04 | [PhenoAssistant](#model-phenoassistant-202604) | Nat. Commun. | training-free | — | phenotype extraction, data visualization, model training |
| 2026-03 | [BioMedAgent](#model-biomedagent-202603) | Nat. Biomed. Eng. | N/A | — | bioinformatics analysis |
| 2026-03 | [AI Scientist](#model-ai-scientist-202603) | Nature | N/A | — | general research automation |
| 2026-02 | [PantheonOS](#model-pantheonos-202602) | bioRxiv | RL; integrated scFM pretraining (generative, masked gene prediction) | CELLxGENE subset (train) | gene panel design, signaling pathway mapping |
| 2026-02 | [DeepRare](#model-deeprare-202602) | Nature | training-free | 9 datasets, 2.9K diseases (eval) | rare disease diagnosis, traceable reasoning |
| 2026-01 | [PHIA](#model-phia-202601) | Nat. Commun. | N/A | 30K users, synthetic (eval) | wearable-data QA, anomaly detection |
| 2026-01 | [BioDSA](#model-biodsa-202601) | Nat. Biomed. Eng. | N/A | — | biomedical data science analysis |
| 2025-12 | [SciSciGPT](#model-sciscigpt-202512) | Nat. Comput. Sci. | training-free | — | literature analysis, science-of-science workflows |
| 2025-12 | [CASSIA](#model-cassia-202512) | Nat. Commun. | training-free | 970+ cell populations (eval) | cell type annotation, quality control |
| 2025-10 | [AILA](#model-aila-202510) | Nat. Commun. | N/A | 100 AFM tasks (eval) | AFM calibration, mechanical property measurement +2 |
| 2025-10 | [AgentMD](#model-agentmd-202510) | Nat. Commun. | training-free | RiskQA + 698 ED notes (eval) | clinical risk calculator curation, risk prediction |
| 2025-09 | [MAP](#model-map-202509) | Nat. Commun. | training-free | PlanBench + planning tasks (eval) | multi-step planning, task decomposition |
| 2025-08 | [SciToolAgent](#model-scitoolagent-202508) | Nat. Comput. Sci. | training-free | — | multi-tool scientific workflow orchestration |
| 2025-07 | [Virtual Lab](#model-virtual-lab-202507) | Nature | training-free | — | nanobody design, binding-profile evaluation |
| 2025-06 | [Oncology AI Agent](#model-oncology-ai-agent-202506) | Nat. Cancer | training-free (agent); pretrained tool models | 20 patient cases (eval) | oncology decision support, tool selection +1 |

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

<a id="model-ai-x-ray-scientist-202607"></a>
<details>
<summary><b>AI X-ray Scientist</b> — An agentic artificially intelligent X-ray scientist <i>(Nat. Mach. Intell. 2026-07)</i></summary>

**[An agentic artificially intelligent X-ray scientist](https://www.nature.com/articles/s42256-026-01261-5)**

*Nat. Mach. Intell.* · 2026-07 · [Zhantao Chen](https://scholar.google.com/citations?user=s_qynKoAAAAJ&hl=en) & [Arun Bansil](https://scholar.google.com/citations?user=SM8HyJ8AAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM-based agent using structured tool use via the Model Context Protocol (MCP), developed on a virtual six-circle-diffractometer beamline simulator before deployment on a real synchrotron beamline |
| **Pre-training** | `training-free`<br>No new model trained; existing LLM guided via MCP tool-calling over experimental-control tools. |
| **Data usage** | —; validated via the virtual beamline simulator and real-beamline deployment rather than a training dataset. |
| **Downstream tasks** | `X-ray sample alignment`, `closed-loop experimentation`<br>Autonomously plans actions, executes instrument commands (motor scans, detector capture), interprets observations and iterates to align single-crystal samples at an operational synchrotron beamline — a first step toward self-driving labs. |
| **Modalities** | `text`, `detector images`, `instrument control` |

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

<a id="model-amie-202606"></a>
<details>
<summary><b>AMIE</b> — Towards conversational artificial intelligence for disease management <i>(Nature 2026-06)</i></summary>

**[Towards conversational artificial intelligence for disease management](https://www.nature.com/articles/s41586-026-10764-5)**

*Nature* · 2026-06 · [Anil Palepu](https://research.google/people/anilpalepu/) & [Mike Schaekermann](https://scholar.google.com/citations?hl=en&user=mwj_ldQAAAAJ)

| | |
| --- | --- |
| **Backbone** | LLM-based agentic system built on Gemini's long-context capabilities, combining in-context retrieval with structured reasoning |
| **Pre-training** | `training-free`<br>No fine-tuning; grounds reasoning in clinical guidelines and drug formularies via in-context retrieval over the base Gemini model. |
| **Data usage** | RxQA, a multiple-choice medication-reasoning benchmark derived from US/UK drug formularies; 100 multi-visit case scenarios aligned with UK NICE Guidance and BMJ Best Practice (eval). |
| **Downstream tasks** | `disease management reasoning`, `medication selection`<br>Multi-visit clinical management dialogue: investigation selection, medication prescribing, and guideline-aligned reasoning; non-inferior to 21 primary care physicians in a blinded OSCE study. |
| **Modalities** | `text` |

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

<a id="model-cipher-202605"></a>
<details>
<summary><b>CIPHER</b> — Hybrid reasoning for perception, explanation, and autonomous action in manufacturing <i>(Nat. Commun. 2026-05)</i></summary>

**[Hybrid reasoning for perception, explanation, and autonomous action in manufacturing](https://www.nature.com/articles/s41467-026-72378-9)**

*Nat. Commun.* · 2026-05 · Christos Margadji & [Sebastian W. Pattinson](https://scholar.google.com/citations?user=I8dpTJMAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Vision-language-action (VLA) model (CIPHER: Control and Interpretation of Production via Hybrid Expertise and Reasoning) integrated with a process-expert regression model and retrieval-augmented generation, instantiated on a commercial-grade 3D printer |
| **Pre-training** | `N/A`<br>Methods beyond the abstract are paywalled; training details of the process-expert regression component could not be confirmed from accessible sources. |
| **Data usage** | —; no specific dataset confirmed from the accessible abstract. |
| **Downstream tasks** | `process monitoring`, `autonomous machine control`<br>Interprets visual/textual process-monitoring inputs, explains its decisions, and autonomously generates precise machine instructions without requiring explicit annotations. |
| **Modalities** | `image`, `text` |

</details>

<a id="model-autonomous-interaction-202605"></a>
<details>
<summary><b>Autonomous Interaction</b> — Proactive collaboration via autonomous interaction <i>(Nat. Commun. 2026-05)</i></summary>

**[Proactive collaboration via autonomous interaction](https://www.nature.com/articles/s41467-026-72797-8)**

*Nat. Commun.* · 2026-05 · Author list not accessible (paywalled article; no preprint or press coverage naming authors was found)

| | |
| --- | --- |
| **Backbone** | Multi-robot team framework contrasting Fixed, Responsive and Proactive Collaboration paradigms; agents use need-driven multi-round communication to negotiate task allocation |
| **Pre-training** | `N/A`<br>Not confirmed from accessible sources (paywalled beyond the abstract). |
| **Data usage** | —; evaluated via real-world and simulated multi-robot tasks. |
| **Downstream tasks** | `multi-robot task negotiation`, `dynamic team coordination`<br>Teams autonomously recruit or release members as tasks evolve, anticipating needs and reorganizing preemptively rather than only reacting to external intervention. |
| **Modalities** | `text`, `robot control` |

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

<a id="model-phenoassistant-202604"></a>
<details>
<summary><b>PhenoAssistant</b> — A conversational multi-agent AI system for automated plant phenotyping <i>(Nat. Commun. 2026-04)</i></summary>

**[A conversational multi-agent AI system for automated plant phenotyping](https://www.nature.com/articles/s41467-026-71090-y)**

*Nat. Commun.* · 2026-04 · Feng Chen & [Sotirios A. Tsaftaris](https://scholar.google.com/citations?user=jC1uFnYAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Centralized multi-agent system: a single LLM-orchestrated manager coordinating specialized tool-agents for phenotype extraction, visualization and model training |
| **Pre-training** | `training-free`<br>No new model trained for the agent framework itself; the model-training tool can train downstream phenotyping models on demand as one of its callable tools. |
| **Data usage** | —; specific evaluation datasets not detailed in accessible sources. |
| **Downstream tasks** | `phenotype extraction`, `data visualization`, `model training`<br>Natural-language-driven plant phenotyping: automated phenotype extraction, data visualization, and automated training of downstream phenotyping models. |
| **Modalities** | `image`, `text` |
| **Code** | [github.com/vios-s/PhenoAssistant](https://github.com/vios-s/PhenoAssistant) |

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

<a id="model-deeprare-202602"></a>
<details>
<summary><b>DeepRare</b> — An agentic system for rare disease diagnosis with traceable reasoning <i>(Nature 2026-02)</i></summary>

**[An agentic system for rare disease diagnosis with traceable reasoning](https://www.nature.com/articles/s41586-025-10097-9)**

*Nature* · 2026-02 · [Weike Zhao](https://scholar.google.com/citations?user=yFSlxpwAAAAJ&hl=en) & [Weidi Xie](https://scholar.google.com/citations?user=Vtrqj4gAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM-based multi-agent system integrating 40+ specialized tools and up-to-date knowledge sources for rare disease differential diagnosis |
| **Pre-training** | `training-free`<br>No new model trained; agent framework over an existing LLM backbone. |
| **Data usage** | 9 datasets from literature, case reports and clinical centers across Asia, North America and Europe, spanning 2,919 diseases and 14 specialties (eval). |
| **Downstream tasks** | `rare disease diagnosis`, `traceable reasoning`<br>Processes free-text descriptions, HPO terms and genetic testing results to generate ranked diagnostic hypotheses with evidence-linked, traceable reasoning (95.4% expert agreement); 57.18% Recall@1 on HPO-based tasks and 69.1% on multimodal tests. |
| **Modalities** | `text`, `EHR data` |
| **Code** | [github.com/MAGIC-AI4Med/DeepRare](https://github.com/MAGIC-AI4Med/DeepRare) |

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

<a id="model-sciscigpt-202512"></a>
<details>
<summary><b>SciSciGPT</b> — SciSciGPT: advancing human–AI collaboration in the science of science <i>(Nat. Comput. Sci. 2025-12)</i></summary>

**[SciSciGPT: advancing human–AI collaboration in the science of science](https://www.nature.com/articles/s43588-025-00906-6)**

*Nat. Comput. Sci.* · 2025-12 · Erzhuo Shao & [Dashun Wang](https://scholar.google.com/citations?user=uQJAkBoAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM-orchestrated conversational agent with a web-based chat interface coordinating auditable workflows for literature understanding, data processing, analytics and visualization |
| **Pre-training** | `training-free`<br>No new model trained; agent framework over an existing LLM backbone. |
| **Data usage** | —; used at inference over science-of-science literature and data corpora rather than a fine-tuning dataset. |
| **Downstream tasks** | `literature analysis`, `science-of-science workflows`<br>Iterative human–AI collaboration for data-driven findings: literature understanding, data processing/analytics/visualization, and accelerated idea exploration and prototyping. |
| **Modalities** | `text` |
| **Code** | [github.com/Northwestern-CSSI/SciSciGPT](https://github.com/Northwestern-CSSI/SciSciGPT) |

</details>

<a id="model-cassia-202512"></a>
<details>
<summary><b>CASSIA</b> — CASSIA: a multi-agent large language model for automated and interpretable cell annotation <i>(Nat. Commun. 2025-12)</i></summary>

**[CASSIA: a multi-agent large language model for automated and interpretable cell annotation](https://www.nature.com/articles/s41467-025-67084-x)**

*Nat. Commun.* · 2025-12 · Elliot Xie & [Christina Kendziorski](https://scholar.google.com/citations?user=KRVBkHsAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Five-agent LLM framework (annotation, validation, formatting, quality scoring, reporting), with optional RAG, subclustering and uncertainty-quantification agents |
| **Pre-training** | `training-free`<br>No new model trained; agent framework over existing LLMs. |
| **Data usage** | >970 cell populations across benchmark single-cell RNA-seq datasets (eval). |
| **Downstream tasks** | `cell type annotation`, `quality control`<br>Reference-free, automated and interpretable single-cell RNA-seq cell-type annotation, with quality scoring and uncertainty assessment of annotations. |
| **Modalities** | `text`, `omics data` |
| **Code** | [github.com/ElliotXie/CASSIA](https://github.com/ElliotXie/CASSIA) |

</details>

<a id="model-agentmd-202510"></a>
<details>
<summary><b>AgentMD</b> — AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning <i>(Nat. Commun. 2025-10)</i></summary>

**[AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning](https://www.nature.com/articles/s41467-025-64430-x)**

*Nat. Commun.* · 2025-10 · [Qiao Jin](https://scholar.google.com/citations?user=tYy-bzgAAAAJ&hl=en) & [Zhiyong Lu](https://scholar.google.com/citations?user=lJAkLo8AAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | LLM tool-builder/tool-user agent that curates and applies clinical risk calculators over a base LLM |
| **Pre-training** | `training-free`<br>No fine-tuning; agent autonomously curates a calculator library and selects/applies tools over the base LLM (compared against a GPT-4 chain-of-thought baseline). |
| **Data usage** | RiskCalcs, a library of 2,164 clinical calculators curated from PubMed; RiskQA benchmark; 698 real-world emergency department notes (eval). |
| **Downstream tasks** | `clinical risk calculator curation`, `risk prediction`<br>Automated construction of a clinical-calculator tool library and autonomous selection/application of the relevant calculator for individual patients; 87.7% vs. 40.9% accuracy over GPT-4 chain-of-thought on RiskQA. |
| **Modalities** | `text`, `EHR data` |

</details>

<a id="model-map-202509"></a>
<details>
<summary><b>MAP</b> — A brain-inspired agentic architecture to improve planning with LLMs <i>(Nat. Commun. 2025-09)</i></summary>

**[A brain-inspired agentic architecture to improve planning with LLMs](https://www.nature.com/articles/s41467-025-63804-5)**

*Nat. Commun.* · 2025-09 · [Taylor Webb](https://scholar.google.com/citations?user=WCmrJoQAAAAJ&hl=en) & [Ida Momennejad](https://scholar.google.com/citations?user=OFdUAJwAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Modular Agentic Planner (MAP): brain-inspired modular LLM architecture with separate conflict-monitoring, state-prediction, state-evaluation, task-decomposition and task-coordination modules |
| **Pre-training** | `training-free`<br>Modules are implemented via prompted LLM calls; no new weights trained. |
| **Data usage** | Graph traversal, Tower of Hanoi, PlanBench, and an NLP multi-step reasoning task (eval). |
| **Downstream tasks** | `multi-step planning`, `task decomposition`<br>Goal-directed multi-step planning via interaction of specialized brain-inspired modules, addressing LLMs' typical struggles with multi-step reasoning and planning. |
| **Modalities** | `text` |

</details>

<a id="model-scitoolagent-202508"></a>
<details>
<summary><b>SciToolAgent</b> — SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration <i>(Nat. Comput. Sci. 2025-08)</i></summary>

**[SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration](https://www.nature.com/articles/s43588-025-00849-y)**

*Nat. Comput. Sci.* · 2025-08 · Keyan Ding & Huajun Chen

| | |
| --- | --- |
| **Backbone** | LLM agent orchestrating 500+ scientific tools (web APIs, ML models, Python functions, knowledge databases) via a scientific-tool knowledge graph and graph-based retrieval-augmented generation, with a safety-checking module |
| **Pre-training** | `training-free`<br>No new model trained; tool selection and execution via knowledge-graph retrieval over an existing LLM. |
| **Data usage** | —; tool knowledge graph spans biology, chemistry and materials science. |
| **Downstream tasks** | `multi-tool scientific workflow orchestration`<br>Automated selection, composition and execution of hundreds of scientific tools across biology, chemistry and materials science research workflows. |
| **Modalities** | `text`, `code` |
| **Code** | [github.com/HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent) |

</details>

<a id="model-virtual-lab-202507"></a>
<details>
<summary><b>Virtual Lab</b> — The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies <i>(Nature 2025-07)</i></summary>

**[The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies](https://www.nature.com/articles/s41586-025-09442-9)**

*Nature* · 2025-07 · [Kyle Swanson](https://scholar.google.com/citations?user=seqcYSUAAAAJ&hl=en) & [James Zou](https://scholar.google.com/citations?user=23ZXZvEAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | An LLM Principal-Investigator agent leading a team of LLM scientist agents through iterative research meetings, with a human researcher providing high-level feedback; computational pipeline combining ESM, AlphaFold-Multimer and Rosetta |
| **Pre-training** | `training-free`<br>No new model trained for the agent framework; uses pretrained ESM, AlphaFold-Multimer and Rosetta models as tools. |
| **Data usage** | —; designed and experimentally validated 92 nanobodies against SARS-CoV-2 variants. |
| **Downstream tasks** | `nanobody design`, `binding-profile evaluation`<br>AI–human collaborative nanobody design against SARS-CoV-2, including variants with improved binding to JN.1/KP.3 while retaining ancestral-spike binding. |
| **Modalities** | `text`, `protein structure` |
| **Code** | [github.com/zou-group/virtual-lab](https://github.com/zou-group/virtual-lab) |

</details>

<a id="model-oncology-ai-agent-202506"></a>
<details>
<summary><b>Oncology AI Agent</b> — Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology <i>(Nat. Cancer 2025-06)</i></summary>

**[Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology](https://www.nature.com/articles/s43018-025-00991-6)**

*Nat. Cancer* · 2025-06 · [Dyke Ferber](https://scholar.google.com/citations?user=r7JtdUcAAAAJ&hl=en) & [Jakob Nikolas Kather](https://scholar.google.com/citations?user=w6-uFdEAAAAJ&hl=en)

| | |
| --- | --- |
| **Backbone** | Autonomous clinical AI agent built on GPT-4 with multimodal precision-oncology tools: vision transformers for MSI/KRAS/BRAF detection from histopathology, MedSAM for radiological image segmentation, and web tools (OncoKB, PubMed, Google) |
| **Pre-training** | `training-free` (agent), `pretrained tool models`<br>The agent itself is training-free tool-use over GPT-4; the vision-transformer and MedSAM tools were previously trained elsewhere. |
| **Data usage** | 20 realistic multimodal patient cases (eval). |
| **Downstream tasks** | `oncology decision support`, `tool selection`, `guideline citation`<br>Autonomous multimodal precision-oncology decision-making: 87.5% correct tool use, 91.0% correct clinical conclusions, 75.5% accurate guideline citation; improved decision accuracy from 30.3% (GPT-4 alone) to 87.2%. |
| **Modalities** | `text`, `histopathology`, `image` |

</details>
