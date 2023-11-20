# tasks.py
from celery import Celery
import time

# Create a Celery instance
app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',  # URL to your Redis server
    backend='redis://localhost:6379/0',
)

@app.task
def hello_world():
    time.sleep(5)  # Simulate some task processing time
    print( 'Hello, World!'
    )