# AI Agents

Agentic, autonomous and tool-using AI systems.

**Maintainer:** @[Meng Wei](https://weimengmeng1999.github.io/meng-wei.github.io/) @[ Feng Lan](https://ai-healthcare-portfolio.hushed-dove-3131.chatgpt.site)

**32 entries** · [Back to index](README.md)

| Date | Model | Venue | Pre-training | Data usage | Downstream tasks |
| --- | --- | --- | --- | --- | --- |
| 2026-09 | Quine [[details]](#model-quine-202609) | Microsoft Research | multimodal world-model training; agentic tool use | pancreatic-cancer cell-state and compound data; multiple wet-lab assays (eval) | cancer compound prioritization, experiment planning, closed-loop biological discovery |
| 2026-09 | Claude ART Discovery Agents [[details]](#model-claude-art-discovery-agents-202609) | Anthropic Research | training-free multi-agent orchestration | ~1.9B protein clusters; 949 agent sessions across 119 tasks | genomic mining, reverse-transcriptase discovery, hypothesis generation |
| 2026-09 | Paper2Agent [[details]](#model-paper2agent-202609) | Nature | training-free multi-agent orchestration | AlphaGenome, Scanpy, and TISSUE case studies; original and novel query evaluations | paper-to-MCP conversion, workflow reproduction, scientific queries, cross-paper analysis |
| 2026-09 | MutexaGPT [[details]](#model-mutexagpt-202609) | Nat. Comput. Sci. | training-free multi-agent orchestration | 600 methyltransferase variants (retrospective eval); WT + 10 amylase linker variants (prospective experimental eval) | enzyme variant design, high-throughput molecular simulation, substrate-specificity engineering, cold-adaptation engineering |
| 2026-09 | On-Premise Medical AI Agent [[details]](#model-on-premise-medical-ai-agent-202609) | Nat. Med. | training-free; open-weight LLM comparison | MIRA-v2 (551), CDM (2,400), VivaBench (990) (eval); 181 cases physician-adjudicated | simulated diagnosis, decision-time reliability estimation, selective-autonomy routing |
| 2026-09 | AI-TEC [[details]](#model-ai-tec-202609) | Nat. Med. | local fine-tuning + iterative feedback | 26,839 CFPs (local tuning); 472 + 348 CFPs (prospective eval); early single-center deployment monitoring | pre-consultation, ophthalmic triage, CFP classification, workflow integration |
| 2026-09 | US-Agent [[details]](#model-us-agent-202609) | Nat. Commun. | ultrasound foundation model; task-specific VLM training | 9,189 internal cases (train/test); 1,704 and 108 external cases (eval) | ultrasound finding classification, report generation, cholecystectomy decision support |
| 2026-09 | MoChiAgent [[details]](#model-mochiagent-202609) | Nat. Med. | self-supervised masked-feature pretraining; supervised multi-task fine-tuning | 1.46M maternal/infant participants, 4.40M visits (development); 90.2K participants (external eval); 25 cases + 6 specialists (agent pilot) | maternal and infant disease prediction, biological-age estimation, transgenerational risk stratification, evidence-grounded clinical reporting +1 |
| 2026-07 | Multi-Agent Architectures [[details]](#model-multi-agent-architectures-202607) | Nat. Mach. Intell. | N/A | 6 benchmarks (eval) | benchmarking, agent coordination |
| 2026-07 | AI X-ray Scientist [[details]](#model-ai-x-ray-scientist-202607) | Nat. Mach. Intell. | training-free | — | X-ray sample alignment, closed-loop experimentation |
| 2026-06 | MIRA [[details]](#model-mira-202606) | Nature | training-free | 500+ ED cases (eval) | history-taking, diagnosis, treatment planning +2 |
| 2026-06 | AMIE [[details]](#model-amie-202606) | Nature | training-free | RxQA + 100 cases (eval) | disease management reasoning, medication selection |
| 2026-05 | Co-Scientist [[details]](#model-co-scientist-202605) | Nature | test-time compute scaling | — | hypothesis generation, research proposals |
| 2026-05 | Robin [[details]](#model-robin-202605) | Nature | training-free | — | hypothesis generation, assay selection, candidate proposal +1 |
| 2026-05 | ERA [[details]](#model-era-202605) | Nature | tree search | — | bioinformatics method discovery, epidemiological forecasting |
| 2026-05 | CIPHER [[details]](#model-cipher-202605) | Nat. Commun. | N/A | — | process monitoring, autonomous machine control |
| 2026-05 | Autonomous Interaction [[details]](#model-autonomous-interaction-202605) | Nat. Commun. | N/A | — | multi-robot task negotiation, dynamic team coordination |
| 2026-04 | SPARK [[details]](#model-spark-202604) | Nat. Med. | training-free (agent); pretrained preprocessing models | 5.4K patients (eval) | biomarker discovery, risk stratification, spatial biology +2 |
| 2026-04 | PhenoAssistant [[details]](#model-phenoassistant-202604) | Nat. Commun. | training-free | — | phenotype extraction, data visualization, model training |
| 2026-03 | BioMedAgent [[details]](#model-biomedagent-202603) | Nat. Biomed. Eng. | N/A | — | bioinformatics analysis |
| 2026-03 | AI Scientist [[details]](#model-ai-scientist-202603) | Nature | N/A | — | general research automation |
| 2026-02 | DeepRare [[details]](#model-deeprare-202602) | Nature | training-free | 9 datasets, 2.9K diseases (eval) | rare disease diagnosis, traceable reasoning |
| 2026-01 | PHIA [[details]](#model-phia-202601) | Nat. Commun. | N/A | 30K users, synthetic (eval) | wearable-data QA, anomaly detection |
| 2026-01 | BioDSA [[details]](#model-biodsa-202601) | Nat. Biomed. Eng. | N/A | — | biomedical data science analysis |
| 2025-12 | SciSciGPT [[details]](#model-sciscigpt-202512) | Nat. Comput. Sci. | training-free | — | literature analysis, science-of-science workflows |
| 2025-12 | CASSIA [[details]](#model-cassia-202512) | Nat. Commun. | training-free | 970+ cell populations (eval) | cell type annotation, quality control |
| 2025-10 | AILA [[details]](#model-aila-202510) | Nat. Commun. | N/A | 100 AFM tasks (eval) | AFM calibration, mechanical property measurement +2 |
| 2025-10 | AgentMD [[details]](#model-agentmd-202510) | Nat. Commun. | training-free | RiskQA + 698 ED notes (eval) | clinical risk calculator curation, risk prediction |
| 2025-09 | MAP [[details]](#model-map-202509) | Nat. Commun. | training-free | PlanBench + planning tasks (eval) | multi-step planning, task decomposition |
| 2025-08 | SciToolAgent [[details]](#model-scitoolagent-202508) | Nat. Comput. Sci. | training-free | — | multi-tool scientific workflow orchestration |
| 2025-07 | Virtual Lab [[details]](#model-virtual-lab-202507) | Nature | training-free | — | nanobody design, binding-profile evaluation |
| 2025-06 | Oncology AI Agent [[details]](#model-oncology-ai-agent-202506) | Nat. Cancer | training-free (agent); pretrained tool models | 20 patient cases (eval) | oncology decision support, tool selection +1 |

## Details

Click a model to expand its record.


<a id="model-quine-202609"></a>
<details>
<summary><b>Quine</b> — Introducing Quine: An AI research system designed for the complexity of biology <i>(Microsoft Research 2026-09)</i></summary>

**[Introducing Quine: An AI research system designed for the complexity of biology](https://www.microsoft.com/en-us/research/blog/introducing-quine-an-ai-research-system-designed-for-the-complexity-of-biology/)**

*Microsoft Research* · 2026-09 · Nicolo Fusi & Jonathan M. Carlson

| | |
| --- | --- |
| **Backbone** | Experimental biology-research system combining a multimodal world model with an interactive harness that connects reasoning and orchestration models, scientific tools, literature, wet-lab experiments and human researchers. |
| **Pre-training** | `multimodal world-model training`, `agentic tool use`<br>The world model is trained jointly across biological scales and modalities; the surrounding harness performs research orchestration and incorporates experimental feedback. |
| **Data usage** | Applied with the Broad Institute to pancreatic-cancer cell-state data and compound libraries; several top-ranked compounds were validated across multiple wet-lab assays. |
| **Downstream tasks** | `cancer compound prioritization`, `experiment planning`, `closed-loop biological discovery`<br>Builds predictive representations of biological state, prioritizes interventions expected to shift tumour states and uses experimental results to update subsequent research decisions. |
| **Modalities** | `text`, `literature`, `multimodal biological data`, `experimental results` |
| **Evaluation boundary** | Early-stage research technology described in an institutional announcement rather than a peer-reviewed system paper. Microsoft states that outputs can be incomplete or inaccurate, require qualified review and experimental validation, and are not intended for clinical or medical use. |

</details>

<a id="model-claude-art-discovery-agents-202609"></a>
<details>
<summary><b>Claude ART Discovery Agents</b> — Autonomous AI agents discover reverse transcriptases with tandem repeat arrays <i>(Anthropic Research 2026-09)</i></summary>

**[Autonomous AI agents discover reverse transcriptases with tandem repeat arrays](https://www-cdn.anthropic.com/22573675ada52a8ca8a97a1a4b4326b2f208a071.pdf)**

*Anthropic Research* · 2026-09 · Peter H. Yoon, Januka S. Athukoralage, Emmanuel Ameisen, Eric Kauderer-Abrams, Nicholas T. Perry & Matthew G. Durrant

| | |
| --- | --- |
| **Backbone** | Large-scale parallel Claude-agent research workflow in which independent sessions inspect genomic and protein-sequence data, write and execute analysis code, record findings in shared artifacts and surface hypotheses for follow-up. |
| **Pre-training** | `training-free multi-agent orchestration`<br>No new biological model is reported; existing Claude agents are orchestrated at inference time over bioinformatics data and tools. |
| **Data usage** | Approximately 1.9 billion protein clusters were screened. The campaign comprised 949 agent sessions across 119 tasks, consuming about 210 million tokens over roughly 21 hours. |
| **Downstream tasks** | `genomic mining`, `reverse-transcriptase discovery`, `hypothesis generation`<br>Agents narrowed more than 200,000 reverse-transcriptase candidates and identified array-associated reverse transcriptases (ART), a phage-associated family next to tandem DNA repeats, for human experimental follow-up. |
| **Modalities** | `text`, `DNA sequences`, `protein sequences`, `bioinformatics data`, `code` |
| **Evaluation boundary** | The biological function of ART remains unknown, physical experiments were performed by humans, and the report is an early technical preprint rather than peer-reviewed validation. Anthropic also reports that ten reruns did not independently rediscover the repeat array, limiting reproducibility claims. |

</details>

<a id="model-paper2agent-202609"></a>
<details>
<summary><b>Paper2Agent</b> — Reimagining research papers as interactive and reliable AI agents <i>(Nature 2026-09)</i></summary>

**[Reimagining research papers as interactive and reliable AI agents](https://www.nature.com/articles/s41586-026-11044-y)**

*Nature* · 2026-09 · Jiacheng Miao, Joe R. Davis, Yaohui Zhang, Jonathan K. Pritchard & James Zou

| | |
| --- | --- |
| **Backbone** | A central agent coordinates specialist agents that inspect a paper and its code. They build and test a Model Context Protocol (MCP) server. |
| **Pre-training** | `training-free multi-agent orchestration`<br>The paper presents a workflow. It does not train a new foundation model. |
| **Data usage** | Case studies use AlphaGenome, Scanpy, and TISSUE. The authors test reproduction of published workflows and new scientific queries. |
| **Downstream tasks** | `paper-to-MCP conversion`, `workflow reproduction`, `scientific queries`, `cross-paper analysis`<br>The system exposes methods as MCP tools and lets agents execute analyses through natural-language requests. |
| **Modalities** | `paper text`, `code`, `research data` |
| **Code** | [github.com/jmiao24/Paper2Agent](https://github.com/jmiao24/Paper2Agent) |
| **Evaluation boundary** | Results depend on usable code and documentation. The authors report that some repositories could not be converted. Human researchers remain responsible for open-ended scientific conclusions. |

</details>

<a id="model-mutexagpt-202609"></a>
<details>
<summary><b>MutexaGPT</b> — MutexaGPT: an intuition-to-design translator for physics-based enzyme engineering <i>(Nat. Comput. Sci. 2026-09)</i></summary>

**[MutexaGPT: an intuition-to-design translator for physics-based enzyme engineering](https://www.nature.com/articles/s43588-026-01049-y)**

*Nature Computational Science* · 2026-09 · Qianzhen Shao, Yinjie Zhong, Sebastian Stull, Xinchun Ran, Ning Ding, Kieran Nehil-Puleo, Ruizhe Yao, Han Xu & Zhongyue J. Yang

| | |
| --- | --- |
| **Backbone** | Multi-LLM-agent system comprising QuestionAnalyzer, WorkPlanningBoard (MetricsPlanner and MutantPlanner), and ResultExplainer, integrated with EnzyHTP for autonomous high-throughput molecular modeling and simulation. |
| **Pre-training** | `training-free multi-agent orchestration`<br>No new foundation model is trained; prompted LLM agents translate plain-English enzyme-engineering intuition into simulation plans, execute tool-backed workflows, and interpret results. |
| **Data usage** | Retrospective cavity-engineering evaluation over a 600-variant halide methyltransferase library; prospective cold-adaptation evaluation of wild type and ten bidomain-amylase linker variants, with experimental activity assays for the two prioritized designs. Separate curated test cases evaluate the core agents. |
| **Downstream tasks** | `enzyme variant design`, `high-throughput molecular simulation`, `substrate-specificity engineering`, `cold-adaptation engineering`<br>Clarifies underspecified design requests, maps intuition to physical metrics and mutation libraries, configures and executes molecular-dynamics workflows, ranks variants, explains limitations, and recommends follow-up experiments. The cavity campaign achieved a 40% hit rate (~4× enrichment); cold-adaptation variants improved relative activity by up to 3.7×. |
| **Modalities** | `text`, `protein structure`, `molecular simulation data` |
| **Code** | [github.com/ChemBioHTP/EnzyHTP-GPT](https://github.com/ChemBioHTP/EnzyHTP-GPT/) |
| **Evaluation boundary** | Cavity-engineering validation is retrospective against a previously characterized library; prospective wet-lab testing covers two prioritized linker variants. The system is an automation and intuition-translation platform rather than a learned predictive model. |

</details>

<a id="model-on-premise-medical-ai-agent-202609"></a>
<details>
<summary><b>On-Premise Medical AI Agent</b> — On-premise medical AI agents for reliable clinical decision-making <i>(Nat. Med. 2026-09)</i></summary>

**[On-premise medical AI agents for reliable clinical decision-making](https://www.nature.com/articles/s41591-026-04609-x)**

*Nature Medicine* · 2026-09 · Li Zhang, Georg Wölflein, Dyke Ferber, Junhao Liang, Zunamys I. Carrero, et al.

| | |
| --- | --- |
| **Backbone** | Fully on-premise dual-agent simulation with a tool-using Physician Agent and case-grounded Patient Agent; evaluates GLM-4.5-Air, GLM-5, Qwen-3.5 and GPT-OSS locally, with GPT-5.2 as a cloud baseline on the primary benchmark. |
| **Pre-training** | `training-free`, `open-weight LLM comparison`<br>No new foundation model is trained. The contribution is a governed local agent workflow plus internal-likelihood, linguistic and cross-run behavioral reliability measures. |
| **Data usage** | MIRA-v2 (551 cases, seven conditions) and CDM (2,400 cases, four abdominal conditions) from MIMIC-IV; external VivaBench (990 PubMed-derived cases across ten specialty groups); physician adjudication of 181 MIRA-v2 cases. |
| **Downstream tasks** | `simulated diagnosis`, `clinical tool use`, `decision-time reliability estimation`, `selective-autonomy routing`<br>The best on-premise model achieved 90.04% accuracy on MIRA-v2 and 83.8% on CDM. Diagnostic behavioral consistency had AUC 0.860; at a 0.90 threshold, 49.4% of MIRA-v2 cases were retained at 98.9% accuracy. |
| **Modalities** | `text`, `structured clinical evidence`, `simulated EHR tools` |
| **Code** | [github.com/KatherLab/onprem-medical-agents](https://github.com/KatherLab/onprem-medical-agents) |
| **Evaluation boundary** | All encounters are retrospective simulations. The demonstrated threshold is configuration-specific, requires five stochastic runs, and does not establish prospective safety, workload benefit, fairness or EHR integration. |

</details>

<a id="model-ai-tec-202609"></a>
<details>
<summary><b>AI-TEC</b> — Initial lessons from real-world implementation of an AI-agent eye clinic in China <i>(Nat. Med. 2026-09)</i></summary>

**[Initial lessons from real-world implementation of an AI-agent eye clinic in China](https://www.nature.com/articles/s41591-026-04631-z)**

*Nature Medicine* · 2026-09 · Tao Yan, Di Zhang, Luxiao Chen, Taizhangtian Ma, Chunyang Tang, et al.

| | |
| --- | --- |
| **Backbone** | AI-Agent Augmented Tsinghua Eye Clinic (AI-TEC), a proposed multi-agent ophthalmic pathway. The early deployed subset contains pre-consultation and triaging agents using Qwen3.5-35B and RETFound; diagnosis, clinician decision-support, patient-support and Agent X remain target-architecture components in this Comment. |
| **Pre-training** | `local fine-tuning`, `iterative expert feedback`<br>RETFound is locally tuned first with historical CFP records and then with ophthalmologist-reviewed data; the article does not fully report model versions or training configuration. |
| **Data usage** | 26,839 historical CFP images for local tuning; Prospective Dataset 1 contains 472 CFPs and Dataset 2 contains 348 CFPs. Passive deployment monitoring reports examination-level use at a single hospital. The Annotated Dataset count conflicts between prose (1,426) and Figure 2 (1,482). |
| **Downstream tasks** | `pre-consultation`, `ophthalmic triage`, `CFP classification`, `workflow integration`<br>Macro-AUROC increased from 0.7996 to 0.9383 after expert-reviewed data were used, while examination-level use changed from 25.7% to 3.8% and then 23.0% across reported snapshots. |
| **Modalities** | `text`, `color fundus photography`, `structured clinical data` |
| **Evaluation boundary** | This is a Comment and early single-center implementation report, not a controlled end-to-end evaluation. The AUROC applies to the CFP component, only two agents are documented as deployed, and decision impact and patient outcomes are not reported. |

</details>

<a id="model-us-agent-202609"></a>
<details>
<summary><b>US-Agent</b> — A multitask framework for automated multi-frame right upper quadrant ultrasound interpretation and clinical decision support <i>(Nat. Commun. 2026-09)</i></summary>

**[A multitask framework for automated multi-frame right upper quadrant ultrasound interpretation and clinical decision support](https://www.nature.com/articles/s41467-026-77498-w)**

*Nature Communications* · 2026-09 · Haiman Guo, Cheng-Yi Li, Yuli Wang, Robin Wang, Yuwei Dai, et al.

| | |
| --- | --- |
| **Backbone** | The workflow combines an ultrasound foundation model, a vision-language report model, and a decision module. It analyzes right upper quadrant ultrasound frames. |
| **Pre-training** | `ultrasound foundation model`, `task-specific VLM training`<br>The study evaluates trained models for finding classification and report generation. |
| **Data usage** | The internal dataset includes 9,189 cases and 594,099 images. External datasets include 1,704 cases and 108 cases. |
| **Downstream tasks** | `16-finding classification`, `diagnostic report generation`, `cholecystectomy decision support`<br>The decision module uses imaging findings, reports, and clinical data. |
| **Modalities** | `multi-frame ultrasound`, `radiology reports`, `clinical data` |
| **Code** | [github.com/Mikeghm/ruq-ultrasound-vlm](https://github.com/Mikeghm/ruq-ultrasound-vlm) |
| **Evaluation boundary** | Internal and external cohorts support an imaging workflow evaluation. The study does not assess dental surgery video recognition or prospective patient outcomes. |

</details>

<a id="model-mochiagent-202609"></a>
<details>
<summary><b>MoChiAgent</b> — Prediction of maternal and infant outcomes from longitudinal electronic health records with a Mother-Child AI agent <i>(Nat. Med. 2026-09)</i></summary>

**[Prediction of maternal and infant outcomes from longitudinal electronic health records with a Mother-Child AI agent](https://www.nature.com/articles/s41591-026-04694-y)**

*Nature Medicine* · 2026-09 · Sian Liu, Wenxin Zheng, Jin Kang, Tianyi Xu, Siming Chen, Gen Li, et al.

| | |
| --- | --- |
| **Backbone** | Modular mother-child clinical AI agent built around MoChiFormer, which combines a visit-level Transformer encoder with a GPT-2-style causal temporal decoder. The agent exposes imputation, biological-age and disease-prediction, visual-interpretability, and knowledge-search tools through an LLM-based routing and report interface. |
| **Pre-training** | `self-supervised masked-feature pretraining`, `supervised multi-task fine-tuning`<br>MoChiFormer is pretrained for 200 epochs by reconstructing masked categorical and numerical EHR features with a variational regularizer, then fine-tuned for 100 epochs on age, current/future disease, and disease-relation objectives. The interface layer is developed separately through prompt engineering and instruction-tuned few-shot examples. |
| **Data usage** | Development data comprise 1,064,733 mothers (3,682,209 visits) and 393,375 infants (719,390 visits) from two Chinese hospitals, with patient-level training, tuning, and held-out internal splits. External evaluation uses 75,816 mothers (263,452 visits) and 14,418 infants (23,192 visits) from a third hospital. A separate agent-interface pilot evaluates 25 enriched unseen cases with six blinded perinatal specialists. |
| **Downstream tasks** | `maternal and infant disease diagnosis`, `future disease prediction`, `biological and developmental age estimation`, `phenotype and trajectory discovery`, `transgenerational risk stratification`, `evidence-grounded clinical reporting`<br>The model restores missing EHR measurements, estimates fetal, gestational, and infant age, predicts current and future maternal/infant outcomes, identifies risk-associated patient clusters, and combines predictions with traceable literature and structured clinical recommendations. |
| **Modalities** | `longitudinal EHR`, `laboratory tests`, `structured clinical events`, `text` |
| **Code** | [github.com/peterzheng98/mochiagent](https://github.com/peterzheng98/mochiagent) |
| **Evaluation boundary** | Large-cohort evidence primarily validates the MoChiFormer prediction engine. The complete LLM/tool interface has only a 25-case offline pilot, and the reported LLM baselines were evaluated without tool access; this is not prospective clinical validation. |

</details>

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

| | || --- | --- |
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
| --- | --- || **Backbone** | LLM agent orchestrating 500+ scientific tools (web APIs, ML models, Python functions, knowledge databases) via a scientific-tool knowledge graph and graph-based retrieval-augmented generation, with a safety-checking module |
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

