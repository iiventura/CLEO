from django.urls import path
from . import views

urlpatterns = [
    path('nuevaPromocion', views.nueva, name='app_nuevaPromocion'),
    path('modificarPromocion', views.modificar, name='app_modificarPromocion'),
    path('borrarPromocion', views.borrar, name='app_borrarPromocion'),
    path('listarPromocion', views.listar, name='app_listarPromociones'),
    path('datosPromocion', views.datos, name='app_datosPromocion'),
]
