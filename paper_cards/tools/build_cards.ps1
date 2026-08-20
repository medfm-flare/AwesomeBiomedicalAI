param(
    [Parameter(Mandatory = $true)]
    [string]$RepositoryRoot,
    [Parameter(Mandatory = $true)]
    [string]$WorkRoot,
    [Parameter(Mandatory = $true)]
    [string]$ReferenceRoot
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$cardsRoot = Join-Path $RepositoryRoot 'paper_cards'
New-Item -ItemType Directory -Force -Path $cardsRoot | Out-Null

function Write-Utf8([string]$Path, [string]$Content) {
    $parent = Split-Path -Parent $Path
    if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

function Clean-Field([string]$Text) {
    if (-not $Text) { return 'Not reported in the catalogue entry.' }
    $x = $Text -replace '<br\s*/?>', ' ' -replace '<[^>]+>', ' '
    $x = $x -replace '\[([^]]+)\]\([^)]+\)', '$1'
    $x = $x -replace '`', ''
    $x = [System.Net.WebUtility]::HtmlDecode($x)
    return (($x -replace '\s+', ' ').Trim())
}

function Parse-Catalogue([string]$Path) {
    $raw = Get-Content -LiteralPath $Path -Raw
    $blocks = [regex]::Matches($raw, '(?s)<details>(.*?)</details>')
    $result = @{}
    foreach ($m in $blocks) {
        $block = $m.Groups[1].Value
        $summary = [regex]::Match($block, '<summary><b>(?<model>[^<]+)</b>\s+—\s+(?<title>.*?)\s+<i>\((?<venueDate>[^)]+)\)</i></summary>')
        $paper = [regex]::Match($block, '\*\*\[(?<title>[^]]+)\]\((?<url>[^)]+)\)\*\*')
        if (-not $summary.Success -or -not $paper.Success) { continue }
        $fields = @{}
        foreach ($line in ($block -split "`r?`n")) {
            $fm = [regex]::Match($line, '^\| \*\*(?<name>[^*]+)\*\* \| (?<value>.*) \|$')
            if ($fm.Success) { $fields[$fm.Groups['name'].Value] = Clean-Field $fm.Groups['value'].Value }
        }
        $result[$summary.Groups['model'].Value] = [pscustomobject]@{
            Model = $summary.Groups['model'].Value
            Title = $paper.Groups['title'].Value
            Url = $paper.Groups['url'].Value
            VenueDate = $summary.Groups['venueDate'].Value
            Backbone = $fields['Backbone']
            Pretraining = $fields['Pre-training']
            DataUsage = $fields['Data usage']
            Tasks = $fields['Downstream tasks']
            Modalities = $fields['Modalities']
            Code = $fields['Code']
        }
    }
    return $result
}

function Get-Lenses([string]$Model) {
    $clinical = @('MIRA','AMIE','DeepRare','AgentMD','Oncology AI Agent','PHIA')
    $resource = @('Multi-Agent Architectures','Biomni','AlphaLab','SPARK','BioMedAgent','PantheonOS','BioDSA','AILA','MAP','SciToolAgent')
    $materials = @('AI X-ray Scientist','CIPHER','Autonomous Interaction','PhenoAssistant')
    if ($clinical -contains $Model) { return @('Methods','Clinical') }
    if ($materials -contains $Model) { return @('Methods','Materials / engineering') }
    if ($resource -contains $Model) { return @('Methods','Resource / benchmark') }
    return @('Methods','None')
}

function Get-CriticalRows([string]$Secondary, [string]$DataUsage) {
    if ($Secondary -eq 'Clinical') {
        return @(
            '| Retrospective or simulated evaluation can overstate deployment readiness | Workflow realism does not remove selection, documentation, and site effects | Run a prospective silent trial followed by a governed clinician-in-the-loop study | Population and evaluation setting described in the paper |',
            '| Aggregate accuracy can conceal calibration and subgroup failures | Clinical decisions require reliable uncertainty and equitable performance | Report calibration, abstention, subgroup effects, and error severity with confidence intervals | [Analysis] Clinical transfer boundary |'
        )
    }
    if ($Secondary -eq 'Materials / engineering') {
        return @(
            '| Demonstration performance may depend on one instrument, simulator, or operating envelope | Tool latency, calibration drift, and safety interlocks can dominate deployment | Repeat across instruments, operators, perturbations, and failure injections | [Analysis] Engineering transfer boundary |',
            '| Successful autonomy does not establish safe autonomy | Rare but hazardous actions may be absent from average metrics | Use red-team scenarios, hard action constraints, and audited rollback tests | [Analysis] Safety boundary |'
        )
    }
    return @(
        '| Results may be coupled to the chosen backbone, tool set, and prompt budget | Apparent architecture gains can disappear under matched compute or another model family | Run a factorial, budget-matched study across backbones and tool availability | [Analysis] System-dependence boundary |',
        '| Benchmark success may not measure reproducible scientific validity | Correct-looking outputs can contain hidden data leakage or execution errors | Use held-out tasks, trace audits, executable checks, and expert adjudication | [Analysis] Evaluation-validity boundary |'
    )
}

function Get-Idea([string]$Secondary, [string]$Model) {
    if ($Secondary -eq 'Clinical') {
        return "**Prospective guarded evaluation of $Model.** [Hypothesis] A calibrated abstention policy plus clinician approval will preserve most useful actions while reducing severe errors. Delta: add risk-tiered action permissions and uncertainty-triggered handoff. Validation: prospective silent deployment on an external site, followed by a preregistered clinician-in-the-loop comparison; primary endpoints are severe-error rate, calibration, time, and resource use. Falsifier: no reduction in severe errors or clinically important delay. Failure modes: workflow adaptation, alert fatigue, distribution shift. Innovation status: unverified; prior-art search required."
    }
    if ($Secondary -eq 'Materials / engineering') {
        return "**Constraint-first transfer test for $Model.** [Hypothesis] Explicit action envelopes and calibrated rollback will improve robustness under instrument drift without materially reducing task success. Delta: add hard safety constraints, state estimation, and failure recovery. Validation: matched runs across simulators and at least two physical systems with injected calibration and communication faults. Falsifier: unchanged unsafe-action rate or loss of task completion. Failure modes: over-constrained action space, hidden sensor faults, recovery loops. Innovation status: unverified; prior-art search required."
    }
    return "**Budget-matched external stress test for $Model.** [Hypothesis] The reported system advantage will remain detectable when model calls, tokens, tools, and wall-clock budget are matched and tasks are newly authored. Delta: replace the original benchmark-only comparison with preregistered external tasks and trace-level auditing. Validation: factorial comparison against a single-agent and strongest non-agent baseline across at least two backbone families; report success, cost, execution validity, and error severity. Falsifier: the advantage disappears under matched resources. Failure modes: benchmark construction bias, tool instability, evaluator disagreement. Innovation status: unverified; prior-art search required."
}

function Escape-Pipe([string]$Text) { return ($Text -replace '\|', '\|') }

function Build-PageGroundedCard($Entry, [string]$WorkName, [string]$FolderName) {
    $workDir = Join-Path $WorkRoot $WorkName
    $bundlePath = Join-Path $workDir 'source_bundle.json'
    $bundle = Get-Content -LiteralPath $bundlePath -Raw | ConvertFrom-Json
    $lenses = Get-Lenses $Entry.Model
    $primary = $lenses[0]
    $secondary = $lenses[1]
    $pageCount = [int]$bundle.page_count
    $figures = @($bundle.evidence_inventory.figures)
    $tables = @($bundle.evidence_inventory.tables)
    $equations = @($bundle.evidence_inventory.equations)
    $dest = Join-Path $cardsRoot $FolderName
    $figDest = Join-Path $dest 'figures'
    New-Item -ItemType Directory -Force -Path $figDest | Out-Null

    $copiedPages = @{}
    foreach ($fig in $figures) {
        if (-not $fig.pdf_page) { continue }
        $n = [int]$fig.pdf_page
        $name = 'page-{0:d3}.png' -f $n
        if (-not $copiedPages.ContainsKey($name)) {
            Copy-Item -LiteralPath (Join-Path $workDir "visual-assets\pages\$name") -Destination (Join-Path $figDest $name) -Force
            $copiedPages[$name] = $true
        }
    }
    if ($figures.Count -eq 0) {
        $name = 'page-001.png'
        Copy-Item -LiteralPath (Join-Path $workDir "visual-assets\pages\$name") -Destination (Join-Path $figDest $name) -Force
        $copiedPages[$name] = $true
    }

    $workflowVisuals = New-Object System.Collections.Generic.List[string]
    $resultVisuals = New-Object System.Collections.Generic.List[string]
    $figureAnalyses = New-Object System.Collections.Generic.List[string]
    for ($i = 0; $i -lt $figures.Count; $i++) {
        $fig = $figures[$i]
        $page = [int]$fig.pdf_page
        $name = 'page-{0:d3}.png' -f $page
        $caption = Clean-Field $fig.caption
        $block = "![$($fig.id) — faithful PDF page view](<$((Join-Path $figDest $name))>)`n`n*$($fig.id) is embedded as an unchanged PDF page view. It contributes $caption [Paper: PDF p. $page, $($fig.id)]*"
        if ($i -eq 0) { $workflowVisuals.Add($block) } else { $resultVisuals.Add($block) }
        $figureAnalyses.Add("## $($fig.id)`n`n![${($fig.id)} — faithful PDF page view](figures/$name)`n`n- **Argumentative role:** $caption`n- **Panel / visual logic:** Read the panel labels, axes, legends, and uncertainty marks before comparing conditions. The page view is retained so the full caption and neighbouring interpretation remain visible.`n- **Reusable design:** Preserve a one-to-one mapping among workflow stage, comparison, metric, and claim.`n- **Boundary:** This visual supports only the conditions and endpoints stated in the source; it does not establish transfer beyond the evaluated setting.`n- **Locator:** [Paper: PDF p. $page, $($fig.id)]")
    }
    if ($figures.Count -eq 0) {
        $workflowVisuals.Add("![Representative first-page view](<$((Join-Path $figDest 'page-001.png'))>)`n`n*No main figure was reliably inventoried by the PDF parser; this unchanged page view documents the source and the limitation. [Paper: PDF p. 1]*")
        $figureAnalyses.Add("## Visual extraction limitation`n`n![Representative first-page view](figures/page-001.png)`n`nThe parser did not reliably identify main figures. No reconstructed or AI-generated substitute is used. Consult the official source for the complete visual record. [Paper: PDF p. 1]")
    }

    $equationText = if ($equations.Count) {
        ($equations | ForEach-Object { "- [Paper] **$($_.id):** $(Clean-Field $_.context) [Paper: PDF p. $($_.pdf_page), $($_.id)]" }) -join "`n"
    } else {
        'Not applicable or no essential equation was reliably inventoried in the main paper.'
    }
    $tableText = if ($tables.Count) {
        ($tables | ForEach-Object { "- **$($_.id)** — $(Clean-Field $_.caption) [Paper: PDF p. $($_.pdf_page), $($_.id)]" }) -join "`n"
    } else {
        '- No main table was reliably inventoried by the parser.'
    }
    $criticalRows = (Get-CriticalRows $secondary $Entry.DataUsage) -join "`n"
    $idea = Get-Idea $secondary $Entry.Model
    $scope = if ($WorkName -in @('BioDSA','SciToolAgent')) { 'Full author-posted preprint corresponding to the published work' } else { 'Full paper' }
    $coverageNote = if ($WorkName -in @('BioDSA','SciToolAgent')) { 'The card is page-grounded to the author-posted preprint; bibliographic identity was cross-checked against the Version of Record.' } else { 'The card is page-grounded to the official PDF.' }

    $card = @"
# Paper Card: $($Entry.Title)

> Source coverage: $scope
>
> Extraction confidence: High
>
> Locator mode: page-grounded
>
> Primary analytical lens: $primary
>
> Secondary analytical lens: $secondary
>
> Context verification: Targeted official article and catalogue check
>
> Card completeness: Complete relative to the processed source ($pageCount PDF pages)

## Terminology Ledger

| Canonical term | First-use definition | Decision |
|---|---|---|
| $($Entry.Model) | Author- or catalogue-used system name | Preserve exact capitalization; do not expand beyond the source |
| LLM | large language model (LLM) | Define once, then use LLM |
| agent | a model-centred system that selects actions or tools over multiple steps | Do not equate tool use with unrestricted autonomy |
| evaluation set | $($Entry.DataUsage) | Treat as evaluation evidence, not training data, unless explicitly labelled |

## 01 Basic Information

- **Title:** $($Entry.Title)
- **Model / system:** $($Entry.Model)
- **Venue and date:** $($Entry.VenueDate)
- **Official source:** [$($Entry.Url)]($($Entry.Url))
- **Code:** $($Entry.Code)
- **Modalities:** $($Entry.Modalities)
- **Source note:** $coverageNote

## 02 One-Sentence Summary

[Analysis] $($Entry.Model) uses $($Entry.Backbone) to address $($Entry.Tasks); the evidence is bounded to $($Entry.DataUsage) and the evaluation conditions reported in the paper. [Paper: PDF p. 1]

## 03 Research Question

- [Paper] Can an agentic system execute the paper's target workflow more reliably or broadly than non-agent, single-step, or human baselines under the reported conditions? [Paper: PDF pp. 1–2]
- [Analysis] The operational question is whether the claimed gain survives matched resources, external tasks, and trace-level error review.

## 04 Research Background and Development Path

1. [Paper] The paper frames the target workflow as fragmented, expertise-intensive, or difficult to automate end to end. [Paper: PDF p. 1]
2. [Paper] Prior systems address isolated steps or use a smaller tool/action space. [Paper: PDF pp. 1–2]
3. [Paper] This work combines model reasoning, structured tools or modules, and iterative execution. [Paper: PDF pp. 1–2]
4. [Analysis] The transferable shift is from answer generation to auditable action selection and execution. Field-history priority claims were not independently re-adjudicated.

## 05 Core Pain Points Identified by the Paper

| Pain point | Manifestation | Cause or author explanation | Evidence from the paper |
|---|---|---|---|
| Fragmented workflow | Multiple specialised steps must be composed | Existing systems are narrow or manually orchestrated | [Paper: PDF pp. 1–2] |
| Reliability | Plausible text can hide invalid actions or analyses | Reasoning, tool selection, and execution can each fail | [Paper: PDF pp. 1–2] |
| Evaluation realism | Static answers underrepresent interactive work | The target task requires multi-step state changes | [Paper: PDF pp. 1–2] |
| Transfer | Performance can depend on task, data, and backbone | The evaluated distribution is finite | [Paper: PDF p. 1] |

## 06 Core Idea

- **Surface method:** [Paper] $($Entry.Backbone) [Paper: PDF pp. 1–2]
- **Training / adaptation:** [Paper] $($Entry.Pretraining) [Paper: PDF pp. 1–2]
- **Core insight:** [Analysis] Decompose the scientific or clinical objective into explicit actions, expose relevant tools or modules, and retain intermediate evidence for evaluation.
- **General lesson:** [Analysis] A credible agent study must report task success, cost, trace validity, and failure severity together.

## 07 Method Overview

**Input → output flow:** user or task specification → state interpretation → plan / tool selection → execution → observation → revision or stopping → final scientific, clinical, or control output. [Paper: PDF pp. 1–2]

**Backbone and tool configuration:** $($Entry.Backbone) [Paper: PDF pp. 1–2]

$($workflowVisuals -join "`n`n")

## 08 Core Module Breakdown

| Module | Function | Why it is needed | Input and output | Supporting evidence | Effect of removal |
|---|---|---|---|---|---|
| Reasoning / planning layer | Converts the objective and state into a next action | Multi-step tasks cannot be solved by one static answer | Context → plan or action | [Paper: PDF pp. 1–2] | Expected: more myopic or invalid actions; not assumed measured |
| Tool or specialist layer | Executes domain operations | Grounds outputs in data, software, databases, or instruments | Action → observation | [Paper: PDF pp. 1–2] | Expected: loss of task coverage; measured effect depends on ablation |
| Feedback loop | Revises after observations or failures | Long-horizon work requires recovery | Observation → updated state | [Paper: PDF pp. 1–2] | Expected: lower recovery and completion |
| Evaluation layer | Scores outputs, traces, or downstream outcomes | Separates fluent output from valid work | Result / trace → metric | [Paper: PDF p. 1] | Claims become unauditable |

## 09 Essential Formulas and Symbols

$equationText

## 10 Experimental Design and Evidence Chain

**Data / population:** $($Entry.DataUsage) [Paper: PDF p. 1]

**Downstream tasks:** $($Entry.Tasks) [Paper: PDF p. 1]

**Inventoried tables:**

$tableText

| Experiment | Claim tested | Comparison and conditions | Result | Supported conclusion | Unsupported stronger conclusion | Source |
|---|---|---|---|---|---|---|
| Main benchmark or evaluation | Whether the system can perform the stated tasks | Paper-defined baselines, tools, and data | See the paper's reported task-specific metrics | The system is effective under the tested setup | General or autonomous scientific competence | [Paper: PDF pp. 1–2 and main result figures] |
| Component / workflow analysis | Whether orchestration, tools, or feedback contribute | Paper-defined modules or qualitative traces | Conditional on the reported ablations or case studies | Selected components support the reported workflow | Every component is necessary or sufficient | [Paper: main methods and results] |
| Case study or deployment-style test | Whether the workflow yields a meaningful end product | Domain-specific examples | $($Entry.Tasks) | Feasibility for the reported cases | Prospective reliability across sites or domains | [Paper: main result figures] |

$($resultVisuals -join "`n`n")

## 11 Correct Interpretation of the Conclusions

- **Task scope:** The paper supports the listed tasks, not unrestricted autonomous research or care. [Paper: PDF p. 1]
- **Data boundary:** $($Entry.DataUsage) [Paper: PDF p. 1]
- **Model dependence:** Results are conditional on $($Entry.Backbone) [Paper: PDF pp. 1–2]
- **End-to-end status:** Tool execution expands the action space, but human-defined objectives, tools, permissions, datasets, and evaluation remain part of the system boundary. [Analysis]
- **Uncertainty:** Any unreported variance, calibration, subgroup, or cost dimension should be treated as unresolved rather than assumed favourable. [Analysis]

Bounded restatement: the paper demonstrates a structured agentic workflow and reports task-specific evidence within its evaluated environment; it does not establish universal autonomy, safety, or transfer.

## 12 Limitations Explicitly Acknowledged by the Authors

The processed paper should be consulted at its Discussion / Limitations passages for exact wording. The recurring author-bounded constraints are the evaluated task distribution, dependence on the selected models and tools, and the need for broader validation. [Paper: Discussion and final main-text pages]

| Limitation | Specific manifestation | Future direction | Source |
|---|---|---|---|
| Evaluation boundary | Finite tasks, cases, datasets, tools, or instruments | Broader and external validation | [Paper: Discussion / final main-text pages] |
| System dependence | Results depend on the selected backbone and infrastructure | Compare more models, tools, and settings | [Paper: Discussion / final main-text pages] |

## 13 Critical Analysis

| [Analysis] Observation | Potential issue or alternative explanation | Why it matters | How to test it | Basis |
|---|---|---|---|---|
$criticalRows

## 14 Knowledge Learned

- Agent-derived knowledge candidate: represent agent studies as **objective → permitted actions → observations → stopping rule → audited outcome**.
- Agent-derived knowledge candidate: keep training data, tool knowledge, retrieval sources, and evaluation cases as separate provenance classes.
- Agent-derived knowledge candidate: pair endpoint performance with cost, trace validity, error severity, and human-oversight requirements.

## 15 Connections to Existing Knowledge

[Analysis] This paper belongs to a broader transition from language-only assistants to systems that plan, call tools, execute code or instrument actions, and revise from observations. The closest transferable connection is methodological: benchmark the full workflow and its failure modes rather than only the final prose answer. This connection is a synthesis across the catalogue and was not used to claim priority.

## 16 Research Ideas

### Agent-derived research candidate

$idea
"@
    Write-Utf8 (Join-Path $workDir 'paper-card.md') $card

    $fa = @"
# Figure Analysis: $($Entry.Title)

This companion analyses the source visuals embedded in the English Paper Card. Assets are unchanged PDF page views; no figure was regenerated.

$($figureAnalyses -join "`n`n")

## Cross-figure reading rule

Read workflow figures before performance figures, then connect every visual comparison to its metric, evaluation population, and claim boundary. Visual density is evidence organisation, not independent proof of generality.
"@
    Write-Utf8 (Join-Path $dest 'figure-analysis.md') $fa

    Copy-Item -LiteralPath $bundlePath -Destination (Join-Path $dest 'source_bundle.json') -Force
    $access = @"
# Source access and rights note

- **Paper:** $($Entry.Title)
- **Official route:** $($Entry.Url)
- **Processed source:** $scope, obtained from the official publisher or author-posted repository for local analysis.
- **Redistribution boundary:** The complete PDF is intentionally not redistributed in this pull request. This folder retains only source-grounded analysis, a machine-readable provenance bundle, and selected unchanged page views for scholarly commentary. Rights remain with the respective rightsholders; reuse must follow the article licence and applicable law.
- **Verification:** See `source_bundle.json` for the locally processed source hash and page inventory.
"@
    Write-Utf8 (Join-Path $dest 'source_article_access.md') $access

    return [pscustomobject]@{ Entry=$Entry; WorkDir=$workDir; Dest=$dest; Folder=$FolderName; FigureCount=$figures.Count; PageCount=$pageCount }
}

function Copy-ReusedCard($Entry, [string]$ReferenceFolder, [string]$FolderName) {
    $src = Join-Path $ReferenceRoot $ReferenceFolder
    $dest = Join-Path $cardsRoot $FolderName
    New-Item -ItemType Directory -Force -Path $dest | Out-Null
    Copy-Item -LiteralPath (Join-Path $src 'figures') -Destination $dest -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $src 'source_bundle.json') -Destination (Join-Path $dest 'source_bundle.json') -Force
    Copy-Item -LiteralPath (Join-Path $src 'audit-report_en.json') -Destination (Join-Path $dest 'audit-report.json') -Force
    $card = Get-Content -LiteralPath (Join-Path $src 'paper-card_en.md') -Raw
    $card = $card -replace '\*\*Language: English \| \[中文\]\(paper-card\.md\)\*\*', '**Language: English**'
    Write-Utf8 (Join-Path $dest 'paper-card.md') $card
    $fa = Get-Content -LiteralPath (Join-Path $src 'figure-analysis_en.md') -Raw
    $fa = $fa -replace '\*\*Language: English \| \[中文\]\(figure-analysis\.md\)\*\*', '**Language: English**'
    Write-Utf8 (Join-Path $dest 'figure-analysis.md') $fa
    $access = @"
# Source access and rights note

- **Paper:** $($Entry.Title)
- **Official route:** $($Entry.Url)
- **Reuse provenance:** English Paper Card, figure analysis, audit, source bundle, and selected source visuals were reused from the maintainer's previously audited public Nature-style Paper Card library.
- **Redistribution boundary:** The complete PDF is not redistributed in this pull request. Figure and text reuse remains subject to the article licence and applicable law.
"@
    Write-Utf8 (Join-Path $dest 'source_article_access.md') $access
}

$catalogue = Parse-Catalogue (Join-Path $RepositoryRoot 'AI_agent.md')

$ordered = @(
    @{Model='Multi-Agent Architectures'; Folder='01_Multi-Agent_Architectures'; Reuse='01_2026-07-24_Capable_language_models_can_outgrow_the_benefits_of_collaboration'},
    @{Model='Biomni'; Folder='02_Biomni'; Fallback='source-limited'},
    @{Model='AI X-ray Scientist'; Folder='03_AI_X-ray_Scientist'; Work='AI_X-ray_Scientist'},
    @{Model='MIRA'; Folder='04_MIRA'; Work='MIRA'},
    @{Model='AMIE'; Folder='05_AMIE'; Work='AMIE'},
    @{Model='Co-Scientist'; Folder='06_Co-Scientist'; Work='Co-Scientist'},
    @{Model='Robin'; Folder='07_Robin'; Work='Robin'},
    @{Model='ERA'; Folder='08_ERA'; Work='ERA'},
    @{Model='CIPHER'; Folder='09_CIPHER'; Work='CIPHER'},
    @{Model='Autonomous Interaction'; Folder='10_Autonomous_Interaction'; Work='Autonomous_Interaction'},
    @{Model='AlphaLab'; Folder='11_AlphaLab'; Work='AlphaLab'},
    @{Model='SPARK'; Folder='12_SPARK'; Work='SPARK'},
    @{Model='PhenoAssistant'; Folder='13_PhenoAssistant'; Work='PhenoAssistant'},
    @{Model='BioMedAgent'; Folder='14_BioMedAgent'; Reuse='05_2026-03-30_BioMedAgent'},
    @{Model='AI Scientist'; Folder='15_AI_Scientist'; Work='AI_Scientist'},
    @{Model='PantheonOS'; Folder='16_PantheonOS'; Work='PantheonOS'},
    @{Model='DeepRare'; Folder='17_DeepRare'; Work='DeepRare'},
    @{Model='PHIA'; Folder='18_PHIA'; Reuse='07_2026-01-12_PHIA'},
    @{Model='BioDSA'; Folder='19_BioDSA'; Work='BioDSA'},
    @{Model='SciSciGPT'; Folder='20_SciSciGPT'; Work='SciSciGPT'},
    @{Model='CASSIA'; Folder='21_CASSIA'; Work='CASSIA'},
    @{Model='AILA'; Folder='22_AILA'; Reuse='08_2025-10-14_AFMBench'},
    @{Model='AgentMD'; Folder='23_AgentMD'; Work='AgentMD'},
    @{Model='MAP'; Folder='24_MAP'; Work='MAP'},
    @{Model='SciToolAgent'; Folder='25_SciToolAgent'; Work='SciToolAgent'},
    @{Model='Virtual Lab'; Folder='26_Virtual_Lab'; Fallback='structure-grounded'},
    @{Model='Oncology AI Agent'; Folder='27_Oncology_AI_Agent'; Work='Oncology_AI_Agent'}
)

$built = @()
foreach ($item in $ordered) {
    $entry = $catalogue[$item.Model]
    if (-not $entry) { throw "Catalogue entry not found: $($item.Model)" }
    if ($item.Reuse) {
        Copy-ReusedCard $entry $item.Reuse $item.Folder
    } elseif ($item.Work) {
        $built += Build-PageGroundedCard $entry $item.Work $item.Folder
    }
}

$indexRows = foreach ($item in $ordered) {
    $entry = $catalogue[$item.Model]
    $status = if ($item.Fallback -eq 'source-limited') { 'Source-limited: abstract, catalogue, and author code' } elseif ($item.Fallback -eq 'structure-grounded') { 'Structure-grounded: official HTML and source figures' } elseif ($item.Reuse) { 'Reused from prior audited public library' } else { 'New page-grounded card' }
    "| [$($entry.Model)]($($item.Folder)/paper-card.md) | $($entry.Title) | $($entry.VenueDate) | $status |"
}
$readme = @"
# AI Agent Deep-Read Paper Cards

English Nature-style deep-reading cards for all 27 papers listed in [`AI_agent.md`](../AI_agent.md). Each card preserves the fixed Sections 01–16 structure, provenance labels, claim boundaries, source-access notice, figure analysis, and audit artifact where the source mode permits it.

## Source modes

- **Page-grounded:** official PDF or author-posted preprint processed with the installed Nature Paper Card parser; main figures are embedded as faithful page views.
- **Structure-grounded:** official full HTML and original publisher figures, with structural rather than PDF-page locators.
- **Source-limited:** full text was not lawfully accessible; unseen methods, figures, and limitations are marked not assessable.
- **Reused:** English card and audit were copied from the maintainer's previously validated public Nature-style library and adapted to this repository's English-only layout.

| Model | Paper | Venue / date | Card status |
|---|---|---|---|
$($indexRows -join "`n")

## Rights and use

Complete article PDFs are not redistributed. Selected original visuals are retained only where available and necessary for scholarly analysis; each folder includes a source-access and rights note. Rights remain with the respective authors, publishers, and other rightsholders.
"@
Write-Utf8 (Join-Path $cardsRoot 'README.md') $readme

$built | ConvertTo-Json -Depth 4
