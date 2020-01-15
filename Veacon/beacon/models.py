from django.db import models


class BeaconModel(models.Model):
    obs = models.TextField(null=True, blank=True, verbose_name="Observação")
    eddy_namespace = models.CharField(max_length=200, verbose_name="Eddystone namespace")

    def __str__(self):
        return self.obs

    class Meta:
        verbose_name = "Beacon"
        verbose_name_plural = "Beacons"