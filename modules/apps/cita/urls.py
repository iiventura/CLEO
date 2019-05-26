from django.urls import path
from . import views

urlpatterns = [
    path('nueva', views.nuevo, name='app_nuevo'),
    path('lista', views.listar, name='app_listar'),
    path('misCitas', views.misCitas, name='app_misCitas'),
    path('<int:pk>/detalle', views.detalle, name='app_detalle'),
    path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]
