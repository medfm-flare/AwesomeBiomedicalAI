param(
    [Parameter(Mandatory = $true)]
    [string]$RepositoryRoot,
    [Parameter(Mandatory = $true)]
    [string]$WorkRoot
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Write-Utf8([string]$Path, [string]$Content) {
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

$mapping = [ordered]@{
    '03_AI_X-ray_Scientist'='AI_X-ray_Scientist'
    '04_MIRA'='MIRA'
    '05_AMIE'='AMIE'
    '06_Co-Scientist'='Co-Scientist'
    '07_Robin'='Robin'
    '08_ERA'='ERA'
    '09_CIPHER'='CIPHER'
    '10_Autonomous_Interaction'='Autonomous_Interaction'
    '11_AlphaLab'='AlphaLab'
    '12_SPARK'='SPARK'
    '13_PhenoAssistant'='PhenoAssistant'
    '15_AI_Scientist'='AI_Scientist'
    '16_PantheonOS'='PantheonOS'
    '17_DeepRare'='DeepRare'
    '19_BioDSA'='BioDSA'
    '20_SciSciGPT'='SciSciGPT'
    '21_CASSIA'='CASSIA'
    '23_AgentMD'='AgentMD'
    '24_MAP'='MAP'
    '25_SciToolAgent'='SciToolAgent'
    '27_Oncology_AI_Agent'='Oncology_AI_Agent'
}

foreach ($folder in $mapping.Keys) {
    $workDir = Join-Path $WorkRoot $mapping[$folder]
    $dest = Join-Path (Join-Path $RepositoryRoot 'paper_cards') $folder
    $card = Get-Content -LiteralPath (Join-Path $workDir 'paper-card.md') -Raw
    foreach ($fig in Get-ChildItem -LiteralPath (Join-Path $dest 'figures') -File) {
        $card = $card.Replace($fig.FullName, "figures/$($fig.Name)")
    }
    Write-Utf8 (Join-Path $dest 'paper-card.md') $card
    Copy-Item -LiteralPath (Join-Path $workDir 'audit-report.json') -Destination (Join-Path $dest 'audit-report.json') -Force

    $bundlePath = Join-Path $dest 'source_bundle.json'
    $bundle = Get-Content -LiteralPath $bundlePath -Raw | ConvertFrom-Json
    foreach ($table in @($bundle.evidence_inventory.tables)) {
        if ($table.pdf_page) {
            $tableName = 'page-{0:d3}.png' -f [int]$table.pdf_page
            $tableSource = Join-Path $workDir "visual-assets\pages\$tableName"
            $tableDest = Join-Path (Join-Path $dest 'figures') $tableName
            if ((Test-Path -LiteralPath $tableSource) -and -not (Test-Path -LiteralPath $tableDest)) {
                Copy-Item -LiteralPath $tableSource -Destination $tableDest -Force
            }
        }
    }
    $bundle.source_path = 'source_article.pdf (local processing only; see source_article_access.md)'
    $bundle.rendered_pages_dir = 'figures'
    foreach ($page in @($bundle.pages)) {
        if ($page.rendered_image) {
            $pageName = 'page-{0:d3}.png' -f [int]$page.pdf_page
            if (Test-Path -LiteralPath (Join-Path (Join-Path $dest 'figures') $pageName)) {
                $page.rendered_image = "figures/$pageName"
            } else {
                $page.rendered_image = $null
            }
        }
    }
    foreach ($figure in @($bundle.evidence_inventory.figures)) {
        if ($figure.page_image) { $figure.page_image = 'figures/page-{0:d3}.png' -f [int]$figure.pdf_page }
    }
    foreach ($table in @($bundle.evidence_inventory.tables)) {
        if ($table.page_image) { $table.page_image = 'figures/page-{0:d3}.png' -f [int]$table.pdf_page }
    }
    Write-Utf8 $bundlePath ($bundle | ConvertTo-Json -Depth 20)
}

"Finalized $($mapping.Count) page-grounded publication cards."
