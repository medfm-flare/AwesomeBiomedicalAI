# Initial lessons from real-world implementation of an AI-agent eye clinic in China

> **Source coverage:** Complete institution-authorized HTML article + official Supplementary Information + publisher Figures 1–2
> **Extraction confidence:** Mixed (article text, figures and reported numbers are available; the standalone Table 1 layout was not exported)
> **Locator mode:** structure-grounded
> **Primary analytical lens:** Review / commentary
> **Secondary analytical lens:** Clinical implementation
> **Context verification:** Externally verified
> **Card completeness:** Partial because Table 1 could not be checked cell by cell

## 01 Basic Information

- **Title:** Initial lessons from real-world implementation of an AI-agent eye clinic in China
- **Authors:** Tao Yan, Di Zhang, Luxiao Chen, Taizhangtian Ma, Chunyang Tang, Zhe Pan, Ziyao Xia, Yiming Qin, Zehua Jiang, Haoyang Liu, Mengda Li, Wan Lu, Junyi Wang, Chendi Li, Chen Xin, Siyong Lin, Chun Zhang, Peng Liu, Jiamin Wu, Ya Xing Wang, Qionghai Dai & Tien Yin Wong
- **Venue / type:** *Nature Medicine*, Comment
- **Published:** 10 September 2026
- **DOI:** [10.1038/s41591-026-04631-z](https://doi.org/10.1038/s41591-026-04631-z)
- **Article:** [Nature Medicine](https://www.nature.com/articles/s41591-026-04631-z)
- **System:** AI-Agent Augmented Tsinghua Eye Clinic (AI-TEC)
- **Deployed models:** Qwen3.5-35B and RETFound; exact versions and tuning settings are not fully reported
- **Code / case-level data:** Not reported as publicly available
- **Reading date:** 2026-09-20

### Terminology ledger

| Canonical term | Meaning |
|---|---|
| AI-TEC | The authors' AI-Agent Augmented Tsinghua Eye Clinic framework |
| deployed prototype | The November 2025 early deployment containing pre-consultation and triaging agents |
| target architecture | The broader Fig. 1b vision, including diagnosis, decision-support, patient-support and Agent X components |
| CFP | Colour fundus photography |
| Annotated Dataset | Ophthalmologist-reviewed CFP data; 1,426 images in prose versus 1,482 in Figure 2 |
| Prospective Dataset 1 / 2 | 472 CFPs (15 Nov 2025–6 Jan 2026) / 348 CFPs (7 Jan–31 Mar 2026) |

## 02 One-Sentence Summary

[Paper] This Comment argues that useful medical AI must be evaluated as a socio-technical care pathway rather than a standalone model, using an early single-centre AI-TEC deployment to show that local expert curation coincided with higher CFP discrimination and that interface friction coincided with large changes in clinical use, while patient outcomes and the full multi-agent architecture remain unevaluated. [Paper: Operational lessons from real-world implementation; Conclusion]

## 03 Research Question

**Can coordinated AI agents embedded across pre-consultation, triage, diagnosis, clinician decision support and follow-up convert algorithmic performance into measurable clinical and system value?**

[Analysis] The paper only partially answers this question: it reports two deployed agents, CFP AUROC and passive use snapshots, not a controlled end-to-end evaluation of the complete AI-TEC pathway.

## 04 Research Background and Development Path

| Stage | Evaluation unit | Advantage | Main gap |
|---|---|---|---|
| Standalone medical AI | Classification, risk score or report | Easy offline comparison | Can add review burden without fixing workflow |
| AI-assisted workflow | Clinician plus an added AI output | Preserves clinician control | Often adds clicks and a fragmented information layer |
| AI-native pathway | Multi-agent, longitudinal care process | Can coordinate information and actions | Requires governance, human-factors and outcome evidence |
| Early implementation | Local data, interface, users and monitoring | Exposes deployment failures | Uncontrolled snapshots are vulnerable to confounding |

[External] DECIDE-AI treats small-scale live clinical evaluation as a distinct stage and requires reporting of human factors, workflow and safety, not only accuracy. [DECIDE-AI](https://www.nature.com/articles/s41591-022-01772-9)

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Author explanation | Evidence |
|---|---|---|---|
| Point models do not equal care improvement | Clinicians still integrate fragmented outputs manually | Care is a continuous adaptive system | [Paper: Introduction; Figure 1] |
| Local data quality is unstable | A model tuned on 26,839 historical CFPs underperformed prospectively | Devices, patients, records and diagnostic conventions vary | [Paper: Operational lessons; Figure 2] |
| Reference labels can be ambiguous | AI/reference disagreement may involve comorbidity or secondary diagnoses | One label may not capture the clinical context | [Paper: Supplementary Figure 1] |
| Interface friction suppresses adoption | Examination-level use fell from 25.7% to 3.8% | Loading, clicks and manual entry added work | [Paper: Operational lessons] |
| Technical metrics do not prove value | Silent evaluation cannot observe action; screening does not guarantee completed care | AUROC covers only discrimination | [Paper: Discrepancies; Table 1] |

## 06 Core Idea

1. **Surface proposal:** Assign specialist agents to stages of the ophthalmic patient journey and coordinate them through an Agent X layer.
2. **Core claim:** The proper evaluation unit is `technology + data + workflow + people + governance + monitoring`, not the image model alone.
3. **[Analysis] Strongest empirical lesson:** Local annotation quality and interface design may dominate real deployment even when the underlying model architecture is unchanged.

## 07 Method Overview

**Figure 1 interpretation.** Figure 1 separates the conventional add-on model from the proposed longitudinal architecture. It is a design map, not evidence that every depicted agent was deployed or effective. [Paper: Figure 1]

**Target pathway:** patient history → pre-consultation agent → visual acuity / IOP / CFP → triaging agent → additional tests → diagnosis agent → clinician decision-support agent → ophthalmologist decision → patient-support agent, with Agent X proposed for coordination and learning.

**Actually deployed:** the pre-consultation and triaging agents were integrated into Beijing Tsinghua Changgung Hospital's information system in November 2025. [Paper: Operational lessons from real-world implementation]

## 08 Core Module Breakdown

| Module | Function | Status/evidence | Known effect of removal |
|---|---|---|---|
| Pre-consultation agent | Collects symptoms/history and prepares a summary | Deployed; independent effect not reported | Not assessed |
| Triaging agent | Analyses screening data and CFPs; proposes risk and next tests | Deployed; RETFound AUROC reported | Annotation/feedback versions improved AUROC, but no clean ablation |
| Diagnosis agent | Integrates multimodal examinations | Target architecture only | Not assessed |
| Clinician decision-support agent | Supplies evidence, differentials and management options | Target architecture only | Not assessed |
| Patient-support agent | Education, follow-up and monitoring | Target architecture only | Not assessed |
| Agent X | Cross-agent coordination and adaptive learning | Conceptual only | Not assessed |
| Feedback loop | Expert review and iterative tuning | Associated with AUROC increase | Training/evaluation separation is incompletely reported |

## 09 Essential Formulas and Symbols

No new algorithmic formula is introduced. The key quantities are:

- `examination-level usage = AI-TEC-assisted CFP examinations / all CFP examinations` (206/801 = 25.7% in Dec 2025; 41/1,113 = 3.8% in Apr 2026; 259/1,126 = 23.0% in May 2026). [Paper: Operational lessons]
- `physician participation = physicians who used AI-TEC / physicians on service` (13/29 = 44.8% in Dec 2025). [Paper: Operational lessons]
- Macro-average AUROC summarizes one-vs-rest discrimination but does not establish calibration, clinical utility or patient benefit.

## 10 Experimental Design and Evidence Chain

**Figure 2 interpretation.** On the same 472-image prospective set, tuning with the expert-reviewed dataset is associated with a macro-AUROC increase from 0.7996 to 0.9383. No confidence intervals are shown, and the reported annotated-data count conflicts with the prose. [Paper: Figure 2]

| Evidence | Comparison | Result | Supported conclusion | Unsupported stronger claim |
|---|---|---|---|---|
| Raw versus expert-reviewed tuning data | Same Prospective Dataset 1 | Macro-AUROC 0.7996 → 0.9383 | The updated model discriminated better on this cohort | Improvement is caused only by label quality |
| Feedback-cycle version | Subsequent Prospective Dataset 2 | AUROC 0.9383 → 0.9482 | A later version reports higher AUROC | Stable independent generalization without a frozen test manifest |
| Passive use monitoring | Dec 2025, Apr and May 2026 | 25.7% → 3.8% → 23.0% after interface revision | Adoption changed substantially over time | The click reduction causally produced the rebound |
| Decision-impact pilot | Clinician diagnoses before and after seeing AI | Workflow described; outcomes not reported | Design can measure AI-induced change | AI improved clinician decisions |

**Supplementary Figure 1 interpretation.** Representative cases expose comorbidity, reflection artifacts and threshold ambiguity. They motivate contextual or multi-label adjudication but do not quantify the overall error spectrum. [Paper: Supplementary Figure 1]

**Supplementary Figure 2 interpretation.** The second-opinion design can distinguish correct from harmful changes, but the Comment does not report the sample size or outcomes. [Paper: Supplementary Figure 2]

## 11 Correct Interpretation of the Conclusions

- This is a Comment with an early single-centre implementation snapshot, not a randomized trial.
- The quantitative AUROC belongs to a CFP component, not end-to-end AI-TEC accuracy.
- Only pre-consultation and triaging agents are documented as deployed; the full Figure 1 architecture is aspirational.
- The annotation intervention changes sample selection, size, labels and potentially training details simultaneously.
- Patient outcomes, referral completion, diagnostic change, time, workload, adverse events and fairness remain unreported.

**Bounded conclusion:** The article provides useful early evidence that data curation and interface design matter in an AI-agent clinic, but it does not establish that AI-TEC improves clinical decisions or patient care.

## 12 Limitations Explicitly Acknowledged by the Authors

The article has no standalone Limitations section. Related author-stated constraints are:

| Constraint | Manifestation | Future direction | Source |
|---|---|---|---|
| Early prototype | Only pre-consultation and triaging agents are deployed | Continue iterating from real-world feedback | [Paper: Operational lessons] |
| Reference diagnosis is not absolute truth | Comorbidity and available information can yield reasonable disagreement | Use clinically appropriate reference standards | [Paper: Discrepancies; Supplementary Figure 1] |
| Value endpoints are incomplete | Efficiency, access, referrals, workload, follow-up and outcomes are still being collected | Evaluate workflow transformation and health outcomes | [Paper: Conclusion] |

## 13 Critical Analysis

| [Analysis] Observation | Why it matters | How to test | Basis |
|---|---|---|---|
| Annotated Dataset is 1,426 in prose and 1,482 in Figure 2 | Prevents exact audit and replication | Publish correction and patient/image manifest | [Paper: Figure 2; Operational lessons] |
| No uncertainty for AUROC | Class imbalance and sampling variability are unknown | Patient-level bootstrap CIs and paired tests | [Paper: Figure 2] |
| Adoption evidence is uncontrolled | Time, staffing and case mix may confound the interface effect | Interrupted time series or stepped-wedge evaluation | [Paper: Operational lessons] |
| Feedback and evaluation sets may overlap conceptually | Continuous learning can consume the test distribution | Version hashes, cut-off dates and locked temporal/external tests | [Paper: Operational lessons] |
| Full multi-agent contribution is untested | Coordination could add benefit or propagate error | Compare component tools, uncoordinated agents and coordinated AI-TEC | [Paper: Figure 1] |

## 14 Knowledge Learned

### Agent-derived knowledge candidates

- Separate model discrimination, workflow adoption, decision impact and patient outcome as distinct layers.
- Report both examination-level use and clinician-level participation.
- Keep adaptive feedback data separate from locked evaluation cohorts.
- Use a before/after-AI decision matrix to count correct corrections and harmful changes, not only agreement.
- Treat reasonable expert disagreement as a reference-standard design problem rather than automatic model error.

## 15 Connections to Existing Knowledge

- [External] DECIDE-AI supports the paper's emphasis on early live workflow and human-factor evaluation, but AI-TEC does not yet provide a complete DECIDE-AI-style report. [DECIDE-AI](https://www.nature.com/articles/s41591-022-01772-9)
- [External] FUTURE-AI similarly emphasizes local adaptation, lifecycle monitoring and deployability; AI-TEC provides examples of those needs but not a full governance or fairness audit. [FUTURE-AI](https://www.bmj.com/content/388/bmj-2024-081554)
- [Analysis] For clinical agents, “interaction” should be evaluated as observable decision change, correction, override and burden—not merely as the presence of a chat interface.

## 16 Research Ideas

### Agent-derived research candidates

#### A. Capability–adoption–outcome evaluation stack

- **Origin:** AI-TEC reports AUROC and use but not their connection to decision quality.
- **[Hypothesis]:** Adding case-level correct/harmful change and review-time measures will reveal workflow failures that geometric or discrimination metrics miss.
- **Delta:** Freeze the agent, record clinicians' independent decision, then reveal the system output.
- **Validation:** Measure acceptance, correct correction, harmful change, time and workload with clinician/case clustering.
- **Failure modes:** Learning effects; study interface differs from production; cases are unrepresentative.
- **Innovation status:** Unverified; prior-art search required.

#### B. Continuous-learning / locked-test dual track

- **Origin:** The relationship between Prospective Dataset 2 and feedback training is unclear.
- **[Hypothesis]:** Versioned feedback adaptation paired with an untouched temporal/external test will reveal whether apparent improvement generalizes.
- **Delta:** Publish version hashes, cut-off dates, manifests and rollback rules.
- **Validation:** Track development feedback, internal temporal and external-site performance across versions.
- **Failure modes:** Small external cohorts; workflow drift; biased feedback labels.
- **Innovation status:** Partially checked; lifecycle-monitoring precedents exist.
