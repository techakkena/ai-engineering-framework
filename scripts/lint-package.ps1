param(
    [Parameter(Mandatory = $true)]
    [string]$PackageName
)

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Package Linter" -ForegroundColor Cyan
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

    $steps = @(
        @{
            Name = "Ruff Check"
            Command = { ruff check --fix . }
        },
        @{
            Name = "Ruff Format"
            Command = { ruff format . }
        },
        @{
            Name = "Black"
            Command = { black . }
        }
    )

    foreach ($step in $steps) {

        Write-Host ""
        Write-Host "-----------------------------------------" -ForegroundColor DarkCyan
        Write-Host $step.Name -ForegroundColor Cyan
        Write-Host "-----------------------------------------" -ForegroundColor DarkCyan

        & $step.Command

        if ($LASTEXITCODE -ne 0) {
            throw "$($step.Name) failed."
        }

        Write-Host "[PASS] $($step.Name)" -ForegroundColor Green
    }

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host " Package Lint Successful" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host " Package Lint Failed" -ForegroundColor Red
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host ""

    Write-Host $_.Exception.Message -ForegroundColor Red

    exit 1
}
finally {

    Set-Location $oldLocation
    $ErrorActionPreference = $oldPreference
}