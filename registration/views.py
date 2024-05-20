from django.shortcuts import render, redirect
from .models import RegisteredUsers
from .forms import RegistrationForm
from django.views.generic import DetailView, UpdateView, DeleteView
import re


def sign_in(request):
    error = ''
    users = RegisteredUsers.objects.all()
    print(users)
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
    users = RegisteredUsers.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        email = request.POST.get("email")
        check_email_pre_valid = re.fullmatch(r"^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:["
                                             r"a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*("
                                             r"?:aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi"
                                             r"|museum|name|net|org|pro|tel|travel|[a-z][a-z])$",
                                             email)
        if check_email_pre_valid:
            for el in users:
                if el.email == email:
                    return redirect('home')
            else:
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
