from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.models import Notification
from task.models import Task


@receiver(post_save,sender=Task)
def send_notification(sender, instance, created, **kwargs):
    if created:
        user=instance.assign_to
        notification=Notification.objects.create(
            to_user=user,
            title=f"{instance.title} - ",
            descriptions='salom')
        return notification
    else:
        if created:
            user = instance.assign_to
            notification = Notification.objects.create(
                to_user=user,
                title=f"{instance.title} update",
                description=f"{instance.description}")
            return notification
