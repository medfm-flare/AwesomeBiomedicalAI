# Paper Card: An atlas of exposome–phenome associations in health and disease risk

> Source coverage: Open-access full text via PubMed Central (PMC13099396), including Main, Results, all named result subsections, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; the 9 Supplementary Tables, Supplementary Figures and Extended Data are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Resource / benchmark
>
> Secondary analytical lens: Statistical methodology
>
> Context verification: Cross-checked against Crossref metadata; the catalogue's open routing question for this entry is addressed in 15
>
> Card completeness: Complete for the main text; Supplementary Tables 1–9 (including the full association catalogue) were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| exposome | the totality of non-genetic exposures — physical, chemical, psychosocial | The paper's operationalization is 619 measured indicators, not the full concept |
| P-ExWAS | phenotype-by-exposome-wide association study; every exposure against every phenotype | The method; deliberately analogous to GWAS |
| replication rate | fraction of significant associations that reach P < 0.05 in more than one survey wave | The paper's own robustness metric, not a standard one |
| poly-exposomic model | up to 20 exposures modelled simultaneously for one phenotype | The aggregate counterpart to a polygenic score |
| exposome globe | a network plot of exposure–exposure correlations | A visualization, not an inferential result |
| shared associational architecture | correlation between two exposures' association profiles across all phenotypes | Measures whether two exposures "act alike" phenome-wide |
| incremental R² | variance explained by exposures after removing demographics | Every R² in the paper is incremental; the raw numbers would be much larger |

## 01 Basic Information

- **Title:** An atlas of exposome–phenome associations in health and disease risk
- **Authors:** Chirag J. Patel, … , Arjun K. Manrai. [Paper: Metadata]
- **Venue / date:** *Nature Medicine*, 2026-03. [Paper: Metadata]
- **DOI:** [10.1038/s41591-026-04266-0](https://doi.org/10.1038/s41591-026-04266-0)
- **Data:** US CDC NHANES, ten serial cross-sectional waves 1999–2018. Catalogued: 374 continuous phenotypes and 810 exposure biomarkers or questionnaire responses; analyzed: **305 phenotypes × 619 exposures**, 123,774 estimable pairs. Median age 40; median income-to-poverty ratio 2.9. External genetic comparison uses UK Biobank. [Paper: Results; Fig. 1]
- **Access boundary:** the open-access full text was read via PMC. Supplementary Tables 1–9 (which hold the actual association catalogue), Supplementary Figures and Extended Data figures were not opened directly.

## 02 One-Sentence Summary

[Paper] An exposome-wide association study of 619 exposures against 305 quantitative phenotypes across ten NHANES waves finds that individual exposures explain a median 0.14% of phenotypic variance, that replicable signal concentrates in cardiometabolic, anthropometric and pulmonary traits, and that aggregating ~20 exposures into a poly-exposomic model explains variance comparable to a whole genome-wide polygenic score — while a dense exposure–exposure correlation web makes attributing any of it to a single cause unsafe. [Paper: Abstract; Results]

## 03 Research Question

- [Paper] Which exposures, if measured, would meaningfully improve risk stratification or refine prognosis, and how large are those effects relative to demographics and genetics? [Paper: Main]
- [Analysis] This is a prioritization question, not a discovery question. The paper's value is that it makes negative and small results visible at the same scale as positive ones — which the candidate-study literature, spread across millions of papers, structurally cannot do.

## 04 Research Background and Development Path

1. [Paper] Exposome–phenome relationships have been interrogated almost entirely through candidate studies targeting a few exposures and a few phenotypes. [Paper: Main]
2. [Paper] Those studies are "presented selectively in millions of papers on claimed associations", yielding fragmented and often biased snapshots, and many reported results may be false positives. [Paper: Main]
3. [Paper] Nutritional and environmental epidemiology have both seen their single-factor associations fail to hold up. [Paper: Main]
4. [Paper] Bradford Hill's causal criteria may not transfer to a setting where most true effects are small, biological plausibility is not readily discernible, and experimental validation is impossible. [Paper: Main]
5. [Analysis] The move is the one GWAS made two decades earlier: replace selective candidate testing with exhaustive testing plus a multiple-comparison threshold, and let the size distribution of effects speak. The paper is explicit about the analogy and carries it through to the poly-exposomic-versus-polygenic comparison.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Selective reporting | Millions of candidate papers, few robust associations | Candidate design plus publication incentives | [Paper: Main] |
| Small effects, no framework | Bradford Hill criteria do not apply | Small effects, no plausibility prior, no experiments possible | [Paper: Main] |
| Self-report noise | Dietary recall associations are diluted | Day-1 vs Day-2 recall correlate only 0.36 | [Paper: "Consistency of associations across exposure categories"] |
| Analytic sensitivity | 15% of significant pairs flip sign under different demographic adjustment | Confounding by age, sex and socioeconomic factors | [Paper: "Demographic adjustment influences association sizes"] |
| Dense exposure correlation | Exposures rarely act in isolation | Shared sources, behaviours and metabolism | [Paper: Fig. 5; Discussion] |
| Cross-sectional design | Cannot separate chronic accumulation from acute reverse causation | NHANES is serial cross-sectional, not longitudinal | [Paper: Discussion] |

## 06 Core Idea

- **Surface method:** survey-weighted regression of every phenotype on every exposure, with Bonferroni and Benjamini–Yekutieli control.
- **Core insight:** run the *same* analysis nine ways — nine demographic adjustment specifications — and ten times — once per survey wave — then report the disagreement as a first-class result rather than choosing one specification and reporting it alone. The replication rate (41% for Bonferroni-significant pairs vs 0.8% for non-significant) and the sign-flip rate (15%) are outputs of that design. [Paper: "Phenotype–exposure associations replicate across cohorts"; "Demographic adjustment influences association sizes"]
- **General lesson:** [Analysis] when the analyst has many defensible specifications and the effects are small, the spread across specifications is the finding. Reporting one number from one model in this regime is not a summary — it is a selection.

## 07 Method Overview

**Flow:** harmonize ten NHANES waves → catalogue 374 phenotypes and 810 exposure indicators → scale continuous variables by their standard deviation → survey-weighted regression of each phenotype on each exposure under **nine adjustment scenarios** → standardized β, P value and R² per pair → Bonferroni (α ≈ 4 × 10⁻⁷) and Benjamini–Yekutieli FDR → per-wave re-estimation for replication rate. [Paper: Results, "Exposure-wide associations across the phenome"]

The **main model** adjusts for age, age², sex, income-to-poverty ratio, ethnicity (5 groups), education (3 groups) and survey year. The other eight scenarios drop or substitute subsets of these, down to a fully unadjusted base model. [Paper: Results]

**Aggregate models:** for phenotypes with more than 20 FDR-significant exposures, up to 20 exposures are modelled simultaneously with imputation of missing exposure values, producing the poly-exposomic R². [Paper: "Variance explained of the exposome"]

**External comparison:** incremental R² from ~1M imputed genotypes in UK Biobank for 29 phenotypes, against the poly-exposomic R² for the same traits. [Paper: "Comparison with GWAS"]

**Main workflow figure:** Fig. 1 and Extended Data Fig. 1. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Survey-weighted regression | Accounts for NHANES's complex sampling design | Unweighted estimates would not represent the US population | Exposure + covariates → β, P, R² | [Paper: Results] | Not optional for NHANES; not ablated |
| Nine adjustment scenarios | Quantifies analytic sensitivity | Confounder choice is a researcher degree of freedom | One pair → nine estimates | [Paper: Extended Data Fig. 3] | **Load-bearing**: produces the 15% sign-flip finding |
| Per-wave re-estimation | Internal replication across ten independent samples | Distinguishes signal from single-sample noise | Pooled fit → ten fits | [Paper: "Phenotype–exposure associations replicate…"] | **Load-bearing**: the 41% vs 0.8% contrast is the paper's main quality filter |
| Bonferroni + Benjamini–Yekutieli | Multiple-comparison control over 123,774 tests | Naive testing would produce thousands of false positives | P values → thresholds | [Paper: Results] | BY is the dependence-robust FDR variant, appropriate given correlated exposures |
| Demographic-subtracted R² | Isolates exposure contribution from demographics | Demographics alone explain 0–80% of variance | Full vs demographics-only fit → incremental R² | [Paper: Fig. 3d] | Every reported R² is incremental; raw R² would be far larger and uninformative |
| Poly-exposomic aggregation (≤20 exposures) | Aggregate rather than single-exposure effect | Single exposures are too small to matter clinically | Exposure set → joint R² | [Paper: Fig. 3d] | Requires imputation of missing exposures; correlated predictors make attribution unsafe |
| Exposome globe | Displays exposure–exposure correlation structure | Makes the attribution problem visible | Correlation matrix → network | [Paper: Fig. 5a,b] | Descriptive only; thresholded at \|r\| > 0.25 |
| Shared associational architecture | Correlates two exposures' phenome-wide β profiles | Detects exposures that are statistically interchangeable | Two β vectors → correlation | [Paper: Extended Data Fig. 7] | Diagnostic; e.g. trans- vs cis-β-carotene at 0.98 |
| Age × exposure interaction | Tests whether effects vary with age | Susceptibility windows are a standard hypothesis | Interaction term → ΔR² | [Paper: Extended Data Fig. 6] | Tested and largely **negative**: only marginal R² improvement |

## 09 Essential Formulas and Symbols

No equations are stated. The estimand is a standardized regression coefficient: the change in phenotype per 1-s.d. increase in log-transformed continuous exposure, or the difference from a predefined reference group for categorical exposures ("adjusted beta" in Fig. 4). Variance explained is reported as *incremental* R² — the model R² minus the R² of a demographics-only model. Significance thresholds: Bonferroni α ≈ 4 × 10⁻⁷ (0.05 over ~123,774 tests) and Benjamini–Yekutieli FDR, whose 5% level corresponds to P = 5.1 × 10⁻⁴. Between-wave heterogeneity is reported as I². [Paper: Results]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Full P-ExWAS, 123,774 pairs | How much of the exposome associates at all? | **5,674 (5%) pass Bonferroni**; 15,386 (12%) pass FDR 5% | Most tested exposure–phenotype pairs show nothing | That the 5% are causal | [Paper: Fig. 2a] |
| Per-phenotype hit rate | Which phenotypes are exposure-sensitive? | Mean 5% of tests significant (range 0.25–20%); **bilirubin, waist circumference and BMI top at 20%** | Signal concentrates in anthropometric and cardiometabolic traits | That these traits are the most environmentally caused | [Paper: Results] |
| Per-category hit rate | Which exposure classes matter? | Smoking ~15%, dietary/nutrient biomarkers ~13% | Smoking and nutrition dominate | Equivalence of effect size across those categories | [Paper: Fig. 2c] |
| Replication across waves | Do significant findings hold in independent samples? | Bonferroni-significant: **41% replicate**; non-significant: **0.8%**. Among the 1,211 pairs testable in all ten waves, **only 13%** replicated, and **76% were nominally significant in zero waves** | Significance screening works, but per-wave replication is low | That a Bonferroni-significant association will reproduce | [Paper: "Phenotype–exposure associations replicate…"] |
| Single-exposure R² | How big is one exposure? | Median incremental R² **0.14%**; Bonferroni-significant median **0.6%** (IQR 0.3–1%) | Individual exposures are clinically negligible alone | That they are unimportant in aggregate | [Paper: Fig. 3a,b] |
| Poly-exposomic R² | How big are 20 together? | Median **3.5%** (IQR 1.8–7.9%) across 119 phenotypes; **maximum 43% for triglycerides** | Aggregation buys an order of magnitude | Independent contributions — the exposures are correlated | [Paper: Fig. 3d] |
| Triglyceride decomposition | What drives the largest signal? | trans,trans-9,12-octadecadienoic acid, α-tocopherol and γ-tocopherol contribute most, positively, after adjusting for total cholesterol | Lipid risk is embedded in dietary and pollutant context | Causal or interventional interpretation | [Paper: Results] |
| Exposome vs genome, 29 phenotypes | Is exposome comparable to polygenic? | Median incremental R²: genetics **7.9%** (IQR 2.8–9.3, max 21%); exposome **7.9%** (max 57%). **55% (16/29) of phenotypes had higher exposomic R²**; BMI ~10% for both | Aggregate exposome rivals a genome-wide array | Like-for-like comparison — different cohorts, different variable counts | [Paper: "Comparison with GWAS"] |
| Adjustment sensitivity | How stable are the estimates? | **932 of 5,194 (15%)** Bonferroni-significant pairs flip sign between univariate and adjusted models; blood cadmium–BMI is the worked example | Analytic choice materially changes conclusions | That the adjusted model is the correct one | [Paper: Extended Data Fig. 3] |
| Self-report vs biomarker | Does measurement modality matter? | Day-1 vs Day-2 dietary recall r = **0.36**; self-report median R² **0.2%** vs dietary biomarker **1%** (5×); recall–biomarker correlation only **0.52** | Objective assays carry substantially more signal | That biomarkers measure the same construct as recall — r = 0.52 says otherwise | [Paper: "Consistency of associations…"] |
| Blood vs urine pollutants | Is the biomarker signal internally consistent? | Association-profile correlation **0.72** overall; cotinine **0.96**, cadmium 0.78, mercury 0.71 | Biomarker-based associations are robust to matrix | — | [Paper: Extended Data Fig. 4c] |
| Lung function biomarkers | Which smoking marker for FEV₁? | NNAL (half-life 10–16 d) **−0.06 per s.d., R² 0.2%**; cotinine (short half-life) **−0.03, R² 0.08%** | Longer-half-life biomarkers give a better cumulative-exposure read | That NNAL is the causal agent | [Paper: "Consistency of exposome associations for lung function"] |
| Epigenetic and cognitive aging | Does the method extend to omic clocks? | GrimAgeMort: strongest with smoking, heavy metals, physical activity; physical activity alone <1% R², **ten exposures reach 10%** | The approach transfers to methylation-derived phenotypes | Causal effect on biological aging | [Paper: "Exposome correlates of methylation and cognitive aging"] |
| Age × exposure interactions | Do effects vary by age? | **Only marginal R² improvement** for most phenotypes; median effect-size difference age 40 vs 80 was −0.0005 | Largely a null result, reported | That susceptibility windows do not exist — cross-sectional data cannot test that | [Paper: Extended Data Fig. 6] |
| Exposure–exposure correlation | How entangled is the exposome? | Median \|r\| 0.05 overall; among Bonferroni-significant correlations median **0.19**, 95th percentile **0.69** | A dense web, concentrated in the significant subset | — | [Paper: Fig. 5c] |
| Benchmark against prior ExWAS | Is the atlas concordant with existing work? | Directionally consistent and robust against three published exposure-wide analyses | External coherence | Novel validation — these are prior analyses, not independent cohorts | [Paper: "Comparison with GWAS"] |

## 11 Correct Interpretation of the Conclusions

- Every R² in the paper is **incremental over demographics**, which themselves explain 0–80% of phenotypic variance. The exposome numbers are what remains after age, sex, ethnicity, income and education have taken their share. [Paper: Fig. 3d]
- The exposome-versus-genome comparison is a comparison of *variance explained*, not of causal contribution, and it is not like-for-like: ~1M genotypes in UK Biobank against 20 exposures in NHANES, in different populations with different sampling frames. The authors flag the sampling-frame problem, including volunteer bias in UK Biobank. [Paper: "Comparison with GWAS"; Discussion]
- "Replication rate 41%" is the *optimistic* figure, computed as significance in more than one wave. Restricted to the 1,211 associations testable in all ten waves, only 13% replicated and 76% were nominally significant in none of them. Both numbers are in the paper. [Paper: "Phenotype–exposure associations replicate…"]
- The 43% figure for triglycerides is the maximum across all phenotypes, not a typical value; the median poly-exposomic R² is 3.5%. [Paper: Fig. 3d]
- The dense correlation web is presented as an obstacle to attribution, not as a discovery. The authors are explicit that top signals must be read as mixtures. [Paper: Discussion]
- The 15% sign-flip result is a warning about the whole literature this atlas is meant to supersede, and it applies to this atlas too — the main model is one specification among nine. [Paper: Extended Data Fig. 3]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] "Despite cataloging hundreds of factors, we capture only a fraction of the total exposome." [Paper: Discussion]
- [Paper] "The cross-sectional design limits causal inference and the capture of cumulative lifetime exposures", and cannot distinguish chronic accumulation from acute reverse-causal effects. [Paper: Discussion]
- [Paper] "Most of the exposome tabulated here adds little incremental clinically relevant predictive value for many phenotypes." [Paper: Discussion]
- [Paper] "Inferred exposure–phenotype relationships are sensitive to analytical choices and confounding control." [Paper: Discussion]
- [Paper] Cross-cohort comparison is complicated by differences in sampling frames, including volunteer bias in cohorts such as UK Biobank. [Paper: Discussion]
- [Paper] Cancer-related phenotypes are underrepresented in the atlas. [Paper: Discussion]
- [Paper] Characterizing exposure–exposure and gene–environment interactions "will require larger sample sizes and broader, high-resolution chemical profiling". [Paper: Discussion]
- [Paper] "Exposomics, at present, is associational discovery" — the authors set out a triangulation programme (replication ranking, longitudinal temporality, Mendelian randomization, functional exposomics, randomized intervention) as what would be needed for causal claims. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| The abstract says poly-exposomic models explain variance "comparable to genome-wide polygenic scores" | The comparison crosses cohorts (NHANES vs UK Biobank), variable counts (20 vs ~1M) and selection procedures (exposures chosen by FDR significance *in the same data*) | This is the paper's most quotable claim and the one most likely to be repeated without its caveats | Select the 20 exposures in one wave and estimate R² in held-out waves; select SNPs by the same procedure for a fair contrast | [Paper: "Comparison with GWAS"] |
| Poly-exposomic exposures are chosen because they were FDR-significant in the same dataset | Selection and estimation share data, which inflates R² | Determines whether 3.5% median and 43% maximum are honest out-of-sample numbers | Wave-split or cross-validated poly-exposomic R² | [Paper: "Variance explained of the exposome"] |
| Missing exposures were imputed before the aggregate models | Imputation across a dense correlation web can propagate the correlations being modelled | Aggregate R² could partly reflect imputation structure | Report aggregate R² on complete cases only, alongside the imputed estimate | [Paper: "Variance explained of the exposome"] |
| Nine adjustment scenarios are run, and one is designated "main" | Once the spread is known, presenting one model as primary re-imports the selection problem the paper diagnoses | The atlas in Fig. 4 is a single specification | Publish the atlas as a distribution over specifications, or as a vibration-of-effects interval per cell | [Paper: Results; Extended Data Fig. 3] |
| Replication is defined as nominal P < 0.05 in more than one wave | An uncorrected threshold applied to already-selected pairs; with ten waves, "more than one" is a weak bar | 41% is the number most likely to be cited as evidence of robustness | Report replication at a corrected threshold and as a function of the number of waves available, which Extended Data Fig. 3 partly does | [Paper: "Phenotype–exposure associations replicate…"] |
| Ten NHANES waves are described as independent samples | Same instrument, same protocols, same national frame — independent draws, not independent studies | Shared instrument bias replicates just as well as a real effect | Attempt replication in a cohort with different assays, e.g. the serum-only Chinese cohort the Discussion cites | [Paper: Results; Discussion] |
| Self-reported diet is judged against biomarkers as ground truth | Recall–biomarker correlation of 0.52 means they measure partly different things, not that one is noisy | "Prioritize biomarkers" is the paper's clearest practical recommendation | Model both jointly and test whether recall adds incremental R² over the biomarker | [Paper: "Consistency of associations…"] |
| 15% of significant associations flip sign under adjustment | Reported as a sensitivity result, but the atlas is then presented from the adjusted model | A sign flip is not a magnitude change; the direction of a health recommendation reverses | Flag the flipping pairs in the published atlas so downstream users see them | [Paper: Extended Data Fig. 3b] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: when many specifications are defensible, report the distribution across specifications; a single reported estimate in that regime is a selection, not a summary.
- Agent-derived knowledge candidate: an internal replication rate computed across sub-samples is a cheap and powerful filter — 41% versus 0.8% separates screened from unscreened findings far more informatively than a P value alone.
- Agent-derived knowledge candidate: always state whether R² is raw or incremental over covariates. Here the incremental framing is what makes a 3.5% median meaningful rather than embarrassing.
- Agent-derived knowledge candidate: when comparing variance explained across two predictor sets, hold the selection procedure constant or the comparison measures selection, not biology.
- Agent-derived knowledge candidate: measurement half-life is a design variable. NNAL beats cotinine for FEV₁ not because it is more toxic but because it integrates over a longer window.
- Agent-derived knowledge candidate: publishing the null and small-effect mass at the same resolution as the hits is what makes an atlas useful; the value is in the denominators.

## 15 Connections to Existing Knowledge

[Analysis] The paper is a deliberate transplant of GWAS methodology — exhaustive testing, genome-wide-style significance thresholds, replication across samples, and an aggregate score benchmarked against its genetic counterpart — into environmental epidemiology, and it says so. Its stated complements are the HHEAR data centre and a serum-only exposome mapping in a Chinese cohort (267 chemicals, 5,700 volunteers), which trade breadth against the biomarker depth NHANES provides.

*On this catalogue's open routing question for this entry:* the full text strengthens the case for keeping it on a biology page rather than moving it. The exposures that carry the signal are molecular assays — serum nutrient and tocopherol concentrations, organochlorine and heavy-metal biomarkers, urinary tobacco metabolites — not questionnaire items, and the paper's own finding is that the questionnaire arm is five times weaker. Two of its phenotypes are methylation-derived epigenetic clocks (Horvath, GrimAge), and the Discussion's forward programme is explicitly "functional exposomics" using proteomics, metabolomics and methylomics. It remains an association study with no model, which is the real argument for the "Other" group it currently sits in.

## 16 Research Ideas

### Agent-derived research candidate

**Does the poly-exposomic score survive out-of-sample?** [Hypothesis] The reported poly-exposomic R² — median 3.5%, maximum 43% for triglycerides — is materially inflated because the ≤20 exposures entering each model were selected for FDR significance in the same pooled data used to estimate the model, and an honest wave-held-out estimate will fall enough to change the headline comparison with polygenic scores. Delta: refit the entire aggregate analysis under strict wave separation — select exposures using waves 1999–2010 only, estimate R² in waves 2011–2018 only, never letting the test waves inform selection or imputation — and compare against the published pooled estimate for the same phenotypes. Validation: all 119 phenotypes with ≥20 FDR-significant exposures; report paired pooled-vs-held-out R² with bootstrap intervals; repeat under all nine demographic adjustment specifications so the result is reported as a range rather than a point; apply the identical select-then-test discipline to the UK Biobank genetic comparison so both sides of the exposome-vs-genome claim are estimated the same way. Falsifier: held-out poly-exposomic R² falls within the bootstrap interval of the pooled estimate for most phenotypes, showing selection bias is negligible at this sample size and the comparison stands as published. Failure modes: later NHANES waves measure a different exposure panel, so selected exposures may be unavailable in the test waves; splitting by wave confounds selection bias with genuine secular change in exposure distributions (leaded fuel, trans-fat bans); imputation of missing exposures must be refit within the training waves only or the leak reappears. Innovation status: unverified; prior-art search required.
