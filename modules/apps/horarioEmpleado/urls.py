from django.urls import path
from . import views

urlpatterns = [
    path('nuevo', views.nuevo, name='app_nuevo'),
    path('lista', views.listar, name='app_listar'),
    path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    path('<int:pk>/modificar', views.modificar, name='app_modificar'),
    path('miHorario', views.horario, name='app_modificar'),
]
