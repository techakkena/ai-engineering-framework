param(
    [Parameter(Mandatory = $true)]
    [string]$ServiceName
)

Write-Host ""
Write-Host "======================================="
Write-Host " Creating AI Service : $ServiceName"
Write-Host "======================================="
Write-Host ""

$root = "..\$ServiceName"

# =====================================================
# Directories
# =====================================================

$folders = @(
    "$root",

    "$root\docs",

    "$root\examples",
    "$root\examples\basic",
    "$root\examples\advanced",
    "$root\examples\integration",

    "$root\tests",

    "$root\src",

    "$root\src\config",
    "$root\src\database",
    "$root\src\models",
    "$root\src\schemas",
    "$root\src\routes",
    "$root\src\services",
    "$root\src\middleware",
    "$root\src\security",
    "$root\src\utils"
)

foreach ($folder in $folders) {

    New-Item `
        -ItemType Directory `
        -Force `
        -Path $folder | Out-Null

    Write-Host "Created Folder : $folder"
}

# =====================================================
# Files
# =====================================================

$files = @(

    "$root\README.md",
    "$root\CHANGELOG.md",
    "$root\requirements.txt",
    "$root\.gitignore",

    "$root\src\main.py",
    "$root\src\__init__.py",

    "$root\src\config\config.py",
    "$root\src\config\__init__.py",

    "$root\src\database\database.py",
    "$root\src\database\__init__.py",

    "$root\src\models\user.py",
    "$root\src\models\__init__.py",

    "$root\src\schemas\user_schema.py",
    "$root\src\schemas\token_schema.py",
    "$root\src\schemas\__init__.py",

    "$root\src\routes\auth_routes.py",
    "$root\src\routes\__init__.py",

    "$root\src\services\auth_service.py",
    "$root\src\services\user_service.py",
    "$root\src\services\__init__.py",

    "$root\src\middleware\auth_middleware.py",
    "$root\src\middleware\__init__.py",

    "$root\src\security\jwt_handler.py",
    "$root\src\security\password.py",
    "$root\src\security\__init__.py",

    "$root\src\utils\helpers.py",
    "$root\src\utils\constants.py",
    "$root\src\utils\__init__.py",

    "$root\docs\architecture.md",
    "$root\docs\api.md",
    "$root\docs\installation.md",
    "$root\docs\usage.md",

    "$root\examples\basic\README.md",
    "$root\examples\basic\main.py",
    "$root\examples\basic\requirements.txt",

    "$root\examples\advanced\README.md",
    "$root\examples\advanced\main.py",

    "$root\examples\integration\README.md",
    "$root\examples\integration\main.py",

    "$root\tests\__init__.py",
    "$root\tests\test_routes.py",
    "$root\tests\test_services.py",
    "$root\tests\test_models.py"
)

foreach ($file in $files) {

    New-Item `
        -ItemType File `
        -Force `
        -Path $file | Out-Null

    Write-Host "Created File   : $file"
}

Write-Host ""
Write-Host "======================================="
Write-Host " AI Service Created Successfully"
Write-Host "======================================="
Write-Host ""