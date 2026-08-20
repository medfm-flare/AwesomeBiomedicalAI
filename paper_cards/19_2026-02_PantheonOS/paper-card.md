# Paper Card: PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery

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
> Card completeness: Complete relative to the processed source (113 PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| PantheonOS | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | Subsets of the CELLxGENE dataset. | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** PantheonOS: An Evolvable Multi-Agent Framework for Automatic Genomics Discovery
- **Model / system:** PantheonOS
- **Venue and date:** bioRxiv 2026-02
- **Official source:** [https://www.biorxiv.org/content/10.64898/2026.02.26.707870v1.full.pdf](https://www.biorxiv.org/content/10.64898/2026.02.26.707870v1.full.pdf)
- **Code:** github.com/aristoteleo/PantheonOS
- **Modalities:** omics data, text
- **Source note:** The card is page-grounded to the official PDF.

## 02 One-Sentence Summary

[Analysis] PantheonOS uses LLM with a reinforcement-learning module routing to 22 integrated single-cell foundation models (scFMs) to address gene panel design, signaling pathway mapping Gene panel design, mapping molecular and signaling events, such as Cer1–Nodal inhibition, in embryonic development.; the evidence is bounded to Subsets of the CELLxGENE dataset. and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

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

- **Surface method:** [Paper] LLM with a reinforcement-learning module routing to 22 integrated single-cell foundation models (scFMs) [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] RL, generative pre-training (scGPT), masked gene prediction (scBERT) The router's LLM/RL layer is trained via reinforcement learning; the 22 integrated scFMs use diverse pretraining methods, including generative pre-training (scGPT), BERT-style masked gene prediction (scBERT), and tabular self-supervised learning. [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** LLM with a reinforcement-learning module routing to 22 integrated single-cell foundation models (scFMs) [Paper: PDF pp. 1–2]

![Representative first-page view](<figures/page-001.png>)

*No main figure was reliably inventoried by the PDF parser; this unchanged page view documents the source and the limitation. [Paper: PDF p. 1]*

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal |
|---|---|---|---|---|---|
| Reasoning / planning layer | Converts the objective and state into a next action | Multi-step tasks cannot be solved by one static answer | Context → plan or action | [Paper: PDF pp. 1–2] | Expected: more myopic or invalid actions; not assumed measured |
| Tool or specialist layer | Executes domain operations | Grounds outputs in data, software, databases, or instruments | Action → observation | [Paper: PDF pp. 1–2] | Expected: loss of task coverage; measured effect depends on ablation |
| Feedback loop | Revises after observations or failures | Long-horizon work requires recovery | Observation → updated state | [Paper: PDF pp. 1–2] | Expected: lower recovery and completion |
| Evaluation layer | Scores outputs, traces, or downstream outcomes | Separates fluent output from valid work | Result / trace → metric | [Paper: PDF p. 1] | Claims become unauditable |

## 09 Essential Formulas and Symbols

- [Paper] **Equation 1:** dynamic injection ensures (1) [Paper: PDF p. 38, Equation 1]
- [Paper] **Equation 2:** ●​ Tool output truncation: Two strategies, selected by a use_smart_truncate flag: Simple mode: Truncate the string representation to characters. Smart mode: Operates on the raw structured result (before stringification). For JSON dicts: (1) filter base64 content, (2) [Paper: PDF p. 32, Equation 2]
- [Paper] **Equation 3:** PantheonOS has rich builtin ToolSets, Agents, Team structures and skill systems. Builtin toolsets: PantheonOS supports a variety of builtin toolsets, including (1) code execution: Python, R, Julia; (2) Shell: Command execution, environment management; (3) [Paper: PDF p. 23, Equation 3]
- [Paper] **Equation 5:** preventing conflation of analysis with curation; (4) Dual gating: Confidence gate ( ) discards unreliable reflections; atomicity gate ( ) rejects vague learnings; (5) [Paper: PDF p. 38, Equation 5]
- [Paper] **Equation 6:** agent: Data analysis, visualization; (2) Biology agent: Domain specific biological interpretation; (3) Browser agent: Web search, literature retrieval, documentation lookup; (4) Coding agent: Code generation; (5) Evolution agent: Algorithm optimization via LLM-guided or more precisely, Agent-guided mutation (see section Pantheon-Evolve framework: Agentic Code Evolution); (6) [Paper: PDF p. 23, Equation 6]

## 10 Experimental Design and Evidence Chain

**Data / population:** Subsets of the CELLxGENE dataset. [Paper: PDF p. 1]

**Downstream tasks:** gene panel design, signaling pathway mapping Gene panel design, mapping molecular and signaling events, such as Cer1–Nodal inhibition, in embryonic development. [Paper: PDF p. 1]

**Inventoried tables:**

- No main table was reliably inventoried by the parser.

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | gene panel design, signaling pathway mapping Gene panel design, mapping molecular and signaling events, such as Cer1–Nodal inhibition, in embryonic development. | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |



## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** Subsets of the CELLxGENE dataset. [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on LLM with a reinforcement-learning module routing to 22 integrated single-cell foundation models (scFMs) [Paper: PDF pp. 1–2]
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

**Budget-matched external stress test for PantheonOS.** [Hypothesis] The reported system advantage will remain detectable when model calls, tokens, tools, and wall-clock budget are matched and tasks are newly authored. Delta: replace the original benchmark-only comparison with preregistered external tasks and trace-level auditing. Validation: factorial comparison against a single-agent and strongest non-agent baseline across at least two backbone families; report success, cost, execution validity, and error severity. Falsifier: the advantage disappears under matched resources. Failure modes: benchmark construction bias, tool instability, evaluator disagreement. Innovation status: unverified; prior-art search required.