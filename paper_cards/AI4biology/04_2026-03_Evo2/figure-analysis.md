# Figure Analysis: Genome modelling and design across all domains of life with Evo 2

Analysis of the six main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41586-026-10176-5) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13128491/) alongside this file.

## Fig. 1 — Architecture, training, datasets and evaluations

- **Argumentative role:** Orientation. Establishes the scope claim before any result: one model, all domains of life, molecules through genomes.
- **Panel logic:** Panel a spans the central dogma and the scale axis simultaneously — this is the figure that licenses every later "generalist" claim.
- **Reusable design:** Put the scope figure first when the contribution is breadth, so readers calibrate what the later benchmarks are sampling from.
- **Boundary:** A scope diagram is a claim about coverage, not about performance within that coverage.
- **Locator:** [Paper: Fig. 1]

## Fig. 2 — Mutational effects on protein, RNA and organismal fitness

- **Argumentative role:** Establishes that a single zero-shot likelihood transfers across molecule types and across domains of life.
- **Panel logic:** Panel a defines the mechanism — likelihood as effect score — and the rest sample it across contexts. Read a before the comparisons.
- **Reusable design:** Define the scoring rule in the first panel, then vary only the evaluation context, so each later panel tests transfer rather than a new method.
- **Boundary:** Breadth across assay types is not accuracy within any one of them; Fig. 3 is where that gets tested.
- **Locator:** [Paper: Fig. 2]

## Fig. 3 — Zero-shot human variant effect prediction

- **Argumentative role:** The paper's central quantitative claim, and the one place the evidence chain is most worth reading carefully.
- **Panel logic:** Panel d gives ClinVar AUROC/AUPRC across models. Panel e is BRCA1 saturation mutagenesis, split coding (n = 2,077 SNVs) and noncoding (n = 1,125 SNVs) — the noncoding split is where Evo 2 outperforms every other model tested. Panels g and i change the setting: a **supervised** classifier trained on Evo 2 embeddings, reaching AUROC 0.95 / AUPRC 0.88, above zero-shot Evo 2 40B.
- **Reusable design:** Keeping the zero-shot and supervised-probe results in the same figure is honest practice — it lets a reader see which number belongs to which regime instead of quoting the larger one.
- **Boundary:** The 0.95 is a supervised result. It does not support a zero-shot claim, and the figure does not ask it to.
- **Locator:** [Paper: Fig. 3d,e,g,i]

## Fig. 4 — Mechanistic interpretability via sparse autoencoders

- **Argumentative role:** Shows the representation contains recoverable biological structure — exon–intron boundaries, transcription factor binding sites, protein structural elements, prophage regions.
- **Panel logic:** Panel a defines the SAE extraction procedure; downstream panels are annotation and discovery applications of those features.
- **Reusable design:** Interpretability presented as a usable annotation tool rather than as a gallery of cherry-picked neurons.
- **Boundary:** Feature recovery is evidence about representations, not additional evidence for predictive accuracy. It cannot be cited to support Fig. 3.
- **Locator:** [Paper: Fig. 4]

## Fig. 5 — Genome-scale generation

- **Argumentative role:** Demonstrates unconstrained autoregressive generation at chromosome and genome scale, prompted from real sequence.
- **Panel logic:** Panel a establishes the prompting setup on the *H. sapiens* mitochondrial genome before extending to prokaryotic and eukaryotic cases.
- **Reusable design:** Anchor generative claims to a small, well-characterized genome first, where naturalness can actually be checked.
- **Boundary:** "Naturalness and coherence" are sequence-statistical properties. No panel here establishes that a generated genome is viable.
- **Locator:** [Paper: Fig. 5]

## Fig. 6 — Generative chromatin accessibility under inference-time guidance

- **Argumentative role:** The strongest design claim, because it is the one with experimental validation attached.
- **Panel logic:** Multi-kilobase sequences designed to place accessible regions at chosen locations and lengths, visualized as peaks.
- **Reusable design:** Pair a controllable design objective with a measurable readout, so the design claim has a falsifier built in.
- **Boundary:** Validation covers the designed accessibility patterns under the tested conditions; it does not extend to arbitrary regulatory programs.
- **Locator:** [Paper: Fig. 6]

## Cross-figure reading rule

Read Fig. 1 for scope, then Fig. 3 before anything else — it is the figure that sets the real claim boundary, because it contains both the zero-shot and the supervised results. Fig. 2 generalizes the mechanism, Fig. 4 explains the representation, and Figs. 5 and 6 move from prediction to design. Extended Data Fig. 2, on biosecurity and population-bias evaluation, is cited in the Discussion and is worth reading with Fig. 5 rather than separately.
