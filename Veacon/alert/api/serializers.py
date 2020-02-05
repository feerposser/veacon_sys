from rest_framework.serializers import ModelSerializer

from alert.models import AlertModel
from watchpost.api.serializers import WatchpostSerializer


class AlertSerializer(ModelSerializer):

    watchpost_fk = WatchpostSerializer()

    class Meta:
        model = AlertModel
        fields = ('watchpost_fk', 'date', 'hour', 'status', 'obs')
