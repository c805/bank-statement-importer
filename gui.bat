@echo off

if not exist ".venv\Scripts\python.exe" (
    echo Virtual environment not found.
    echo.
    echo Please create it first:
    echo    python -m venv .venv
    echo    .venv\Scripts\pip install -r requirements.txt
    pause
    exit /b
)

.venv\Scripts\python.exe -m src.app.main_app

pause