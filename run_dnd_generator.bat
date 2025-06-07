:: run_dnd_generator.bat
:: Double-click this file to run the D&D Item Generator

@echo off
cd /d "%~dp0"
python main_app.py
if errorlevel 1 (
    echo.
    echo Error running the application. Make sure Python is installed.
    echo.
    pause
)