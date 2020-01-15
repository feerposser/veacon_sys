from django.db import models


class GatewayBeaconModel(models.Model):
    obs = models.TextField(blank=True, null=True, verbose_name="Observação")

    def __str__(self):
        return self.obs

    class Meta:
        verbose_name = "Gateway Beacons"
        verbose_name_plural = "Beacons Gateways"