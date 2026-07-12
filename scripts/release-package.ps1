param(
    [Parameter(Mandatory = $true)]
    [string]$PackageName,

    [Parameter(Mandatory = $true)]
    [string]$Version,

    [string]$Message = "Release $Version"
)

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Package Release" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

$verifyScript = Join-Path $PSScriptRoot "verify-package.ps1"
$buildScript = Join-Path $PSScriptRoot "build-package.ps1"

$oldLocation = Get-Location
$oldPreference = $ErrorActionPreference

$ErrorActionPreference = "Stop"

try {

    Set-Location $root

    # -------------------------------------------------
    # Verify
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 1 : Verify Package" -ForegroundColor Cyan

    & $verifyScript $PackageName

    if ($LASTEXITCODE -ne 0) {
        throw "Package verification failed."
    }

    # -------------------------------------------------
    # Build
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 2 : Build Package" -ForegroundColor Cyan

    & $buildScript $PackageName

    if ($LASTEXITCODE -ne 0) {
        throw "Package build failed."
    }

    # -------------------------------------------------
    # Git Status
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 3 : Git Status" -ForegroundColor Cyan

    git status

    # -------------------------------------------------
    # Git Add
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 4 : Git Add" -ForegroundColor Cyan

    git add .

    # -------------------------------------------------
    # Commit
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 5 : Commit" -ForegroundColor Cyan

    git commit -m $Message

    # -------------------------------------------------
    # Tag
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 6 : Create Tag" -ForegroundColor Cyan

    git tag $Version

    # -------------------------------------------------
    # Push
    # -------------------------------------------------

    Write-Host ""
    Write-Host "Step 7 : Push Branch" -ForegroundColor Cyan

    git push

    Write-Host ""
    Write-Host "Step 8 : Push Tag" -ForegroundColor Cyan

    git push origin $Version

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host " Package Released Successfully" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host " Package Release Failed" -ForegroundColor Red
    Write-Host "=========================================" -ForegroundColor Red
    Write-Host ""

    Write-Host $_.Exception.Message -ForegroundColor Red

    exit 1
}
finally {

    Set-Location $oldLocation
    $ErrorActionPreference = $oldPreference
}