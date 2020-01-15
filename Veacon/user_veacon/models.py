from django.db import models
from django.contrib.auth.models import User


class UserVeaconModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Veacon User"
        verbose_name_plural = "Veacon Users"
