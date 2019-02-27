from django.urls import path
from . import views

urlpatterns = [
    path('nuevaPublicidad', views.nueva, name='app_nuevaPublicidad'),
    path('modificarPublicidad', views.modificar, name='app_modificarPublicidad'),
    path('borrarPublicidad', views.borrar, name='app_borrarPublicidad'),
    path('listarPublicidad', views.listar, name='app_listarPublicidad'),
]
