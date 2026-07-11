param(
    [Parameter(Mandatory = $true)]
    [string]$Package
)

$packagePath = Join-Path $PSScriptRoot "..\$Package"

Push-Location $packagePath

ruff check . --fix
ruff format .
black .

Pop-Location