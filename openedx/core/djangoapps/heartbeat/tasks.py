"""
A trivial task for health checks
"""


from celery.task import task
from django.conf import settings


@task(routing_key=settings.HEARTBEAT_CELERY_ROUTING_KEY, queue=settings.HIGH_PRIORITY_QUEUE)
def sample_task():
    return True
