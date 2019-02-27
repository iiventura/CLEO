from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cleo/', include('modules.Main.urls')),
    path('empleado/',include('modules.Empleado.urls')),
    path('sala/',include('modules.Sala.urls')),
    path('maquina/',include('modules.Maquina.urls')),
]
"""
  path('cliente/',include('modules.Cliente.urls')), #cliente
  path('maquina/',include('modules.Maquina.urls')), #maquina
  path('promocion/', include('modules.Promocion.urls')), #promocion
  path('producto/', include('modules.Producto.urls')), #promocion
  path('proveedor/', include('modules.Proveedor.urls')), #promocion

"""