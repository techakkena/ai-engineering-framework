param(
    [Parameter(Mandatory = $true)]
    [string]$Root
)

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " Test Generator" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = "Stop"

try {

    if (!(Test-Path $Root)) {
        throw "Package not found: $Root"
    }

    $src = Join-Path $Root "src"
    $tests = Join-Path $Root "tests"

    if (!(Test-Path $src)) {
        throw "src directory not found."
    }

    if (!(Test-Path $tests)) {
        New-Item `
            -ItemType Directory `
            -Path $tests | Out-Null
    }

    $processed = 0
    $generated = 0
    $skipped = 0
    $directories = 0

    Get-ChildItem `
        -Path $src `
        -Filter "*.py" `
        -Recurse |
    Where-Object {

        $_.Name -notin @(
            "__init__.py"
        )

    } | ForEach-Object {

        $processed++

        $relative = $_.DirectoryName.Substring($src.Length).TrimStart("\")
        $targetDirectory = Join-Path $tests $relative

        if (!(Test-Path $targetDirectory)) {

            New-Item `
                -ItemType Directory `
                -Path $targetDirectory | Out-Null

            $directories++

            Write-Host "Created directory : tests\$relative" -ForegroundColor Green
        }

        $testFile = Join-Path $targetDirectory ("test_" + $_.Name)

        if (Test-Path $testFile) {

            Write-Host "Skipped test : $($testFile.Replace($Root + '\',''))" -ForegroundColor Yellow
            $skipped++
            return
        }

        $module = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)

        $content = @"
\"\"\"
Unit tests for $module.
\"\"\"

def test_placeholder():

    assert True
"@

        Set-Content `
            -Path $testFile `
            -Value $content `
            -Encoding UTF8

        Write-Host "Generated test : $($testFile.Replace($Root + '\',''))" -ForegroundColor Green

        $generated++
    }

    Write-Host ""
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host " Test Generation Complete" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Modules Processed    : $processed"
    Write-Host "Directories Created  : $directories"
    Write-Host "Tests Generated      : $generated"
    Write-Host "Tests Skipped        : $skipped"

    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "Test generation failed." -ForegroundColor Red
    Write-Host $_.Exception.Message

    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}