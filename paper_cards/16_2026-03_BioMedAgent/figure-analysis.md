# BioMedAgent: figure analysis

**Language: English**

Paper: Bu D, Sun J, Li K, et al. *Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses*. **Nature Biomedical Engineering**. 2026. [DOI](https://doi.org/10.1038/s41551-026-01634-6)

![Figure 1 — inputs, planner–programmer–executor loop, and benchmark taxonomy](figures/biomedagent_fig1.png)

- **Purpose:** panel a describes the planner–programmer–executor loop, including failure return and tool updating; panel b presents the BioMed-AQA task hierarchy and construction.
- **Reusable pattern:** put system workflow and benchmark composition in two coordinated panels while keeping their roles distinct.
- **Limitation:** the information density suits a full-page figure, not a narrow column.

![Figure 2 — success rates, task-level states, and ablation](figures/biomedagent_fig2.png)

- **Purpose:** a summary table reports overall/category success; a concentric task plot encodes success/failure, wins, plan length, tools, and question type; remaining panels show step distributions and components.
- **Limitation:** the concentric encoding has high legend and color-learning costs and makes precise task lookup difficult.

![Figure 5 — item-level external BixBench comparison and capability table](figures/biomedagent_fig5.png)

- **Purpose:** the top compares two systems item by item; the table distinguishes biomedical agents by planning, coding, tools, scale, and scoring.
- **Reusable pattern:** external evaluation can show item-level differences rather than only one mean, while separately declaring system capability boundaries.
- **Boundary:** performance on external analysis questions does not substitute for clinical external validation or patient outcomes.

## Source boundary

This analysis is limited to the publisher's lawful preview and accessible figure/metadata surfaces. The article is under exclusive publisher rights, so this repository provides an access notice rather than redistributing the full PDF.
