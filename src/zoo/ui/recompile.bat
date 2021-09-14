@echo off

REM Stash current directory
setlocal disabledelayedexpansion
set currentpath=%cd%

REM Go to directory where this script is
cd %~dp0

REM Compile
pyuic5 zoo.ui -o zoo_ui.py

REM Return to original directory
cd %currentpath%
