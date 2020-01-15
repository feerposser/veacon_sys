from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from gateway_beacon.manage_data import GatewayBeaconManager


class GatewayBeaconViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        gateway_beacon_id = request.query_params.get('gateway_beacon_id', None)

        if gateway_beacon_id:
            gateway_beacon_manager = GatewayBeaconManager(gateway_beacon_id)

            beacons = gateway_beacon_manager.get_beacons_in_watchposts()

            if beacons:
                return Response(beacons)

        return Response(status=status.HTTP_404_NOT_FOUND)
