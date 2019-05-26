from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.listar, name='app_listar'),
    path('<int:pk>/detalle', views.detalle, name='app_detalle'),
]
