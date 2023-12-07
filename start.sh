#!/bin/bash

# Activate your virtual environment if needed
# source /path/to/your/virtualenv/bin/activate

# Run the FastAPI server using uvicorn
uvicorn backend.app.config:app --host 127.0.0.1 --port 8000 --reload
