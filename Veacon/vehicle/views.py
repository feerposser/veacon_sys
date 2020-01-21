from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .manage_data import get_vehicles


@login_required(login_url='/login/')
def vehicles(request):
    vehicles_list = get_vehicles(request.user)
    return render(request, 'vehicles.html', {'vehicles': vehicles_list})
