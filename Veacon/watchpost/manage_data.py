from django.core.exceptions import ObjectDoesNotExist

from .models import WatchpostModel


class WatchpostManager:

    @staticmethod
    def get_watchpost_by_gateway(gateway_beacon_id):
        try:
            if WatchpostModel.objects.filter(gateway_beacon=gateway_beacon_id, status='A').exists():
                return WatchpostModel.objects.filter(gateway_beacon=gateway_beacon_id, status='A')
            raise ObjectDoesNotExist("Objeto inexistente")
        except ObjectDoesNotExist as e:
            return None