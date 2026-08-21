# AI Agents

Agentic, autonomous and tool-using AI systems.

**Maintainer:** @[Meng Wei](https://weimengmeng1999.github.io/meng-wei.github.io/) @[ Feng Lan](https://ai-healthcare-portfolio.hushed-dove-3131.chatgpt.site)

**Notebook:** [NotebookLM](https://notebook.google.com/notebook/b25c668a-4926-45b8-bca3-329885628a36)

**27 entries** · [Back to index](README.md)

| Date | Model | Venue | Pre-training | Data usage | Downstream tasks |
| --- | --- | --- | --- | --- | --- |
| 2026-07 | [Multi-Agent Architectures](#model-multi-agent-architectures-202607) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/02_2026-07_Multi-Agent_Architectures) | Nat. Mach. Intell. | N/A | 6 benchmarks (eval) | benchmarking, agent coordination |
| 2026-07 | [Biomni](#model-biomni-202607) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/03_2026-07_Biomni) | Science | RL fine-tuning, training-free tool use | agent trajectories (train); 433 instances (eval) | CRISPR planning, scRNA-seq annotation, ADMET prediction +2 |
| 2026-07 | [AI X-ray Scientist](#model-ai-x-ray-scientist-202607) | Nat. Mach. Intell. | training-free | — | X-ray sample alignment, closed-loop experimentation |
| 2026-06 | [MIRA](#model-mira-202606) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/05_2026-06_MIRA) | Nature | training-free | 500+ ED cases (eval) | history-taking, diagnosis, treatment planning +2 |
| 2026-06 | [AMIE](#model-amie-202606) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/04_2026-06_AMIE) | Nature | training-free | RxQA + 100 cases (eval) | disease management reasoning, medication selection |
| 2026-05 | [Co-Scientist](#model-co-scientist-202605) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/07_2026-05_Co-Scientist) | Nature | test-time compute scaling | — | hypothesis generation, research proposals |
| 2026-05 | [Robin](#model-robin-202605) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/08_2026-05_Robin) | Nature | training-free | — | hypothesis generation, assay selection, candidate proposal +1 |
| 2026-05 | [ERA](#model-era-202605) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/09_2026-05_ERA) | Nature | tree search | — | bioinformatics method discovery, epidemiological forecasting |
| 2026-05 | [CIPHER](#model-cipher-202605) | Nat. Commun. | N/A | — | process monitoring, autonomous machine control |
| 2026-05 | [Autonomous Interaction](#model-autonomous-interaction-202605) | Nat. Commun. | N/A | — | multi-robot task negotiation, dynamic team coordination |
| 2026-04 | [AlphaLab](#model-alphalab-202604) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/10_2026-04_AlphaLab) | Preprint | N/A | — | general research automation |
| 2026-04 | [SPARK](#model-spark-202604) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/13_2026-04_SPARK) | Nat. Med. | training-free (agent); pretrained preprocessing models | 5.4K patients (eval) | biomarker discovery, risk stratification, spatial biology +2 |
| 2026-04 | [PhenoAssistant](#model-phenoassistant-202604) | Nat. Commun. | training-free | — | phenotype extraction, data visualization, model training |
| 2026-03 | [BioMedAgent](#model-biomedagent-202603) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/15_2026-03_BioMedAgent) | Nat. Biomed. Eng. | N/A | — | bioinformatics analysis |
| 2026-03 | [AI Scientist](#model-ai-scientist-202603) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/16_2026-03_AI_Scientist) | Nature | N/A | — | general research automation |
| 2026-02 | [PantheonOS](#model-pantheonos-202602) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/19_2026-02_PantheonOS) | bioRxiv | RL; integrated scFM pretraining (generative, masked gene prediction) | CELLxGENE subset (train) | gene panel design, signaling pathway mapping |
| 2026-02 | [DeepRare](#model-deeprare-202602) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/20_2026-02_DeepRare) | Nature | training-free | 9 datasets, 2.9K diseases (eval) | rare disease diagnosis, traceable reasoning |
| 2026-01 | [PHIA](#model-phia-202601) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/23_2026-01_PHIA) | Nat. Commun. | N/A | 30K users, synthetic (eval) | wearable-data QA, anomaly detection |
| 2026-01 | [BioDSA](#model-biodsa-202601) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/24_2026-01_BioDSA) | Nat. Biomed. Eng. | N/A | — | biomedical data science analysis |
| 2025-12 | [SciSciGPT](#model-sciscigpt-202512) | Nat. Comput. Sci. | training-free | — | literature analysis, science-of-science workflows |
| 2025-12 | [CASSIA](#model-cassia-202512) | Nat. Commun. | training-free | 970+ cell populations (eval) | cell type annotation, quality control |
| 2025-10 | [AILA](#model-aila-202510) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/27_2025-10_AILA) | Nat. Commun. | N/A | 100 AFM tasks (eval) | AFM calibration, mechanical property measurement +2 |
| 2025-10 | [AgentMD](#model-agentmd-202510) | Nat. Commun. | training-free | RiskQA + 698 ED notes (eval) | clinical risk calculator curation, risk prediction |
| 2025-09 | [MAP](#model-map-202509) | Nat. Commun. | training-free | PlanBench + planning tasks (eval) | multi-step planning, task decomposition |
| 2025-08 | [SciToolAgent](#model-scitoolagent-202508) | Nat. Comput. Sci. | training-free | — | multi-tool scientific workflow orchestration |
| 2025-07 | [Virtual Lab](#model-virtual-lab-202507) [Paper Card](https://github.com/medfm-flare/AwesomeBiomedicalAI/tree/ai_agent/paper_cards/30_2025-07_Virtual_Lab) | Nature | training-free | — | nanobody design, binding-profile evaluation |
| 2025-06 | [Oncology AI Agent](#model-oncology-ai-agent-202506) | Nat. Cancer | training-free (agent); pretrained tool models | 20 patient cases (eval) | oncology decision support, tool selection +1 |

