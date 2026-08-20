# Paper Card: An agentic system for rare disease diagnosis with traceable reasoning

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
> Card completeness: Complete relative to the processed source (23 PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| DeepRare | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | 9 datasets from literature, case reports and clinical centers across Asia, North America and Europe, spanning 2,919 diseases and 14 specialties (eval). | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** An agentic system for rare disease diagnosis with traceable reasoning
- **Model / system:** DeepRare
- **Venue and date:** Nature 2026-02
- **Official source:** [https://www.nature.com/articles/s41586-025-10097-9](https://www.nature.com/articles/s41586-025-10097-9)
- **Code:** github.com/MAGIC-AI4Med/DeepRare
- **Modalities:** text, EHR data
- **Source note:** The card is page-grounded to the official PDF.

## 02 One-Sentence Summary

[Analysis] DeepRare uses LLM-based multi-agent system integrating 40+ specialized tools and up-to-date knowledge sources for rare disease differential diagnosis to address rare disease diagnosis, traceable reasoning Processes free-text descriptions, HPO terms and genetic testing results to generate ranked diagnostic hypotheses with evidence-linked, traceable reasoning (95.4% expert agreement); 57.18% Recall@1 on HPO-based tasks and 69.1% on multimodal tests.; the evidence is bounded to 9 datasets from literature, case reports and clinical centers across Asia, North America and Europe, spanning 2,919 diseases and 14 specialties (eval). and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

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

- **Surface method:** [Paper] LLM-based multi-agent system integrating 40+ specialized tools and up-to-date knowledge sources for rare disease differential diagnosis [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] training-free No new model trained; agent framework over an existing LLM backbone. [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** LLM-based multi-agent system integrating 40+ specialized tools and up-to-date knowledge sources for rare disease differential diagnosis [Paper: PDF pp. 1–2]

![Figure 1 — faithful PDF page view](<figures/page-003.png>)

*Figure 1 is embedded as an unchanged PDF page view. It contributes DeepRare: an agentic framework for rare disease prioritization. a, System workflow: multi-modal patient data (HPO terms, genomic variants) are processed through a tiered MCP-inspired architecture, generating a ranked top-K diagnosis list with evidence-supported reasoning chains. b, Knowledge [Paper: PDF p. 3, Figure 1]*

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal |
|---|---|---|---|---|---|
| Reasoning / planning layer | Converts the objective and state into a next action | Multi-step tasks cannot be solved by one static answer | Context → plan or action | [Paper: PDF pp. 1–2] | Expected: more myopic or invalid actions; not assumed measured |
| Tool or specialist layer | Executes domain operations | Grounds outputs in data, software, databases, or instruments | Action → observation | [Paper: PDF pp. 1–2] | Expected: loss of task coverage; measured effect depends on ablation |
| Feedback loop | Revises after observations or failures | Long-horizon work requires recovery | Observation → updated state | [Paper: PDF pp. 1–2] | Expected: lower recovery and completion |
| Evaluation layer | Scores outputs, traces, or downstream outcomes | Separates fluent output from valid work | Result / trace → metric | [Paper: PDF p. 1] | Claims become unauditable |

## 09 Essential Formulas and Symbols

- [Paper] **Equation 1:** diagnosis is not ranked among the top five recommendations. Each case was reviewed independently and classified by three rare disease specialists, each with a decade of clinical experience. We categorized failures based on the system’s output structure: (1) [Paper: PDF p. 7, Equation 1]
- [Paper] **Equation 2:** ≠∅ , otherwise (2) [Paper: PDF p. 11, Equation 2]
- [Paper] **Equation 3:** (ˆ, , ), (3) [Paper: PDF p. 11, Equation 3]
- [Paper] **Equation 4:** a = ( ˆ) (4) [Paper: PDF p. 11, Equation 4]
- [Paper] **Equation 5:** ( , ) (5) [Paper: PDF p. 11, Equation 5]
- [Paper] **Equation 6:** ′= (ˆ, | ) (6) [Paper: PDF p. 11, Equation 6]
- [Paper] **Equation 7:** a ˆ = ( ) (7) [Paper: PDF p. 11, Equation 7]
- [Paper] **Equation 8:** , ′, | ) (8) [Paper: PDF p. 12, Equation 8]
- [Paper] **Equation 9:** ″ = ′if, = ∅ (9) [Paper: PDF p. 12, Equation 9]
- [Paper] **Equation 10:** ∪ ← ″ (10) [Paper: PDF p. 12, Equation 10]
- [Paper] **Equation 11:** ′= (ˆ, | ) (11) [Paper: PDF p. 12, Equation 11]
- [Paper] **Equation 12:** } = ( , ˆ, | ) (12) [Paper: PDF p. 12, Equation 12]
- [Paper] **Equation 13:** = ( ( | )| ) (13) [Paper: PDF p. 12, Equation 13]
- [Paper] **Equation 14:** = (document, | ) (14) [Paper: PDF p. 13, Equation 14]
- [Paper] **Equation 15:** = (Case, | ) (15) [Paper: PDF p. 13, Equation 15]

## 10 Experimental Design and Evidence Chain

**Data / population:** 9 datasets from literature, case reports and clinical centers across Asia, North America and Europe, spanning 2,919 diseases and 14 specialties (eval). [Paper: PDF p. 1]

**Downstream tasks:** rare disease diagnosis, traceable reasoning Processes free-text descriptions, HPO terms and genetic testing results to generate ranked diagnostic hypotheses with evidence-linked, traceable reasoning (95.4% expert agreement); 57.18% Recall@1 on HPO-based tasks and 69.1% on multimodal tests. [Paper: PDF p. 1]

**Inventoried tables:**

- No main table was reliably inventoried by the parser.

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | rare disease diagnosis, traceable reasoning Processes free-text descriptions, HPO terms and genetic testing results to generate ranked diagnostic hypotheses with evidence-linked, traceable reasoning (95.4% expert agreement); 57.18% Recall@1 on HPO-based tasks and 69.1% on multimodal tests. | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |

![Figure 2 — faithful PDF page view](<figures/page-005.png>)

*Figure 2 is embedded as an unchanged PDF page view. It contributes HPO-wise cross-dataset evaluation and comparative performance of DeepRare. a, Diagnostic accuracy on seven public rare disease registries, demonstrating DeepRare’s significant advantage over leading baselines— particularly in RareBench-MME (70.0% top-1 accuracy) and RareBench-RAMEDIS [Paper: PDF p. 5, Figure 2]*

![Figure 3 — faithful PDF page view](<figures/page-006.png>)

*Figure 3 is embedded as an unchanged PDF page view. It contributes DeepRare diagnostic performance. a, Comparison of diagnostic accuracy across 14 body systems, showing DeepRare’s superior performance in most specialties compared with LLM (DeepSeek-V3), Reasoning LLM (DeepSeek-R1) and Medical LLM (Baichuan-M1). b, Disease-level recall [Paper: PDF p. 6, Figure 3]*

![Figure 4 — faithful PDF page view](<figures/page-007.png>)

*Figure 4 is embedded as an unchanged PDF page view. It contributes Human expert validation of traceable reasoning chain and failure mode in the DeepRare diagnostic system. a, Representative case output demonstrating differential diagnosis with an evidence-based reference list. b, Histogram of reference accuracy scores with density curve (mean = 0.954, [Paper: PDF p. 7, Figure 4]*

![Figure 5 — faithful PDF page view](<figures/page-008.png>)

*Figure 5 is embedded as an unchanged PDF page view. It contributes Ablation study of the DeepRare system. a, Performance comparison across different LLMs (Claude-3.7-Sonnet, DeepSeek-R1, DeepSeek-V3, GPT-4o and Gemini-2.0-flash) as central hosts on eight rare disease datasets. b, Performance enhancement comparison between baseline LLMs and their [Paper: PDF p. 8, Figure 5]*

## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** 9 datasets from literature, case reports and clinical centers across Asia, North America and Europe, spanning 2,919 diseases and 14 specialties (eval). [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on LLM-based multi-agent system integrating 40+ specialized tools and up-to-date knowledge sources for rare disease differential diagnosis [Paper: PDF pp. 1–2]
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

**Prospective guarded evaluation of DeepRare.** [Hypothesis] A calibrated abstention policy plus clinician approval will preserve most useful actions while reducing severe errors. Delta: add risk-tiered action permissions and uncertainty-triggered handoff. Validation: prospective silent deployment on an external site, followed by a preregistered clinician-in-the-loop comparison; primary endpoints are severe-error rate, calibration, time, and resource use. Falsifier: no reduction in severe errors or clinically important delay. Failure modes: workflow adaptation, alert fatigue, distribution shift. Innovation status: unverified; prior-art search required.