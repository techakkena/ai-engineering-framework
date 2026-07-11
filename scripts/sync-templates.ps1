param()

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$templatePath = Join-Path $PSScriptRoot "templates"

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Template Synchronizer" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

if (!(Test-Path $templatePath)) {
    Write-Host "Templates folder not found." -ForegroundColor Red
    exit 1
}

$templateFiles = Get-ChildItem `
    -Path $templatePath `
    -File

$packages = Get-ChildItem `
    -Path $root `
    -Directory `
    -Filter "ai-*"

if ($packages.Count -eq 0) {
    Write-Host "No packages found." -ForegroundColor Yellow
    exit 0
}

$updatedPackages = 0
$totalFiles = 0

foreach ($package in $packages) {

    Write-Host ""
    Write-Host "Updating $($package.Name)..." -ForegroundColor Cyan

    foreach ($template in $templateFiles) {

        try {

            Copy-Item `
                -Path $template.FullName `
                -Destination (Join-Path $package.FullName $template.Name) `
                -Force `
                -ErrorAction Stop

            Write-Host "  Updated : $($template.Name)" -ForegroundColor Green
            $totalFiles++

        }
        catch {

            Write-Host "  Failed  : $($template.Name)" -ForegroundColor Red
            Write-Host "            $($_.Exception.Message)"
        }
    }

    $updatedPackages++
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Synchronization Complete" -ForegroundColor Green
Write-Host "===================================" -ForegroundColor Cyan

Write-Host ""
Write-Host "Packages Updated : $updatedPackages"
Write-Host "Files Copied     : $totalFiles"
Write-Host ""
Write-Host "Done." -ForegroundColor Green