param(
    [Parameter(Mandatory = $true)]
    [string]$CardsRoot
)

$ErrorActionPreference = 'Stop'
$errors = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]
$folders = @(Get-ChildItem -LiteralPath $CardsRoot -Directory | Where-Object { $_.Name -match '^\d{2}_' } | Sort-Object Name)

if ($folders.Count -ne 27) { $errors.Add("Expected 27 paper folders; found $($folders.Count).") }

foreach ($folder in $folders) {
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
            if ($folder.Name -in @('02_Biomni','26_Virtual_Lab') -and [int]$audit.summary.warnings -eq 1) {
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
