from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('i', views.index, name='index'),
    path('', views.home, name='home'),
    path('client', views.client, name='client'),
    path('doctor', views.doctor, name='doctor'),
    path('login', views.login, name='login')
]
