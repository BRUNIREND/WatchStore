from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import RegisteredUsers
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.views.generic import DetailView, UpdateView, DeleteView
import re


# def sign_in(request):
#     error = ''
#     users = RegisteredUsers.objects.all()
#     print(users)
#     if request.method == 'POST':
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         for el in users:
#             if el.email == email and el.password == password:
#                 return redirect('home')
#         else:
#             error = 'Оей, что то не так'
#     form = RegistrationForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'registration/login.html', data)
#
#
# def create(request):
#     error = ''
#     users = RegisteredUsers.objects.all()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         email = request.POST.get("email")
#         check_email_pre_valid = re.fullmatch(r"^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:["
#                                              r"a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*("
#                                              r"?:aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi"
#                                              r"|museum|name|net|org|pro|tel|travel|[a-z][a-z])$",
#                                              email)
#         if check_email_pre_valid:
#             for el in users:
#                 if el.email == email:
#                     return redirect('home')
#             else:
#                 if form.is_valid():
#                     form.save()
#                     return redirect('home')
#                 else:
#                     error = 'Форма была неверной'
#
#     form = RegistrationForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'registration/registration.html', data)
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в акаунт")
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'WStore - Авторизация',
        'form': form
    }
    return render(request, 'registration/login.html', context)


def registration(request):

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user=user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'WStore - Авторизация',
        'form': form
    }
    return render(request, 'registration/registration.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'WStore - Профиль',
        'form': form
    }
    return render(request, 'registration/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('home'))
