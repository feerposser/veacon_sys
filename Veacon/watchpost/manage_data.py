from django.core.exceptions import ObjectDoesNotExist

from utils.utils import is_from_group
from .models import WatchpostModel


def count_watchpost_user(user, status='A'):
    try:
        if status:
            return WatchpostModel.objects.filter(user_veacon__user=user, status='A').count()
        return WatchpostModel.objects.filter(user_veacon__user=user).count()
    except ObjectDoesNotExist as o:
        print(o)
        return None
    except Exception as e:
        print(e)
        return None


def count_watchpost_all(status='A'):
    try:
        if status:
            return WatchpostModel.objects.filter(status='A').count()
        return WatchpostModel.objects.all().count()
    except ObjectDoesNotExist as o:
        print(o)
        return None
    except Exception as e:
        print(e)
        return None


def count_watchposts(user):
    """
    Conta os monitoramentos referentes ao usuário solicitante. Se for um usuário normal, retorna apenas os alertas
    criados por ele. Se for um adm ou ssp group retorna todos
    :param user: django.contrib.auth.models.User
    :return: querySet ou none
    """
    if is_from_group(user, 'ssp') or user.is_superuser:
        return count_watchpost_all()
    else:
        return count_watchpost_user(user)


class WatchpostManager:

    @staticmethod
    def get_watchpost_by_gateway(gateway_beacon_id):
        try:
            if WatchpostModel.objects.filter(gateway_beacon=gateway_beacon_id, status='A').exists():
                return WatchpostModel.objects.filter(gateway_beacon=gateway_beacon_id, status='A')
            raise ObjectDoesNotExist("Objeto inexistente")
        except ObjectDoesNotExist as e:
            return None