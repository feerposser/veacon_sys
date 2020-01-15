from rest_framework.serializers import ModelSerializer

from beacon.models import BeaconModel


class BeaconSerializer(ModelSerializer):

    class Meta:
        model = BeaconModel
        fields = ('obs', 'eddy_namespace')
