from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('doctorRegPage', views.doctorRegPage, name='doctorRegPage'),
    path('doctorRegProcess', views.doctorRegProcess, name='doctorRegProcess'),
]
