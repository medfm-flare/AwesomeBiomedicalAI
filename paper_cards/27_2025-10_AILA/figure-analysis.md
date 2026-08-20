# AFMBench: figure analysis

**Language: English**

Paper: Mandal I, Soni J, Zaki M, et al. *Evaluating large language model agents for automation of atomic force microscopy*. **Nature Communications**. 2025;16:9104. [DOI](https://doi.org/10.1038/s41467-025-64105-7)

![Figure 1 — multi-agent architecture, physical instrument, and trajectory](figures/afmbench_fig1.png)

- **Purpose:** panel a shows routing among agents and tools, panel b the real AFM, and panel c the natural-language-to-tool execution trajectory.
- **Reusable pattern:** pair architecture with the physical/clinical environment and one complete trajectory to show that the benchmark is not text QA alone.
- **Boundary:** one trajectory demonstrates executability, not aggregate reliability.

![Figure 2 — benchmark composition and task overlap](figures/afmbench_fig2.png)

- **Purpose:** report single/multi-tool, single/multi-agent, and basic/advanced proportions; show task counts by module; use a Venn diagram for Documentation, Analysis, and Calculation overlap.
- **Reusable pattern:** publish task difficulty and tool requirements before model outcomes.
- **Limitation:** Venn area may not be proportional and does not scale beyond three clear sets.

![Figure 3 — performance, efficiency, and task strata](figures/afmbench_fig3.png)

- **Purpose:** combine domain overlaps, tool/step/token/success/latency metrics, and accuracy stratified by tool, difficulty, and agent count.
- **Reusable pattern:** close the loop between performance, resource cost, and task complexity; repeated-trial points are more informative than a single bar.

## Evidence boundary
