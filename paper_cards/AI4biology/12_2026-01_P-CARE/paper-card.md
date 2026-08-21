# Paper Card: Genomic risk model to implement precision prostate cancer screening in clinical care: the ProGRESS study

> Source coverage: Open-access full text via PubMed Central (PMC13181739), including Results, Discussion, Methods and all main-figure and table captions
>
> Extraction confidence: High for the main text, Methods and figure captions; Supplemental Tables 1–11, Supplementary Data and the example clinical report are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Clinical evaluation
>
> Secondary analytical lens: Translation / implementation
>
> Context verification: Cross-checked against Crossref metadata, the authors' released code and the ClinicalTrials.gov registration NCT05926102; this card resolves the catalogue record's open full-text pass
>
> Card completeness: Complete for the main text and Methods; Supplemental Tables 1–11 and the Supplementary Data variant list were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| P-CARE | Prostate CAncer integrated Risk Evaluation — PHS601 + genetic principal components + family history | The deployed model |
| PHS601 | polygenic hazard score over 601 variants, selected by LASSO-Cox from 707 candidates | The polygenic component alone |
| PHS290 | the authors' prior 290-variant score | The predecessor being improved on |
| genetic ancestry | modelled as **continuous principal components**, never as discrete categories | A deliberate design choice, argued at length in the Discussion |
| BGE | blended genome-exome assay — high-coverage exome plus low-coverage whole genome | The clinical laboratory platform |
| HR80/50, HR20/50 | hazard ratio of the 80th or 20th percentile against the median | The paper's stratification metric |
| risk-equivalent age | the age at which a high-risk man reaches the risk a standard-risk man has at some later age | How the model translates into screening timing |
| ProGRESS | the randomized trial (NCT05926102) deploying the model, 5,000 VA patients | Ongoing; no outcomes reported here |

## 01 Basic Information

- **Title:** Genomic risk model to implement precision prostate cancer screening in clinical care: the ProGRESS study
- **Authors:** Jason L. Vassy, … , Tyler M. Seibert (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature Cancer*, 2026-01. [Paper: Metadata]
- **DOI:** [10.1038/s43018-025-01103-0](https://doi.org/10.1038/s43018-025-01103-0)
- **Code:** [precimed/MVP-PCa-PHS](https://github.com/precimed/MVP-PCa-PHS)
- **Trial registration:** ClinicalTrials.gov **NCT05926102** (ProGRESS), randomizing 5,000 screen-eligible VA patients to usual care versus P-CARE-informed precision screening.
- **Development cohort:** **585,418 male Million Veteran Program participants**, genotyped on a custom Affymetrix Axiom biobank array of 723,305 variants enriched for low-frequency variants in African and Hispanic populations. [Paper: Methods, "Million Veteran Program"]
- **External validation:** four PRACTICAL Consortium datasets — African ancestry (n = 6,253), Asian ancestry (n = 2,320), Cohort of Swedish Men (n = 3,415), and ProtecT (biopsy results for men with PSA ≥ 3 ng/mL); plus All of Us v7 (4,473 cases, 69,858 controls). [Paper: Methods]
- **Access boundary:** the open-access full text was read via PMC. Supplemental Tables 1–11, the Supplementary Data variant list and the example clinical report package were not opened directly.

## 02 One-Sentence Summary

[Paper] P-CARE combines a 601-variant polygenic hazard score with continuous genetic ancestry and family history, trained on 585,418 Million Veteran Program men and validated across four PRACTICAL cohorts and All of Us, to stratify risk of any, clinically significant, metastatic and fatal prostate cancer — and has been carried all the way through clinical laboratory validation on a blended genome-exome assay into a randomized trial of precision screening. [Paper: Abstract; Results]

## 03 Research Question

- [Paper] Can a genomic risk model distinguish the men most likely to benefit from prostate cancer screening from those for whom its harms may outweigh its benefits, and can it be implemented in a real health system rather than only demonstrated in a biobank? [Paper: Discussion]
- [Analysis] The second half is the paper's actual subject. The statistical result — a polygenic score stratifies prostate cancer risk — is well established. What is new is the unbroken chain from biobank to CLIA-grade assay to clinical report to randomized trial, with each link's failure modes reported.

## 04 Research Background and Development Path

1. [Paper] PSA screening reduces prostate cancer mortality in randomized trials, but guidelines disagree on balancing early detection against overdiagnosis of indolent disease and harms from unnecessary procedures; screening practice is consequently highly variable. [Paper: Discussion]
2. [Paper] Risk models that inform net benefit depend on **calibration within a population**, so estimates from a health-system-linked biobank are especially informative for patients in that system. [Paper: Discussion]
3. [Paper] Polygenic score effect sizes vary between biobanks, so a model must be validated where it will be used. [Paper: Discussion]
4. [Paper] The net benefit of screening depends on downstream diagnostic and therapeutic practice, which is system-specific. [Paper: Discussion]
5. [Paper] Black men are more likely to be diagnosed with and die from prostate cancer, and guidelines name them for earlier screening — but using race in medical decisions "can inappropriately ascribe to biology effects that arise from a complex social construct". [Paper: Discussion]
6. [Analysis] Points 2–4 are an argument that this kind of model cannot be developed once and shipped. The paper's own framing is that portability is *not* the goal; calibration in the deploying system is.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Screening ambivalence | Guidelines vary by organization and country | Benefits and harms are close in the average man | [Paper: Discussion] |
| Undifferentiated risk | PSA applied uniformly regardless of underlying risk | No routinely available stratification tool | [Paper: Discussion] |
| Low PSA specificity | PPV of PSA ≥ 3 ng/mL is 0.13 in ProtecT | PSA rises for benign reasons too | [Paper: Fig. 2] |
| Race as a proxy | Guidelines use a social category as a biological risk factor | Genetic, environmental and structural causes are confounded | [Paper: Discussion] |
| Unknown carrier status | Rare pathogenic variants unknown for nearly all screen-eligible men | Genomic testing is not routine | [Paper: Discussion] |
| Discovery–implementation gap | Models validated in biobanks rarely reach clinical assays | No CLIA-grade platform, report or trial pathway | [Paper: Results, "Overview…"] |

## 06 Core Idea

- **Surface method:** a LASSO-regularized Cox proportional-hazards polygenic hazard score, combined with principal components and family history.
- **Core insight:** two design choices do most of the work. First, the outcome is modelled as **age at diagnosis** in a time-to-event framework rather than as case/control status — which is what makes "risk-equivalent age" expressible, and screening timing is an age decision. Second, ancestry enters as **continuous principal components** rather than discrete race or ancestry categories, so the model can capture the elevated risk that motivates guideline recommendations for Black men without encoding race as biology. The reported consequence is that most Black men, but not all, land in the high-risk category. [Paper: Methods; Discussion]
- **General lesson:** [Analysis] the estimand should match the decision. A model that outputs "risk category" answers a different question than one that outputs "you reach the standard 55-year-old's risk at age 50" — and only the second tells a clinician when to start screening.

## 07 Method Overview

**Variant candidates.** 707 unique candidates pooled from five prior sources: 290 from PHS290, 613 multi-ancestry GWAS susceptibility loci, 23 loci for *benign* PSA elevation or BPH, 9 African-ancestry loci, and 128 from a multi-ancestry meta-analysis. [Paper: Methods, "Candidate variants and training…"]

**Score construction.** Correlated pairs (r² > 0.95) reduced by univariable Cox association; remaining candidates entered a Cox model with genotype allele counts plus the first five FastPop principal components (from 2,309 ancestry-informative markers); LASSO regularization with cross-validated error selecting the penalty. **601 of 707 variants retained.** Cases contribute age at diagnosis; controls are censored at last follow-up. [Paper: Methods]

**Model assembly.** A Cox model for age at prostate cancer diagnosis as a function of PHS601 (continuous), family history (paternal history), and principal components. Family history and ancestry were included **a priori** on the basis of prior work, not selected on performance. [Paper: Results, "Association of P-CARE…"]

**Risk categories.** Thresholds set at HR = 0.75 and HR = 1.5 **for metastatic prostate cancer** — the outcome that screening is meant to prevent, not the most common one.

**Clinical implementation.** Blended genome-exome assay carrying both P-CARE and targeted analysis of 12 hereditary prostate cancer genes; a pathogenic or likely pathogenic variant in any of those 12 overrides P-CARE to high risk. Report package links category to tailored screening recommendations. [Paper: Results, "Clinical P-CARE and monogenic reports"]

**Main workflow figure:** Fig. 1. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| LASSO-Cox variant selection | Chooses 601 of 707 candidates | Correlated candidates from overlapping GWAS | Genotypes + age at event → weights | [Paper: Methods] | Penalty chosen by cross-validated error |
| Benign-PSA loci in the candidate pool | 23 variants for benign PSA elevation / BPH | Separates cancer signal from benign PSA rise | Candidates → score | [Paper: Methods] | A subtle and important inclusion for a PSA-triggered pathway |
| Time-to-event outcome | Models age at diagnosis, not case status | Screening is an age decision; also uses controls' follow-up | Ages + censoring → hazard | [Paper: Methods] | Enables risk-equivalent age and cumulative incidence |
| Continuous principal components | Ancestry without discrete categories | Avoids race as a biological variable | 2,309 AIMs → 5 PCs | [Paper: Methods; Discussion] | Authors report ancestry is "mostly accounted for by PHS601" but kept it rather than dropping it post hoc |
| Family history term | Independent clinical risk factor | Significant in Supplemental Table 1 | Paternal history → covariate | [Paper: Results] | Modest at population level, "substantial for individuals" |
| HR-based thresholds on metastatic disease | Defines low / average / high | Ties the cut points to the outcome screening targets | HR 0.75, 1.5 → categories | [Paper: Table 3] | Thresholds are chosen, not derived from a decision analysis |
| BGE assay | One test for polygenic and monogenic risk | Cost-efficient multiplex platform | DNA → PRS + rare variants | [Paper: Results] | **Validated and its failures reported**: PMS2 coverage, small CNVs |
| 12-gene monogenic override | Pathogenic variant ⇒ high risk regardless of P-CARE | Existing NCCN guidelines govern these carriers | Variant → category | [Paper: Results] | Deliberate: PRS is not allowed to modify rare-variant management |
| Clinical report package | Turns risk into screening advice | The deployable artefact | Category → recommendation | [Paper: Results] | Now in use in ProGRESS |

## 09 Essential Formulas and Symbols

No equations are stated. The model is a **Cox proportional-hazards** regression for age at prostate cancer diagnosis, with the polygenic score constructed by **LASSO-regularized Cox** regression over candidate genotype allele counts and five FastPop principal components, the penalty selected to minimize cross-validated error. Reported quantities: hazard ratio per standard deviation of the score; **HR80/50** and **HR20/50**, the hazard ratios at the 80th and 20th percentiles relative to the median; cause-specific cumulative incidence; time-dependent AUC; sensitivity and specificity at the category thresholds; positive predictive value of PSA ≥ 3 ng/mL within P-CARE strata; and odds ratios in the case-control All of Us analysis. A random survival forest was fitted as a robustness check. [Paper: Methods; Results]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| PHS601 in MVP | Does the polygenic score alone stratify? | HR per s.d.: any prostate cancer **2.02** (1.97–2.07), metastatic **2.07** (1.95–2.17), fatal **1.96** (1.75–2.18) | Strong, consistent association including for lethal disease | Causality; these are risk associations | [Paper: Table 1] |
| Ancestry-stratified PHS601 | Does it hold across ancestries? | Similar in every MVP stratum with >100 events and in each PRACTICAL ancestry dataset; Asian PRACTICAL HR **2.11** (1.90–2.39) | Multi-ancestry validity where powered | Validity in small strata — East Asian MVP and "American" subgroups were non-significant for metastatic/fatal, though directionally consistent | [Paper: Table 1] |
| P-CARE in MVP | Does the full model add? | HR per s.d.: any **2.04**, metastatic **2.05**, fatal **1.95** — essentially **identical to PHS601 alone** | The full model performs at population level | That family history and ancestry add population-level discrimination — the Discussion says they do not | [Paper: Table 2; Discussion] |
| Quintile extremes, MVP + PRACTICAL | Risk gradient | Lowest quintile HR **0.35–0.46** vs median; highest quintile HR **2.48–4.03** across the four outcomes | A ~6–10-fold spread between extremes | Clinical utility, which the trial is designed to test | [Paper: Table 2] |
| PPV of PSA within P-CARE strata, ProtecT | Does it sharpen an existing test? | PPV of PSA ≥ 3: **0.13** overall → **0.19** in the top 20% → **0.23** in the top 5% | Nearly doubles PSA's precision in high-risk men | That it improves net benefit — that requires the trial | [Paper: Fig. 2] |
| Risk categories, MVP | Population distribution | **25.1% low, 37.3% average, 37.6% high**; **68.7%** of men with positive family history are high-risk and only 5.6% low-risk; only **2.8%** of self-reported Black participants are low-risk | Categories behave as expected against known risk factors | — | [Paper: Table 3] |
| Cumulative incidence by age 80 | Absolute risk | High-risk group: any **37.4%**, metastatic **4.4%**, fatal **0.8%**. Low-risk metastatic: **0.8%** | Absolute risks usable for counselling | Transportability to other health systems | [Paper: Table 4; Discussion] |
| Risk-equivalent age | Screening timing | A high-risk man reaches the standard 55-year-old's detection risk at **age 50**, and the standard 70-year-old's metastatic risk at **63.5** | Translates a hazard ratio into a screening date | That earlier screening improves outcomes | [Paper: Supplemental Table 11] |
| All of Us external validation | Does it hold in a non-VA cohort? | PHS601 OR per s.d. **1.91** (1.85–1.98); high-risk vs average OR **2.41** (2.25–2.60); low-risk vs average OR **0.48** (0.44–0.54); holds across ancestries | Independent replication | Calibration in All of Us — only discrimination is reported | [Paper: Results; Extended Data Fig. 3] |
| Robustness checks | Is the result method-dependent? | Time-dependent AUC, threshold sensitivity/specificity and **random survival forest** all confirmed consistent discrimination | Not an artefact of the Cox specification | — | [Paper: Supplemental Tables 8–10] |
| BGE analytic validation | Does the clinical assay reproduce the research score? | Pearson **r > 0.998** for PHS601 and **r > 0.999** for both principal components against reference samples; **100% precision** within and between runs | The assay is faithful | — | [Paper: Results] |
| BGE monogenic validation | Does it detect rare variants? | 11 of 12 genes met coverage thresholds; **all 18** variants of interest detected (7 SNVs, 5 indels, 6 CNVs) — but **3 of the 6 CNVs would not have been clinically reported** under pre-specified quality thresholds | Honest, bounded assay performance | Full CNV sensitivity — small CNVs under three exons remain a known gap | [Paper: Results] |
| PMS2 coverage | Known technical weakness | Exons 13–15 undercovered; **80%** of samples missing full coverage in one region, 20% in another | A specific, quantified limitation | — | [Paper: Results] |

## 11 Correct Interpretation of the Conclusions

- **This card resolves the catalogue record's open items.** Training data: 585,418 male MVP participants on a 723,305-variant array. Downstream tasks: age-at-diagnosis risk stratification for any, clinically significant, metastatic and fatal prostate cancer; PSA positive-predictive-value enrichment; risk-equivalent-age calculation for screening timing; and paired monogenic reporting across 12 genes.
- P-CARE and PHS601 alone perform almost identically at the population level. The authors say so directly: "family history and agnostic genetic ancestry have less prognostic value in the current multivariable model than in our prior model." Family history is retained because its effect "is substantial for individuals", which is an individual-decision argument, not a discrimination argument. [Paper: Discussion]
- The model reports **no outcomes**. Every result is risk stratification; whether stratified screening helps anyone is the question ProGRESS is running, and no trial result exists yet.
- Ancestry is handled as continuous principal components specifically so race is not treated as biology. The finding that "most Black men, but not all" are high-risk is the point — the model recovers the group-level signal while still individualizing. The authors are explicit that it "does not fully disentangle the confounded associations between genetic ancestry and social determinants".
- Thresholds are anchored to **metastatic** disease, not to any prostate cancer. That choice makes the categories about the harm screening is meant to avert rather than about detection volume.
- The polygenic score is deliberately **not** allowed to modify rare-variant management: modified associations were judged "not yet robust enough for individual variant-level clinical reporting and should not supersede NCCN guidelines".
- Generalization is explicitly not claimed. "This system-specific model may not generalize to other settings with different population risks and screening practices"; other systems "should examine model calibration in their own data before implementation".

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] "This system-specific model may not generalize to other settings with different population risks and screening practices." [Paper: Discussion]
- [Paper] The model "cannot disentangle the effects of genetic predisposition from environmental exposures and other social determinants that shape prostate cancer risk". [Paper: Discussion]
- [Paper] BGE has "lower sensitivity around complex regions of genes like PMS2 and reduced sensitivity of small copy number variants below 3 exons in size"; a purpose-built capture panel might do better. [Paper: Discussion]
- [Paper] Three of six validation CNVs fell below pre-specified clinical reporting quality thresholds and would not have been reported in practice. [Paper: Results]
- [Paper] Family history and genetic ancestry contribute less than in the prior PHS290-based model. [Paper: Discussion]
- [Paper] Polygenic modification of rare-variant risk is "not yet robust enough" for variant-level clinical reporting. [Paper: Discussion]
- [Paper] Future work should consider additional risk factors and "other machine learning-based prediction approaches". [Paper: Discussion]
- [Paper] Cost-effectiveness is unresolved; ProGRESS is intended to supply the empirical data. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| P-CARE ≈ PHS601 on every population metric | The two extra components add complexity and a family-history data requirement for no measurable population gain | Deployment cost and missing-data burden fall on the simpler score's side | Report net reclassification and decision-curve analysis for P-CARE vs PHS601, not only hazard ratios | [Paper: Tables 1, 2; Discussion] |
| Discrimination is reported; calibration is not | Absolute risks in Table 4 drive counselling and screening timing, and calibration is what makes them trustworthy | The paper's own argument is that calibration within a population is the reason to build system-specific models | Publish calibration plots by ancestry group and by decile in MVP, PRACTICAL and All of Us | [Paper: Table 4; Discussion] |
| Model developed and cross-validated in MVP, then validated externally | Cross-validation within MVP still uses MVP-specific case ascertainment and follow-up | Optimism is bounded by the external cohorts, but the headline HRs are the MVP ones | Report the PRACTICAL and All of Us HRs alongside the MVP HRs in the abstract | [Paper: Methods; Table 2] |
| Category thresholds are HR 0.75 and 1.5 | Round numbers, not the output of a decision analysis weighing overdiagnosis against missed metastatic disease | Where the cut points sit determines who is screened, which is the entire clinical consequence | Derive thresholds from a net-benefit or cost-effectiveness model, and show sensitivity to them | [Paper: Table 3] |
| 37.6% of MVP participants are classified high-risk | More than a third of the population in the elevated tier | A category that includes over a third of men provides limited triage value at the top end | Report the operating characteristics of a narrower high-risk definition alongside | [Paper: Table 3] |
| Only 2.8% of self-reported Black participants are low-risk | The model reproduces the group-level pattern almost completely | If nearly no Black man can be classified low-risk, the model's individualizing benefit is asymmetric across groups | Report category distributions by group *and* whether within-group gradients predict outcomes equally well | [Paper: Table 3; Discussion] |
| The MVP cohort is US veterans | Not representative in age structure, comorbidity, exposure history or healthcare access | The absolute risks in Table 4 are veteran-specific | Already partly addressed by All of Us replication; a calibration comparison across the two would close it | [Paper: Methods; Discussion] |
| Family history is paternal history | Brothers and sons carry substantial information for prostate cancer | A narrower definition weakens a component already found to add little | Test full first-degree family history where available and re-estimate the component's contribution | [Paper: Methods] |
| PPV improvement is from 0.13 to 0.19–0.23 | Still means most positive results in high-risk men are not clinically significant cancer | This is the number that patients experience | Pair PPV with negative predictive value and expected biopsies avoided per cancer detected | [Paper: Fig. 2] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: match the estimand to the decision. Modelling age at diagnosis rather than case status is what makes "risk-equivalent age" available, and screening is fundamentally a question of when, not whether.
- Agent-derived knowledge candidate: continuous ancestry principal components can capture group-level risk differences without encoding race as a biological variable — and the informative result is the exception rate ("most Black men, but not all").
- Agent-derived knowledge candidate: include loci for the *benign* causes of a screening test's positivity in the candidate pool. A model feeding a PSA pathway benefits from knowing what raises PSA without cancer.
- Agent-derived knowledge candidate: anchor risk-category thresholds to the outcome the intervention is meant to prevent (metastatic disease) rather than the most frequent outcome (any diagnosis).
- Agent-derived knowledge candidate: report the assay's failures at the same resolution as its successes — "3 of 6 CNVs would not have been clinically reported" is more useful than "all 18 variants detected", and this paper gives both.
- Agent-derived knowledge candidate: when a simpler nested model matches the full one on every population metric, say so plainly and give the individual-level reason for keeping the extra terms. This paper does.
- Agent-derived knowledge candidate: a risk model destined for clinical use needs calibration evidence, not only discrimination; hazard ratios cannot support the absolute-risk statements that drive counselling.

## 15 Connections to Existing Knowledge

[Analysis] P-CARE is the successor to the same group's PHS290, and its variant pool is assembled from the multi-ancestry prostate cancer GWAS literature rather than discovered here — so the modelling contribution is selection and integration, not discovery. Its framing borrows explicitly from breast cancer screening models, which likewise combine polygenic risk with family history and rare variants rather than replacing them, and it defers to NCCN guidelines for monogenic carriers instead of letting the polygenic score modify their management.

Within this catalogue it is the clearest example of a *translational* entry: it introduces no new architecture — a LASSO-Cox model is decades-old machinery — and its novelty is entirely in the pipeline from biobank to CLIA-validated assay to clinical report to a registered randomized trial. That makes it a useful contrast with the modelling entries on this page. It also pairs naturally with the other genomics entries: where AlphaGenome and Evo 2 predict the molecular consequences of individual variants, P-CARE aggregates 601 variants into a single actuarial hazard and never asks what any of them does mechanistically.

## 16 Research Ideas

### Agent-derived research candidate

**Does the model's benefit reach everyone it classifies?** [Hypothesis] P-CARE's within-group risk gradient is materially weaker in men of African genetic ancestry than in men of European ancestry — the near-absence of low-risk classifications among self-reported Black participants (2.8%) reflects a compressed usable range rather than uniformly high true risk — so the model individualizes screening decisions less well in precisely the group whose disparity motivated it. Delta: rather than reporting pooled HR-per-standard-deviation by ancestry stratum, which can look similar while the underlying calibration differs, estimate **calibration slope and intercept, and decile-level observed-versus-expected cumulative incidence**, separately within each ancestry stratum in MVP, in the PRACTICAL African-ancestry cohort and in All of Us; then compute, per stratum, the fraction of men whose screening recommendation would actually change relative to age-based guidelines. Validation: pre-specify calibration-in-the-large and calibration slope as co-primary endpoints; bootstrap confidence intervals for the between-stratum difference; replicate the analysis using self-reported race as the stratifier as well as genetic ancestry, since the paper reports both and they are not interchangeable; use decision-curve analysis at the deployed HR 0.75 / 1.5 thresholds to express the result in net-benefit terms. Falsifier: calibration slopes and the proportion of recommendation-changing classifications are equivalent across strata within their confidence intervals, indicating the compressed low-risk fraction reflects genuine population risk rather than reduced model resolution. Failure modes: African-ancestry strata may have too few metastatic and fatal events for stable decile-level calibration, particularly in PRACTICAL; differential ascertainment of prostate cancer diagnosis by race within the VA would bias observed incidence and be indistinguishable from miscalibration; genetic ancestry and self-reported race disagree for a substantial minority, so stratum definition itself affects the result. Innovation status: unverified; prior-art search required.
