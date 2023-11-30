@echo off

rem Activate your virtual environment if needed
rem call \path\to\your\virtualenv\Scripts\activate

rem Run the FastAPI server using uvicorn
uvicorn config:app --host 127.0.0.1 --port 8000 --reload
