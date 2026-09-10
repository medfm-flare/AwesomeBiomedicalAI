# Figure Analysis: Predictive biomarkers of response to CAR T-cell therapy for pan-haematologic cancer

Analysis of the four main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41551-026-01633-7) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13435093/) alongside this file.

## Fig. 1 — The data resource, and the two crudest predictors

- **Argumentative role:** Establishes the resource before any claim depends on it, then tests the two simplest hypotheses — does the manufactured product expand, and does it expand in the patient.
- **Panel logic:** Panels a–d are cohort description (framework, 256 patients across 13 trials and 5 cancers, response distribution, age by cancer type). Panel e is post-infusion CAR qPCR by outcome, peaking at 1–3 weeks. Panel f is the manufacturing signal, Days 3–9.
- **Reusable design:** Panel f prints every FDR-adjusted p-value in the caption rather than only asterisks — 0.24, 0.10, 0.10, 0.048, 0.048, 0.10, 0.14. A reader can see immediately that only two of seven days clear 0.05, and only just.
- **Boundary:** Panel e is measured after infusion, so it is a correlate of response and cannot inform the decision to treat. Panel f's signal is weak in effect size; the Discussion says so.
- **Locator:** [Paper: Fig. 1a–f; Extended Data Fig. 1]

## Fig. 2 — Apheresis T-cell phenotype

- **Argumentative role:** The pre-infusion result that matters, because apheresis material is available before any decision is made.
- **Panel logic:** Panel a is the UMAP of 1,062,975 CD3+ cells from 179 patients across 11 IC-panel markers; b colours it by FlowSOM cluster; c contrasts the density of Favorable and Non-favorable patients on the same embedding. **Panel d is the methodological control** — FlowSOM nClus swept 3→30, ten repeats each, with downstream out-of-bag AUROC on the y axis. Panel e is the annotated cluster heatmap ranked by Gini importance with univariate direction overlaid.
- **Reusable design:** Panel d answers "did you tune the clustering until the answer appeared?" before anyone asks. Sweeping the free parameter and plotting downstream performance is the right shape for that control, and it belongs in the main figure exactly where it is.
- **Boundary:** UMAP density contours in panel c are qualitative. The quantitative claims come from cluster proportions in panel e, and cluster proportions are compositional — they sum to one per patient, which the importance ranking does not account for.
- **Locator:** [Paper: Fig. 2a–e; Extended Data Figs. 2, 3]

## Fig. 3 — Cytokine dynamics

- **Argumentative role:** Shows that cytokine association with outcome is not a fixed property of a cytokine but a function of *when* it is measured.
- **Panel logic:** Panel a is the whole story compressed — cytokines as rows, time bins as columns, colour as direction of association. Panels b and c are volcano plots at two specific windows. Panels d–f are LOESS time courses for IL-2, IFN-γ and IL-6, the three favorable-direction cytokines, showing IL-2 peaking before one week and IFN-γ and IL-6 around Day +7.
- **Reusable design:** Making time an explicit axis in panel a, rather than reporting one association per cytokine, is what surfaces the sign structure: early IL-2/IFN-γ/IL-6 are good, sustained IL-2R/CXCL9/CXCL10/IL-10 are bad, and some of the same inflammatory axis appears in both directions at different times.
- **Boundary:** These are univariate logistic regressions with FDR correction, not a predictive model. Panel a is the inferential arm; the classifier in Fig. 4 is a separate analysis on an overlapping patient set.
- **Locator:** [Paper: Fig. 3a–f; Extended Data Fig. 4]

## Fig. 4 — Benchmarking and validation

- **Argumentative role:** The paper's evidentiary core, and the figure to read first if reading only one.
- **Panel logic:** Panel a is the pre-infusion ladder — manufacturing 0.55, clinical 0.60, cytokines 0.71, flow 0.76, combined 0.77. Panel b is the post-infusion ladder — qPCR 0.80, cytokines 0.83, combined 0.85. Panel c compares six learners on all features (RF 0.875 through naive Bayes 0.687). Panel e is the validation design; f shows the hold-out spans all 5 cancers and 10 trials; g and h give the hold-out result, AUROC 0.74 with p = 3.7 × 10⁻³.
- **Reusable design:** Separating panels a and b is the single best decision in the paper. It makes visible that the impressive integrated number depends on measurements taken after the patient has already been treated, and it lets a reader take away the honest pre-infusion ceiling of 0.77.
- **Boundary:** Panel c is 10-fold cross-validated on the same 141 patients used to choose among six algorithms; panel g is the number that estimates prospective performance, and it is lower. The hold-out is genuinely independent in time and batch, but not in institution, trial portfolio or manufacturing process.
- **Locator:** [Paper: Fig. 4a–h; Extended Data Figs. 5, 6]

## Extended Data

Extended Data Fig. 5b,c carries the per-cancer breakdown that qualifies the pan-cancer claim (leave-one-cancer-type-out AUROC 0.69 NHL, 0.76 MM, 0.89 B-ALL, 0.95 CLL; AML not estimable), and Extended Data Fig. 6d–i carries the mRMR feature-reduction result. Both are cited in the card but were not opened directly; they are referenced only as the main text describes them.

## Cross-figure reading rule

Read Fig. 4a and 4b together before anything else — they locate where the predictive signal lives in time, and they set the correct expectation for the headline in 4c. Then Fig. 4g, which is the only prospective number. Fig. 2d is the methodological control that makes Fig. 2e believable. Fig. 3a is the most informative single panel in the inferential arm because it makes the direction of cytokine association a function of time rather than a fixed label. Fig. 1 is the resource; its two result panels are the weakest evidence in the paper and the caption's printed p-values say so.
