import logging

from celery.result import AsyncResult
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Task
from .tasks import task_start_notification


@receiver(post_save, sender=Task)
def post_save_task_create_celery_task(sender, instance: Task, created, **kwargs):
    """
    При создании задачи создаётся цепочка задач в Celery, чтобы потом уведомить пользователя
    """
    if created:
        delay = (instance.start_datetime - timezone.now()).total_seconds()
        celery_task = task_start_notification.apply_async(instance, countdown=delay)
        task_id = celery_task.id
        instance.celery_task_id = task_id
        instance.save()
        logging.info(f"Task with PK {instance.pk} and ID {task_id} HAS BEEN CREATED! delay: {round(delay, 1)} s.")


@receiver(pre_delete, sender=Task)
def pre_delete_task_destroy_celery_task(sender, instance: Task, **kwargs):
    """
    При удалении задачи, лучше убрать её из очереди!
    """
    task_id = instance.celery_task_id
    if task_id:
        found_task = AsyncResult(task_id)
        if found_task.state in ['PENDING', "STARTED"]:
            found_task.revoke(terminate=True)
            logging.info(f"Task with PK {instance.pk} and ID {task_id} HAS BEEN TERMINATED!")

