from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm
from vehicle.manage_data import count_vehicles
from alert.manage_data import count_alerts
from beacon.manage_data import count_beacons
from watchpost.manage_data import count_watchposts


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print('deu merda')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def index(request):
    data = {}

    try:
        vehicles = count_vehicles(request.user)
        alerts = count_alerts(request.user)
        beacons = count_beacons(request.user)
        watchposts = count_watchposts(request.user)

        if vehicles:
            data['vehicles'] = vehicles
        if alerts:
            data['alerts'] = alerts
        if beacons:
            data['beacons'] = beacons
        if watchposts:
            data['watchposts'] = watchposts

    except Exception as e:
        print(e)
        return request(request, 'index.html')

    return render(request, 'index.html', {'data': data})
