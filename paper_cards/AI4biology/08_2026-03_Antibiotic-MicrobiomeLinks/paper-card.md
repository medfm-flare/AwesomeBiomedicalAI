# Paper Card: Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals

> Source coverage: Open-access full text via PubMed Central (PMC13099378), including Main, Results, all named result subsections, Discussion, Tables 1–2 and all main-figure captions
>
> Extraction confidence: High for the main text, the two in-text tables and figure captions; the 14 Supplementary Tables, 12 Supplementary Figures and Extended Data are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Epidemiology
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Cross-checked against Crossref metadata; the catalogue's open routing question for this entry is addressed in 15
>
> Card completeness: Complete for the main text; Supplementary Tables 1–14 (the association catalogue) and Methods in full were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| NPDR | Swedish National Prescribed Drug Register — every outpatient prescription dispensed in Sweden since 2005 | The exposure source; captures dispensing, not ingestion |
| SCAPIS / SIMPLER / MOS | the three Swedish population cohorts contributing fecal metagenomes | Analysed separately, then meta-analysed; never pooled directly |
| basic vs full model | covariate sets chosen from two directed acyclic graphs | Results quoted are from the full model unless stated |
| alpha diversity | within-sample species diversity: Shannon index, species richness, inverse Simpson | Three metrics, reported together throughout |
| functional regression | spline model over time-since-exposure rather than discrete periods | Used to describe recovery, not to test it |
| negative control exposure | antibiotic use in the *year after* fecal sampling | The paper's confounding check; a true effect is impossible by construction |
| single-course analysis | restriction to people with exactly one or zero courses in 8 years | The cleanest sub-analysis, n = 7,664 |

## 01 Basic Information

- **Title:** Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals
- **Authors:** Gabriel Baldanzi, … , Tove Fall (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature Medicine*, 2026-03. [Paper: Metadata]
- **DOI:** [10.1038/s41591-026-04284-y](https://doi.org/10.1038/s41591-026-04284-y)
- **Cohorts:** SCAPIS (n = 8,488), SIMPLER (n = 4,784) and MOS (n = 1,707); 14,979 individuals total, 14,974 in the adjusted models. Median ages differ sharply between cohorts — ~57 (SCAPIS), ~72 (SIMPLER), ~40 (MOS). Between 69.7% and 73.7% had used any antibiotic in the past 8 years. [Paper: "Study population and antibiotic use"; Table 1]
- **Measurements:** fecal deep shotgun metagenomics, 1,340 species present in >2% of participants; 11 antibiotic classes; three exposure windows (<1, 1–4, 4–8 years before sampling).
- **Access boundary:** the open-access full text was read via PMC. Supplementary Tables 1–14, Supplementary Figures 1–12 and the Extended Data figures were not opened directly.

## 02 One-Sentence Summary

[Paper] Linking Sweden's complete outpatient prescription register to fecal metagenomes from 14,979 adults shows that antibiotics used up to 8 years earlier are still associated with reduced gut species diversity and altered abundance of individual species; that clindamycin, flucloxacillin and fluoroquinolones account for most of it (37.9%, 25.8% and 17.9% of significant species associations) while penicillin V — the most-prescribed antibiotic — accounts for almost none; and that this holds even for people with exactly one course in eight years. [Paper: Abstract; Results]

## 03 Research Question

- [Paper] Does oral antibiotic use in the years before sampling remain associated with gut microbiome composition long after the course has ended, once the confounders that drive high antibiotic use — comorbidity, polypharmacy, other microbiome-active drugs — are controlled for? [Paper: Main]
- [Analysis] The scientific question is about duration; the methodological question is whether an observational design can support a duration claim at all. Most of the paper's machinery exists to answer the second.

## 04 Research Background and Development Path

1. [Paper] Observational studies link recurrent antibiotic use to obesity, type 2 diabetes, cardiovascular disease and colorectal cancer, hypothetically via microbiome disruption. [Paper: Main]
2. [Paper] Small intervention studies in healthy volunteers show drastic short-term changes days after a course — reduced diversity and gene richness, *E. coli* overgrowth, resistance-gene enrichment, higher *C. difficile* risk. [Paper: Main]
3. [Paper] Recovery is only partly understood: partial recovery within weeks, full recovery possibly years, and one study found a quarter of participants had lasting effects up to 2.5 years after ciprofloxacin. [Paper: Discussion]
4. [Paper] Prior population studies (MetaCardis n = 2,173; Estonian Microbiome Cohort n = 2,509) linked cumulative antibiotic use to microbiome variation, but "neither of these studies differentiated recent antibiotic use from past use or performed analysis by antibiotic class". [Paper: Discussion]
5. [Analysis] That sentence is the paper's positioning in one line. The novelty is not the association; it is the resolution — by time window and by drug class simultaneously, at a sample size where both can be estimated.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Short follow-up | Intervention studies run days to months, n = 6–66 | Cost and feasibility of repeated metagenomics | [Paper: Main; Discussion] |
| Aggregated exposure | Prior cohorts pooled "antibiotic use over N years" | Insufficient sample size to split by class and window | [Paper: Discussion] |
| Confounding by indication | Heavy antibiotic users are sicker and take more drugs | Comorbidity, polypharmacy, PPIs, metformin all alter the microbiome | [Paper: "Recent and past use…"] |
| Self-reported exposure | Recall of past antibiotic courses is unreliable | Solved here by register linkage | [Paper: Main] |
| Infection vs antibiotic | Cannot separate the drug from the illness that prompted it | NPDR extract carries no treatment indication | [Paper: Discussion] |
| Batch and cohort effects | Analysis plate was the largest technical source of microbiome variation | DNA extraction and sequencing differ across cohorts | [Paper: "Recent and past use…"; Discussion] |

## 06 Core Idea

- **Surface method:** confounder-adjusted regression of microbiome diversity and per-species abundance on antibiotic courses, per cohort, then inverse-variance fixed-effect meta-analysis.
- **Core insight:** resolve exposure on **two axes at once** — 11 drug classes × 3 time windows — and let the pharmacology validate the statistics. Flucloxacillin, a narrow-spectrum anti-Gram-positive penicillin, hits Bacillota A; fluoroquinolones and clindamycin, broad-spectrum and anti-anaerobe, hit Bacteroidota and Actinomycetota too. The taxonomic pattern matches each drug's known spectrum, which is evidence no confounder would naturally produce. [Paper: Fig. 3; Results]
- **General lesson:** [Analysis] in observational work, the strongest defence against confounding is not another covariate — it is a prediction only the causal hypothesis makes. Drug-specific taxonomic selectivity is that prediction here, and it does more work than the adjustment set.

## 07 Method Overview

**Flow:** NPDR prescription records (8 years pre-sampling) → count courses per antibiotic class per time window → link to fecal shotgun metagenomes → per-cohort regression adjusted for covariates → inverse-variance fixed-effect meta-analysis → FDR < 5%.

**Covariate selection by DAG.** Two directed acyclic graphs were drawn first. The **basic model** covers temporally stable covariates: age, sex, education, smoking, country of birth, plus test-site-specific analysis plate for batch. The **full model** adds BMI, Charlson Comorbidity Index, polypharmacy (≥5 medications) and use of PPIs, metformin, SSRIs, statins, beta-blockers and antipsychotics. [Paper: "Recent and past use…"]

**Exposure modelling:** courses per window as three continuous variables entered simultaneously with restricted cubic splines, so a dose–response shape is estimated rather than assumed.

**Outcomes:** three alpha-diversity metrics; abundance of 1,340 species present in >2% of participants.

**Validation layers:** a negative control exposure (antibiotics dispensed in the year *after* sampling), four alternative exclusion thresholds for recent use, exclusion of people hospitalized for infection (n = 540) or for any reason (n = 5,132), a single-course-only sub-analysis (n = 7,664), sex- and age-stratified models with interaction tests, and generalized VIF for multicollinearity.

**Main workflow figure:** Extended Data Fig. 1 (participant flow). No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Register linkage (NPDR) | Objective, complete exposure history | Removes recall bias entirely | Person → dispensed courses by date | [Paper: Main] | Misses antibiotics given abroad or in hospital — tested by exclusion analyses |
| DAG-driven covariate choice | Principled adjustment set | Prevents both under-adjustment and collider bias | Causal graph → covariate list | [Paper: "Recent and past use…"] | Two models reported; coefficients agree at Spearman 0.95 (diversity) and 0.99 (species) |
| Analysis-plate term | Absorbs batch effects | Plate was the largest technical source of microbiome variation | Sample → plate indicator | [Paper: "Recent and past use…"] | Not removable; a known dominant artefact |
| Restricted cubic splines | Dose–response shape for course count | The first two courses matter more than the third and fourth | Course count → nonlinear term | [Paper: Fig. 1a,b] | Reveals saturation that a linear term would hide |
| Per-cohort fit + meta-analysis | Avoids pooling incompatible cohorts | Cohorts differ in age, sequencing and extraction | 3 fits → 1 pooled estimate | [Paper: Fig. 1c] | Most coefficients had I² = 0, supporting the pooling |
| Negative control exposure | Tests residual confounding | Future antibiotic use cannot cause present microbiome | Post-sampling scripts → null test | [Paper: Extended Data Fig. 2] | **Passed**: no association, so the adjustment set is doing its job |
| Single-course restriction | Isolates a clean contrast | Heavy users differ systematically from non-users | 7,664 people → 1 course vs 0 | [Paper: Extended Data Figs. 3, 4] | The paper's strongest design; costs power for rare classes |
| Functional regression over time | Describes recovery trajectory | Three discrete windows cannot show a curve | Time-since-exposure → spline | [Paper: Fig. 2] | Descriptive; rare classes merged into one predictor for stability |
| Cardiometabolic linkage | Connects affected species to host phenotype | Motivates why microbiome change might matter | 101 shared species → partial Spearman with BMI, WHR, TG, CRP | [Paper: Fig. 4] | Cross-sectional correlation only; no causal chain established |

## 09 Essential Formulas and Symbols

No equations are stated. The statistical apparatus is named rather than derived: linear regression with restricted cubic splines for course count; estimated marginal means with 95% confidence intervals; inverse-variance weighted **fixed-effect** meta-analysis across the three cohorts, with I² reported as the heterogeneity measure; Benjamini–Hochberg FDR at 5% (reported as q-values); likelihood-ratio tests for sex and age interaction terms; generalized variance inflation factor for multicollinearity; partial Spearman correlation for the species–cardiometabolic associations; and a functional regression fitting a cubic spline across time-since-exposure to exploit correlation between temporally adjacent coefficients. [Paper: Results; figure captions]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Dose–response by window | Does each additional course lower diversity? | Diversity falls with each course in all three windows; **the first two courses matter more than the third and fourth** | Saturating dose–response | A per-course causal effect size | [Paper: Fig. 1a,b] |
| Diversity by class, <1 year | Which drugs act recently? | **6 of 11 classes** significant. Species richness: clindamycin **−47 species per course** (q = 2.1 × 10⁻¹⁷), fluoroquinolones **−20** (q = 1.3 × 10⁻⁶), flucloxacillin **−21** (q = 1.4 × 10⁻⁶) | Large, drug-specific recent effects | Equivalence across metrics or classes | [Paper: Fig. 1c] |
| Diversity by class, 1–4 and 4–8 years | Does it persist? | Fluoroquinolones, flucloxacillin and tetracyclines significant at **both** 1–4 and 4–8 years; clindamycin and macrolides at 1–4 but **not** 4–8 | Persistence, but class-dependent | Uniform persistence | [Paper: Fig. 1c] |
| Nitrofurantoin | An outlier positive association | Positive with diversity <1 year (q = 0.043), **not confirmed** in the single-course analysis; authors attribute it to chance or collider bias | Reported and self-discounted | That nitrofurantoin increases diversity | [Paper: Results] |
| Null classes | Where is there no signal? | No association for extended-spectrum penicillins, amoxicillin-clavulanic acid or sulfamethoxazole-trimethoprim | Consistent with intervention data for amoxicillin | Absence of effect — Sweden prescribes amox-clav rarely, so power is low | [Paper: Results; Discussion] |
| Negative control exposure | Is residual confounding present? | Antibiotics dispensed in the year **after** sampling show **no** association with diversity | The adjustment set controls the main confounding | Complete absence of confounding | [Paper: Extended Data Fig. 2] |
| Exclusion-threshold sensitivity | Are results driven by very recent users? | Estimates for 4–8 and 1–4 years "remained largely unchanged" across four exclusion thresholds; only clindamycin <1 year attenuated | Long-window results are robust | — | [Paper: Supplementary Fig. 8] |
| Hospitalization sensitivity | Is it the infection rather than the drug? | Excluding 540 hospitalized for infection: species coefficients Spearman **≥0.87**. Excluding 5,132 hospitalized for any reason: ≥0.87 except amox-clav (0.78) and SMZ-TMP (0.58) | Not explained by severe infection | Exclusion of confounding by outpatient infection, which is not measured | [Paper: Results; Discussion] |
| Species-level associations | How many species move? | Clindamycin <1 year: **296 of 1,340** species; flucloxacillin 203; fluoroquinolones 172. **Penicillin V, the most-prescribed antibiotic: 29** | Class matters far more than frequency of use | Causality per species | [Paper: Fig. 3] |
| Share of all associations | Concentration | Clindamycin **37.9%**, flucloxacillin **25.8%**, fluoroquinolones **17.9%** of FDR < 5% associations | Three drugs dominate | That they are the only drugs with effects | [Paper: Results] |
| Direction of change | Loss or replacement? | Clindamycin 1–4 years: **208 species down, 141 up** | Community restructuring, not only depletion | Which direction is harmful | [Paper: Results] |
| Taxonomic specificity | Does the pattern match pharmacology? | Flucloxacillin (narrow, Gram-positive) → Bacillota A, orders Lachnospirales and Oscillospirales. Clindamycin and fluoroquinolones (broad, anti-anaerobe) → also Bacteroidota and Actinomycetota | Mechanistic coherence | Proof of causation | [Paper: Fig. 3] |
| Single course vs none (n = 7,664) | Does one course suffice? | A single course of tetracyclines, flucloxacillin, fluoroquinolones, clindamycin, SMZ-TMP, cephalosporins or macrolides — at **<4 or 4–8 years** — associated with lower diversity. Species: clindamycin **196**, flucloxacillin **148**, fluoroquinolones **80** species at 4–8 years | The headline claim survives the cleanest contrast | Generalization to rare classes; only 72 people had a single cephalosporin course | [Paper: Extended Data Figs. 3, 4] |
| Functional regression | What does recovery look like? | Fastest recovery in the first ~2 years, markedly slower after; **recovery rate proportional to the size of the initial reduction** | A described trajectory consistent with prior work | A measured recovery — the design is cross-sectional, not longitudinal | [Paper: Fig. 2] |
| Sex and age interactions | Does effect vary by person? | Sex interaction for **74 species** (mostly stronger in women: 22 clindamycin, 15 fluoroquinolone, 11 flucloxacillin); age interaction for **97 species** | Real effect modification | Mechanism — pharmacokinetics vs baseline microbiome | [Paper: Results] |
| Species–cardiometabolic linkage | Does it matter for health? | Among the 101 species associated with all three drugs: *Sellimonas intestinalis*, *R. gnavus*, *E. clostridioformis*, *E. aldenensis*, *T. ramosa* up with antibiotics **and** up with BMI, WHR, TG, CRP; *Alistipes communis* and *Odoribacter splanchnicus* the reverse | A directionally coherent link | A causal path from antibiotics to cardiometabolic disease | [Paper: Fig. 4] |

## 11 Correct Interpretation of the Conclusions

- Every result is an **association at one time point**. The word "recovery" in the functional-regression section describes the shape of a curve fitted across people with different times-since-exposure, not the same people followed over time. The authors say a longitudinal design is what would be needed, and that SCAPIS is collecting second samples now. [Paper: Fig. 2; Discussion]
- The single-course analysis is the strongest evidence here, because it compares people with exactly one course against people with none, removing the confounding that comes with being a frequent antibiotic user. It reproduces the main finding. [Paper: Extended Data Figs. 3, 4]
- The negative control is a genuine test and it passed. Antibiotics dispensed *after* sampling cannot affect the sample, so an association there would have exposed residual confounding; none was found. [Paper: Extended Data Fig. 2]
- "No association" for extended-spectrum penicillins, amoxicillin-clavulanic acid and SMZ-TMP must not be read as no effect: Swedish outpatient prescribing is restrictive and these are rarely used, so power is low. The authors state this explicitly. [Paper: Discussion]
- The nitrofurantoin positive association is reported and then argued against by the authors themselves on the grounds that it did not survive the single-course analysis. [Paper: Results]
- Species counts are not effect sizes. "Clindamycin was associated with 296 species" counts associations passing FDR; it says nothing about how large each shift was.
- Exposure is *dispensing*, not ingestion. Adherence is invisible to the register.

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] Antibiotics given abroad or during hospitalization are not captured by the NPDR, so use is underestimated. [Paper: Discussion]
- [Paper] The NPDR extract "does not include treatment indications, which hampered analyses to distinguish the effect of antibiotics from the effects of infections". [Paper: Discussion]
- [Paper] "Stronger evidence for causality could be achieved from a longitudinal study with sampling before and after the antibiotic course or from a randomized trial." [Paper: Discussion]
- [Paper] The exact date of fecal collection was not systematically recorded; the test-site visit date was used instead. [Paper: Discussion]
- [Paper] Methodological differences in DNA extraction and sequencing across cohorts cannot be fully excluded, though most coefficients had I² = 0. [Paper: Discussion]
- [Paper] Lower detection efficiency for some species in one cohort could bias those estimates toward the null. [Paper: Discussion]
- [Paper] Generalizability may be limited to countries with similar prescribing practices; Swedish antibiotic use is notably restrictive and antimicrobial resistance is comparatively low. [Paper: Discussion]
- [Paper] For rarely prescribed antibiotics, "the absence of associations should not be interpreted as an absence of effect". [Paper: Discussion]
- [Paper] Only 72 individuals had a single cephalosporin course, preventing analysis by generation despite differing spectra. [Paper: Results]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Three cohorts have median ages of ~57, ~72 and ~40 | A fixed-effect meta-analysis assumes one common underlying effect across populations that differ this much | If the true effect varies with age — and the age-interaction analysis says it does for 97 species — a fixed-effect pooled estimate is the wrong summary | Report random-effects estimates alongside; the age-interaction result already argues for it | [Paper: Table 1; Results] |
| Confounding by indication is addressed by hospitalization exclusions | Hospitalized infection is the severe tail; the typical exposure is an outpatient airway, urinary or skin infection, which is never measured | The core alternative explanation — the infection changed the microbiome, not the drug — remains untested for the common case | Compare classes used for the *same* indication but with different spectra, e.g. flucloxacillin vs penicillin V for skin infection | [Paper: Discussion] |
| The negative control is antibiotic use in the year *after* sampling | It controls for stable confounders, but a person's health can change between sampling and the following year | A clean pass here is reassuring but weaker than it looks for time-varying confounding | Add a second negative control with a longer lag, and a negative-control *outcome* unaffected by antibiotics | [Paper: Extended Data Fig. 2] |
| Recovery trajectory is inferred from a cross-sectional spline | Time-since-exposure is confounded with calendar time, age at exposure, and prescribing practice, all of which changed over the 8 years | "Recovery" is the paper's most memorable claim and the least supported by the design | Reserve the claim for the SCAPIS repeat-sampling follow-up the authors describe | [Paper: Fig. 2; Discussion] |
| Prescription counts declined over the study period, except nitrofurantoin which rose | Exposure window and calendar period are entangled: the 4–8 year window contains systematically more prescribing than the <1 year window | Could inflate or deflate the long-window estimates independently of biology | Adjust for calendar year of the prescription, not only survey period | [Paper: "Study population and antibiotic use"] |
| Species-count comparisons across classes | Statistical power differs enormously by class — penicillin V has ~25% users, clindamycin ~4% | Yet clindamycin shows 296 species and penicillin V 29, which is the *opposite* of the power ordering | The comparison is safe in this direction, and stating why would strengthen it; a power-matched subsample would make it airtight | [Paper: Table 2; Fig. 3] |
| Fig. 4 links species to cardiometabolic markers, both measured at sampling | Two cross-sectional associations sharing one time point are not a chain from antibiotic to disease | This is the figure most likely to be read as "antibiotics cause metabolic disease" | Use incident outcomes from register follow-up rather than concurrent markers | [Paper: Fig. 4] |
| Dispensing is used as the exposure | Non-adherence is invisible and non-random — sicker people may adhere more | Biases per-course effect sizes toward the null by an unknown amount | Sensitivity analysis using repeat dispensing as an adherence proxy | [Paper: Main] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: a negative control exposure — something that cannot causally affect the outcome but shares the confounding structure — is a cheap, decisive test of whether an adjustment set is working, and belongs in any observational design.
- Agent-derived knowledge candidate: when a mechanism predicts *which* subgroups should respond, testing that specificity is stronger evidence than any additional covariate. Drug spectrum predicting affected phyla is the model case.
- Agent-derived knowledge candidate: restricting to a clean contrast — exactly one exposure versus none — costs power but removes the confounding that scales with exposure frequency. Report it as a co-primary analysis, not a sensitivity check.
- Agent-derived knowledge candidate: draw the DAG before choosing covariates, and publish both. It converts "we adjusted for these" into a falsifiable claim about the causal structure assumed.
- Agent-derived knowledge candidate: distinguish "no association" from "no effect" whenever exposure prevalence is low, and say which one the data supports.
- Agent-derived knowledge candidate: counts of significant features are a function of power as well as effect. They are only safe to compare across groups when the ordering runs opposite to the power ordering, as it does here.

## 15 Connections to Existing Knowledge

[Analysis] The paper sits between two literatures it explicitly bridges: small intervention studies (n = 6–66) that measure large short-term microbiome disruption with real temporal resolution, and population cohorts (MetaCardis n = 2,173, Estonian Microbiome Cohort n = 2,509) that measure long-term association without resolving class or timing. Its contribution is to bring register-grade exposure resolution to cohort-grade sample size, which is a Nordic-registry capability more than a methodological invention. Downstream, it connects to the register-epidemiology literature on antibiotics and incident disease — the Nurses' Health Study cardiovascular finding (n = 36,429) and the Danish IBD registry study — by supplying the intermediate step those studies assume: that the microbiome is still altered years later.

*On this catalogue's open routing question for this entry:* the full text confirms the record's own assessment. There is no model and no learned component; the analysis is regression plus meta-analysis. The molecular content is real and substantial — deep shotgun metagenomics over 1,340 species — so it is not misplaced among omics, but it belongs with the association studies rather than with the modelling entries, which is what the "Other" group currently encodes. Its closest relative on this page is the Exposome–Phenome Atlas, which shares the exhaustive-testing-plus-FDR shape and the same inability to make causal claims from cross-sectional data.

## 16 Research Ideas

### Agent-derived research candidate

**Same indication, different spectrum.** [Hypothesis] The confounding-by-indication objection can be closed without a trial by contrasting antibiotic classes prescribed for the *same* infection but with different antibacterial spectra — in Swedish outpatient practice, flucloxacillin versus penicillin V for skin and soft-tissue infection, and nitrofurantoin versus pivmecillinam for uncomplicated urinary tract infection. If the infection drives the microbiome change, the two classes should behave alike within an indication; if the drug drives it, they should diverge in the direction their spectra predict. Delta: obtain treatment indication by linking the NPDR extract to primary-care diagnosis codes, then re-run the existing full model restricted within each indication stratum, testing the class contrast directly rather than comparing classes across the whole cohort. Validation: pre-specify the expected taxonomic direction from each drug's spectrum before analysis — flucloxacillin depleting Gram-positive Bacillota A more than penicillin V — and score the prediction, not just the significance; require the contrast to reproduce independently in SCAPIS and SIMPLER; use the single-course subsample as the primary analysis to avoid frequent-user confounding. Falsifier: within an indication, the two classes show statistically indistinguishable diversity and species profiles, which would place the effect with the infection rather than the drug and would substantially weaken the paper's central interpretation. Failure modes: indication data may be unavailable or poorly coded in Swedish primary-care registers; channelling bias means clinicians choose flucloxacillin for more severe skin infection, reintroducing confounding within the stratum; the single-course subsample may be too small once split by indication, particularly for clindamycin. Innovation status: unverified; prior-art search required.
