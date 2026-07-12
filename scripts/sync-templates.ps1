param(
    [switch]$All
)

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$templatePath = Join-Path $PSScriptRoot "templates"

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Template Synchronizer" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = "Stop"

try {

    # -------------------------------------------------
    # Validate Templates
    # -------------------------------------------------

    if (!(Test-Path $templatePath)) {
        throw "Templates folder not found: $templatePath"
    }

    # -------------------------------------------------
    # Files to Synchronize
    # -------------------------------------------------

    if ($All) {

        $templateFiles = Get-ChildItem `
            -Path $templatePath `
            -File

        Write-Host "Mode : Full Template Synchronization" -ForegroundColor Yellow
    }
    else {

        $templateFiles = @(
            ".gitignore",
            "pyproject.toml",
            "pytest.ini",
            "MANIFEST.in",
            "LICENSE"
        ) | ForEach-Object {

            Get-Item (Join-Path $templatePath $_)
        }

        Write-Host "Mode : Infrastructure Files Only" -ForegroundColor Green
    }

    # -------------------------------------------------
    # Packages
    # -------------------------------------------------

    $packages = Get-ChildItem `
        -Path $root `
        -Directory `
        -Filter "ai-*"

    if ($packages.Count -eq 0) {
        Write-Host ""
        Write-Host "No packages found." -ForegroundColor Yellow
        exit 0
    }

    $updatedPackages = 0
    $copiedFiles = 0
    $failedFiles = 0

    # -------------------------------------------------
    # Synchronize
    # -------------------------------------------------

    foreach ($package in $packages) {

        Write-Host ""
        Write-Host "Package : $($package.Name)" -ForegroundColor Cyan

        foreach ($template in $templateFiles) {

            try {

                Copy-Item `
                    -Path $template.FullName `
                    -Destination (Join-Path $package.FullName $template.Name) `
                    -Force

                Write-Host "  Copied  : $($template.Name)" -ForegroundColor Green
                $copiedFiles++
            }
            catch {

                Write-Host "  Failed  : $($template.Name)" -ForegroundColor Red
                Write-Host "            $($_.Exception.Message)"

                $failedFiles++
            }
        }

        $updatedPackages++
    }

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host " Template Synchronization Complete" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Packages Updated : $updatedPackages"
    Write-Host "Files Copied     : $copiedFiles"
    Write-Host "Files Failed     : $failedFiles"

    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "Template synchronization failed." -ForegroundColor Red
    Write-Host $_.Exception.Message

    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}