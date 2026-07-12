param(
    [Parameter(Mandatory = $true)]
    [string]$Directory,

    [Parameter(Mandatory = $true)]
    [string[]]$Files
)

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host " AI Engineering Framework" -ForegroundColor Cyan
Write-Host " File Generator" -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$created = 0
$skipped = 0

$oldPreference = $ErrorActionPreference
$ErrorActionPreference = "Stop"

try {

    # -------------------------------------------------
    # Validate Directory
    # -------------------------------------------------

    if (!(Test-Path $Directory)) {

        throw "Directory does not exist: $Directory"
    }

    Write-Host "Directory : $Directory"
    Write-Host ""

    # -------------------------------------------------
    # Create Files
    # -------------------------------------------------

    foreach ($file in $Files) {

        $path = Join-Path $Directory $file

        if (!(Test-Path $path)) {

            New-Item `
                -ItemType File `
                -Path $path | Out-Null

            Write-Host "Created file    : $file" -ForegroundColor Green
            $created++
        }
        else {

            Write-Host "Skipped file    : $file" -ForegroundColor Yellow
            $skipped++
        }
    }

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    Write-Host ""
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host " File generation completed." -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Cyan
    Write-Host ""

    Write-Host "Summary" -ForegroundColor Cyan
    Write-Host "-------"

    Write-Host "Created : $created"
    Write-Host "Skipped : $skipped"

    Write-Host ""

}
catch {

    Write-Host ""
    Write-Host "File generation failed." -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}
finally {

    $ErrorActionPreference = $oldPreference
}