from django.apps import AppConfig


class TaskCreatingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_creating'

    def ready(self):
        from . import signals
