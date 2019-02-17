from django.urls import path
from . import views

urlpatterns = [
    path('loginEmpleado', views.login, name='app_loginEmpleado'),
    path('alta', views.alta, name='app_altaEmpleado'),
    path('baja', views.baja, name='app_bajaEmpleado'),
    path('modificar', views.modificar, name='app_modificarEmpleado'),
    path('listar', views.listar, name='app_listarEmpleados'),
    path('perfil', views.datosEmpleado, name='app_datosEmpleado'),
    path('buscar', views.datosOtrosEmpleado, name='app_datosOtrosEmpleado'),
    path('', views.logout, name='app_logout'),
]
