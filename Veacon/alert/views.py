from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .manage_data import get_alerts


@login_required(login_url='/login/')
def alerts(request):
    alert_list = get_alerts(request.user)
    return render(request, 'alerts.html', {'alerts': alert_list})
