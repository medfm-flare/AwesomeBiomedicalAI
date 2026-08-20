# Paper Card: An agentic AI system for automated pharmacogenomic recommendation generation

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
> Card completeness: Complete relative to the processed source (9 PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| Pharmacogenomic Recommendation Agent | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | N/A | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** An agentic AI system for automated pharmacogenomic recommendation generation
- **Model / system:** Pharmacogenomic Recommendation Agent
- **Venue and date:** npj Digit. Med. 2026-04
- **Official source:** [https://www.nature.com/articles/s41746-026-02590-w](https://www.nature.com/articles/s41746-026-02590-w)
- **Code:** Not reported in the catalogue entry.
- **Modalities:** See the paper for task-specific modalities.
- **Source note:** The card is page-grounded to the official PDF.

## 02 One-Sentence Summary

[Analysis] Pharmacogenomic Recommendation Agent uses Modular LLM pipeline for literature and FDA-label retrieval, biomedical entity extraction, cross-study evidence aggregation and phenotype-specific recommendation generation to address End-to-end pharmacogenomic evidence synthesis and generation of traceable CPIC-style gene–drug dosing recommendations; the evidence is bounded to N/A and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

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

- **Surface method:** [Paper] Modular LLM pipeline for literature and FDA-label retrieval, biomedical entity extraction, cross-study evidence aggregation and phenotype-specific recommendation generation [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] N/A [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** Modular LLM pipeline for literature and FDA-label retrieval, biomedical entity extraction, cross-study evidence aggregation and phenotype-specific recommendation generation [Paper: PDF pp. 1–2]

![Figure 1 — faithful PDF page view](<figures/page-002.png>)

*Figure 1 is embedded as an unchanged PDF page view. It contributes Architecture of the PGxAI-recommender. Final system design incorpor- ating structured literature-derived evidence prior to recommendation generation. This evidence-aware pipeline emerged from comparative benchmarking and expert scoring, demonstrating substantial gains over baseline prompting alone. [Paper: PDF p. 2, Figure 1]*

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

**Downstream tasks:** End-to-end pharmacogenomic evidence synthesis and generation of traceable CPIC-style gene–drug dosing recommendations [Paper: PDF p. 1]

**Inventoried tables:**

- **Table 1** — Potential coverage and update frequency of the PGxAI-Recommender compared with CPIC [Paper: PDF p. 5, Table 1]

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | End-to-end pharmacogenomic evidence synthesis and generation of traceable CPIC-style gene–drug dosing recommendations | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |

![Figure 2 — faithful PDF page view](<figures/page-003.png>)

*Figure 2 is embedded as an unchanged PDF page view. It contributes Accuracy of structured evidence extraction. A Field-level accuracy, aver- aged across 22 articles and three annotators. Accuracy represents the proportion of extracted ﬁelds that annotators judged to be correct. The model achieved high accuracy on structured factual items, with lower scores on interpretive ﬁelds. B Per- [Paper: PDF p. 3, Figure 2]*

![Figure 3 — faithful PDF page view](<figures/page-004.png>)

*Figure 3 is embedded as an unchanged PDF page view. It contributes Expert ratings of guideline-style recommendations across models. A Overview of the recommendation generation workﬂow. The PGxAI- Recommender incorporates structured pharmacogenomic evidence prior to gen- erating guideline-style outputs. Baseline models receive only a gene–drug pair and [Paper: PDF p. 4, Figure 3]*

## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** N/A [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on Modular LLM pipeline for literature and FDA-label retrieval, biomedical entity extraction, cross-study evidence aggregation and phenotype-specific recommendation generation [Paper: PDF pp. 1–2]
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

**Prospective guarded evaluation of Pharmacogenomic Recommendation Agent.** [Hypothesis] A calibrated abstention policy plus clinician approval will preserve most useful actions while reducing severe errors. Delta: add risk-tiered action permissions and uncertainty-triggered handoff. Validation: prospective silent deployment on an external site, followed by a preregistered clinician-in-the-loop comparison; primary endpoints are severe-error rate, calibration, time, and resource use. Falsifier: no reduction in severe errors or clinically important delay. Failure modes: workflow adaptation, alert fatigue, distribution shift. Innovation status: unverified; prior-art search required.