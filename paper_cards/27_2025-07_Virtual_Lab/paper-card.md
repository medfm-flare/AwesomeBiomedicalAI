# Paper Card: The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies

> Source coverage: Full official Nature HTML with all five main figures; PDF unavailable
>
> Extraction confidence: High for HTML structure, captions, and main text
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Discovery
>
> Context verification: Official Nature article and author code repository
>
> Card completeness: Complete relative to the official HTML main article

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| Virtual Lab | AI–human collaboration led by an LLM Principal Investigator agent | Preserve capitalization |
| PI agent | Principal Investigator agent | Distinguish from human researcher |
| scientist agent | role-specialized LLM team member | Do not imply independent legal or scientific agency |
| ESM / AlphaFold-Multimer / Rosetta | protein-language, structure-prediction, and molecular-modelling tools | Treat as tools within the design pipeline |
| nanobody | single-domain antibody fragment | Use the paper's term consistently |

## 01 Basic Information

- **Title:** The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies
- **Authors:** Kyle Swanson, Wesley Wu, Nash L. Bulaong, John E. Pak and James Zou. [Paper: Metadata]
- **Venue:** *Nature* 646, 716–723 (2025); published 29 July 2025. [Paper: Metadata]
- **DOI:** [10.1038/s41586-025-09442-9](https://doi.org/10.1038/s41586-025-09442-9)
- **Code / records:** [zou-group/virtual-lab](https://github.com/zou-group/virtual-lab)
- **Access:** official HTML main text and figures; PDF unavailable in this run.

## 02 One-Sentence Summary

[Paper] A human-guided team of LLM agents built an ESM–AlphaFold-Multimer–Rosetta nanobody-design pipeline, proposed 92 SARS-CoV-2 nanobodies, and experimentally identified candidates with improved binding to JN.1 or KP.3 while retaining ancestral-spike binding. [Paper: Abstract; Figure 4]

## 03 Research Question

- [Paper] Can a role-specialized LLM team, with high-level human guidance, perform an open-ended interdisciplinary project that culminates in experimentally testable molecular designs? [Paper: Introduction]
- [Analysis] The central causal question is which part of the observed discovery value comes from multi-agent collaboration, the human researcher, pretrained protein tools, the search budget, or ordinary iterative engineering.

## 04 Research Background and Development Path

1. [Paper] Scientific teams benefit from interdisciplinary expertise, but access to such teams is uneven. [Paper: Introduction]
2. [Paper] Earlier LLM applications largely answered bounded questions rather than conducting open-ended projects. [Paper: Introduction]
3. [Paper] The Virtual Lab assigns a PI agent, scientist agents, and a scientific critic to structured meetings, while a human provides high-level feedback. [Paper: Figure 1]
4. [Paper] The system applied this organization to a real nanobody-design and experimental-validation workflow. [Paper: Figures 2–4]

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Interdisciplinary coordination | Protein sequence, structure, modelling, and assay expertise must be combined | Individual researchers may lack every speciality | [Paper: Introduction] |
| Open-ended planning | The path from objective to experiment is not a fixed QA task | Research requires iterative decisions and critique | [Paper: Figure 1] |
| Design search | Nanobody mutations must balance several computational signals | No single score captures binding and developability | [Paper: Figures 2–3] |
| Experimental truth | Computational rankings can fail in wet-lab assays | Predicted structure or score is not binding evidence | [Paper: Figure 4] |

## 06 Core Idea

- **Surface method:** a PI agent leads specialist agents through team and individual meetings with a scientific critic and human feedback. [Paper: Figure 1]
- **Core insight:** use role assignment and deliberation to let an LLM team assemble and iterate an interdisciplinary computational pipeline. [Paper: Figures 1–2]
- **General lesson:** [Analysis] autonomous-looking discovery should be decomposed into human decisions, agent decisions, pretrained tool outputs, and wet-lab confirmation.

## 07 Method Overview

**Flow:** human objective and feedback → PI agent selects roles → team / individual meetings → tool and pipeline design → nanobody mutation proposal → ESM, AlphaFold-Multimer, and Rosetta scoring → candidate selection → experimental expression and binding assays → interpretation. [Paper: Figures 1–4]

![Figure 1 — Virtual Lab architecture](figures/figure-1.png)

*Figure 1 maps the PI agent, specialist scientist agents, scientific critic, meeting types, and the human feedback channel; it defines the system boundary before any biological claim. [Paper: Figure 1]*

![Figure 2 — nanobody-design workflow](figures/figure-2.png)

*Figure 2 connects agent discussion to the ESM–AlphaFold-Multimer–Rosetta pipeline and iterative candidate selection. [Paper: Figure 2]*

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| PI agent | Sets agenda, selects roles, and coordinates meetings | Maintains a coherent research programme | Objective → tasks and decisions | [Paper: Figure 1] | Necessity is not established by a single end-to-end demonstration |
| Scientist agents | Contribute domain-specific proposals | Provides functional specialization | Questions → analyses / proposals | [Paper: Figure 1] | Role labels may not guarantee independent expertise |
| Scientific critic | Challenges plans and outputs | Adds error checking | Proposal → critique | [Paper: Figure 1] | Isolation evidence must be read from reported ablations |
| Protein-tool pipeline | Scores and filters nanobody variants | Converts language proposals into molecular candidates | Sequences → computational scores / structures | [Paper: Figures 2–3] | Tool priors can dominate agent contribution |
| Wet-lab validation | Measures expression and binding | Establishes empirical relevance | Candidates → assay outcomes | [Paper: Figure 4] | Tested assays do not establish therapeutic efficacy |

## 09 Essential Formulas and Symbols

No single equation is essential to understanding the agent architecture. The source figures use ESM likelihood-related scores, AlphaFold confidence metrics, Rosetta energy-related scores, and combined weighting; their exact definitions and normalization should be taken from the Methods and figure captions rather than inferred here. [Paper: Figures 2–3]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Comparison / conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Computational design | Can the workflow produce ranked mutant nanobodies? | Four parental nanobodies, iterative mutation and multi-tool scoring | 92 designs advanced to experimental testing | The pipeline generated a tractable candidate set | Scores alone predict binding or developability | [Paper: Figures 2–3] |
| Experimental validation | Do proposed nanobodies express and bind spike variants? | Multiplexed binding assays across ancestral and variant RBDs | A range of functional binders; two candidates improved JN.1 or KP.3 binding while retaining ancestral binding | Some AI–human designs have promising binding profiles | Therapeutic efficacy, neutralization, or in-vivo protection | [Paper: Figure 4] |
| Discussion analysis | How did roles and meetings contribute to the process? | Word / action distributions and meeting records | Distinct role participation is documented | The workflow is inspectable | Role specialization caused the biological outcome | [Paper: Figure 5] |

![Figure 3 — Nb21 computational analysis](figures/figure-3.png)

*Figure 3 shows the multi-score computational narrowing of Nb21 variants; it supports candidate ranking, not experimental binding. [Paper: Figure 3]*

![Figure 4 — experimental validation](figures/figure-4.png)

*Figure 4 is the key biological evidence because it moves from predicted candidates to measured binding profiles. [Paper: Figure 4]*

![Figure 5 — discussion analysis](figures/figure-5.png)

*Figure 5 audits participation and workflow behaviour; communication volume should not be interpreted as scientific contribution without causal ablation. [Paper: Figure 5]*

## 11 Correct Interpretation of the Conclusions

- The work is an AI–human collaboration: a human provides high-level feedback and the experimental team supplies the wet-lab infrastructure. [Paper: Figure 1]
- The computational toolchain uses strong pretrained models and software; the study does not isolate all value attributable to the LLM team. [Paper: Figure 2]
- Ninety-two designs and successful binding candidates demonstrate feasibility, not a general success probability for open-ended research. [Paper: Figure 4]
- Improved binding to selected RBD variants is not equivalent to viral neutralization, therapeutic safety, manufacturability, or clinical benefit. [Analysis]

Bounded restatement: the study shows that a structured human-guided LLM team can assemble a computational nanobody pipeline that yields experimentally functional candidates in one project.

## 12 Limitations Explicitly Acknowledged by the Authors

| Limitation | Specific manifestation | Future direction | Source |
|---|---|---|---|
| Human involvement remains integral | High-level feedback and physical experiments are provided by people | Study different oversight levels and more automated laboratory integration | [Paper: Figure 1; Discussion] |
| One project domain | The end-to-end demonstration concerns SARS-CoV-2 nanobody design | Evaluate other interdisciplinary questions and teams | [Paper: Discussion] |
| Tool and model dependence | The workflow depends on selected LLM and protein tools | Compare models, role structures, and toolchains | [Paper: Discussion] |

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Pretrained protein tools may explain much of the design quality | Agent contribution is confounded with tool strength | Attribution determines what generalizes | Compare agentic, scripted, expert, and random-search pipelines under matched tool calls | [Paper: Figure 2] |
| One successful project is selection-sensitive | Failed or abandoned projects are not represented | Success rate across objectives is unknown | Preregister a portfolio of projects and publish all outcomes | [Paper: Figures 2–4] |
| Binding is an intermediate endpoint | Molecular efficacy requires additional assays | Stronger claims could be biologically premature | Add neutralization, stability, aggregation, developability, and in-vivo tests | [Paper: Figure 4] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: use role and meeting records as process evidence, but require causal ablations before attributing outcome gains.
- Agent-derived knowledge candidate: separate computational prioritization from wet-lab confirmation in both text and figures.
- Agent-derived knowledge candidate: preregister project portfolios so failed research attempts remain visible.

## 15 Connections to Existing Knowledge

[Analysis] The Virtual Lab combines multi-agent deliberation with established protein-design tools and a lab-in-the-loop endpoint. Its strongest methodological connection is to closed-loop discovery systems: language agents organize the search, specialized models score candidates, and experiments determine which claims survive.

## 16 Research Ideas

### Agent-derived research candidate

**Matched attribution study for agentic molecular design.** [Hypothesis] A structured multi-agent team will improve experimentally validated hit rate over a single-agent and scripted pipeline when all groups share the same protein tools and compute budget. Delta: replace a single end-to-end demonstration with randomized, preregistered attribution across multiple targets. Validation: at least ten targets, fixed candidate budget, blinded wet-lab assays, and endpoints for hit rate, diversity, cost, failure recovery, and severe design defects. Falsifier: no gain over scripted or single-agent baselines. Failure modes: assay noise, target heterogeneity, evaluator leakage, excessive meeting cost. Innovation status: unverified; prior-art search required.
