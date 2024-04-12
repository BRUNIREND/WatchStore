from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница!!!!!',
        'values': ['Some', 'Hello', '123'],
        'obj':{
            'car':'BMW',
            'age':18,
            'some':'some'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def watch(request):
    return render(request, 'registration/index.html')

def registr(request):
    return render(request, 'registration/registration.html')