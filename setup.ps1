$ErrorActionPreference = "Stop"

Clear-Host
Write-Host "Valecraft Windows Setup" -ForegroundColor Cyan
Write-Host "`n[1/4] Checking Python"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
	Write-Host "Python was not found" -ForegroundColor Red
	exit 1
}

python --version

Write-Host "`n[2/4] Creating virtual environment"

if (-not (Test-Path ".venv")) {
	python -m venv .venv
	Write-Host "Virtual environment created" -ForegroundColor Green
}
else {
	Write-Host "Virtual environment already exists" -ForegroundColor Yellow
}

$python = ".venv\Scripts\python.exe"

Write-Host "`n[3/4] Updating pip"

& $python -m pip install --upgrade pip

Write-Host "`n[4/4] Installing Valecraft"

& $python -m pip install -e .

Write-Host "`nSetup complete!" -ForegroundColor Green