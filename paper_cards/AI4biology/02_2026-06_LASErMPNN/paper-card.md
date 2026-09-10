# Paper Card: Zero-shot design of drug-binding proteins via neural iterative selection−expansion

> Source coverage: Open-access full text via PubMed Central (PMC13441969), including Main, all named result sections, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; Methods, Supplementary Information and Extended Data are cited only where the main text quotes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Experimental validation
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code
>
> Card completeness: Complete for the main text; Extended Data Table 1 (ablations) and the Supplementary figures are marked where not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| LASErMPNN | the ligand-aware graph neural network that designs a protein sequence for a given backbone plus docked ligand | The network; not the design loop |
| NISE | neural iterative selection–expansion, the closed-loop algorithm pairing LASErMPNN with a co-structure predictor | The algorithm; the paper's actual contribution to hit rate |
| self-consistency | agreement between the intended structure and the structure predicted from the designed sequence | Here extended to a third axis, the ligand pose |
| ligand pLDDT | the co-structure predictor's confidence in the placed ligand | The optimization target NISE actually climbs |
| EPIC / APEX | the best exatecan binder and the best apixaban binder produced | Named proteins, not model variants |
| zero-shot design | design with no experimental selection round in the loop | Does not mean no experiment; means no experiment *feeding back* into design |

## 01 Basic Information

- **Title:** Zero-shot design of drug-binding proteins via neural iterative selection−expansion
- **Authors:** Benjamin Fry, … , Nicholas F. Polizzi (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature*, 2026-06. [Paper: Metadata]
- **DOI:** [10.1038/s41586-026-10670-w](https://doi.org/10.1038/s41586-026-10670-w)
- **Code:** [polizzilab/LASErMPNN](https://github.com/polizzilab/LASErMPNN)
- **Access boundary:** the open-access full text was read via PMC. Methods, Supplementary Information and Extended Data tables were not opened directly and are cited only as the main text describes them.

## 02 One-Sentence Summary

[Paper] Pairing a ligand-aware sequence-design network (LASErMPNN) with a protein–ligand co-structure predictor in a closed loop (NISE) designs small-molecule binding proteins from scratch with 100% and 83% experimental success rates against two clinical drugs, reaching nanomolar-to-picomolar affinities that beat the previous leading methods by 70-fold and nearly 10,000-fold. [Paper: Abstract]

## 03 Research Question

- [Paper] Can the self-consistency principle that works for protein and peptide binder design be extended to small molecules, so that binders are designed zero-shot rather than found by high-throughput experimental selection? [Paper: Main]
- [Analysis] The question underneath it is narrower and more interesting: is the bottleneck the *sequence-design* network or the *optimization loop* around it? The paper answers that directly, and the answer is the loop.

## 04 Research Background and Development Path

1. [Paper] De novo small-molecule binder design has lagged the rest of the field; notable successes relied mainly on high-throughput experimental selection. [Paper: Main]
2. [Paper] The few methods with high computational hit rates (about 33%) worked by approximating ligand functional groups as parts of amino acids, which does not generalize. [Paper: Main]
3. [Paper] Self-consistency — does the designed sequence fold back to the intended structure — has guided topology and protein-binder design, but had not been extended to small molecules because non-amino-acid chemistry is hard to encode. [Paper: Main]
4. [Paper] Co-structure predictors (RFAA, Boltz-1/2, AF3) now predict a protein–ligand complex from sequence plus SMILES, which supplies the missing third axis: is the *ligand* also where it was meant to be? [Paper: Main]
5. [Analysis] The development path is therefore not "a better sequence designer" but "a scoring signal that finally exists". LASErMPNN is roughly at parity with LigandMPNN on sequence recovery; what changed is that a ligand-pose confidence score became available to iterate against.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Reliance on experimental selection | Binders found by screening, not designed | No computational signal reliable enough to pick winners | [Paper: Main] |
| Frozen initial pose | Sequence designed for a docked pose that is rarely optimal | Docking and design are run once, in sequence, never jointly | [Paper: "NISE sampling algorithm"] |
| Backbone-only self-consistency is too weak a screen | Most designs pass backbone r.m.s.d. but few place the ligand correctly | Backbone agreement says nothing about the pocket | [Paper: "Design of exatecan binders using NISE"] |
| Physics-based energy functions do not improve designs | Rosetta-driven iteration fails to lower sequence NLL or raise ligand pLDDT | Empirical energy gradients lie partly orthogonal to the learned joint distribution | [Paper: Fig. 1c; Discussion] |
| Chemistry absent from the training distribution | Exatecan has no structure in the PDB or CSD | Neural design must extrapolate to unseen ligands | [Paper: "Exatecan design objective"] |

## 06 Core Idea

- **Surface method:** a ligand-conditioned sequence designer plus a co-structure predictor, run in a loop.
- **Core insight:** the two networks are *reciprocal conditionals* — P(sequence | structure, ligand) and P(structure, ligand | sequence) — so alternating between them is coordinate ascent on the joint distribution P(sequence, structure, ligand). Climbing that joint is what makes designs look like the PDB. [Paper: "NISE sampling algorithm"; Fig. 1d]
- **General lesson:** [Analysis] the loop, not the network, was the missing piece. Substituting LigandMPNN for LASErMPNN gives similar aggregate metrics; substituting Rosetta for the co-structure predictor breaks optimization entirely. When a method's ablation shows one component is swappable and the other is not, that identifies where the contribution actually lives.

## 07 Method Overview

**Flow:** designable backbone scaffolds (hallucinated four-helix bundles, or published NTF2 folds) → ligand docked in (COMBS, or brute-force rigid-body docking) → **repeat:** LASErMPNN samples ~1,000 sequences per structure at high temperature (expansion) → co-structure predictor folds each (RFAA for exatecan, Boltz-2 for apixaban) → keep only designs self-consistent in backbone *and* ligand r.m.s.d., select the top few by ligand pLDDT (selection) → those become the next round's input coordinates. [Paper: "NISE sampling algorithm"]

LASErMPNN itself is an encoder–decoder heterograph network over protein backbone atoms and ligand atoms, trained on PDB protein–ligand co-crystal structures. It autoregressively decodes amino-acid identity **and** side-chain dihedrals together, in a random decoding order, using a pretrained-and-frozen ligand encoder whose own training task is predicting quantum-chemistry-derived atomic properties such as partial charge. [Paper: "LASErMPNN neural network"; Fig. 2a]

A typical 14-iteration NISE trajectory takes about 5 h on four A6000 GPUs, most of it co-structure prediction. [Paper: Discussion]

**Main workflow figure:** Fig. 1b — the NISE loop. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Pretrained ligand encoder | Embeds ligand atoms from coordinates and elements | Lets the model generalize to ligands absent from the PDB | Ligand atoms → frozen embeddings | [Paper: "LASErMPNN neural network"; Fig. 2a] | Ablation reported in Extended Data Table 1, not directly assessed here; authors state performance depends on it |
| Joint sequence + dihedral decoding | Predicts residue identity and χ angles in one pass | Rotamer-after-sequence decoding overpacks the pocket | Backbone + ligand → sequence + side chains | [Paper: "LASErMPNN neural network"] | Authors attribute LigandMPNN's overpacking to lacking this (Extended Data Fig. 1) |
| Frame-level backbone noising | Idealizes then noises whole backbone frames | Independent per-atom noise lets the model memorize crystal artefacts | Clean structure → noised training input | [Paper: "LASErMPNN neural network"] | Not independently ablated in the main text |
| Expansion step | Samples ~1,000 sequences per structure at high softmax temperature | Escapes local minima in a rugged design landscape | Structure → sequence ensemble | [Paper: "NISE sampling algorithm"] | Not ablated; framed as necessary for exploration |
| Selection step | Keeps the top ~3 structures by ligand pLDDT | Ligand confidence is the only signal that tracks real binding | Predicted co-structures → next-round inputs | [Paper: "NISE sampling algorithm"] | **Ablated**: replacing the predictor with Rosetta energy minimization stops optimization (Fig. 1c) |
| Neural proofreading | Rescores single binding-site substitutions at low temperature | High-temperature design leaves each residue unrevisited in full context | Designed sequence → point mutations | [Paper: "Neural proofreading of the EPIC sequence"] | Post hoc; separable from NISE and separately validated |
| P(bind) composite score | Adds Boltz-2's binder/non-binder probability to ranking | Ligand pLDDT alone does not discriminate binders | Co-structure → composite rank | [Paper: "Design of apixaban binders using NISE"] | Used only in the apixaban campaign |

## 09 Essential Formulas and Symbols

The main text states no equations. The algorithm is described in probabilistic terms: NISE samples broadly from P(sequence | structure, ligand conformation) and takes a confidence-based argmax over P(structure, ligand conformation | sequence), which is characterized as iterative coordinate ascent toward a high-probability mode of the joint P(sequence, structure, ligand conformation). [Paper: "NISE sampling algorithm"] The ranking function that penalizes buried, non-hydrogen-bonded polar atoms is referenced but not written out in the main text.

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Held-out test-set sequence recovery | Is LASErMPNN a better designer? | Beats a ligand-free version of itself; **comparable to, slightly above, a retrained LigandMPNN** | Ligand conditioning helps | That LASErMPNN is the source of the hit-rate gain | [Paper: Fig. 2b] |
| Streptavidin fold held out by sequence, structure and evolution | Can it recover a fold it has never seen? | 53% binding-site recovery with biotin (36% for retrained LigandMPNN); top-25 designs reach **94%** recovery; Boltz-1 self-consistency **65% vs 13%** | Strong generalization to an unseen fold | That recovery predicts affinity | [Paper: "LASErMPNN neural network"; Fig. 2c; Extended Data Fig. 2] |
| PiB benchmark (held out from both networks) | Can it re-find a known designed binder? | Top-ranked design 74% binding-site / 80% core recovery; the real PiB sequence ranked 4th of 1,001 | The ranking scheme prioritizes good binders | Prospective success | [Paper: Fig. 2d] |
| NISE vs energy-based ISE | Is the co-structure predictor replaceable? | Rosetta-driven loop raises neither ligand pLDDT nor sequence likelihood over 35 rounds | The neural predictor is load-bearing | That Rosetta is useless generally | [Paper: Fig. 1c] |
| Exatecan binders, 4 NISE designs vs 16 COMBS designs | Zero-shot design success | **4/4 NISE bound** (Kd 0.12–17 µM); **3/16 COMBS bound** (best 8 µM); HSA control 43 µM | 100% success, ~70-fold tighter than the prior method | That 4 designs establish a rate | [Paper: Fig. 3f; "Characterization of exatecan binders"] |
| Neural proofreading of EPIC | Affinity maturation with no experimental input | Q51N **8.0 nM**, M97L **7.4 nM**, double mutant **1.2 nM** (100-fold over EPIC, additive); predicted-bad G104M **57 µM** | The likelihood is causally predictive in both directions | Generality beyond one protein | [Paper: Fig. 4c; Supplementary Fig. 20] |
| Crystal structures of EPIC (2.0 Å) and EPIC(Q51N) (2.2 Å) | Did it build what it designed? | Backbone Cα r.m.s.d. **0.8 Å** to the NISE input; ligand within ~1 Å and 14° after binding-site superposition; rotamers accurately predicted | Atomic-level design accuracy | That prediction errors are absent — RFAA mis-modelled the δ-lactone | [Paper: "Crystal structures of EPIC and EPIC(Q51N)"; Fig. 4d,e] |
| Hydrolysis protection | Functional consequence of burial | **>99% of exatecan stays ring-closed for ≥50 h**; holds with 500 µM HSA present; HSA alone does not protect | Designed burial delivers a real pharmacological function | In vivo stability | [Paper: "EPIC protects exatecan from hydrolysis"; Fig. 5d,e] |
| Apixaban, head-to-head on the same published NTF2 backbones | Fold- and target-generality vs a named competitor | **5/6 bound at Kd < 50 nM (83%)**; best **APEX Kd = 80 pM**. Prior LigandMPNN+Rosetta on the same backbones: **4 binders from 9,024 designs**, best 680 nM | Three-orders-of-magnitude better hit rate, ~10,000-fold better affinity | Equal compute or equal effort between the two campaigns | [Paper: "Design of apixaban binders using NISE"; Fig. 6e,f; Discussion] |
| APEX specificity | Is positive design enough for specificity? | No detectable exatecan binding; off-target ligand pLDDT and P(bind) stay low across the design lineage | Positive design sufficed here | Specificity against *similar* off-targets, which the authors say needs explicit negative design | [Paper: Fig. 6e; Discussion] |

## 11 Correct Interpretation of the Conclusions

- "100% success" is 4 of 4 designs tested; "83%" is 5 of 6. These are honest hit rates for the designs ordered, not estimates with confidence intervals. [Paper: Fig. 3f, Fig. 6e]
- The 10,000-fold affinity claim is a comparison of *best binder to best binder* across two campaigns, not a distributional comparison. The hit-rate comparison (5/6 vs 4/9,024) is the stronger of the two, because the backbones were identical. [Paper: Discussion]
- "Zero-shot" means no experimental feedback entered the design loop. Both campaigns still ended in wet-lab characterization; the crystal structures and Kd values are validation, not selection. [Paper: Discussion]
- LASErMPNN is **not** claimed to be a better sequence designer than LigandMPNN — the paper says they are comparable and interchangeable in aggregate metrics. The gain attributed to LASErMPNN specifically is reduced overpacking. [Paper: Fig. 2b; Discussion]
- The choice of co-structure predictor is consequential, not cosmetic: an RFAA-based assessment would have led the authors to discard the apixaban binders that Boltz-2 correctly kept. [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] "Maximizing model confidence and agreement was necessary but perhaps not sufficient by themselves"; downstream filtering on additional biophysical metrics was still required. [Paper: Discussion]
- [Paper] Positive design alone gave specificity against *dissimilar* off-targets; for similar on- and off-target molecules the authors state explicit negative design would be needed. [Paper: Discussion]
- [Paper] NISE is agnostic to the networks used and is bounded by them — RFAA would have discarded the apixaban binders, and RFAA struggled with the streptavidin β-barrel (0.4% self-consistency vs 65% for Boltz-1). [Paper: Discussion; "LASErMPNN neural network"]
- [Paper] RFAA mis-modelled the δ-lactone bond angles of exatecan, a discrepancy visible against the crystal structure. [Paper: "Crystal structures of EPIC and EPIC(Q51N)"]
- [Paper] Designs were seeded from two precomputed scaffold sets (helical bundles, NTF2); ligand-conditioned bespoke backbones are named as future work. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Success rates are 4/4 and 5/6 | Denominators this small cannot separate 83% from 50% | The headline number is the paper's main selling point and is quoted without an interval | Report a binomial confidence interval; test a pre-registered batch of ≥30 designs | [Paper: Fig. 3f, Fig. 6e] |
| The apixaban comparison reuses the competitor's backbones but not its compute budget | 9,024 designs synthesized vs 6 is a different experiment, not a slower one | A hit-rate ratio across unequal selection pressure overstates the method gap | Match designs-tested, or report cost per binder found | [Paper: "Design of apixaban binders using NISE"; Discussion] |
| Designs were chosen by "fewest buried non-hydrogen-bonded polar atoms" after pooling | A human-designed filter sits between the algorithm output and the ordered constructs | This filter is outside the loop, so "zero-shot" credit partly belongs to it | Order an unfiltered random sample from the same pool alongside the filtered picks | [Paper: "Design of exatecan binders using NISE"] |
| LASErMPNN ≈ LigandMPNN on metrics, yet the paper is titled for the network | Attribution drifts from the loop to the network | Readers may adopt the network and skip the loop, which is the part that was ablated as necessary | Run NISE with LigandMPNN end-to-end, wet-lab included | [Paper: Fig. 2b; Discussion] |
| Ligand pLDDT correlates with affinity for EPIC variants, but only weakly across the five apixaban binders | The optimization target may rank binders vs non-binders well and affinities poorly | NISE optimizes pLDDT directly; if it does not track affinity, later iterations buy less than assumed | Pre-register a pLDDT→Kd correlation on a held-out design set | [Paper: "Design of apixaban binders using NISE"; Extended Data Figs. 6, 7] |
| Exatecan has no PDB or CSD structure, and conformers were built by molecular mechanics | The starting ligand conformer is itself a model, and RFAA then distorted it | The design target's geometry is an assumption entering every round | Repeat NISE from several independently generated conformers | [Paper: "Exatecan design objective"; Extended Data Fig. 4] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: when two components are combined, ablate both — the one that cannot be swapped out is where the contribution lives, regardless of which one the title names.
- Agent-derived knowledge candidate: a design method's screen should be scored on the axis it is meant to control; backbone self-consistency passing while ligand placement fails is a warning that the screen is measuring the wrong thing.
- Agent-derived knowledge candidate: report hit rates as fractions with denominators, not percentages, when the denominator is under ten.
- Agent-derived knowledge candidate: a model that can predict which single mutation makes a protein *worse*, and is right, is providing stronger evidence than one that only predicts improvements.

## 15 Connections to Existing Knowledge

[Analysis] This work sits at the junction of two lines: the inverse-folding line (ProteinMPNN → LigandMPNN → LASErMPNN), from which it takes the sequence designer, and the co-folding line (RFAA, Boltz-1/2, AF3), from which it takes the scoring signal. Its contribution is the coupling rather than either endpoint, and it is explicitly benchmarked against the physics-based alternatives it displaces (COMBS/van der Mers, Rosetta minimization). The self-consistency principle it extends comes from de novo topology and protein-binder design; the novelty is adding the ligand as a third self-consistency axis. The paper positions ligand-conditioned generative backbone models (RFdiffusion-All Atom, BoltzDesign1, BoltzGen) as the natural next input stage. A priority comparison against concurrent co-folding-driven design methods was not attempted here.

## 16 Research Ideas

### Agent-derived research candidate

**Does the loop transfer, or only this pair of networks?** [Hypothesis] The NISE gain is a property of closed-loop reciprocal-conditional optimization, not of LASErMPNN, and will reproduce with any competent (inverse-folding, co-folding) pair. Delta: run four arms on one shared target set — LASErMPNN+Boltz-2, LigandMPNN+Boltz-2, LASErMPNN+AF3, LigandMPNN+AF3 — with identical scaffolds, identical iteration counts, identical post-filters, and identical numbers of constructs ordered. Validation: three ligands spanning the chemistry range (one PDB-abundant, one PDB-absent, one charged), ≥30 designs expressed per arm, affinity by fluorescence polarization, blinded Kd fitting. Falsifier: LigandMPNN arms match LASErMPNN arms within the confidence interval on hit rate *and* best affinity, which would place the contribution wholly in the loop; conversely, arms sharing a co-structure predictor diverging sharply would place it in the sequence designer. Failure modes: co-structure predictors differ in ligand-conformer handling, confounding the comparison; scaffold set biased toward one method's training distribution; expression failures correlated with arm. Innovation status: unverified; prior-art search required.
