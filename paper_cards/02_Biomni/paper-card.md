# Paper Card: Autonomous biomedical research with an artificial intelligence agent

> Source coverage: Abstract, verified bibliographic metadata, catalogue record, and author code repository
>
> Extraction confidence: High for the abstract and repository; unavailable for the paywalled full text
>
> Locator mode: source-limited
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Targeted check of Science, PubMed, and the author repository
>
> Card completeness: Partial; unseen full-text methods, figures, tables, and limitations are not inferred

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| Biomni | the general-purpose biomedical AI agent described in the paper | Preserve author capitalization |
| Biomni-R0 | the Qwen-32B-based biological reasoning model described by the catalogue and repository | Keep distinct from the broader agent system |
| Biomni-Eval1 | 433-instance, 10-task biological reasoning benchmark | Treat as evaluation evidence |
| action-discovery agent | component that mines tools, databases, and protocols | Do not equate discovery with validation |

## 01 Basic Information

- **Title:** Autonomous biomedical research with an artificial intelligence agent
- **Authors:** Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Ryan Li, Yusuf Roohani, Lin Qiu, Shiyi Cao, Gavin Li, Junze Zhang, Di Yin, Rick Wierenga, Deniz Kavi, Sherry Liu, Tianwei She, Shruti Marwaha, Jennefer N. Carter, Xin Zhou, Matthew T. Wheeler, Jonathan A. Bernstein, Mengdi Wang, Peng He, Jingtian Zhou, Michael P. Snyder, Le Cong, Aviv Regev and Jure Leskovec. [Paper: Metadata]
- **Venue / date:** *Science*, published online 9 July 2026. [Paper: Metadata]
- **DOI:** [10.1126/science.adz4351](https://doi.org/10.1126/science.adz4351)
- **Code:** [snap-stanford/biomni](https://github.com/snap-stanford/biomni)
- **Access boundary:** the official full text was not accessible in this run; no PDF, main figure, full method, or supplement claim is presented as assessed.

## 02 One-Sentence Summary

[Paper] Biomni combines LLM reasoning, action discovery, retrieval-augmented planning, and code execution to compose biomedical workflows without task-specific templates, with abstract-level evidence spanning heterogeneous reasoning tasks and real-world case studies. [Paper: Abstract]

## 03 Research Question

- [Paper] Can one biomedical agent dynamically assemble tools, databases, protocols, and code into workflows across many research domains without task-specific tuning? [Paper: Abstract]
- [Analysis] The unresolved deployment question is whether the same breadth remains reliable when tools fail, evidence conflicts, tasks are prospectively authored, and outputs require wet-lab confirmation.

## 04 Research Background and Development Path

1. [Paper] Biomedical research contains repetitive, fragmented workflows. [Paper: Abstract]
2. [Paper] Biomni maps a biomedical action space by mining tools, databases, and protocols from thousands of publications across 25 domains. [Paper: Abstract]
3. [Paper] It joins retrieval-augmented planning with code-based execution and dynamically composes workflows. [Paper: Abstract]
4. [Analysis] The central shift is from a fixed task assistant to a tool environment whose action space can be expanded and reused; the full-text controls for action quality are not assessable here.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Fragmentation | Researchers move among databases, software, protocols, and manual handoffs | The biomedical action space is dispersed | [Paper: Abstract] |
| Task heterogeneity | One template does not cover causal genes, drugs, diagnoses, microbiomes, and cloning | Workflows require different tool compositions | [Paper: Abstract] |
| Action discovery | The useful tool set changes across domains | Static tool libraries are incomplete | [Paper: Abstract] |
| Experimental grounding | Fluent recommendations may not be executable or testable | Scientific value requires data or laboratory confirmation | [Paper: Abstract] |

## 06 Core Idea

- **Surface method:** an LLM agent with action discovery, retrieval-augmented planning, and code execution. [Paper: Abstract]
- **Core insight:** represent biomedical research as a reusable action space and let the agent compose task-specific workflows at inference time. [Paper: Abstract]
- **General lesson:** [Analysis] breadth should be audited at the level of tools, traces, outputs, and confirmation—not only final-answer plausibility.

## 07 Method Overview

**Abstract-grounded flow:** biomedical objective → retrieve relevant actions and knowledge → plan a workflow → execute code or tools → integrate observations → return an analysis, protocol, or candidate. [Paper: Abstract]

The catalogue describes a configurable LLM backbone and Biomni-R0, while the author repository documents installation, configuration, tools, and Biomni-Eval1. These sources do not substitute for unseen full-text method details. [Paper: Metadata]

**Main workflow figure:** Not assessable from the accessible source. No logo or repository illustration is substituted for a paper figure.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Action-discovery agent | Mines tools, databases, and protocols | Expands coverage across 25 domains | Publications → action catalogue | [Paper: Abstract] | Full ablation not assessable |
| Retrieval-augmented planner | Selects relevant knowledge and actions | Avoids fixed task templates | Objective + catalogue → plan | [Paper: Abstract] | Full ablation not assessable |
| Code-based execution | Runs computational steps | Converts plans into inspectable operations | Plan → results / files | [Paper: Abstract] | Execution-validity controls not assessable |
| Biomni-R0 | Dedicated biological reasoning model | Supports domain reasoning | Task context → reasoning output | [Paper: Metadata] | Training and ablation details not assessable |

## 09 Essential Formulas and Symbols

Not assessable from the accessible source. No equations are inferred from the abstract or code repository.

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Heterogeneous benchmark | Generalization across biomedical reasoning tasks | Strong performance is reported across causal gene prioritization, drug repurposing, rare-disease diagnosis, microbiome analysis, and molecular cloning | Breadth is demonstrated at abstract level | Universal superiority or leakage-free evaluation | [Paper: Abstract] |
| Biomni-Eval1 | Biological reasoning over 10 tasks | Repository reports 433 instances | A concrete benchmark is released | Benchmark validity or full comparative statistics | [Paper: Metadata] |
| Real-world case studies | Whether workflows produce usable scientific outputs | Abstract reports multimodal analysis, protein-stability optimization, wet-lab orchestration, and testable protocols | Feasibility across varied cases | Autonomous discovery without expert or laboratory oversight | [Paper: Abstract] |

Main result figures, uncertainty, baselines, and ablations are not assessable from the accessible source.

## 11 Correct Interpretation of the Conclusions

- The abstract supports heterogeneous task coverage, not unrestricted biomedical competence. [Paper: Abstract]
- Biomni's released environment and code improve inspectability, but code availability alone does not validate every scientific output. [Analysis]
- Training trajectories for Biomni-R0 and evaluation instances must remain provenance-separated; the full-text split and contamination controls are not assessable here. [Analysis]
- Wet-lab orchestration is evidence of integration, not permission for unsupervised laboratory operation. [Analysis]

## 12 Limitations Explicitly Acknowledged by the Authors

Not assessable from the accessible source. The abstract does not provide a formal limitations section, and unseen full-text limitations are not reconstructed.

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| A mined action space can import stale or unsafe procedures | Discovery is not validation | Tool quality bounds workflow quality | Version, license, and expert-audit every action; inject deprecated tools | [Paper: Abstract] |
| Broad benchmarks can mix task validity with retrieval advantages | Hidden overlap may inflate results | Generalization claims depend on clean provenance | Time-split tasks and audit source overlap | [Paper: Metadata] |
| Code execution can produce technically valid but scientifically invalid analyses | Runtime success is not epistemic correctness | Errors can propagate into experiments | Independent executable tests plus domain-expert adjudication | [Paper: Abstract] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: treat the action catalogue as a governed scientific dependency with version, provenance, licence, and safety metadata.
- Agent-derived knowledge candidate: evaluate tool selection, parameterization, execution, interpretation, and final claim separately.
- Agent-derived knowledge candidate: pair benchmark breadth with prospective tasks authored after the system and dataset freeze.

## 15 Connections to Existing Knowledge

[Analysis] Biomni combines two recurring agent patterns: retrieval over a structured tool environment and iterative code execution. Its distinguishing abstract-level emphasis is action-space discovery across biomedical domains. Priority and closest-prior-work claims require a dedicated full-text and literature comparison.

## 16 Research Ideas

### Agent-derived research candidate

**Prospective, provenance-locked Biomni evaluation.** [Hypothesis] Requiring every selected action to carry versioned provenance and an executable validation test will reduce scientifically invalid outputs without eliminating most task completion. Delta: add a provenance gate before execution and a result-validation gate afterward. Validation: 100 newly authored tasks across at least five domains, matched model/tool budget, blinded expert adjudication, and endpoints for completion, execution validity, claim validity, cost, and severe error. Falsifier: no reduction in invalid outputs or an unacceptable loss of completion. Failure modes: incomplete provenance, expert disagreement, tool nondeterminism. Innovation status: unverified; prior-art search required.
