<!-- GENERATED FILE - DO NOT EDIT BY HAND -->
<!-- Generated from data/LLM.yaml in https://github.com/1nslyn/biomedical-ai-pipeline -->
<!-- Edits made here are overwritten by the next build. -->

# Large Language Models

Top foundational and recent research papers on medical large language models (LLMs) focusing on clinical knowledge encoding, multi-modal integration, reasoning benchmarks, and expert-level question-answering alignment.

**Maintainer:** [Leo Chen](https://github.com/leochenmd)

**57 entries**

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
| 2026.03 | [LLM-assisted systematic review of large language models in clinical medicine](#model-llm-assisted-systematic-review-202603) | Nat. Med. | An LLM-assisted systematic review of 4,609 clinical LLM studies (2022-2025) found only 19 prospective randomized trials, showing rigorous patient-centered evidence remains scarce. | 4,609 peer-reviewed studies | — | benchmarking, patient communication, question answering | — |
| 2026.02 | [A large language model for complex cardiology care](#model-amie-articulate-medical-intelligence-explorer-202602) | Nat. Med. | AMIE, built on Gemini 2.0 Flash, helped cardiologists outperform unassisted peers on complex cases, though it occasionally hallucinated self-corrected findings. | 107 patient cases | — | triage, diagnosis, treatment response | — |
| 2026.02 | [Reliability of LLMs as medical assistants for the general public: a randomized preregistered study](#model-llm-medical-assistant-human-factors-rct-202602) | Nat. Med. | An RCT found LLMs diagnose accurately alone, but public users of the same LLMs performed no better than unassisted controls. | 1,298 participants | — | diagnosis, triage | — |
| 2026.02 | [ChatGPT Health performance in a structured test of triage recommendations](#model-chatgpt-health-202602) | Nat. Med. | A stress test of ChatGPT Health, built on gpt-5-mini, found systematic under-triage of emergencies and anchoring bias from family framing. | 960 responses | — | triage | — |
| 2026.02 | [Scaling medical AI across clinical contexts](#model-context-switching-perspective-202602) | Nat. Med. | A perspective paper proposes inference-time context switching, adjusting reasoning without retraining, as a scalable alternative to fine-tuning for clinical AI. | — | — | question answering, report generation, planning | — |
| 2026.01 | [A community-codesigned LLM-powered chatbot for primary care: a randomized controlled trial](#model-p-p-care-202601) | Nat. Health | A GPT-4o-mini-powered chatbot, codesigned with Chinese community stakeholders, significantly improved health awareness in a 2,113-participant randomized trial. | 2,113 participants | — | patient communication, question answering | — |
| 2026.01 | [MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks](#model-medhelm-202601) | Nat. Med. | A clinician-validated LLM benchmark found DeepSeek R1 and o3-mini leading, with Claude Sonnet close behind at meaningfully lower computational cost. | 121 tasks, 9 models | — | clinical decision support, clinical note generation, patient communication +3 | — |
| 2026.01 | [Safety of a large language model-based clinical decision support system in African primary healthcare](#model-gpt-4o-chatgpt-4o-202601) | Nat. Health | An EMR-embedded GPT-4o clinical decision support system across 16 Kenyan clinics aligned with local guidelines in 99% of cases but produced harmful recommendations in 7.8% of encounters, with asymmetric clinician adoption. | 1,469 records across 16 primary care clinics | — | clinical decision support | — |
| 2025.12 | [A large language model for clinical outcome adjudication from telephone follow-up interviews: a secondary analysis of a multicenter randomized clinical trial](#model-fu-llm-202512) | Nat. Commun. | Fu-LLM, fine-tuned from Qwen2-7B, automated clinical-trial outcome adjudication, outperforming GPT-4o, Claude 3.5 Sonnet, Gemini and human adjudicators. | 1,046 vignettes | supervised | clinical decision support, classification | — |
| 2025.10 | [LINS: A general medical Q&A framework for enhancing the quality and credibility of LLM-generated responses](#model-lins-202510) | Nat. Commun. | LINS, a retrieval-augmented medical Q&A framework, improved LLM response credibility, helping resident physicians in 87% of evidence-based scenarios. | 15,530 questions | — | question answering, clinical decision support | — |
| 2025.10 | [A personal health large language model for sleep and fitness coaching](#model-ph-llm-202510) | Nat. Med. | A Gemini-based personal health LLM finetuned for wearable sleep and fitness data outperformed human experts on sleep and fitness multiple-choice exams and predicted self-reported sleep quality. | 3 benchmark datasets; 857 real-world case studies | instruction tuning | question answering, reasoning, risk prediction | — |
| 2025.09 | [A foundation model for human-AI collaboration in medical literature mining](#model-leads-202509) | Nat. Commun. | LEADS, a foundation model trained on 633,759 literature-mining samples, improved recall and extraction accuracy while saving 20-27% of review time. | 633,759 samples | — | question answering, benchmarking, classification | — |
| 2025.09 | [Large language model-based biological age prediction in large-scale populations](#model-llm-based-aging-assessment-framework-202509) | Nat. Med. | An LLM framework estimated biological age from health examination reports across six cohorts (>10 million participants), outperforming traditional aging proxies for all-cause mortality prediction (C-index 0.757). | >10 million participants across six population-based cohorts | instruction tuning | risk prediction, prognosis, biomarker prediction | — |
| 2025.08 | [Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning](#model-deepseek-r1-202508) | Nat. Med. | DeepSeek-R1 performed comparably to ChatGPT-o1 on USMLE, clinical case reasoning and RECIST classification, with more accurate diagnostic reasoning steps but lower-quality imaging report summaries. | 4 medical task benchmarks | — | question answering, classification, reasoning +2 | — |
| 2025.08 | [Open-source LLM DeepSeek on a par with proprietary models in clinical decision making](#model-deepseek-models-202508) | Nat. Med. | An evaluation of open-source LLMs such as DeepSeek on clinical decision-making tasks found performance comparable to, and partly better than, proprietary GPT-4o and Gemini-2.0 Flash Thinking Experimental. | — | none | clinical decision support, benchmarking | — |
| 2025.06 | [Sociodemographic biases in medical decision making by large language models](#model-nine-llms-evaluated-202506) | Nat. Med. | Nine LLMs exhibited medically unjustified sociodemographic biases in emergency department decisions, directing Black, unhoused, LGBTQIA+, and income-labeled cases toward more invasive, urgent, or mental health care across 1.7 million outputs. | 1,000 ED cases; 1.7M outputs | none | triage, clinical decision support | — |
| 2025.06 | [A vaccine chatbot intervention for parents to improve HPV vaccination uptake among middle school girls: a cluster randomized trial](#model-vaccine-chatbot-202506) | Nat. Med. | An LLM-powered vaccine chatbot for parents increased HPV vaccination uptake (7.1% vs 1.8%) and vaccine literacy in a cluster randomized trial of 2,671 parents across 180 middle-school classes. | 2,671 parents; 180 classes | — | patient communication, question answering | — |
| 2025.06 | [Towards conversational diagnostic artificial intelligence](#model-amie-202506) | Nature | AMIE, an LLM-based system optimized for diagnostic dialogue through self-play with automated feedback, outperformed primary care physicians in a randomized crossover study of text-based consultations. | 159 case scenarios; 20 primary care physicians | reinforcement learning | diagnosis, reasoning, patient communication +1 | — |
| 2025.06 | [Towards accurate differential diagnosis with large language models](#model-amie-differential-diagnosis-202506) | Nature | AMIE outperformed unassisted clinicians at differential diagnosis and improved clinicians' top-10 accuracy when used as an assistive tool on 302 challenging cases. | 302 cases; 20 clinicians | — | diagnosis, reasoning, clinical decision support | — |
| 2025.04 | [An automated framework for assessing how well LLMs cite relevant medical references](#model-sourcecheckup-202504) | Nat. Commun. | SourceCheckup, an automated agent-based pipeline, found that 50-90% of LLM responses to medical questions were not fully supported by the sources they cited. | 800 questions, 58,000 statement-source pairs | none | benchmarking | — |
| 2025.04 | [Benchmarking large language models for biomedical natural language processing applications and recommendations](#model-gpt-and-llama-llms-benchmarked-202504) | Nat. Commun. | A systematic benchmark of four LLMs on 12 BioNLP benchmarks found traditional fine-tuning outperforms zero-/few-shot LLMs on most tasks, while GPT-4 excels at medical question answering. | 12 BioNLP benchmarks across 6 applications | none | benchmarking, question answering, reasoning +1 | — |
| 2025.04 | [GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](#model-gpt-4-202504) | Nat. Med. | In a randomized controlled trial of 92 physicians on five clinical vignettes, GPT-4 assistance improved management reasoning scores by 6.5% over conventional resources alone, with no significant gain over the LLM by itself. | 92 physicians; 5 vignettes | — | clinical decision support, reasoning | — |
| 2025.03 | [A generalist medical language model for disease diagnosis assistance](#model-medfound-202503) | Nat. Med. | MedFound, a 176-billion-parameter generalist medical LLM pretrained on medical text and clinical records and aligned via chain-of-thought fine-tuning and preference alignment, outperformed baselines across eight specialties including rare diseases and assisted physicians in the clinical workflow. | 8 medical specialties | instruction tuning | diagnosis, clinical decision support, reasoning | — |
| 2025.03 | [Toward expert-level medical question answering with large language models](#model-med-palm-2-202503) | Nat. Med. | Med-PaLM 2 reached up to 86.5% on MedQA (+19% over Med-PaLM), was preferred by physicians on eight of nine clinical axes, and was preferred by specialists over generalist answers 65% of the time. | 4 benchmark datasets (MedQA, MedMCQA, PubMedQA, MMLU clinical) | instruction tuning | question answering, reasoning, clinical decision support | — |
| 2025.01 | [The TRIPOD-LLM reporting guideline for studies using large language models](#model-tripod-llm-202501) | Nat. Med. | TRIPOD-LLM, an expert-consensus extension of TRIPOD+AI, provides a 19-item, 50-subitem reporting checklist for LLM studies in biomedicine. | 19 items / 50 subitems | — | — | — |
| 2025.01 | [An evaluation framework for clinical use of large language models in patient interaction tasks](#model-craft-md-202501) | Nat. Med. | CRAFT-MD evaluates clinical LLMs through simulated natural dialogues, exposing conversational-reasoning and history-taking limitations across four models and 12 specialties. | 12 medical specialties | — | benchmarking, diagnosis, reasoning | — |
| 2024.12 | [A toolbox for surfacing health equity harms and biases in large language models](#model-equity-harms-and-bias-toolbox-202412) | Nat. Med. | A toolbox of human-assessment methods and seven EquityMedQA datasets surfaced equity biases in Med-PaLM 2 answers that narrower evaluations miss. | 7 datasets | — | benchmarking | — |
| 2024.11 | [Using large language models to accelerate communication for eye gaze typing users with ALS](#model-speakfaster-202411) | Nat. Commun. | SpeakFaster, an LLM-powered AAC interface for abbreviated text entry, saved 57% more motor actions than predictive keyboards in simulation and raised text-entry rates 29-60% in eye-gaze users with ALS. | 19 non-AAC participants, 2 eye-gaze ALS users | none | patient communication, generation | — |
| 2024.11 | [In-context learning enables multimodal large language models to classify cancer pathology images](#model-gpt-4v-202411) | Nat. Commun. | In-context learning let the multimodal LLM GPT-4V match or beat task-specific networks on colorectal cancer subtyping, colon polyp subtyping, and breast tumor detection without parameter updates. | 3 cancer histopathology tasks | none | classification, subtyping, detection | — |
| 2024.11 | [Influence of believed AI involvement on the perception of digital medical advice](#model-ai-involvement-perception-study-202411) | Nat. Med. | Believed AI involvement made identical medical advice seem less reliable, less empathetic and less worth following (n = 2,280). | 2,280 participants | — | — | — |
| 2024.10 | [Evaluating the use of large language models to provide clinical recommendations in the Emergency Department](#model-gpt-3-5-turbo-gpt-4-turbo-202410) | Nat. Commun. | Zero-shot GPT-4-turbo and GPT-3.5-turbo gave clinical recommendations on 10,000 ED visits that were on average 8% and 24% less accurate than a resident physician, respectively. | 10,000 Emergency Department visits | none | clinical decision support, triage | — |
| 2024.10 | [Outpatient reception via collaboration between nurses and a large language model: a randomized controlled trial](#model-sspec-202410) | Nat. Med. | SSPEC, a prompt-engineering chatbot built on 35,418 reception conversations, resolved queries faster and improved satisfaction in a 2,164-participant RCT. | 35,418 conversation cases | — | triage, patient communication, question answering | — |
| 2024.10 | [Integrated image-based deep learning and language models for primary diabetes care](#model-deepdr-llm-202410) | Nat. Med. | An integrated image-language system (DeepDR-LLM) supported primary care physicians in diabetes management and DR screening, improving patient self-management and referral adherence in a prospective study. | 769 patients (prospective study) | — | diagnosis, triage, clinical decision support | — |
| 2024.09 | [Evaluation and mitigation of the limitations of large language models in clinical decision-making](#model-clinical-decision-making-simulation-framework-202409) | Nat. Med. | An evaluation on 2,400 MIMIC-based clinical cases found state-of-the-art LLMs underperform physicians and are not ready for autonomous clinical decision-making. | 2,400 patient cases | — | diagnosis, reasoning, benchmarking +1 | — |
| 2024.07 | [Pre-trained multimodal large language model enhances dermatological diagnosis using SkinGPT-4](#model-skingpt-4-202407) | Nat. Commun. | SkinGPT-4, a multimodal LLM built on Llama-2-13b-chat and trained on 52,929 skin disease images, provides interactive dermatological diagnosis and treatment recommendations, evaluated on 150 real-life cases with board-certified dermatologists. | 52,929 skin disease images; 150 real-life cases | instruction tuning | diagnosis, classification, clinical decision support | — |
| 2024.06 | [Large language models for preventing medication direction errors in online pharmacies](#model-medic-202406) | Nat. Med. | MEDIC, an LLM-based medication direction copilot, produced fewer near-miss medication direction errors than LLM benchmarks and cut near-miss events by 33% in a production online pharmacy. | 1,200 expert-reviewed prescriptions | supervised | information extraction, generation | — |
| 2024.02 | [Large language models streamline automated machine learning for clinical studies](#model-chatgpt-ada-202402) | Nat. Commun. | ChatGPT ADA, an extension of GPT-4, autonomously built clinical ML models from real trial datasets that matched or beat manually crafted counterparts with no significant performance differences. | Real-world clinical datasets from large trials across various medical specialties | — | risk prediction, biomarker prediction | — |
| 2024.02 | [Closing the accessibility gap to mental health treatment with a personalized self-referral chatbot](#model-limbic-202402) | Nat. Med. | An NHS observational study of 129,400 patients found a personalized AI self-referral chatbot increased mental health referrals, especially among minority groups. | 129,400 patients | — | triage, patient communication | — |
| 2023.12 | [Reporting standards for the use of large language model-linked chatbots for health advice](#model-reporting-standards-checklist-202312) | Nat. Med. | An expert-consensus checklist for reporting the use of LLM-linked chatbots for health advice, covering transparency, accountability and evaluation. | — | — | — | — |
| 2023.10 | [Large language model AI chatbots require approval as medical devices](#model-medical-device-regulatory-commentary-202310) | Nat. Med. | A commentary arguing that AI chatbots used in patient care are regulated as medical devices but their unreliability precludes approval as such. | — | — | — | — |
| 2023.07 | [Large language models encode clinical knowledge](#model-med-palm-202307) | Nature | Med-PaLM, a 540-billion-parameter LLM adapted from PaLM, was the first to pass USMLE-style questions, achieving 67.6% accuracy on MedQA-USMLE (clinicians 86.5%) and preferred long-form answers on 9 of 14 human-evaluation axes. | 3,150 consumer medical questions | instruction tuning | question answering, reasoning | — |
| 2023.06 | [Health system-scale language models are all-purpose prediction engines](#model-nyutron-202306) | Nature | NYUTron, large language models trained on unstructured EHR notes, predicted 30-day all-cause unplanned readmission with AUROC 0.797, improving on machine learning baselines and physicians. | NYU Langone Health EHRs (no size reported) | next-token prediction | risk prediction, prognosis, forecasting | — |

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

<a id="model-llm-assisted-systematic-review-202603"></a>
<details>
<summary><b>LLM-assisted systematic review</b> — LLM-assisted systematic review of large language models in clinical medicine <i>(Nat. Med. 2026-03)</i></summary>

**[LLM-assisted systematic review of large language models in clinical medicine](https://www.nature.com/articles/s41591-026-04229-5)**

*Nat. Med.* · 2026-03 · Sully F Chen & Eric K Oermann · [doi:10.1038/s41591-026-04229-5](https://doi.org/10.1038/s41591-026-04229-5)

| | |
| --- | --- |
| **Summary** | • This LLM-assisted systematic review identified 4,609 peer-reviewed studies of LLMs in clinical medicine between January 2022 and September 2025, roughly 3.2 papers per day.<br>• Only 1,048 studies used real-world patient data and only 19 were prospective randomized trials; most addressed simulated scenarios (n = 1,857) or exam-style tasks (n = 1,704).<br>• ChatGPT and related OpenAI models constituted 65.7% of evaluated models (Gemini/Bard 13.1%); across 1,046 head-to-head comparisons LLMs outperformed humans in 33%, and at least 25% of studies had sample sizes below 30. |
| **Models** | LLM-assisted systematic review of the large language model literature in clinical medicine from January 2022 to September 2025, using LLMs to scale screening and evaluation of the evidence base. |
| **Downstream tasks** | `benchmarking`, `patient communication`, `question answering`<br>Categorization of the clinical LLM literature by task type, including patient-facing communication and education (17% of tasks), knowledge retrieval, and education and assessment simulation, plus head-to-head LLM versus human comparisons. |
| **Modalities** | `text` |
| **Data** | 4,609 peer-reviewed studies of LLMs in clinical medicine (January 2022 - September 2025), categorized by study type (real-world patient data, prospective randomized trials, simulated scenarios, exam-style tasks) and task, with head-to-head LLM versus human comparisons.<br>**4,609** studies · **1,048** real world patient data studies · **19** prospective rcts |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Head-to-head LLM vs human comparisons (1,046 comparisons) | proportion of comparisons won by LLMs | 33% | strong dependency on task realism and level of training |
| Evaluated models across studies | share of ChatGPT and related OpenAI models | 65.7% |  |
| Evaluated models across studies | share of Gemini/Bard models | 13.1% |  |

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

<a id="model-gpt-4o-chatgpt-4o-202601"></a>
<details>
<summary><b>GPT-4o (ChatGPT 4o)</b> — Safety of a large language model-based clinical decision support system in African primary healthcare <i>(Nat. Health 2026-01)</i></summary>

**[Safety of a large language model-based clinical decision support system in African primary healthcare](https://www.nature.com/articles/s44360-026-00082-5)**

*Nat. Health* · 2026-01 · Ambrose Agweyu & Bilal A Mateen · [doi:10.1038/s44360-026-00082-5](https://doi.org/10.1038/s44360-026-00082-5)

| | |
| --- | --- |
| **Summary** | • Retrospective safety evaluation of an electronic medical record-embedded LLM clinical decision support system deployed across 16 primary care clinics in Kenya (July-September 2024), with 1,469 records reviewed by trained physicians.<br>• Hallucinations were uncommon (50 encounters, 3.4%) and clinical management guidance aligned with local guidelines in almost all cases (1,455; 99%), yet clinicians did not modify documentation in 917 encounters (62%).<br>• Safety assessments identified actively harmful recommendations in 115 encounters (7.8%, 67 in final documentation), while risk in clinicians' initial notes was fully mitigated in 118 encounters (8.0%). |
| **Models** | An electronic medical record-embedded LLM clinical decision support system (GPT-4o / ChatGPT 4o) that provides real-time diagnostic and therapeutic guidance during patient encounters. |
| **Downstream tasks** | `clinical decision support`<br>Real-time diagnostic and therapeutic guidance for clinicians during primary care encounters, with retrospective assessment of hallucinations, guideline alignment and safety of recommendations. |
| **Modalities** | `EHR`, `text` |
| **Data** | 1,469 patient encounter records from 16 primary care clinics in Kenya (July-September 2024), reviewed by a panel of trained physicians for hallucinations, guideline alignment, documentation modification and safety of LLM recommendations.<br>**1,469** records · **16** clinics |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Hallucinations in LLM outputs | proportion of encounters | 50 of 1,469 (3.4%, 95% CI 2.5-4.5) | most often misexpanded acronyms or drug names |
| Alignment of clinical management guidance with local guidelines | proportion of encounters | 1,455 of 1,469 (99%, 95% CI 98.4-99.5) |  |
| Clinician documentation modification | proportion of encounters not modified | 917 of 1,469 (62%, 95% CI 59.9-64.9) |  |
| Safety assessment - actively harmful recommendations | proportion of encounters | 115 of 1,469 (7.8%, 95% CI 6.5-9.3); 67 in final documentation |  |
| Safety assessment - risk fully mitigated from clinicians' initial notes | proportion of encounters | 118 of 1,469 (8.0%, 95% CI 6.7-9.5; 12.1% of amended cases) |  |

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

<a id="model-ph-llm-202510"></a>
<details>
<summary><b>PH-LLM</b> — A personal health large language model for sleep and fitness coaching <i>(Nat. Med. 2025-10)</i></summary>

**[A personal health large language model for sleep and fitness coaching](https://www.nature.com/articles/s41591-025-03888-0)**

*Nat. Med.* · 2025-10 · Justin Khasentino & Cory Y McLean · [doi:10.1038/s41591-025-03888-0](https://doi.org/10.1038/s41591-025-03888-0)

| | |
| --- | --- |
| **Summary** | • PH-LLM is a version of the Gemini LLM finetuned for text understanding and reasoning when applied to aggregated daily-resolution numerical sensor data.<br>• PH-LLM achieved scores that exceeded a sample of human experts on multiple-choice examinations in sleep medicine (79% versus 76%) and fitness (88% versus 71%).<br>• In an evaluation involving 857 real-world case studies, PH-LLM performed similarly to human experts for fitness-related tasks, improved over the base Gemini model in providing personalized sleep insights, and effectively predicted self-reported sleep quality from multimodal wearable sensor data. |
| **Models** | PH-LLM, a finetuned version of the Gemini large language model for text understanding and reasoning over aggregated daily-resolution numerical sensor data. |
| **Downstream tasks** | `question answering`, `reasoning`, `risk prediction`<br>Multiple-choice exams in sleep medicine and fitness; generation of personalized insights and recommendations; prediction of self-reported sleep quality from longitudinal wearable sensor data. |
| **Modalities** | `text`, `physiological signals` |
| **Pre-training** | `instruction tuning`<br>Finetuned from Gemini for understanding and reasoning over numerical wearable sensor data. |
| **Data** | Three benchmark datasets covering expert domain knowledge, personalized insights and recommendations, and prediction of self-reported sleep quality from longitudinal data, plus an evaluation with 857 real-world case studies.<br>**3** benchmark datasets · **857** case studies |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Sleep medicine multiple-choice examination | accuracy | 79% (vs. 76% human experts) |  |
| Fitness multiple-choice examination | accuracy | 88% (vs. 71% human experts) |  |

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

<a id="model-llm-based-aging-assessment-framework-202509"></a>
<details>
<summary><b>LLM-based aging assessment framework</b> — Large language model-based biological age prediction in large-scale populations <i>(Nat. Med. 2025-09)</i></summary>

**[Large language model-based biological age prediction in large-scale populations](https://www.nature.com/articles/s41591-025-03856-8)**

*Nat. Med.* · 2025-09 · Yanjun Li & Qian Di · [doi:10.1038/s41591-025-03856-8](https://doi.org/10.1038/s41591-025-03856-8)

| | |
| --- | --- |
| **Summary** | • A framework that leverages large language models to estimate individual overall and organ-specific biological age from health examination reports, validated across six population-based cohorts encompassing over 10 million participants.<br>• LLM-predicted overall age achieved a concordance index (C-index) of 0.757 (95% CI 0.752-0.761) for all-cause mortality, significantly outperforming other aging proxies such as telomere length, frailty index, eight epigenetic ages and four machine-learning models.<br>• The overall age gap showed a hazard ratio of 1.055 (95% CI 1.050-1.060) for all-cause mortality and was applied to identify proteomic biomarkers of accelerated aging and to develop risk prediction models for 270 diseases. |
| **Models** | LLM-based intelligent agents constructed using Llama3-70B-Instruct with chain-of-thought reasoning, parsing health examination reports to estimate overall and organ-specific biological age. |
| **Downstream tasks** | `risk prediction`, `prognosis`, `biomarker prediction`<br>Estimation of overall and organ-specific biological age from health examination reports; prediction of all-cause mortality and organ-specific diseases; identification of proteomic biomarkers associated with accelerated aging; risk prediction models for 270 diseases. |
| **Modalities** | `text` |
| **Pre-training** | `instruction tuning` |
| **Data** | Health examination reports from six population-based cohorts encompassing over 10 million participants, used to estimate overall and organ-specific biological age, compare against aging proxies, identify proteomic biomarkers of accelerated aging and develop risk prediction models for 270 diseases.<br>**10,000,000** participants · **6** cohorts |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| All-cause mortality prediction (LLM-predicted overall age) | concordance index (C-index) | 0.757 (95% CI 0.752-0.761) | outperformed telomere length, frailty index, eight epigenetic ages and four machine-learning models |
| All-cause mortality (overall age gap) | hazard ratio | 1.055 (95% CI 1.050-1.060) |  |

</details>

<a id="model-deepseek-r1-202508"></a>
<details>
<summary><b>DeepSeek-R1</b> — Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning <i>(Nat. Med. 2025-08)</i></summary>

**[Comparative benchmarking of the DeepSeek large language model on medical tasks and clinical reasoning](https://www.nature.com/articles/s41591-025-03726-3)**

*Nat. Med.* · 2025-08 · Mickael Tordjman & Xueyan Mei · [doi:10.1038/s41591-025-03726-3](https://doi.org/10.1038/s41591-025-03726-3)

| | |
| --- | --- |
| **Summary** | • Benchmarked DeepSeek-R1, ChatGPT-o1 and Llama 3.1-405B on four medical tasks: USMLE question answering, text-based diagnostic and management cases, RECIST 1.1 tumor classification and diagnostic imaging report summarization.<br>• On USMLE, DeepSeek-R1 (accuracy 0.92) was slightly inferior to ChatGPT-o1 (0.95, P = 0.04) but better than Llama 3.1-405B (0.83, P < 10-3); on text-based cases it performed similarly to ChatGPT-o1 (0.57 vs 0.55 and 0.74 vs 0.76) and on RECIST classification (0.74 vs 0.81, P = 0.10).<br>• DeepSeek's diagnostic reasoning steps were rated more accurate than those of ChatGPT and Llama 3.1-405B (average Likert 3.61 vs 3.22 and 3.13), but its imaging report summaries had lower global quality than ChatGPT-o1's (4.5 vs 4.8, P < 10-3). |
| **Models** | DeepSeek-R1, ChatGPT-o1 and Llama 3.1-405B evaluated on USMLE questions, text-based diagnostic and management case databases (NEJM and Médicilline), RECIST 1.1 tumor classification and diagnostic imaging report summarization across multiple modalities. |
| **Downstream tasks** | `question answering`, `classification`, `reasoning`, `report generation`, `benchmarking`<br>USMLE question answering; interpretation and reasoning on text-based diagnostic and management cases; tumor classification according to RECIST 1.1 criteria; summarization of diagnostic imaging reports across multiple modalities. |
| **Modalities** | `text`, `multimodal` |
| **Data** | Four medical task sets: United States Medical Licensing Examination (USMLE) questions; text-based diagnostic and management cases from the New England Journal of Medicine and Médicilline databases; RECIST 1.1 tumor classification; and summaries of diagnostic imaging reports across multiple modalities. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| USMLE medical licensing examination | accuracy | DeepSeek-R1 0.92; ChatGPT-o1 0.95 (P = 0.04); Llama 3.1-405B 0.83 (P < 10-3) |  |
| Text-based diagnostic and management cases (NEJM database) | accuracy | 0.57 (DeepSeek-R1) vs 0.55 (ChatGPT-o1); P = 0.76 |  |
| Text-based diagnostic and management cases (Médicilline database) | accuracy | 0.74 (DeepSeek-R1) vs 0.76 (ChatGPT-o1); P = 0.06 |  |
| RECIST 1.1 tumor classification | accuracy | 0.74 (DeepSeek-R1) vs 0.81 (ChatGPT-o1); P = 0.10 |  |
| Diagnostic reasoning steps | average Likert score | DeepSeek 3.61; ChatGPT 3.22; Llama 3.1-405B 3.13 (P = 0.005 and P < 10-3) |  |
| Diagnostic imaging report summaries (global quality) | 5-point Likert score | 4.5 (DeepSeek-R1) vs 4.8 (ChatGPT-o1); P < 10-3 |  |

</details>

<a id="model-deepseek-models-202508"></a>
<details>
<summary><b>DeepSeek models</b> — Open-source LLM DeepSeek on a par with proprietary models in clinical decision making <i>(Nat. Med. 2025-08)</i></summary>

**[Open-source LLM DeepSeek on a par with proprietary models in clinical decision making](https://www.nature.com/articles/s41591-025-03850-0)**

*Nat. Med.* · 2025-08 · Sarah Sandmann & R. Eils · [doi:10.1038/s41591-025-03850-0](https://doi.org/10.1038/s41591-025-03850-0)

| | |
| --- | --- |
| **Summary** | • Correspondence reporting a systematic analysis of patient cases to evaluate the clinical utility of open-source large language models, such as the DeepSeek models, for implementation in medical applications.<br>• Performance on clinical decision-making tasks was comparable to, and partly better than, proprietary models GPT-4o and Gemini-2.0 Flash Thinking Experimental, respectively. |
| **Models** | Evaluation of open-source large language models, such as the DeepSeek models, on clinical decision-making tasks through systematic analysis of patient cases; compared with proprietary GPT-4o and Gemini-2.0 Flash Thinking Experimental. |
| **Downstream tasks** | `clinical decision support`, `benchmarking`<br>Clinical decision-making tasks evaluated through systematic analysis of patient cases; open-source LLMs (DeepSeek) compared with proprietary models GPT-4o and Gemini-2.0 Flash Thinking Experimental. |
| **Modalities** | `text` |
| **Pre-training** | `none` |
| **Data** | Patient cases analyzed to evaluate the clinical utility of open-source LLMs such as the DeepSeek models for medical applications; no cohort size or dataset description is given in the abstract. |

</details>

<a id="model-nine-llms-evaluated-202506"></a>
<details>
<summary><b>Nine LLMs (evaluated)</b> — Sociodemographic biases in medical decision making by large language models <i>(Nat. Med. 2025-06)</i></summary>

**[Sociodemographic biases in medical decision making by large language models](https://www.nature.com/articles/s41591-025-03626-6)**

*Nat. Med.* · 2025-06 · Mahmud Omar & Eyal Klang · [doi:10.1038/s41591-025-03626-6](https://doi.org/10.1038/s41591-025-03626-6)

| | |
| --- | --- |
| **Summary** | • Nine LLMs were evaluated on 1,000 emergency department cases (500 real and 500 synthetic), each presented in 32 variations (31 sociodemographic groups plus a control) with clinical details held constant, yielding over 1.7 million model-generated outputs.<br>• Compared with a physician-derived baseline and each model's own control case, cases labeled as Black, unhoused, or LGBTQIA+ were more frequently directed toward urgent care, invasive interventions, or mental health evaluations; certain LGBTQIA+-labeled cases received mental health assessment recommendations approximately six to seven times more often than clinically indicated.<br>• High-income-labeled cases received significantly more advanced imaging recommendations such as CT and MRI (P < 0.001), while low- and middle-income-labeled cases were often limited to basic or no further testing; differences persisted after multiple-hypothesis correction in both proprietary and open-source models and were not supported by clinical reasoning or guidelines. |
| **Models** | Nine proprietary and open-source large language models evaluated on 1,000 emergency department cases (500 real, 500 synthetic) presented in 32 sociodemographic variations each, with a physician-derived baseline for comparison. |
| **Downstream tasks** | `triage`, `clinical decision support`<br>Emergency department management recommendations (urgent care, invasive interventions, mental health evaluations, advanced imaging) compared across 31 sociodemographic group labels and a control, benchmarked against a physician-derived baseline. |
| **Modalities** | `text` |
| **Pre-training** | `none` |
| **Data** | 1,000 emergency department cases (500 real and 500 synthetic), each presented in 32 variations (31 sociodemographic groups plus a control) while holding clinical details constant, producing over 1.7 million model-generated outputs from nine LLMs; a physician-derived baseline was used for comparison.<br>**1,000** emergency department cases · **1,700,000** model generated outputs |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Bias evaluation - mental health assessment recommendations for LGBTQIA+-labeled cases | recommendation rate relative to clinically indicated | approximately 6-7x more often | persisted after multiple-hypothesis correction |
| Bias evaluation - advanced imaging recommendations (CT, MRI) for high-income-labeled cases | recommendation rate | significantly more than control (P < 0.001) | low- and middle-income-labeled cases often limited to basic or no further testing |

</details>

<a id="model-vaccine-chatbot-202506"></a>
<details>
<summary><b>Vaccine chatbot</b> — A vaccine chatbot intervention for parents to improve HPV vaccination uptake among middle school girls: a cluster randomized trial <i>(Nat. Med. 2025-06)</i></summary>

**[A vaccine chatbot intervention for parents to improve HPV vaccination uptake among middle school girls: a cluster randomized trial](https://www.nature.com/articles/s41591-025-03618-6)**

*Nat. Med.* · 2025-06 · Zhiyuan Hou & Leesa Lin · [doi:10.1038/s41591-025-03618-6](https://doi.org/10.1038/s41591-025-03618-6)

| | |
| --- | --- |
| **Summary** | • School-based cluster randomized trial (18 January to 31 May 2024) of an LLM-powered vaccine chatbot for parents of female middle school students aged 12-15 years across diverse socioeconomic settings in Shanghai and Anhui, China, where HPV vaccination is primarily paid out-of-pocket.<br>• 2,671 parents from 180 middle-school classes were randomized to a two-week chatbot intervention (90 classes, 1,294 parents) or usual care (90 classes, 1,377 parents); in intention-to-treat analyses 7.1% of the intervention group met the primary outcome (HPV vaccine receipt or scheduled appointment for their daughters) versus 1.8% of controls (P < 0.001).<br>• Chatbot users also had significantly more HPV vaccination-specific consultations with health professionals (49.1% versus 17.6%, P < 0.001) and improved vaccine literacy and rumor discernment (both P < 0.001). Clinical trial registration: NCT06227689. |
| **Models** | A conversational vaccine chatbot powered by large language models, engaging parents in human-like two-week interactions about HPV vaccination. |
| **Downstream tasks** | `patient communication`, `question answering`<br>Two-week conversational interactions with parents about HPV vaccination; assessment of vaccination uptake, HPV-specific health professional consultations, vaccine literacy and rumor discernment. |
| **Modalities** | `text` |
| **Data** | School-based cluster randomized trial (18 January to 31 May 2024) enrolling 2,671 parents of female middle school students aged 12-15 years from 180 classes stratified by socioeconomic setting, school and grade level in Shanghai, and urban and rural regions of Anhui Province, China; the intervention group (90 classes, 1,294 parents) engaged with the chatbot for two weeks versus usual care (90 classes, 1,377 parents). Primary outcome: receipt or scheduled appointment of the HPV vaccine for participants' daughters.<br>**2,671** parents · **180** classes |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Cluster RCT primary outcome - HPV vaccine receipt or scheduled appointment | intention-to-treat uptake rate | 7.1% vs 1.8% (P < 0.001) | two-week intervention period |
| HPV vaccination-specific consultations with health professionals | consultation rate | 49.1% vs 17.6% (P < 0.001) |  |

</details>

<a id="model-amie-202506"></a>
<details>
<summary><b>AMIE</b> — Towards conversational diagnostic artificial intelligence <i>(Nature 2025-06)</i></summary>

**[Towards conversational diagnostic artificial intelligence](https://www.nature.com/articles/s41586-025-08866-7)**

*Nature* · 2025-06 · Tao Tu & Vivek Natarajan · [doi:10.1038/s41586-025-08866-7](https://doi.org/10.1038/s41586-025-08866-7)

| | |
| --- | --- |
| **Summary** | • AMIE (Articulate Medical Intelligence Explorer) is an LLM-based AI system optimized for diagnostic dialogue, scaling learning across disease conditions, specialties and contexts through a self-play-based simulated environment with automated feedback.<br>• In a randomized, double-blind crossover study of text-based consultations with validated patient-actors, AMIE demonstrated greater diagnostic accuracy than primary care physicians.<br>• Specialist physicians rated AMIE superior on 30 of 32 evaluation axes and patient-actors on 25 of 26 axes. |
| **Models** | AMIE (Articulate Medical Intelligence Explorer), an LLM-based AI system optimized for diagnostic dialogue; learning is scaled via a self-play-based simulated environment with automated feedback. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `patient communication`, `clinical decision support`<br>Text-based consultations evaluated on history-taking, diagnostic accuracy, management, communication skills and empathy. |
| **Modalities** | `text` |
| **Pre-training** | `reinforcement learning`<br>Learning scaled across disease conditions, specialties and contexts using a self-play-based simulated environment with automated feedback. |
| **Data** | Randomized, double-blind crossover study of text-based consultations with validated patient-actors similar to objective structured clinical examinations. The study included 159 case scenarios from providers in Canada, the United Kingdom and India, 20 primary care physicians compared with AMIE, and evaluations by specialist physicians and patient-actors.<br>**159** case scenarios · **20** primary care physicians |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Specialist physician evaluation (randomized crossover study) | axes where AMIE rated superior | 30 of 32 |  |
| Patient-actor evaluation | axes where AMIE rated superior | 25 of 26 |  |

</details>

<a id="model-amie-differential-diagnosis-202506"></a>
<details>
<summary><b>AMIE (differential diagnosis)</b> — Towards accurate differential diagnosis with large language models <i>(Nature 2025-06)</i></summary>

**[Towards accurate differential diagnosis with large language models](https://www.nature.com/articles/s41586-025-08869-4)**

*Nature* · 2025-06 · Daniel McDuff & Vivek Natarajan · [doi:10.1038/s41586-025-08869-4](https://doi.org/10.1038/s41586-025-08869-4)

| | |
| --- | --- |
| **Summary** | • AMIE, a large language model optimized for diagnostic reasoning, generated differential diagnoses either alone or as an aid to clinicians.<br>• Across 302 challenging real-world cases, AMIE's standalone top-10 accuracy (59.1%) exceeded that of unassisted clinicians (33.6%, P = 0.04).<br>• Clinicians assisted by AMIE achieved higher top-10 accuracy (51.7%) than clinicians without it (36.1%, P < 0.01) or with search assistance (44.4%, P = 0.03), and produced more comprehensive differential lists. |
| **Models** | AMIE (Articulate Medical Intelligence Explorer), a large language model optimized for diagnostic reasoning, evaluated alone and as an assistive tool for clinicians. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `clinical decision support`<br>Differential diagnosis generation alone or as an aid to clinicians; assisted study arms compared with and without AMIE. |
| **Modalities** | `text` |
| **Data** | 302 challenging, real-world medical cases sourced from published case reports. Each case report was read by two clinicians randomized to one of two assistive conditions (search engines and standard medical resources, with or without AMIE), after providing a baseline unassisted differential diagnosis.<br>**302** cases · **20** clinicians |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Standalone AMIE differential diagnosis (top-10) | accuracy | 59.1% (vs. 33.6% unassisted clinicians, P = 0.04) |  |
| Clinicians assisted by AMIE (top-10) | accuracy | 51.7% (vs. 36.1% for clinicians without AMIE, P < 0.01; vs. 44.4% for clinicians with search, P = 0.03) |  |

</details>

<a id="model-sourcecheckup-202504"></a>
<details>
<summary><b>SourceCheckup</b> — An automated framework for assessing how well LLMs cite relevant medical references <i>(Nat. Commun. 2025-04)</i></summary>

**[An automated framework for assessing how well LLMs cite relevant medical references](https://www.nature.com/articles/s41467-025-58551-6)**

*Nat. Commun.* · 2025-04 · Kevin Wu & James Zou · [doi:10.1038/s41467-025-58551-6](https://doi.org/10.1038/s41467-025-58551-6)

| | |
| --- | --- |
| **Summary** | • SourceCheckup is an automated agent-based pipeline that evaluates the relevance and supportiveness of sources cited in LLM responses to health-related queries.<br>• On a dataset of 800 questions and 58,000 pairs of statements and sources covering common medical queries, between 50% and 90% of responses from seven popular LLMs were not fully supported, and sometimes contradicted, by the sources they cited.<br>• Even GPT-4o with Web Search left approximately 30% of individual statements unsupported and nearly half of its responses not fully supported; independent assessments by doctors validated the findings. |
| **Models** | SourceCheckup, an automated agent-based pipeline that evaluates the relevance and supportiveness of sources cited in LLM responses. |
| **Downstream tasks** | `benchmarking`<br>Automated evaluation of the relevance and supportiveness of sources cited in LLM responses to health-related queries. |
| **Modalities** | `text` |
| **Pre-training** | `none` |
| **Data** | Dataset of 800 health-related questions and 58,000 pairs of statements and sources representing common medical queries, used to evaluate the relevance and supportiveness of sources cited by seven popular LLMs.<br>**800** questions · **58,000** statement source pairs |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Seven popular LLMs on 800 medical questions | responses not fully supported by cited sources | 50-90% |  |
| GPT-4o with Web Search | unsupported individual statements | ~30% |  |
| GPT-4o with Web Search | responses not fully supported | nearly half |  |

</details>

<a id="model-gpt-and-llama-llms-benchmarked-202504"></a>
<details>
<summary><b>GPT and LLaMA LLMs (benchmarked)</b> — Benchmarking large language models for biomedical natural language processing applications and recommendations <i>(Nat. Commun. 2025-04)</i></summary>

**[Benchmarking large language models for biomedical natural language processing applications and recommendations](https://www.nature.com/articles/s41467-025-56989-2)**

*Nat. Commun.* · 2025-04 · Qingyu Chen & Hua Xu · [doi:10.1038/s41467-025-56989-2](https://doi.org/10.1038/s41467-025-56989-2)

| | |
| --- | --- |
| **Summary** | • The authors systematically evaluated four LLMs (GPT and LLaMA representatives) on 12 BioNLP benchmarks across six applications, comparing zero-shot, few-shot, and fine-tuning performance with traditional fine-tuning of BERT or BART models.<br>• Traditional fine-tuning outperformed zero- or few-shot LLMs on most tasks, while closed-source LLMs such as GPT-4 excelled at reasoning-related tasks like medical question answering and open-source LLMs still required fine-tuning to close performance gaps.<br>• The evaluation also examined inconsistencies, missing information, hallucinations, and cost, offering practical insights for applying LLMs in BioNLP. |
| **Models** | Four LLMs (GPT and LLaMA representatives) evaluated across 12 BioNLP benchmarks, compared with traditional fine-tuning of BERT or BART models. |
| **Downstream tasks** | `benchmarking`, `question answering`, `reasoning`, `information extraction`<br>Zero-shot, few-shot, and fine-tuned evaluation of four LLMs on 12 BioNLP benchmarks across six applications, including medical question answering; comparison with fine-tuned BERT/BART baselines; analysis of inconsistencies, missing information, hallucinations, and cost. |
| **Modalities** | `text` |
| **Pre-training** | `none` |
| **Data** | 12 BioNLP benchmarks spanning six applications of biomedical natural language processing; LLMs were evaluated in zero-shot, few-shot, and fine-tuning regimes and compared with traditional fine-tuning of BERT or BART models.<br>**12** benchmarks · **6** applications |

</details>

<a id="model-gpt-4-202504"></a>
<details>
<summary><b>GPT-4</b> — GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial <i>(Nat. Med. 2025-04)</i></summary>

**[GPT-4 assistance for improvement of physician performance on patient care tasks: a randomized controlled trial](https://www.nature.com/articles/s41591-024-03456-y)**

*Nat. Med.* · 2025-04 · Ethan Goh & Adam Rodman · [doi:10.1038/s41591-024-03456-y](https://doi.org/10.1038/s41591-024-03456-y)

| | |
| --- | --- |
| **Summary** | • Prospective randomized controlled trial (November 2023 to April 2024) in which 92 practicing physicians were randomized to use either GPT-4 plus conventional resources or conventional resources alone to answer five expert-developed clinical vignettes based on real, de-identified patient encounters with information revealed sequentially.<br>• Physicians using the LLM scored significantly higher on expert-developed scoring rubrics (mean difference = 6.5%, 95% CI = 2.7 to 10.2, P < 0.001) but spent more time per case (mean difference = 119.3 s, 95% CI = 17.4 to 221.2, P = 0.02).<br>• There was no significant difference between LLM-augmented physicians and the LLM alone (-0.9%, 95% CI = -9.0 to 7.2, P = 0.8). ClinicalTrials.gov registration: NCT06208423. |
| **Models** | GPT-4 used alongside conventional resources for open-ended management reasoning on clinical vignettes, compared with conventional resources alone. |
| **Downstream tasks** | `clinical decision support`, `reasoning`<br>Open-ended management reasoning on clinical vignettes, balancing treatment decisions and testing strategies while managing risk. |
| **Modalities** | `text` |
| **Data** | Prospective randomized controlled trial (November 2023 to April 2024): 92 practicing physicians randomized to GPT-4 plus conventional resources or conventional resources alone answered five expert-developed clinical vignettes based on real, de-identified patient encounters with information revealed sequentially; primary outcome was the difference in total score on expert-developed scoring rubrics, with secondary outcomes of domain-specific scores and time spent per case.<br>**92** physicians · **5** vignettes |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Expert-developed management reasoning vignettes (RCT) | total score difference (LLM-assisted vs conventional resources) | +6.5% (95% CI = 2.7 to 10.2, P < 0.001) |  |
| Time spent per case | mean difference (LLM users vs conventional resources) | +119.3 s (95% CI = 17.4 to 221.2, P = 0.02) |  |
| LLM-augmented physicians vs LLM alone | total score difference | -0.9% (95% CI = -9.0 to 7.2, P = 0.8) | no significant difference |

</details>

<a id="model-medfound-202503"></a>
<details>
<summary><b>MedFound</b> — A generalist medical language model for disease diagnosis assistance <i>(Nat. Med. 2025-03)</i></summary>

**[A generalist medical language model for disease diagnosis assistance](https://www.nature.com/articles/s41591-024-03416-6)**

*Nat. Med.* · 2025-03 · Xiaohong Liu & Guangyu Wang · [doi:10.1038/s41591-024-03416-6](https://doi.org/10.1038/s41591-024-03416-6)

| | |
| --- | --- |
| **Summary** | • MedFound is a generalist medical language model with 176 billion parameters, pre-trained on a large-scale corpus derived from diverse medical text and real-world clinical records.<br>• It was fine-tuned to learn physicians' inferential diagnosis with a self-bootstrapping strategy-based chain-of-thought approach and aligned with standard clinical practice through a unified preference alignment framework.<br>• MedFound outperformed other baseline LLMs and specialized models in in-distribution (common diseases), out-of-distribution (external validation) and long-tailed distribution (rare diseases) scenarios across eight specialties; a comprehensive evaluation framework (AI versus physician comparison, AI-assistance study, human evaluation) with eight clinical metrics, covering medical record summarization, diagnostic reasoning and risk management, demonstrated feasibility for assisting physicians with diagnosis in the clinical workflow. |
| **Models** | MedFound, a generalist medical language model with 176 billion parameters, pre-trained on a large-scale corpus of diverse medical text and real-world clinical records, fine-tuned with a self-bootstrapping strategy-based chain-of-thought approach and aligned via a unified preference alignment framework. |
| **Parameters** | 176B |
| **Downstream tasks** | `diagnosis`, `clinical decision support`, `reasoning`<br>Disease diagnosis assistance across eight specialties, including medical record summarization, diagnostic reasoning and risk management; evaluated in in-distribution, out-of-distribution and long-tailed distribution scenarios with AI-versus-physician comparison, AI-assistance study and human evaluation. |
| **Modalities** | `text` |
| **Pre-training** | `instruction tuning`<br>Pre-trained on a large-scale corpus derived from diverse medical text and real-world clinical records; fine-tuned to learn physicians' inferential diagnosis via a self-bootstrapping strategy-based chain-of-thought approach; aligned with standard clinical practice through a unified preference alignment framework. |
| **Data** | Large-scale corpus derived from diverse medical text and real-world clinical records; evaluation across eight specialties covering in-distribution (common diseases), out-of-distribution (external validation) and long-tailed distribution (rare diseases) scenarios, with an AI versus physician comparison, AI-assistance study and human evaluation framework incorporating eight clinical evaluation metrics (medical record summarization, diagnostic reasoning, risk management).<br>**8** specialties · **8** clinical evaluation metrics |

</details>

<a id="model-med-palm-2-202503"></a>
<details>
<summary><b>Med-PaLM 2</b> — Toward expert-level medical question answering with large language models <i>(Nat. Med. 2025-03)</i></summary>

**[Toward expert-level medical question answering with large language models](https://www.nature.com/articles/s41591-024-03423-7)**

*Nat. Med.* · 2025-03 · Karan Singhal & Vivek Natarajan · [doi:10.1038/s41591-024-03423-7](https://doi.org/10.1038/s41591-024-03423-7)

| | |
| --- | --- |
| **Summary** | • Med-PaLM 2 combines base LLM improvements, medical domain fine-tuning, and new strategies for improving reasoning and grounding through ensemble refinement and chain of retrieval.<br>• Med-PaLM 2 scores up to 86.5% on the MedQA dataset, improving upon Med-PaLM by over 19%, with dramatic performance increases across MedMCQA, PubMedQA and MMLU clinical topics datasets.<br>• In human evaluations physicians preferred Med-PaLM 2 answers to those from other physicians on eight of nine clinical axes; in a pilot study with real-world medical questions, specialists preferred Med-PaLM 2 answers to generalist physician answers 65% of the time, and both specialists and generalists rated Med-PaLM 2 as safe as physician answers. |
| **Models** | Med-PaLM 2, built on base LLM improvements plus medical domain fine-tuning and new reasoning/grounding strategies via ensemble refinement and chain of retrieval. |
| **Downstream tasks** | `question answering`, `reasoning`, `clinical decision support`<br>Medical question answering including long-form questions and USMLE-style questions, with reasoning and grounding via chain of retrieval; real-world medical question pilot study and adversarial evaluation. |
| **Modalities** | `text` |
| **Pre-training** | `instruction tuning`<br>Base LLM improvements and medical domain fine-tuning; reasoning and grounding improved via ensemble refinement and chain-of-retrieval. |
| **Data** | Evaluation on the MedQA, MedMCQA, PubMedQA and MMLU clinical topics datasets, adversarial datasets designed to probe LLM limitations, and a pilot study using real-world medical questions; human evaluation framework spanning nine clinical axes with physician and specialist ratings of answer safety and preference.<br>**4** benchmarks · **9** clinical evaluation axes |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MedQA | accuracy | up to 86.5% (+19% over Med-PaLM) |  |
| Physician preference (human evaluation, nine clinical axes) | axes where physicians preferred Med-PaLM 2 answers | 8 of 9 clinical axes | Med-PaLM 2 answers preferred over those from other physicians |
| Real-world medical questions pilot | specialist preference for Med-PaLM 2 over generalist answers | 65% of the time | specialist answers still preferred overall; both groups rated Med-PaLM 2 as safe as physician answers |
| Adversarial datasets probing LLM limitations | multiple evaluation metrics | significant improvements over Med-PaLM (P < 0.001) | exact figures not stated in the abstract |

</details>

<a id="model-tripod-llm-202501"></a>
<details>
<summary><b>TRIPOD-LLM</b> — The TRIPOD-LLM reporting guideline for studies using large language models <i>(Nat. Med. 2025-01)</i></summary>

**[The TRIPOD-LLM reporting guideline for studies using large language models](https://www.nature.com/articles/s41591-024-03425-5)**

*Nat. Med.* · 2025-01 · Jack Gallifant & Danielle S Bitterman · [doi:10.1038/s41591-024-03425-5](https://doi.org/10.1038/s41591-024-03425-5)

| | |
| --- | --- |
| **Summary** | • TRIPOD-LLM extends the TRIPOD+AI statement into a reporting guideline tailored to the unique challenges LLMs pose in biomedical applications.<br>• The checklist comprises 19 main items and 50 subitems covering key aspects from title to discussion, with a modular format (14 main items and 32 subitems applicable across all categories) accommodating various LLM research designs and tasks.<br>• Developed through an expedited Delphi process and expert consensus, it emphasizes transparency, human oversight and task-specific performance reporting, and ships an interactive website for guideline completion and PDF generation. |
| **Models** | A reporting guideline, not a model: an extension of the TRIPOD+AI statement providing a comprehensive checklist of 19 main items and 50 subitems (14 main items and 32 subitems applicable across all categories) in a modular format covering title through discussion, with an interactive website (https://tripod-llm.vercel.app/) for completion and PDF generation. |
| **Modalities** | `text` |
| **Data** | The guideline's checklist structure: 19 main items and 50 subitems covering key aspects from title to discussion, with 14 main items and 32 subitems applicable across all LLM research designs and tasks; developed through an expedited Delphi process and expert consensus.<br>**19** main items · **50** subitems · **14** cross category main items · **32** cross category subitems |

</details>

<a id="model-craft-md-202501"></a>
<details>
<summary><b>CRAFT-MD</b> — An evaluation framework for clinical use of large language models in patient interaction tasks <i>(Nat. Med. 2025-01)</i></summary>

**[An evaluation framework for clinical use of large language models in patient interaction tasks](https://www.nature.com/articles/s41591-024-03328-5)**

*Nat. Med.* · 2025-01 · Shreya Johri & Pranav Rajpurkar · [doi:10.1038/s41591-024-03328-5](https://doi.org/10.1038/s41591-024-03328-5)

| | |
| --- | --- |
| **Summary** | • CRAFT-MD (Conversational Reasoning Assessment Framework for Testing in Medicine) evaluates clinical LLMs through natural dialogues using simulated AI agents in a controlled environment, instead of structured medical examinations.<br>• Applied to GPT-4, GPT-3.5, Mistral and LLaMA-2-7b across 12 medical specialties, it exposed limitations in conversational reasoning, history-taking and diagnostic accuracy, which persisted for GPT-4V's multimodal conversational and visual abilities.<br>• The paper proposes recommendations for future clinical LLM evaluation -- realistic doctor-patient conversations, comprehensive history-taking, open-ended questioning, and a combination of automated and expert evaluations. |
| **Models** | CRAFT-MD, a conversational evaluation framework in which simulated artificial intelligence agents interact with clinical LLMs (GPT-4, GPT-3.5, Mistral, LLaMA-2-7b; GPT-4V for multimodal assessment) in a controlled environment; introduces no new model. |
| **Downstream tasks** | `benchmarking`, `diagnosis`, `reasoning`<br>Simulated doctor-patient dialogue evaluation of clinical LLMs across 12 medical specialties, probing diagnostic accuracy, history-taking and conversational reasoning (including multimodal GPT-4V assessment), with recommendations for combining automated and expert evaluation. |
| **Modalities** | `text`, `multimodal` |
| **Data** | Natural-dialogue evaluations of GPT-4, GPT-3.5, Mistral and LLaMA-2-7b across 12 medical specialties, plus multimodal conversational and visual assessment of GPT-4V, probing diagnostic capability, history-taking and conversational reasoning.<br>**12** medical specialties · **4** models evaluated |

</details>

<a id="model-equity-harms-and-bias-toolbox-202412"></a>
<details>
<summary><b>Equity harms and bias toolbox</b> — A toolbox for surfacing health equity harms and biases in large language models <i>(Nat. Med. 2024-12)</i></summary>

**[A toolbox for surfacing health equity harms and biases in large language models](https://www.nature.com/articles/s41591-024-03258-2)**

*Nat. Med.* · 2024-12 · Stephen R Pfohl & Karan Singhal · [doi:10.1038/s41591-024-03258-2](https://doi.org/10.1038/s41591-024-03258-2)

| | |
| --- | --- |
| **Summary** | • The toolbox provides a multifactorial framework for human assessment of biases in long-form, LLM-generated answers to medical questions, plus EquityMedQA, a collection of seven datasets enriched for adversarial queries.<br>• In a large-scale empirical case study with the Med-PaLM 2 LLM, the approach surfaced biases that narrower evaluation approaches may miss.<br>• The framework and datasets were grounded in an iterative participatory approach, underscoring the importance of diverse assessment methodologies and raters of varying backgrounds and expertise. |
| **Models** | A toolbox, not a trained model: a multifactorial framework for human assessment of equity-related biases in long-form LLM-generated medical answers, applied in a large-scale empirical case study with the Med-PaLM 2 LLM and grounded in an iterative participatory approach; includes EquityMedQA, seven datasets enriched for adversarial queries. |
| **Downstream tasks** | `benchmarking`<br>Surfacing equity-related harms and biases in long-form LLM-generated answers to medical questions via a multifactorial human assessment framework and adversarial-query-enriched datasets (EquityMedQA), demonstrated empirically on Med-PaLM 2. |
| **Modalities** | `text` |
| **Data** | EquityMedQA, a collection of seven datasets enriched for adversarial queries about health equity, evaluated alongside the multifactorial human assessment framework on long-form Med-PaLM 2 answers to medical questions in a large-scale empirical case study.<br>**7** datasets |

</details>

<a id="model-speakfaster-202411"></a>
<details>
<summary><b>SpeakFaster</b> — Using large language models to accelerate communication for eye gaze typing users with ALS <i>(Nat. Commun. 2024-11)</i></summary>

**[Using large language models to accelerate communication for eye gaze typing users with ALS](https://www.nature.com/articles/s41467-024-53873-3)**

*Nat. Commun.* · 2024-11 · Shanqing Cai & Michael P Brenner · [doi:10.1038/s41467-024-53873-3](https://doi.org/10.1038/s41467-024-53873-3)

| | |
| --- | --- |
| **Summary** | • SpeakFaster is an LLM-powered user interface for augmentative and alternative communication that lets users type in a highly abbreviated form, saving 57% more motor actions than traditional predictive keyboards in offline simulation.<br>• A pilot study on a mobile device with 19 non-AAC participants demonstrated motor savings in line with the simulation and relatively small changes in typing speed.<br>• Lab and field testing with two eye-gaze AAC users with amyotrophic lateral sclerosis demonstrated text-entry rates 29-60% above baselines, driven by savings of expensive keystrokes based on LLM predictions. |
| **Models** | SpeakFaster, an LLM-powered user interface for abbreviated text entry in augmentative and alternative communication. |
| **Downstream tasks** | `patient communication`, `generation`<br>Abbreviated text entry and keystroke prediction to accelerate communication in augmentative and alternative communication (AAC). |
| **Modalities** | `text` |
| **Pre-training** | `none` |
| **Data** | Offline simulation of text entry; a pilot study on a mobile device with 19 non-AAC participants; and lab and field testing with two eye-gaze AAC users with amyotrophic lateral sclerosis.<br>**19** non aac participants · **2** aac users with als |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Offline simulation of AAC text entry | motor action savings vs. traditional predictive keyboards | 57% |  |
| Lab and field testing on two eye-gaze AAC users with ALS | text-entry rate increase vs. baselines | 29-60% |  |

</details>

<a id="model-gpt-4v-202411"></a>
<details>
<summary><b>GPT-4V</b> — In-context learning enables multimodal large language models to classify cancer pathology images <i>(Nat. Commun. 2024-11)</i></summary>

**[In-context learning enables multimodal large language models to classify cancer pathology images](https://www.nature.com/articles/s41467-024-51465-9)**

*Nat. Commun.* · 2024-11 · Dyke Ferber & Jakob Nikolas Kather · [doi:10.1038/s41467-024-51465-9](https://doi.org/10.1038/s41467-024-51465-9)

| | |
| --- | --- |
| **Summary** | • The authors systematically evaluated GPT-4V (Generative Pretrained Transformer 4 with Vision capabilities) with in-context learning on three cancer histopathology tasks: tissue subtype classification in colorectal cancer, colon polyp subtyping, and breast tumor detection in lymph node sections.<br>• In-context learning was sufficient to match or even outperform specialized neural networks trained for particular tasks, while requiring only a minimal number of samples and no parameter updates.<br>• The results demonstrate that large vision-language models trained on non-domain-specific data can be applied out-of-the-box to histopathology, democratizing access to generalist AI for medical experts, especially where annotated data is scarce. |
| **Models** | GPT-4V (Generative Pretrained Transformer 4 with Vision capabilities), a multimodal large language model applied with in-context learning and no parameter updates. |
| **Downstream tasks** | `classification`, `subtyping`, `detection`<br>Classification of tissue subtypes in colorectal cancer, colon polyp subtyping, and breast tumor detection in lymph node sections via in-context learning. |
| **Modalities** | `histopathology`, `text`, `multimodal` |
| **Pre-training** | `none`<br>Applied via in-context learning with no parameter updates; the underlying model was trained on non-domain-specific data. |
| **Data** | Three cancer histopathology tasks of high importance: classification of tissue subtypes in colorectal cancer, colon polyp subtyping, and breast tumor detection in lymph node sections, evaluated with GPT-4V using in-context learning.<br>**3** histopathology tasks |

</details>

<a id="model-ai-involvement-perception-study-202411"></a>
<details>
<summary><b>AI-involvement perception study</b> — Influence of believed AI involvement on the perception of digital medical advice <i>(Nat. Med. 2024-11)</i></summary>

**[Influence of believed AI involvement on the perception of digital medical advice](https://www.nature.com/articles/s41591-024-03180-7)**

*Nat. Med.* · 2024-11 · Moritz Reis & Wilfried Kunde · [doi:10.1038/s41591-024-03180-7](https://doi.org/10.1038/s41591-024-03180-7)

| | |
| --- | --- |
| **Summary** | • Two preregistered studies (n = 2,280) presented participants with scenarios of patients obtaining medical advice, with identical information but a manipulated putative source ('AI', 'human physician', 'human + AI').<br>• Advice labeled as involving AI was rated significantly less reliable and less empathetic than 'human'-labeled advice, and participants were less willing to follow it -- an anti-AI bias that persisted even when AI was supposedly supervised by physicians. |
| **Models** | No model introduced: two preregistered behavioral studies (n = 2,280) presenting scenarios of patients obtaining medical advice, with identical information and a manipulated putative source ('AI', 'human physician', 'human + AI'). |
| **Modalities** | `text` |
| **Data** | Two preregistered studies (n = 2,280 participants total) presenting scenarios of patients obtaining medical advice; all participants received identical information while the putative source of the advice ('AI', 'human physician', 'human + AI') was manipulated.<br>**2,280** participants · **2** preregistered studies |

</details>

<a id="model-gpt-3-5-turbo-gpt-4-turbo-202410"></a>
<details>
<summary><b>GPT-3.5-turbo / GPT-4-turbo</b> — Evaluating the use of large language models to provide clinical recommendations in the Emergency Department <i>(Nat. Commun. 2024-10)</i></summary>

**[Evaluating the use of large language models to provide clinical recommendations in the Emergency Department](https://www.nature.com/articles/s41467-024-52415-1)**

*Nat. Commun.* · 2024-10 · Christopher Y K Williams & Atul J Butte · [doi:10.1038/s41467-024-52415-1](https://doi.org/10.1038/s41467-024-52415-1)

| | |
| --- | --- |
| **Summary** | • The authors conducted a highly powered study on 10,000 randomly selected Emergency Department visits to test whether zero-shot GPT-3.5-turbo and GPT-4-turbo could provide clinical recommendations for three tasks: admission status, radiological investigation request status, and antibiotic prescription status, across four prompting strategies.<br>• Both LLMs performed poorly compared with a resident physician, with average accuracy 8% (GPT-4-turbo) and 24% (GPT-3.5-turbo) lower.<br>• The LLMs tended to be overly cautious, with high sensitivity at the cost of specificity, leading the authors to conclude that LLM performance must improve significantly before deployment as decision support systems. |
| **Models** | Zero-shot GPT-3.5-turbo and GPT-4-turbo generating clinical recommendations from Emergency Department clinical notes under four prompting strategies. |
| **Downstream tasks** | `clinical decision support`, `triage`<br>Generation of clinical recommendations for admission status, radiological investigation request status, and antibiotic prescription status from Emergency Department clinical notes. |
| **Modalities** | `text`, `EHR` |
| **Pre-training** | `none`<br>Zero-shot prompting of GPT-3.5-turbo and GPT-4-turbo; no fine-tuning. |
| **Data** | 10,000 randomly selected Emergency Department visits; clinical notes were used to evaluate LLM recommendations for admission status, radiological investigation request status, and antibiotic prescription status across four prompting strategies.<br>**10,000** emergency department visits |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Clinical recommendation accuracy on 10,000 ED visits vs. a resident physician | average accuracy difference vs. physician | GPT-4-turbo 8% lower; GPT-3.5-turbo 24% lower |  |

</details>

<a id="model-sspec-202410"></a>
<details>
<summary><b>SSPEC</b> — Outpatient reception via collaboration between nurses and a large language model: a randomized controlled trial <i>(Nat. Med. 2024-10)</i></summary>

**[Outpatient reception via collaboration between nurses and a large language model: a randomized controlled trial](https://www.nature.com/articles/s41591-024-03148-7)**

*Nat. Med.* · 2024-10 · Peixing Wan & Erping Long · [doi:10.1038/s41591-024-03148-7](https://doi.org/10.1038/s41591-024-03148-7)

| | |
| --- | --- |
| **Summary** | • SSPEC, a site-specific prompt-engineering chatbot, was developed on 35,418 real-world conversation audio cases from 10 reception sites across two medical centers and resolved a higher proportion of queries in fewer rounds than nurse-led sessions (68.0% versus 50.5% within 2 rounds, P = 0.009).<br>• In a single-center randomized controlled trial with 2,164 participants, the nurse-SSPEC collaboration model received significantly higher patient satisfaction than the nurse group (3.91 +/- 0.90 versus 3.39 +/- 1.15, P < 0.001).<br>• Secondary outcomes favored the collaboration model on repeated query-response rate (3.2% versus 14.4%), negative emotions (2.4% versus 7.8%) and response integrity, empathy and readability. |
| **Models** | SSPEC, a site-specific prompt-engineering chatbot built on a curated corpus of 35,418 real-world conversation audio cases between outpatients and receptionist nurses from 10 reception sites across two medical centers, deployed within a nurse-SSPEC collaboration model that oversees uncertainties during real-world reception. |
| **Downstream tasks** | `triage`, `patient communication`, `question answering`<br>Resolving outpatient reception queries (administrative, triaging and primary care concerns) with fewer rounds of queries and responses than nurse-led sessions, deployed as a nurse-SSPEC collaboration model and evaluated in a single-center randomized controlled trial. |
| **Modalities** | `text`, `audio` |
| **Data** | 35,418 real-world conversation audio cases between outpatients and receptionist nurses from 10 reception sites across two medical centers (administrative, triaging and primary care concerns), used to develop SSPEC; single-center randomized controlled trial with 2,164 participants comparing the nurse-SSPEC collaboration model against nurse-only reception. Chinese Clinical Trial Registry identifier ChiCTR2300077245.<br>**35,418** conversation audio cases · **10** reception sites · **2,164** rct participants |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Queries resolved within 2 query-response rounds, SSPEC vs. nurse-led sessions | percentage of queries | 68.0% vs 50.5% (P = 0.009) |  |
| RCT primary endpoint, patient satisfaction, nurse-SSPEC vs. nurse-only (2,164 participants) | mean satisfaction score | 3.91 +/- 0.90 vs 3.39 +/- 1.15 (P < 0.001) |  |
| RCT secondary, repeated query-response rate | percentage | 3.2% vs 14.4% (P < 0.001) |  |
| RCT secondary, negative emotions during visits | percentage | 2.4% vs 7.8% (P < 0.001) |  |
| RCT secondary, response quality (integrity / empathy / readability) | mean score | integrity 4.37 vs 3.42; empathy 4.14 vs 3.27 (P < 0.001); readability 3.86 vs 3.71 (P = 0.006) |  |

</details>

<a id="model-deepdr-llm-202410"></a>
<details>
<summary><b>DeepDR-LLM</b> — Integrated image-based deep learning and language models for primary diabetes care <i>(Nat. Med. 2024-10)</i></summary>

**[Integrated image-based deep learning and language models for primary diabetes care](https://www.nature.com/articles/s41591-024-03139-8)**

*Nat. Med.* · 2024-10 · Jiajia Li & Tien Yin Wong · [doi:10.1038/s41591-024-03139-8](https://doi.org/10.1038/s41591-024-03139-8)

| | |
| --- | --- |
| **Summary** | • DeepDR-LLM combines a large language model module with an image-based deep learning system (DeepDR-Transformer) to provide individualized diabetes management recommendations and diabetic retinopathy (DR) screening support to primary care physicians.<br>• In retrospective evaluation, the LLM module performed comparably to primary care physicians (PCPs) and endocrinology residents in English, and outperformed PCPs with performance comparable to endocrinology residents in Chinese.<br>• In a single-center real-world prospective study, patients with newly diagnosed diabetes in the PCP+DeepDR-LLM arm showed better self-management behaviors (P < 0.05) and patients with referral DR showed better DR referral adherence (P < 0.01), while recommendation quality and empathy improved. |
| **Models** | DeepDR-LLM integrates a large language model module with DeepDR-Transformer, an image-based deep learning system, to provide individualized diabetes management recommendations and diabetic retinopathy screening support. |
| **Downstream tasks** | `diagnosis`, `triage`, `clinical decision support`<br>Individualized diabetes management recommendations for PCPs; referable diabetic retinopathy identification and screening; referral support for primary diabetes care. |
| **Modalities** | `fundus`, `text` |
| **Data** | Retrospective evaluation tested the LLM module in English and Chinese; a single-center real-world prospective study compared 397 patients in the unassisted PCP arm with 372 patients in the PCP+DeepDR-LLM arm, assessing diabetes self-management behaviors and DR referral adherence.<br>**769** patients |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Referable DR identification by PCPs | accuracy | 92.3% (assisted by DeepDR-Transformer) vs 81.0% unassisted |  |
| Diabetes self-management behaviors in newly diagnosed patients | statistical significance | P < 0.05 | Better self-management behaviors in the PCP+DeepDR-LLM arm |
| DR referral adherence in patients with referral DR | statistical significance | P < 0.01 | Higher adherence in the PCP+DeepDR-LLM arm |

</details>

<a id="model-clinical-decision-making-simulation-framework-202409"></a>
<details>
<summary><b>Clinical decision-making simulation framework</b> — Evaluation and mitigation of the limitations of large language models in clinical decision-making <i>(Nat. Med. 2024-09)</i></summary>

**[Evaluation and mitigation of the limitations of large language models in clinical decision-making](https://www.nature.com/articles/s41591-024-03097-1)**

*Nat. Med.* · 2024-09 · Paul Hager & Daniel Rueckert · [doi:10.1038/s41591-024-03097-1](https://doi.org/10.1038/s41591-024-03097-1)

| | |
| --- | --- |
| **Summary** | • The authors created a curated dataset based on the Medical Information Mart for Intensive Care (MIMIC) database spanning 2,400 real patient cases and four common abdominal pathologies, plus a framework to simulate a realistic clinical setting.<br>• Current state-of-the-art LLMs did not accurately diagnose patients (performing significantly worse than physicians), followed neither diagnostic nor treatment guidelines, and could not interpret laboratory results.<br>• LLMs often failed to follow instructions and were sensitive to the quantity and order of information, indicating they are not yet ready for autonomous clinical decision-making. |
| **Models** | A curated dataset derived from the MIMIC database combined with a framework for simulating a realistic clinical decision-making setting; the paper introduces an evaluation benchmark rather than a model. |
| **Downstream tasks** | `diagnosis`, `reasoning`, `benchmarking`, `clinical decision support`<br>Simulated clinical decision-making covering information gathering, diagnosis, adherence to diagnostic and treatment guidelines, interpretation of laboratory results, and integration into clinical workflows. |
| **Modalities** | `text`, `EHR` |
| **Data** | Curated dataset based on the MIMIC database spanning 2,400 real patient cases and four common abdominal pathologies, used with a framework that simulates a realistic clinical decision-making environment to evaluate LLM diagnosis, guideline adherence, laboratory interpretation and workflow integration.<br>**2,400** patient cases |

</details>

<a id="model-skingpt-4-202407"></a>
<details>
<summary><b>SkinGPT-4</b> — Pre-trained multimodal large language model enhances dermatological diagnosis using SkinGPT-4 <i>(Nat. Commun. 2024-07)</i></summary>

**[Pre-trained multimodal large language model enhances dermatological diagnosis using SkinGPT-4](https://www.nature.com/articles/s41467-024-50043-3)**

*Nat. Commun.* · 2024-07 · Juexiao Zhou & Xin Gao · [doi:10.1038/s41467-024-50043-3](https://doi.org/10.1038/s41467-024-50043-3)

| | |
| --- | --- |
| **Summary** | • SkinGPT-4 is an interactive dermatology diagnostic system based on a multimodal large language model that aligns a pre-trained vision transformer with Llama-2-13b-chat using 52,929 skin disease images, clinical concepts, and doctors' notes via a two-step training strategy.<br>• Users can upload their own skin photos for diagnosis, and the system autonomously evaluates the images, identifies the characteristics and categories of the skin conditions, performs in-depth analysis, and provides interactive treatment recommendations.<br>• The system was quantitatively evaluated on 150 real-life cases with board-certified dermatologists. |
| **Models** | SkinGPT-4, an interactive dermatology diagnostic system aligning a pre-trained vision transformer with the Llama-2-13b-chat large language model. |
| **Downstream tasks** | `diagnosis`, `classification`, `clinical decision support`<br>Autonomous evaluation of uploaded skin photos, identification of the characteristics and categories of skin conditions, in-depth analysis, and interactive treatment recommendations. |
| **Modalities** | `clinical photography`, `text`, `multimodal` |
| **Pre-training** | `instruction tuning`<br>A pre-trained vision transformer was aligned with Llama-2-13b-chat using 52,929 skin disease images paired with clinical concepts and doctors' notes, via a two-step training strategy. |
| **Data** | 52,929 publicly available and proprietary skin disease images collected together with clinical concepts and doctors' notes and used to align a pre-trained vision transformer with Llama-2-13b-chat; the system was evaluated on 150 real-life cases with board-certified dermatologists.<br>**52,929** skin disease images · **150** real life cases |

</details>

<a id="model-medic-202406"></a>
<details>
<summary><b>MEDIC</b> — Large language models for preventing medication direction errors in online pharmacies <i>(Nat. Med. 2024-06)</i></summary>

**[Large language models for preventing medication direction errors in online pharmacies](https://www.nature.com/articles/s41591-024-02933-8)**

*Nat. Med.* · 2024-06 · Cristobal Pais & Mohsen Bayati · [doi:10.1038/s41591-024-02933-8](https://doi.org/10.1038/s41591-024-02933-8)

| | |
| --- | --- |
| **Summary** | • MEDIC (medication direction copilot) emulates pharmacist reasoning by fine-tuning a first-generation LLM on 1,000 expert-annotated and augmented medication directions from Amazon Pharmacy to extract core components such as dosage and frequency, then assembling complete directions with pharmacy logic and safety guardrails.<br>• On 1,200 expert-reviewed prescriptions, two LLM-based benchmarks recorded 1.51 (CI 1.03, 2.31) and 4.38 (CI 3.13, 6.64) times more near-miss events than MEDIC.<br>• Deployed in a production online pharmacy system, MEDIC reduced near-miss events by 33% (CI 26%, 40%). |
| **Models** | MEDIC fine-tunes a first-generation large language model with expert-annotated and augmented medication directions, combining extraction of core prescription components with pharmacy logic and safety guardrails. |
| **Downstream tasks** | `information extraction`, `generation`<br>Extracting core clinical components (e.g., dosage and frequency) from prescriptions and assembling complete medication directions using pharmacy logic and safety guardrails. |
| **Modalities** | `text` |
| **Pre-training** | `supervised`<br>Fine-tuned a first-generation LLM on 1,000 expert-annotated and augmented medication directions from Amazon Pharmacy. |
| **Data** | 1,000 expert-annotated and augmented medication directions from Amazon Pharmacy for fine-tuning; evaluation on 1,200 expert-reviewed prescriptions; one comparison benchmark leveraged 1.5 million medication directions, the other used state-of-the-art LLMs.<br>**1,000** annotated directions · **1,500,000** benchmark directions · **1,200** expert reviewed prescriptions |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Expert-reviewed prescriptions (1.5M-direction LLM benchmark) | relative near-miss events | 1.51x more than MEDIC (CI 1.03, 2.31) | Near-miss events are errors caught and corrected before reaching the patient |
| Expert-reviewed prescriptions (state-of-the-art LLM benchmark) | relative near-miss events | 4.38x more than MEDIC (CI 3.13, 6.64) |  |
| Production online pharmacy deployment | reduction in near-miss events | 33% (CI 26%, 40%) |  |

</details>

<a id="model-chatgpt-ada-202402"></a>
<details>
<summary><b>ChatGPT ADA</b> — Large language models streamline automated machine learning for clinical studies <i>(Nat. Commun. 2024-02)</i></summary>

**[Large language models streamline automated machine learning for clinical studies](https://www.nature.com/articles/s41467-024-45879-8)**

*Nat. Commun.* · 2024-02 · Soroosh Tayebi Arasteh & Sven Nebelung · [doi:10.1038/s41467-024-45879-8](https://doi.org/10.1038/s41467-024-45879-8)

| | |
| --- | --- |
| **Summary** | • ChatGPT ADA (Advanced Data Analysis), an extension of GPT-4, was given real-world clinical datasets and study details from large trials across various medical specialties without specific guidance and autonomously developed machine learning models to predict clinical outcomes.<br>• Predicted outcomes included cancer development, cancer progression, disease complications and biomarkers such as pathogenic gene sequences.<br>• In head-to-head comparisons after re-implementation and optimization, ChatGPT ADA-crafted models showed no significant differences in traditional performance metrics versus manually crafted counterparts (p >= 0.072) and often outperformed them. |
| **Models** | ChatGPT ADA (Advanced Data Analysis), an extension of GPT-4 that autonomously performs end-to-end machine learning analysis on clinical datasets and study details. |
| **Downstream tasks** | `risk prediction`, `biomarker prediction`<br>Autonomous development of machine learning models to predict clinical outcomes and biomarkers from real-world clinical trial datasets. |
| **Modalities** | `EHR`, `text` |
| **Data** | Real-world clinical datasets and study details from large trials across various medical specialties, used to develop ML models that predict clinical outcomes such as cancer development, cancer progression, disease complications and biomarkers such as pathogenic gene sequences. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Head-to-head comparison of ChatGPT ADA-crafted vs manually crafted ML models | p-value for differences in traditional performance metrics | p >= 0.072 (no significant differences) | ChatGPT ADA-crafted models often outperformed their counterparts |

</details>

<a id="model-limbic-202402"></a>
<details>
<summary><b>Limbic</b> — Closing the accessibility gap to mental health treatment with a personalized self-referral chatbot <i>(Nat. Med. 2024-02)</i></summary>

**[Closing the accessibility gap to mental health treatment with a personalized self-referral chatbot](https://www.nature.com/articles/s41591-023-02766-x)**

*Nat. Med.* · 2024-02 · Johanna Habicht & Max Rollwage · [doi:10.1038/s41591-023-02766-x](https://doi.org/10.1038/s41591-023-02766-x)

| | |
| --- | --- |
| **Summary** | • In a multisite observational study of 129,400 patients within England's NHS services, services that used a personalized AI-enabled self-referral chatbot saw substantially increased referrals (15% increase) versus control services (6% increase).<br>• The increase was particularly pronounced in minorities, including nonbinary (179% increase) and ethnic minority (29% increase) individuals.<br>• Natural language processing of qualitative feedback from 42,332 individuals suggested the chatbot's human-free nature and patients' self-realization of their treatment need drove the improved diversity of access. |
| **Models** | A personalized AI-enabled self-referral chatbot deployed in NHS mental health services; an observational deployment study rather than a model-development paper. |
| **Downstream tasks** | `triage`, `patient communication`<br>Personalized self-referral for mental health services, gathering patient information to support referral and increasing referral diversity. |
| **Modalities** | `text` |
| **Data** | Multisite observational study of 129,400 patients within England's NHS services comparing referral volume and diversity in ethnicity, gender and sexual orientation between services using the chatbot and control services; qualitative feedback from 42,332 individuals analyzed with natural language processing.<br>**129,400** patients · **42,332** qualitative feedback responses |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| Referral increase (chatbot services vs control services) | referral increase | 15% vs 6% |  |
| Nonbinary individual referrals | referral increase | 179% |  |
| Ethnic minority individual referrals | referral increase | 29% |  |

</details>

<a id="model-reporting-standards-checklist-202312"></a>
<details>
<summary><b>Reporting standards checklist</b> — Reporting standards for the use of large language model-linked chatbots for health advice <i>(Nat. Med. 2023-12)</i></summary>

**[Reporting standards for the use of large language model-linked chatbots for health advice](https://www.nature.com/articles/s41591-023-02656-2)**

*Nat. Med.* · 2023-12 · Bright Huo & Gordon Guyatt · [doi:10.1038/s41591-023-02656-2](https://doi.org/10.1038/s41591-023-02656-2)

| | |
| --- | --- |
| **Summary** | • Presents a checklist for reporting the use of LLM-linked chatbots for health advice, covering transparency, accountability and evaluation.<br>• The checklist was developed through expert consensus. |
| **Modalities** | `text` |
| **Data** | Reporting-standards checklist for the use of LLM-linked chatbots for health advice, developed through expert consensus; no dataset or cohort. |

</details>

<a id="model-medical-device-regulatory-commentary-202310"></a>
<details>
<summary><b>Medical device regulatory commentary</b> — Large language model AI chatbots require approval as medical devices <i>(Nat. Med. 2023-10)</i></summary>

**[Large language model AI chatbots require approval as medical devices](https://www.nature.com/articles/s41591-023-02412-6)**

*Nat. Med.* · 2023-10 · Stephen Gilbert & Paul Wicks · [doi:10.1038/s41591-023-02412-6](https://doi.org/10.1038/s41591-023-02412-6)

| | |
| --- | --- |
| **Summary** | • Argues that AI-powered chatbots used in patient care are regulated as medical devices, but their unreliability currently precludes approval as such. |
| **Modalities** | `text` |
| **Data** | Commentary on the regulatory status of AI-powered chatbots used in patient care; no dataset or cohort. |

</details>

<a id="model-med-palm-202307"></a>
<details>
<summary><b>Med-PaLM</b> — Large language models encode clinical knowledge <i>(Nature 2023-07)</i></summary>

**[Large language models encode clinical knowledge](https://www.nature.com/articles/s41586-023-06291-2)**

*Nature* · 2023-07 · Karan Singhal & Vivek Natarajan · [doi:10.1038/s41586-023-06291-2](https://doi.org/10.1038/s41586-023-06291-2)

| | |
| --- | --- |
| **Summary** | • Med-PaLM, a 540-billion-parameter LLM adapted from PaLM for the medical domain, was the first LLM to exceed a passing score on United States Medical Licensing Examination style questions.<br>• On MultiMedQA, a benchmark combining seven existing open question answering datasets, Med-PaLM achieved 67.6% accuracy on MedQA-USMLE, below clinician performance (86.5%).<br>• Human evaluation of long-form answers found clinician raters preferred Med-PaLM answers to those produced by physicians on 9 of 14 axes, with noted limitations including lower levels of consensus. |
| **Models** | Med-PaLM, a 540-billion-parameter large language model adapted from the PaLM LLM for the medical domain. |
| **Parameters** | 540B |
| **Downstream tasks** | `question answering`, `reasoning`<br>Medical question answering on professional exams, research and consumer queries, including evaluation of long-form answers. |
| **Modalities** | `text` |
| **Pre-training** | `instruction tuning`<br>Med-PaLM is adapted from the PaLM large language model for the medical domain. |
| **Data** | MultiMedQA, a benchmark combining seven existing open question answering datasets spanning professional medical exams, research and consumer queries, plus a newly introduced dataset of 3,150 manually curated consumer medical questions.<br>**7** datasets · **3,150** consumer medical questions |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| MedQA-USMLE | accuracy | 67.6% (clinician performance 86.5%) |  |
| Long-form answer human evaluation | axes preferred by clinician raters | 9 of 14 | Clinician raters preferred Med-PaLM answers to those produced by physicians, with noted limitations including lower levels of consensus. |

</details>

<a id="model-nyutron-202306"></a>
<details>
<summary><b>NYUTron</b> — Health system-scale language models are all-purpose prediction engines <i>(Nature 2023-06)</i></summary>

**[Health system-scale language models are all-purpose prediction engines](https://www.nature.com/articles/s41586-023-06160-y)**

*Nature* · 2023-06 · Lavender Yao Jiang & Eric Karl Oermann · [doi:10.1038/s41586-023-06160-y](https://doi.org/10.1038/s41586-023-06160-y)

| | |
| --- | --- |
| **Summary** | • NYUTron is a framework for training large language models on longitudinal electronic health records (EHRs) using unlabeled training data, enabling all-purpose prediction of clinical outcomes from unstructured clinical notes.<br>• NYUTron identified patients at high risk of 30-day, all-cause, unplanned readmission with an AUROC of 0.797, a relative improvement of 5.36% over established machine learning baselines and 6.53% over physicians.<br>• The models also predicted mortality and a high probability of prolonged hospital stay across the NYU Langone Health system. |
| **Models** | NYUTron, a framework of scalable clinical large language models trained on unstructured notes from longitudinal electronic health records. |
| **Downstream tasks** | `risk prediction`, `prognosis`, `forecasting`<br>Prediction of 30-day all-cause unplanned readmission, mortality and high probability of prolonged hospital stay from longitudinal EHR text. |
| **Modalities** | `text`, `EHR` |
| **Pre-training** | `next-token prediction`<br>Trained on unstructured clinical notes from longitudinal EHRs using unlabeled training data across the NYU Langone Health system. |
| **Data** | Longitudinal electronic health records across the health system of NYU Langone Health, used to train scalable clinical language models on unstructured clinical notes with unlabeled training data. The abstract reports no cohort or dataset size. |

**Reported performance**

| Benchmark | Metric | Value | Note |
| --- | --- | --- | --- |
| 30-day all-cause unplanned readmission | AUROC | 0.797 | Relative improvement of 5.36% over established machine learning baselines and 6.53% over physicians. |

</details>

---

This page is generated. Add a paper by editing [`data/LLM.yaml`](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/data/LLM.yaml) in the [pipeline repository](https://github.com/1nslyn/biomedical-ai-pipeline) and rebuilding — edits made here are overwritten. The schema and house rules are in [CONTRIBUTING.md](https://github.com/1nslyn/biomedical-ai-pipeline/blob/main/CONTRIBUTING.md).
