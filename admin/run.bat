@echo off
echo Starting Flask server...
start cmd /c "python app.py"
ping 127.0.0.1 -n 2 > nul
start firefox http://127.0.0.1:5000