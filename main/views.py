from django.shortcuts import render

def index(request):
    data = {
        'title': 'Watch Store',
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    data = {
        'title': 'Contact',
    }
    return render(request, 'main/contact.html', data)

def profile(request):
    return render(request, 'main/profile.html')

