from django.urls import path
from . import views

urlpatterns = [
    path('nuevo', views.nuevo, name='app_nuevo'),
    path('lista', views.listar, name='app_listar'),
    #path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    #path('<int:pk>/detalle', views.detalle, name='app_detalle'),
    #path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]
"""
 path('nuevoProveedor', views.nuevo, name='app_nuevoProveedor'),
    path('modificarProveedor', views.modificar, name='app_modificarProveedor'),
    path('borrarProveedor', views.borrar, name='app_borrarProveedor'),
    path('listarProveedor', views.listar, name='app_listarProveedores'),
    path('datosProveedor', views.datos, name='app_datosProveedor'),

"""