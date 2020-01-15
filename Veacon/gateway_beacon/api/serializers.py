from rest_framework.serializers import ModelSerializer

from gateway_beacon.models import GatewayBeaconModel


class GatewayBeaconSerializer(ModelSerializer):

    class Meta:
        model = GatewayBeaconModel
        fields = ('id', 'obs')
