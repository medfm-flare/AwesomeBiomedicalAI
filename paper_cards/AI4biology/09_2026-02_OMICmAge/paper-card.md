# Paper Card: OMICmAge quantifies biological age by integrating multi-omics with electronic medical records

> Source coverage: Open-access full text via PubMed Central (PMC13004675), including Main, Results, all named result subsections, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; the 18 Supplementary Tables, Methods in full and Extended Data are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Clinical evaluation
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code; this entry's cross-page duplication is noted in 15
>
> Card completeness: Complete for the main text; Supplementary Tables 1–18 and the Extended Data figures were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| EMRAge | a mortality-risk score built by Cox regression on 19 routine clinical lab variables, rescaled into years | The **target** all downstream clocks are trained to predict; not itself a molecular measure |
| DNAmEMRAge | an elastic-net DNA-methylation clock trained to predict EMRAge | Methylation only |
| OMICmAge | the same, plus 396 epigenetic biomarker proxies as candidate features | Multi-omic *in training*, methylation-only *at inference* |
| EBP | epigenetic biomarker proxy — a DNAm-based elastic-net prediction of one metabolite, protein or clinical value | The mechanism by which other omics enter a methylation clock |
| PC clocks | principal-component versions of Horvath, Hannum, PhenoAge, GrimAge | The comparators, chosen for their improved precision |
| ICC | intraclass correlation across 30 technical replicates | Reproducibility, distinct from accuracy |
| DunedinPACE | a pace-of-aging clock rather than an age estimate | Included as a comparator; measures a different quantity |

## 01 Basic Information

- **Title:** OMICmAge quantifies biological age by integrating multi-omics with electronic medical records
- **Authors:** Qingwen Chen, … , Jessica Lasky-Su (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature Aging*, 2026-02. [Paper: Metadata]
- **DOI:** [10.1038/s43587-026-01073-7](https://doi.org/10.1038/s43587-026-01073-7)
- **Code:** [LaskySuLab/OMICmAge](https://github.com/LaskySuLab/OMICmAge)
- **Cohorts:** EMRAge development — MGB Biobank, 31,264 individuals with complete data on 19 clinical variables (from 60,370 screened), split 70:30. DNAm clocks — MGB-ABC, n = 3,451 (2,762 train / 689 test). Validation — All of Us (n = 10,769), TruDiagnostic Biobank (n = 14,213), Generation Scotland (n = 18,672). [Paper: Abstract; Results]
- **Omics:** 1,459 metabolites (Metabolon, n = 1,986; 1,691 methylation-matched); 2,098 annotated proteins / 536 protein groups (Seer SP100 LC–MS, n = 1,789; 1,475 matched); 46 candidate clinical variables.
- **Access boundary:** the open-access full text was read via PMC. Supplementary Tables 1–18, Methods in full and the Extended Data figures were not opened directly.

## 02 One-Sentence Summary

[Paper] EMRAge is a mortality-risk clock built from 19 routine lab values in ~31,000 electronic medical records; DNAmEMRAge and OMICmAge are methylation clocks trained to reproduce it, with OMICmAge additionally drawing on proteomic, metabolomic and clinical information that has first been distilled into methylation-based proxies — so that a multi-omic signal can be read out from a DNA methylation array alone. [Paper: Abstract]

## 03 Research Question

- [Paper] Can a biological-age measure be built that combines dense clinical phenotype *and* mortality risk — rather than optimizing one at the expense of the other — and can multi-omic information be folded into a methylation readout without requiring proteomics and metabolomics at inference time? [Paper: Main]
- [Analysis] The second half is the engineering question and it is the paper's real contribution: multi-omic clocks are, in the authors' words, "often impractical due to high costs and logistics". The EBP construction is a way to pay the multi-omic cost once, at training time, and never again.

## 04 Research Background and Development Path

1. [Paper] Aging clocks exist across many substrates — telomeres, neuroimaging, immune counts, methylation, metabolomics, glycomics, proteomics. [Paper: Main]
2. [Paper] Existing biological-age phenotypes optimize *either* clinical quality-of-life data (PhenoAge) *or* mortality (GrimAge), so each is incomplete with respect to the other. [Paper: Main]
3. [Paper] EMRs supply dense longitudinal clinical data that could support both at once, and are reproducible across clinical settings. [Paper: Main]
4. [Paper] Each omic layer gives a distinct window on aging, so an integrated biomarker should be better — but integration "remains an area of unfulfilled clinical potential", largely on cost grounds. [Paper: Main]
5. [Analysis] The path taken is a surrogate chain: clinical labs → EMRAge → methylation surrogate of EMRAge → methylation surrogate augmented with methylation surrogates of proteins and metabolites. Each step buys scalability and spends a little accuracy, and the paper is unusually explicit about the mechanics.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| One-attribute clocks | PhenoAge captures phenotype, GrimAge captures mortality; neither both | Training targets were chosen separately | [Paper: Main] |
| Multi-omic cost | Metabolomic and proteomic clocks are impractical at scale | Assay cost and logistics | [Paper: Discussion] |
| Uninterpretable methylation | "Functions implied by specific methylation perturbations are often unclear" | CpG-level weights carry no obvious biology | [Paper: Discussion] |
| Reproducibility | Epigenetic clocks have historically had poor technical replication | Addressed previously only by PC-based summarization | [Paper: Discussion] |
| Stochastic drift | Highly age-correlated clocks may just be measuring accumulated noise | Cited prior work | [Paper: Discussion] |
| EMR missingness | "Real-world data are not systematically collected and so missingness is universal" | Clinical data are collected for care, not research | [Paper: Discussion] |

## 06 Core Idea

- **Surface method:** elastic-net regression from methylation to a clinical mortality score.
- **Core insight:** other omic layers do not have to be *measured* at inference — they only have to be *learned once*. Each selected metabolite, protein and clinical value gets its own DNAm elastic-net predictor (an EBP); the EBPs then become candidate features in the final clock. Multi-omic information enters the model, but the deployed assay is a methylation array. [Paper: "Metabolomic, proteomic and clinical EBPs"; Fig. 4]
- **General lesson:** [Analysis] a proxy is worth building when the expensive modality is needed for *training signal* rather than for *inference input*. The cost of the trick is that every EBP is an approximation of an approximation, and the paper's own numbers bound how good those approximations are — retained EBPs needed only ρ > 0.2 with their measured counterpart, with the best examples reaching ρ = 0.66 (CRP) and 0.63 (HbA1c).

## 07 Method Overview

**Stage 1 — EMRAge.** 60,370 MGB Biobank individuals filtered to **31,264** with complete data on 19 clinical variables. Cox proportional-hazards fit on the 70% training split; the linear predictor is rescaled into an age metric following the GrimAge approach. Correlation with chronological age: ρ = 0.76 (test), 0.75 (train). [Paper: "Development of EMRAge"]

**Stage 2 — DNAmEMRAge.** Elastic net (α = 0.1) from methylation to EMRAge, 25-fold cross-validation. Retains **1,097 CpGs plus age**. [Paper: "Development of DNAmEMRAge"]

**Stage 3 — EBP construction.** Two sequential filters, both shown in Fig. 4:
1. Correlation with EMRAge — |ρ| > 0.1 and P < 0.05 — retaining 110 proteins, 25 clinical variables, and 286 metabolites (metabolites first collapsed by hierarchical clustering into 286 low-intercorrelation clusters, one representative each). 421 candidates.
2. Each candidate gets a DNAm elastic-net predictor; the EBP is retained only if it correlates with its own measured counterpart at ρ > 0.2, P < 0.05. **396 survive**: 266 metabolite, 109 protein, 21 clinical. [Paper: "Metabolomic, proteomic and clinical EBPs"; Fig. 4b,c]

**Stage 4 — OMICmAge.** Penalized elastic net predicting EMRAge from CpGs, 12 immune cell fractions, the 396 EBPs, age and sex. Retains **990 CpGs, 40 EBPs (16 protein, 14 metabolite, 10 clinical) and age**. No immune cell fraction survived penalization. Computing the 40 EBPs requires a further 10,315 CpGs, of which 50.8% are on the 450K array. [Paper: "Predictive model for the OMICmAge"]

**Main workflow figures:** Fig. 1a (study design) and Fig. 4a (EBP filtration). No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Cox model on 19 lab variables | Defines EMRAge | Hybrid of clinical status and mortality risk in one target | Labs → linear predictor → years | [Paper: "Development of EMRAge"] | Everything downstream inherits this target's properties |
| Retraining at four time points | Robustness of EMRAge to when it is computed | EMR values shift over time | 2008/2010/2012/2014 fits → 2016 predictions | [Paper: Fig. 2a] | **Passed**: pairwise correlations ≈ 1 |
| Elastic net α = 0.1 | Feature selection from methylation | ~800K CpGs, ~3K samples | CpGs → 1,097 (DNAmEMRAge) / 990 (OMICmAge) | [Paper: Results] | Low α means mostly ridge, keeping correlated CpGs together |
| Metabolite clustering | Reduces 1,459 metabolites to 286 near-independent representatives | Metabolites are heavily intercorrelated | Metabolites → clusters → representatives | [Paper: "Metabolomic, proteomic and clinical EBPs"] | Cluster criteria stated: inter-cluster 90th pct < 0.15, intra-cluster 10th pct > 0.5 |
| EBP layer | Encodes proteins/metabolites/clinical values as methylation predictions | Removes the need to assay them at inference | Measured value → DNAm predictor | [Paper: Fig. 4c] | **The load-bearing idea**; retention bar is only ρ > 0.2 |
| Two-stage EBP filter | Keeps proxies that are both aging-relevant and faithful | Either filter alone would admit useless proxies | 421 candidates → 396 EBPs | [Paper: Fig. 4b,c] | Fig. 4b,c show the background distributions, so the selectivity is visible |
| Immune cell fractions | Candidate confounder / feature | Cell composition drives much methylation variance | 12 fractions → dropped | [Paper: "Predictive model for the OMICmAge"] | **Ablated both ways**: penalized (dropped) and unpenalized (no substantial change) |
| Technical replicate ICC | Reproducibility check | Epigenetic clocks have a replication history problem | 30 replicates → ICC | [Paper: Fig. 3c,f] | DNAmEMRAge 0.995, OMICmAge 0.998 |

## 09 Essential Formulas and Symbols

No equations are stated. The components are named: Cox proportional-hazards regression for EMRAge, with the linear predictor converted into an age scale "in a manner analogous to the GrimAge approach"; elastic net regression (α = 0.1 for DNAmEMRAge) with lambda chosen by 25-fold cross-validation; hierarchical clustering with explicit inter- and intra-cluster correlation criteria for metabolite reduction; Pearson correlation and R² for agreement; mean absolute error in years; intraclass correlation across 30 technical replicates; Cox hazard ratios and logistic odds ratios per 1 s.d., adjusted for chronological age, sex, race, BMI, smoking and alcohol; Benjamini–Hochberg FDR at 0.05; and ROC AUC for 5- and 10-year survival. [Paper: Results; figure captions]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| EMRAge vs PhenoAge, MGB test set | Is the hybrid target better? | EMRAge highest HR for mortality (**4.53**), stroke (2.00), COPD (2.21), cancer (2.22); comparable for T2D, depression, CVD | A strong clinical mortality score | Superiority across all outcomes | [Paper: Fig. 2b] |
| Joint model, both scores | Does EMRAge add over PhenoAge? | EMRAge consistently higher HRs when both are in one model | Non-redundant information | Causal or mechanistic priority | [Paper: Fig. 2d] |
| Temporal robustness | Does EMRAge depend on when it is computed? | Four fits (2008–2014) applied to 2016: pairwise correlations ≈ 1 | Stable to EMR snapshot timing | Stability across different EMR systems | [Paper: Fig. 2a] |
| All of Us validation (n = 10,769) | External validity of EMRAge | Strongest association with mortality (**HR 3.08**) and with prevalent stroke, COPD, depression, cancer | Generalizes to a second EMR system | That it beats PhenoAge for incident disease — the authors say it does not, citing shorter follow-up (median 3 vs 5.5 y) | [Paper: Extended Data Fig. 3; Discussion] |
| DNAmEMRAge fit | Can methylation reproduce EMRAge? | Train R² 0.82, test R² 0.83, ρ 0.91; **MAE 8.33 / 8.50 years**; ICC 0.995 | A faithful surrogate | That 8.5 years of error is negligible | [Paper: Fig. 3a–c] |
| OMICmAge fit | Do EBPs improve the surrogate? | Train R² 0.83, test R² 0.84, ρ 0.92; **MAE 4.96 / 4.97 years**; ICC 0.998 | EBPs nearly halve the error against the target | That halving error against EMRAge means better outcome prediction — see next row | [Paper: Fig. 3d–f] |
| 5-/10-year mortality AUC, MGB | Does the better surrogate predict better? | **DNAmEMRAge highest** (0.898 / 0.890); OMICmAge close behind (0.892 / 0.873); both above chronological age and all other clocks | Both are strong mortality classifiers | That OMICmAge dominates — on this endpoint it does not | [Paper: Fig. 5c] |
| 5-/10-year mortality AUC, Generation Scotland | External mortality prediction | **PCGrimAge first** (0.870 / 0.866); OMICmAge second (0.861 / 0.859) | Competitive with the leading prior clock | Superiority over PCGrimAge | [Paper: Extended Data Fig. 7] |
| CpG overlap with prior clocks | Is it measuring something new? | DNAmEMRAge and OMICmAge have 660 and 657 unique CpGs, 411 shared with each other; **maximum overlap with any prior clock is 3 probes** | Near-complete independence from existing clocks | That novelty implies better biology | [Paper: Fig. 5a] |
| Disease associations, MGB-ABC | Prevalent and incident disease | Prevalent: OMICmAge highest OR for 4 of 6 — T2D **5.04**, CVD **4.62**, stroke 2.21, depression 1.94; chronological age highest for cancer. Incident: OMICmAge highest for T2D (2.68), CVD (3.28), mortality (**11.31**) | Strong associations in the discovery cohort | Discrimination between top clocks — the paper states several differences fall within overlapping CIs | [Paper: Fig. 5b] |
| Disease associations, Generation Scotland | Does it hold externally? | **Chronological age strongest** for mortality (5.58), stroke (4.10), cancer (2.76); OMICmAge generally **second after PCGrimAge**; OMICmAge strongest for incident depression (3.14) | Consistent but not dominant | That OMICmAge outperforms established clocks externally | [Paper: Extended Data Fig. 6b] |
| Disease associations, TruDiagnostic | A third external cohort | Chronological age stronger here than elsewhere, and the only measure associated with stroke; OMICmAge top-two for T2D, depression, cancer | Cohort composition changes the ranking | A stable ordering of biomarkers | [Paper: Extended Data Fig. 6a] |
| Lifestyle associations | Face validity | Negative with female sex, education, weekly exercise; positive with obesity and smoking, consistently across cohorts | Behaves as an aging measure should | Causal effect of lifestyle on the biomarker | [Paper: Fig. 6] |
| Immune-fraction sensitivity | Is it just cell composition? | No immune subset retained under penalization; an unpenalized variant "did not change substantially" | Not reducible to cell mix | Full independence from cell composition | [Paper: "Predictive model for the OMICmAge"] |
| Array portability | Can it run on older data? | 40 EBPs need 10,315 additional CpGs; **50.8% (5,740) available on 450K**; a 450K version "is in development" | Honest statement of deployment constraint | That it currently runs on 450K data | [Paper: Results] |

## 11 Correct Interpretation of the Conclusions

- OMICmAge is **not** a multi-omic measurement. Proteomics and metabolomics were used to build proxies during training; at inference the input is DNA methylation only. This is the design's main selling point and must not be read as "measures your proteome". [Paper: Discussion]
- The training target is EMRAge, which is itself a model output, not an observed quantity. R² = 0.84 and MAE ≈ 5 years describe agreement with *another estimate*, not with biological age or with survival. [Paper: Fig. 3d,e]
- Because of that, "OMICmAge is more accurate than DNAmEMRAge" is true against EMRAge (MAE 4.97 vs 8.50) and **false** on 5- and 10-year mortality AUC in the same cohort, where DNAmEMRAge is slightly ahead. Both facts are in the paper. [Paper: Fig. 3; Fig. 5c]
- In both external cohorts, chronological age or PCGrimAge takes the top rank on several major endpoints. The defensible claim is that OMICmAge is consistently top-two, not that it is best. [Paper: Extended Data Figs. 6, 7]
- Near-zero CpG overlap with prior clocks (max 3 probes) means OMICmAge is not a repackaging of Horvath, Hannum, PhenoAge or GrimAge. It does not by itself mean the new CpGs are more biological. [Paper: Fig. 5a]
- The EBP retention threshold is ρ > 0.2 with the measured value. Some retained proxies are therefore weak stand-ins, and the biological interpretation of a retained EBP inherits that looseness — the authors say explicitly that "not all retained features are causal". [Paper: Fig. 4c; Discussion]
- ICC ≈ 0.998 is technical reproducibility across replicates of the same sample. It is not accuracy and not test–retest stability in a person over time. [Paper: Fig. 3f]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] EMRAge is built on real-world EMR data, where "missingness is universal". [Paper: Discussion]
- [Paper] EMRAge "did not consistently outperform PhenoAge for other incident aging-related diseases" in All of Us, which the authors attribute to shorter follow-up (median 3 vs 5.5 years). [Paper: Discussion]
- [Paper] "More work is necessary to further improve the accuracy and precision of EBPs"; targeted quantitative assays would improve them. [Paper: Discussion]
- [Paper] "It is important to highlight that not all retained features are causal, nor do they necessarily have the strongest overall associations with OMICmAge"; functional or causal modelling is needed. [Paper: Discussion]
- [Paper] Some retained EBPs have little mechanistic backing — ribitol is named as a mortality-predictive metabolite with "very little mechanistic information". [Paper: Discussion]
- [Paper] Future work should test EMRAge across diverse populations and different EMR systems to confirm generalizability. [Paper: Discussion]
- [Paper] A 450K-array version does not yet exist; only 50.8% of the required EBP CpGs are on that platform. [Paper: Results]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| The clocks are trained to predict EMRAge, itself a model estimate | Errors compound along a surrogate chain, and the final model can only be as good as the target it imitates | Every accuracy figure is agreement with an estimate, not with an outcome | Train a methylation clock directly on observed mortality in the same data and compare AUC | [Paper: Fig. 3; "Development of EMRAge"] |
| OMICmAge halves MAE against EMRAge but does not beat DNAmEMRAge on mortality AUC | The added EBP features improve imitation of the target without improving prediction of what the target is for | This is the clearest evidence that the surrogate chain leaks, and it deserves foregrounding | Report both endpoints side by side as co-primary, in the abstract | [Paper: Fig. 3d,e; Fig. 5c] |
| The Discussion argues that lower correlation with chronological age indicates less stochastic and more biological signal | This reasoning rewards a clock for being worse at the thing clocks were originally validated on, and can justify almost any deviation | It is used to defend broad applicability, so it is doing real argumentative work | Pre-register a mechanistic prediction that follows from "non-stochastic physiology" and test it | [Paper: Discussion] |
| EBPs are retained at ρ > 0.2 with their measured counterpart | ρ = 0.2 is about 4% shared variance; such a proxy carries very little of the protein or metabolite it names | The biological narrative rests on what the retained EBPs are named after | Report the ρ distribution of the 40 *retained* EBPs, not just the 396 candidates | [Paper: Fig. 4c] |
| Metabolite clusters are represented by the single member most correlated with EMRAge | The representative is chosen using the outcome, inside a step framed as unsupervised dimension reduction | Selecting on the target before model fitting can inflate downstream performance | Choose cluster representatives by intra-cluster centrality instead, and compare | [Paper: "Metabolomic, proteomic and clinical EBPs"] |
| DNAm clocks are developed in MGB-ABC (n = 3,451; 689 test) while EMRAge comes from 31,264 people | The molecular half of the paper rests on a sample two orders of magnitude smaller than the clinical half | Confidence intervals in Fig. 5b are correspondingly wide, and the paper notes several comparisons fall within them | Report the test-set n prominently beside every clock comparison | [Paper: Results; Fig. 5b] |
| Chronological age wins several endpoints in Generation Scotland and TruDiagnostic | An age-adjusted biomarker losing to age itself suggests limited incremental value on those endpoints | Determines when a clock is worth measuring at all | Report incremental AUC over an age-and-sex baseline for every endpoint and cohort | [Paper: Extended Data Fig. 6] |
| Race is included as a covariate and Black race shows a consistent positive association with OMICmAge | Treating race as a biological adjustment variable can encode structural exposure as intrinsic aging | An aging biomarker deployed clinically would inherit this | Model socioeconomic and exposure variables explicitly and test whether the race term attenuates | [Paper: Fig. 6] |
| 19 clinical variables were selected from 43 by requiring complete data in 31,264 of 60,370 people | Complete-case selection halves the cohort and is unlikely to be missing-at-random in EMR data | The healthiest and the sickest have different missingness patterns | Compare EMRAge fitted with multiple imputation on the full 60,370 | [Paper: "Development of EMRAge"] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: an expensive modality is worth proxying when it supplies training signal rather than inference input — but state the proxy's fidelity, because the deployed model inherits it.
- Agent-derived knowledge candidate: when a model is trained on a surrogate target, always report performance on the *downstream* endpoint too. Improving agreement with the surrogate and improving the endpoint are different results and can diverge, as they do here.
- Agent-derived knowledge candidate: reproducibility (ICC across replicates) and accuracy are orthogonal. Reporting a 0.998 ICC says nothing about whether the number is right.
- Agent-derived knowledge candidate: an argument of the form "our measure correlates less with the obvious variable, therefore it is more biological" is unfalsifiable as stated and needs a mechanistic prediction attached.
- Agent-derived knowledge candidate: when an unsupervised reduction step picks representatives using the outcome, it is not unsupervised. Say so, or pick by an outcome-blind criterion.
- Agent-derived knowledge candidate: always report incremental performance over an age-and-sex baseline for any biological-age measure — several of this paper's external comparisons turn on exactly that.

## 15 Connections to Existing Knowledge

[Analysis] The paper sits squarely in the epigenetic-clock lineage — Horvath and Hannum (chronological age), PhenoAge (clinical phenotype), GrimAge (mortality, and the source of the linear-predictor-to-years rescaling used here), DunedinPACE (pace of aging) — and benchmarks against the principal-component versions of all of them. Its structural novelty is the EBP layer, which is a generalization of the GrimAge trick of predicting plasma proteins from methylation and using those predictions as features; here it is scaled from a handful of proteins to 396 proxies across three data types. The near-zero CpG overlap with every prior clock (maximum 3 shared probes) makes it genuinely distinct in feature space rather than a reweighting.

*On this catalogue's cross-page note for this entry:* the record already flags that OMICmAge is also catalogued on `longitudinal.md` with a fuller entry, and that CONTRIBUTING's routing rule 2 (longitudinal clinical records) precedes rule 3 (molecular data). The full text supports that reading — EMRAge is built from longitudinal EMR data and is the target the whole paper is organized around, with methylation entering as a surrogate for it. If the entry moves, this card should move with it rather than be deleted; nothing in it is specific to this page.

## 16 Research Ideas

### Agent-derived research candidate

**Does the surrogate chain cost anything?** [Hypothesis] Training a methylation clock directly on observed mortality will match or beat OMICmAge on 5- and 10-year survival AUC, showing that the intermediate EMRAge target buys interpretability and EMR portability but not predictive power — and that the EBP layer's apparent gain (MAE 4.97 vs 8.50) is gain against the surrogate only, which is why it does not appear at the endpoint. Delta: in MGB-ABC, fit three clocks on identical folds and identical feature pools — (a) elastic net → EMRAge, the published design; (b) elastic net → observed time-to-death via Cox-penalized regression; (c) elastic net → EMRAge but with the EBP block removed — then evaluate all three, plus published PCGrimAge, on the same held-out mortality endpoint. Validation: pre-register folds and the primary endpoint (10-year survival AUC) before fitting; replicate the full comparison in Generation Scotland, the larger external cohort with mortality follow-up; report incremental AUC over an age-and-sex baseline rather than raw AUC; bootstrap all differences. Falsifier: the direct-mortality clock's AUC confidence interval overlaps OMICmAge's in both cohorts, which would show the surrogate chain is free and would justify EMRAge as a target on portability grounds alone. Failure modes: MGB-ABC has only 83 incident deaths in the test set, likely too few to separate nearby AUCs — the comparison may only be decidable in Generation Scotland; a direct-mortality clock will overfit differently and needs its own regularization search, which must not be tuned on the test folds; competing risks and differential follow-up between cohorts complicate the survival endpoint. Innovation status: unverified; prior-art search required.
