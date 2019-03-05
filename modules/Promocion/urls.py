from django.urls import path
from . import views

urlpatterns = [
    path('nueva', views.nueva, name='app_nueva'),
    path('lista', views.listar, name='app_listar'),
    path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    path('<int:pk>/detalle', views.detalle, name='app_detalle'),
    path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]

