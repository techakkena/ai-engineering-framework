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
# Create __init__.py
# --------------------------------------------------

$initFile = Join-Path $testModule "__init__.py"

if (!(Test-Path $initFile)) {

    New-Item `
        -ItemType File `
        -Path $initFile `
        -Force | Out-Null

    Write-Host "Created test file   : tests\$module\__init__.py" -ForegroundColor DarkGray
    $createdFiles++
}
else {

    Write-Host "Skipped test file   : tests\$module\__init__.py" -ForegroundColor Yellow
    $skippedFiles++
}

# --------------------------------------------------
# Create Standard Test Files
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