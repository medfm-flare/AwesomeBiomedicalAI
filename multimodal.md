**Maintainer:** @Yeonwoo Seo

# Multimodal AI

Cross-modal health models without a single dominant biomedical domain.

| Date | Title | First & Last Authors | Model | Network Backbone | Pre-training Method | Training Data | Downstream Tasks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 202607 | [Learning the shared structure of human health across diseases, modalities, and time](https://doi.org/10.64898/2026.07.07.26357373) (medRxiv) | [Paul Hager](https://scholar.google.com/citations?user=LeI7UOYAAAAJ&hl=en&oi=ao) & [Francesco Paolo Casale](https://scholar.google.com/citations?user=AUFp6j4AAAAJ&hl=en&oi=ao) | [RisQ](https://github.com/RisQ-Lab/RisQ) | Transformer | N/A | UK Biobank | Disease risk prediction |
| 202604 | [A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/pdf/2604.18570) (arXiv) | [Andrew Zhang](https://scholar.google.com/citations?user=WDiKxmcAAAAJ&hl=en) & [Faisal Mahmood](https://scholar.google.com/citations?user=9MsdbKoAAAAJ&hl=en) | APOLLO | Transformer | masking & reconstruction objectives | MGB-7M (7,155,044 patient EHR / 25,296,943,893 distinct medical events) | 322 downstream tasks - patient retrieval (61 cohorts), predicting new disease onset (95 tasks), disease progression (78 tasks), treatment response (59 tasks), drug adverse events (17 tasks), hospital operations endpoints (12 tasks) |
| 202601 | [Multimodal learning with next-token prediction for large multimodal models](https://www.nature.com/articles/s41586-025-10041-x) (Nature) | [Xinlong Wang](https://scholar.google.com/citations?user=DPz0DjYAAAAJ) & [Tiejun Huang](https://scholar.google.com/citations?user=knvEK4AAAAAJ) | [Emu3](https://github.com/baaivision/Emu3) | Transformer (Decoder-only) | Next-token prediction (Autoregressive) | Large-scale multimodal dataset (~3PB) | Image generation, video generation, vision-language understanding |
