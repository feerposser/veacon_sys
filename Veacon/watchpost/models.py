from django.db import models

from gateway_beacon.models import GatewayBeaconModel
from vehicle.models import VehicleModel
from beacon.models import BeaconModel
from user_veacon.models import UserVeaconModel

class WatchpostModel(models.Model):
    STATUS_CHOICES = (
        ('A', 'Ativo'),
        ('I', 'Invativo')
    )

    gateway_beacon = models.ForeignKey(GatewayBeaconModel, on_delete=models.DO_NOTHING)
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    beacon = models.ForeignKey(BeaconModel, on_delete=models.DO_NOTHING, help_text="Não mexer")
    user_veacon = models.ForeignKey(UserVeaconModel, on_delete=models.DO_NOTHING, unique=False)
    start_date = models.DateField(auto_now=True)
    start_hour = models.TimeField(auto_now=True)
    end_date = models.DateField(null=True, blank=True)
    end_hour = models.TimeField(null=True, blank=True)
    rssi = models.FloatField(null=True, blank=True, help_text="Não mexer",
                             verbose_name="Indicador de Intensidade de Sinal Recebido")
    obs = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    last_update = models.DateTimeField(null=True, blank=True, help_text="Não mexer")

    def __str__(self):
        return str(self.start_date) + " - " + self.vehicle.plaque

    class Meta:
        verbose_name = "Monitoramento"
        verbose_name_plural = "Monitoramenros"