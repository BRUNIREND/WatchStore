from django.urls import path
from . import views
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

urlpatterns = [
    path('', views.create, name='create'),
    path('authorization', views.sign_in, name='sign_in'),
]
