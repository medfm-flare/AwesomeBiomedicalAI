# Figure Analysis: An atlas of exposome–phenome associations in health and disease risk

Analysis of the five main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41591-026-04266-0) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13099396/) alongside this file.

## Fig. 1 — Schematic of the P-ExWAS

- **Argumentative role:** Declares the scope before any result: 305 phenotypes on one side, 619 exposures on the other, harmonized across NHANES 1999–2018, with the outputs named — exposome globes, the atlas, and a database plus software.
- **Panel logic:** Deliberately symmetric. Putting phenotype and exposure catalogues on equal footing is the argument in miniature: neither side is the candidate hypothesis, both are enumerated.
- **Reusable design:** A scope figure that lists the *deliverables* (atlas, globes, tooling) rather than only the method tells a reader what they can reuse. That is the right first figure for a resource paper.
- **Boundary:** A scope diagram claims coverage, not validity. The 619 exposures are what NHANES measured, which is a convenience sample of the exposome, not a designed one.
- **Locator:** [Paper: Fig. 1; Extended Data Fig. 1]

## Fig. 2 — Associational architecture

- **Argumentative role:** The denominator figure. Shows the full distribution of 123,774 tests, of which 5% clear Bonferroni and 12% clear FDR.
- **Panel logic:** Panel a plots two-sided log₁₀(P) against exposure type, colour-coded by threshold, **uncorrected** — so the reader sees the raw mass of null results before any filtering. Panels b and c count significant pairs per phenotype category and per exposome category, printing the total tests above each bar so the rate, not just the count, is legible.
- **Reusable design:** Printing the denominator above every bar is the single most useful choice in this figure. A bar chart of hit counts without test counts would make smoking look important because it was measured often.
- **Boundary:** Counting significant associations rewards categories with many measured variables. Panel c's "smoking ~15%, dietary biomarkers ~13%" are rates, which corrects for that; the raw counts do not.
- **Locator:** [Paper: Fig. 2a–c]

## Fig. 3 — Variance explained

- **Argumentative role:** Converts significance into consequence. This is where the paper says, in effect, that almost none of these associations matter individually.
- **Panel logic:** Panels a–c give R² distributions by exposure and phenotype category with medians annotated (single-exposure median 0.14%; 0.6% among Bonferroni-significant). **Panel d is the key panel**: exposure R² on the y axis against demographics-only R² on the x axis, with red points showing what up to ten or twenty simultaneous exposures achieve. Triglycerides sits at 43%, the maximum.
- **Reusable design:** Plotting the effect of interest against the effect of the covariates you already have is the honest way to present incremental value. It makes "demographics explain 0–80%, exposures add a median 0.14%" visible in one glance rather than buried in a table.
- **Boundary:** The exposures in the aggregate models were selected for significance in this same dataset, so the red points are in-sample. Nothing in this figure is cross-validated.
- **Locator:** [Paper: Fig. 3a–d]

## Fig. 4 — The Phenome–Exposome Atlas

- **Argumentative role:** The deliverable. 305 phenotypes as columns, 625 exposures as rows, each cell an adjusted β.
- **Panel logic:** One matrix, no thresholding — and crucially, **grey shading marks cells that could not be estimated** because of pairwise missingness or n < 500.
- **Reusable design:** Rendering "not estimable" as its own visual state, distinct from "zero", is what keeps a matrix like this from being read as a complete map. Most heatmaps of this kind silently colour missingness as null.
- **Boundary:** Every cell is from the single "main" adjustment specification. Extended Data Fig. 3 shows 15% of significant cells would flip sign under a different one, and that instability is not visible in this figure.
- **Locator:** [Paper: Fig. 4]

## Fig. 5 — Exposome globes

- **Argumentative role:** Argues that attribution is unsafe. If exposures travel in correlated bundles, a significant association names a bundle, not a cause.
- **Panel logic:** Panel a is 50 randomly sampled correlations as a reference; panel b is the sub-network of exposures associated with BMI or HbA1c; panel c is the correlation distribution with the random subset in grey, the BMI/HbA1c subset in blue and Bonferroni-significant correlations in black. The blue curve sitting right of the grey is the finding: phenotype-associated exposures are *more* correlated with each other than exposures in general.
- **Reusable design:** Including the random-sample baseline in the same panel as the subset of interest is what turns a network picture into a claim. Without the grey curve, panel b would be decorative.
- **Boundary:** Edges are drawn only above |r| > 0.25 — the top 15% of the distribution — so the globes are a thresholded view. The median exposure–exposure correlation is 0.05, and the picture would look sparse without the threshold.
- **Locator:** [Paper: Fig. 5a–c]

## Extended Data

Extended Data Fig. 3 (adjustment sensitivity, including the 15% sign-flip result and the cadmium–BMI example), Fig. 4 (self-report vs biomarker concordance), Fig. 6 (age × exposome interactions, largely null) and Fig. 8 (exposomic vs genomic R² across 29 phenotypes) carry claims cited in the card but were not opened directly; they are referenced only as the main text describes them.

## Cross-figure reading rule

Read Fig. 2a for the denominator, then Fig. 3d for what the survivors are worth — those two panels together are the paper's actual message, and it is a deflationary one about individual exposures. Fig. 5c is the reason the surviving associations cannot be read causally. Fig. 4 is the deliverable but should be consulted with Extended Data Fig. 3 open beside it, because the atlas shows one specification out of nine and 15% of its significant cells change sign in another.
