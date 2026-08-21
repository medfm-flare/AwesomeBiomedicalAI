# Figure Analysis: Compact deep neural network models of the visual cortex

Analysis of the four main figures, read from their published captions in the
open-access full text. **No figure image is reproduced.** The captions carry the
argument; the images are the publisher's and are not redistributed here. Open
them at the [article](https://www.nature.com/articles/s41586-026-10150-1) or on
[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13359075/) alongside this file.

## Fig. 1 — Identifying compact models

- **Argumentative role:** Carries the whole method and the headline number in one figure: the hybrid architecture, the closed-loop training gain, the compression procedure, and what survives it.
- **Panel logic:** Panel a is the hybrid — fixed task-driven backbone (blue) feeding a trainable ensemble (green). Panel b is the accuracy comparison that justifies the hybrid (0.62 vs 0.48). Panel c isolates the closed-loop contribution by plotting model-chosen and gaudy images against randomly chosen ones across sessions. Panel d is distillation-then-pruning. Panels e and f are the payoff: R² 0.55 for the compact model against 0.60 for the ensemble and 0.48 for the best task-driven DNN, at ~5,000× fewer parameters. **Panel g is the argument for the whole paper** — every filter of one compact model drawn in a single diagram.
- **Reusable design:** Panel g is the figure that earns the title. A compression ratio is an abstraction; showing that the resulting model fits on one page, in the same visual idiom used for LN filter models for decades, demonstrates interpretability rather than asserting it.
- **Reusable design (second):** Panels e and f are placed adjacent so accuracy and size are read together. Reporting either alone would be misleading in opposite directions.
- **Boundary:** Panel f's 5,000× compares one per-neuron compact model against the ensemble that predicts *many* neurons simultaneously. The like-for-like population comparison lives in Fig. 3c, not here. And the 0.60 → 0.55 accuracy loss is set by the pruning stopping rule, so the compression figure and the loss are one choice, not two findings.
- **Locator:** [Paper: Fig. 1a–g]

## Fig. 2 — Experimental validation in vivo

- **Argumentative role:** The credibility figure. Takes the model's claims back to the animal, which most encoding-model papers do not do.
- **Panel logic:** Three tests of increasing stringency. Panel b: response-maximizing images *selected from a 500,000-image database* drive V4 above randomly chosen images. Panel c: images *synthesized* by gradient ascent do the same. Panels d–f: ε-perturbed images — perceptually near-identical to a base image, ε = 10 in mean pixel intensity — drive responses **up or down** as the model predicts.
- **Reusable design:** The ε-perturbation test is the strongest of the three and the least common in this literature. A maximizing-stimulus test can be passed by any model that has learned roughly what excites a neuron; a bidirectional near-distribution test cannot, because it requires the model to be right about the local gradient in two directions from an ordinary image.
- **Reusable design (second):** The procedure is stated as a discipline — train on prior sessions, probe the model, then present the probes in a *subsequent* session. That ordering makes the validation prospective rather than a re-analysis.
- **Boundary:** Panel c's synthesized images are acknowledged to look less crisp than those from studies using large generative priors. The paper argues that is a feature — a strong image prior can "embellish" a maximizing image, synthesizing elaborate eyes for a neuron that merely prefers two dots — which is a fair point but also means these images are not directly comparable to published ones.
- **Locator:** [Paper: Fig. 2a–f; Extended Data Figs. 3–5]

## Fig. 3 — The consolidation step, and generality

- **Argumentative role:** Turns compression from an engineering result into a claim about cortex.
- **Panel logic:** Panel a plots filters per layer after pruning, one line per model: many in layers 1–3, abruptly few in 4–5, with the drop between 3 and 4 significant at p < 0.001 and occurring at the same layer for nearly all models. Panel b uses CKA to show early layers are similar across models while outputs are not (mean signal ρ² = 0.11, and lower still after controlling for receptive-field overlap). Panel c asks how few filters a *shared* core needs — 5 per layer to match ResNet50 features, ~35 to come within 5% of the ensemble — and includes two controls in the same axes: a linear-activation model that fails, and a no-distillation model that underperforms. Panels d–f repeat the shared-core analysis for V1, V4 and IT from other studies, giving ~5, ~10 and ~60 filters.
- **Reusable design:** Panels a and b make a two-step argument that neither alone would support. Panel a says the *architecture* narrows; panel b says the wide part is *shared* and the narrow part is *individual*. Together they license the interpretation that specialization happens at the consolidation step.
- **Reusable design (second):** Putting the linear and no-distillation controls inside panel c, on the same axes as the main curve, means the reader sees what the result is being compared against without turning a page.
- **Boundary:** The student's depth was fixed at five layers, so "consolidation between 3 and 4" is partly a statement about a chosen architecture. The control that matters — that pruning alone does not produce this shape — is in Supplementary Fig. 3, not here. Panels d–f pool three datasets from different studies with different recording conditions, so the 5 < 10 < 60 ordering is suggestive of hierarchy rather than a controlled measurement.
- **Locator:** [Paper: Fig. 3a–f; Supp. Fig. 3; Extended Data Fig. 6]

## Fig. 4 — Dissecting a dot detector

- **Argumentative role:** The demonstration that a compact model can actually be explained, end to end, in mechanistic terms.
- **Panel logic:** Panel a shows the chosen model's preferred stimuli, panel b its dot-size tuning. Panel c defines the DSI index through two contrasting single-filter ablations. Panel d gives DSI across all filters — the striking result being that **no layer-3 filter individually exceeds 0.25 while layer-4 filter L4F1 reaches ≈1.0**. Panel e uses cumulative ablation to isolate the ~10 layer-3 filters that feed it. Panels f and g are the mechanism: for a small dot, four curvature-detecting filters produce spatially overlapping positive activity while two large-edge-inhibitory filters stay quiet; for a large dot, the four no longer overlap and the two inhibit strongly. Panel h condenses this into a circuit diagram.
- **Reusable design:** Panel d's structure — nothing individually necessary in one layer, one thing necessary in the next — is exactly the signature of a readout, and it makes the consolidation-step hypothesis testable rather than descriptive. Devising a task-specific invariance index (DSI) rather than reusing a generic attribution method is what makes the ablation interpretable.
- **Reusable design (second):** Panels f and g are the same analysis run on two stimuli chosen to differ in the one variable of interest. Showing the mechanism *and* the condition under which it fails to fire is what distinguishes an explanation from an illustration.
- **Boundary:** Every causal statement here is causal *within the model*. Ablating a distilled filter is not perturbing a cortical circuit. The paper is explicit that panel h is a testable hypothesis, and names tracing, paired V1/V2–V4 recordings and circuit perturbation as the tests. Note also that the model being dissected explains R² ≈ 0.55 of a noise-corrected ceiling, so roughly 45% of the neuron's explainable response is outside this diagram.
- **Locator:** [Paper: Fig. 4a–h; Extended Data Figs. 7–9]

## Extended Data

Extended Data Fig. 1 (ensemble size, session count and nonlinearity contributions), Fig. 2 (comparison of noise-corrected R² against prior studies, and cross-dataset generalization), Figs. 4–5 (further in vivo validation, including neuron specificity and saliency maps), Fig. 6 (compressibility of V1/V4/IT and of task-driven DNN units, which are notably *less* compressible) and Figs. 7–9 (real dot detectors and replication of the mechanism in other models) carry claims cited in the card but were not opened directly.

## Cross-figure reading rule

Fig. 1g first — one page holding every filter of a model that predicts a V4 neuron is the paper's thesis in a single panel. Then Fig. 2d–f, the ε-perturbation validation, which is the strongest evidence that the models are right about real neurons rather than merely fitting them. Fig. 3a and 3b must be read together, since neither the narrowing nor the sharing means much alone. Fig. 4 is the payoff but should be read with two boundaries held in mind: the causality is in-model, and the model captures a bit over half the explainable response.
