@echo off
setlocal enabledelayedexpansion

echo   /$$$$$$              /$$                                   /$$ /$$
echo  /$$__  $$            ^| $$                                  ^|__/^| $$
echo ^| $$  \__/  /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$  /$$    /$$ /$$^| $$
echo ^|  $$$$$$  /$$__  $$^|^  $$_/   /$$__  $$^|____  $$^|  $$  /$$/^| $$^| $$
echo  \____  $$^| $$  \ $$  ^| $$    ^| $$  \__/ /$$$$$$$ \  $$/$$/ ^| $$^| $$
echo  /$$  \ $$^| $$  ^| $$  ^| $$ /$$^| $$      /$$__  $$  \  $$$/  ^| $$^| $$
echo ^|  $$$$$$/^|  $$$$$$/  ^|  $$$$/^| $$     ^|  $$$$$$$   \  $/   ^| $$^| $$
echo  \______/  \______/    \___/  ^|__/      \_______/    \_/    ^|__/^|__/
echo.
echo.
echo --------------------------------------------
echo              Sotravil (c) 2023
echo --------------------------------------------
echo.

echo Installing dependencies...
echo.

echo Checking Python version...
python --version

echo.

echo Installing selenium, undetected-chromedriver, and PySimpleGUI...
pip install selenium undetected-chromedriver PySimpleGUI

echo.
echo Dependencies installed successfully!

echo.

echo  /$$$$$$              /$$                                   /$$ /$$
echo /$$__  $$            ^| $$                                  ^|__/^| $$
echo ^| $$  \__/  /$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$  /$$    /$$ /$$^| $$
echo ^|  $$$$$$  /$$__  $$^|^  $$_/   /$$__  $$^|____  $$^|  $$  /$$/^| $$^| $$
echo  \____  $$^| $$  \ $$  ^| $$    ^| $$  \__/ /$$$$$$$ \  $$/$$/ ^| $$^| $$
echo /$$  \ $$^| $$  ^| $$  ^| $$ /$$^| $$      /$$__  $$  \  $$$/  ^| $$^| $$
echo ^|  $$$$$$/^|  $$$$$$/  ^|  $$$$/^| $$     ^|  $$$$$$$   \  $/   ^| $$^| $$
echo  \______/  \______/    \___/  ^|__/      \_______/    \_/    ^|__/^|__/
echo.
echo.
echo --------------------------------------------
echo              Sotravil (c) 2023
echo --------------------------------------------
echo.

echo Press any key to exit.
pause > nul
