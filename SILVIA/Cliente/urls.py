from django.urls import path
from . import views

urlpatterns = [
    path('loginCliente', views.login, name='app_loginCliente'),
    path('registro', views.registro, name='app_registro'),
    path('nuevo', views.alta, name='app_altaCliente'),
    path('eliminar', views.baja, name='app_bajaCliente'),
    path('modificar', views.modificar, name='app_modificarCliente'),
    path('listar', views.listar, name='app_listarClientes'),
    path('misdatos', views.datosCliente, name='app_datosCliente'),
    path('datosClienteEmp', views.datosClienteEmp, name='app_datosClienteEmp'),
    path('citasCliente', views.citasCliente, name='app_citasCliente'),
    path('modificarMisDatosCliente', views.modificarMisDatosCliente, name='app_modificarMisDatosCliente'),
]
