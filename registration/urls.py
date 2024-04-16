from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('/authorization', views.sign_in, name='sign_in'),
    path('/news', views.news_home, name='news')
]
