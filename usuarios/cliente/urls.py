from django.urls import path
from usuarios.cliente import views

urlpatterns = [
    path('lista', views.listar, name='app_listar'),
    path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    path('<int:pk>/modificar', views.modificar, name='app_modificar'),
]

