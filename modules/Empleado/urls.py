from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='app_main'),
    path('nuevo', views.nuevo, name='app_nuevo'),
    path('listar', views.listar, name='app_listar'),


]

"""



urlpatterns = [
    path('loginEmpleado', views.login, name='app_loginEmpleado'),
    
    path('bajaEmpleado', views.baja, name='app_bajaEmpleado'),
    path('modificarEmpleado', views.modificar, name='app_modificarEmpleado'),
    
    path('datosEmpleado', views.datosEmpleado, name='app_datosEmpleado'),
    path('datosOtrosEmpleado', views.datosOtrosEmpleado, name='app_datosOtrosEmpleado'),
    path('', views.logout, name='app_logout'),
]

"""