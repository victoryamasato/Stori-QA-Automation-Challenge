@echo off
cd "C:\StoriChallenge"
cmd /k python -m pytest --browser "chrome" src/TestCases -s --html="HTMLreport.html"