function Write-Utf8NoBom {
    param(
        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [string]$Content
    )

    $utf8NoBom = [System.Text.UTF8Encoding]::new($false)

    [System.IO.File]::WriteAllText(
        $Path,
        $Content,
        $utf8NoBom
    )
}


param(
    [Parameter(Mandatory)]
    [string]$PackageName,

    [ValidateSet(
        "Basic",
        "Config",
        "Storage",
        "RAG",
        "Agents",
        "Workflow",
        "Service",
        "Processor"
    )]
    [string]$Type = "Basic"
)

if ($PackageName -notmatch "^[a-z][a-z0-9-]+$") {
    Write-Host ""
    Write-Host "Invalid package name." -ForegroundColor Red
    Write-Host "Example: ai-memory" -ForegroundColor Yellow
    exit 1
}

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$packagePath = Join-Path $root $PackageName
$templatePath = Join-Path $PSScriptRoot "templates"

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Package Generator" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = "Stop"

try {

    # -------------------------------------------------
    # Create Package
    # -------------------------------------------------

    & "$PSScriptRoot\create-package.ps1" $PackageName

    $moduleName = $PackageName.Replace("-", "_")

    $createdFiles = @()
    $skippedFiles = @()

    $testPath = Join-Path $packagePath "tests\test_package.py"

    # -------------------------------------------------
    # Copy Templates
    # -------------------------------------------------

    if (!(Test-Path $templatePath)) {
        throw "Templates folder not found: $templatePath"
    }

    $templateFiles = Get-ChildItem `
        -Path $templatePath `
        -File |
        Sort-Object Name

    foreach ($template in $templateFiles) {

        $destination = Join-Path $packagePath $template.Name

        if (Test-Path $destination) {

            Write-Host "Skipped : $($template.Name)" -ForegroundColor Yellow
            $skippedFiles += $template.Name
            continue
        }

        Copy-Item `
            -Path $template.FullName `
            -Destination $destination

        Write-Host "Created : $($template.Name)" -ForegroundColor Green
        $createdFiles += $template.Name
    }

    # -------------------------------------------------
    # Smoke Test
    # -------------------------------------------------

    if (!(Test-Path $testPath)) {

        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)

        [System.IO.File]::WriteAllText(
            $destination,
            $content,
            $utf8NoBom
        ) @"
def test_import():

    import $moduleName

    assert $moduleName is not None
"@

        Write-Host "Created : tests/test_package.py" -ForegroundColor Green
        $createdFiles += "tests/test_package.py"
    }
    else {

        Write-Host "Skipped : tests/test_package.py" -ForegroundColor Yellow
        $skippedFiles += "tests/test_package.py"
    }

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host " Package Ready" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Package  : $PackageName"
    Write-Host "Module   : $moduleName"
    Write-Host "Location : $packagePath"

    Write-Host ""
    Write-Host "Summary" -ForegroundColor Cyan
    Write-Host "-------"
    Write-Host "Created : $($createdFiles.Count)"
    Write-Host "Skipped : $($skippedFiles.Count)"

}
catch {

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Red
    Write-Host " Package Generation Failed" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
    Write-Host ""

    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""

    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}