from django.db.models.signals import post_save
from .models import AlertModel


def send_pubsub_message(sender, instance, created, **kwargs):
    if created:
        pass


post_save.connect(send_pubsub_message, sender=AlertModel)
