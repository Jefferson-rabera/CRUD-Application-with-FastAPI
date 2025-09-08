@echo off
echo ===============================
echo Starting FastAPI CRUD Application
echo ===============================

REM Activate virtual environment
call venv\Scripts\activate

REM Check if virtual environment activated successfully
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    echo Please make sure venv exists and Python is installed
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Checking dependencies...
pip install -r requirements.txt

REM Start the FastAPI application
echo Starting server...
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

REM Keep window open after server stops
pause