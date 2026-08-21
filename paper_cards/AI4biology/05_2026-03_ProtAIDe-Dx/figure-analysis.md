# Figure Analysis: A deep joint-learning proteomics model for diagnosis of six conditions associated with dementia

Analysis of the six main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41591-026-04303-y) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13190262/) alongside this file.

## Fig. 1 — Workflow and overall performance on GNPC

- **Argumentative role:** Sets up the whole paper: the pipeline (a), the headline accuracy (b), two biological sanity checks (c, d), and a transfer result (e).
- **Panel logic:** Panel b is six side-by-side task comparisons, not one score — and the spread across tasks (95% for ALS down to 70% for stroke/TIA) is more informative than the range quoted in the abstract. Panels c and d are the sanity checks that make the probabilities interpretable as continuous scores: AD probability tracks APOE ε4 dosage in the expected direction and correlates negatively with MMSE. Panel e uses the embedding, not the classifier, on a task the model was never trained for.
- **Reusable design:** Putting sanity checks in the same figure as the accuracy panel is good practice — it answers "is this signal or artefact?" before the reader has to ask.
- **Boundary:** Every number in panel b is cross-validated within GNPC. Fig. 4a is where that gets tested properly, and it is a different figure for a reason.
- **Locator:** [Paper: Fig. 1a–e]

## Fig. 2 — The diagnostic probability map

- **Argumentative role:** Turns six probabilities into a 2D space, then argues that where a patient falls in that space is clinically meaningful even when it disagrees with their chart.
- **Panel logic:** Panel a is the t-SNE coloured by clinical diagnosis. Panels b–d overlay phenotype (CDR, APOE, hypertension) and land where they should. Panel e places the ambiguous cases — SCD and MCI patients excluded from training — across the map. Panel f finds subclusters *within* each diagnosis, and g–i characterize them.
- **Reusable design:** The control against artefact is in Extended Data Fig. 1: the same embedding coloured by contributing site, showing patients cluster by diagnosis and not by site. A projection figure without that companion panel would prove nothing.
- **Boundary:** t-SNE geometry is not metric. Distances and cluster sizes on this map carry no quantitative meaning, and the subcluster claims in f–i rest on the differential-abundance analyses in Supplementary Data, not on the layout.
- **Locator:** [Paper: Fig. 2a–i; Extended Data Figs. 1, 2]

## Fig. 3 — Model interpretation

- **Argumentative role:** Two different interpretability claims stacked in one figure: which individual proteins drive predictions (a), and what the learned embeddings correspond to biologically (b, c).
- **Panel logic:** Panel a is permutation importance counted across cross-validation folds — a stability criterion, which is stronger than importance from a single fit. Panel b asks whether embedding-specific proteins are organ-enriched, and finds brain-specific proteins prevalent across all of them. Panel c pairs embedding importance with GO enrichment: Z1 reads as brain health/resilience, Z3 as AD, Z21 as ALS and PD, Z25 as vascular dysfunction.
- **Reusable design:** Counting importance by fold rather than averaging it makes the reader's question "would this protein appear again?" the thing being measured.
- **Boundary:** Permutation importance identifies what the model uses, not what causes disease. The ACHE result illustrates the gap directly — it is a top AD feature and also the target of the most commonly prescribed AD drug class.
- **Locator:** [Paper: Fig. 3a–c]

## Fig. 4 — External validation in BioFINDER-2

- **Argumentative role:** The honesty figure. Panel a is where cross-validated performance meets leave-one-site-out reality, and it drops for every model.
- **Panel logic:** Panel a spans 14 test sites and includes two recovery strategies (retraining on 100 participants' proteins; finetuning on 100 participants' embeddings) — the second works better, which is itself an argument for the embedding. Panel b applies the model to BioFINDER-2. Panels c and d are the strongest evidence in the paper: probabilities correlated against actual pathology biomarkers, within diagnostic groups.
- **Reusable design:** Panel d asks the question that separates a good biomarker model from a good chart-matching model — do the probabilities track pathology in people whose *clinical* label says nothing is wrong? For AD, Lewy body and neurovascular markers among cognitively unimpaired participants, they do.
- **Boundary:** The same panel contains the paper's cleanest negative result: PD probability shows no significant relationship with CSF α-synuclein SAA, and correlates instead with UPDRS symptom score. That is reported, not buried, and it bounds what the PD head can be claimed to measure.
- **Locator:** [Paper: Fig. 4a–d; Extended Data Figs. 4–6]

## Fig. 5 — Clinical utility

- **Argumentative role:** The only figure that answers "should a clinic use this?", and it answers "alongside, not instead".
- **Panel logic:** Panel a is a nested-model comparison — demographics alone, plus proteomics, plus accessible clinical markers, then everything — which isolates the *added* value rather than reporting standalone accuracy. Panel b shows baseline predicted diagnosis stratifying MMSE decline where baseline clinical diagnosis does not. Panels c and d convert probabilities into thresholds, with a two-cutoff scheme leaving an explicit indeterminate zone.
- **Reusable design:** The nested-model design in panel a is the right way to make an "adds value" claim: model 3 versus model 2 is the comparison that matters, and it is the one plotted. The two-cutoff scheme in panel d is honest in a second way — it refuses to classify the middle rather than forcing a call.
- **Boundary:** Cutoffs were fit on non-SCD participants and applied to SCD, which is a real holdout; but the α-synuclein PPV target was relaxed to 40% "owing to sample validity constraints", so that one column is not comparable to the others.
- **Locator:** [Paper: Fig. 5a–d]

## Fig. 6 — Individual risk report

- **Argumentative role:** A deployment mock-up. Shows what a clinician would actually receive: probabilities, position on the disease map, SHAP-based per-patient protein contributions, and linked health traits.
- **Panel logic:** Case A is a 75–80-year-old man with subjective complaints and intact cognition; the model predicts comorbid AD and Lewy body pathology; panel f reports the confirmation — amyloid-PET and tau-PET positive, CSF Aβ42/Aβ40 positive, CSF α-synuclein SAA positive. Notably p-tau217 was *not* positive in this case.
- **Reusable design:** Reporting per-patient feature attributions rather than global importance is what makes the output auditable at the point of care, which is the difference between a score and a report.
- **Boundary:** Three cases, selected. The main text says plainly that not all probabilities were accurate or biomarker-confirmed. This figure is a design proposal, not evidence.
- **Locator:** [Paper: Fig. 6a–f; Extended Data Figs. 8, 9]

## Cross-figure reading rule

Read Fig. 1b for what the model can do in-sample, then go straight to Fig. 4a, which is the same question asked honestly and gives a lower answer. Fig. 4d is the most load-bearing panel in the paper — probabilities against real pathology biomarkers, including the PD/α-synuclein null. Fig. 5a is the one a clinician should read: it is the only place the model is measured as an *addition* to existing workup rather than on its own. Figs. 2, 3 and 6 are interpretation and design; they explain and package the result rather than establishing it.
