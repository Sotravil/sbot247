@echo off

REM Find the directory of the Python file
for %%I in ("%~dp0.") do set "SCRIPT_DIR=%%~fI"

REM Navigate to the script directory
cd /d "%SCRIPT_DIR%"

REM Run the Python script
python sbot247.py

REM Pause the batch file to see any error messages
pause
