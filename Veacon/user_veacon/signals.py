from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token as TokenModel

from .models import UserVeaconModel


def create_userveacon(sender, instance, created, **kwargs):
    if created:
        UserVeaconModel.objects.create(user=instance)
        TokenModel.objects.create(user=instance)


post_save.connect(create_userveacon, sender=User)

