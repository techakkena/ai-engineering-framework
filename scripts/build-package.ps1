param(
    [Parameter(Mandatory = $true)]
    [string]$Package
)

$packagePath = Join-Path $PSScriptRoot "..\$Package"

if (!(Test-Path $packagePath)) {
    Write-Host "Package '$Package' not found." -ForegroundColor Red
    exit 1
}

Push-Location $packagePath

Write-Host "Building $Package..." -ForegroundColor Cyan

python -m build

Pop-Location