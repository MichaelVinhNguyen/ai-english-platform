@echo off
setlocal EnableDelayedExpansion
title AI English Learning Platform - VihTech 2026

REM Set UTF-8 encoding for Windows Command Prompt and Python
chcp 65001 >nul
set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"

REM 1. Set working directory to project root folder
cd /d "%~dp0"

echo ======================================================================
echo   AI ENGLISH LEARNING PLATFORM - VIHTECH 2026
echo   Dang khoi dong he thong Flashcards 30 Chu De (1,500 Tu Vung)...
echo ======================================================================
echo.

REM 2. Try default python command first
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python run.py
    goto :EXIT_CHECK
)

REM 3. Try py launcher
py -3 --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    py -3 run.py
    goto :EXIT_CHECK
)

REM 4. Try Python in AppData (Python 3.10, 3.11, 3.12, 3.13)
for %%v in (Python313 Python312 Python311 Python310 Python39) do (
    if exist "%LOCALAPPDATA%\Programs\Python\%%v\python.exe" (
        "%LOCALAPPDATA%\Programs\Python\%%v\python.exe" run.py
        goto :EXIT_CHECK
    )
)

REM 5. If all failed, show error message
echo.
echo ======================================================================
echo  [ERROR] Khong tim thay Python trong he thong PATH.
echo  Vui long cai dat Python 3.10+ va tich vao "Add Python to PATH".
echo ======================================================================
echo.

:EXIT_CHECK
echo.
echo Server da dung. Nhan phim bat ky de thoat...
pause >nul

:DONE
endlocal
