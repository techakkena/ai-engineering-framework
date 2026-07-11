param(
    [Parameter(Mandatory = $true)]
    [string]$PackageName,

    [string]$Description = "Reusable AI Engineering Framework Package"
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

# -----------------------------------------------------
# Create Package Structure
# -----------------------------------------------------

& "$PSScriptRoot\create-package.ps1" $PackageName

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "Applying package templates..." -ForegroundColor Cyan
Write-Host ""

if (!(Test-Path $packagePath)) {
    
    Write-Host "Failed to create package." -ForegroundColor Red
    exit 1
}

$moduleName = $PackageName.Replace("-", "_")

$requirements = Join-Path $packagePath "requirements.txt"

$testPath = Join-Path $packagePath "tests\test_package.py"

$examplePath = Join-Path $packagePath "examples\basic\main.py"

$initPath = Join-Path $packagePath "src\$moduleName\__init__.py"

$createdFiles = @()
$skippedFiles = @()

# -----------------------------------------------------
# Copy Template Files
# -----------------------------------------------------

if (!(Test-Path $templatePath)) {
    Write-Host "Templates folder not found." -ForegroundColor Red
    exit 1
}

$templateFiles = Get-ChildItem `
    -Path $templatePath `
    -File |
    Sort-Object Name |
    Select-Object -ExpandProperty Name

foreach ($file in $templateFiles) {

    $source = Join-Path $templatePath $file
    $destination = Join-Path $packagePath $file

    if (!(Test-Path $destination)) {

        if (!(Test-Path $source)) {
            Write-Host "Template missing: $source" -ForegroundColor Red
            continue
        }

        try {

            Copy-Item `
                -Path $source `
                -Destination $destination `
                -ErrorAction Stop

            $createdFiles += $file
            Write-Host "Created : $file" -ForegroundColor Green
        }
        catch {

            Write-Host "Failed  : $file" -ForegroundColor Red
            Write-Host $_.Exception.Message
            continue
        }
    }
    else {

        $skippedFiles += $file
        Write-Host "Skipped : $file" -ForegroundColor Yellow
    }
}
# -----------------------------------------------------
# Replace Template Variables
# -----------------------------------------------------

$replaceFiles = @(
    "README.md",
    "pyproject.toml"
)

foreach ($file in $replaceFiles) {

    if (!($createdFiles -contains $file)) {
        continue
    }

    $path = Join-Path $packagePath $file

    $content = Get-Content `
        -Path $path `
        -Raw `
        -Encoding UTF8

    $content = $content.Replace("__PACKAGE_NAME__", $PackageName)
    $content = $content.Replace("__MODULE_NAME__", $moduleName)
    $content = $content.Replace("__PACKAGE_DESCRIPTION__", $Description)

    Set-Content `
    -Path $path `
    -Value $content `
    -Encoding UTF8
}

# -----------------------------------------------------
# requirements.txt
# -----------------------------------------------------

if (!(Test-Path $requirements)) {

    Set-Content `
        -Path $requirements `
        -Value "" `
        -Encoding UTF8

    Write-Host "Created : requirements.txt" -ForegroundColor Green
    $createdFiles += "requirements.txt"
}
else {
    $skippedFiles += "requirements.txt"
}
# -----------------------------------------------------
# Sample Test
# -----------------------------------------------------

if (!(Test-Path $testPath)) {

    Set-Content `
        -Path $testPath `
        -Value @"
def test_import():
    assert True
"@ `
        -Encoding UTF8

    Write-Host "Created : tests/test_package.py" -ForegroundColor Green
    $createdFiles += "tests/test_package.py"
}
else {
    $skippedFiles += "tests/test_package.py"
}
# -----------------------------------------------------
# Example Program
# -----------------------------------------------------

if (!(Test-Path $examplePath)) {

    $exampleContent = @"
def main():
    print("Hello from $PackageName")

if __name__ == "__main__":
    main()
"@

    Set-Content `
        -Path $examplePath `
        -Value $exampleContent `
        -Encoding UTF8

    Write-Host "Created : examples/basic/main.py" -ForegroundColor Green
    $createdFiles += "examples/basic/main.py"
}
else {
    $skippedFiles += "examples/basic/main.py"
}
# -----------------------------------------------------
# Package __init__.py
# -----------------------------------------------------

if (!(Test-Path $initPath)) {

    Set-Content `
        -Path $initPath `
        -Value @"
\"\"\"
$PackageName

Author: TECHAKKENA
\"\"\"

__version__ = "0.1.0"
"@ `
        -Encoding UTF8

    Write-Host "Created : src/$moduleName/__init__.py" -ForegroundColor Green
    $createdFiles += "src/$moduleName/__init__.py"
}
else {
    $skippedFiles += "src/$moduleName/__init__.py"
}
# -----------------------------------------------------
# Finish
# -----------------------------------------------------
Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Package '$PackageName' is ready." -ForegroundColor Green
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

Write-Host ""
Write-Host "Created Files" -ForegroundColor Green

foreach ($item in ($createdFiles | Sort-Object)) {
    Write-Host "  + $item"
}

Write-Host ""

Write-Host "Skipped Files" -ForegroundColor Yellow

foreach ($item in ($skippedFiles | Sort-Object)) {
    Write-Host "  - $item"
}

Write-Host ""
Write-Host "Package scaffold completed successfully." -ForegroundColor Green
Write-Host ""

