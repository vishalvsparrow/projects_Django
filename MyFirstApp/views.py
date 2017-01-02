from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

@login_required(login_url="/login/")
def foo(request):
    return render(request, "index.html", {})


@login_required(login_url="/login/")
def corey(request):
    return render(request, "second.html", {})


def login(request):
    return render(request, auth_views.login, {'template_name': 'registration/login.html'})
