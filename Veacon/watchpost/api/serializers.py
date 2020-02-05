from rest_framework.serializers import ModelSerializer

from watchpost.models import WatchpostModel
from gateway_beacon.api.serializers import GatewayBeaconSerializer
from vehicle.api.serializers import VehicleSerializer
from beacon.api.serializers import BeaconSerializer
from user_veacon.api.serializers import UserVeaconSerializer


class WatchpostSerializer(ModelSerializer):
    gateway_beacon = GatewayBeaconSerializer()
    vehicle = VehicleSerializer()
    beacon = BeaconSerializer()
    user_veacon = UserVeaconSerializer()

    class Meta:
        model = WatchpostModel
        fields = ('id', 'user_veacon', 'gateway_beacon', 'beacon', 'vehicle', 'rssi_far', 'rssi_near', 'obs')
