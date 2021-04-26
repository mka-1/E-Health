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
    path('appt/check', views.checkdr, name="check appointments"),
    path('appt/admin', views.list_view_admin, name= 'database appointments'),
    path('appt/<id>', views.detail_view, name='detail'),
    path('appt/<id>/update', views.update_view, name='update'),
    path('appt/<id>/delete', views.delete_view, name='delete'),
    path('adminportal', views.adminportal, name= 'Admin Portal'),
    path('adminportal/d', views.admin_d, name= 'database doctor'),
    path('adminportal/d/create', views.create_view_dr, name='new entry dr')
    #path('adminportal/p', views.admin_p, name= 'database patient'),

]
