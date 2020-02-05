from django.db import models

from gateway_beacon.models import GatewayBeaconModel
from vehicle.models import VehicleModel
from beacon.models import BeaconModel
from user_veacon.models import UserVeaconModel

from utils.pubnub import PubSubManager


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
    rssi_far = models.FloatField(null=True, blank=True, help_text="RSSI mais distante", verbose_name="RSSI distante")
    rssi_near = models.FloatField(null=True, blank=True, help_text="RSSI mais próximo", verbose_name="RSSI próximo")
    obs = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    last_update = models.DateTimeField(null=True, blank=True, help_text="Não mexer")

    def __str__(self):
        return str(self.start_date) + " - " + self.vehicle.plaque

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        Publica o monitoramento no canal pub sub do veacon e persiste os dados no banco
        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return:
        """
        PubSubManager().publish_in_gateway_channel(self.beacon.eddy_namespace, "add", self.gateway_beacon.id)
        super(WatchpostModel, self).save()

    class Meta:
        verbose_name = "Monitoramento"
        verbose_name_plural = "Monitoramenros"
