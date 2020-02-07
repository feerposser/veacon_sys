from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from watchpost.models import WatchpostModel
from .serializers import WatchpostSerializer
from watchpost.manage_data import WatchpostManager


class WatchpostViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    serializer_class = WatchpostSerializer

    def get_queryset(self):
        return WatchpostModel.objects.filter(status='A')


class WatchpostGatewayAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        gateway_beacon_id = request.query_params.get('gateway_beacon_id', None)

        if gateway_beacon_id:
            watchposts = WatchpostManager().get_watchpost_by_gateway(gateway_beacon_id)

            if watchposts:
                return Response(watchposts)

        return Response(status=status.HTTP_404_NOT_FOUND)
