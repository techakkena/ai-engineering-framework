param(
    [string]$Root = "..\ai-core\tests"
)

Write-Host ""
Write-Host "======================================="
Write-Host " AI Framework Test Cleanup"
Write-Host "======================================="
Write-Host ""

Get-ChildItem -Path $Root -Recurse -Filter "*.py" | ForEach-Object {

    $file = $_.FullName
    $lines = Get-Content $file

    $newLines = @()

    $skip = $false

    foreach ($line in $lines) {

        # Skip the main() function
        if ($line -match '^\s*def\s+main\s*\(') {
            $skip = $true
            continue
        }

        # Stop skipping when __name__ block starts
        if ($skip -and $line -match '^\s*if\s+__name__\s*==\s*["'']__main__["'']\s*:') {
            $skip = $false
            continue
        }

        # Remove __name__ block
        if ($line -match '^\s*if\s+__name__\s*==\s*["'']__main__["'']\s*:') {
            continue
        }

        # Remove main() call
        if ($line -match '^\s*main\(\)\s*$') {
            continue
        }

        if (-not $skip) {
            $newLines += $line
        }
    }

    Set-Content -Path $file -Value $newLines

    Write-Host "Cleaned:" $_.Name
}

Write-Host ""
Write-Host "Done."