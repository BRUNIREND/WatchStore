from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('watch', views.watch),
    path('registration', views.registr)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
