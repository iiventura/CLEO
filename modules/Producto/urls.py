from django.urls import path
from . import views

urlpatterns = [
    path('nuevo', views.nuevo, name='app_nuevo'),
    #path('lista', views.listar, name='app_listar'),
    #path('<int:pk>/eliminar', views.eliminar, name='app_eliminar'),
    #path('<int:pk>/detalle', views.detalle, name='app_detalle'),
    # path('<int:pk>/modificar', views.modificar, name='app_modificar'),

]

"""
    path('nuevoProducto', views.nueva, name='app_nuevoProducto'),
   path('modificarProducto', views.modificar, name='app_modificarProducto'),
   path('borrarProducto', views.borrar, name='app_borrarProducto'),
   path('listarProductos', views.listar, name='app_listarProductos'),
   """