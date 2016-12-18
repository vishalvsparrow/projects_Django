from django.shortcuts import render
from django.http import HttpResponse

def foo(request):
    return render(request,"index.html",{})	

def corey(request):
    return render(request,"second.html",{})
