from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('oldUIhomepage', views.home, name='homeoldUI'),
    path('client', views.client, name='client'),
    path('doctor', views.doctor, name='doctor'),
    path('login', views.login, name='login'),
    path('loginDr', views.loginDr, name='loginDr'),
    path('drfinder', views.drfinder, name='doctor finder'),
    path('aboutus',views.aboutus, name='About us'),
    path('appt', views.list_view, name='list'),
    path('appt/check', views.checkdr, name="check appointments"),
    path('appt/create', views.create_view, name='appt'),
    path('appt/<id>/update', views.update_view, name='update'),
    path('appt/<id>/delete', views.delete_view, name='delete'),
    path('appt/<id>/approve', views.approve_view_dr, name='update entry dr'),
    path('adminportal', views.adminportal, name='Admin Portal'),
    path('adminportal/d', views.admin_d, name='database doctor'),
    path('adminportal/d/create', views.create_view_dr, name='new entry dr'),
    path('adminportal/d/<id>/delete', views.delete_view_dr, name='delete entry dr'),
    path('adminportal/d/<id>/update', views.update_view_dr, name='update entry dr'),
    path('adminportal/p', views.admin_p, name='database patient'),
    path('adminportal/p/create', views.create_view_pt, name='new entry patient'),
    path('adminportal/p/<id>/update', views.update_view_pt, name='update entry patient'),
    path('adminportal/p/<id>/delete', views.delete_view_pt, name='delete entry patient'),
    path('adminportal/a', views.list_view_admin, name='database appointments'),
    path('adminportal/a/create', views.create_view_admin, name='Create appt entry'),
    path('adminportal/a/submit', views.submitquery, name='Create appt entry'),
    path('adminportal/a/<id>/update', views.update_view_admin, name='update entry patient'),
    path('adminportal/a/<id>/delete', views.delete_view_admin, name='update entry patient')


]
