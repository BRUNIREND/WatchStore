from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:category_slug>/', views.catalog, name='catalog'),
    path('<slug:category_slug>/<int:page>/', views.catalog, name='catalog'),
    path('create/', views.create, name='create'),
    path('product/<slug:product_slug>/', views.product, name='product-detail'),

    # path('product/update/<slug:product_slug>/', views.ProductUpdate, name='product-update'),
    path('product/delete/<slug:product_slug>/', views.ProductDelete, name='product-delete'),

]
