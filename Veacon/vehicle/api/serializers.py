from rest_framework.serializers import ModelSerializer

from vehicle.models import VehicleModel
from beacon.api.serializers import BeaconSerializer
from user_veacon.api.serializers import UserVeaconSerializer


class VehicleSerializer(ModelSerializer):
    users = UserVeaconSerializer(many=True)

    class Meta:
        model = VehicleModel
        fields = ('users', 'plaque', 'color', 'model', 'brand')
