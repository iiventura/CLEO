from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cleo/', include('modules.Main.urls')),
    path('empleado/',include('modules.Empleado.urls')),
    path('sala/',include('modules.Sala.urls')),
    path('maquina/',include('modules.Maquina.urls')),
    #path('tratamiento/',include('modules.Tratamiento.urls')),
    #path('producto/',include('modules.Producto.urls')),
    #path('proveedor/',include('modules.Proveedor.urls')),
    #path('promocion/',include('modules.Promocion.urls')),
    #path('publicidad/',include('modules.Publicidad.urls')),
    #path('cliente/',include('modules.Cliente.urls')),
    #path('notificacion/',include('modules.Notificacion.urls')),
]
