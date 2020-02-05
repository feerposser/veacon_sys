from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from alert.models import AlertModel, WatchpostModel
from .serializers import AlertSerializer


class AlertViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    serializer_class = AlertSerializer

    def get_queryset(self):
        return AlertModel.pbjects.all(status='A')

    def create(self, request, *args, **kwargs):
        try:
            assert 'watchpost_fk' in request.data, "'watchpost_fk' not found"

            obs = None

            if 'obs' in request.data:
                obs = request.data['obs']

            watchpost_fk = int(request.data['watchpost_fk'])

            print('-->', watchpost_fk, type(watchpost_fk))

            alert = AlertModel.objects.create(
                watchpost_fk=WatchpostModel.objects.get(id=watchpost_fk),
                obs=obs
            )

            return Response({'id': alert.id})

        except AssertionError as a:
            return Response({a.args})
        except Exception as e:
            return Response({e.args[0]})
