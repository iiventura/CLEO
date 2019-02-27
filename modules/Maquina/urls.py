from django.urls import path
from . import views

urlpatterns = [
    path('nuevo', views.nuevo, name='app_nuevo'),
    #path('lista', views.listar, name='app_listar'),
    #path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    #path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]
"""
   path('nuevaMaquina', views.nueva, name='app_nuevaMaquina'),
   path('modificarMaquina', views.modificar, name='app_modificarMaquina'),
   path('borrarMaquina', views.borrar, name='app_borrarMaquina'),
   path('listarMaquinas', views.listar, name='app_listarMaquinas'),
   path('datosMaquina', views.datos, name='app_datosMaquina'),
   """