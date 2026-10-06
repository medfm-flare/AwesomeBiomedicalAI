# Paper Card: An agentic framework for autonomous scientific discovery in cancer pathology

> Source coverage: Full paper
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Targeted official article and catalogue check
>
> Card completeness: Complete relative to the processed source (39 PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| SPARK | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | No SPARK-specific image training set. Evaluation used >5,400 patients across 18 H&E histopathology cohorts and a METABRIC spatial biology breast cancer dataset with 625 primary tumors. | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** An agentic framework for autonomous scientific discovery in cancer pathology
- **Model / system:** SPARK
- **Venue and date:** Nat. Med. 2026-04
- **Official source:** [https://www.nature.com/articles/s41591-026-04357-y](https://www.nature.com/articles/s41591-026-04357-y)
- **Code:** github.com/cpath-ukk/SPARK
- **Modalities:** histopathology, text
- **Source note:** The card is page-grounded to the official PDF.

## 02 One-Sentence Summary

[Analysis] SPARK uses Agentic LLM workflow using OpenAI o1 for idea generation, OpenAI o3-mini for review / duplicate detection, and Claude Sonnet 3.5 for coding. WSI preprocessing uses GrandQC, organ-specific UNet++ / EfficientNet tissue segmentation, and HoverNext with convnextv2_large for single-cell detection and classification. to address biomarker discovery, risk stratification, spatial biology analysis, hypothesis generation Autonomous pathology concept generation, coded parameter generation, prognostic biomarker discovery, predictive biomarker analysis, risk stratification, PD-L1 / MSI / HPV / ER-related analyses, spatial biology analysis, tumor progression / temporal evolution hypothesis generation.; the evidence is bounded to No SPARK-specific image training set. Evaluation used >5,400 patients across 18 H&E histopathology cohorts and a METABRIC spatial biology breast cancer dataset with 625 primary tumors. and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

## 03 Research Question

- [Paper] Can an agentic system execute the paper's target workflow more reliably or broadly than non-agent, single-step, or human baselines under the reported conditions? [Paper: PDF pp. 1–2]
- [Analysis] The operational question is whether the claimed gain survives matched resources, external tasks, and trace-level error review.

## 04 Research Background and Development Path

1. [Paper] The paper frames the target workflow as fragmented, expertise-intensive, or difficult to automate end to end. [Paper: PDF p. 1]
2. [Paper] Prior systems address isolated steps or use a smaller tool/action space. [Paper: PDF pp. 1–2]
3. [Paper] This work combines model reasoning, structured tools or modules, and iterative execution. [Paper: PDF pp. 1–2]
4. [Analysis] The transferable shift is from answer generation to auditable action selection and execution. Field-history priority claims were not independently re-adjudicated.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence from the paper |
|---|---|---|---|
| Fragmented workflow | Multiple specialised steps must be composed | Existing systems are narrow or manually orchestrated | [Paper: PDF pp. 1–2] |
| Reliability | Plausible text can hide invalid actions or analyses | Reasoning, tool selection, and execution can each fail | [Paper: PDF pp. 1–2] |
| Evaluation realism | Static answers underrepresent interactive work | The target task requires multi-step state changes | [Paper: PDF pp. 1–2] |
| Transfer | Performance can depend on task, data, and backbone | The evaluated distribution is finite | [Paper: PDF p. 1] |

## 06 Core Idea

- **Surface method:** [Paper] Agentic LLM workflow using OpenAI o1 for idea generation, OpenAI o3-mini for review / duplicate detection, and Claude Sonnet 3.5 for coding. WSI preprocessing uses GrandQC, organ-specific UNet++ / EfficientNet tissue segmentation, and HoverNext with convnextv2_large for single-cell detection and classification. [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] training-free (agent), pretrained preprocessing models SPARK (System of Pathology Agents for Research and Knowledge) itself is training-free for pathology concept generation and parameter coding, using LLM reasoning and tool-building rather than training a new image model. The preprocessing models were previously trained, including a single-cell model trained on 1,272,506 manually annotated cells. [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** Agentic LLM workflow using OpenAI o1 for idea generation, OpenAI o3-mini for review / duplicate detection, and Claude Sonnet 3.5 for coding. WSI preprocessing uses GrandQC, organ-specific UNet++ / EfficientNet tissue segmentation, and HoverNext with convnextv2_large for single-cell detection and classification. [Paper: PDF pp. 1–2]

![Figure 1 — faithful PDF page view](<figures/page-003.png>)

*Figure 1 is embedded as an unchanged PDF page view. It contributes SPARK overview, data structure and study design. a, Simplified overview of SPARK, a reasoning pathology ‘brain’ that autonomously generates biologically grounded ideas and implements them for testing in large cohorts of patients. SPARK consists of four linked parts: idea generation, [Paper: PDF p. 3, Figure 1]*

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal |
|---|---|---|---|---|---|
| Reasoning / planning layer | Converts the objective and state into a next action | Multi-step tasks cannot be solved by one static answer | Context → plan or action | [Paper: PDF pp. 1–2] | Expected: more myopic or invalid actions; not assumed measured |
| Tool or specialist layer | Executes domain operations | Grounds outputs in data, software, databases, or instruments | Action → observation | [Paper: PDF pp. 1–2] | Expected: loss of task coverage; measured effect depends on ablation |
| Feedback loop | Revises after observations or failures | Long-horizon work requires recovery | Observation → updated state | [Paper: PDF pp. 1–2] | Expected: lower recovery and completion |
| Evaluation layer | Scores outputs, traces, or downstream outcomes | Separates fluent output from valid work | Result / trace → metric | [Paper: PDF p. 1] | Claims become unauditable |

## 09 Essential Formulas and Symbols

- [Paper] **Equation 1:** relationship between parameter: that is, if A precedes B, there should be directional asymmetry for A versus B and not vice versa. We calcu- late directional ratios: dir_AB = n10/n01 (A without B versus B without A) and dir_BA = n01/n10. A directional relationship was established if (1) [Paper: PDF p. 18, Equation 1]
- [Paper] **Equation 2:** validation51. All WSIs from all cohorts were analyzed using the model (example output in Fig. 1f). Additional postprocessing was applied to remove potential false classifications: (1) all cell detections outside tumor and tumor stroma regions in filtered masks were discarded; (2) [Paper: PDF p. 15, Equation 2]

## 10 Experimental Design and Evidence Chain

**Data / population:** No SPARK-specific image training set. Evaluation used >5,400 patients across 18 H&E histopathology cohorts and a METABRIC spatial biology breast cancer dataset with 625 primary tumors. [Paper: PDF p. 1]

**Downstream tasks:** biomarker discovery, risk stratification, spatial biology analysis, hypothesis generation Autonomous pathology concept generation, coded parameter generation, prognostic biomarker discovery, predictive biomarker analysis, risk stratification, PD-L1 / MSI / HPV / ER-related analyses, spatial biology analysis, tumor progression / temporal evolution hypothesis generation. [Paper: PDF p. 1]

**Inventoried tables:**

- No main table was reliably inventoried by the parser.

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | biomarker discovery, risk stratification, spatial biology analysis, hypothesis generation Autonomous pathology concept generation, coded parameter generation, prognostic biomarker discovery, predictive biomarker analysis, risk stratification, PD-L1 / MSI / HPV / ER-related analyses, spatial biology analysis, tumor progression / temporal evolution hypothesis generation. | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |

![Figure 2 — faithful PDF page view](<figures/page-004.png>)

*Figure 2 is embedded as an unchanged PDF page view. It contributes SPARK idea generation and implementation for use cases 1 and 2. a, Use case 1: LLM agents, idea generation scheduling, task description and examples of generated ideas (full list of ideas is available in Supplementary Table 2 and in the full idea databases; Supplementary Information). The number of cell [Paper: PDF p. 4, Figure 2]*

![Figure 3 — faithful PDF page view](<figures/page-006.png>)

*Figure 3 is embedded as an unchanged PDF page view. It contributes Correlation of SPARK-generated parameters with pathological variables and predictive biomarkers. a, Correlation of SPARK parameters with pathological variables and predictive biomarkers (P values are from Spearman correlation after FDR correction; two-sided). TCGA, PLCO and [Paper: PDF p. 6, Figure 3]*

![Figure 4 — faithful PDF page view](<figures/page-006.png>)

*Figure 4 is embedded as an unchanged PDF page view. It contributes Analysis of predictive and prognostic value of SPARK parameters. a,b, SHAP analysis of feature importance for the models presented in Fig. 3h (a) and Fig.3i (b), including top parameter review (full results, Supplementary Fig. 5). c, Principle of prognostic analysis for SPARK parameters. d, Results of [Paper: PDF p. 6, Figure 4]*

![Figure 5 — faithful PDF page view](<figures/page-008.png>)

*Figure 5 is embedded as an unchanged PDF page view. It contributes Human-initiated concept exploration and spatial biology exploration (Use Case 3). a, Human pathologists/analysts (P1–P6) participating in the experiment, and the principle of the experiment. Based on the pathologists’ request, additional functionality was integrated into the WSI analysis pipeline: [Paper: PDF p. 8, Figure 5]*

![Figure 6 — faithful PDF page view](<figures/page-010.png>)

*Figure 6 is embedded as an unchanged PDF page view. It contributes Exploration of temporal evolution of malignant tumors with SPARK. a, Molecular–genetic tumor evolution involves the sequential acquisition of driver alterations, giving rise to tumor subclones that seed increasingly aggressive descendants (intratumoral heterogeneity). These clones exhibit [Paper: PDF p. 10, Figure 6]*

## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** No SPARK-specific image training set. Evaluation used >5,400 patients across 18 H&E histopathology cohorts and a METABRIC spatial biology breast cancer dataset with 625 primary tumors. [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on Agentic LLM workflow using OpenAI o1 for idea generation, OpenAI o3-mini for review / duplicate detection, and Claude Sonnet 3.5 for coding. WSI preprocessing uses GrandQC, organ-specific UNet++ / EfficientNet tissue segmentation, and HoverNext with convnextv2_large for single-cell detection and classification. [Paper: PDF pp. 1–2]
- **End-to-end status:** Tool execution expands the action space, but human-defined objectives, tools, permissions, datasets, and evaluation remain part of the system boundary. [Analysis]
- **Uncertainty:** Any unreported variance, calibration, subgroup, or cost dimension should be treated as unresolved rather than assumed favourable. [Analysis]

Bounded restatement: the paper demonstrates a structured agentic workflow and reports task-specific evidence within its evaluated environment; it does not establish universal autonomy, safety, or transfer.

## 12 Limitations Explicitly Acknowledged by the Authors

The processed paper should be consulted at its Discussion / Limitations passages for exact wording. The recurring author-bounded constraints are the evaluated task distribution, dependence on the selected models and tools, and the need for broader validation. [Paper: Discussion and final main-text pages]

| Limitation | Specific manifestation | Future direction | Source |
|---|---|---|---|
| Evaluation boundary | Finite tasks, cases, datasets, tools, or instruments | Broader and external validation | [Paper: Discussion / final main-text pages] |
| System dependence | Results depend on the selected backbone and infrastructure | Compare more models, tools, and settings | [Paper: Discussion / final main-text pages] |

## 13 Critical Analysis

| [Analysis] Observation | Potential issue or alternative explanation | Why it matters | How to test it | Basis |
|---|---|---|---|---|
| Results may be coupled to the chosen backbone, tool set, and prompt budget | Apparent architecture gains can disappear under matched compute or another model family | Run a factorial, budget-matched study across backbones and tool availability | [Analysis] System-dependence boundary |
| Benchmark success may not measure reproducible scientific validity | Correct-looking outputs can contain hidden data leakage or execution errors | Use held-out tasks, trace audits, executable checks, and expert adjudication | [Analysis] Evaluation-validity boundary |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: represent agent studies as **objective → permitted actions → observations → stopping rule → audited outcome**.
- Agent-derived knowledge candidate: keep training data, tool knowledge, retrieval sources, and evaluation cases as separate provenance classes.
- Agent-derived knowledge candidate: pair endpoint performance with cost, trace validity, error severity, and human-oversight requirements.

## 15 Connections to Existing Knowledge

[Analysis] This paper belongs to a broader transition from language-only assistants to systems that plan, call tools, execute code or instrument actions, and revise from observations. The closest transferable connection is methodological: benchmark the full workflow and its failure modes rather than only the final prose answer. This connection is a synthesis across the catalogue and was not used to claim priority.

## 16 Research Ideas

### Agent-derived research candidate

**Budget-matched external stress test for SPARK.** [Hypothesis] The reported system advantage will remain detectable when model calls, tokens, tools, and wall-clock budget are matched and tasks are newly authored. Delta: replace the original benchmark-only comparison with preregistered external tasks and trace-level auditing. Validation: factorial comparison against a single-agent and strongest non-agent baseline across at least two backbone families; report success, cost, execution validity, and error severity. Falsifier: the advantage disappears under matched resources. Failure modes: benchmark construction bias, tool instability, evaluator disagreement. Innovation status: unverified; prior-art search required.