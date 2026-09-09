param(
    [Parameter(Mandatory = $true)]
    [string]$CardsRoot
)

$ErrorActionPreference = 'Stop'
$errors = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]
$folders = @(Get-ChildItem -LiteralPath $CardsRoot -Directory | Where-Object { $_.Name -match '^\d{2}_' } | Sort-Object Name)

$cataloguePath = Join-Path (Split-Path -Parent (Resolve-Path -LiteralPath $CardsRoot).Path) 'AI_agent.md'
$catalogue = Get-Content -LiteralPath $cataloguePath -Raw
$mapping = Get-Content -LiteralPath (Join-Path $CardsRoot 'catalogue-map.json') -Raw | ConvertFrom-Json
$expectedFolders = @($mapping.folder)
$rows = @($catalogue -split "`n" | Where-Object { $_ -match '^\| 20\d\d-\d\d ' })
if ($rows.Count -ne 30 -or $mapping.Count -ne 30) { $errors.Add('Expected 30 catalogue rows and mapping entries') }
for ($i=0; $i -lt $mapping.Count; $i++) {
    $item = $mapping[$i]
    $name = (($rows[$i] -split '\|')[2] -split ' \[\[details\]\]')[0].Trim()
    if ($item.number -ne ($i+1) -or $item.name -cne $name -or -not $item.folder.StartsWith(('{0:D2}_' -f ($i+1)))) { $errors.Add("Order mismatch at row $($i+1)") }
}
foreach ($folder in $folders) {
    if ($folder.Name -notin $expectedFolders) { $errors.Add("Card absent from catalogue: $($folder.Name)") }
}
foreach ($expected in $expectedFolders) {
    if ($expected -notin $folders.Name) { $errors.Add("Catalogue link has no card: $expected") }
}

foreach ($folder in $folders) {
    $entry = $mapping | Where-Object { $_.folder -eq $folder.Name }
    if ($entry.status -eq 'pending') {
        if (-not (Test-Path -LiteralPath (Join-Path $folder.FullName 'README.md')) -or (Test-Path -LiteralPath (Join-Path $folder.FullName 'paper-card.md'))) { $errors.Add("Invalid pending folder: $($folder.Name)") }
        continue
    }
    foreach ($required in @('paper-card.md','figure-analysis.md','audit-report.json','source_article_access.md')) {
        if (-not (Test-Path -LiteralPath (Join-Path $folder.FullName $required))) {
            $errors.Add("$($folder.Name): missing $required")
        }
    }
    $cardPath = Join-Path $folder.FullName 'paper-card.md'
    if (Test-Path -LiteralPath $cardPath) {
        $card = Get-Content -LiteralPath $cardPath -Raw
        $sectionCount = [regex]::Matches($card, '(?m)^## (0[1-9]|1[0-6]) ').Count
        if ($sectionCount -ne 16) { $errors.Add("$($folder.Name): expected 16 numbered sections; found $sectionCount") }
        if ($card -match '[A-Za-z]:\\|file://') { $errors.Add("$($folder.Name): publication card contains a local absolute path") }
    }
    foreach ($md in Get-ChildItem -LiteralPath $folder.FullName -File -Filter '*.md') {
        $text = Get-Content -LiteralPath $md.FullName -Raw
        foreach ($match in [regex]::Matches($text, '!\[[^]]*\]\((?:<)?([^)>]+)(?:>)?\)')) {
            $target = $match.Groups[1].Value
            if ($target -notmatch '^https?://') {
                $resolved = Join-Path $md.DirectoryName ($target -replace '/', '\')
                if (-not (Test-Path -LiteralPath $resolved)) { $errors.Add("$($folder.Name): broken image link $target") }
            }
        }
    }
    $auditPath = Join-Path $folder.FullName 'audit-report.json'
    if (Test-Path -LiteralPath $auditPath) {
        $audit = Get-Content -LiteralPath $auditPath -Raw | ConvertFrom-Json
        if ([int]$audit.summary.errors -ne 0) { $errors.Add("$($folder.Name): audit has $($audit.summary.errors) error(s)") }
        if ([int]$audit.summary.warnings -ne 0) {
            if ($folder.Name -in @('05_2026-07_Biomni','29_2025-07_Virtual_Lab') -and [int]$audit.summary.warnings -eq 1) {
                $warnings.Add("$($folder.Name): expected fallback warning because no PDF source bundle was supplied")
            } else {
                $errors.Add("$($folder.Name): audit has unresolved warning(s)")
            }
        }
    }
}

$result = [ordered]@{
    status = if ($errors.Count) { 'fail' } else { 'pass' }
    paper_folders = $folders.Count
    errors = @($errors)
    reviewed_warnings = @($warnings)
}
$result | ConvertTo-Json -Depth 5
if ($errors.Count) { exit 1 }
