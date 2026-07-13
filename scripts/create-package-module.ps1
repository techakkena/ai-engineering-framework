param(
    [Parameter(Mandatory = $true)]
    [string]$Package,

    [Parameter(Mandatory = $true)]
    [string[]]$Modules
)

$root = Resolve-Path (Join-Path $PSScriptRoot "..")

$packageRoot = Join-Path $root $Package

$createdDirectories = 0
$skippedDirectories = 0
$createdFiles = 0
$skippedFiles = 0

$packageModule = $Package.Replace("-", "_")

if (!(Test-Path $packageRoot)) {
    throw "Package not found: $Package"
}

$moduleRoot = Join-Path $packageRoot "src\$packageModule"

$testRoot = Join-Path $packageRoot "tests"

$sourceFiles = @(
    "__init__.py",
    "constants.py",
    "exceptions.py",
    "operations.py"
)

$testFiles = @(
    "__init__.py",
    "test_constants.py",
    "test_exceptions.py",
    "test_operations.py"
)

if (!(Test-Path $moduleRoot)) {

    New-Item `
        -ItemType Directory `
        -Path $moduleRoot `
        -Force | Out-Null

    $createdDirectories++
}

if (!(Test-Path $testRoot)) {

    New-Item `
        -ItemType Directory `
        -Path $testRoot `
        -Force | Out-Null

    $createdDirectories++
}

foreach ($module in $Modules) {

    # --------------------------------------------------
    # Source Module
    # --------------------------------------------------

    $modulePath = Join-Path $moduleRoot $module

    if (!(Test-Path $modulePath)) {

        New-Item `
            -ItemType Directory `
            -Path $modulePath `
            -Force | Out-Null

        Write-Host "Created module      : src\$packageModule\$module" -ForegroundColor Green
        $createdDirectories++
    }
    else {

        Write-Host "Skipped module      : src\$packageModule\$module" -ForegroundColor Yellow
        $skippedDirectories++
    }

    # --------------------------------------------------
    # Source Files
    # --------------------------------------------------

    foreach ($file in $sourceFiles) {

        $path = Join-Path $modulePath $file

        if (!(Test-Path $path)) {

            New-Item `
                -ItemType File `
                -Path $path `
                -Force | Out-Null

            Write-Host "Created file        : src\$packageModule\$module\$file" -ForegroundColor DarkGray
            $createdFiles++
        }
        else {

            Write-Host "Skipped file        : src\$packageModule\$module\$file" -ForegroundColor Yellow
            $skippedFiles++
        }
    }

    # --------------------------------------------------
    # Test Module
    # --------------------------------------------------

    $testModule = Join-Path $testRoot $module

    if (!(Test-Path $testModule)) {

        New-Item `
            -ItemType Directory `
            -Path $testModule `
            -Force | Out-Null

        Write-Host "Created tests       : tests\$module" -ForegroundColor Green
        $createdDirectories++
    }
    else {

        Write-Host "Skipped tests       : tests\$module" -ForegroundColor Yellow
        $skippedDirectories++
    }
  
    # --------------------------------------------------
    # Standard Test Files
    # --------------------------------------------------

    foreach ($file in $testFiles) {

        $path = Join-Path $testModule $file

        if (!(Test-Path $path)) {

            New-Item `
                -ItemType File `
                -Path $path `
                -Force | Out-Null

            Write-Host "Created test file   : tests\$module\$file" -ForegroundColor DarkGray
            $createdFiles++
        }
        else {

            Write-Host "Skipped test file   : tests\$module\$file" -ForegroundColor Yellow
            $skippedFiles++
        }
    }
}