param(
    [Parameter(Mandatory = $true)]
    [string]$PackageName
)

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Package Test Runner" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$packagePath = Join-Path $root $PackageName

if (!(Test-Path $packagePath)) {

    Write-Host "Package not found: $PackageName" -ForegroundColor Red
    exit 1
}

$oldLocation = Get-Location
$oldPreference = $ErrorActionPreference

$ErrorActionPreference = "Stop"

try {

    Set-Location $packagePath

    Write-Host "Running Pytest..." -ForegroundColor Cyan
    Write-Host ""

    pytest -v

    if ($LASTEXITCODE -ne 0) {
        throw "Pytest failed."
    }

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host " All Tests Passed" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host " Test Execution Failed" -ForegroundColor Red
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host ""

    Write-Host $_.Exception.Message -ForegroundColor Red

    exit 1
}
finally {

    Set-Location $oldLocation
    $ErrorActionPreference = $oldPreference
}