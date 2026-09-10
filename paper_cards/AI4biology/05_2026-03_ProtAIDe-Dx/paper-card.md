# Paper Card: A deep joint-learning proteomics model for diagnosis of six conditions associated with dementia

> Source coverage: Open-access full text via PubMed Central (PMC13190262), including Main, Results, Discussion, the ProtAIDe-Dx architecture and loss subsections of Methods, and all main-figure captions
>
> Extraction confidence: High for the main text, the model Methods subsection and figure captions; Supplementary Tables, Supplementary Data and Extended Data are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Clinical evaluation
>
> Secondary analytical lens: Methods
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code
>
> Card completeness: Complete for the main text and the model-definition Methods; the 15 Supplementary Tables and 13 Supplementary Data files are marked where not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| ProtAIDe-Dx | Proteomics-based AI for Dementia Diagnosis; an MLP-based multi-task network over plasma proteomics | The model; distinguish from the ensemble variant |
| GNPC | Global Neurodegenerative Proteomics Consortium v1.3MS, the 19-site development dataset | Development data; BioFINDER-2 is a member site, held out |
| BioFINDER-2 | the external memory-clinic cohort (N = 1,786) with biomarker-supported diagnosis | The only evaluation with a pathology-adjacent ground truth |
| multi-task joint learning | six binary heads trained together, not one six-way softmax | The design choice that makes co-pathology expressible |
| BCA | balanced classification accuracy | The paper's primary metric; AUC is reported as secondary and explicitly cautioned against |
| co-pathology | more than one neurodegenerative pathology in the same patient | The clinical problem the architecture is shaped around |
| leave-one-site-out | training on 18 sites and testing on the held-out one | The honest generalization number, well below cross-validated performance |

## 01 Basic Information

- **Title:** A deep joint-learning proteomics model for diagnosis of six conditions associated with dementia
- **Authors:** Lijun An, … , Jacob W. Vogel (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature Medicine*, 2026-03. [Paper: Metadata]
- **DOI:** [10.1038/s41591-026-04303-y](https://doi.org/10.1038/s41591-026-04303-y)
- **Code:** [DeMONLab-BioFINDER/An_ProtAIDe-Dx](https://github.com/DeMONLab-BioFINDER/An_ProtAIDe-Dx)
- **Cohort:** 17,187 participants (age 70.3 ± 11.5, 53.2% female) across 19 GNPC sites, SomaLogic 7k proteomics (7,595 proteins); external validation on BioFINDER-2 (N = 1,786). [Paper: Abstract; Results; Discussion]
- **Access boundary:** the open-access full text was read via PMC. Supplementary Tables 1–15, Supplementary Data 1–13, Supplementary Results 1–4 and the Extended Data figures were not opened directly and are cited only as the main text describes them.

## 02 One-Sentence Summary

[Paper] ProtAIDe-Dx is a multi-task deep network that reads one plasma proteomic profile and returns simultaneous probabilities for six conditions of aging — control, AD, PD, FTD, ALS and stroke/TIA — reaching 70–95% balanced accuracy in cross-validation, adding diagnostic value on top of existing clinical biomarkers in an external memory clinic, and flagging co-pathology that a single-diagnosis model cannot express. [Paper: Abstract]

## 03 Research Question

- [Paper] Can plasma proteomics from a single blood draw support simultaneous, probabilistic diagnosis across several neurodegenerative conditions, including the co-pathologies that make clinical diagnosis unreliable? [Paper: Main]
- [Analysis] The question the paper actually settles is a negative one, and it settles it carefully: not "can this replace clinical biomarkers" — the authors say plainly it cannot — but "does it add anything they do not already contain". That framing is what makes the result usable.

## 04 Research Background and Development Path

1. [Paper] Disease-modifying therapies have arrived for AD and are in trials for PD and ALS, which raises the cost of getting the diagnosis wrong. [Paper: Main]
2. [Paper] Misdiagnosis runs 25–30% in specialist dementia clinics and can exceed 50% in primary care; 70% of patients aged 80+ carry multiple neurodegenerative pathologies at once. [Paper: Main]
3. [Paper] Blood biomarkers for AD are maturing, but scalable and specific biomarkers for the other conditions do not exist — for most, high-confidence diagnosis is still at autopsy. [Paper: Main]
4. [Paper] Plasma proteomics can survey thousands of candidates from one draw, but the data are high-rank, carry heavy technological artefacts, and the blood–brain barrier limits how many brain-expressed proteins are visible at all. [Paper: Main]
5. [Analysis] The development path is therefore constrained on both ends: the input signal is partly blocked by biology, and the training labels are clinical rather than pathological. The paper's contribution is as much about measuring those ceilings honestly as about the architecture.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Misdiagnosis | 25–30% in specialist clinics, >50% in primary care | Overlapping clinical presentations, no in vivo pathological confirmation | [Paper: Main] |
| Co-pathology | 70% of patients aged 80+ carry several pathologies | Single-diagnosis tooling cannot represent it | [Paper: Main] |
| One biomarker, one disease | Multiple separate tests, often invasive (CSF) | Biomarkers were developed disease by disease | [Paper: Discussion] |
| Missing labels across cohorts | A patient diagnosed with AD may never have been assessed for PD | GNPC aggregates cohorts with different research aims | [Paper: Methods, "ProtAIDe-Dx"] |
| Site effects | Large performance drop from cross-validation to leave-one-site-out | High variation in per-protein effect sizes across sites | [Paper: "Out-of-sample generalization…"; Discussion] |
| Unreliable ground truth | Models trained on clinical diagnoses that mostly lacked biomarker confirmation | GNPC is a retrospective collection with varying diagnostic criteria | [Paper: Discussion] |

## 06 Core Idea

- **Surface method:** an MLP over 7,595 plasma proteins with six binary classification heads trained jointly.
- **Core insight:** the choice of *multi-task over multi-class* is doing two jobs at once. It lets the output represent co-pathology (several probabilities can be high simultaneously), and it lets every patient contribute to every task for which they have a label, instead of forcing imputation or exclusion of the incomplete label vectors that a six-way softmax would require. [Paper: Methods, "ProtAIDe-Dx"]
- **General lesson:** [Analysis] when labels are missing not at random because cohorts were assembled for different purposes, the loss structure is a data-availability decision before it is a modelling decision. The architecture here follows from the shape of the label matrix, not from a hypothesis about proteomics.

## 07 Method Overview

**Flow:** SomaLogic 7k plasma proteomics → per-participant normalization by mean protein level → 10-NN imputation fit on the training split → Gaussian rank normalization fit on the training split → MLP trunk → low-dimensional embedding layer (Z) → six binary heads → per-condition probability. Proteomics only: no site, demographic, cognitive or diagnostic information enters the model. [Paper: Methods, "ProtAIDe-Dx"; Results]

**Evaluation ladder,** in increasing order of difficulty: tenfold cross-validation stratified by site → leave-one-site-out across 14 test sites → K-shot transfer to a new site → external application to BioFINDER-2, which is a GNPC member site excluded from fitting. [Paper: Results; "Out-of-sample generalization…"]

**Baselines:** Random Forest, XGBoost, TabPFN, and an XGBoost + ProtAIDe-Dx ensemble. [Paper: Results]

**Downstream uses of the same model:** the embedding layer is reused for a task it was never trained on (progression from CDR 0), the six probabilities are projected by t-SNE into a disease map, and per-patient SHAP values drive a proof-of-concept diagnostic report. [Paper: Results; Fig. 6]

**Main workflow figure:** Fig. 1a. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Six binary heads (multi-task) | Independent per-condition prediction | Expresses co-pathology; uses partially labelled patients | Embedding → 6 probabilities | [Paper: Methods, "ProtAIDe-Dx"] | Not ablated against a multi-class head; the justification is label availability, not measured accuracy |
| Label-smoothed BCE | Main classification loss | Calibrates confidence against noisy clinical annotations | Predictions + labels → loss | [Paper: Methods, "ProtAIDe-Dx"] | Smoothing factor α is a searched hyperparameter |
| Multi-class rank loss | Constrains the *ordering* of the six probabilities per patient | Robustness to severe class imbalance; couples the tasks | Probability pairs → hinge loss | [Paper: Methods, "ProtAIDe-Dx"] | Weight λ searched; the coupling term is what makes it "joint" rather than six separate models |
| Embedding layer Z | Compressed nonlinear proteomic representation | Reused for transfer and for biological interpretation | Proteins → Z | [Paper: Fig. 1a, Fig. 3b,c] | Load-bearing: K-shot finetuning on embeddings recovers site generalization better than retraining on raw proteins |
| Preprocessing chain | Mean normalization → 10-NN imputation → Gaussian rank normalization | Proteomics are missing-heavy and non-normal | Raw SomaScan → model input | [Paper: Methods, "ProtAIDe-Dx"] | Imputer and normalizer fit on the training split only — the leakage control the Discussion claims |
| Inference-time dropout, 100 passes | Empirical spread as an overfitting proxy | Interval width read through the bias–variance tradeoff | Model → prediction distribution | [Paper: Methods, "ProtAIDe-Dx"] | A diagnostic on the model, not a calibrated uncertainty for patients |
| Feature permutation at inference | Identifies discriminative proteins | Deep models are otherwise opaque to clinicians | Model + data → protein importance | [Paper: Fig. 3a] | Post hoc; does not change predictions |
| Two-cutoff strategy | Converts a probability into a triage decision | A single threshold cannot deliver both high PPV and high NPV | Probability → positive / indeterminate / negative | [Paper: Fig. 5d] | Cutoffs fit on non-SCD participants, applied to SCD — a genuine holdout |

## 09 Essential Formulas and Symbols

The loss is a weighted sum of two terms, both stated in Methods. [Paper: Methods, "ProtAIDe-Dx"]

- **Label-smoothed binary cross-entropy** over N participants and 6 conditions, with smoothing factor α mixing each label toward 0.5: `L_BCE = −(1/N) Σ_k Σ_i [ (y_{k,i}(1−α) + α/2) log ŷ_{k,i} + ((1−y_{k,i})(1−α) + α/2) log(1−ŷ_{k,i}) ]`.
- **Pairwise rank loss** over all 15 condition pairs, a hinge with margin ε = 0.25: `L_RL^{i,j} = (1/N) Σ_k max[0, (ŷ_{k,i} − ŷ_{k,j})(y_{k,j} − y_{k,i}) + ε]`, summed over i < j.
- **Total:** `L = L_BCE + λ · L_RL`.

Symbols: N participants, k participant index, i and j condition indices, y true label, ŷ predicted probability, α label-smoothing factor, ε rank margin (0.25), λ rank-loss weight. α and λ were tuned by Optuna over 50 trials on the validation split. [Paper: Methods, "ProtAIDe-Dx"]

[Analysis] The rank term is the mathematically interesting part: it penalizes getting the *relative order* of two conditions wrong within a patient, which is exactly the differential-diagnosis question, and it is what stops six binary heads from being six unrelated models.

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Tenfold CV on GNPC, site-stratified | Multi-diagnosis accuracy | Median BCA **ALS 95%, PD 92%, control 83%, AD 81%, FTD 72%, stroke/TIA 70%**; AUC >0.8 for all but stroke/TIA | Proteomics carries multi-disease diagnostic signal | Clinical-grade accuracy — the authors deny this | [Paper: Fig. 1b] |
| vs Random Forest, XGBoost, TabPFN | Does the deep model earn its complexity? | Beats RF everywhere; beats XGBoost on AD, FTD, stroke only; beats TabPFN on **FTD only** (P = 0.047) | A modest, task-specific advantage | Broad superiority over gradient boosting | [Paper: Fig. 1b] |
| XGBoost + ProtAIDe-Dx ensemble | Is the combination better? | **Beats ProtAIDe-Dx** on control and PD; but "did not aid generalization performance" | Ensembling helps in-sample | That the ensemble is the better deployable model | [Paper: Fig. 1b; "Out-of-sample generalization…"] |
| APOE and MMSE sanity checks | Are probabilities biologically coherent? | AD probability rises with ε4 copies, falls with ε2, correlates negatively with MMSE | Probabilities behave as continuous disease scores | Causal or mechanistic interpretation | [Paper: Fig. 1c,d] |
| Transfer to an untrained task | Are the embeddings general? | CDR 0 → 0.5/1 progressors (N = 218) vs stable (N = 1,445): **BCA 70%, AUC 74%** | The representation transfers | Prognostic utility at the individual level | [Paper: Fig. 1e] |
| Leave-one-site-out, 14 sites | Real generalization | **Substantial drop in both BCA and AUC** for every model; partially recovered by K-shot finetuning on embeddings | Site effects are the binding constraint | That reported CV numbers apply at a new site | [Paper: Fig. 4a; Discussion] |
| BioFINDER-2 external application | Behaviour in a real memory clinic | Performance near the median of leave-one-site-out; PD probability elevated in DLB, stroke probability elevated in vascular dementia | Sensible transfer to biomarker-confirmed diagnoses | Equivalence to in-sample performance | [Paper: Fig. 4b; Extended Data Fig. 5] |
| Probabilities vs pathology biomarkers | Are "false positives" actually right? | In cognitively unimpaired people, control-probability was **lower** when AD, Lewy body or neurovascular pathology was present; AD probability higher in non-AD cases with Aβ/tau; stroke probability tracked WMH burden | Some apparent errors detect preclinical pathology | That all false positives are hidden true positives | [Paper: Fig. 4d] |
| PD probability vs α-synuclein SAA | Does PD prediction track Lewy pathology? | **No significant relationship** with CSF α-synuclein SAA; correlated instead with UPDRS symptom progression | The PD head tracks symptoms, not the pathology marker | That PD probability is a Lewy-body biomarker | [Paper: Fig. 4d] |
| Additive value, models 0–3 | Does it add to existing workup? | Model 3 (clinical markers + ProtAIDe-Dx) **significantly beats** model 2 (demographics, MMSE, AD-signature cortical thickness, p-tau217, NEFL), most for non-AD dementias | Complementary information, especially where blood biomarkers are missing | Standalone replacement | [Paper: Fig. 5a] |
| Longitudinal decline stratification | Prognostic signal from a baseline-trained model | Baseline **clinical** diagnosis did not stratify MMSE decline after FDR correction; baseline **predicted** diagnosis did, in GNPC and in BioFINDER-2 MCI (P = 0.0015) | Predicted labels carry progression information clinical labels do not | Causality, or use for treatment decisions | [Paper: Fig. 5b] |
| Two-cutoff triage | Actionable thresholds | >90% specificity and PPV in SCD patients; **94% NPV** for Lewy-body-related positivity by CSF α-synuclein | Usable as a rule-out / rule-in triage layer | Blanket diagnostic accuracy | [Paper: Fig. 5d] |

## 11 Correct Interpretation of the Conclusions

- The "70–95% balanced accuracy" range is **cross-validated within GNPC**. The number that matters for deployment is the leave-one-site-out number, which is substantially lower for every model tested. The abstract quotes the first; the Discussion is explicit about the second. [Paper: Fig. 1b, Fig. 4a; Discussion]
- The deep model's advantage over strong tabular baselines is narrow. Against TabPFN it is significant on exactly one of six tasks. The strongest deployable configuration in-sample was an ensemble that then failed to help generalization. [Paper: Fig. 1b]
- "Improved differential diagnosis" means *added to* existing clinical markers, not *replaced* them. The authors state directly that contemporary plasma proteomics "cannot yet replace currently available clinical markers". [Paper: Fig. 5a; Discussion]
- The evidence that apparent false positives detect real preclinical pathology is genuine and biomarker-anchored — but it is asymmetric. The one place it was tested against a specific pathology assay and failed is PD versus α-synuclein SAA, and the paper reports that rather than omitting it. [Paper: Fig. 4d]
- Training labels are clinical diagnoses without biomarker confirmation, drawn from cohorts with differing criteria. Every accuracy number is therefore an agreement-with-clinician number, not an agreement-with-pathology number. [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] "The performance of ProtAIDe-Dx is not sufficient at present to replace currently available clinical markers." [Paper: Discussion]
- [Paper] Performance drops in leave-one-site-out and site-to-site settings, especially for conditions unevenly distributed across sites — ALS patients "mainly come from one site". [Paper: Discussion]
- [Paper] Training and evaluation labels "for the most part, lacked biomarker confirmation", and diagnostic criteria varied across the retrospective cohorts. [Paper: Discussion]
- [Paper] Performance was comparable to UK Biobank proteomics studies, "suggesting that there may be a performance ceiling of high-throughput plasma proteomics as biomarkers". [Paper: Discussion]
- [Paper] Aptamer panels target arbitrary protein conformations and are limited to secreted or surface proteins; the blood–brain barrier blocks many disease-relevant brain-expressed proteins. [Paper: Discussion]
- [Paper] Plasma p-tau biomarkers discriminate AD better than this model does, because they target specific peptides and post-translational modifications. [Paper: Discussion]
- [Paper] Medication use can shift circulating protein levels beyond physiological ranges "and may therefore dominate model predictions". [Paper: Discussion]
- [Paper] Some conditions are intrinsically harder: FTD is heterogeneous with multiple underlying pathologies, and stroke/TIA is a stochastic event that often goes undiagnosed. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| The abstract leads with 70–95% BCA; the deployment-relevant leave-one-site-out numbers are not quantified in the main text | The headline is the optimistic end of a range the paper itself argues is optimistic | Downstream citation will carry the abstract number, not the caveat | State the leave-one-site-out BCA per task in the abstract alongside the CV range | [Paper: Abstract; Fig. 4a] |
| ACHE is strongly discriminative for AD, and 35 of 52 mapped drugs map to ACHE | A top feature may be reporting treatment, not disease | A diagnostic that detects "is on a cholinesterase inhibitor" will not work pre-treatment, which is when it is needed | Refit excluding treated patients, or stratify performance by medication status | [Paper: "Model interpretation…"; Discussion] |
| ALS reaches the highest accuracy (95%) and ALS patients come mainly from one site | Site and diagnosis are confounded for the best-performing task | The most impressive number may be the least transferable | Report per-task leave-one-site-out separately; ALS specifically | [Paper: Fig. 1b; Discussion] |
| PD probability correlates with UPDRS but not with α-synuclein SAA | The PD head may be reading symptom severity rather than PD pathology | The stated goal is *pathological* diagnosis in vivo | Evaluate PD probability against SAA in a prospectively enriched sample; report separately from symptom correlation | [Paper: Fig. 4d] |
| Deep model beats TabPFN on 1 of 6 tasks; ensemble beats it on 2 | The margin over off-the-shelf tabular methods is thin | Determines whether the deep architecture is worth the deployment burden | Pre-register a superiority margin; power the comparison for it | [Paper: Fig. 1b] |
| "False positives may correctly identify underlying preclinical neuropathology" | This reframing is supported for AD, Lewy body and vascular markers, but it is unfalsifiable if applied generally | It can absorb any error into a claim of hidden truth | Fix the interpretation rule in advance: which biomarker, which threshold, before looking | [Paper: Fig. 4d; Supplementary Table 6] |
| Diagnostic report shows three hand-picked cases | Case selection is not a performance estimate | Reports are the deployment surface; a curated example sets expectations the model cannot meet | Report the fraction of consecutive patients whose report would have been correct | [Paper: Fig. 6; Extended Data Figs. 8, 9] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: when cohorts are aggregated from studies with different aims, the label matrix is sparse and non-randomly so; multi-task binary heads use that data where a single softmax discards it.
- Agent-derived knowledge candidate: a rank loss across a patient's outputs turns independent classifiers into a differential-diagnosis model, because differential diagnosis is a question about ordering, not about absolute probability.
- Agent-derived knowledge candidate: report the leave-one-site-out number, not the cross-validated one, whenever the intended use is a new site. The gap between them is the honest estimate of what deployment will cost.
- Agent-derived knowledge candidate: a feature that is also a drug target for the condition being predicted should be treated as a suspected treatment marker until shown otherwise.
- Agent-derived knowledge candidate: "the false positives are really true positives" is a strong claim; it is only credible when the confirming biomarker and threshold were fixed before the errors were examined, and when the cases where it fails are reported too.

## 15 Connections to Existing Knowledge

[Analysis] This sits in the blood-biomarker line that runs from single-analyte assays (plasma p-tau217, NEFL) toward broad proteomic panels, and it is explicitly benchmarked against that line rather than against other deep models: the comparison that decides its usefulness is Fig. 5a, model 2 versus model 3. Methodologically it belongs with tabular deep learning, where its rivals are XGBoost and TabPFN, and the honest finding is near-parity. The two-cutoff probability strategy is positioned against the Amyloid Probability Score 2 (APS2) from C2N Diagnostics, an existing commercial precedent for turning a model output into a clinical triage rule. Its most transferable methodological contribution to this catalogue is the evaluation ladder — cross-validation, leave-one-site-out, K-shot transfer, external cohort — and the willingness to publish the whole ladder rather than the top rung. A priority comparison against concurrent GNPC analyses was not attempted here.

## 16 Research Ideas

### Agent-derived research candidate

**Does ProtAIDe-Dx diagnose the disease or the prescription?** [Hypothesis] A measurable fraction of the model's discriminative signal — largest for AD, where ACHE is a top feature and 35 of 52 mapped drugs act on it — reflects medication exposure rather than pathology, and performance will fall in treatment-naive patients. Delta: partition GNPC and BioFINDER-2 by documented medication status at draw, then evaluate the frozen published model separately in treatment-naive and treated strata; refit with drug-associated proteins removed and measure the accuracy cost per condition. Validation: pre-register the drug–protein map (the paper's own Supplementary Data 5 as the starting list) before splitting; report per-condition BCA with bootstrap intervals in both strata; replicate the split in the held-out BioFINDER-2 sample. Falsifier: treatment-naive and treated BCA agree within their confidence intervals for every condition, and removing drug-associated proteins costs nothing — which would show the drug features are redundant with genuine disease signal. Failure modes: medication records incomplete or unharmonized across the 19 sites; treatment status confounded with disease stage and with site; treatment-naive strata too small for FTD and ALS to be conclusive. Innovation status: unverified; prior-art search required.
