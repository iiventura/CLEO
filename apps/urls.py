
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleado/',include('modules.Empleado.urls')), #empleado
    path('cliente/',include('modules.Cliente.urls')), #cliente
    path('maquina/',include('modules.Maquina.urls')), #maquina
    path('sala/',include('modules.Sala.urls')), #sala
]
