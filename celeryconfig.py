# celeryconfig.py
from celery.schedules import crontab

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "rpc://"
CELERYBEAT_SCHEDULE = {
    "nightly-task": {
        "task": "tasks.nightly_task",
        "schedule": crontab(minute=40, hour=0),
    },
}
