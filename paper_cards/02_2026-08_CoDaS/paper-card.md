# Deep-Reading Paper Card: CoDaS

> **Source coverage:** Full 67-page arXiv v2 paper, including appendices, 18 figures and 12 tables; no independent row-level datasets were supplied  
> **Extraction confidence:** High after manual review of every figure/table page and correction of extraction artefacts  
> **Locator mode:** page-grounded; `PDF p.` denotes the physical page in arXiv v2  
> **Primary analytical lens:** Methods / data-science-agent evaluation  
> **Secondary analytical lens:** Clinical biomarker evidence boundaries  
> **Context verification:** Official arXiv record checked on 9 September 2026; not a systematic review of digital biomarkers  
> **Card completeness:** Complete relative to the supplied source

`[Paper]` denotes author-reported evidence, `[Analysis]` this card's interpretation, and `[Hypothesis]` an unvalidated proposal. “Candidate biomarker” is deliberately not shortened to “validated biomarker.”

### Terminology ledger

| Term | Meaning used here |
|---|---|
| CoDaS | AI Co-Data-Scientist: multi-agent orchestration around deterministic statistical/ML tools and report generation |
| Participant-observation | A cohort observation/wave; not necessarily a unique person |
| Screened / conditional / exploratory | Internal prioritization states; none means clinically validated |
| Fact Sheet | Structured store of reportable numerical results used to constrain writing |
| Validity / added value / confidence to act | Separate clinician-rating constructs that must not be collapsed into one score |

## 01 Basic information

| Field | Details |
|---|---|
| Title | *An AI Co-Data-Scientist for Prioritizing Candidate Biomarkers from Wearable Sensor Data* |
| Authors | Yubin Kim, Salman Rahman, Samuel Schmidgall, et al. (36 authors) |
| Source / date | arXiv:2604.14615v2; first submitted 16 April 2026, revised 19 June 2026 |
| Official record | [arXiv abstract](https://arxiv.org/abs/2604.14615) and [v2 record](https://arxiv.org/abs/2604.14615v2) |
| System | CoDaS, using pretrained Gemini models plus deterministic statistical and machine-learning tools |
| Data | DWB: 7,497 people; GLOBEM: 704 waves from 497 people; WEAR-ME: 1,078 people; total 9,279 participant-observations but 9,072 unique people |
| Outcomes | Depression-related questionnaire outcomes and insulin resistance; several cohorts use different instruments or feature definitions |
| Availability | Sensitive cohort data and parts of the code/infrastructure are restricted; access is conditional on original data terms or reasonable request. [Paper: PDF pp.44-45] |
| Read on | 31 August 2026; bibliographic record refreshed 9 September 2026 |

## 02 One-sentence summary

CoDaS organizes hypothesis generation, deterministic statistical/ML execution, an 11-check validation battery, adversarial Critic/Defender review, literature interpretation and Fact-Sheet-constrained reporting to prioritize wearable candidate biomarkers; it produces several internally stable associations and modest DWB/WEAR-ME prediction gains, but the study is exploratory and unregistered, cross-cohort “replication” often changes measurements, GLOBEM prediction is near chance, expert preference is confounded by unequal compute, and clinician ratings support plausibility more than actionability. [Paper: PDF pp.2, 20-25, 28-43]

## 03 Research question

Can an AI co-data-scientist turn large wearable datasets into traceable, reviewable candidate associations while separating calculation from language generation, screening leakage and instability, and exposing the result to research and clinical experts? The correct endpoint is prioritization for follow-up—not autonomous biomarker validation or patient-level decision-making. [Paper: PDF pp.2-6, 44]

## 04 Research background and development path

Wearables yield dense behavioural and physiological measurements, but useful candidates require outcome definition, missing-data decisions, feature construction, participant-level validation, robustness checks, construct review, literature interpretation and readable reporting. CoDaS places LLM agents around deterministic runners rather than asking one model to infer statistics from raw text. This improves traceability but still permits an adaptive search path because model agents read intermediate summaries and decide what to test next. [Paper: PDF pp.3-12] [Analysis]

## 05 Core pain points identified by the paper

| Problem | Why it matters | CoDaS response | Remaining boundary |
|---|---|---|---|
| Labels and proxies can leak | Outcome components or near-identities can inflate performance | Target screening, correlation threshold and construct gates | Summary-guided iteration may still adapt to evaluation feedback [Paper: PDF pp.9-11] |
| Statistical significance can be clinically redundant | A strong association may reproduce the outcome definition | Critic/Defender and construct review | Clinical redundancy remains expert- and context-dependent [Paper: PDF pp.23-24] |
| Generated prose can drift from calculations | Numbers may be rounded, altered or selectively reported | Fact Sheet, report gates and numeric checking | Suppressed failures may become less visible without a complete candidate ledger [Paper: PDF p.12] |
| One aggregate score hides different evidence levels | Internal stability, expert preference and actionability are not the same | Six benchmark axes and separate clinician dimensions | The axes use different units and cannot be summed as one clinical score [Paper: PDF pp.25, 36] |
| Agent comparisons use unequal resources | More search can improve a report regardless of architecture | Runtime/token reporting | The reported baselines are not compute-matched [Paper: PDF p.52, Table 7] |

## 06 Core idea

The system separates language-agent roles from deterministic execution: a data layer describes the dataset; Scout and Researcher agents propose directions; statistical and ML runners compute effects and predictions; a validation runner applies up to 11 checks; Critic and Defender dispute leakage, confounding and construct redundancy; literature agents ground interpretation; the Fact Sheet constrains the final report. Shared memory keeps the state visible across stages. [Paper: PDF pp.5-12, 51]

## 07 Method overview

User objective/data → DataLoader and EDA → hypotheses and analysis plan → statistical and ML loops → validation battery → adversarial review → literature/mechanism interpretation → Fact Sheet → parallel report agents → numerical audit and human review. [Paper: PDF pp.5-8]

![Figure 1 — problem, system and evaluation overview](figures/page-002.png)

Figure 1 is a compact summary, not a single composite validation endpoint. The 9,279 count is participant-observations, the radar axes use different definitions, 57% is willingness to retain content rather than measured clock time, and 10/21 accept-or-minor is different from 18/21 non-reject. [Paper: PDF p.2]

![Figure 2 — high-level architecture](figures/page-005.png)

![Figure 8 — detailed stages and data flow](figures/page-051.png)

## 08 Core module breakdown

| Module | Function | Evidence boundary |
|---|---|---|
| DataLoader / EDA | Defines units, outcomes, missingness and descriptive structure | A correct description does not remove cohort-specific bias [Paper: PDF pp.5-6] |
| Scout / Researcher ensemble | Proposes candidate features and next analyses | Human prompts and repeated feedback constrain what counts as “autonomous” [Paper: PDF pp.5-6] |
| Stat Runner | Computes univariate effects, tests and robustness summaries | Multiple adaptive rounds complicate global false-discovery control [Paper: PDF pp.6, 19] |
| ML Runner | Participant-level cross-validation with ridge/tree models | Internal CV is not external validation [Paper: PDF pp.6, 9-10] |
| Leakage protection | Removes direct targets/proxies; flags absolute Spearman correlation >.85 | It limits obvious leakage but does not prove the whole adaptive pipeline is independent [Paper: PDF pp.9-10] |
| Eleven-check battery | Tests holdout confirmation, permutation, bootstrap, leave-one-out, subgroup and construct/CI criteria | Checks are conditional; passing count alone does not determine final status [Paper: PDF pp.10-11, 64-66] |
| Critic / Defender | Challenges confounding, leakage and redundancy | Strong internal statistics can still be rejected, as with glucose_sq or TG/HDL [Paper: PDF pp.23-24] |
| Fact Sheet / report gates | Freezes reportable values and suppresses invalid tables | Reduces transcription drift but needs a visible full failure ledger [Paper: PDF p.12] |

## 09 Essential formulas and symbols

The paper's contribution is procedural rather than a new named mathematical model. Spearman `rho` measures rank association; `Delta R^2` is the incremental explained variance after adding candidates; AUC measures ranking discrimination and is not accuracy. A correlation of `.252` is not “25.2% accuracy.” [Paper: PDF pp.19, 39-40]

The automated source inventory labelled an enumerated output item on PDF p.6 as **Equation 2**. Manual page review shows that it is not a mathematical equation, so this card records it as an extraction false positive rather than inventing a formula. [Paper: PDF p.6] [Analysis]

Simple constructed candidates include `steps / resting-heart-rate` and laboratory ratios such as `AST / ALT`. A data-driven name such as “fitness index” does not turn a wearable ratio into a cardiopulmonary exercise test, and laboratory-inclusive results are not wearable-only results. [Paper: PDF pp.21, 25, 65]

Inter-rater coefficients answer different questions: ordinal alpha reflects absolute/ordinal agreement, ICC(3,k) the reliability of an average of `k` fixed raters, and Kendall's W rank concordance. A high 12-rater-average ICC can coexist with weak single-rater agreement. [Paper: PDF pp.33, 36, 67]

## 10 Experimental design and evidence chain

### 10.1 Cohorts and predictive results

| Cohort | Unit / outcome | Main result | Correct boundary |
|---|---|---|---|
| DWB | 7,497 people; PHQ-8 depression | Sleep-duration variability `rho=.252`, p<.001; demographic-model R² .188→.228 (`Delta=.040`) | Internal association and modest prediction gain, not diagnosis or causality [Paper: PDF pp.20, 23, 39] |
| GLOBEM | 704 waves from 497 people; PHQ-4 | Sleep-onset variability `rho=.126`, p<.001; main AUC .535 | Related construct with different operationalization; main discrimination is near chance [Paper: PDF pp.20, 22-23, 40] |
| WEAR-ME | 1,078 people; HOMA-IR | Wearable-only R² .260→.281 (`Delta=.021`); laboratory-inclusive model .389 | The larger value is not wearable-only and no clinical threshold is validated [Paper: PDF pp.21, 39-40] |

![Figure 3 — sleep-instability associations](figures/page-023.png)

The large distribution overlap and different features/outcomes preclude an individual diagnostic rule or exact cross-cohort replication claim.

### 10.2 Agent and expert evaluation

CoDaS is evaluated on six heterogeneous benchmarks, against other agent systems, through blinded research-expert review and with a separate 12-clinician panel. These layers should remain separate rather than averaged. [Paper: PDF pp.25-38]

![Figure 9 — six general benchmarks](figures/page-056.png)

Reported benchmark point estimates include HealthBench .724, HealthBench Hard .391, DSBench 64.0%, DataSciBench 77.5%, DSGym 84.4% and DiscoveryBench HMS .32. The comparators differ in model, tools, feedback and budget and the figure has no uncertainty bars. [Paper: PDF pp.25, 56]

![Figure 4 — blinded research-expert evaluation](figures/page-028.png)

The mean quality score is 3.74/5. Editorial recommendations are 2 accept, 8 minor, 8 major and 3 reject. Thus 18/21 are non-reject, but only 10/21 are accept-or-minor. The reported 56.9% is a subjective content-retention estimate, not observed time saved. [Paper: PDF pp.28-30]

![Figure 5 — estimated human effort](figures/page-032.png)

Thirty-four responses estimate 37±23 person-days (range 5-90) for an analogous human workflow. This is not a randomized timing comparison with the agent. [Paper: PDF p.32]

![Figure 6 — research-expert agreement](figures/page-033.png)

Overall ordinal alpha is .443, ICC(3,k) .888 and Kendall W .503. These statistics describe different agreement properties and do not imply strong reliability of an arbitrary single reviewer. [Paper: PDF p.33]

![Figure 7 — clinician ratings and disagreement](figures/page-036.png)

Clinician judgements align with confidence tiers (`rho=.67`, p=.005), but mean added clinical value and confidence to act are much lower (about 2.37 and 2.34). Twelve clinicians and the reported specialty mix are not a prospective utility study. [Paper: PDF pp.36-38]

### 10.3 Interface and held-out mechanism checks

![Figure 10 — expert profile form](figures/page-057.png)

![Figure 11 — anonymized review instructions](figures/page-058.png)

![Figure 12 — paper and anchored quality scales](figures/page-059.png)

![Figure 13 — editorial, safety and effort fields](figures/page-059.png)

![Figure 14 — forced four-system ranking](figures/page-060.png)

![Figure 15 — workload anchor and PHQ label mismatch](figures/page-061.png)

![Figure 16 — requested follow-up validation](figures/page-062.png)

![Figure 17 — open feedback field](figures/page-063.png)

![Figure 18 — two validation checks on held-out data](figures/page-063.png)

The interface figures establish what reviewers could see and score, not the frequency of every response. Figure 15 labels the DWB target PHQ-9, whereas the main paper/tables use PHQ-8; the PDF cannot establish which form version each reviewer saw. Figure 18 tests two checks, not all 11: several robustness measures improve, while held-out R² changes only +.002 in DWB and -.007 (not significant) in WEAR-ME. [Paper: PDF pp.53-55, 57-63, 66]

### 10.4 Resource comparison

Reported usage is approximately 8.28 hours and 7.2 million input tokens for CoDaS, compared with about 11.6 minutes/99,000 for Biomni and 2.76 minutes/1,200 for ADK in the reported configurations. This makes architecture-only attribution unsafe. [Paper: PDF p.52, Table 7]

### 10.5 Complete main-table inventory

- **Table 1** defines cohorts, units, modalities and outcomes; **Table 2** summarizes candidate counts/statuses; **Table 3** reports principal associations and uncertainty; **Table 4** separates main and post hoc prediction results. [Paper: PDF pp.13, 39-40]
- **Table 5** and **Table 6** report research- and clinician-review results; **Table 7** reports runtime/token budgets. These are different evidence layers and should not be pooled into one quality score. [Paper: PDF pp.41-42, 52]
- **Table 8**, **Table 9** and **Table 10** preserve screened, conditional, exploratory, rejected, unstable and sign-reversing candidates; passing all checks is not sufficient for every final status. [Paper: PDF pp.64-66]
- **Table 11** gives the two-check held-out experiment, including the small/non-significant prediction changes; **Table 12** separates single-rater from average-rater agreement. [Paper: PDF pp.66-67]

## 11 Correct interpretation of the conclusions

Evidence supports a traceable workflow that connects computational outputs, construct criticism, literature interpretation and human-reviewable reports. It also supports internally stable candidate associations and small predictive gains in two cohorts, plus a research-expert preference for the produced reports. [Paper: PDF pp.20-21, 28-30]

It does not show that every candidate passed 11 checks, that one operational biomarker replicated unchanged across cohorts, that wearable-only data yield the laboratory-inclusive performance, that 86% of real submissions would be accepted, that 57% of labour was measured as saved, or that patient outcomes improve. “Candidate prioritization” is the defensible description. [Paper: PDF pp.36, 40, 42, 64-66] [Analysis]

## 12 Limitations explicitly acknowledged by the authors

- Analyses are exploratory and unregistered; GLOBEM has severe missingness, repeated observations, endpoint choices and weak signal. [Paper: PDF pp.42-43]
- The populations, modalities and static mental-health/metabolic endpoints are limited; external/prospective clinical validation is absent. [Paper: PDF pp.42-43]
- Mechanistic explanations may be post hoc, and measured features remain affected by medication, activity and other confounders. [Paper: PDF pp.42-43]
- The fixed role topology, model/platform dependence and proprietary infrastructure constrain portability and reproduction. [Paper: PDF pp.43-45]
- Clinician-panel size, specialties and rating scales limit claims about general clinical actionability. [Paper: PDF pp.36-38]
- Sensitive DWB data are closed, GLOBEM/WEAR-ME remain subject to original access terms, and full code/prompts/runtime are not an unrestricted reproducibility package. [Paper: PDF pp.44-45]

## 13 Critical analysis

1. **Execution discipline is stronger than endpoint novelty.** Target shielding, Fact Sheets, hard gates and retained failures are useful engineering controls, but should be evaluated by error interception, false rejection and supervision cost—not only R² or prose quality. [Paper: PDF pp.12, 24] [Analysis]
2. **Hidden labels are not the same as a non-adaptive search.** Agents read statistical summaries and choose later tests; per-round BH correction does not automatically control the full dynamically generated hypothesis family. [Paper: PDF pp.9, 19] [Analysis]
3. **Compute is a major alternative explanation.** CoDaS uses orders of magnitude more time/tokens than several baselines. Equal-model, equal-tool and equal-budget comparisons are needed for architectural causality. [Paper: PDF p.52] [Analysis]
4. **Human ratings have dependency and wording issues.** Fifteen research experts repeat ratings across three datasets; 21 versus 13 evaluations are unbalanced; “effort saved” wording and the PHQ-9 interface label could alter interpretation. Raw nested ratings would be needed to quantify impact. [Paper: PDF pp.29, 59, 61] [Analysis]
5. **Some validation outcomes resemble their screening criteria.** Held-out versions show limited transfer for two checks but not complete independent biological validation; predictive gains are small or inconsistent. [Paper: PDF pp.53-55, 66] [Analysis]
6. **Negative results are part of the method.** Near-chance GLOBEM prediction, sign reversal, TG/HDL redundancy and unchanged WEAR-ME held-out R² should remain visible in the final candidate ledger. [Paper: PDF pp.12, 40, 66] [Analysis]

## 14 Knowledge learned

An agent can be correct at several different levels: code execution, numerical calculation, internal stability, construct plausibility, expert interest, clinical actionability and patient benefit. CoDaS provides evidence mainly for the early levels and expert review, not the last. Passing more checks is less important than whether hard gates can reject the right failure types. [Paper: PDF pp.8, 11, 24, 36] [Analysis]

Five denominator/version distinctions change the conclusion: 9,279 observations versus 9,072 people; 18/21 non-reject versus 10/21 accept/minor; average-rater ICC versus single-rater reliability; primary GLOBEM AUC .535 versus post hoc .694; and 8.28 machine hours versus an estimated 37 human person-days. [Paper: PDF pp.13, 28, 32, 40, 52, 67]

## 15 Connections to existing knowledge

For biomedical planning agents, the transferable design is to freeze case identity and hard constraints, let deterministic tools generate structured measurements, and restrict the language model to interpretation and reporting. A Fact Sheet could store geometry, safety margins, candidate status and human-review state. CoDaS does not test anatomy segmentation, 3D pose optimization, surgical margins or postoperative outcomes, so it cannot validate those components. [Paper: PDF pp.5-12] [Analysis]

Its separation of statistical validity, added clinical value and confidence to act is also a useful evaluation principle: geometric validity, clinician acceptability, workflow efficiency and patient benefit should not be collapsed into one score. No project-specific endpoint or threshold is adopted here. [Paper: PDF p.36] [Analysis]

## 16 Research ideas

**Innovation status:** unverified; the following are `[Hypothesis]` candidates, not author conclusions or approved project changes.

1. **Compute-matched pipeline test.** Hypothesis: after fixing model, tools, tokens, wall time and retry limits, the Fact Sheet plus construct gates will still reduce high-severity errors without excessive rejection. Validation: freeze tasks with auditable leakage/redundancy traps and compare a single agent, rule pipeline, full CoDaS-style workflow and targeted ablations; report error classes and cost. Failure criterion: benefit disappears under matched budget or valid candidates are rejected at an unacceptable rate. [Paper: PDF pp.40, 52]
2. **Frozen external confirmation of identical candidate definitions.** Hypothesis: locking feature definition, missing-data handling, outcome and direction before an unseen cohort will retain fewer but more credible candidates. Validation: publish the full adaptive search ledger, map identical measurements to a new cohort once, and test direction, incremental prediction and calibration without feeding failures back. Failure criterion: sign reversal, near-zero gain or success only after redefining the feature. [Paper: PDF pp.23, 66]
3. **Planning Fact Sheet rather than LLM safety judgement.** Hypothesis: tool-generated case/site identity, geometry and constraint status, with the LLM restricted to explanation, will reduce missed hazardous candidates. Validation: an isolated test set with geometry errors, identity mismatches and boundary cases; compare manual, rule-only and rule-plus-explanation workflows on misses, false alarms and review time. Failure criterion: no safety gain, slower review, or shared measurement errors. [Paper: PDF pp.6, 12]

**Possible failure modes across the proposals:** the external cohort may not support identical measurements, the audit traps may be artificial, or the deterministic measurement layer may share the same upstream data and coordinate errors as the agent.

