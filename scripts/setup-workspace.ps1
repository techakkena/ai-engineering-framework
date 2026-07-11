Write-Host "Setting up AI Engineering Framework..." -ForegroundColor Cyan

python -m venv .venv

.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

pip install pre-commit
pip install build
pip install mypy
pip install black
pip install ruff
pip install pytest

pre-commit install

Write-Host ""
Write-Host "Workspace is ready." -ForegroundColor Green