# Figure Analysis: Antibiotic use and gut microbiome composition links from individual-level prescription data of 14,979 individuals

Analysis of the four main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41591-026-04284-y) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13099378/) alongside this file.

## Fig. 1 — Diversity by course count and by class

- **Argumentative role:** Establishes both a dose–response and a class ordering, which together are what distinguish this study from prior cohort work.
- **Panel logic:** Panels a and b give estimated marginal means per additional course in each of the three windows, across all three diversity metrics. The shape matters: the first two courses cost more diversity than the third and fourth, which is saturation and would be invisible under a linear model. Panel c is the class-by-window forest plot of meta-analysed coefficients, with filled symbols for FDR < 5%.
- **Reusable design:** Reporting three alpha-diversity metrics side by side throughout, rather than picking Shannon and moving on, means a reader can see whether a finding is metric-specific. Clindamycin's "−47 species detected" comes from richness specifically, and the caption makes that recoverable.
- **Boundary:** Panel c shows only antibiotics with at least one significant association. Classes with null results are in Supplementary Table 1, not here — so the figure cannot be used to judge how many classes were tested.
- **Locator:** [Paper: Fig. 1a–c]

## Fig. 2 — Functional regression over time

- **Argumentative role:** The recovery picture — diversity returning fastest in the first two years and slowly thereafter, with recovery rate proportional to the size of the initial drop.
- **Panel logic:** Continuous meta-analysed coefficients against time since the antibiotic course, with confidence bands, replacing the three discrete windows of Fig. 1c with a curve. Infrequently prescribed classes were merged into one predictor for model stability, which the caption states.
- **Reusable design:** Borrowing strength across temporally adjacent coefficients via a spline is the right move when the underlying process is smooth and each individual window is underpowered. It is also honest about what it assumes — smoothness.
- **Boundary:** This is the figure most likely to be misread. It looks like a recovery trajectory but is assembled from different people sampled once each, at different times since their exposure. Time-since-exposure is confounded with calendar year, age at exposure and changing prescribing practice. The authors point to SCAPIS repeat sampling as what would actually test this.
- **Locator:** [Paper: Fig. 2]

## Fig. 3 — Species-level associations

- **Argumentative role:** The paper's most informative figure, and the one carrying its mechanistic evidence.
- **Panel logic:** Rows are the 11 classes × 3 windows; columns are 1,340 species **ordered by taxonomy**, with phyla labelled along the bottom and orders shown within Bacillota A. Blue and red bars mark negative and positive coefficients; only FDR < 5% associations are drawn. Each row also carries the proportion of participants exposed in that window.
- **Reusable design:** Ordering species taxonomically rather than by effect size is what converts a significance plot into a mechanism plot. Because the columns are phylogenetically arranged, flucloxacillin's hits visibly concentrate in Gram-positive Bacillota A while fluoroquinolone and clindamycin hits spread across Bacteroidota and Actinomycetota — the pattern each drug's spectrum predicts. A sorted-by-p-value version of this figure would show none of that.
- **Reusable design (second):** Printing the proportion of users beside each row lets the reader discount for power without leaving the figure. Penicillin V has the most users and among the fewest associations, which is the comparison that makes the class ordering credible.
- **Boundary:** Bar presence encodes significance, not magnitude, so a wall of blue is a count of detections and not a measure of disruption. Positive associations are real and substantial — clindamycin at 1–4 years raised 141 species while lowering 208 — so this is restructuring, not simple depletion.
- **Locator:** [Paper: Fig. 3]

## Fig. 4 — Species and cardiometabolic markers

- **Argumentative role:** Answers "why should anyone care", by connecting the 101 species associated with all three high-impact antibiotics to BMI, waist–hip ratio, triglycerides and CRP in SCAPIS.
- **Panel logic:** A two-block heatmap — antibiotic–species regression coefficients on one side, partial Spearman correlations between species and cardiometabolic markers on the other, with species ordered by hierarchical clustering of the antibiotic associations. The visual claim is alignment between the blocks: species that go up with antibiotics (*Sellimonas intestinalis*, *R. gnavus*, *E. clostridioformis*, *E. aldenensis*, *T. ramosa*) also go up with adiposity and inflammation, while species that go down (*Alistipes communis*, *Odoribacter splanchnicus*) go the other way.
- **Reusable design:** Clustering the rows by one association block and then displaying the second block against that fixed ordering is a fair way to show correspondence — the ordering is not chosen to flatter the second block.
- **Boundary:** Both blocks are cross-sectional and share a single time point. Two aligned associations do not make a chain, and this figure does not show that antibiotic use leads to cardiometabolic change. The species involved are also the ones most often reported in obesity-microbiome literature, so some of the alignment is prior expectation being confirmed rather than independently discovered.
- **Locator:** [Paper: Fig. 4]

## Extended Data

Extended Data Fig. 1 (participant exclusion flow), Fig. 2 (the negative control exposure), Figs. 3 and 4 (the single-course analysis, which is arguably the paper's primary evidence) and Fig. 5 (species previously linked to colorectal cancer and IBD) carry claims cited in the card but were not opened directly; they are referenced only as the main text describes them.

## Cross-figure reading rule

Fig. 3 first — the taxonomic ordering of its columns is where the pharmacological coherence lives, and that coherence is the strongest argument against pure confounding. Then Fig. 1c for the diversity ordering by class and window. Extended Data Figs. 2 and 3 matter more than their placement suggests: the negative control and the single-course contrast are the two design features that make the long-window claims credible, and neither is in a main figure. Fig. 2 should be read as a description, not a measurement. Fig. 4 is motivation, and should be read as two cross-sectional association sets that happen to align rather than as a causal chain.
