# Figure Analysis: AI-enabled virtual spatial proteomics from histopathology for interpretable biomarker discovery in lung cancer

Analysis of the six main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41591-025-04060-4) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12823406/) alongside this file.

The single most important thing the figure titles tell you, and the abstract does
not: **Figs. 2 and 3 are HEX figures; Figs. 4, 5 and 6 are MICA figures.** Every
prognosis and immunotherapy number in this paper is titled for MICA, the
multimodal co-attention model that consumes HEX's output. Read the titles before
the panels.

## Fig. 1 — Development, validation and clinical applications of HEX

- **Argumentative role:** Orientation and scope. Panel a is the technical pipeline (ten NSCLC patients, 40-antibody panel, >755,000 matched tiles, validation on 372 co-stained samples, external validation on 206 pan-cancer cores across 34 tissue types); panel b is the clinical programme (five prognosis cohorts, 2,150 patients; 5,019 TCGA patients across 12 further cancer types; 148 ICI-treated patients).
- **Panel logic:** The split between a and b is the paper's real structure — a is what HEX is, b is what MICA does with it. Panel b is also where the multimodal integration method is first named, which is why the later clinical figures are titled for MICA rather than HEX.
- **Reusable design:** Putting the training-data provenance (ten patients, one panel, same-section staining) in the same panel as the validation breadth (34 tissue types) lets a reader see the asymmetry immediately rather than reconstructing it from Methods.
- **Boundary:** A scope diagram is a claim about coverage, not accuracy. Specifically, panel a's "over 755,000 image tiles" is a tile count, not a sample count — the biological *n* for training is **ten patients at one hospital**, and nothing in this figure tests whether ten is enough.
- **Locator:** [Paper: Fig. 1a,b]

## Fig. 2 — Cross-validation performance of HEX for protein prediction

- **Argumentative role:** The core technical claim: 40 proteins predicted from H&E at mean Pearson *r* 0.790, Spearman 0.787, SSIM 0.949, MSE 0.076, with a 46% Pearson margin over the best GAN baseline.
- **Panel logic:** Panel a is per-marker accuracy across all 40 biomarkers; panel b is the head-to-head against DeepLIIF (conditional GAN) and Virtual Multiplexer (contrastive unpaired translation); panel c is the qualitative virtual-CODEX gallery at both 224- and 14-pixel patch sizes. The caption states plainly that bars in a and b are means across fivefold cross-validation **on n = 10 WSIs**, with dots for individual folds — the error bars are fold-to-fold variation over ten slides, not patient-to-patient variation over a population.
- **Reusable design:** Four complementary metrics (linear correlation, rank correlation, perceptual structure, absolute error) rather than one. SSIM catches spatial-pattern fidelity that Pearson over tile means would miss.
- **Boundary:** This figure establishes nothing about generalization — the folds are patient splits of the same ten-patient, single-institution, single-scanner dataset. It also does not establish superiority over regression baselines: the only comparators are two stain-translation GANs, and no MUSK-linear-probe or MUSK-MLP-without-FDS/ALF control appears. And the 14-pixel images in panel c come from a **separate model retrained on 1/20 of the data**, whose accuracy is never quantified anywhere in the paper.
- **Locator:** [Paper: Fig. 2a–c]

## Fig. 3 — Independent validation of HEX on 372 TMA cores

- **Argumentative role:** Transfer off the training slides. Stanford-TMA (n = 264 cores) and TA-TMA (n = 108 cores), with bootstrap CIs from 1,000 resamples rather than fold means.
- **Panel logic:** Same three-panel structure as Fig. 2, deliberately, so the two can be read side by side. Panel b reports the headline contrast: Pearson 0.738 versus CGAN 0.370, Spearman 0.741 versus 0.382, SSIM 0.875 versus 0.463, MSE 0.189 versus 0.782.
- **Reusable design:** Repeating the figure template between the cross-validation and independent-validation settings makes the degradation visible at a glance instead of requiring the reader to hold two numbers in their head.
- **Boundary:** The honest reading of Figs. 2 and 3 together is that accuracy **falls from 0.790 to 0.738** moving off the training slides, and that the CGAN baseline collapses far more (0.370) than HEX does — so the widening margin is partly a story about baseline fragility, not only about HEX robustness. Neither figure touches a different institution, scanner or tissue type; that is Extended Data Fig. 5's job. Panel c's visualizations again use the unquantified 14-pixel variant.
- **Locator:** [Paper: Fig. 3a–c]

## Fig. 4 — MICA improves prognosis prediction in early-stage NSCLC

- **Argumentative role:** The prognosis headline, and the paper's best-designed experiment: trained on NLST, tested on four untouched cohorts, with **all risk cutoffs fixed on the training cohort** before validation.
- **Panel logic:** Panel a is Kaplan–Meier stratification in stage I and stage II separately (HR 2.43–3.33, all *P* ≤ 0.002 for stage I; 2.27–4.28, all *P* ≤ 0.012 for stage II). Panel b is the C-index comparison that contains the number most worth reading — MICA 0.68 overall adjusted, against **H&E-only 0.56** and **virtual-CODEX-only 0.59**. Panel c is MICA against clinicopathological variables, the source of the "22%" claim (0.71 versus 0.58). Panel d is multivariable Cox across five cohorts with stated *n* per cohort (NLST 336, TCGA-LUNG 746, PLCO-LUNG 364, Stanford-TMA 187, TA-TMA 94) and explicitly **unadjusted** *P* values.
- **Reusable design:** Fixing the cutoff on the training cohort and reusing it unchanged across all four validation cohorts is the design choice that makes panel a credible. Most prognostic-model papers re-optimize per cohort; this one does not, and says so in the caption.
- **Boundary:** Panel b does not establish that the predicted proteins carry the signal — the virtual-CODEX-only model reaches 0.59, barely above the H&E-only 0.56, and no *P* value is reported for the MICA-versus-CODEX-only comparison in the main text. Panel c's 22% is a *relative* gain between two modest absolute C-indices. NLST's 0.80 is a training-cohort number and belongs to a different regime than the four validation values (0.67, 0.68, 0.72, 0.62). Nothing here is prospective, and panel d's *P* values are not corrected for multiplicity.
- **Locator:** [Paper: Fig. 4a–d]

## Fig. 5 — Biological interpretation of MICA risk via HEX virtual proteomics

- **Argumentative role:** Converts a risk score into biology, and is the strongest support for the "interpretable biomarker discovery" in the title.
- **Panel logic:** Panel a is paired H&E and virtual CODEX for one high-risk and one low-risk patient. Panel b is the integrated-gradient histogram that defines the risk groups. Panel c compares marker distributions between groups over **26,519 high-risk and 26,416 low-risk patches** — the top and bottom 1% of tiles by attribution — with Mann–Whitney tests. Panel d is co-expression fractions for three marker pairs (CD3e⁺/PanCK⁺, Ki-67⁺/PanCK⁺, CD44⁺/EpCAM⁺) by chi-squared. Panel e converts those into patient-level survival: HR 0.58, 1.64 and 1.56 respectively, log-rank, explicitly **with no multiple-comparison adjustment**.
- **Reusable design:** The chain b → c → d → e is the transferable structure: attribution defines groups, groups define marker contrasts, marker contrasts define a *patient-level* count, and the count is tested against survival. Each step converts a model-internal quantity into something a pathologist could in principle count on a slide.
- **Boundary:** These are extreme-tail contrasts — the top and bottom **1%** of tiles — and "high expression" is defined at the 80th percentile; no sensitivity to either threshold is shown. Panel c's *P* values come from tens of thousands of patches within a handful of patients, so they measure patch-level separation, not patient-level effect. The panel e HRs are NLST-internal, in the cohort MICA was trained on. Crucially, nothing in Fig. 5 shows the biology is not an artefact of HEX's predictions — that is Extended Data Fig. 10's job, and it is the more important figure of the pair.
- **Locator:** [Paper: Fig. 5a–e]

## Fig. 6 — MICA for immunotherapy response and spatial proteomic signatures

- **Argumentative role:** The most clinically consequential figure and the weakest design. Objective response AUC 0.82 (0.73–0.90) against H&E-only 0.72 and virtual-CODEX-only 0.75; PD-L1 0.66 (0.54–0.77) and TMB 0.59 (0.37–0.80). PFS C-index 0.72 (0.65–0.76); multivariable HR 1.67 (1.36–2.05); KM HR 3.11 (2.11–4.57) with median PFS 4.4 versus 15.1 months.
- **Panel logic:** Panels a and b are the model comparisons with ROC and forest plots. Panel c stratifies PFS within PD-L1 tumour-proportion-score bands (0, 1–49%, ≥50%), which is what licenses the Discussion's treatment-selection arguments. Panel d gives the six pre-specified dual-marker cell states; panel e the normalized Jaccard co-localization indices; panel f the paired H&E/virtual-CODEX examples.
- **Reusable design:** Panel e is the genuine conceptual contribution — moving from marker *abundance* to marker-pair *co-localization*. It is backed by a stated negative control elsewhere in the text: single biomarkers did not stratify PFS at all, so the spatial pairing is doing the work rather than merely re-expressing expression level.
- **Boundary:** Everything in this figure comes from **fivefold cross-validation inside a single 148-patient Stanford cohort**. There is no external immunotherapy validation anywhere in the paper. The cutoff in panel c is the median, chosen in the same data. The TMB comparator's CI (0.37–0.80) includes 0.5, so the upper end of the abstract's "24–39%" range is measured against a comparator that does not beat chance here. The six marker pairs in panel d were selected from prior literature, not discovered — this figure confirms known immunobiology, it does not find it — and their *P* values are nominal and uncorrected by the authors' stated design.
- **Locator:** [Paper: Fig. 6a–f]

## Extended Data

There are ten Extended Data figures and several carry claims the main text leans on. Their **captions were read in full**; the underlying panels and their per-marker values were not opened. Extended Data Fig. 1 is the HEX architecture schematic (MUSK backbone, three-layer head via 256- and 128-dimensional representations, FDS with exponential moving average, ALF). Extended Data Fig. 2 is the inclusion/exclusion flow chart for the six clinical cohorts and is the only place the per-cohort attrition is documented. Extended Data Fig. 3 extends the Fig. 2c gallery. Extended Data Fig. 4 stratifies accuracy by subcellular localization (nuclear, cytoplasmic, membrane) and reports comparable accuracy across the three. Extended Data Fig. 5 is the **Bern external validation** — 24 overlapping markers across 206 cores, mean Pearson 0.658 without fine-tuning against 0.718 on the Stanford data restricted to the same markers, plus a direct Leica-AT2-versus-Keyence-BZ-X710 scanner comparison; this is the paper's only cross-institution, cross-protocol, cross-scanner evidence and it covers 24 of the 40 markers. Extended Data Figs. 6 and 7 are the **colorectal retraining and fine-tuning** experiments on 140 CRC cores, 57 markers, 33 of them novel: retrained from scratch reaches mean Pearson 0.566, fine-tuned from the NSCLC model reaches 0.659 — fine-tuning wins, and the gap is the clearest evidence that the NSCLC training transfers. Extended Data Fig. 8 splits that comparison into 24 legacy and 33 novel markers. Extended Data Fig. 9 is the **orthogonal IHC validation** on three lung samples from the ANHIR dataset, Pearson 0.479 (CD31) and 0.606 (Ki-67) — the only check against an assay outside the CODEX family, and by some distance the smallest experiment supporting the paper's central technical claim. Extended Data Fig. 10 repeats the Fig. 5d co-expression survival analysis in Stanford-TMA using **measured** CODEX rather than HEX predictions, and is the figure that separates "the model found real biology" from "the model found its own artefacts"; it too is log-rank with no multiple-comparison adjustment.

## Cross-figure reading rule

Read the figure titles first: 2 and 3 are HEX, 4 through 6 are MICA, and the whole HEX-versus-MICA attribution problem resolves itself in one pass. Then read Fig. 4b before Fig. 4c — the virtual-CODEX-only C-index of 0.59 tells you what the predicted proteins contribute on their own, and the 22% headline in 4c is a fusion result that cannot be read back onto HEX. Fig. 3 next to Fig. 2 gives the degradation off the training slides (0.790 → 0.738), and Extended Data Fig. 5 continues that curve to a different institution (0.658) while Extended Data Fig. 9 continues it to a different assay family (0.479–0.606, n = 3). Fig. 6 is where the clinical stakes are highest and the design is weakest — internal cross-validation in one cohort — so read its confidence intervals, particularly TMB's. Finish on Extended Data Fig. 10, the quiet figure that does the most work: it is where the co-expression biology is checked against measured CODEX instead of predicted CODEX.
