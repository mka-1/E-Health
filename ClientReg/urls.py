from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('clientRegPage', views.clientRegPage, name='clientRegPage'),
    path('clientRegProcess', views.clientRegProcess, name='clientRegProcess'),
]
