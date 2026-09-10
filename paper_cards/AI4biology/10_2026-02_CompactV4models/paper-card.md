# Paper Card: Compact deep neural network models of the visual cortex

> Source coverage: Open-access full text via PubMed Central (PMC13359075), including all named result sections, Discussion and all main-figure captions
>
> Extraction confidence: High for the main text and figure captions; the 53k-character Methods, Extended Data figures 1–9 and Supplementary material are cited only where the main text describes them
>
> Locator mode: structure-grounded
>
> Primary analytical lens: Methods
>
> Secondary analytical lens: Experimental validation
>
> Context verification: Cross-checked against Crossref metadata and the authors' released code; this entry's routing question is addressed in 15
>
> Card completeness: Complete for the main text; Methods, Supplementary Figures 1–3, Supplementary Table 2 and Extended Data were not directly assessed

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| task-driven DNN | a network pretrained on object recognition, used as a fixed feature backbone | Prior art baseline; not trained on neural data |
| data-driven DNN | a network trained directly on neural responses | The other baseline; needs many images |
| hybrid deep ensemble | fixed task-driven backbone feeding an ensemble of trainable convolutional networks | The 60M-parameter "teacher"; the paper's high-accuracy model |
| compact model | a 5-layer network distilled from the ensemble and then pruned, one per neuron | The object of study; ~150 filters, ~10k parameters |
| consolidation step | the abrupt drop in filter count between layers 3 and 4 | The paper's central empirical claim about V4 |
| closed-loop / active learning | the model selects the next session's images by ensemble disagreement | The experimental design that produced the accuracy gain |
| noise-corrected R² | prediction accuracy normalized by trial-to-trial response reliability | The metric throughout; not comparable to raw R² |
| CKA | centered kernel alignment, similarity of two layers' representations up to linear rotation | Used to show early layers agree and outputs do not |
| DSI | dot size invariance index, from single-filter ablation | A purpose-built causal-in-the-model metric |

## 01 Basic Information

- **Title:** Compact deep neural network models of the visual cortex
- **Authors:** Benjamin R. Cowley, … , Matthew A. Smith (first and last author). [Paper: Metadata]
- **Venue / date:** *Nature*, 2026-02. [Paper: Metadata]
- **DOI:** [10.1038/s41586-026-10150-1](https://doi.org/10.1038/s41586-026-10150-1)
- **Code:** [cowleygroup/V4_compact_models](https://github.com/cowleygroup/V4_compact_models)
- **Data:** 44 recording sessions from **3 macaques**, ~50 simultaneously recorded V4 units per session via chronic multi-electrode array, ~2,000 unique images per session, ~78,000 unique images total; 4 held-out sessions (≥1 per animal) with new natural images. Additional public V1, V4 and IT datasets from other studies for the generality analysis. [Paper: "Compact models of V4 neurons"]
- **Access boundary:** the open-access full text was read via PMC. Methods, Extended Data Figs. 1–9, Supplementary Figures and Supplementary Table 2 were not opened directly.

## 02 One-Sentence Summary

[Paper] A 60-million-parameter hybrid ensemble trained on macaque V4 responses through closed-loop adaptive experiments is compressed by distillation plus pruning into per-neuron models with **5,000× fewer parameters** and only slightly lower accuracy; those compact models are small enough to read, and reading them reveals a shared early-layer basis followed by an abrupt "consolidation step" at which each neuron specializes — a motif that also holds for V1 and IT. [Paper: Abstract]

## 03 Research Question

- [Paper] "Have we simply replaced one complicated system in vivo with another in silico?" — can a model be both highly predictive of individual visual-cortical neurons and small enough for a human to understand? [Paper: Abstract]
- [Analysis] The question is unusual in that the object of study is the *model*, and the brain is the thing being explained. The paper's move is to treat compressibility as an empirical measurement about cortex rather than as an engineering convenience.

## 04 Research Background and Development Path

1. [Paper] Deep networks are the leading predictive models of visual cortex, but their computations are "buried beneath millions of parameters". [Paper: Abstract]
2. [Paper] Data-driven models (trained directly on neural responses) are unbiased but need long recordings from the same neuron, which is experimentally hard. [Paper: "Compact models of V4 neurons"]
3. [Paper] Task-driven models (ImageNet backbones) predict V4 well with fewer than 1,000 training images, but their features are not fitted to the neuron. [Paper: "Compact models of V4 neurons"]
4. [Paper] Combining both should do better, and doing so requires far more images than prior benchmark datasets contained. [Paper: "Compact models of V4 neurons"]
5. [Analysis] The development path runs through the *experiment*, not only the architecture. Active learning is what made ~78,000 image–response pairs affordable, and that dataset is what makes the data-driven half competitive at all.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence |
|---|---|---|---|
| Uninterpretable predictors | 60M parameters cannot be inspected | Model scale far exceeds what a human can hold | [Paper: "Compact models of V4 neurons"] |
| Recording instability | Same neuron cannot be held across long sessions | Chronic arrays drift; only a subset of units persist | [Paper: "Compact models of V4 neurons"] |
| Too few training images | Data-driven networks underperform task-driven ones | Prior benchmarks had insufficient image counts | [Paper: "Compact models of V4 neurons"] |
| Unvalidated preferred stimuli | Synthesized "maximizing images" often never tested in vivo | Requires returning to the same animal with new stimuli | [Paper: "Preferred features of compact models"] |
| Over-compression risk | Too much compression destroys interpretability | "One cannot easily infer an object in an image from its JPEG compressed values" | [Paper: "Compact models of V4 neurons"] |

## 06 Core Idea

- **Surface method:** knowledge distillation plus filter pruning applied to a neural-response predictor.
- **Core insight:** compression is used as a *measurement instrument*. How small a model can get while still predicting a neuron is a fact about that neuron's computation, and the layer-wise shape of the surviving network — many filters early, abruptly few after layer 3 — is an empirical result about cortex rather than an artefact of the compressor. The authors check exactly that, showing the trend "could not be explained by our method of pruning". [Paper: "A consolidation step for diverse tuning"; Supp. Fig. 3]
- **General lesson:** [Analysis] distillation makes small models reachable that direct training cannot reach — training the same 5-layer network directly on V4 data failed to beat a task-driven backbone. The large model is not the product; it is scaffolding that makes the small model trainable.

## 07 Method Overview

**Flow:** natural image → fixed task-driven backbone (ResNet50-family) → intermediate-layer features → trainable ensemble of convolutional DNNs → per-neuron linear readout → predicted spike response.

**Closed-loop training.** Across 44 sessions the model chose the next session's images by maximizing **ensemble disagreement**, supplemented with synthetic "gaudy images". Each neuron in each session received its own linear readout, so units that drifted between sessions did not have to be matched. [Paper: "Compact models of V4 neurons"]

**Compression, two stages.**
1. *Distillation* — the deep ensemble is the teacher; its predicted responses to **12 million natural images** train a 5-layer student (100 filters per layer).
2. *Pruning* — filters contributing little are ablated and the model retrained, stopping when accuracy falls 5% below the ensemble. One compact model per V4 neuron, ~150 filters and ~10k parameters. [Paper: "Compact models of V4 neurons"; Fig. 1d]

**Interpretation tools:** gradient-synthesized response-maximizing images; ε-perturbed images (bounded pixel change, maximizing or minimizing the model's output); CKA between layers of different compact models; single-filter ablation with the DSI index; cumulative ablation to isolate contributing filters.

**Main workflow figure:** Fig. 1a,d. No figure image is reproduced here; see `figure-analysis.md`.

## 08 Core Module Breakdown

| Module | Function | Why needed | Input → output | Evidence | Removal boundary |
|---|---|---|---|---|---|
| Fixed task-driven backbone | Supplies higher-order natural-image statistics | Priors that data alone cannot learn from 78k images | Image → features | [Paper: Fig. 1a] | Hybrid beats either pure approach by 30% |
| Trainable deep ensemble | Fits V4 responses; disagreement measures uncertainty | Avoids overfitting and supplies the active-learning signal | Features → predicted responses | [Paper: Fig. 1b] | Ensemble size ablated in Extended Data Fig. 1 |
| Closed-loop image selection | Chooses maximally informative next stimuli | Recording time is the scarce resource | Uncertainty → next session's images | [Paper: Fig. 1c] | **Ablated**: model-chosen + gaudy images beat randomly chosen natural images |
| Per-session per-neuron readout | Handles unit drift across sessions | Chronic arrays do not hold the same neurons | Shared features → one linear readout each | [Paper: "Compact models of V4 neurons"] | Sidesteps unit matching rather than solving it |
| Distillation on 12M images | Makes a small network trainable | Direct training of the same architecture on V4 data failed | Teacher predictions → student | [Paper: Fig. 1b,d] | **Load-bearing**: without it the compact architecture underperforms task-driven DNNs |
| Iterative pruning to 5% | Finds the smallest sufficient model | Compression is the measurement | Student → compact model | [Paper: Fig. 1d] | The 5% tolerance is a chosen threshold, not derived |
| Shallow-architecture constraint | Keeps the compressed model readable | Maximal compression would destroy interpretability | Constraint on search space | [Paper: "Compact models of V4 neurons"] | An explicit accuracy-for-interpretability trade |
| CKA across models | Tests whether early layers share a basis | Motivates the shared-core experiment | Two layers → similarity | [Paper: Fig. 3b] | Similarity high early, low at output (mean signal ρ² = 0.11) |
| Shared-core distillation | Asks how few filters serve a whole population | Tests reuse rather than per-neuron economy | Teacher → shared model | [Paper: Fig. 3c] | 5 filters/layer ≈ ResNet50; ~35 within 5% of the ensemble |
| DSI ablation | Localizes a specific selectivity to specific filters | Turns interpretability into a measurement | Ablate filter → invariance change | [Paper: Fig. 4c–e] | In-model causality; the circuit claim remains a hypothesis |

## 09 Essential Formulas and Symbols

No equations are stated in the main text. The quantitative apparatus is named: **noise-corrected R²** on held-out sessions as the accuracy metric; **CKA** (centered kernel alignment) for representational similarity, invariant to linear rotation, with 1 meaning identical; **ensemble disagreement** as the active-learning acquisition function; a **dot size invariance (DSI) index** defined by the authors, where ≈1 means a filter is necessary for dot-size selectivity and ≈0 means it contributes nothing; **ε-perturbation** with ε = 10 as average absolute pixel-intensity difference from the base image; and **paired permutation tests** for the layer-wise filter-count and CKA comparisons. Signal correlation between model outputs is reported as ρ² = 0.11. [Paper: Results; figure captions]

## 10 Experimental Design and Evidence Chain

| Experiment | Claim tested | Accessible result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|
| Hybrid vs task-driven vs data-driven | Does combining both help? | Hybrid ensemble **noise-corrected R² = 0.62** vs **0.48** for the best of either alone — a 30% gain | Task-driven features are a good prior that response data must refine | Generalization to other V4 datasets — tested separately and found merely *no worse* than the backbone | [Paper: Fig. 1b; Extended Data Fig. 2] |
| Closed-loop vs random images | Does active learning drive the gain? | Model-chosen plus gaudy images outperform randomly chosen natural images across sessions | Active learning is a main cause of the 30% boost | That it is the only cause — nonlinearities, session count and ensemble size also contribute | [Paper: Fig. 1c; Extended Data Fig. 1] |
| Compression | How small can a per-neuron model be? | Compact **R² = 0.55** vs ensemble 0.60 vs best task-driven 0.48, with **~5,000× fewer parameters** than the ensemble, ~500× fewer than ResNet50 | Most parameters are spurious or redundant for one neuron | That accuracy is preserved — 0.60 → 0.55 is a real loss, bounded by the 5% stopping rule | [Paper: Fig. 1e,f] |
| Preferred natural images, in vivo | Do model preferences transfer to the animal? | Model-selected natural images drove V4 responses above randomly chosen images | Preferences are real, not model artefacts | — | [Paper: Fig. 2b] |
| Synthesized maximizing images, in vivo | Do gradient-synthesized images work? | Synthesized images also drove responses well above random, **and** targeted specific neurons rather than the whole population | Model gradients point at real stimulus structure | Superiority over natural-image search — the paper finds them roughly equally effective | [Paper: Fig. 2c; Extended Data Figs. 4, 5] |
| ε-perturbation, in vivo | Do predictions hold near the natural-image manifold? | Perceptually near-identical images, perturbed to maximize or minimize model output, produced large V4 response changes in **both directions** as predicted | A strong within-distribution test | Complete model fidelity | [Paper: Fig. 2d–f] |
| Layer-wise filter counts | Is there structure in what survives pruning? | Layers 1–3 keep many filters, layers 4–5 few; the drop between 3 and 4 is significant (**p < 0.001**, paired permutation) and occurs at the same layer for almost all models | The consolidation step is a hallmark of V4 processing | An anatomical correspondence between model layers and cortical stages | [Paper: Fig. 3a; Supp. Fig. 3] |
| Pruning-artefact control | Is consolidation an artefact of the compressor? | "This trend could not be explained by our method of pruning" | The motif is a property of the fit, not the tool | — | [Paper: Supp. Fig. 3] |
| CKA across compact models | Do neurons share early computations? | Early-layer representations substantially more similar than late (**p < 0.001**); output similarity low, and lower still after controlling for receptive-field overlap | Shared basis early, specialization late | Shared anatomy — neurons were ≥400 μm apart and presumably read different V1/V2 inputs | [Paper: Fig. 3b] |
| Shared compact models | How few filters serve a population? | **5 filters per core layer** matches ResNet50 features; **~35** comes within 5% of the ensemble | V4 neurons reuse early computations despite diverse tuning | That ~200-neuron results extend to thousands — the Discussion says they likely do not | [Paper: Fig. 3c; Discussion] |
| Linear control | Are nonlinearities needed? | A same-architecture linear-activation model "performed poorly" | Nonlinearity is essential | — | [Paper: Fig. 3c] |
| No-distillation control | Is the teacher needed? | A compact model trained directly on V4 responses is also compressible but weaker | Distillation is what makes small models competitive | — | [Paper: Fig. 3c] |
| V1, V4, IT across datasets | Is compressibility general? | Compressible everywhere, ordered **V1 (~5 filters) < V4 (~10) < IT (~60)** | A hierarchy-consistent general principle | Equivalence of datasets and recording conditions across the three studies | [Paper: Fig. 3d–f] |
| DNN-unit control | Are all networks this compressible? | **DNN units from task-driven networks were not nearly as compressible** | Compressibility is specific to predicting neurons | — | [Paper: Extended Data Fig. 6] |
| BrainScore | External benchmark | Compact versions **outperform task-driven DNNs** with orders-of-magnitude fewer parameters | Independent confirmation | — | [Paper: Supp. Table 2] |
| Dot-detector dissection | Can a compact model be explained? | No layer-3 filter alone matters (DSI < 0.25) but layer-4 filter **L4F1 has DSI ≈ 1.0**; ~10 layer-3 filters contribute, of which 4 detect curvature at the dot's edge (excitatory) and 2 inhibit large oriented edges | Dot-size selectivity emerges *at* the consolidation step, by balanced excitation and inhibition | That real V4 circuits work this way — the paper calls it a testable hypothesis | [Paper: Fig. 4c–h; Extended Data Figs. 8, 9] |
| Replication across dot detectors | Is the mechanism idiosyncratic? | Other dot-detecting compact models "operated with almost identical computations" | The motif recurs | Generality beyond dot detection | [Paper: Extended Data Fig. 9] |

## 11 Correct Interpretation of the Conclusions

- Compression is measured **per neuron**. "5,000× fewer parameters" compares one compact model to the whole 60M-parameter ensemble that predicts many neurons at once; the shared-core analysis in Fig. 3c is the fairer population-level comparison. [Paper: Fig. 1f; Fig. 3c]
- Accuracy is not preserved under compression. R² falls from 0.60 to 0.55, and the pruning rule stops at exactly 5% loss — so the compression figure and the accuracy loss are two sides of one chosen threshold. [Paper: Fig. 1e]
- The "consolidation step" is a property of the *fitted compact models*, supported by a control showing pruning alone does not produce it. It is not an observation of cortical anatomy, and the paper does not claim layer 3 corresponds to any particular cortical stage.
- The dot-detector mechanism is established **inside the model** by ablation. Its status in the animal is a "testable circuit hypothesis", and the paper names the experiments that would test it — anatomical tracing, simultaneous V1/V2 and V4 recording, circuit perturbation. [Paper: Fig. 4h; Discussion]
- The in vivo validations are the strongest part of the paper: preferred stimuli, synthesized maximizing images and bidirectional ε-perturbations were all shown to the same animals and behaved as predicted. That is a much higher standard than reporting held-out R².
- Generality across V1, V4 and IT uses datasets from other studies with different recording conditions, so the ordering 5 < 10 < 60 filters is suggestive of a hierarchy rather than a controlled measurement of one.
- The authors state the compression result "likely will not hold true when predicting thousands of neurons with diverse feature selectivity". [Paper: Discussion]

## 12 Limitations Explicitly Acknowledged by the Authors

- [Paper] Compression was demonstrated for up to ~200 neurons together and "likely will not hold true when predicting thousands of neurons with diverse feature selectivity". [Paper: Discussion]
- [Paper] Repeat-to-repeat response variability "may conceal subtle computations that would otherwise increase model complexity". [Paper: Discussion]
- [Paper] "It is thus possible that an understanding of visual cortex in terms of conceptual, human-digestible diagrams … will not fully capture the complexity of visual processing in the brain." [Paper: Discussion]
- [Paper] The analysis focuses on predicting the recorded neurons "without regard to generalizing to other V4 neurons from other datasets". [Paper: "Compact models of V4 neurons"]
- [Paper] Synthesized maximizing images "may appear less crisp" than those from studies using large generative priors, attributed to colour and lower optimization resolution. [Paper: "Preferred features of compact models"]
- [Paper] The dot-detector result is presented as a circuit *hypothesis* requiring tracing, paired recordings and perturbation to confirm. [Paper: Discussion]

## 13 Critical Analysis

| [Analysis] Observation | Potential issue | Why it matters | Test | Basis |
|---|---|---|---|---|
| Pruning stops at exactly 5% accuracy loss below the ensemble | The compression ratio is a function of that tolerance, not an intrinsic property | "5,000×" is the headline number and it moves with a free parameter | Publish the full compression-versus-accuracy curve, and report the ratio at 1%, 5% and 10% | [Paper: "Compact models of V4 neurons"] |
| The consolidation step is located between layers 3 and 4 of a 5-layer student | Layer depth was fixed by design, so "where" consolidation happens is partly architectural | The claim that it occurs "at the same layer for almost all models" is less surprising if depth is fixed | Repeat with 4-, 6- and 8-layer students and check whether consolidation tracks relative depth or absolute layer | [Paper: Fig. 3a] |
| Every compact model is distilled from one shared teacher | Common ancestry could induce the shared early-layer representations that CKA then detects | The shared-basis conclusion is the paper's main claim about cortical reuse | Distill from independently trained teachers, or from data-driven models with no shared backbone, and re-measure CKA | [Paper: Fig. 3b] |
| Three animals, 44 sessions, ~200 neurons | The unit of replication is unclear — neurons within an animal are not independent | Confidence in "hallmark of V4 processing" depends on between-animal consistency | Report the layer-wise filter-count result per animal | [Paper: "Compact models of V4 neurons"] |
| V1/V4/IT comparison uses three external datasets | Recording method, stimulus set, image count and noise levels all differ across them | The hierarchy claim (5 < 10 < 60 filters) could reflect dataset quality rather than cortical complexity | Estimate compressibility as a function of training-set size within one dataset, then compare areas at matched data volume | [Paper: Fig. 3d–f] |
| Closed-loop image selection served both training and the accuracy comparison | Images were chosen to reduce this model's uncertainty, then the same model family is compared against baselines on those data | Baselines never got to choose their own training images | Give a task-driven-plus-readout baseline the same active-learning budget | [Paper: Fig. 1b,c] |
| DSI ablation establishes in-model necessity | Ablating a filter in a distilled student says nothing about a synapse in cortex | The dot-detector diagram is the paper's most vivid claim and the easiest to over-read | Already correctly framed as a hypothesis; the proposed V1/V2–V4 paired recordings are the right next step | [Paper: Fig. 4; Discussion] |
| Compact models reach R² = 0.55 against a noise ceiling | Roughly 45% of explainable variance is still unexplained | Interpretation is being performed on a model that captures a bit over half the signal | State explicitly what fraction of the neuron is being explained whenever a mechanism is read off the model | [Paper: Fig. 1e] |

## 14 Knowledge Learned

- Agent-derived knowledge candidate: compressibility can be an experimental measurement, not just an engineering step — how small a model can get while retaining accuracy is a quantitative claim about the system being modelled.
- Agent-derived knowledge candidate: when reporting compression, always publish the accuracy tolerance that terminated it; the ratio is meaningless without it.
- Agent-derived knowledge candidate: distillation reaches small models that direct training cannot. The large model can be scaffolding rather than product.
- Agent-derived knowledge candidate: active learning is most valuable when the scarce resource is measurement time rather than compute — the acquisition function should target the experiment, not the epoch.
- Agent-derived knowledge candidate: a bidirectional, near-distribution perturbation test (make the response go up *and* down with perceptually identical images) is a far stronger validation than a maximizing-stimulus test alone, because it cannot be passed by a model that has only learned overall drive.
- Agent-derived knowledge candidate: whenever a structural motif is read off a fitted model, run the control that asks whether the fitting procedure alone would produce it. This paper does, and the claim rests on that control.

## 15 Connections to Existing Knowledge

[Analysis] The work sits in the neural-prediction line running from Gabor and linear–nonlinear models through task-driven DNN encoders and the BrainScore benchmark, and it deliberately closes a loop back to the earlier era: the compact models are described as "akin to a cascade of LN filter models", and the ambition named in the Discussion is a diagram in the spirit of Hubel and Wiesel. Methodologically it borrows from the model-compression literature — knowledge distillation and structured pruning — and from adversarial and eigen-distortion work for the ε-perturbation test. The authors position it against concurrent studies that used distillation to improve V4 prediction without compressing, and against simplified models of V1 neurons and fMRI voxels.

*On this catalogue's routing question for this entry:* the full text confirms the record's own note without qualification. There is no molecular, genomic, proteomic or omic data of any kind — the measurements are extracellular spike responses from chronically implanted electrode arrays in three macaques, and the images are natural photographs. Nothing on an AI-for-biology page depends on it, and the `modalities` field is empty because the controlled vocabulary has no electrophysiology term to give it. The recommendation in the record — move it under CONTRIBUTING rule 7 — is supported. If it stays anywhere in the catalogue, a vocabulary term for electrophysiology has to be added first.

## 16 Research Ideas

### Agent-derived research candidate

**Is the shared early basis cortical, or inherited from the teacher?** [Hypothesis] The high CKA similarity among compact models' early layers — the evidence that V4 neurons reuse a common early representation — is substantially inflated because every compact model was distilled from the same 60M-parameter ensemble, which itself sits on one fixed ImageNet backbone; models distilled from independently constructed teachers will share far less, and the residual shared structure is the part attributable to cortex. Delta: build three or more teachers that differ in their inductive priors — different backbone families (ResNet, VGG, CORnet), different random initializations of the trainable ensemble, and at least one purely data-driven teacher with no ImageNet backbone at all — distil and prune compact models for the *same* V4 neurons from each, then recompute layer-wise CKA both within-teacher and across-teacher. Validation: the within-teacher CKA reproduces the published result and serves as the upper bound; the across-teacher CKA is the estimate of neuron-driven shared structure; repeat the shared-core experiment (filters per core layer needed to reach within 5% of each teacher) separately per teacher and check that the ~35-filter figure is teacher-invariant; run the same procedure on the public V1 and IT datasets to see whether the ordering survives. Falsifier: across-teacher CKA in early layers collapses toward the output-layer baseline, which would show the shared basis is an artefact of common ancestry rather than a property of V4, and would weaken the consolidation-step interpretation. Failure modes: a purely data-driven teacher may not reach comparable accuracy, making its compact models incomparable; CKA is sensitive to layer width and depth, so teachers must be matched in student architecture; pruning stochasticity may need many seeds per teacher to separate signal from run-to-run variation. Innovation status: unverified; prior-art search required.
