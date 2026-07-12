param(
    [Parameter(Mandatory = $true)]
    [string]$PackageName
)

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$packagePath = Join-Path $root $PackageName
$moduleName = $PackageName.Replace("-", "_")

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Package Structure Creator" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$directories = @(
    "docs",
    "examples",
    "examples/basic",
    "examples/advanced",
    "examples/integration",
    "src",
    "tests"
)

$files = @(
    ".gitignore",
    "pyproject.toml",
    "pytest.ini",
    "MANIFEST.in",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "requirements.txt",

    "docs\api.md",
    "docs\architecture.md",
    "docs\installation.md",
    "docs\usage.md",

    "examples\basic\README.md",
    "examples\basic\requirements.txt",

    "examples\advanced\README.md",

    "examples\integration\README.md",

    "tests\__init__.py",

    "src\$moduleName\__init__.py"
)

$createdDirectories = 0
$createdFiles = 0
$skippedDirectories = 0
$skippedFiles = 0

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = "Stop"

try {

    # -------------------------------------------------
    # Package Root
    # -------------------------------------------------

    if (!(Test-Path $packagePath)) {

        New-Item `
            -ItemType Directory `
            -Path $packagePath | Out-Null

        Write-Host "Created package      : $PackageName" -ForegroundColor Green
    }
    else {

        Write-Host "Package exists       : $PackageName" -ForegroundColor Yellow
    }

    # -------------------------------------------------
    # Directories
    # -------------------------------------------------

    foreach ($dir in $directories) {

        $path = Join-Path $packagePath $dir

        if (!(Test-Path $path)) {

            New-Item `
                -ItemType Directory `
                -Path $path | Out-Null

            Write-Host "Created directory   : $dir" -ForegroundColor Green
            $createdDirectories++
        }
        else {

            Write-Host "Skipped directory   : $dir" -ForegroundColor Yellow
            $skippedDirectories++
        }
    }

    # -------------------------------------------------
    # Python Package
    # -------------------------------------------------

    $srcPackage = Join-Path $packagePath "src\$moduleName"

    if (!(Test-Path $srcPackage)) {

        New-Item `
            -ItemType Directory `
            -Path $srcPackage | Out-Null

        Write-Host "Created module      : src\$moduleName" -ForegroundColor Green
        $createdDirectories++
    }
    else {

        Write-Host "Skipped module      : src\$moduleName" -ForegroundColor Yellow
        $skippedDirectories++
    }

    # -------------------------------------------------
    # Files
    # -------------------------------------------------

    foreach ($file in $files) {

        $path = Join-Path $packagePath $file

        if (!(Test-Path $path)) {

            New-Item `
                -ItemType File `
                -Path $path | Out-Null

            Write-Host "Created file        : $file" -ForegroundColor Green
            $createdFiles++
        }
        else {

            Write-Host "Skipped file        : $file" -ForegroundColor Yellow
            $skippedFiles++
        }
    }

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host " Package structure is ready." -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Package  : $PackageName"
    Write-Host "Module   : $moduleName"
    Write-Host "Location : $packagePath"

    Write-Host ""
    Write-Host "Summary" -ForegroundColor Cyan
    Write-Host "-------"

    Write-Host "Directories Created : $createdDirectories"
    Write-Host "Directories Skipped : $skippedDirectories"

    Write-Host ""

    Write-Host "Files Created       : $createdFiles"
    Write-Host "Files Skipped       : $skippedFiles"

    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "Package creation failed." -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}