from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-cart/', views.users_cart, name='users-cart'),
    path('logout/', views.logout, name='logout'),
]
