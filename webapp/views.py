from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return render(request, 'home.html')

def camera(request):
    return render(request, 'camera.html')

def predict(request):
    return HttpResponse('not implemented yet')

def favorites(request):
    return ''