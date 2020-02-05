from django.db import models

from watchpost.models import WatchpostModel


class AlertModel(models.Model):
    CHOICES = (
        ('')
    )
    watchpost_fk = models.ForeignKey(WatchpostModel, on_delete=models.DO_NOTHING, verbose_name="Monitoramento")
    date = models.DateField(auto_now=True, editable=True)
    hour = models.TimeField(auto_now=True, editable=True)
    status = models.CharField(max_length=10, default='A')
    obs = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.watchpost_fk.vehicle.plaque) + " - " + str(self.date) + ":" + str(self.hour)

    def get_date_hour(self):
        return self.date.strftime("%m/%d/%Y") + self.hour.strftime('%H:%M')

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"