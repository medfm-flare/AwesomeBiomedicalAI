# Figure Analysis: Advancing regulatory variant effect prediction with AlphaGenome

Analysis of the seven main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41586-025-10014-0) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12851941/) alongside this file.

## Fig. 1 — Architecture, training regimes and headline performance

- **Argumentative role:** Establishes the model, and — importantly — establishes that there are *two* of them.
- **Panel logic:** Panel a is the architecture: 1 Mb in, U-Net with a transformer tower, 1-D embeddings for tracks and 2-D embeddings for contact maps. Panel b is the fold-specific regime, used for track evaluation on held-out genome intervals. Panel c is distillation: all-fold teachers, one student. Panels d and e are the two win counts — 22 of 24 track evaluations, 25 of 26 variant evaluations.
- **Reusable design:** Drawing panels b and c as separate training regimes, before showing any results, is what keeps the paper honest. A reader who has seen this figure knows that the track numbers and the variant numbers come from different models and cannot conflate them.
- **Boundary:** Win counts compress margins that range from +1.6% (ATAC) to +42.3% (cell-type-specific contact-map differences), and "matches or exceeds" folds ties into wins. The per-task margins live in Supplementary Tables 3 and 4, not in these panels.
- **Locator:** [Paper: Fig. 1a–e]

## Fig. 2 — Track predictions in detail

- **Argumentative role:** Shows what the model actually outputs, at the resolution claimed.
- **Panel logic:** Panel a is observed versus predicted coverage across a held-out 1-Mb interval. Panel b zooms to the LDLR gene in HepG2 and shows strand-specific base-pair-resolution RNA-seq coverage over exons *together with* splice sites, splice site usage and junction coverage — the multimodal claim made concrete at one locus. Panel c gives Pearson correlations across human and mouse tracks. Panel d is the honest panel: cell-type-specific expression deviation, which the text says "remains a challenging task".
- **Reusable design:** Putting the single-locus qualitative view (b) adjacent to the genome-wide quantitative view (c) is the right pairing. One shows what the prediction looks like, the other shows whether that example is representative.
- **Boundary:** Panel d marks the real limitation: overall expression is predicted well, cell-type-specific deviation much less so — and cell-type specificity is precisely what most downstream applications need.
- **Locator:** [Paper: Fig. 2a–e]

## Fig. 3 — Splicing variant effects

- **Argumentative role:** Head-to-head against the splicing specialists, on their own benchmarks.
- **Panel logic:** Panel a compares what each model predicts, which matters because AlphaGenome predicts junction usage where SpliceAI and Pangolin predict site scores. Panel h is the ClinVar comparison — auPRC 0.66 vs 0.64 (Pangolin) on deep intronic/synonymous, 0.57 vs 0.55 on splice region, 0.18 vs 0.16 on missense. **Panel i is the loss**: on MFASS splicing outliers, Pangolin wins 0.54 to 0.51.
- **Reusable design:** Panel i is the most credibility-building panel in the paper. Publishing the one benchmark you lose, at the same visual prominence as the ones you win, is what makes a 25-of-26 claim believable.
- **Boundary:** The ClinVar margins are 0.02 auPRC in every category, with no confidence intervals given in the main text. Consistency of direction across three categories is the real signal; the magnitudes are small. Note too that missense auPRC of 0.18 is low in absolute terms — the improvement is over a weak baseline.
- **Locator:** [Paper: Fig. 3a,h,i]

## Fig. 4 — Gene expression variant effects

- **Argumentative role:** The largest quantitative gains, and the clearest demonstration of why they matter.
- **Panel logic:** Panels c–f give eQTL magnitude and sign against Borzoi and Enformer (tissue-weighted Spearman 0.39 → 0.49, sign auROC 0.75 → 0.80). **Panel g is the important one**: at a score threshold yielding 90% sign accuracy, AlphaGenome recovers 41% of GTEx eQTLs against Borzoi's 19%, and at an 80% threshold it gives a confident sign call for at least one variant in 49% of GWAS credible sets. Panel i covers causality — comparable to Borzoi single-modality, but 0.68 → 0.75 when modalities are combined, above Borzoi's 0.71.
- **Reusable design:** Panel g translates a metric improvement into an operating-point consequence. "Sign auROC 0.75 → 0.80" is hard to act on; "twice as many eQTLs recovered at the same accuracy" is not. Every benchmark paper should have this panel.
- **Reusable design (second):** Panel i separates the single-modality result (a tie) from the multimodal result (a win), which correctly attributes the gain to the unified architecture rather than to raw predictive strength.
- **Boundary:** The GWAS credible-set number drops from 49% to 11% under a conservative setting, and both are reported. The model predicts molecular consequences; the credible-set analysis is variant triage, not phenotype prediction.
- **Locator:** [Paper: Fig. 4c–i]

## Fig. 5 — Accessibility and TF binding

- **Argumentative role:** Extends the variant-effect claim to chromatin, against ChromBPNet — the specialist that Evo 2's own paper reports losing to on comparable tasks.
- **Panel logic:** Panel a is the centre-mask variant scoring strategy; the remainder benchmarks accessibility QTLs and SPI1 binding QTLs.
- **Reusable design:** Stating the variant-scoring strategy schematically before reporting results makes the comparison auditable — how a variant is turned into a score is a design choice that can dominate benchmark outcomes.
- **Boundary:** The +8.0% figure is averaged across five datasets; per-dataset margins are not in the main text.
- **Locator:** [Paper: Fig. 5a]

## Fig. 6 — Multimodal interpretation at the TAL1 locus

- **Argumentative role:** The demonstration that unified prediction enables *mechanism*, not just ranking. This is what the whole architecture was for.
- **Panel logic:** Panel b is the mechanistic recapitulation for chr1:47239296 C>ACG — activating marks H3K27ac and H3K4me1 up at the variant, repressive H3K9me3 and H3K27me3 down near the TSS, elongation mark H3K36me3 up across the gene body, and TAL1 mRNA up. Panel c compares oncogenic variants against length-matched, sequence-shuffled controls. Panel d shows unsupervised clustering separating oncogenic from shuffled across modalities. Panel e is ISM: nothing within 40 bp matters in the reference sequence, while the alternative sequence creates a MYB motif — plus a second ETS-like motif of unknown role. Panel f is the enrichment analysis for trait-altering variants.
- **Reusable design:** Panel b is a coherence argument, not a benchmark: five separate predicted signals all point the same way and match what the experimental literature reports. That kind of internal consistency across independent modalities is evidence a single-modality model structurally cannot provide.
- **Reusable design (second):** The shuffled-control comparison in panel c is what stops panel b from being anecdote. Without it, one well-chosen variant proves nothing.
- **Boundary:** These variants were already characterized; this is recapitulation, not discovery. Predictions were made in CD34+ CMP, "the closest available match to the T-ALL cell of origin", not the cell type itself. And panel e mixes a confirmed finding (MYB) with an unconfirmed one (the ETS-like motif) at equal visual weight.
- **Locator:** [Paper: Fig. 6a–f; Extended Data Fig. 9]

## Fig. 7 — Ablations

- **Argumentative role:** Says which design decisions actually earned their place. Unusually, it reports several that did not matter much.
- **Panel logic:** Panel a — target resolution: 1 bp best for splicing (PSI5/PSI3) and ATAC, but contact maps and histone ChIP are largely insensitive. Panel b — sequence length, separated into *training* length and *inference* length, with the result that training at 1 Mb helps even when inference is short. Panel c — distillation versus ensembling, including the finding that removing input mutation during distillation costs eQTL sign −0.06. Panel d — multimodal versus single-modality-group training.
- **Reusable design:** Panel b's separation of training context from inference context is the most transferable idea here. Most papers conflate them; separating them yields an actionable deployment result — you can train long and infer short.
- **Boundary:** Panel d undercuts the paper's own framing somewhat: dropping a modality group causes "only modest performance decreases", implying substantial redundancy across the eleven modalities. The strongest multimodal case is for eQTLs; accessibility variants do about as well on accessibility data alone.
- **Locator:** [Paper: Fig. 7a–d; Supplementary Fig. 12]

## Extended Data

Extended Data Fig. 1 (full architecture, including the splice-junction mechanism), Figs. 2–4 (splicing, track and contact-map benchmarking against Enformer, Borzoi and Orca), Fig. 5 (eQTL stratification), Fig. 7 (enhancer–gene linking via input gradients), Fig. 8 (CAGI5 MPRA challenge) and Fig. 9 (Mendelian disease variant interpretation) carry claims cited in the card but were not opened directly.

## Cross-figure reading rule

Fig. 1b,c before any result — the paper uses two differently trained models and the rest of the figures only make sense once that is clear. Then Fig. 4g, which is where a metric improvement becomes a practical one. Fig. 3i is worth reading deliberately: it is the benchmark AlphaGenome loses, and its presence is what makes the 25-of-26 claim credible. Fig. 6 is the architectural payoff — the multimodal coherence argument no single-modality model could make — and Fig. 7 is the honest accounting of which design choices mattered, including two that mattered less than the framing implies.
