@echo off
setlocal

rem Try to use py launcher first
where py >nul 2>nul
if %errorlevel%==0 (
    py -m pip show PyQt6 >nul 2>nul || py -m pip install --user PyQt6
    py "%~dp0career_guidance_qt.py"
    goto :eof
)

rem Fallback to python
where python >nul 2>nul
if %errorlevel%==0 (
    python -m pip show PyQt6 >nul 2>nul || python -m pip install --user PyQt6
    python "%~dp0career_guidance_qt.py"
    goto :eof
)

echo Python not found. Please install Python from https://www.python.org/downloads/
pause


