from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='app_main'),
    path('nuevo', views.nuevo, name='app_nuevo'),
    path('lista', views.listar, name='app_listar'),
    path('<int:pk>', views.perfil, name='app_perfil'),
    path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    #path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]

"""



urlpatterns = [
    path('loginEmpleado', views.login, name='app_loginEmpleado'),
    path('', views.logout, name='app_logout'),
    
    path('bajaEmpleado', views.baja, name='app_bajaEmpleado'),
    path('modificarEmpleado', views.modificar, name='app_modificarEmpleado'),
    
    path('datosEmpleado', views.datosEmpleado, name='app_datosEmpleado'),
    
    
]

"""