#!/bin/bash

# Activate your virtual environment if needed
# source /path/to/your/virtualenv/bin/activate

# Run the FastAPI server using uvicorn
cd ./backend/app/

uvicorn config:app --host 0.0.0.0 --port 8000 --reload
