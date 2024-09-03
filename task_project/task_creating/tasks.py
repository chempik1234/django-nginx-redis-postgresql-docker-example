from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Task


@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def task_start_notification(task: Task):
    email_from = settings.DEFAULT_EMAIL_FROM
    send_mail(subject="Task started!",
              message=f"The task you called has started at {task.start_datetime} with name {task.name}.",
              from_email=email_from,
              recipient_list=[task.email],
              fail_silently=False)
