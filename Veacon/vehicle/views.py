from django.shortcuts import render

from .manage_data import get_vehicles


def vehicles(request):
    vehicles_list = get_vehicles(request.user)
    return render(request, 'vehicles.html', {'vehicles': vehicles_list})
