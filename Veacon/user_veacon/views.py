from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm


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
def blank(request):
    return render(request, 'blank.html')
