from watchpost.models import WatchpostModel


class GatewayBeaconManager:
    """
    Classe responsável pelo gerenciamento de dados dos gateways
    """

    def __init__(self, gateway_beacon_id):
        """
        :param gateway_beacon_id: id do gateway
        """
        self.gateway_beacon_id = gateway_beacon_id

    def get_beacons_in_watchposts(self, status='A'):
        """
        Retorna os beacons dos watchposts monitorados por um gateway (id do __init__)
        :param status: status do watchpost
        :return: django queryset ou None
        """
        if WatchpostModel.objects.filter(gateway_beacon=self.gateway_beacon_id, status=status).exists():
            return WatchpostModel.objects.filter(gateway_beacon=self.gateway_beacon_id, status='A').values('beacon')
        return None
