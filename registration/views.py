from django.shortcuts import render, redirect
from .models import RegisteredUsers
from .forms import RegistrationForm
from django.views.generic import DetailView, UpdateView, DeleteView


def sign_up(request):
    return render(request, 'registration/sign_up.html')


def sign_in(request):
    error = ''
    users = RegisteredUsers.objects.all()
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        for el in users:
            if el.email == email and el.password == password:
                return redirect('home')
        else:
            error = 'Оей, что то не так'
    form = RegistrationForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/sign_in.html', data)

def create(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = RegistrationForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'registration/sign_up.html', data)