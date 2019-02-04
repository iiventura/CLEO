from django.urls import path
from . import views

urlpatterns = [
    path('loginCliente', views.login, name='app_login'),
    path('registro', views.registro, name='app_registro'),
    path('bajaCliente', views.baja, name='app_bajaCliente'),
    path('modificarCliente', views.modificar, name='app_modificarCliente'),
    path('listarClientes', views.listar, name='app_listarClientes'),
    path('', views.logout, name='app_logout'),
]
