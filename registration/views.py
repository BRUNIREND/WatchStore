from django.shortcuts import render, redirect
from .models import RegisteredUsers
from .forms import RegistrationForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def sign_up(request):
    return render(request, 'registration/index.html')

def sign_in(request):
    return render(request, 'registration/sign_in.html')

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

    return render(request, 'registration/index.html', data)