from django.urls import path
from . import views

urlpatterns = [
    path('loginCliente', views.login, name='app_loginCliente'),
    path('registro', views.registro, name='app_registro'),
    path('altaCliente', views.alta, name='app_altaCliente'),
    path('bajaCliente', views.baja, name='app_bajaCliente'),
    path('modificarCliente', views.modificar, name='app_modificarCliente'),
    path('listarClientes', views.listar, name='app_listarClientes'),
    path('datosCliente', views.datosCliente, name='app_datosCliente'),
    path('citasCliente', views.citasCliente, name='app_citasCliente'),
    path('modificarMisDatosCliente', views.modificarMisDatosCliente, name='app_modificarMisDatosCliente'),
]
