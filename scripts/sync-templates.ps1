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

            $templateFiles = @()

            foreach ($name in @(
                ".gitignore",
                "pyproject.toml",
                "pytest.ini",
                "MANIFEST.in",
                "LICENSE",
            )) {

                $path = Join-Path $templatePath $name

                if (Test-Path $path) {
                    $templateFiles += Get-Item $path
                }
                else {
                    Write-Host "Skipping missing template : $name" -ForegroundColor Yellow
                }
            }
    }
    # -------------------------------------------------
    # Packages
    # -------------------------------------------------

    $packages = Get-ChildItem `
        -Path $root `
        -Directory `
        -Filter "ai-*"

    if (@($packages).Count -eq 0) {
        Write-Host ""
        Write-Host "No packages found." -ForegroundColor Yellow
        return
    }

    $updatedPackages = 0
    $copiedFiles = 0
    $failedFiles = 0

    # -------------------------------------------------
    # Synchronize
    # -------------------------------------------------

    foreach ($package in $packages) {
        $moduleName = $package.Name.Replace("-", "_")

        $descriptions = @{
                "ai-core"   = "Core abstractions for the AI Engineering Framework."
                "ai-utils"  = "Common utilities for the AI Engineering Framework."
                "ai-config" = "Configuration management for the AI Engineering Framework."
                "ai-memory" = "Memory management for AI applications."
            }

            $description = $descriptions[$package.Name]

            if ([string]::IsNullOrWhiteSpace($description)) {
                $description = "Enterprise $($package.Name) package."
            }

            $replacements = @{
                "__PACKAGE_NAME__"        = $package.Name
                "__PACKAGE_MODULE__"      = $moduleName
                "__PACKAGE_DESCRIPTION__" = $description
                "__YEAR__"                = (Get-Date).Year
                "__AUTHOR__"              = "AI Engineering Framework"
            }
        Write-Host ""
        Write-Host "Package : $($package.Name)" -ForegroundColor Cyan

        foreach ($template in $templateFiles) {

        try {

            $destination = Join-Path $package.FullName $template.Name

            Copy-Item `
                -Path $template.FullName `
                -Destination $destination `
                -Force
            if ($template.Extension -in @(".toml", ".md", ".ini", ".txt") -or
                $template.Name -eq ".gitignore" -or
                $template.Name -eq "LICENSE") {

                $content = Get-Content $destination -Raw

                foreach ($key in $replacements.Keys) {
                    $content = $content.Replace($key, $replacements[$key])
                }

                $content | Set-Content `
                    -Path $destination `
                    -Encoding UTF8 `
                    -NoNewline
            }

            Write-Host "  Updated : $($template.Name)" -ForegroundColor Green

            $copiedFiles++

        }
        catch {

            Write-Host "  Failed : $($template.Name)" -ForegroundColor Red
            Write-Host "          $($_.Exception.Message)"

            $failedFiles++
        }
            }   # foreach ($template in $templateFiles)

                $updatedPackages++
            }       # foreach ($package in $packages)

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host " Template Synchronization Complete" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Packages Updated : $updatedPackages"
    Write-Host "Files Updated    : $copiedFiles"
    Write-Host "Files Failed     : $failedFiles"
    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Red
    Write-Host " Template Synchronization Failed" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
    Write-Host ""

    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""

    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}