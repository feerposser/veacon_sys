from django.db import models

from django.contrib.auth.models import User


class BeaconModel(models.Model):
    obs = models.TextField(null=True, blank=True, verbose_name="Observação")
    eddy_namespace = models.CharField(max_length=200, verbose_name="Eddystone namespace")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.obs

    class Meta:
        verbose_name = "Beacon"
        verbose_name_plural = "Beacons"