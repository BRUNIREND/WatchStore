from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def watch(request):
    return render(request, 'registration/index.html')

def registr(request):
    return render(request, 'registration/registration.html')