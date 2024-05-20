from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('create/', views.create, name='create')
]
