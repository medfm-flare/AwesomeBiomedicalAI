# Figure Analysis: OMICmAge quantifies biological age by integrating multi-omics with electronic medical records

Analysis of the six main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://doi.org/10.1038/s43587-026-01073-7) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13004675/) alongside this file.

## Fig. 1 — Study design

- **Argumentative role:** Establishes that this is three biomarkers in sequence, not one, and that discovery and validation live in different cohorts.
- **Panel logic:** Panel a is the workflow — EMRAge from MGB Biobank EMR data, then DNAmEMRAge and OMICmAge trained to predict it in MGB-ABC, then validation in All of Us, TruDiagnostic and Generation Scotland. Panel b describes the populations.
- **Reusable design:** Drawing the *target* of each model explicitly in the workflow is what makes the surrogate chain legible. A reader can see immediately that the molecular clocks are trained against a model output rather than against an outcome.
- **Boundary:** A design diagram shows what was done, not how large each step's sample was. The asymmetry matters here — 31,264 people define EMRAge, but only 689 sit in the test set for the methylation clocks.
- **Locator:** [Paper: Fig. 1a,b]

## Fig. 2 — EMRAge development and comparators

- **Argumentative role:** Justifies the target before anything is trained on it. If EMRAge is not a good clinical score, nothing downstream matters.
- **Panel logic:** Panel a is the robustness check — the algorithm retrained at four biennial time points and applied to a common 2016 cohort, yielding pairwise correlations of ~1. Panel b compares hazard ratios against PhenoAge and chronological age. Panel c is Kaplan–Meier separation. Panel d puts EMRAge and PhenoAge into the *same* model.
- **Reusable design:** Panel d is the right way to claim added value. Two forest plots side by side would only show that both scores work; putting both predictors in one model tests whether either survives the other.
- **Reusable design (second):** The caption lists incident and prevalent case counts per phenotype (mortality n = 496, stroke 443, T2D 339, COPD 217, depression 523, CVD 699, cancer 385). Publishing the numerators lets a reader calibrate every confidence interval in the panel.
- **Boundary:** Panel b is restricted to the subset where PhenoAge is available (N = 5,171), not the full test set. Panel a shows stability to *when* EMRAge is computed within one EMR system, which is a narrower claim than portability across systems.
- **Locator:** [Paper: Fig. 2a–d]

## Fig. 3 — Agreement and reproducibility

- **Argumentative role:** Quantifies how well each methylation clock reproduces EMRAge, and how reproducible each is technically.
- **Panel logic:** Panels a–c are DNAmEMRAge (train ρ 0.906, test ρ 0.913, ICC 0.995); d–f are OMICmAge (train ρ 0.911, test ρ 0.915, ICC 0.998). Laid out as two matched rows so the comparison is immediate.
- **Reusable design:** Pairing an agreement plot with a replicate-based ICC in the same figure separates two things that are routinely conflated — how close the estimate is to its target, and how stable the estimate is when you measure the same sample twice.
- **Boundary:** The correlations here are nearly identical between the two clocks (0.913 vs 0.915); the real difference is in mean absolute error (8.50 vs 4.97 years), which is in the text and *not* in the figure. Reading the panels alone would suggest the two clocks are equivalent.
- **Boundary (second):** Everything in this figure is agreement with EMRAge, which is itself an estimate. None of it is agreement with an observed outcome.
- **Locator:** [Paper: Fig. 3a–f]

## Fig. 4 — The EBP filtration

- **Argumentative role:** The methodological core. Shows how proteomic, metabolomic and clinical information is converted into methylation-computable features.
- **Panel logic:** Panel a is the schematic. **Panels b and c are the important ones**: histograms of feature-wise correlation to EMRAge for each modality, with the *unfiltered background in grey* and the retained subset overlaid in colour. Panel b applies the first filter (|ρ| > 0.1, P < 0.05: 2,098 proteins → 110, 286 metabolite clusters → 286, 46 clinical → 25). Panel c applies the second (EBP must correlate with its measured counterpart at ρ > 0.2: → 109, 266, 21; total 396).
- **Reusable design:** Plotting the retained features against the background distribution they were drawn from is exactly how a selection step should be reported. It makes the selectivity visible and lets a reader judge whether the threshold is doing real work or merely cutting a tail.
- **Boundary:** The second filter's bar is low — ρ > 0.2 is roughly 4% shared variance. The panel shows the distribution of candidates but not the fidelity of the **40 EBPs that actually survived into the final model**, which is the number that would matter for interpreting them biologically.
- **Locator:** [Paper: Fig. 4a–c]

## Fig. 5 — Comparison against established clocks

- **Argumentative role:** Positions the new clocks against PCHorvath, PCHannum, PCPhenoAge, PCGrimAge and DunedinPACE on features, disease association and survival.
- **Panel logic:** Panel a is an UpSet-style intersection of CpG sets — the striking result being that DNAmEMRAge and OMICmAge share 411 probes with each other but at most **3** with any prior clock, while PhenoAge and Horvath share 50 and Horvath and Hannum share 29. Panel b is the disease forest plot in the MGB-ABC test set. Panel c is 5- and 10-year survival ROC curves.
- **Reusable design:** Panel a answers "is this a new measurement or a reweighting of an old one?" with a set operation rather than a correlation, which is the cleaner test.
- **Boundary:** Panel b's caption gives test-set case counts that are small — 83 deaths, 45 strokes, 39 COPD cases — and the text says several differences between the strongest biomarkers fall within overlapping confidence intervals. Panel c is where DNAmEMRAge slightly **beats** OMICmAge on both 5-year (0.898 vs 0.892) and 10-year (0.890 vs 0.873) AUC, which is the inverse of the ordering in Fig. 3.
- **Locator:** [Paper: Fig. 5a–c]

## Fig. 6 — Lifestyle associations

- **Argumentative role:** Face validity. An aging biomarker should move with the things known to affect aging.
- **Panel logic:** Forest plot of effect sizes with 95% CIs across MGB-ABC and TruDiagnostic — negative with female sex, education and weekly exercise; positive with obesity and smoking, consistently in both cohorts.
- **Reusable design:** Replicating the same lifestyle panel in two cohorts with different ascertainment is a cheap and convincing consistency check.
- **Boundary:** These are cross-sectional associations, and the panel includes a race term with a consistent positive coefficient. Interpreting that as biological aging rather than as accumulated exposure and access is a choice the figure does not adjudicate.
- **Locator:** [Paper: Fig. 6]

## Extended Data

Extended Data Fig. 3 (EMRAge vs PhenoAge in All of Us), Fig. 5 (clock correlations with immune cell fractions), Fig. 6 (disease associations in Generation Scotland and TruDiagnostic, where chronological age and PCGrimAge frequently rank above OMICmAge) and Fig. 7 (Generation Scotland survival ROC) carry claims cited in the card but were not opened directly; they are referenced only as the main text describes them.

## Cross-figure reading rule

Read Fig. 4b,c first — the EBP filtration is the paper's actual invention, and the grey background distributions show how selective it is. Then Fig. 3 and Fig. 5c **together**: Fig. 3 shows OMICmAge reproducing EMRAge far better than DNAmEMRAge does, and Fig. 5c shows DNAmEMRAge slightly ahead on the mortality endpoint. That inversion is the most informative thing in the paper about what a surrogate target does and does not buy. Fig. 5a settles the novelty question in one panel. Fig. 2 justifies the target; Fig. 6 is face validity, not evidence.
