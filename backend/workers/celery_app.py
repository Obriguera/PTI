import os
from celery import Celery

app = Celery(
    "pti",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
)

app.conf.task_routes = {
    "workers.tasks.*": {"queue": "default"},
}
