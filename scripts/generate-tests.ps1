param(
    [Parameter(Mandatory = $true)]
    [string]$Root
)

Write-Host ""
Write-Host "========================================="
Write-Host " AI Framework Test Generator"
Write-Host "========================================="
Write-Host ""

$processed = 0
$generated = 0
$skipped = 0

Get-ChildItem -Path $Root -Filter "*.py" -Recurse | ForEach-Object {

    $processed++

    $file = $_.FullName
    $content = Get-Content $file -Raw

    # Skip if tests already exist
    if ($content -match "(?m)^def\s+test_") {

        Write-Host "[SKIP] Tests already exist -> $($_.Name)" -ForegroundColor Yellow
        $skipped++
        return
    }

    # Find Demo class
    $match = [regex]::Match($content, "class\s+(Demo\w+)\s*\(")

    if (!$match.Success) {

        Write-Host "[SKIP] No Demo class -> $($_.Name)" -ForegroundColor DarkYellow
        $skipped++
        return
    }

    $className = $match.Groups[1].Value

    $test = @"

def test_${className.ToLower()}_creation():
    obj = $className()

    assert obj is not None

"@

    Add-Content $file $test

    Write-Host "[OK] Added tests -> $($_.Name)" -ForegroundColor Green
    $generated++
}

Write-Host ""
Write-Host "========================================="
Write-Host " Summary"
Write-Host "========================================="
Write-Host "Processed : $processed"
Write-Host "Generated : $generated"
Write-Host "Skipped   : $skipped"
Write-Host ""