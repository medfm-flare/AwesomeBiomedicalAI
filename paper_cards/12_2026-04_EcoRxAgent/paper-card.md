# Paper Card: EcoRxAgent: an AI agent for generating economically substitutable prescriptions

> Source coverage: Full paper
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Clinical
>
> Context verification: Targeted official article and catalogue check
>
> Card completeness: Complete relative to the processed source (16 PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| EcoRxAgent | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | N/A | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** EcoRxAgent: an AI agent for generating economically substitutable prescriptions
- **Model / system:** EcoRxAgent
- **Venue and date:** npj Digit. Med. 2026-04
- **Official source:** [https://www.nature.com/articles/s41746-026-02612-7](https://www.nature.com/articles/s41746-026-02612-7)
- **Code:** https://github.com/AllminerLab/EcoRxAgent
- **Modalities:** See the paper for task-specific modalities.
- **Source note:** The card is page-grounded to the official PDF.

## 02 One-Sentence Summary

[Analysis] EcoRxAgent uses Qwen3-Max controlled by a sequential four-tool workflow for candidate-drug retrieval, prescription generation, safety checking and cost-effectiveness analysis to address Generates physician-reviewable, safety-checked prescription alternatives that aim to preserve therapeutic effectiveness while reducing medication cost; the evidence is bounded to N/A and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

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

- **Surface method:** [Paper] Qwen3-Max controlled by a sequential four-tool workflow for candidate-drug retrieval, prescription generation, safety checking and cost-effectiveness analysis [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] N/A [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** Qwen3-Max controlled by a sequential four-tool workflow for candidate-drug retrieval, prescription generation, safety checking and cost-effectiveness analysis [Paper: PDF pp. 1–2]

![Figure 1 — faithful PDF page view](<figures/page-002.png>)

*Figure 1 is embedded as an unchanged PDF page view. It contributes Overview of this study. a The pipeline of the proposed EcoRxAgent system, which autonomously utilizes four tools so as to generate economically substitutable prescriptions for physician review and selection by taking as input the baseline prescription along with patient’s clinical information, hospital pharmacy database, [Paper: PDF p. 2, Figure 1]*

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal |
|---|---|---|---|---|---|
| Reasoning / planning layer | Converts the objective and state into a next action | Multi-step tasks cannot be solved by one static answer | Context → plan or action | [Paper: PDF pp. 1–2] | Expected: more myopic or invalid actions; not assumed measured |
| Tool or specialist layer | Executes domain operations | Grounds outputs in data, software, databases, or instruments | Action → observation | [Paper: PDF pp. 1–2] | Expected: loss of task coverage; measured effect depends on ablation |
| Feedback loop | Revises after observations or failures | Long-horizon work requires recovery | Observation → updated state | [Paper: PDF pp. 1–2] | Expected: lower recovery and completion |
| Evaluation layer | Scores outputs, traces, or downstream outcomes | Separates fluent output from valid work | Result / trace → metric | [Paper: PDF p. 1] | Claims become unauditable |

## 09 Essential Formulas and Symbols

Not applicable or no essential equation was reliably inventoried in the main paper.

## 10 Experimental Design and Evidence Chain

**Data / population:** N/A [Paper: PDF p. 1]

**Downstream tasks:** Generates physician-reviewable, safety-checked prescription alternatives that aim to preserve therapeutic effectiveness while reducing medication cost [Paper: PDF p. 1]

**Inventoried tables:**

- **Table 1** — Patient demographic and prescription statistic information for the Guangzhou cohort [Paper: PDF p. 4, Table 1]
- **Table 2** — Patient demographic and prescription statistic information for the external Shenshan cohort [Paper: PDF p. 4, Table 2]
- **Table 3** — Distribution of the number of substituted drugs per prescription across different disease categories for the Guangzhou cohort [Paper: PDF p. 9, Table 3]

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | Generates physician-reviewable, safety-checked prescription alternatives that aim to preserve therapeutic effectiveness while reducing medication cost | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |

![Figure 2 — faithful PDF page view](<figures/page-005.png>)

*Figure 2 is embedded as an unchanged PDF page view. It contributes Clinical effectiveness evaluation for the Guangzhou cohort. a–f Comparison between best possible prescription score and baseline prescription score, where (p) indicates the number of the same points. g–l Capacity to generate multiple clinically effective substitutable prescriptions, quantifying the number of [Paper: PDF p. 5, Figure 2]*

![Figure 3 — faithful PDF page view](<figures/page-006.png>)

*Figure 3 is embedded as an unchanged PDF page view. It contributes Clinical effectiveness evaluation for the Shenshan cohort. a–f Comparison between best possible prescription score and baseline prescription score, where (p) indicates the number of the same points. g–l Capacity to generate multiple clinically effective substitutable prescriptions, quantifying the number of economically sub- [Paper: PDF p. 6, Figure 3]*

![Figure 4 — faithful PDF page view](<figures/page-007.png>)

*Figure 4 is embedded as an unchanged PDF page view. It contributes Comparing all generated economically substitutable prescription scores against baseline prescription scores. a–f Comparison results for the Guangzhou cohort. g–l Comparison results for the Shenshan cohort. https://doi.org/10.1038/s41746-026-02612-7 [Paper: PDF p. 7, Figure 4]*

![Figure 5 — faithful PDF page view](<figures/page-008.png>)

*Figure 5 is embedded as an unchanged PDF page view. It contributes Cost effectiveness evaluation for the Guangzhou cohort. a–f Cost reduction ratio (y-axis) achieved on baseline prescriptions ordered by baseline prescription total cost (x-axis). Each data point represents the best possible eco- nomically substitutable prescription for a single patient (n = 799). g–h Mean value of [Paper: PDF p. 8, Figure 5]*

![Figure 6 — faithful PDF page view](<figures/page-010.png>)

*Figure 6 is embedded as an unchanged PDF page view. It contributes Cost effectiveness evaluation for the Shenshan cohort. a–f Cost reduction ratio (y-axis) achieved on baseline prescriptions ordered by baseline prescription total cost (x-axis). Each data point represents the best possible economically sub- stitutable prescription for a single patient (n = 760). g–h Mean value of best possible [Paper: PDF p. 10, Figure 6]*

![Figure 7 — faithful PDF page view](<figures/page-011.png>)

*Figure 7 is embedded as an unchanged PDF page view. It contributes Joint evaluation of therapeutic efﬁcacy and economic impact for the Guangzhou cohort. a–f Group 1: maintained clinical effectiveness with substantial cost reduction. g Group 2: enhanced clinical effectiveness with cost savings. h Group 3: trade-offs between cost and clinical effectiveness. https://doi.org/10.1038/s41746-026-02612-7 [Paper: PDF p. 11, Figure 7]*

![Figure 8 — faithful PDF page view](<figures/page-012.png>)

*Figure 8 is embedded as an unchanged PDF page view. It contributes Joint evaluation of therapeutic efﬁcacy and economic impact for the Shenshan cohort. a–f Group 1: maintained clinical effectiveness with substantial cost reduction. g Group 2: enhanced clinical effectiveness with cost savings. h Group 3: trade-offs between cost and clinical effectiveness. https://doi.org/10.1038/s41746-026-02612-7 [Paper: PDF p. 12, Figure 8]*

![Figure 9 — faithful PDF page view](<figures/page-013.png>)

*Figure 9 is embedded as an unchanged PDF page view. It contributes Illustrating example of EcoRxAgent and senior physicians’ double-blind evaluation for a 71-year-old female patient in the Guangzhou cohort. Compared to the baseline (CNY 22.72, score: 5.0), EcoRxAgent generated Prescriptions 1 and 2, reducing costs to CNY 15.76 (−30.63%) and CNY 17.60 (−22.54%). In blind eva- [Paper: PDF p. 13, Figure 9]*

## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** N/A [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on Qwen3-Max controlled by a sequential four-tool workflow for candidate-drug retrieval, prescription generation, safety checking and cost-effectiveness analysis [Paper: PDF pp. 1–2]
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
| Retrospective or simulated evaluation can overstate deployment readiness | Workflow realism does not remove selection, documentation, and site effects | Run a prospective silent trial followed by a governed clinician-in-the-loop study | Population and evaluation setting described in the paper |
| Aggregate accuracy can conceal calibration and subgroup failures | Clinical decisions require reliable uncertainty and equitable performance | Report calibration, abstention, subgroup effects, and error severity with confidence intervals | [Analysis] Clinical transfer boundary |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: represent agent studies as **objective → permitted actions → observations → stopping rule → audited outcome**.
- Agent-derived knowledge candidate: keep training data, tool knowledge, retrieval sources, and evaluation cases as separate provenance classes.
- Agent-derived knowledge candidate: pair endpoint performance with cost, trace validity, error severity, and human-oversight requirements.

## 15 Connections to Existing Knowledge

[Analysis] This paper belongs to a broader transition from language-only assistants to systems that plan, call tools, execute code or instrument actions, and revise from observations. The closest transferable connection is methodological: benchmark the full workflow and its failure modes rather than only the final prose answer. This connection is a synthesis across the catalogue and was not used to claim priority.

## 16 Research Ideas

### Agent-derived research candidate

**Prospective guarded evaluation of EcoRxAgent.** [Hypothesis] A calibrated abstention policy plus clinician approval will preserve most useful actions while reducing severe errors. Delta: add risk-tiered action permissions and uncertainty-triggered handoff. Validation: prospective silent deployment on an external site, followed by a preregistered clinician-in-the-loop comparison; primary endpoints are severe-error rate, calibration, time, and resource use. Falsifier: no reduction in severe errors or clinically important delay. Failure modes: workflow adaptation, alert fatigue, distribution shift. Innovation status: unverified; prior-art search required.