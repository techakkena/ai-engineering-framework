param(
    [Parameter(Mandatory = $true)]
    [string]$Directory,

    [Parameter(Mandatory = $true)]
    [string[]]$Files
)

Write-Host ""
Write-Host "========================================="
Write-Host " AI Engineering Framework"
Write-Host " File Generator"
Write-Host "========================================="
Write-Host ""

# Check directory exists
if (!(Test-Path $Directory)) {
    Write-Host "Directory does not exist:"
    Write-Host $Directory
    exit
}

foreach ($file in $Files) {

    $path = Join-Path $Directory $file

    if (!(Test-Path $path)) {

        New-Item `
            -ItemType File `
            -Path $path `
            -Force | Out-Null

        Write-Host "[CREATED] $file"

    }
    else {

        Write-Host "[EXISTS ] $file"

    }

}

Write-Host ""
Write-Host "Completed Successfully."
Write-Host ""