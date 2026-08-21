# Paper Card: Predictive biomarkers of response to chimeric antigen receptor (CAR) T-cell therapy for pan-haematologic cancer

> Source coverage: Open-access full text via PubMed Central (PMC13435093), including Introduction, Results, Discussion, Methods and all main- and Extended-Data-figure captions
>
> Extraction confidence: High for the main text and figure captions; Supplementary Tables are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Resource / benchmark
>
> Secondary analytical lens: Clinical evaluation
>
> Context verification: Cross-checked against Crossref metadata; the cohort-size discrepancy carried in this catalogue's YAML record was resolved from the full text (see 11)
>
> Card completeness: Complete for the main text; Supplementary Table 2 (trial list) and the underlying per-patient data were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| Favorable / Non-favorable | complete response, partial response or upgraded response vs non-response or progressive disease | The dichotomized outcome every model predicts; not standard RECIST categories |
| apheresis T cells | the patient's starting T-cell material, collected before manufacture | Pre-infusion, pre-manufacture — the earliest predictive time point |
| IC panel / TCD panel | the 11-marker immune-checkpoint and 10-marker T-cell-differentiation flow panels | Two separate stains on overlapping patients; cluster IDs are panel-specific |
| CAR qPCR | serial quantification of the CAR transgene in peripheral blood post-infusion | A pharmacokinetic measure, not a baseline biomarker |
| 4-1BB costimulation | the costimulatory domain shared by every construct in the study | The stated scope boundary of the entire result |
| out-of-bag AUROC | Random Forest's internal held-out estimate | Used for the single-modality comparisons; distinct from the 10-fold CV and hold-out numbers |

## 01 Basic Information

- **Title:** Predictive biomarkers of response to chimeric antigen receptor (CAR) T-cell therapy for pan-haematologic cancer
- **Authors:** Gregory M. Chen, … , Joseph A. Fraietta (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature Biomedical Engineering*, 2026-03. [Paper: Metadata]
- **DOI:** [10.1038/s41551-026-01633-7](https://doi.org/10.1038/s41551-026-01633-7)
- **Cohort:** 256 patients, 13 investigator-initiated trials at the University of Pennsylvania, 5 haematologic cancers (CLL, MM, B-ALL, NHL, AML); all constructs 4-1BB/CD3ζ targeting CD19, CD22, BCMA or CD123. Median age 58.6 (IQR 48.4–65.3); 66.8% male. [Paper: Results, "A framework for predictive modeling…"]
- **Data resource:** >2M apheresis T cells across two 11- and 10-marker flow panels (179 patients), >90,000 measurements of 30 serum cytokines, ex vivo expansion curves during manufacture, serial CAR qPCR. [Paper: Abstract]
- **Access boundary:** the open-access full text was read via PMC. Supplementary Table 2 and the per-patient data were not opened directly.

## 02 One-Sentence Summary

[Paper] By standardizing data generation across 13 in-house CAR T-cell trials, this study builds a 256-patient pan-haematologic-cancer resource and shows that a Random Forest integrating pre-infusion T-cell phenotype, manufacturing expansion and post-infusion cytokine and CAR-qPCR dynamics predicts clinical response with cross-validated AUROC 0.875, holding at 0.74 on a genuinely prospective 53-patient hold-out. [Paper: Abstract; Fig. 4c,g]

## 03 Research Question

- [Paper] Can predictive biomarkers of CAR T-cell response be found that generalize *across* haematologic cancers, rather than being rediscovered per indication in cohorts too small to support machine learning? [Paper: Introduction]
- [Analysis] The paper's real subject is the infrastructure that makes the question askable. The scientific claim rests on an institutional fact — apheresis, manufacture, infusion and follow-up all happen in one building under one set of protocols — more than on any modelling choice.

## 04 Research Background and Development Path

1. [Paper] Seven CAR T-cell therapies are FDA-approved and decade-long remissions have been reported, but responses are heterogeneous both between cancer types and between patients with the same cancer. [Paper: Introduction]
2. [Paper] Machine learning has matured, but its use here is blocked by small cohorts and by non-uniform data collection: protocols, infrastructure and personnel change between trials. [Paper: Introduction; Abstract]
3. [Paper] Prior work linked naive-like T-cell phenotypes to response, largely within CLL. [Paper: Results, "Multiparameter flow cytometry…"]
4. [Paper] The Center for Cellular Immunotherapies runs early-phase trials end to end in-house, which makes uniform measurement across 13 trials possible. [Paper: Results, "A framework for predictive modeling…"]
5. [Analysis] The development path is therefore organizational before it is computational — and that is the part hardest for others to reproduce. The models used (Random Forest, BART, ridge, lasso, XGBoost, naive Bayes) are all standard and pre-existing.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Response heterogeneity | Wide variation between and within cancer types | Underlying T-cell biology differs at baseline | [Paper: Introduction] |
| Small cohorts | Single-trial studies cannot support predictive modelling | Early-phase trials are small by design | [Paper: Introduction] |
| Non-uniform data | Features not comparable across trials | Changing protocols, infrastructure and personnel | [Paper: Introduction] |
| Per-indication silos | Biomarkers found in CLL not tested elsewhere | Trials are organized by disease | [Paper: Results, "Multiparameter flow cytometry…"] |
| Missing modalities | Only 141 of 256 patients had both flow and cytokine data | Sample availability, retrospective assembly | [Paper: Results, "Designing and validating…"] |
| Late-arriving signal | The strongest predictors are post-infusion | Response depends on in vivo expansion, unknowable at decision time | [Paper: Fig. 4a,b] |

## 06 Core Idea

- **Surface method:** a Random Forest over 272 harmonized features spanning three time points.
- **Core insight:** benchmark the modalities *and the time points separately before combining them*, so the reader can see exactly how much predictive power exists at each clinical decision point. The pre-infusion ceiling (AUROC 0.77) and the post-infusion ceiling (0.85) are reported as distinct results, not folded into the headline 0.875. [Paper: Fig. 4a,b,c]
- **General lesson:** [Analysis] when features arrive at different times, a single combined performance number is close to meaningless for practice. A model that needs Day-7 cytokines cannot inform a decision made at apheresis. Splitting the benchmark by time point is what makes the result actionable, and this paper does it in the main figure.

## 07 Method Overview

**Flow:** four measurement streams, harmonized across 13 trials → per-patient feature extraction → Random Forest → dichotomized Favorable/Non-favorable response.

- *Pre-infusion:* age, sex, peripheral blood counts; flow cytometry on CD3+ apheresis T cells with two panels (IC: CD4, CD8, CD27, CD45RO, Granzyme B, Eomes, TIM-3, CTLA-4, LAG-3, Ki-67, PD-1; TCD: CD4, CD8, CD27, CD45RO, CCR7, HLA-DR, KLRG1, CD95, CD28, CD127). [Paper: Results, "Multiparameter flow cytometry…"]
- *Manufacturing:* daily ex vivo T-cell expansion and viability, Days 3–9.
- *Post-infusion:* 30 serum cytokines by Luminex binned to pre-infusion, early (≤3.5 d), and Days +7/+14/+21/+28; serial CAR qPCR.

**Feature extraction from flow:** UMAP for visualization, FlowSOM (nClus = 25) for clustering, then each patient summarized as the *relative proportions* of their T cells across clusters. Cluster-count stability was checked by sweeping FlowSOM nClus 3→30 and Louvain resolution 0.1→2.0 and re-measuring downstream AUROC. [Paper: Fig. 2d]

**Model comparison:** six algorithms under 10-fold cross-validation on 141 patients; validation on 53 later-processed patients. [Paper: Fig. 4c,e]

**Main workflow figure:** Fig. 1a and Fig. 4e. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| In-house trial framework | Uniform measurement across 13 trials | Cross-trial pooling is otherwise invalid | Trials → harmonized features | [Paper: Fig. 1a] | Not removable; it is the study's precondition |
| FlowSOM cluster proportions | Turns ~1M cells per panel into per-patient features | Unbiased alternative to manual gating | Cells → 25 proportions | [Paper: Fig. 2b,e] | **Swept**: AUROC > 0.65 for ≥13 FlowSOM clusters, >0.60 for Louvain resolution ≥0.2 — the choice of 25 is shown not to matter |
| Cytokine time-binning | Aligns irregular draws to comparable windows | Sampling schedules differ across trials | Timestamps → 6 bins | [Paper: Extended Data Fig. 4a] | Binning boundaries are a modelling choice, not swept |
| Per-timepoint logistic regression | Univariate cytokine–outcome associations with FDR control | Interpretable biology, separate from prediction | Cytokine + day → Wald test | [Paper: Fig. 3a–c] | Inferential arm; independent of the classifier |
| Random Forest classifier | Integrative prediction | Best of six methods tested; robust to correlated high-dimensional features | 272 features → probability | [Paper: Fig. 4c] | **Ablated across five alternatives**; BART close behind (0.868), naive Bayes far behind (0.687) |
| Leave-one-study-out / leave-one-cancer-type-out CV | Tests whether the model learned trial or disease identity | Pan-cancer claim depends on it | Folds by study or cancer → AUROC | [Paper: Extended Data Fig. 5a] | Load-bearing for the paper's central claim |
| Prospective hold-out on 53 patients | True external test | Flow data for these patients was generated in a later batch, after the model was fixed | Frozen model → AUROC 0.74 | [Paper: Fig. 4e–h] | The strongest evidence in the paper |
| mRMR feature selection | Reduces 272 features to 10 | Clinical assays cannot measure 272 things | Features → 10 | [Paper: Extended Data Fig. 6d,e] | Costs 0.87→0.84 in training, 0.74→0.69 in hold-out |

## 09 Essential Formulas and Symbols

No equations are stated. The methods used are standard and named rather than derived: logistic regression with two-sided Wald tests and Benjamini–Hochberg FDR correction for the cytokine associations; Wilcoxon rank-sum with BH correction for the expansion comparisons; Welch's two-sided t-test for the classifier score comparisons; mean decrease in Gini index for Random Forest feature importance; minimum redundancy maximum relevance (mRMR) for feature selection; Spearman correlation for feature redundancy; LOESS for the time-course curves. [Paper: Figs. 1–4 captions; Methods]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| CAR qPCR time courses | Does in vivo expansion track response? | Strong association; peak expansion 1–3 weeks post-infusion | Post-infusion expansion is a response correlate | Usable for treatment selection — it is measured after treatment | [Paper: Fig. 1e] |
| Ex vivo expansion during manufacture | Does manufacturing predict? | Higher expansion associates with favorable outcome, but only Days 6–7 reach FDR < 0.05 (0.048), with "substantial overlap between the clinical outcome groups" | A weak, real signal | A manufacturing release criterion | [Paper: Fig. 1f; Discussion] |
| Blood counts and viabilities | Do routine measures predict? | **No significant correlation** | Rules out the cheapest features | — | [Paper: Extended Data Fig. 1d,e] |
| Apheresis flow, IC panel (179 patients, 1,062,975 cells) | Does baseline phenotype predict? | CD8+CD27+CD45RO− naive-like cluster favorable; CD4+CD27+CD45RO+PD1+ central-memory-like cluster non-favorable | Baseline T-cell state carries signal | Causality; these are associations | [Paper: Fig. 2e] |
| Clustering-parameter sweep | Is the result an artefact of cluster count? | AUROC stable across FlowSOM 13–30 clusters and Louvain resolution ≥0.2 | The finding survives the analyst's free parameter | — | [Paper: Fig. 2d] |
| Cytokines by time point | When does cytokine signal appear? | Pre-infusion: IL-2R, CXCL9, CXCL10, IL-10 unfavorable, EGF favorable. Early: IL-2 favorable. Day +7: IL-6 and IFN-γ favorable. Day +14 onward: MIP-1α/β, MCP-1, IL-2R, CXCL9/10, IL-10, IL-1RA, IL-15, IL-8 unfavorable | A temporal signature, with direction reversing for inflammatory markers | That any single cytokine is a usable test | [Paper: Fig. 3a–f] |
| Single-modality benchmarks | Where does the predictive power live? | Manufacturing **0.55**, clinical **0.60**, pre-infusion cytokines **0.71**, pre-infusion flow **0.76**, all pre-infusion combined **0.77**; post-infusion qPCR **0.80**, post-infusion cytokines **0.83**, combined **0.85** | Pre-infusion prediction is real but modest; post-infusion is stronger | That the 0.875 headline is available before treatment | [Paper: Fig. 4a,b] |
| Six algorithms, 10-fold CV, n = 141 | Which learner? | RF **0.875**, BART 0.868, ridge 0.833, lasso 0.814, XGBoost 0.812, naive Bayes 0.687 | Tree ensembles win, narrowly | A meaningful gap between RF and BART | [Paper: Fig. 4c] |
| Leave-one-study-out / leave-one-cancer-type-out | Is it learning trial or disease identity? | **0.81** and **0.82** | The signal is not merely cancer type or trial | Equal performance per cancer | [Paper: Extended Data Fig. 5a] |
| Per-cancer-type generalization | Does it transfer to an unseen indication? | Trained excluding each type: NHL **0.69**, MM **0.76**, B-ALL **0.89**, CLL **0.95**. Trained within type: 0.68 / 0.72 / 0.89 / 0.92. AML **not estimable** | Performance is highly disease-dependent | A uniform "pan-cancer" performance | [Paper: Extended Data Fig. 5b,c] |
| Prospective hold-out, n = 53 | Does it hold on new patients whose data came later? | **AUROC 0.74**, p = 3.7 × 10⁻³; spans all 5 cancer types and 10 trials | Genuine, if reduced, generalization | Parity with the 0.875 cross-validated figure | [Paper: Fig. 4g,h] |
| T-cell-derived vs other cytokines | Is the signal T-cell biology? | RF on 13 candidate T-cell-produced factors **0.83** vs 0.77 on the rest | Consistent with a T-cell-intrinsic mechanism | Cellular source attribution — assignment is literature-based | [Paper: Extended Data Fig. 6b,c] |
| mRMR to 10 features | Can it be simplified for the clinic? | Training 0.87→0.84; hold-out 0.74→**0.69** | A compact panel is plausible | That the compact panel is validated | [Paper: Extended Data Fig. 6d,e] |

## 11 Correct Interpretation of the Conclusions

- **Cohort-size note for this catalogue.** The three numbers are not in conflict and each means something different: **256** patients in the data resource; **179** with apheresis flow cytometry; **141** with both flow and serial cytokines, used to train and cross-validate; **53** later-processed patients used as the hold-out. The catalogue's `training_slides: 256 patients, 13 trials` describes the resource; the model was trained on 141. [Paper: Results, "Designing and validating…"]
- The 0.875 headline is 10-fold cross-validated on 141 patients. The number that estimates prospective performance is **0.74**. [Paper: Fig. 4c,g]
- "Pan-cancer" means the model does not reduce to cancer-type identity — leave-one-cancer-type-out holds at 0.82. It does **not** mean uniform performance: CLL reaches 0.95 and NHL 0.69, and AML could not be assessed at all because no AML patient had both assays. [Paper: Extended Data Fig. 5b,c]
- Most of the predictive power is post-infusion. At the moment a clinician would want to choose therapy, the ceiling demonstrated here is 0.77. [Paper: Fig. 4a]
- The hold-out is stronger than a random split because those patients' flow data was generated in a separate later batch, after the model was developed — but they come from the same institution, the same trials portfolio and the same manufacturing process. [Paper: Fig. 4e]
- Every construct used 4-1BB costimulation at one centre. The authors state generalizability to commercial products or other costimulatory domains "is unclear". [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] All patients came from investigator-initiated 4-1BB-costimulated trials at a single institution; "the generalizability of our findings to other CAR T-cell studies, such as those using commercial CAR T-cell products or CAR constructs with different costimulatory domains, is unclear". [Paper: Discussion]
- [Paper] The manufacturing-expansion association showed "substantial overlap between the clinical outcome groups". [Paper: Discussion]
- [Paper] AML performance was not estimable because no AML patient had both flow cytometry and cytokine measurements available. [Paper: Results, "Designing and validating…"]
- [Paper] Tumour-specific attributes were not incorporated and are named as a future direction. [Paper: Discussion]
- [Paper] The mRMR result is offered as a *basis for future validation*, not as a validated simplified biomarker. [Paper: Discussion]
- [Paper] Mechanistic interpretation of the highlighted features is left to future work. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Flow cytometry for the 53 hold-out patients was generated specifically to complete this validation | The batch is temporally and procedurally distinct from training — good for independence, but batch effects and the 0.875→0.74 drop are confounded | Determines whether the drop is overfitting, batch effect, or both | Re-run a subset of training patients' apheresis samples in the hold-out batch and measure the shift | [Paper: Fig. 4e] |
| Two flow panels, each clustered separately at nClus = 25, contribute 50 cluster-proportion features | Cluster proportions are compositional and sum to one, so features are structurally dependent | Random Forest importance is unstable under compositional constraints | Repeat with a log-ratio transform; compare selected features | [Paper: Fig. 2e; Extended Data Fig. 3f] |
| CLL drives many of the strongest univariate findings and reaches the best model performance | The pan-cancer claim may rest disproportionately on one indication | "Pan-cancer biomarker" is the paper's framing | Re-estimate every headline association excluding CLL | [Paper: Extended Data Figs. 1f,g, 4g, 5b] |
| Outcome is dichotomized into Favorable (CR, PR, or "upgraded response") vs Non-favorable | Grouping partial response with complete response, and folding in an "upgraded" category, is a consequential choice made once | Every AUROC in the paper depends on this boundary | Report performance under CR-vs-rest as a sensitivity analysis | [Paper: Fig. 1f caption] |
| Post-infusion features dominate importance rankings | The best model answers a question that is largely already answered clinically | Prediction after infusion has narrower clinical use than prediction before | Report the pre-infusion-only model as the primary result; treat the integrated model as prognostic monitoring | [Paper: Fig. 4a,b; Extended Data Fig. 5d] |
| T-cell-derived cytokine assignment comes from a published atlas plus literature, then is used to argue mechanism | A literature-derived label carried into a performance comparison can encode the expected answer | The 0.83 vs 0.77 gap is presented as biological evidence | Pre-register the assignment; test with a randomized-label null | [Paper: Extended Data Fig. 6b,c] |
| 272 features, 141 training patients | Roughly two features per patient | Feature selection and model choice were both made using the same 141 patients | Nest all selection inside the cross-validation loop and report the change | [Paper: Extended Data Fig. 6a; Fig. 4c] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: benchmark by *time point*, not only by modality — a combined AUROC hides whether the model can inform the decision the clinician actually faces.
- Agent-derived knowledge candidate: when an unsupervised clustering step feeds a supervised model, sweep the clustering parameter and plot downstream performance against it. That sweep converts an arbitrary choice into a reported robustness result.
- Agent-derived knowledge candidate: a hold-out whose data was *physically generated later*, after the model was fixed, is much stronger than a random split — and it should be reported as a separate number, not averaged in.
- Agent-derived knowledge candidate: "pan-cancer" should be read as "does not reduce to cancer identity", not as "works equally everywhere"; publish the per-type breakdown alongside it.
- Agent-derived knowledge candidate: in multi-cohort resources, state the denominator for every claim separately — resource size, assay-available size, model-training size and validation size are four different numbers and will otherwise be conflated downstream.

## 15 Connections to Existing Knowledge

[Analysis] This work belongs to the clinical-biomarker line rather than the model-architecture line: nothing here is a new algorithm, and the six learners compared are all off the shelf. Its neighbours are prior CLL-specific studies linking naive-like apheresis phenotypes to CAR T-cell response, which it extends across indications, and the cytokine-monitoring literature developed for predicting cytokine release syndrome — the paper explicitly positions its findings as complementary to that toxicity work, arguing the same serial measurements predict efficacy as well as toxicity. Within this catalogue it is the clearest example of a resource-plus-benchmark paper where the contribution is standardized data generation, and its methodological transferable idea is the time-point-stratified benchmark. Priority relative to concurrent multi-trial CAR T-cell biomarker analyses was not assessed here.

## 16 Research Ideas

### Agent-derived research candidate

**Move the benchmark to the decision point.** [Hypothesis] A model restricted to features available *before* apheresis-to-infusion decisions are made can be brought materially above the 0.77 ceiling reported here by adding tumour burden and prior-therapy features, while post-infusion features — which dominate the current model — add nothing to that decision because they arrive too late to change it. Delta: refit the identical Random Forest pipeline under a strict pre-infusion feature mask, then add a pre-specified block of tumour-specific and treatment-history covariates that the authors name as missing; compare against the published pre-infusion model on the same 141/53 split. Validation: the frozen 53-patient hold-out as primary endpoint, with leave-one-cancer-type-out as secondary; report per-cancer AUROC with bootstrap intervals; pre-register the covariate block before unblinding the hold-out. Falsifier: the augmented pre-infusion model's hold-out AUROC confidence interval overlaps the pre-infusion baseline, indicating baseline T-cell phenotype has already saturated what is knowable before infusion. Failure modes: tumour-burden variables recorded inconsistently across 13 trials, reintroducing exactly the non-uniformity the framework was built to remove; hold-out of 53 too small to separate nearby AUROCs; per-cancer strata too small once CLL is excluded. Innovation status: unverified; prior-art search required.
