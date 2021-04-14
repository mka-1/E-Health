from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('i', views.index, name='index'),
    path('', views.home, name='home'),
    path('client', views.client, name='client'),
    path('doctor', views.doctor, name='doctor'),
    path('login', views.login, name='login'),
    path('appt',views.create_view, name='appt'),
    path('list', views.list_view, name='list'),
    path('<id>', views.detail_view, name='detail'),
    path('<id>/update', views.update_view, name='update'),
    path('<id>/delete', views.delete_view, name='delete')
]
