@echo off

REM Generate a random port between 10000 and 50000
set /a port=%random% * 40000 / 32768 + 10000

REM Open the default web browser to the local server URL
start http://localhost:%port%

REM Start a simple HTTP server with Python
python -m http.server %port%
