from django.urls import path
from . import views

urlpatterns = [
    path('nuevo', views.nuevo, name='nuevo_producto'),
    #path('lista', views.listar, name='app_listar'),
]

"""
     path('nuevaSala', views.nueva, name='app_altaSala'),
    path('modificarSala', views.modificar, name='app_modificarSala'),
    path('borrarSala', views.borrar, name='app_bajaSala'),
    path('listarSala', views.listar, name='app_listarSalas'),
    path('datosSala', views.datos, name='app_datosSala'),
    """