"""CLEO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('modules.Index.urls')),
    path('cliente/',include('modules.Cliente.urls')), #cliente
    path('empleado/',include('modules.Empleado.urls')), #empleado
    path('maquina/',include('modules.Maquina.urls')), #maquina
    path('sala/',include('modules.Sala.urls')), #sala
    path('promocion/', include('modules.Promocion.urls')), #promocion
    path('producto/', include('modules.Producto.urls')), #promocion
    path('proveedor/', include('modules.Proveedor.urls')), #promocion

]
