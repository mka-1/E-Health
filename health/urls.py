from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('oldUIhomepage', views.home, name='homeoldUI'),
    path('client', views.client, name='client'),
    path('doctor', views.doctor, name='doctor'),
    path('login', views.login, name='login'),
    path('appt/create',views.create_view, name='appt'),
    path('appt', views.list_view, name='list'),
    path('appt/admin',views.list_view_admin, name='adminlist'),
    path('appt/<id>', views.detail_view, name='detail'),
    path('appt/<id>/update', views.update_view, name='update'),
    path('appt/<id>/delete', views.delete_view, name='delete')
]
