<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from data/LLM.yaml in https://github.com/1nslyn/biomedical-ai-pipeline -->
<!-- Edits made here are overwritten by the next build. -->

# Large Language Models

Top foundational and recent research papers on medical large language models (LLMs) focusing on clinical knowledge encoding, multi-modal integration, reasoning benchmarks, and expert-level question-answering alignment.

**Maintainer:** [Leo Chen](https://github.com/leochenmd)

**24 entries**

| Date | Paper | Journal | Summary | Datasets/Models | Pre-training | Downstream tasks | NotebookLM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026.08 | [Divergent impacts of explainable AI for dermatological diagnosis on clinicians versus lay people](#model-dermatology-xai-human-factors-study-cdann-gpt-4v-202608) | Nat. Med. | LLM explanations were a double-edged sword for diagnostic accuracy, while fairness-constrained training reduced skin-tone disparities for lay users and physicians. | 108,585 images | supervised | classification, diagnosis | — |
| 2026.08 | [A clinically validated framework for auditing AI chatbot behavior in mental health interactions](#model-sim-vail-202608) | Nat. Med. | A validated framework audits nine chatbots for mental-health safety, finding widespread concerning behavior that eased in newer models. | 810 conversations | — | benchmarking, risk prediction | — |
| 2026.06 | [Towards conversational artificial intelligence for disease management](#model-amie-disease-management-202606) | Nature | AMIE's successor was non-inferior to twenty-one primary care physicians on multivisit disease management and outperformed them on hard medication-reasoning questions. | 100 case scenarios | supervised, reinforcement learning | diagnosis, treatment response, question answering +1 | — |
| 2026.06 | [Generative AI-enabled clinical decision support system in primary care: a pragmatic, cluster-randomized trial](#model-ai-consult-v2-0-202606) | Nat. Med. | A GPT-4o-based decision support tool in a Kenyan primary-care trial did not reduce treatment failure; it caused no safety signal. | 9,691 patients | — | clinical decision support, diagnosis, treatment response | — |
| 2026.06 | [BRIDGE: benchmarking large language models for understanding real-world clinical practice texts](#model-bridge-202606) | Nat. Biomed. Eng. | A multilingual NLP benchmark spanning 87 tasks and 95 LLMs found open-source models matching proprietary ones, outperforming older medical fine-tunes. | 87 tasks, 95 models | — | triage, information extraction, diagnosis +3 | — |
| 2026.06 | [Evaluating the robustness and readiness of large frontier models in health AI applications](#model-health-ai-robustness-stress-test-suite-202606) | Nat. Med. | Adversarial stress tests on ten frontier models exposed brittle reasoning and fabricated explanations behind popular health AI benchmarks. | 10 models tested | — | benchmarking, reasoning | — |
| 2026.06 | [General-purpose large language models outperform specialized clinical AI tools on medical benchmarks](#model-frontier-llm-vs-clinical-ai-tool-benchmark-202606) | Nat. Med. | Frontier LLMs (GPT-5.2, Gemini 3.1 Pro, Claude Opus 4.6) beat specialized clinical AI tools (OpenEvidence, UpToDate) across three medical benchmarks. | 1,800 clinician annotations | — | question answering, benchmarking, reasoning | — |
| 2026.05 | [Advancing conversational diagnostic AI with multimodal reasoning](#model-multimodal-amie-202605) | Nat. Med. | A multimodal extension of AMIE, built on Gemini 2.0 Flash, outperformed primary care physicians on 29 of 32 evaluation axes. | 105 telehealth cases | — | diagnosis, reasoning, question answering | — |
| 2026.05 | [A cognitive layer architecture to support large-language model performance in psychotherapy interactions](#model-cognitive-layer-architecture-psychotherapy-llm-202605) | Nat. Med. | A cognitive layer architecture, tested across GPT-4, Claude, Gemini and Llama 3, outperformed standalone LLMs and human clinicians on CBT competencies. | 19,674 transcripts | — | clinical decision support, reasoning, question answering | — |
| 2026.04 | [Performance of a large language model on the reasoning tasks of a physician](#model-llm-physician-reasoning-evaluation-202604) | Science | OpenAI's o1-preview outperformed physician baselines and GPT-4 across five diagnostic reasoning experiments and a real-world emergency room comparison. | hundreds of physicians | — | diagnosis, reasoning, benchmarking | — |
| 2026.04 | [Graph augmented transformers improve chemotherapy toxicity symptom extraction from clinical notes](#model-gat-cn-202604) | Nat. Commun. | GAT-CN combines Bio+ClinicalBERT embeddings with graph neural networks to extract chemotherapy toxicity symptoms, reaching 0.850 weighted AUROC. | 1,753 patients | — | classification, clinical decision support | — |
| 2026.03 | [Grounding large language models in clinical diagnostics](#model-clindiag-gpt-202603) | Nat. Commun. | ClinDiag-GPT, fine-tuned for full diagnostic workflows, outperformed GPT-4o, Claude-3-Haiku and Qwen2.5 baselines on a 4,421-case benchmark. | 4,421 clinical cases | — | diagnosis, reasoning, benchmarking | — |
| 2026.03 | [TrialMatchAI: an end-to-end AI-powered clinical trial recommendation system to streamline patient-to-trial matching](#model-trialmatchai-202603) | Nat. Commun. | TrialMatchAI, built on fine-tuned Gemma-2-2b and Phi-4 models with retrieval-augmented reasoning, retrieved a relevant trial for 92% of oncology patients. | 92% patients matched | — | clinical decision support, reasoning, classification | — |
| 2026.03 | [A clinical environment simulator for dynamic AI evaluation](#model-clinical-environment-simulator-ces-202603) | Nat. Med. | A proposed Clinical Environment Simulator evaluates LLMs within dynamic digital hospital environments, testing temporal reasoning, resource tradeoffs and resilience. | — | — | reasoning, benchmarking, planning | — |
| 2026.03 | [An LLM chatbot to facilitate primary-to-specialist care transitions: a randomized controlled trial](#model-prea-202603) | Nat. Med. | PreA, an LLM chatbot for primary-to-specialist transitions, cut physician consultation time by 28.7% and significantly improved care coordination. | 2,069 patients | — | diagnosis, patient communication, clinical decision support | — |
| 2026.02 | [A large language model for complex cardiology care](#model-amie-articulate-medical-intelligence-explorer-202602) | Nat. Med. | AMIE, built on Gemini 2.0 Flash, helped cardiologists outperform unassisted peers on complex cases, though it occasionally hallucinated self-corrected findings. | 107 patient cases | — | triage, diagnosis, treatment response | — |
| 2026.02 | [Reliability of LLMs as medical assistants for the general public: a randomized preregistered study](#model-llm-medical-assistant-human-factors-rct-202602) | Nat. Med. | An RCT found LLMs diagnose accurately alone, but public users of the same LLMs performed no better than unassisted controls. | 1,298 participants | — | diagnosis, triage | — |
| 2026.02 | [ChatGPT Health performance in a structured test of triage recommendations](#model-chatgpt-health-202602) | Nat. Med. | A stress test of ChatGPT Health, built on gpt-5-mini, found systematic under-triage of emergencies and anchoring bias from family framing. | 960 responses | — | triage | — |
| 2026.02 | [Scaling medical AI across clinical contexts](#model-context-switching-perspective-202602) | Nat. Med. | A perspective paper proposes inference-time context switching, adjusting reasoning without retraining, as a scalable alternative to fine-tuning for clinical AI. | — | — | question answering, report generation, planning | — |
| 2026.01 | [A community-codesigned LLM-powered chatbot for primary care: a randomized controlled trial](#model-p-p-care-202601) | Nat. Health | A GPT-4o-mini-powered chatbot, codesigned with Chinese community stakeholders, significantly improved health awareness in a 2,113-participant randomized trial. | 2,113 participants | — | patient communication, question answering | — |
| 2026.01 | [MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks](#model-medhelm-202601) | Nat. Med. | A clinician-validated LLM benchmark found DeepSeek R1 and o3-mini leading, with Claude Sonnet close behind at meaningfully lower computational cost. | 121 tasks, 9 models | — | clinical decision support, clinical note generation, patient communication +3 | — |
| 2025.12 | [A large language model for clinical outcome adjudication from telephone follow-up interviews: a secondary analysis of a multicenter randomized clinical trial](#model-fu-llm-202512) | Nat. Commun. | Fu-LLM, fine-tuned from Qwen2-7B, automated clinical-trial outcome adjudication, outperforming GPT-4o, Claude 3.5 Sonnet, Gemini and human adjudicators. | 1,046 vignettes | supervised | clinical decision support, classification | — |
| 2025.10 | [LINS: A general medical Q&A framework for enhancing the quality and credibility of LLM-generated responses](#model-lins-202510) | Nat. Commun. | LINS, a retrieval-augmented medical Q&A framework, improved LLM response credibility, helping resident physicians in 87% of evidence-based scenarios. | 15,530 questions | — | question answering, clinical decision support | — |
| 2025.09 | [A foundation model for human-AI collaboration in medical literature mining](#model-leads-202509) | Nat. Commun. | LEADS, a foundation model trained on 633,759 literature-mining samples, improved recall and extraction accuracy while saving 20-27% of review time. | 633,759 samples | — | question answering, benchmarking, classification | — |

## Details

Click a model to expand its record.

<a id="model-dermatology-xai-human-factors-study-cdann-gpt-4v-202608"></a>
<details>
<summary><b>Dermatology XAI human-factors study (CDANN + GPT-4V)</b> — Divergent impacts of explainable AI for dermatological diagnosis on clinicians versus lay people <i>(Nat. Med. 2026-08)</i></summary>

**[Divergent impacts of explainable AI for dermatological diagnosis on clinicians versus lay people](https://www.nature.com/articles/s41591-026-04553-w)**

*Nat. Med.* · 2026-08 · Xuhai 'Orson' Xu & Marzyeh Ghassemi · [doi:10.1038/s41591-026-04553-w](https://doi.org/10.1038/s41591-026-04553-w)

| | |
| --- | --- |
| **Summary** | • LLM-generated explanations (GPT-4V) boosted diagnostic accuracy more than other XAI methods when the AI was right, but hurt it most when the AI was wrong -- a "double-edged sword" effect.<br>• A fairness-constrained diagnostic model (CDANN) narrowed skin-tone accuracy disparities by ~47% for lay people and ~36% for physicians.<br>• Experienced PCPs were more resilient to misleading AI explanations than lay users, who showed stronger automation bias. |
| **Models** | ViT-B/32 trained with CDANN (conditional domain adversarial neural network) fairness-constrained training for study 1's binary nevus/melanoma classification; DenseNet-121 for study 2's differential diagnosis (5-class primary + 30-class secondary). Post hoc explanations (GradCAM, CBIR, and a multimodal LLM -- GPT-4V) generated from the same trained models' outputs; the paper studies XAI's effect on human diagnostic decisions rather than introducing a new diagnostic model architecture. |
| **Downstream tasks** | `classification`, `diagnosis`<br>Randomized 4x2 factorial study (4 XAI methods: basic, GradCAM, CBIR, multimodal-LLM x 2 decision paradigms: Human-First, AI-First) measuring how explanation type and decision order affect diagnostic accuracy, automation bias and anchoring bias, comparing lay people against experienced PCPs. |
| **Modalities** | `clinical photography`, `text` |
| **Pre-training** | `supervised`<br>Supervised training with a CDANN domain-adversarial fairness constraint across skin tones (study 1) and standard supervised training (study 2, DenseNet-121). GPT-4V used off-the-shelf for explanation generation, not fine-tuned. |
| **Data** | 108,585 clinical dermatology images (16 combined public/private datasets) spanning multiple skin tones and conditions (nevus, melanoma, atopic dermatitis, pityriasis rosea, Lyme disease, CTCL, others), with 18,265 images carrying expert-annotated Fitzpatrick skin-tone labels. Evaluated via two human studies: 623 lay people (binary nevus/melanoma task) and 153 primary care physicians plus 320 medical students (differential diagnosis task).<br>**108,585** images · **18,265** images with fitzpatrick labels · **623** lay participants · **153** physicians · **320** medical students |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| PCP differential diagnosis, top-1 / top-3 accuracy with AI assistance | accuracy increase over no-AI baseline | top-1 +21.4pp (from 11.5%), top-3 +43.5pp (from 16.1%) |  |
| General public nevus/melanoma detection with AI assistance | accuracy increase | +6.1pp (69.7% to 75.8%) |  |
| Skin-tone diagnostic accuracy disparity, with vs. without fairness-constrained AI | relative reduction in disparity | 46.9% (general public), 35.6% (PCPs) | general public disparity 3.2% to 1.7%; PCP disparity 4.5% to 2.7% |
| Binary nevus/melanoma classifier (ViT-B/32 + CDANN) | weighted AUROC | 0.93 | 0.933 light skin / 0.898 dark skin (Delta = 0.035) |
| LLM (GPT-4V) explanation effect on general public accuracy | accuracy change vs. no explanation | +7.7% when AI correct-leaning trust; -21.1% when AI incorrect | largest swing of the four XAI methods in both directions -- the paper's "double-edged sword" finding |

</details>

<a id="model-sim-vail-202608"></a>
<details>
<summary><b>SIM-VAIL</b> — A clinically validated framework for auditing AI chatbot behavior in mental health interactions <i>(Nat. Med. 2026-08)</i></summary>

**[A clinically validated framework for auditing AI chatbot behavior in mental health interactions](https://www.nature.com/articles/s41591-026-04577-2)**

*Nat. Med.* · 2026-08 · Veith Weilnhammer & Matthew M. Nour · [doi:10.1038/s41591-026-04577-2](https://doi.org/10.1038/s41591-026-04577-2)

| | |
| --- | --- |
| **Summary** | • A clinically validated auditing framework simulates vulnerable users in multi-turn conversations to test 9 frontier chatbots for mental-health safety failures.<br>• Concerning behavior was widespread across all 9 chatbots tested (Claude, GPT, Gemini, Grok, Llama), though reduced in newer model versions.<br>• Risk was highest in a pattern the authors call a VAIL, when supportive-seeming chatbot behavior reinforces the user's underlying psychological vulnerability. |
| **Models** | An auditing framework, not a trained model. A claude-sonnet-4.5 auditor LLM simulates vulnerable users against nine target chatbots (claude-sonnet-3.7, claude-sonnet-4.5, gemini-2.5-flash, gemini-2.5-pro, llama-3.1-70b-instruct, gpt-4o, gpt-5, grok-3, grok-4, accessed via OpenRouter), scored by an automated safety judge (claude-opus-4.5 for conversation-level scores, claude-sonnet-4.5 for turn-level scores). |
| **Downstream tasks** | `benchmarking`, `risk prediction`<br>Audits mental-health safety behavior of nine frontier consumer AI chatbots via simulated vulnerable users across 30 vulnerability x intent profiles. Concerning behavior was widespread across target chatbots (reduced in newer models), accumulated over conversation turns, and was highest when otherwise-supportive chatbot behavior reinforced the psychological mechanism underlying the simulated vulnerability -- a pattern the authors term a VAIL. |
| **Modalities** | `text` |
| **Data** | 810 simulated multi-turn conversations (30 clinically grounded user profiles x 9 target chatbots x 3 repetitions), spanning 6,329 turns; over 10,000 conversation-level and 90,000 turn-level mental-health risk ratings across 13 clinically grounded risk dimensions. Validated against 488 turn-level ratings from 27 clinician annotators.<br>**810** conversations · **6,329** turns · **30** user profiles · **9** target chatbots · **27** clinician annotators |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Safety-judge inter-judge agreement (claude-opus-4.5 vs. gpt-5.2) | correlation | r = 0.91 |  |
| Safety judge vs. curated high/low-risk conversations | median AUC | 0.98 |  |
| Human-LLM vs. human-human turn-level agreement (27 clinician annotators, 488 ratings) | correlation | human-LLM r=0.49 vs. human-human r=0.41 | automated ratings were at least as reliable as an independent clinical judgment |
| Simulated-conversation realism (27 clinician annotators) | rated "broadly plausible" or "reads as genuine" | 80% (36% + 44%) | only 1% rated "clearly artificial" |

</details>

<a id="model-amie-disease-management-202606"></a>
<details>
<summary><b>AMIE (disease management)</b> — Towards conversational artificial intelligence for disease management <i>(Nature 2026-06)</i></summary>

**[Towards conversational artificial intelligence for disease management](https://www.nature.com/articles/s41586-026-10764-5)**

*Nature* · 2026-06 · Valentin Liévin & Mike Schaekermann · [doi:10.1038/s41586-026-10764-5](https://doi.org/10.1038/s41586-026-10764-5)

| | |
| --- | --- |
| **Summary** | • AMIE's successor extends diagnostic dialogue to multivisit disease management -- treatment planning, monitoring and medication reasoning grounded in clinical guidelines via Gemini's long-context retrieval.<br>• In a randomized blinded OSCE study, AMIE was non-inferior to 21 PCPs and scored better on treatment preciseness and guideline grounding.<br>• On RxQA, a new drug-formulary reasoning benchmark, AMIE outperformed PCPs on the hardest medication questions. |
| **Models** | LLM-based agentic system built on Gemini 2.5 Flash (evolved from earlier AMIE versions built on Gemini 1.5 Flash), combining long-context in-context retrieval of clinical guidelines and drug formularies with structured reasoning, agent scaffolding, and reinforcement learning from human/AI feedback for multivisit management dialogue. |
| **Downstream tasks** | `diagnosis`, `treatment response`, `question answering`, `planning`<br>Multivisit disease-management reasoning (treatment planning, investigation selection, guideline-grounded monitoring and plan adjustment) compared against 21 PCPs in a randomized blinded OSCE; separately benchmarks medication/drug-formulary reasoning via RxQA. |
| **Modalities** | `text` |
| **Pre-training** | `supervised`, `reinforcement learning`<br>Dialogue agent trained via supervised fine-tuning plus reinforcement learning from human/AI feedback (reward model on human and LLM preferences), with an agentic "Mx" management-reasoning module performing guideline retrieval, draft generation, critique and revision, layered on the Gemini 2.5 Flash long-context backbone. |
| **Data** | Randomized, blinded virtual OSCE study: 100 multivisit case scenarios across five medical specialties (built from UK NICE guidance and BMJ Best Practice guidelines), AMIE vs. 21 primary care physicians, evaluated by specialist physicians and patient actors. Medication reasoning separately benchmarked via RxQA, a multiple-choice question set derived from US and UK national drug formularies and validated by board-certified pharmacists.<br>**100** case scenarios · **5** medical specialties · **21** pcps |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| OSCE management reasoning, AMIE vs. 21 PCPs (100 multivisit cases, 5 specialties) | specialist-assessed outcome | non-inferior overall; better on treatment/investigation preciseness and guideline grounding |  |
| RxQA medication reasoning, higher-difficulty subset (pharmacist-rated) | accuracy vs. PCPs | AMIE outperformed PCPs | both benefited significantly from access to external drug information |
| Backbone hallucination rate (Hughes Hallucination Evaluation Model leaderboard) | hallucination rate | Gemini 1.5 Flash >5% -> Gemini 2.0 Flash 0.7% | illustrates rapid backbone improvement cited by the authors, not a result of this paper's own training |

</details>

<a id="model-ai-consult-v2-0-202606"></a>
<details>
<summary><b>AI Consult (v2.0)</b> — Generative AI-enabled clinical decision support system in primary care: a pragmatic, cluster-randomized trial <i>(Nat. Med. 2026-06)</i></summary>

**[Generative AI-enabled clinical decision support system in primary care: a pragmatic, cluster-randomized trial](https://www.nature.com/articles/s41591-026-04503-6)**

*Nat. Med.* · 2026-06 · Ambrose Agweyu & Bilal A. Mateen · [doi:10.1038/s41591-026-04503-6](https://doi.org/10.1038/s41591-026-04503-6)

| | |
| --- | --- |
| **Summary** | • A GPT-4o-based clinical decision support tool embedded in the EMR was tested in a real-world cluster-randomized trial across 16 Kenyan primary care facilities.<br>• LLM assistance did not significantly reduce 14-day treatment failure (2.2% vs. 2.0% control, P = 0.13) -- a rare rigorously tested null result for this kind of tool.<br>• No safety signal was identified, and the intervention cost about 4 cents per patient in LLM inference. |
| **Models** | Custom LLM-based CDSS ("AI Consult", version 2.0) embedded in Penda Health's EMR, built on GPT-4o (May 2025 release; temperature 0.1, top-p 1.0, 1024-token max output), with structured system prompts defining clinical role and scope aligned to Kenyan national treatment guidelines, and rule-based, version-controlled prompt logic for color-coded severity alerts. |
| **Downstream tasks** | `clinical decision support`, `diagnosis`, `treatment response`<br>Cluster-randomized (by clinical officer) trial of an always-on, prompt-triggered LLM clinical decision support tool embedded in the EMR for real-world low-resource primary care, measuring 14-day treatment failure, documentation quality, prescribing, patient satisfaction and safety. |
| **Modalities** | `text`, `EHR` |
| **Pre-training** | Uses GPT-4o off-the-shelf (not fine-tuned); clinical alignment is achieved entirely through structured system prompts and version-controlled prompt-based alert logic rather than model training. |
| **Data** | Pragmatic cluster-randomized trial across 16 primary care facilities in Nairobi/Kiambu, Kenya (Penda Health network). 103 clinical officers (52 intervention, 51 control) randomized; 9,691 patients analyzed (4,693 intervention, 4,654 control) between 22 April and 16 July 2025.<br>**16** facilities · **103** clinical officers · **9,691** patients analyzed |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Primary outcome, 14-day treatment failure, intervention vs. control (9,691 patients, 103 clinical officers) | adjusted odds ratio | OR 0.77 (95% CI 0.55-1.08), P = 0.13 | 2.2% intervention vs. 2.0% control; not statistically significant |
| Safety | adverse events attributed to the intervention | 0 serious adverse events; no safety signal on independent review |  |
| Per-patient LLM cost (intervention arm) | mean cost | US$0.04 (95% CI 0.04-0.04) |  |

</details>

<a id="model-bridge-202606"></a>
<details>
<summary><b>BRIDGE</b> — BRIDGE: benchmarking large language models for understanding real-world clinical practice texts <i>(Nat. Biomed. Eng. 2026-06)</i></summary>

**[BRIDGE: benchmarking large language models for understanding real-world clinical practice texts](https://www.nature.com/articles/s41551-026-01719-2)**

*Nat. Biomed. Eng.* · 2026-06 · [Jiageng Wu](https://scholar.google.co.uk/citations?user=vz5MGDoAAAAJ&hl=en&oi=ao) & Jie Yang · [doi:10.1038/s41551-026-01719-2](https://doi.org/10.1038/s41551-026-01719-2)

| | |
| --- | --- |
| **Summary** | • A multilingual benchmark of 87 real-world clinical NLP tasks (triage, extraction, diagnosis, billing coding and more) across 9 languages and 14 specialties.<br>• 95 LLMs were evaluated, including DeepSeek-R1, GPT-4o, Gemini and Qwen3, revealing large performance gaps by language, task type and specialty.<br>• Open-source models matched proprietary ones, while older medically fine-tuned models often lagged behind newer general-purpose LLMs. |
| **Models** | Benchmarking framework introducing no new model architecture. Evaluates 95 existing LLMs, including DeepSeek-R1, GPT-4o, Gemini and Qwen3, under multiple inference strategies. |
| **Downstream tasks** | `triage`, `information extraction`, `diagnosis`, `prognosis`, `billing coding`, `benchmarking`<br>Multilingual benchmark across eight task types covering the patient care continuum. Open-source LLMs matched proprietary models; medically fine-tuned models on older backbones often lagged updated general-purpose LLMs. |
| **Modalities** | `text` |
| **Data** | 87 clinical NLP tasks sourced from 59 real-world clinical data sources across 9 languages and 14 clinical specialties, spanning the patient care continuum (triage, information extraction, diagnosis, prognosis, billing coding).<br>**87** tasks · **59** clinical data sources · **9** languages · **14** specialties · **95** models evaluated |

</details>

<a id="model-health-ai-robustness-stress-test-suite-202606"></a>
<details>
<summary><b>Health AI robustness stress-test suite</b> — Evaluating the robustness and readiness of large frontier models in health AI applications <i>(Nat. Med. 2026-06)</i></summary>

**[Evaluating the robustness and readiness of large frontier models in health AI applications](https://www.nature.com/articles/s41591-026-04501-8)**

*Nat. Med.* · 2026-06 · [Yu Gu](https://scholar.google.co.uk/citations?user=1PoaURIAAAAJ&hl=en&oi=ao) & Paul Vozila · [doi:10.1038/s41591-026-04501-8](https://doi.org/10.1038/s41591-026-04501-8)

| | |
| --- | --- |
| **Summary** | • Adversarial stress tests were applied to 10 flagship frontier models (GPT-5, Gemini 2.5 Pro, Claude 3.5 Sonnet, MedGemma and others) across popular health AI benchmarks.<br>• Models could often guess correct answers with key inputs removed, yet were derailed by trivial prompt changes and fabricated plausible-sounding but flawed reasoning.<br>• Popular health benchmarks vary widely in what they actually measure, exposing a gap between benchmark scores and real robustness. |
| **Models** | Adversarial stress-test suite applied to flagship frontier models (GPT-4o, GPT-5, OpenAI o3, OpenAI o4-mini, Gemini 2.5 Pro, Claude 3.5 Sonnet, DeepSeek-VL2, Qwen3-VL, LLaVA-Med 1.5, MedGemma) rather than a new model itself. |
| **Downstream tasks** | `benchmarking`, `reasoning`<br>Adversarial stress testing reveals brittleness: models can guess correct answers with key inputs removed, yet are confused by minor prompt changes and fabricate convincing but flawed reasoning traces. Popular health benchmarks vary widely in what they actually measure. |
| **Modalities** | `multimodal`, `text` |
| **Data** | Clinician-guided rubrics applied to popular health AI benchmarks under a series of adversarial transformations (key-input removal, prompt alterations) to probe multimodal medical reasoning robustness. |
| **Weights** | [doi.org/10.5281/zenodo.20047288](https://doi.org/10.5281/zenodo.20047288) |

</details>

<a id="model-frontier-llm-vs-clinical-ai-tool-benchmark-202606"></a>
<details>
<summary><b>Frontier LLM vs. clinical AI tool benchmark</b> — General-purpose large language models outperform specialized clinical AI tools on medical benchmarks <i>(Nat. Med. 2026-06)</i></summary>

**[General-purpose large language models outperform specialized clinical AI tools on medical benchmarks](https://www.nature.com/articles/s41591-026-04431-5)**

*Nat. Med.* · 2026-06 · Krithik Vishwanath & Eric Karl Oermann · [doi:10.1038/s41591-026-04431-5](https://doi.org/10.1038/s41591-026-04431-5)

| | |
| --- | --- |
| **Summary** | • A head-to-head evaluation pits three frontier LLMs (GPT-5.2, Gemini 3.1 Pro, Claude Opus 4.6) against two proprietary clinical AI tools (OpenEvidence, UpToDate Expert AI) across MedQA, HealthBench and 100 real clinical queries.<br>• Frontier LLMs beat clinical AI tools in all three evaluations; Gemini scored highest on MedQA at 97.4% vs. OpenEvidence's 89.6% and UpToDate's 88.4%.<br>• On real clinical queries reviewed blindly by 12 clinicians, specialized clinical AI tools performed no better than Google Search's AI Overview. |
| **Models** | Comparative evaluation of two proprietary clinical AI tools (OpenEvidence, UpToDate Expert AI; architectures undisclosed) against three frontier LLMs (GPT-5.2, Gemini 3.1 Pro, Claude Opus 4.6), plus Google Search AI Overview as a real-world control. Introduces no new model. |
| **Downstream tasks** | `question answering`, `benchmarking`, `reasoning`<br>Compares frontier general-purpose LLMs against specialized proprietary clinical AI tools on medical knowledge (MedQA), clinician alignment (HealthBench) and real-world physician queries (RCQ), finding frontier LLMs outperform clinical tools at every stage and that clinical tools matched only Google's AI Overview. |
| **Modalities** | `text` |
| **Data** | Three-stage evaluation: 500 MedQA (USMLE-style) questions, 500 HealthBench items measuring clinician alignment, and a new real clinical queries (RCQ) benchmark of 100 de-identified physician queries from live clinical deployment, reviewed blindly by 12 US clinicians (1,800 model-question annotations).<br>**500** medqa questions · **500** healthbench items · **100** real clinical queries · **1,800** clinician annotations · **12** clinician reviewers |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MedQA (500 USMLE-style questions) | accuracy | Gemini 3.1 Pro 97.4% > GPT-5.2 94.2% > Claude Opus 4.6 90.2% > OpenEvidence 89.6% > UpToDate 88.4% | Gemini outperformed all others (P < 1e-4 vs. OpenEvidence/UpToDate/Claude, P = 0.02 vs. GPT) |
| RCQ clinician rating, rater-leniency adjusted (1,800 annotations, 12 clinicians) | odds of a higher rating vs. Gemini | clinical AI tools (incl. Google AI Overview) had 49-87% lower odds (OR 0.13-0.51) | all P < 0.0001; frontier models beat clinical tools on individual questions, not just averages (rank-biserial r = 0.5-0.9) |
| RCQ vs. Google Search AI Overview | comparative clinician rating | clinical AI tools scored no better than Google AI Overview |  |

</details>

<a id="model-multimodal-amie-202605"></a>
<details>
<summary><b>Multimodal AMIE</b> — Advancing conversational diagnostic AI with multimodal reasoning <i>(Nat. Med. 2026-05)</i></summary>

**[Advancing conversational diagnostic AI with multimodal reasoning](https://www.nature.com/articles/s41591-026-04371-0)**

*Nat. Med.* · 2026-05 · Khaled Saab & Ryutaro Tanno · [doi:10.1038/s41591-026-04371-0](https://doi.org/10.1038/s41591-026-04371-0)

| | |
| --- | --- |
| **Summary** | • A multimodal extension of AMIE gathers, interprets and reasons over dermatology photos, ECGs and clinical documents within a diagnostic conversation, not just text.<br>• In a randomized study of 105 simulated telehealth consultations judged by 18 specialists, multimodal AMIE outperformed PCPs on 29 of 32 evaluation axes.<br>• A state-aware dialogue framework that adapts history-taking to diagnostic uncertainty was key to bridging text and visual reasoning. |
| **Models** | Multimodal AMIE, built on Gemini 2.0 Flash, extending the AMIE conversational diagnostic system with a state-aware dialogue framework that dynamically guides history-taking based on diagnostic uncertainty and evolving patient state. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `question answering`<br>Multimodal diagnostic dialogue combining history-taking, interpretation of visual/document evidence and structured reasoning, evaluated against PCPs on diagnostic accuracy and conversation quality (history-taking, empathy). |
| **Modalities** | `text`, `clinical photography`, `ECG`, `multimodal` |
| **Data** | Randomized, blinded exploratory study: 105 simulated telehealth consultations including dermatology photographs, ECGs and clinical documents, judged by 18 specialist physicians against primary care physicians across 32 evaluation axes.<br>**105** simulated consultations · **18** specialist judges · **32** evaluation axes |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Multimodal AMIE vs. PCPs (105 consultations, 18 specialist judges) | evaluation axes won | 29 of 32 axes, including 7 of 9 multimodal-reasoning metrics |  |

</details>

<a id="model-cognitive-layer-architecture-psychotherapy-llm-202605"></a>
<details>
<summary><b>Cognitive layer architecture (psychotherapy LLM)</b> — A cognitive layer architecture to support large-language model performance in psychotherapy interactions <i>(Nat. Med. 2026-05)</i></summary>

**[A cognitive layer architecture to support large-language model performance in psychotherapy interactions](https://www.nature.com/articles/s41591-026-04278-w)**

*Nat. Med.* · 2026-05 · Max Rollwage & Ross Harper · [doi:10.1038/s41591-026-04278-w](https://doi.org/10.1038/s41591-026-04278-w)

| | |
| --- | --- |
| **Summary** | • A cognitive layer architecture adds specialized clinical psychotherapeutic reasoning to general-purpose LLMs, tested across four base models (GPT-4, Claude, Gemini, Llama 3).<br>• In a randomized double-blind evaluation judged by 22 expert clinicians, cognitive-layer agents outperformed both standalone LLMs and human clinicians on CBT competencies, independent of the specific base LLM.<br>• Validated on 19,674 real-world transcripts from 8,920 users, greater cognitive-layer activation was associated with more symptom improvement and long-term clinical recovery. |
| **Models** | A cognitive layer architecture layered on top of four general-purpose base LLMs (GPT-4, Claude, Gemini and Llama 3), each tested standalone and enhanced with the cognitive layer (2 architectures x 4 base LLMs = 8 experimental AI conditions), adding specialized clinical psychotherapeutic reasoning for patient-facing interactions. |
| **Downstream tasks** | `clinical decision support`, `reasoning`, `question answering`<br>Patient-facing cognitive-behavioral therapy conversations; the cognitive layer architecture augments general-purpose LLMs with specialized psychotherapeutic reasoning, evaluated against standalone LLMs (same 4 base models) and human clinicians on key clinical competencies. |
| **Modalities** | `text` |
| **Data** | Randomized double-blind evaluation: 227 participants generated naturalistic mental-well-being session transcripts across 8 experimental AI conditions (cognitive-layer agents, n=101: Claude 25, Gemini 26, GPT-4 26, Llama 3 24; standalone LLMs, n=100: Claude 25, Gemini 24, GPT-4 27, Llama 3 24) plus a human-clinician arm, assessed by 22 expert clinicians. Validated on 19,674 real-world transcripts from a large-scale deployment supporting 8,920 users.<br>**227** rct participants · **22** expert clinicians · **19,674** real world transcripts · **8,920** real world users |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| RCT vs. standalone LLMs and human clinicians, across 4 base LLMs (227 participants, 22 expert raters) | clinical competency ratings | cognitive-layer-augmented LLMs outperformed both standalone LLMs and human clinicians | performance uplift was independent of the specific base LLM (GPT-4, Claude, Gemini or Llama 3) |
| Real-world deployment (19,674 transcripts, 8,920 users, ~10-week follow-up) | association with symptom improvement | increased cognitive-layer activation associated with greater improvement and higher long-term recovery likelihood |  |

</details>

<a id="model-llm-physician-reasoning-evaluation-202604"></a>
<details>
<summary><b>LLM physician-reasoning evaluation</b> — Performance of a large language model on the reasoning tasks of a physician <i>(Science 2026-04)</i></summary>

**[Performance of a large language model on the reasoning tasks of a physician](https://www.science.org/doi/10.1126/science.adz4433)**

*Science* · 2026-04 · Peter G. Brodeur & Adam Rodman · [doi:10.1126/science.adz4433](https://doi.org/10.1126/science.adz4433)

| | |
| --- | --- |
| **Summary** | • Across five experiments benchmarked against hundreds of physicians on classic diagnostic reasoning cases, OpenAI's o1-preview outperformed physician baselines and GPT-4 in every experiment.<br>• On 20 NEJM Healer virtual-patient cases, o1-preview achieved a perfect clinical-reasoning (R-IDEA) score in 78 of 80 case reviews.<br>• A real-world study in a tertiary academic emergency room compared o1-series second opinions against human expert second opinions on randomly selected patients, with face validity as a proof of concept. |
| **Models** | OpenAI's o1 series (primarily o1-preview), evaluated against GPT-4 and physician baselines on physician-authored diagnostic reasoning cases. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `benchmarking`<br>Physician-evaluation of o1-preview against the 65-year-old gold-standard format for expert medical computing systems (complex diagnostic reasoning cases), plus a real-world emergency room second-opinion comparison (proof of concept, not diagnostic-accuracy-focused since ED decisions center on triage/disposition). |
| **Modalities** | `text` |
| **Data** | Five experiments comparing o1-preview to a baseline of hundreds of physicians on classic clinical diagnostic reasoning cases (including 20 NEJM Healer virtual-patient cases), plus a real-world study comparing human-expert and AI second opinions on randomly selected emergency room patients at a tertiary academic medical center.<br>**20** nejm healer cases |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| NEJM Healer diagnostic reasoning cases (20 cases, R-IDEA 10-point scale) | perfect R-IDEA score rate | 78 of 80 case reviews (2 reviewers x ~40 cases each) | reviewer agreement 99% (kappa = 0.89); significantly higher than the prior GPT-4 study these cases were drawn from |
| Across all 5 experiments vs. physician and GPT-4 baselines | outperformance | o1-preview outperformed both physician baselines and GPT-4 in every experiment | authors note gains were not always robust for "cannot-miss" diagnoses in NEJM Healer and landmark diagnostic cases |

</details>

<a id="model-gat-cn-202604"></a>
<details>
<summary><b>GAT-CN</b> — Graph augmented transformers improve chemotherapy toxicity symptom extraction from clinical notes <i>(Nat. Commun. 2026-04)</i></summary>

**[Graph augmented transformers improve chemotherapy toxicity symptom extraction from clinical notes](https://www.nature.com/articles/s41467-026-72347-2)**

*Nat. Commun.* · 2026-04 · Elia Saquand & Tina Hernandez-Boussard · [doi:10.1038/s41467-026-72347-2](https://doi.org/10.1038/s41467-026-72347-2)

| | |
| --- | --- |
| **Summary** | • GAT-CN embeds clinical notes with Bio+ClinicalBERT and links them to symptom terms within a heterogeneous clinical graph learned via GraphSAGE.<br>• Across 1,753 patients receiving acute cancer care, GAT-CN outperformed transformer-only models at multi-symptom classification, reaching 0.850 weighted AUROC.<br>• The model surfaced additional chemotherapy-related diagnoses missed by structured EHR data, confirmed through manual chart review. |
| **Models** | Graph-Augmented Transformer for Clinical Notes (GAT-CN): notes embedded with Bio+ClinicalBERT, linked to symptom-related terms within a heterogeneous clinical graph learned using GraphSAGE. |
| **Downstream tasks** | `classification`, `clinical decision support`<br>Multi-symptom classification extracting chemotherapy-related toxicity symptoms from unstructured clinical notes to support earlier monitoring of acute care events (emergency department visits, hospitalizations). |
| **Modalities** | `text`, `EHR` |
| **Data** | 1,753 patients who received acute care for chemotherapy-related toxicity; clinical notes plus structured EHR data, with symptom categories including pain (1,140 patients) and additional diagnoses recovered from notes and confirmed via manual annotation.<br>**1,753** patients |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Multi-symptom classification (1,753 patients) | weighted AUROC / AUPRC | AUROC 0.850, AUPRC 0.812 | outperformed transformer-only baselines |

</details>

<a id="model-clindiag-gpt-202603"></a>
<details>
<summary><b>ClinDiag-GPT</b> — Grounding large language models in clinical diagnostics <i>(Nat. Commun. 2026-03)</i></summary>

**[Grounding large language models in clinical diagnostics](https://www.nature.com/articles/s41467-026-70274-w)**

*Nat. Commun.* · 2026-03 · Xi Chen & Kang Li · [doi:10.1038/s41467-026-70274-w](https://doi.org/10.1038/s41467-026-70274-w)

| | |
| --- | --- |
| **Summary** | • ClinDiag-GPT is fine-tuned to execute full iterative diagnostic procedures, not just answer static medical questions, using a new 4,421-case benchmark.<br>• It outperformed GPT-4o, GPT-4o-mini, Claude-3-Haiku and three Qwen2.5 baselines on both diagnostic accuracy and procedural performance.<br>• Physician-ClinDiag-GPT collaboration achieved higher diagnostic accuracy and efficiency than either the physician or the model working alone. |
| **Models** | ClinDiag-GPT, a specialized LLM fine-tuned on clinical cases for iterative diagnostic workflows (base foundation model not stated in the accessible text). Evaluated against GPT-4o-mini, GPT-4o, Claude-3-Haiku and Qwen2.5-72b/32b/14b as baselines. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `benchmarking`<br>Executes full iterative diagnostic procedures (not static question answering) via the ClinDiag-Framework evaluation system, benchmarked against six baseline LLMs and evaluated for physician-AI collaboration. |
| **Modalities** | `text` |
| **Data** | ClinDiag-Benchmark: 4,421 real-world clinical cases spanning 32 medical specialties across three subsets (Challenging Case, Emergency Case, Rare Disease), sourced from MIMIC-IV-Ext, a prior rare-disease dataset, and published case reports.<br>**4,421** clinical cases · **32** medical specialties |
| **Code** | [github.com/geteff1/ClinDiag](https://github.com/geteff1/ClinDiag) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| ClinDiag-Benchmark (4,421 cases) vs. 6 baseline LLMs | diagnostic accuracy and procedural performance | ClinDiag-GPT outperformed all baselines (GPT-4o-mini, GPT-4o, Claude-3-Haiku, Qwen2.5-72b/32b/14b) | exact accuracy percentages not extracted from the accessible text |

</details>

<a id="model-trialmatchai-202603"></a>
<details>
<summary><b>TrialMatchAI</b> — TrialMatchAI: an end-to-end AI-powered clinical trial recommendation system to streamline patient-to-trial matching <i>(Nat. Commun. 2026-03)</i></summary>

**[TrialMatchAI: an end-to-end AI-powered clinical trial recommendation system to streamline patient-to-trial matching](https://www.nature.com/articles/s41467-026-70509-w)**

*Nat. Commun.* · 2026-03 · Majd Abdallah & Macha Nikolski · [doi:10.1038/s41467-026-70509-w](https://doi.org/10.1038/s41467-026-70509-w)

| | |
| --- | --- |
| **Summary** | • TrialMatchAI automates patient-to-trial matching from structured records and unstructured physician notes using fine-tuned open-source LLMs in a RAG pipeline.<br>• A fine-tuned Gemma-2-2b model re-ranks candidate trials, and a fine-tuned Phi-4 model performs criterion-level eligibility classification with medical chain-of-thought reasoning.<br>• In real-world validation, 92% of oncology patients had a relevant trial retrieved in the top 20 recommendations, with over 90% eligibility-classification accuracy. |
| **Models** | Retrieval-augmented pipeline: BM25 lexical + k-NN semantic retrieval (Elasticsearch) for candidate trials, a fine-tuned Gemma-2-2b model for criterion-level re-ranking, and a fine-tuned Phi-4 model for eligibility classification via medical chain-of-thought reasoning. |
| **Downstream tasks** | `clinical decision support`, `reasoning`, `classification`<br>End-to-end patient-to-trial matching: biomedical entity normalization, hybrid lexical/semantic candidate retrieval, criterion-level re-ranking and chain-of-thought eligibility classification with traceable explanations, deployable locally for privacy. |
| **Modalities** | `text`, `EHR` |
| **Data** | Synthetic "Ideal Candidates" patient profiles from cancer-related trials with long/complex eligibility criteria, plus publicly available TREC Clinical Trials track summaries, and real-world validation on oncology patients. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Real-world oncology patient validation | relevant trial retrieved in top-20 recommendations | 92% |  |
| Criterion-level eligibility classification (expert-assessed) | accuracy | over 90%, particularly strong on biomarker-driven matches |  |
| End-to-end runtime per patient | average time | ~4.6 min (2.7s retrieval, 92.7s re-ranking, 180.7s CoT reasoning) | vs. 10 min to 2+ hours for manual eligibility screening per trial |

</details>

<a id="model-clinical-environment-simulator-ces-202603"></a>
<details>
<summary><b>Clinical Environment Simulator (CES)</b> — A clinical environment simulator for dynamic AI evaluation <i>(Nat. Med. 2026-03)</i></summary>

**[A clinical environment simulator for dynamic AI evaluation](https://www.nature.com/articles/s41591-026-04252-6)**

*Nat. Med.* · 2026-03 · Luyang Luo & Pranav Rajpurkar · [doi:10.1038/s41591-026-04252-6](https://doi.org/10.1038/s41591-026-04252-6)

| | |
| --- | --- |
| **Summary** | • The Clinical Environment Simulator proposes evaluating clinical LLMs inside dynamic digital hospital environments instead of static datasets and isolated scenarios.<br>• A parallel "hospital engine" (beds, staff, equipment) and "patient engine" (disease progression, treatment response) let every LLM decision alter future states.<br>• CES targets three gaps in current benchmarks -- temporal reasoning, resource-aware decision-making and operational resilience under adversarial conditions. |
| **Models** | A proposed evaluation framework (Clinical Environment Simulator, CES), not a trained model: a parallel simulation architecture pairing a "hospital engine" (bed availability, staffing, equipment) with a "patient engine" (disease progression, treatment response) to score clinical LLM decisions dynamically via realistic EHR interfaces. |
| **Downstream tasks** | `reasoning`, `benchmarking`, `planning`<br>Proposes evaluating clinical LLMs on temporal reasoning under evolving constraints, resource-aware decision-making (individual vs. system-wide tradeoffs), and operational resilience via adversarial testing (simultaneous emergencies, system failures) -- capabilities absent from static benchmarks. |
| **Modalities** | `text` |
| **Data** | Conceptual framework proposal; no completed empirical evaluation run through CES itself. |

</details>

<a id="model-prea-202603"></a>
<details>
<summary><b>PreA</b> — An LLM chatbot to facilitate primary-to-specialist care transitions: a randomized controlled trial <i>(Nat. Med. 2026-03)</i></summary>

**[An LLM chatbot to facilitate primary-to-specialist care transitions: a randomized controlled trial](https://www.nature.com/articles/s41591-025-04176-7)**

*Nat. Med.* · 2026-03 · Xinge Tao & Shasha Han · [doi:10.1038/s41591-025-04176-7](https://doi.org/10.1038/s41591-025-04176-7)

| | |
| --- | --- |
| **Summary** | • PreA is an LLM chatbot co-designed with local stakeholders to perform general medical consultations (history-taking, preliminary diagnosis, test ordering) before specialist visits.<br>• In a 2,069-patient RCT across 111 specialists and 24 disciplines, PreA-only use cut physician consultation time by 28.7% versus no-PreA.<br>• Co-designed PreA outperformed the same base model further fine-tuned on local dialogues, arguing codesign beats passive local data collection for LLM deployment. |
| **Models** | PreA (preassessment): an LLM chatbot co-designed with local stakeholders (specific base LLM not stated in the accessible text), compared against the same model with additional fine-tuning on local dialogues. |
| **Downstream tasks** | `diagnosis`, `patient communication`, `clinical decision support`<br>History-taking, preliminary diagnosis, test ordering and referral-report generation for primary-to-specialist transitions, compared across PreA-only, PreA-with-staff-support and no-PreA arms. |
| **Modalities** | `text` |
| **Data** | Randomized controlled trial: 2,069 patients (1,141 women, 928 men) across two health centers and 111 specialists spanning 24 medical disciplines, randomized to PreA-only, PreA-human (staff-supported) or No-PreA arms.<br>**2,069** patients · **111** specialists · **24** disciplines |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Physician consultation duration, PreA-only vs. No-PreA (2,069 patients) | mean duration | 3.14 +/- 2.25 min vs. 4.41 +/- 2.77 min | 28.7% reduction, P < 0.001 |
| Physician-perceived care coordination | mean score | 3.69 +/- 0.90 vs. 1.73 +/- 0.95 | 113.1% increase, P < 0.001 |
| Patient-reported communication ease | mean score | 3.99 +/- 0.62 vs. 3.44 +/- 0.97 | 16.0% increase, P < 0.001 |

</details>

<a id="model-amie-articulate-medical-intelligence-explorer-202602"></a>
<details>
<summary><b>AMIE (Articulate Medical Intelligence Explorer)</b> — A large language model for complex cardiology care <i>(Nat. Med. 2026-02)</i></summary>

**[A large language model for complex cardiology care](https://www.nature.com/articles/s41591-025-04190-9)**

*Nat. Med.* · 2026-02 · [Jack W. O'Sullivan](https://scholar.google.ca/citations?hl=zh-TW&user=n5l7tL8AAAAJ) & [Tao Tu](https://scholar.google.ca/citations?hl=zh-TW&user=VlR6u4AAAAJ&view_op=list_works&sortby=pubdate) · [doi:10.1038/s41591-025-04190-9](https://doi.org/10.1038/s41591-025-04190-9)

| | |
| --- | --- |
| **Summary** | • Google's AMIE (built on Gemini 2.0 Flash) assisted general cardiologists managing complex suspected-cardiomyopathy cases, judged by 9 subspecialists.<br>• Subspecialists preferred AMIE-assisted assessments 46.7% of the time vs. 32.7% for cardiologists alone, with fewer clinically significant errors and less missing content.<br>• AMIE occasionally hallucinated findings (e.g. fabricating left ventricular hypertrabeculation), but self-corrected when directly challenged by cardiologists. |
| **Models** | AMIE, an LLM-based system built upon Gemini 2.0 Flash. |
| **Downstream tasks** | `triage`, `diagnosis`, `treatment response`<br>Nine general cardiologists managed complex suspected-cardiomyopathy cases with or without AMIE assistance; three blinded subspecialists rated triage, diagnosis and management quality on a ten-domain rubric. |
| **Modalities** | `text`, `ECG`, `ultrasound`, `MRI`, `physiological signals` |
| **Data** | Randomized controlled trial on a real-world dataset of complex cases from a subspecialist cardiology practice, with clinical text reports plus raw diagnostic data (ECG, echocardiogram, cardiac MRI, cardiopulmonary exercise testing).<br>**107** patient cases · **9** cardiologists |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Subspecialist preference, AMIE-assisted vs. cardiologist-alone assessments | preferred response rate | 46.7% vs. 32.7% | P = 0.02; remaining 20.6% rated a tie |
| Clinically significant errors | error rate | 13.1% (AMIE-assisted) vs. 24.3% (cardiologist alone) | P = 0.033 |
| Missing content in assessment | rate | 17.8% (AMIE-assisted) vs. 37.4% (cardiologist alone) | P = 0.0021 |

</details>

<a id="model-llm-medical-assistant-human-factors-rct-202602"></a>
<details>
<summary><b>LLM medical-assistant human-factors RCT</b> — Reliability of LLMs as medical assistants for the general public: a randomized preregistered study <i>(Nat. Med. 2026-02)</i></summary>

**[Reliability of LLMs as medical assistants for the general public: a randomized preregistered study](https://www.nature.com/articles/s41591-025-04074-y)**

*Nat. Med.* · 2026-02 · Andrew M. Bean & Adam Mahdi · [doi:10.1038/s41591-025-04074-y](https://doi.org/10.1038/s41591-025-04074-y)

| | |
| --- | --- |
| **Summary** | • In a 1,298-participant RCT, LLMs alone (GPT-4o, Llama 3, Command R+) correctly identified conditions in up to 99% of cases, but participants using those same LLMs did no better than a control group using internet search.<br>• Participants assisted by LLMs identified relevant conditions in under 34.5% of cases and chose the correct disposition in under 44.2%, both underperforming the unassisted control group.<br>• Standard medical benchmarks and simulated patient interactions failed to predict these real human-user failures, arguing for mandatory human user testing before public deployment. |
| **Models** | Human-factors RCT using three off-the-shelf LLMs (GPT-4o, Llama 3, Command R+) as assistant conditions, compared against an internet-search control. Introduces no new model. |
| **Downstream tasks** | `diagnosis`, `triage`<br>Participants chose a disposition (5-point scale, staying home to calling an ambulance) and listed suspected conditions for 10 medical scenarios, with or without LLM assistance (GPT-4o, Llama 3, Command R+) versus an internet-search control. |
| **Modalities** | `text` |
| **Pre-training** | All three LLMs used off-the-shelf via their consumer/API interfaces, not fine-tuned for this study. |
| **Data** | 1,298 UK-based adult participants across 10 medical scenarios (5-point disposition scale plus condition identification), randomized to one of three LLM-assisted arms (GPT-4o, Llama 3, Command R+) or an internet-search control; 600 responses collected per experimental condition.<br>**1,298** participants · **10** scenarios · **600** responses per condition |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| LLM standalone task validation (60 responses/model/scenario), relevant condition identified | accuracy | GPT-4o 94.7%, Llama 3 99.2%, Command R+ 90.8% |  |
| LLM standalone disposition accuracy | accuracy | GPT-4o 64.7%, Llama 3 48.8%, Command R+ 55.5% |  |
| Human participants assisted by LLMs vs. control, relevant condition identification | odds ratio (control vs. aggregate LLM-assisted) | control had 1.76x higher odds (95% CI 1.45-2.13) | P < 0.001 for all three models; LLM-assisted participants identified conditions in under 34.5% of cases |
| Human participants assisted by LLMs vs. control, correct disposition | rate | LLM-assisted under 44.2%, no better than control |  |

</details>

<a id="model-chatgpt-health-202602"></a>
<details>
<summary><b>ChatGPT Health</b> — ChatGPT Health performance in a structured test of triage recommendations <i>(Nat. Med. 2026-02)</i></summary>

**[ChatGPT Health performance in a structured test of triage recommendations](https://doi.org/10.1038/s41591-026-04297-7)**

*Nat. Med.* · 2026-02 · [Ashwin Ramaswamy](https://scholar.google.co.uk/citations?user=p80HpI0AAAAJ&hl=en&oi=ao) & Girish N. Nadkarni · [doi:10.1038/s41591-026-04297-7](https://doi.org/10.1038/s41591-026-04297-7)

| | |
| --- | --- |
| **Summary** | • A structured stress test of OpenAI's ChatGPT Health (gpt-5-mini backbone) across 60 clinician-authored vignettes found systematic under-triage of emergencies (52%) and over-triage of non-urgent cases.<br>• Anchoring bias was significant, when family/friends minimized symptoms, triage recommendations shifted toward less urgent care (OR 11.7).<br>• Crisis-intervention safeguards for suicidal ideation activated unpredictably, raising safety concerns ahead of consumer-scale deployment. |
| **Models** | ChatGPT Health web interface, running the gpt-5-mini thinking backbone. |
| **Downstream tasks** | `triage`<br>Structured stress test of triage recommendations; failures concentrated at clinical extremes (nonurgent and emergency presentations), with anchoring bias from family/friends' framing and unpredictable crisis-intervention activation. |
| **Modalities** | `text` |
| **Data** | 60 clinician-authored triage vignettes across 21 clinical domains under 16 factorial conditions, yielding 960 total responses.<br>**60** vignettes · **21** clinical domains · **960** total responses |
| **Code** | [github.com/ashwinra-code/gpt-health-eval](https://github.com/ashwinra-code/gpt-health-eval) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Dangerous triage failures by presentation type | failure rate | 35% (nonurgent) / 48% (emergency) | inverted U-shaped pattern across the severity spectrum |
| Gold-standard emergencies (e.g. DKA, impending respiratory failure) | undertriage rate | 52% | directed to 24-48h evaluation rather than the emergency department |
| Anchoring bias (family/friends minimizing symptoms) | odds ratio for a less-urgent triage shift | 11.7 (95% CI 3.7-36.6) |  |

</details>

<a id="model-context-switching-perspective-202602"></a>
<details>
<summary><b>Context switching (perspective)</b> — Scaling medical AI across clinical contexts <i>(Nat. Med. 2026-02)</i></summary>

**[Scaling medical AI across clinical contexts](https://doi.org/10.1038/s41591-025-04184-7)**

*Nat. Med.* · 2026-02 · [Michelle M. Li](https://scholar.google.co.uk/citations?user=jQ1VLuUAAAAJ&hl=en&oi=ao) & [Marinka Zitnik](https://scholar.google.co.uk/citations?user=YtUDgPIAAAAJ&hl=en&oi=ao) · [doi:10.1038/s41591-025-04184-7](https://doi.org/10.1038/s41591-025-04184-7)

| | |
| --- | --- |
| **Summary** | • A perspective paper proposes "context switching" -- adjusting a model's reasoning at inference time, without retraining -- as a scalable alternative to fine-tuning or prompting for adapting clinical AI across settings.<br>• Argues today's adaptation strategies (fine-tuning, prompting, retrieval) scale poorly and risk contextual errors when patient or situational information is missing.<br>• Introduces no trained model or experiments; it is a conceptual roadmap for future medical AI system design. |
| **Models** | Perspective article proposing "context switching" -- adjusting model reasoning at inference without retraining -- as an alternative to fine-tuning/prompting/retrieval for adapting clinical LLMs, VLMs and multimodal health record models. Introduces no trained model. |
| **Downstream tasks** | `question answering`, `report generation`, `planning`<br>Envisions medical AI adapting across specialties, populations and geographies via inference-time context switching rather than retraining, requiring advances in data design, model architecture and evaluation. |
| **Modalities** | `multimodal`, `text` |
| **Data** | Conceptual framework; no empirical dataset. Discusses generative, multimodal and agent models switching between notes, labs, imaging and genomics. |

</details>

<a id="model-p-p-care-202601"></a>
<details>
<summary><b>P&P Care</b> — A community-codesigned LLM-powered chatbot for primary care: a randomized controlled trial <i>(Nat. Health 2026-01)</i></summary>

**[A community-codesigned LLM-powered chatbot for primary care: a randomized controlled trial](https://www.nature.com/articles/s44360-025-00021-w)**

*Nat. Health* · 2026-01 · Sairan Li & Shasha Han · [doi:10.1038/s44360-025-00021-w](https://doi.org/10.1038/s44360-025-00021-w)

| | |
| --- | --- |
| **Summary** | • P&P Care is an LLM-powered primary care chatbot codesigned with Chinese community stakeholders via a dual-track role-play framework across four development phases.<br>• In a 2,113-participant RCT across 11 Chinese provinces, the e-learning-integrated chatbot group showed significantly higher objective health awareness than consultation-only controls.<br>• The codesign approach, not just the underlying LLM, is presented as the scalable ingredient for deploying chatbots in resource-limited primary care settings. |
| **Models** | P&P Care (Population Medicine and Public Health): prototyped on GPT-4, deployed as a GPT-4o mini (OpenAI)-powered chatbot, codesigned with community stakeholders via a dual-track role-play framework. |
| **Downstream tasks** | `patient communication`, `question answering`<br>LLM-powered primary care chatbot integrated with e-learning modules, codesigned with community stakeholders across contextual understanding, cocreation, testing/refinement and implementation/evolution phases. |
| **Modalities** | `text` |
| **Data** | Randomized controlled trial: 2,113 participants (1,052 women, 1,061 men) from urban and rural areas across 11 Chinese provinces, randomized to receive a consultation with or without preparatory P&P Care e-learning.<br>**2,113** participants · **11** provinces |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Objective health awareness, e-learning group vs. consultation-only (2,113 participants) | mean score | 2.95 +/- 1.22 vs. 2.34 +/- 1.02 | P < 0.001 |

</details>

<a id="model-medhelm-202601"></a>
<details>
<summary><b>MedHELM</b> — MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks <i>(Nat. Med. 2026-01)</i></summary>

**[MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks](https://www.nature.com/articles/s41591-025-04151-2)**

*Nat. Med.* · 2026-01 · [Suhana Bedi](https://scholar.google.com/citations?user=jiu9TasAAAAJ&hl=en) & [Nigam H. Shah](https://scholar.google.com/citations?user=n63DmP8AAAAJ&hl=en) · [doi:10.1038/s41591-025-04151-2](https://doi.org/10.1038/s41591-025-04151-2)

| | |
| --- | --- |
| **Summary** | • MedHELM introduces a clinician-validated taxonomy of 5 categories / 22 subcategories / 121 real clinical tasks, plus a 37-evaluation benchmark suite for medical LLMs.<br>• Nine frontier LLMs were compared via an automated LLM-jury method; reasoning models DeepSeek R1 and o3-mini led with 66% win rates.<br>• Claude 3.5 Sonnet achieved comparable results at 15% lower computational cost, highlighting a cost/performance tradeoff for real-world deployment. |
| **Models** | Extensible evaluation framework, not a trained model. Systematically compares nine frontier LLMs (Claude 3.5 Sonnet, Claude 3.7 Sonnet, DeepSeek R1, Gemini 1.5 Pro, Gemini 2.0 Flash, GPT-4o, GPT-4o mini, Llama 3.3, o3-mini) using an automated LLM-jury method. |
| **Downstream tasks** | `clinical decision support`, `clinical note generation`, `patient communication`, `medical research assistance`, `administration`, `benchmarking`<br>Five categories mirroring real clinical tasks: clinical decision support (diagnostic decisions, treatment planning), clinical note generation (visit documentation, procedure reports), patient communication (education materials, care instructions), medical research (literature analysis, clinical data analysis) and administration (scheduling, workflow coordination). |
| **Modalities** | `text` |
| **Data** | Clinician-validated taxonomy of 5 categories / 22 subcategories / 121 tasks mirroring real clinical practice, with a 37-evaluation benchmark suite covering every subcategory.<br>**5** categories · **22** subcategories · **121** tasks · **37** evaluations · **9** models evaluated |
| **Code** | [github.com/stanford-crfm/helm](https://github.com/stanford-crfm/helm) |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| LLM-jury evaluation across 37 evaluations, 9 frontier LLMs | win rate | 66% (DeepSeek R1, o3-mini) | Claude 3.5 Sonnet achieved comparable results at 15% lower computational cost |

</details>

<a id="model-fu-llm-202512"></a>
<details>
<summary><b>Fu-LLM</b> — A large language model for clinical outcome adjudication from telephone follow-up interviews: a secondary analysis of a multicenter randomized clinical trial <i>(Nat. Commun. 2025-12)</i></summary>

**[A large language model for clinical outcome adjudication from telephone follow-up interviews: a secondary analysis of a multicenter randomized clinical trial](https://www.nature.com/articles/s41467-025-66910-6)**

*Nat. Commun.* · 2025-12 · Zhao Shi & Long Jiang Zhang · [doi:10.1038/s41467-025-66910-6](https://doi.org/10.1038/s41467-025-66910-6)

| | |
| --- | --- |
| **Summary** | • Fu-LLM automates preadjudication of clinical trial outcomes (death, hospitalization, medication use) from telephone follow-up call transcripts.<br>• Fine-tuned from Qwen2-7B, it outperformed general-purpose LLMs (GPT-3.5-turbo, GPT-4o, DeepSeek-v3, Claude 3.5 Sonnet, Gemini-2.0-Pro), an SVM baseline, and human adjudicators.<br>• Fu-LLM also showed greater robustness than different GPT-4 versions in temporal drift tests, evaluated on 1,046 vignettes from a 3-center RCT. |
| **Models** | Fu-LLM: supervised fine-tuning (SFT) of Qwen2-7B on telephone follow-up interview transcripts for clinical outcome adjudication. |
| **Downstream tasks** | `clinical decision support`, `classification`<br>Automated preadjudication of clinical trial endpoints (death, hospitalization, medication use) from telephone follow-up transcripts, compared against general-purpose LLMs, an SVM baseline, and human adjudicators, including temporal-drift robustness tests across GPT-4 versions. |
| **Modalities** | `text` |
| **Pre-training** | `supervised`<br>Supervised fine-tuning (SFT) based on Qwen2-7B; ablations compared fine-tuning with and without data augmentation. |
| **Data** | 1,046 vignettes of follow-up telephone interviews conducted across three centers in a randomized clinical trial (China CT-FFR Study 3), used for a secondary in silico human-model comparative analysis.<br>**1,046** vignettes · **3** centers |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Fu-LLM vs. general-purpose LLMs and SVM (1,046 vignettes) | adjudication accuracy | Fu-LLM outperformed GPT-3.5-turbo, GPT-4o, DeepSeek-v3, Claude 3.5 Sonnet, Gemini-2.0-Pro and SVM | also outperformed human adjudicators in the in silico comparison |

</details>

<a id="model-lins-202510"></a>
<details>
<summary><b>LINS</b> — LINS: A general medical Q&A framework for enhancing the quality and credibility of LLM-generated responses <i>(Nat. Commun. 2025-10)</i></summary>

**[LINS: A general medical Q&A framework for enhancing the quality and credibility of LLM-generated responses](https://www.nature.com/articles/s41467-025-64142-2)**

*Nat. Commun.* · 2025-10 · Sheng Wang & Yi Zhao · [doi:10.1038/s41467-025-64142-2](https://doi.org/10.1038/s41467-025-64142-2)

| | |
| --- | --- |
| **Summary** | • LINS is a retrieval-augmented medical question-answering framework that continuously gathers up-to-date medical knowledge to generate evidence-traceable LLM responses.<br>• Evaluated against 15,530 objective questions plus two physician-curated clinical test sets, LINS improved evidence validity, medical expertise and timeliness of LLM outputs.<br>• In blinded trials, resident physicians found LINS meaningfully helpful in 87.00% of evidence-based scenarios, and lay users found it helpful in 90.09% of medical-order explanations. |
| **Models** | General retrieval-augmented generation (RAG) framework layered on an underlying LLM (specific base model not stated in the accessible text), continuously retrieving up-to-date medical knowledge sources. |
| **Downstream tasks** | `question answering`, `clinical decision support`<br>Retrieval-augmented medical Q&A generating evidence-traceable responses; blinded evaluation by resident physicians (evidence-based scenarios) and lay users (medical order explanations). |
| **Modalities** | `text` |
| **Data** | 15,530 objective evaluation questions plus two physician-curated clinical test sets covering evidence-based medical practice and medical order explanation.<br>**15,530** objective questions |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Resident physician blinded evaluation, evidence-based medical scenarios | rated meaningfully helpful | 87.00% |  |
| Lay user blinded evaluation, medical order explanations | rated helpful | 90.09% |  |

</details>

<a id="model-leads-202509"></a>
<details>
<summary><b>LEADS</b> — A foundation model for human-AI collaboration in medical literature mining <i>(Nat. Commun. 2025-09)</i></summary>

**[A foundation model for human-AI collaboration in medical literature mining](https://www.nature.com/articles/s41467-025-62058-5)**

*Nat. Commun.* · 2025-09 · Zifeng Wang & Jimeng Sun · [doi:10.1038/s41467-025-62058-5](https://doi.org/10.1038/s41467-025-62058-5)

| | |
| --- | --- |
| **Summary** | • LEADS is a foundation model trained on 633,759 samples from systematic reviews, clinical trial publications and trial registries, for AI-assisted literature mining.<br>• It consistently improved over four cutting-edge LLMs on six literature-mining tasks including study search, screening and data extraction.<br>• In a 16-user study across 14 institutions, experts using LEADS reached 0.81 recall (vs. 0.78) and 0.85 extraction accuracy (vs. 0.80), saving 21-27% time. |
| **Models** | LEADS, an AI foundation model trained specifically for literature-mining tasks (specific base architecture not stated in the accessible text), compared against four cutting-edge general-purpose LLMs. |
| **Downstream tasks** | `question answering`, `benchmarking`, `classification`<br>Systematic-review literature mining (study search, screening, data extraction) as a human-AI collaboration tool, evaluated against four frontier LLMs and in a real expert-workflow user study. |
| **Modalities** | `text` |
| **Data** | 633,759 samples curated from 21,335 systematic reviews, 453,625 clinical trial publications and 27,015 clinical trial registries. User study: 16 clinicians/researchers from 14 institutions.<br>**633,759** training samples · **21,335** systematic reviews · **453,625** trial publications · **27,015** trial registries · **16** user study participants |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Study selection, LEADS-assisted vs. unassisted (16 experts, 14 institutions) | recall | 0.81 vs. 0.78 | 20.8% time savings |
| Data extraction, LEADS-assisted vs. unassisted | accuracy | 0.85 vs. 0.80 | 26.9% time savings |

</details>

---

This page is generated. Add a paper by editing [`data/LLM.yaml`](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/data/LLM.yaml) in the [pipeline repository](https://github.com/1nslyn/biomedical-ai-pipeline) and rebuilding — edits made here are overwritten. The schema and house rules are in [CONTRIBUTING.md](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/CONTRIBUTING.md).
