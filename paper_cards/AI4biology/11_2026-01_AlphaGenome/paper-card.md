# Paper Card: Advancing regulatory variant effect prediction with AlphaGenome

> Source coverage: Open-access full text via PubMed Central (PMC12851941), including Main, all named result sections, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; Methods are only a stub in the deposited text, and Supplementary Tables, Supplementary Figures and Extended Data are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code
>
> Card completeness: Complete for the main text; Supplementary Tables 1–4 (track metadata and full benchmark results), Supplementary Figs. 1–12 and Extended Data Figs. 1–9 were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| genome track | a per-base functional measurement along the genome (RNA-seq coverage, ATAC signal, a histone mark) | The prediction target; 5,930 human + 1,128 mouse |
| fold-specific model | trained on 3/4 of the reference genome, evaluated on the held-out quarter | Used for **track** evaluations |
| all-fold model | trained on all reference-genome intervals | Never evaluated directly; used only as a distillation teacher |
| student / distilled model | a single model trained to imitate an ensemble of all-fold teachers | Used for **variant effect** evaluations |
| QTL | quantitative trait locus — eQTL (expression), sQTL (splicing), caQTL/dsQTL (accessibility), paQTL (polyadenylation), bQTL (TF binding) | The main variant-effect benchmark family |
| sign prediction | getting the *direction* of a variant's effect right | Reported separately from magnitude and from causality |
| ISM | in silico mutagenesis — systematically mutating each base and reading the change | The interpretability tool used at the TAL1 locus |
| PSI5 / PSI3 | percent-spliced-in at 5′ and 3′ splice sites | Quantitative splicing metrics |

## 01 Basic Information

- **Title:** Advancing regulatory variant effect prediction with AlphaGenome
- **Authors:** Žiga Avsec, … , Pushmeet Kohli (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature*, 2026-01. [Paper: Metadata]
- **DOI:** [10.1038/s41586-025-10014-0](https://doi.org/10.1038/s41586-025-10014-0)
- **Code:** [google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome), plus a hosted model and API. [Paper: Discussion]
- **Scale:** 1-Mb input sequence; **5,930 human and 1,128 mouse tracks** across **11 modalities**; base-pair-resolution training made possible by sequence parallelism across **eight TPU v3 devices**; the distilled student runs in **under 1 s on an NVIDIA H100** per variant. [Paper: "Unifying DNA sequence-to-function model"]
- **Access boundary:** the open-access full text was read via PMC, where the Methods section is a stub. Supplementary Tables 1–4, Supplementary Figs. 1–12 and Extended Data Figs. 1–9 were not opened directly.

## 02 One-Sentence Summary

[Paper] AlphaGenome takes 1 Mb of DNA and predicts thousands of functional genomic tracks at up to single-base resolution across eleven modalities at once — expression, transcription initiation, splicing (including junctions), accessibility, histone marks, TF binding and contact maps — matching or beating the strongest specialized model on **25 of 26** variant-effect benchmarks and **22 of 24** track benchmarks, and scoring a variant across every modality in a single inference pass. [Paper: Abstract; "Performance overview"]

## 03 Research Question

- [Paper] Existing sequence-to-function models trade input length against prediction resolution, which limits both the modalities they can cover and their accuracy. Can one model have both — megabase context *and* base-pair resolution — across all the modalities at once? [Paper: Abstract]
- [Analysis] The scientific payoff of resolving that trade-off is not a better score on any one task; it is that a single variant can be scored across every modality simultaneously, which is what makes a *mechanistic* reading of a non-coding variant possible rather than just a ranking.

## 04 Research Background and Development Path

1. [Paper] Deep models predicting functional genomics from sequence are the leading tools for reading the regulatory code. [Paper: Abstract]
2. [Paper] Every existing method trades sequence length against resolution, so each covers a limited modality scope. [Paper: Abstract]
3. [Paper] 1 Mb is chosen deliberately: 99% (465 of 471) of validated enhancer–gene pairs fall within that distance. [Paper: "Unifying DNA sequence-to-function model"]
4. [Paper] The field has split into multimodal models with coarse resolution (Enformer, Borzoi) and specialists at fine resolution on one modality (SpliceAI, Pangolin, ChromBPNet, ProCapNet, Orca). [Paper: "Performance overview"]
5. [Analysis] The development path is engineering-led — sequence parallelism across eight TPUs is what makes base-pair training over 1 Mb affordable at all. The architecture is a U-Net with transformers in the middle, which is conventional; the enabling move is the training system.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Length–resolution trade-off | Long-context models are coarse; fine-resolution models are short-context | Memory cost of base-pair targets over megabases | [Paper: Abstract] |
| Narrow modality scope | A separate model per assay | Each was built for one task | [Paper: "Performance overview"] |
| Splice junctions unmodelled | Prior splicing models score sites, not junction usage | Junctions require modelling donor–acceptor pairs, not positions | [Paper: "Unifying DNA sequence-to-function model"; Discussion] |
| Ensembling cost | High accuracy required running several models per variant | Independent models must each be evaluated | [Paper: "Unifying DNA sequence-to-function model"] |
| Fragmented mechanism | A variant's expression, accessibility and splicing effects come from different tools | No shared representation | [Paper: Discussion] |

## 06 Core Idea

- **Surface method:** a U-Net backbone with a central transformer tower, predicting 1-D embeddings (1 bp and 128 bp) for tracks and 2-D embeddings (2,048 bp) for contact maps.
- **Core insight:** the two-stage training split does two different jobs. Fold-specific models exist to prove **generalization** to unseen genome intervals; all-fold models exist only to be **teachers**, and a single distilled student inherits their ensemble accuracy at one model's inference cost. Crucially, distillation uses *randomly mutated* input sequences — removing that perturbation costs measurable accuracy on every QTL task. [Paper: "Unifying DNA sequence-to-function model"; Fig. 7c]
- **General lesson:** [Analysis] a model can be evaluated in one regime and deployed in another, provided the paper says which numbers come from which. This one does, consistently: track results are fold-specific, variant results are the student. The distillation-with-mutation detail is the interesting part — the student is taught not just the teacher's answers but the teacher's *local sensitivity*, which is exactly what variant effect prediction needs.

## 07 Method Overview

**Architecture.** 1 Mb DNA → U-Net-inspired encoder → transformer tower → decoder. Convolutions capture local sequence patterns for fine-grained prediction; transformers capture long-range dependencies such as enhancer–promoter interactions. Outputs are linear transformations of the embeddings, with one exception: **splice junction counts** use a separate mechanism modelling interactions between the 1-D embeddings of donor–acceptor pairs. [Paper: "Unifying DNA sequence-to-function model"; Extended Data Fig. 1]

**Two-stage training.**
1. *Pretraining* on observed experimental data, producing (a) **fold-specific** models under 4-fold cross-validation over the reference genome, used for track evaluation, and (b) **all-fold** models trained on everything, used only as teachers.
2. *Distillation* — one student trained to reproduce an ensemble of all-fold teachers on **randomly augmented (mutated) input sequences**. The student is what performs variant effect prediction. [Paper: Fig. 1b,c]

**Evaluation.** 24 track evaluations across all 11 modalities against the strongest external model per task; 26 variant-effect benchmarks spanning expression, splicing, polyadenylation, enhancer–gene linking, accessibility and TF binding. [Paper: "Performance overview"]

**Main workflow figure:** Fig. 1a–c. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| U-Net encoder–decoder | Multi-scale representation | Needs both 1-bp detail and megabase context | 1 Mb sequence → 1-bp and 128-bp embeddings | [Paper: Fig. 1a; Extended Data Fig. 1a] | Not ablated as an architecture |
| Transformer tower | Long-range dependencies | Enhancer–promoter interactions span >100 kb | Embeddings → contextualized embeddings | [Paper: "Unifying DNA sequence-to-function model"] | Sequence length ablated instead (Fig. 7b) |
| 2-D embeddings at 2,048 bp | Pairwise genomic interactions | Contact maps are inherently pairwise | Sequence → contact map | [Paper: Fig. 1a] | Beats Orca: +6.3% Pearson, +42.3% on cell-type differences |
| Splice junction head | Models donor–acceptor pair interactions | Junction usage is not a per-position quantity | Paired 1-D embeddings → junction counts | [Paper: Extended Data Fig. 1] | **New capability**; the junction scorer alone beats prior methods on all but two benchmarks |
| Sequence parallelism, 8× TPU v3 | Makes 1-bp targets over 1 Mb trainable | Memory, not compute, is the binding constraint | — | [Paper: "Unifying DNA sequence-to-function model"] | The enabling engineering step |
| Fold-specific training | Demonstrates generalization to unseen intervals | Track predictions must hold off-fold | 3/4 genome → 1/4 held out | [Paper: Fig. 1b] | Used for all 24 track evaluations |
| Distillation with input mutation | Single-model accuracy at ensemble level | Ensembles are expensive per variant | Teacher ensemble → one student | [Paper: Fig. 7c] | **Ablated**: without mutation, eQTL sign −0.06, splicing outlier −0.015, eQTL/sQTL causality −0.01 |
| Multimodal training | Shared representation across 11 modalities | Modalities inform one another | All assays → one model | [Paper: Fig. 7d] | **Ablated**: helps eQTLs; accessibility variants do fine on accessibility data alone |
| 1-bp target resolution | Fine-scale accuracy | Splicing and accessibility need it | — | [Paper: Fig. 7a] | **Ablated**: matters for PSI5/PSI3 and ATAC; contact maps and histone ChIP are insensitive |

## 09 Essential Formulas and Symbols

No equations are stated in the main text, and the deposited Methods section is a stub. The reported metrics are named: Pearson *r* for track coverage agreement; Spearman ρ for eQTL effect-size magnitude; auROC for eQTL sign and for causality (fine-mapped variants vs distance-matched controls); auPRC for ClinVar splicing categories and MFASS; Jensen–Shannon divergence for DNase profile shape; PSI5 and PSI3 for quantitative splicing; and in silico mutagenesis (ISM) for per-base attribution. [Paper: Results; figure captions]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| 24 track evaluations, fold-specific | Generalization to unseen genome intervals | **Wins 22 of 24** against the best external model per task | Broad track-level superiority | Winning everywhere — two losses are not detailed in the main text | [Paper: Fig. 1d] |
| vs Borzoi, expression LFC | Multimodal-model comparison | **+14.7%** relative on cell-type-specific gene-level log-fold change | Better than the closest architectural rival | — | [Paper: Fig. 1e] |
| vs specialists on their own tasks | Does a generalist beat specialists? | Orca contact maps **+6.3%** Pearson, **+42.3%** cell-type differences; ProCapNet **+15%**; ChromBPNet ATAC **+1.6%**, DNase JSD **+9.5%** | Generalist beats specialists here | Uniform margins — +1.6% and +42.3% are very different results | [Paper: Fig. 1d; Extended Data Figs. 3, 4] |
| 26 variant-effect benchmarks, student model | Variant effect prediction | **Matches or beats on 25 of 26** | Broad variant-level superiority | That every win is a clear margin, given "matches or" | [Paper: Fig. 1e] |
| ClinVar splicing categories | Clinical variant classification | auPRC deep intronic/synonymous **0.66** vs 0.64 (Pangolin); splice region **0.57** vs 0.55; missense **0.18** vs 0.16 | Beats the prior best in all three | Practical significance — margins are 0.02, and missense auPRC is 0.18 in absolute terms | [Paper: Fig. 3h] |
| MFASS splicing outliers | Massively parallel reporter splicing | **Outperformed by Pangolin**, 0.54 vs 0.51; beats SpliceAI and DeltaSplice (both 0.49) | An honest reported loss | — | [Paper: Fig. 3i] |
| Splice junction scorer alone | Is the new head doing the work? | Beats previous approaches on all benchmarks **except** deep intronic/synonymous ClinVar and MFASS | The junction mechanism is a real contribution | — | [Paper: Results] |
| GTEx eQTLs vs Borzoi | Expression variant effects | Tissue-weighted mean Spearman **0.39 → 0.49**; mean sign auROC **0.75 → 0.80**; **+25.5%** on sign prediction | Substantial improvement | — | [Paper: Fig. 4c–f] |
| Practical recall at fixed accuracy | Does the margin matter downstream? | At a threshold giving 90% sign accuracy, AlphaGenome recovers **41%** of GTEx eQTLs vs Borzoi's **19%** — more than twice as many | Threshold effects amplify modest metric gains | — | [Paper: Fig. 4g] |
| GWAS credible sets | Application to complex traits | At an 80%-accuracy threshold, a confident sign prediction for at least one variant in **49%** of credible sets (**11%** under a conservative setting) | Useful for a substantial fraction | Phenotype prediction — the model predicts molecular consequences only | [Paper: Fig. 4g; Discussion] |
| eQTL causality | Distinguishing fine-mapped eQTLs from matched controls | Single-modality auROC **comparable** to Borzoi; combining modalities raises mean auROC **0.68 → 0.75**, above Borzoi's 0.71 | Multimodality is what wins this task | Single-modality superiority | [Paper: Fig. 4i] |
| Accessibility and binding QTLs | Chromatin variant effects | **+8.0%** vs ChromBPNet averaged across five datasets | Beats the accessibility specialist | — | [Paper: "Performance overview"] |
| TAL1 oncogenic variants | Mechanistic recapitulation | For chr1:47239296 C>ACG: predicted H3K27ac and H3K4me1 **up** at the variant (neo-enhancer), repressive H3K9me3/H3K27me3 **down** near the TSS, H3K36me3 **up** across the gene body, TAL1 mRNA **up** — all concordant with the experimental literature | A coherent multimodal mechanism, recovered | Prospective discovery — these variants were already characterized | [Paper: Fig. 6b] |
| Oncogenic vs shuffled controls | Is the TAL1 result specific? | Oncogenic mutations increase predicted TAL1 expression more than length-matched shuffled controls; unsupervised clustering separates them across modalities; effect is strongest in thymus, CMP and haematopoietic progenitor tracks | Specificity to sequence and to tissue | — | [Paper: Fig. 6c,d; Supplementary Fig. 10] |
| ISM at the TAL1 variant | Sequence determinants | No mutation within 40 bp affects TAL1 in the **reference** sequence; the **alternative** sequence introduces a MYB motif raising expression, accessibility and H3K27ac — as previously discovered — plus a second ETS-like motif "whose role is currently unknown" | The model localizes the causal motif | That the ETS-like motif is real biology | [Paper: Fig. 6e] |
| Trait-altering variant enrichment | Utility for causal-variant triage | High score thresholds strongly enrich for causal candidates "at the cost of low recall, particularly for GWAS variants" | Useful as a high-precision filter | High-sensitivity screening | [Paper: Fig. 6f] |
| Resolution ablation | Does 1 bp matter? | Best at 1 bp, especially for PSI5/PSI3 and ATAC; contact maps and histone ChIP largely insensitive; variant metrics that aggregate over regions also robust | Resolution matters where the signal is fine | That 1 bp is necessary for everything | [Paper: Fig. 7a] |
| Sequence-length ablation | Does 1 Mb matter? | Training at 1 Mb beats training at ≤32 kb **even when the short models are evaluated at 1 Mb**; inference degrades as context shrinks; a 1-Mb-trained model at short context matches models trained at that length | Long training context is the durable gain | — | [Paper: Fig. 7b] |
| Distillation vs ensembling | Is one student enough? | 64-teacher distillation is competitive with, sometimes better than, a 4-model ensemble; distilling even a single teacher helps caQTL, splicing-outlier and eQTL-sign tasks; removing input mutation costs measurable accuracy | Distillation is a genuine accuracy technique, not only a compression one | — | [Paper: Fig. 7c] |
| Multimodal ablation | Is joint training necessary? | Full multimodal generally best, but **excluding single modality groups causes only modest decreases**, suggesting redundancy; variant tasks benefit most from expression and accessibility, with diminishing returns after | Multimodality helps, unevenly | That all 11 modalities are each load-bearing | [Paper: Fig. 7d; Supplementary Fig. 12] |

## 11 Correct Interpretation of the Conclusions

- Two different models produce the two headline numbers. **22 of 24 track wins** come from fold-specific models evaluated on held-out genome intervals; **25 of 26 variant wins** come from the distilled student, which was trained on all folds. Track generalization and variant performance are therefore not measured on the same model. [Paper: Fig. 1b–e]
- "Matches or exceeds" on 25 of 26 includes ties. The one clear loss is reported: Pangolin beats it on MFASS splicing outliers (auPRC 0.54 vs 0.51). [Paper: Fig. 3i]
- Margins vary by orders of magnitude and should not be averaged: +42.3% on cell-type-specific contact-map differences and +1.6% on ATAC accessibility are both counted as wins.
- The practically important result is Fig. 4g, not the metric deltas: at a fixed 90% sign-accuracy threshold, doubling recovered eQTLs (41% vs 19%) is what a modest auROC gain buys downstream.
- Held-out intervals are held out from the **reference** genome. The authors state they have not benchmarked personal-genome prediction, "which is a known weakness of models in this space". [Paper: Discussion]
- The TAL1 analysis is a recapitulation of variants already characterized in the literature, in the closest available cell type (CD34+ CMP) rather than the T-ALL cell of origin. It demonstrates mechanistic coherence, not discovery.
- The model predicts **molecular** consequences. The authors are explicit that complex-trait application is limited because phenotypes involve gene function, development, environment and gene-to-disease effects beyond sequence-to-function scope. [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] "Accurately capturing the influence of distal regulatory elements (more than 100 kb away) remains a continuing objective." [Paper: Discussion]
- [Paper] Recapitulating tissue- and cell-type-specific patterns and predicting condition-specific variant effects "remain challenging". [Paper: Discussion]
- [Paper] "Both our training data and evaluations are heavily focused on protein-coding genes"; non-coding genes such as microRNAs are under-covered. [Paper: Discussion]
- [Paper] Species coverage is limited to human and mouse, and evaluations are primarily human. [Paper: Discussion]
- [Paper] "We have not yet benchmarked the model on personal genome prediction, which is a known weakness of models in this space." [Paper: Discussion]
- [Paper] Complex-trait application is limited because the model predicts molecular, not phenotypic, consequences. [Paper: Discussion]
- [Paper] Enrichment for causal trait variants comes "at the cost of low recall, particularly for GWAS variants". [Paper: Results]
- [Paper] "Estimates of model certainty would aid in better interpreting predictions" — the model has no uncertainty output. [Paper: Discussion]
- [Paper] Predicting intermediate splicing efficiencies and tissue-specific splicing nuances needs further improvement. [Paper: "Improved track prediction performance"]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Track and variant results come from differently trained models | The student saw all reference-genome folds, so no variant-effect number is accompanied by a held-out-interval generalization check on that same model | The headline 25/26 is the number practitioners will rely on, and its generalization is inferred rather than shown | Report student-model variant performance stratified by whether the locus fell in a fold-specific model's test set | [Paper: Fig. 1b,c] |
| "22 of 24" and "25 of 26" compare against a *different* external model per task | The best-per-task baseline is a strong bar, but a single model losing 2 of 24 is not comparable to 24 separate models each losing once | Counts of wins compress margins that range from +1.6% to +42.3% | Publish the per-task margin distribution as the headline, not the win count | [Paper: Fig. 1d,e] |
| ClinVar auPRC margins are 0.02 in each of three categories | Consistent direction, but small magnitude, and no confidence intervals in the main text | These are the clinically framed results | Bootstrap the auPRC differences and report intervals | [Paper: Fig. 3h] |
| Evaluation is on the reference genome throughout | Personal-genome prediction is a known failure mode for this model class, and it is the setting rare-disease diagnostics actually needs | The Discussion names rare-disease diagnostics as a target application while acknowledging this gap | Benchmark on a personal-genome dataset before the diagnostic claim is repeated | [Paper: Discussion] |
| Modality ablations show "only modest performance decreases" when a modality group is dropped | Substantial redundancy weakens the argument that all 11 modalities are necessary | The unified-multimodal framing is the paper's identity | Report, per modality, the marginal value added at fixed compute | [Paper: Fig. 7d; Supplementary Fig. 12] |
| The ETS-like motif at TAL1 is flagged as having unknown role | An unexplained model-derived finding presented alongside a confirmed one | Readers may treat both with equal confidence | Test the ETS motif experimentally, or label model-only findings distinctly in the figure | [Paper: Fig. 6e] |
| The model has no uncertainty estimate, though the ensemble it was distilled from did | Distillation discards exactly the ensemble disagreement that would have provided calibration | For diagnostic use, a confidence-free score is hard to act on | Distil a variance head alongside the mean, or retain a small ensemble for calibration | [Paper: Discussion; "Unifying DNA sequence-to-function model"] |
| Deposited Methods are a stub in the open-access text | Training data composition, fold construction and the exact benchmark protocols are not verifiable from the PMC record | Reproducibility and benchmark fairness both depend on those details | Consult the publisher's Methods and Supplementary Tables 3–4 directly | [Paper: Methods] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: distillation can improve accuracy, not only reduce cost — and the mechanism matters. Distilling on *mutated* inputs teaches the student the teacher's local sensitivity, which is precisely what variant effect prediction requires.
- Agent-derived knowledge candidate: when different models produce different headline numbers, say which model produced which. This paper does it cleanly, and that clarity is what makes the numbers usable.
- Agent-derived knowledge candidate: report the operating-point consequence, not just the metric delta. "Twice as many eQTLs recovered at 90% sign accuracy" communicates more than "+25.5% sign prediction".
- Agent-derived knowledge candidate: a win count over heterogeneous benchmarks hides margin structure; publish the margin distribution alongside it.
- Agent-derived knowledge candidate: ablate the input context in both training and inference separately. Here training length mattered more than inference length, which is not the intuitive result and changes deployment advice.
- Agent-derived knowledge candidate: a losing benchmark reported plainly (MFASS) buys more credibility than a marginally winning one, and makes the rest of the table easier to trust.

## 15 Connections to Existing Knowledge

[Analysis] AlphaGenome is positioned directly against two lines it names throughout. The multimodal sequence-to-function line — Enformer then Borzoi — supplies its architecture lineage and its main comparator; the specialist line supplies per-task baselines it must beat on their own ground: SpliceAI, Pangolin and DeltaSplice for splicing, ChromBPNet for accessibility, ProCapNet for transcription initiation, Orca for contact maps. Its distinguishing capabilities are the combination of 1-Mb context with base-pair resolution across all modalities simultaneously, and the splice-junction head, which is genuinely new rather than an improvement on an existing quantity.

Within this catalogue it forms an informative pair with **Evo 2**, the other genomics foundation model on the page. They are complementary rather than competing: Evo 2 is an autoregressive likelihood model over raw nucleotides across all domains of life, scoring variants zero-shot and generating sequence; AlphaGenome is a supervised sequence-to-function model over human and mouse only, predicting measured assay tracks. The comparison that connects them is ChromBPNet — Evo 2's own paper reports losing to it on DART-eval accessibility QTLs, while AlphaGenome reports beating it by 8.0% averaged over five datasets. That is the cleanest available evidence of where each paradigm's strength lies: generalist likelihood where labels are scarce, supervised track prediction where the assay exists.

## 16 Research Ideas

### Agent-derived research candidate

**Distil the disagreement, not just the mean.** [Hypothesis] The distilled student discards the one thing its teacher ensemble had that clinical use most requires — calibrated uncertainty — and a student trained to predict both the ensemble mean *and* its variance will recover a usable confidence estimate at negligible inference cost, materially improving the precision–recall trade-off that currently forces "low recall, particularly for GWAS variants". Delta: modify the distillation objective so the student emits a predictive distribution per track rather than a point estimate, supervised by the teacher ensemble's per-position mean and spread under the same random-mutation augmentation already in use; leave architecture, data and teacher count unchanged so the comparison is isolated to the objective. Validation: evaluate on the published 26 variant-effect benchmarks to confirm no loss in point accuracy; then measure calibration directly — expected calibration error and coverage of nominal intervals on held-out GTEx eQTL effect sizes — and re-run the Fig. 4g operating-point analysis using uncertainty-aware thresholds, asking whether eQTL recovery at 90% sign accuracy exceeds the published 41%; repeat the trait-variant enrichment analysis to test whether recall improves at matched precision. Falsifier: uncertainty-aware thresholding fails to beat score-magnitude thresholding on recovery at matched accuracy, indicating the ensemble's disagreement carries no information beyond the predicted effect size itself. Failure modes: teacher spread may reflect training-data noise rather than epistemic uncertainty, making it well-calibrated for the wrong quantity; variance targets are unstable at 1-bp resolution on sparse tracks; the augmentation distribution used in distillation may not resemble the natural variant distribution, so calibration could hold for random mutations and fail for real variants. Innovation status: unverified; prior-art search required.
