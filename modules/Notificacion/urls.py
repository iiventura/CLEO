from django.urls import path
from . import views

urlpatterns = [
    path('nuevaNotificacion', views.nueva, name='app_nuevaNotificacion'),
    path('modificarNotificacion', views.modificar, name='app_modificarNotificacion'),
    path('borrarNotificacion', views.borrar, name='app_borrarNotificacion'),
    path('listarNotificaciones', views.listar, name='app_listarNotificaciones'),
]
