# Figure Analysis: Zero-shot design of drug-binding proteins via neural iterative selection−expansion

Analysis of the six main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41586-026-10670-w) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13441969/) alongside this file.

## Fig. 1 — The self-consistency optimization algorithm

- **Argumentative role:** Defines the contribution before any result. Panel a introduces the third self-consistency axis — not just "does the sequence fold back to the backbone", but "does the ligand land where it was meant to".
- **Panel logic:** Panel a is conceptual, b is the loop, **c is the ablation**, d is the probabilistic justification. Panel c is the one that matters: NISE and an energy-based loop are run side by side for 35 rounds, and only NISE improves both ligand pLDDT and sequence likelihood. Read c before b.
- **Reusable design:** Putting the negative control (Rosetta-driven ISE) in the *method* figure rather than in supplementary material forces the reader to see immediately which component is load-bearing.
- **Boundary:** Panel c is one trajectory on one input structure. It shows the energy-based loop fails to optimize the neural metrics; it does not show Rosetta fails at its own objective.
- **Locator:** [Paper: Fig. 1a–d]

## Fig. 2 — LASErMPNN and its held-out benchmarks

- **Argumentative role:** Establishes the sequence designer is competent — and, read carefully, that it is *not* dramatically better than what came before.
- **Panel logic:** Panel b is two comparisons: against a ligand-free ablation of itself (a large gap, ligand conditioning works) and against a retrained LigandMPNN (comparable, slightly ahead). Panels c and d are the strict held-out tests — streptavidin excluded by sequence, structure and evolutionary similarity; PiB excluded from both LASErMPNN's and RFAA's training sets.
- **Reusable design:** The streptavidin holdout is the model of a good negative-control benchmark: a fold famous enough that recovering it is meaningful, excluded on three independent axes so the holdout cannot leak.
- **Boundary:** Sequence recovery is agreement with a native sequence, not affinity. The 94% figure in panel c is the best of 10,000 designs, selected by a ranking function — a ceiling, not an expectation.
- **Locator:** [Paper: Fig. 2a–d]

## Fig. 3 — The exatecan campaign

- **Argumentative role:** First prospective result, and the direct head-to-head against the physics-based predecessor.
- **Panel logic:** Panels b and c show the same starting pose taken down two paths (COMBS/Rosetta vs NISE), which is what makes the comparison fair. Panel d shows what NISE actually changed structurally — a 3₁₀ helix regularized, the helix–helix interface narrowed, superhelical radius 7.5 Å → ~7.2 Å, ligand drawn deeper. Panel f is the payoff: EPIC at 0.12 µM against the best traditional design at 8 µM and HSA at 43 µM. Panels g and h test specificity across the camptothecin series.
- **Reusable design:** Panel d is the rare "what did the optimizer do" panel. Most design papers report only the endpoint; showing the structural delta makes the mechanism auditable.
- **Boundary:** Panel f compares four NISE designs against sixteen COMBS designs. The affinity gap is real; the success-rate gap rests on a denominator of four.
- **Locator:** [Paper: Fig. 3b–h]

## Fig. 4 — Neural proofreading, and the crystal structures

- **Argumentative role:** Carries two distinct claims that are worth separating — that the model can improve its own design without experiment (a–c), and that the design was built as intended (d–f).
- **Panel logic:** Panel b shows the proofreading mechanism: rescore each binding-site residue at low temperature in full sequence context. Panel c reports the result — Q51N 8.0 nM, M97L 7.4 nM, additive at 1.2 nM. Panels d–f are the 2.0 Å and 2.2 Å crystal structures; panel f explains the affinity gain mechanistically, with Asn51's shorter side chain drawing exatecan ~0.5 Å deeper into a bidentate hydrogen bond.
- **Reusable design:** The strongest evidence in the figure is not in it — the G104M mutant, predicted to *lose* affinity and measured at 57 µM, is in supplementary material. A prediction that is right in the losing direction rules out selection effects far better than another win.
- **Boundary:** Panels d–f validate one designed protein and one point mutant. Crystallographic agreement here does not generalize to the other designs, which were not crystallized.
- **Locator:** [Paper: Fig. 4a–f]

## Fig. 5 — Hydrolysis protection

- **Argumentative role:** Moves the claim from binding to function. This is the figure that makes the design useful rather than merely accurate.
- **Panel logic:** Panel c states the thermodynamic argument as two competing schemes — EPIC buries the lactone and shifts the equilibrium, HSA binds but leaves the ring exposed. Panels d and e test it: exatecan alone converts within ~6 h, HSA does not prevent it, EPIC(Q51N/M97L) holds >99% ring-closed for at least 50 h.
- **Reusable design:** Including HSA as a binding-but-not-protecting control separates "binds the drug" from "protects the drug", which a simple affinity panel would have conflated.
- **Boundary:** PBS at room temperature, plus one experiment at physiological HSA concentration. Nothing here is an in vivo or plasma-stability result.
- **Locator:** [Paper: Fig. 5a–e]

## Fig. 6 — The apixaban campaign

- **Argumentative role:** Generality across fold and target, and the paper's cleanest competitive comparison, because the NTF2 backbones are the *same published backbones* a LigandMPNN+Rosetta study used for the same ligand.
- **Panel logic:** Panel b is the scaffold set (50 NTF2 folds), c the NISE trajectories, d the predicted APEX pocket with main-chain and side-chain hydrogen bonds including a Cα hydrogen bond via glycine. Panels e and f give APEX at 80 pM for apixaban with no detectable exatecan binding.
- **Reusable design:** Reusing a competitor's published scaffolds is the strongest form of head-to-head available without rerunning their pipeline. It removes the "you had better starting points" objection entirely.
- **Boundary:** It does not remove the compute-and-scale objection: six designs tested here against 9,024 there. The hit-rate ratio is not a like-for-like efficiency measurement.
- **Locator:** [Paper: Fig. 6a–f]

## Extended Data

Extended Data Fig. 1 (LigandMPNN overpacking), Fig. 2 (streptavidin holdout head-to-head), Figs. 6–8 (whether ligand pLDDT and Boltz-2 P(bind) track measured affinity) and Extended Data Table 1 (the LASErMPNN ablations) carry claims cited in the card but were not opened directly; they are referenced only as the main text describes them.

## Cross-figure reading rule

Read Fig. 1c first — it is the ablation, and it establishes that the co-structure predictor is the component that cannot be removed. Then Fig. 2b, which quietly shows the sequence designer is roughly at parity with its predecessor. Those two panels together locate the contribution in the loop rather than the network, which is the reading the rest of the figures support. Figs. 3 and 6 are the two prospective campaigns; Fig. 4 is affinity maturation plus structural proof; Fig. 5 is the only figure about what the protein is *for*.
