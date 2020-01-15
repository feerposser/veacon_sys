from django.core.exceptions import ObjectDoesNotExist

from utils.utils import is_from_group
from .models import VehicleModel


def get_vehicles_user(user):
    try:
        return VehicleModel.objects.filter(users__user__username=user.username)
    except ObjectDoesNotExist as o:
        print(o)
        return None


def get_vehicles_all(status=None):
    try:
        if status:
            return VehicleModel.objects.filter(status=status)
        return VehicleModel.objects.all()
    except ObjectDoesNotExist as o:
        print(o)
        return None


def get_vehicles(user):
    """
    Procura os alertas referentes ao usuário solicitante. Se for um usuário normal, retorna apenas os alertas
    criados por ele. Se for um adm ou ssp group retorna todos
    :param user: django.contrib.auth.models.User
    :return: querySet
    """

    if is_from_group(user, 'ssp') or user.is_superuser:
        return get_vehicles_all()
    else:
        return get_vehicles_user(user)
