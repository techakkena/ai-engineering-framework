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

# -------------------------------------------------
# Package Root
# -------------------------------------------------

if (!(Test-Path $packagePath)) {
    New-Item `
        -ItemType Directory `
        -Path $packagePath | Out-Null

    Write-Host "Created package: $PackageName" -ForegroundColor Green
}
else {
    Write-Host "Package already exists: $PackageName" -ForegroundColor Yellow
}

# -------------------------------------------------
# Directories
# -------------------------------------------------

$directories = @(
    "docs",
    "examples",
    "examples/basic",
    "examples/advanced",
    "examples/integration",
    "src",
    "tests"
)

foreach ($dir in $directories) {

    $path = Join-Path $packagePath $dir

    if (!(Test-Path $path)) {

        New-Item `
            -ItemType Directory `
            -Path $path | Out-Null

        Write-Host "Created directory : $dir" -ForegroundColor Green
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

    Write-Host "Created module directory : src\$moduleName" -ForegroundColor Green
}

# -------------------------------------------------
# Empty Files
# -------------------------------------------------

$files = @(
    ".gitignore",
    ".pre-commit-config.yaml",
    ".ruff.toml",
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

    "examples\basic\main.py",
    "examples\basic\README.md",
    "examples\basic\requirements.txt",

    "examples\advanced\main.py",
    "examples\advanced\README.md",

    "examples\integration\main.py",
    "examples\integration\README.md",

    "tests\__init__.py",

    "src\$moduleName\__init__.py"
)

foreach ($file in $files) {

    $path = Join-Path $packagePath $file

    if (!(Test-Path $path)) {

        New-Item `
            -ItemType File `
            -Path $path | Out-Null

        Write-Host "Created file      : $file" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Package structure is ready." -ForegroundColor Green
Write-Host "Location : $packagePath"
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""