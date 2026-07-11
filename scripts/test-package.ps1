param(
    [Parameter(Mandatory = $true)]
    [string]$Package
)

$packagePath = Join-Path $PSScriptRoot "..\$Package"

Push-Location $packagePath

pytest

Pop-Location