from django.urls import path
from . import views
urlpatterns = [
    path('loginEmpleado', views.login, name='app_loginEmpleado'),
    path('altaEmpleado', views.alta, name='app_altaEmpleado'),
    path('bajaEmpleado', views.baja, name='app_bajaEmpleado'),
    path('modificarEmpleado', views.modificar, name='app_modificarEmpleado'),
    path('listarEmpleados', views.listar, name='app_listarEmpleados'),
    path('datosEmpleado', views.datosEmpleado, name='app_datosEmpleado'),
    path('datosOtrosEmpleado', views.datosOtrosEmpleado, name='app_datosOtrosEmpleado'),
    path('', views.logout, name='app_logout'),
]
