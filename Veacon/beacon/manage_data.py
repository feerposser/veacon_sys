from django.core.exceptions import ObjectDoesNotExist

from utils.utils import is_from_group
from .models import BeaconModel


def count_beacon_user(user):
    try:
        return BeaconModel.objects.filter(user=user).count()
    except ObjectDoesNotExist as o:
        print(o)
        return None
    except Exception as e:
        print(e)
        return None


def count_beacon_all():
    try:
        return BeaconModel.objects.all().count()
    except ObjectDoesNotExist as o:
        print(o)
        return None
    except Exception as e:
        print(e)
        return None


def count_beacons(user):
    """
    Conta os beacons referentes ao usuário solicitante. Se for um usuário normal, retorna apenas os alertas
    criados por ele. Se for um adm ou ssp group retorna todos
    :param user: django.contrib.auth.models.User
    :return: querySet ou none
    """
    if is_from_group(user, 'ssp') or user.is_superuser:
        return count_beacon_all()
    else:
        return count_beacon_user(user)
