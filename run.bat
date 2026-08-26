@echo off
setlocal EnableDelayedExpansion
title AI English Learning Platform - VihTech 2026

REM Set UTF-8 encoding for Python and console
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"

REM 1. Set working directory to script folder
cd /d "%~dp0"

REM 2. Try default python command first
python run.py
if %ERRORLEVEL% EQU 0 goto :DONE

REM 3. Try py launcher
py -3 run.py
if %ERRORLEVEL% EQU 0 goto :DONE

REM 4. Try direct Python313 path
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" run.py
    if %ERRORLEVEL% EQU 0 goto :DONE
)

REM 5. If all failed, show error message
echo.
echo ======================================================================
echo  [ERROR] Python is not installed or not found in system PATH.
echo  Please install Python 3.10+ and check "Add Python to PATH".
echo ======================================================================
echo.
pause

:DONE
endlocal
