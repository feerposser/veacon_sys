from django.db import models


class GatewayBeaconModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    obs = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gateway Beacons"
        verbose_name_plural = "Beacons Gateways"
