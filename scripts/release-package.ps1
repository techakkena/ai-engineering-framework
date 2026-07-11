param(
    [Parameter(Mandatory = $true)]
    [string]$Package,

    [Parameter(Mandatory = $true)]
    [string]$Version
)

& "$PSScriptRoot\lint-package.ps1" $Package

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

& "$PSScriptRoot\test-package.ps1" $Package

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

& "$PSScriptRoot\build-package.ps1" $Package

Push-Location (Join-Path $PSScriptRoot "..")

git tag "$Version-$Package"
git push origin "$Version-$Package"

Pop-Location