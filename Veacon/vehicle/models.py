from django.db import models

from user_veacon.models import UserVeaconModel


class VehicleModel(models.Model):
    users = models.ManyToManyField(UserVeaconModel)
    plaque = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.plaque

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"