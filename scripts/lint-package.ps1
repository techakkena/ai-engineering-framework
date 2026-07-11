param(
    [Parameter(Mandatory = $true)]
    [string]$Package
)

$packagePath = Join-Path $PSScriptRoot "..\$Package"

Push-Location $packagePath

ruff check .
ruff format --check .
black --check .
mypy .

Pop-Location