from django.apps import AppConfig


class TaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task'


    def ready(self):
        from task.signals import send_notification
        # from .signals import *