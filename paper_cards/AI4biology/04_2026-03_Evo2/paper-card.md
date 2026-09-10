# Paper Card: Genome modelling and design across all domains of life with Evo 2

> Source coverage: Open-access full text via PubMed Central (PMC13128491), including Main, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; Methods and Extended Data are cited only where the main text quotes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Resource / benchmark
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code and dataset
>
> Card completeness: Complete for the main text; supplementary tables and Extended Data figures are marked where not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| Evo 2 | the genomic foundation model described in the paper, released at 7B and 40B parameters | Preserve author capitalization; always state which size |
| OpenGenome2 | the curated non-redundant nucleotide dataset assembled for training | Treat as a released resource distinct from the model |
| StripedHyena 2 | the convolutional multi-hybrid architecture underlying Evo 2 | Keep distinct from a plain Transformer |
| zero-shot likelihood | the model's sequence likelihood used directly as a variant effect score, with no task training | Do not conflate with the supervised-embedding results |
| SAE | sparse autoencoder trained on Evo 2 activations for interpretability | Interpretability evidence, not predictive evidence |

## 01 Basic Information

- **Title:** Genome modelling and design across all domains of life with Evo 2
- **Authors:** Garyk Brixi, … , Brian L. Hie (first and last of a large consortium). [Paper: Metadata]
- **Venue / date:** *Nature*, 2026-03. [Paper: Metadata]
- **DOI:** [10.1038/s41586-026-10176-5](https://doi.org/10.1038/s41586-026-10176-5)
- **Code and weights:** [arcinstitute/evo2](https://github.com/arcinstitute/evo2) — parameters, distributed training code, multi-GPU inference code and the OpenGenome2 dataset are all released under an open-source licence. [Paper: Discussion]
- **Access boundary:** the open-access full text was read via PMC. Supplementary tables and most Extended Data panels were not opened directly and are cited only as the main text describes them.

## 02 One-Sentence Summary

[Paper] Evo 2 is a genomic foundation model trained on 9 trillion DNA base pairs across all domains of life with a 1-million-token context at single-nucleotide resolution, which predicts variant effects without task-specific fine-tuning, exposes interpretable biological features, and generates genome-scale sequences. [Paper: Abstract]

## 03 Research Question

- [Paper] Can one sequence model trained across all domains of life predict the functional consequences of genomic variation and generate coherent sequence at genome scale, without task-specific fine-tuning? [Paper: Abstract]
- [Analysis] The unresolved question is where generalist likelihood modelling stops being competitive with task-specific supervised models — the paper answers this honestly in one place (chromatin accessibility QTLs) and leaves it open elsewhere.

## 04 Research Background and Development Path

1. [Paper] Sequencing, synthesis and editing tools have transformed biology, but the complexity encoded in genomes is still not understood well enough to predict the effects of many classes of genomic change. [Paper: Abstract]
2. [Paper] Models that learn from genomic sequence across diverse organisms have been steadily improving prediction and design. [Paper: Abstract]
3. [Paper] Evo 2 scales that idea: 9 trillion base pairs, all domains of life, a 1M-token context window, single-nucleotide resolution. [Paper: Abstract]
4. [Analysis] The step change is context length plus taxonomic breadth together. Either alone had been tried; holding both at nucleotide resolution is what makes genome-scale generation and long-range regulatory reasoning available to the same model.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Variant interpretation | Many variant classes, especially noncoding, have no reliable effect prediction | Effects depend on long-range and cross-scale context | [Paper: Abstract] |
| Task-specific tooling | A separate supervised model per assay | No shared representation of genomic function | [Paper: Abstract] |
| Context truncation | Regulatory logic spans far more than a few kilobases | Prior models had short context windows | [Paper: Abstract] |
| Closed models | Results cannot be interrogated or extended | Weights, data and code withheld | [Paper: Discussion] |

## 06 Core Idea

- **Surface method:** an autoregressive genomic language model over raw nucleotides. [Paper: Abstract]
- **Core insight:** a single likelihood over DNA, learned broadly enough and at long enough context, becomes a general-purpose functional predictor — pathogenicity, splicing, essentiality and fitness all fall out of it without task heads. [Paper: Abstract]
- **General lesson:** [Analysis] a generalist likelihood buys breadth and zero-shot transfer, and pays for it against specialists on assays with abundant supervision. The paper's own DART-eval numbers make that trade explicit rather than hiding it.

## 07 Method Overview

**Flow:** curated genomes (OpenGenome2) → autoregressive pretraining at 8,192-token context → multi-stage midtraining extending context to 1M tokens → zero-shot likelihood scoring, embedding extraction, or autoregressive generation. [Paper: "Evo 2 architecture, training, and data"]

Two models were trained: **Evo 2 7B** on 2.4 trillion tokens, and **Evo 2 40B** on 9.3 trillion tokens. OpenGenome2 comprises more than 8.8 trillion nucleotides from bacteria, archaea, eukarya and bacteriophage. [Paper: "Evo 2 architecture, training, and data"]

**Main workflow figure:** Fig. 1 — architecture, training procedure, datasets and evaluations. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| StripedHyena 2 backbone | Long-context sequence modelling | 1M tokens is impractical for dense attention | Nucleotides → hidden states | [Paper: "Evo 2 architecture, training, and data"] | Architecture ablation not assessed from the main text |
| OpenGenome2 | Curated, non-redundant, cross-domain corpus | Breadth is the source of generalist behaviour | Genomes → training tokens | [Paper: "Evo 2 architecture, training, and data"] | Data-composition ablation appears in Extended Data, not assessed here |
| Context extension midtraining | Raises context from 8K to 1M tokens | Regulatory logic is long-range | Short-context model → long-context model | [Paper: "Evo 2 architecture, training, and data"] | Not independently ablated in the main text |
| Zero-shot likelihood scoring | Turns likelihood into a variant score | Avoids per-task supervision | Sequence pair → score | [Paper: "Human variant effect prediction"] | Compared against supervised baselines, see 10 |
| SAE interpretability layer | Extracts human-readable features | Makes representations auditable | Activations → sparse features | [Paper: "Feature interpretation in Evo 2"] | Post hoc; removing it does not change predictions |
| Safety data exclusion | Removes eukaryote-infecting viral sequences | Dual-use mitigation | Corpus → filtered corpus | [Paper: Discussion] | Authors state post-training may circumvent it |

## 09 Essential Formulas and Symbols

Not assessable from the sources read. The main text describes the objective as autoregressive next-token prediction over nucleotides but states no equations; formal definitions, if any, sit in Methods, which was not opened directly.

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| ClinVar pathogenic vs benign | Zero-shot clinical variant classification | AUROC and AUPRC reported across models, Evo 2 competitive | Zero-shot likelihood carries clinical signal | Clinical readiness or diagnostic use | [Paper: "Human variant effect prediction", Fig. 3] |
| BRCA1 saturation mutagenesis | Coding and noncoding variant effects | Strong on coding SNVs (n = 2,077); **outperformed all other models on noncoding SNVs** (n = 1,125) | Noncoding variant effect is where the generalist wins | That it replaces functional assays | [Paper: "Human variant effect prediction", Fig. 3] |
| BRCA1 supervised probe | Whether embeddings beat zero-shot | Ridge regression on Evo 2 embeddings: **AUROC 0.95, AUPRC 0.88**, above zero-shot Evo 2 40B | Embeddings are a strong lightweight substrate | Zero-shot parity with supervised use | [Paper: "Human variant effect prediction", Fig. 3g,i] |
| DART-eval caQTL / dsQTL | Generalist vs specialist on accessibility | Evo 2 40B **caQTL 0.58, dsQTL 0.66**; Nucleotide Transformer 0.52 / 0.61; **ChromBPNet 0.77 / 0.89** | Beats other DNA language models; **trails** sequence-to-function specialists | General superiority over task-specific models | [Paper: "Human variant effect prediction", Extended Data Fig.] |
| Genome-scale generation | Coherence at chromosome scale | Mitochondrial, prokaryotic and eukaryotic sequence generated with greater naturalness and coherence than prior methods | Generation is coherent at scale | Biological viability of generated genomes | [Paper: Abstract; "Genome-scale generation", Fig. 5] |
| Chromatin-accessibility design | Guided generation of accessibility patterns | Experimentally validated patterns under inference-time guidance | Design is steerable and testable | Routine wet-lab reliability | [Paper: Abstract; "Designing mammalian chromatin patterns", Fig. 6] |

## 11 Correct Interpretation of the Conclusions

- Zero-shot means no task-specific fine-tuning; it does not mean no supervision anywhere in the comparison. The strongest BRCA1 number on this card (AUROC 0.95) comes from a **supervised** probe on Evo 2 embeddings. [Paper: "Human variant effect prediction"]
- Evo 2's advantage is clearest where supervision is scarce — noncoding variants — and reverses where a specialist has abundant labels, as DART-eval shows. [Paper: "Human variant effect prediction"]
- "Greater naturalness and coherence" is a sequence-statistics claim, not a claim that generated genomes function. [Analysis]
- The 40B 1M-context model is the best overall; the released 1B short-context model is explicitly described by the authors as one to avoid. [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] The experimental 1B short-context model "should be avoided owing to overall weaker performance". [Paper: Discussion]
- [Paper] Safety data exclusions deliberately weakened language-modelling and mutational-effect performance on human viruses — a cost the authors accepted. [Paper: Discussion]
- [Paper] "Task-specific post-training may circumvent this risk mitigation measure and should be approached with caution." [Paper: Discussion]
- [Paper] Fully open release may enable unanticipated accident or misuse. [Paper: Discussion]
- [Analysis] The paper does not frame the DART-eval shortfall as a limitations-section item, though it is one.

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Training corpus spans all of life and evaluation sets are human clinical databases | Sequence overlap between ClinVar-adjacent regions and training genomes is not excluded in what was read | Zero-shot claims depend on clean separation | Held-out-by-locus evaluation; report overlap statistics | [Paper: "Human variant effect prediction"] |
| Best BRCA1 result uses a supervised probe | Headline "zero-shot" framing can absorb credit from a supervised result | Readers compare across papers on the headline | Always report probe and zero-shot side by side | [Paper: Fig. 3g,i] |
| Specialists still win on accessibility QTLs | Generalist framing may be over-read | Determines whether to deploy Evo 2 or a specialist | Per-assay decision rule based on label availability | [Paper: DART-eval comparison] |
| Safety filtering is a data-exclusion measure the authors say post-training can undo | Mitigation is not a property of the released weights | An open model cannot retract a capability | Red-team after fine-tuning, not only at release | [Paper: Discussion] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: report zero-shot and supervised-probe results as separate rows, never as one number, when a foundation model is evaluated.
- Agent-derived knowledge candidate: a generalist sequence model's value concentrates where labels are scarce; benchmark selection should be chosen to expose that boundary rather than hide it.
- Agent-derived knowledge candidate: for open weights, treat safety evaluations as needing to survive fine-tuning, because data exclusion does not.

## 15 Connections to Existing Knowledge

[Analysis] Evo 2 sits in the DNA-language-model line that runs through Nucleotide Transformer and the first Evo, and is compared directly against both classes on this page — other DNA LMs, which it beats on DART-eval, and sequence-to-function supervised models such as ChromBPNet, which beat it. Its distinguishing contributions are the 1M-token context at nucleotide resolution and the completeness of the open release, which includes the training dataset and not only the weights. Priority claims against concurrent long-context genomic models require a dedicated literature comparison not attempted here.

## 16 Research Ideas

### Agent-derived research candidate

**Label-scarcity crossover for generalist genomic models.** [Hypothesis] There is a predictable training-set size below which Evo 2 embeddings beat a task-specific supervised model, and above which the specialist wins; the crossover point is a usable deployment rule. Delta: for a set of assays with large labelled corpora (accessibility, splicing, expression), subsample labels across several orders of magnitude and fit both a probe on Evo 2 embeddings and a specialist from scratch at each size. Validation: five assays, matched compute, three seeds, report crossover with confidence intervals. Falsifier: no consistent crossover, or one that varies so much across assays that it gives no rule. Failure modes: specialist architectures not tuned at small sample sizes; assay-specific label noise dominating; embedding extraction cost making the comparison unfair on compute. Innovation status: unverified; prior-art search required.
