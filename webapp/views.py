from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def camera(request):
    return render(request, 'camera.html')

def favorites(request):
    return ''