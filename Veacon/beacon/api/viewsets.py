from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from beacon.models import BeaconModel
from .serializers import BeaconSerializer


class BeaconViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = BeaconSerializer

    def get_queryset(self):
        return BeaconModel.objects.all()
