from django.urls import path
from . import views

urlpatterns = [
    path('nuevoProducto', views.nueva, name='app_nuevoProducto'),
    path('modificarProducto', views.modificar, name='app_modificarProducto'),
    path('borrarProducto', views.borrar, name='app_borrarProducto'),
    path('listarProductos', views.listar, name='app_listarProductos'),
]
