from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.contrib import messages
from carts.models import Cart
from orders.models import Order, OrderItem
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.views.generic import DetailView, UpdateView, DeleteView
import re
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

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в акаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get('next', None)

                if redirect_page and redirect_page != reverse('home'):
                    return HttpResponseRedirect(request.POST.get('next'))

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
            session_key = request.session.session_key
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
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

    orders = (Order.objects.filter(user=request.user).prefetch_related(Prefetch('orderitem_set', queryset=OrderItem.objects.select_related("product"),)).order_by("-id"))
    context = {
        'title': 'WStore - Профиль',
        'form': form,
        'orders': orders
    }
    return render(request, 'registration/profile.html', context)

def users_cart(request):
    return render(request, 'registration/users_cart.html')

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы успешно вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('home'))


