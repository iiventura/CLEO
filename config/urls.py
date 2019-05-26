
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    #path('horario/', include('modules.apps.horarioEmpleado.urls')),
    path('maquina/', include('modules.apps.maquina.urls')),
    path('sala/', include('modules.apps.sala.urls')),
    #path('promocion/', include('modules.apps.promocion.urls')),
    #path('publicidad/', include('modules.apps.publicidad.urls')),
    #path('notificacion/', include('modules.apps.notificacion.urls')),
    path('proveedor/', include('modules.apps.proveedor.urls')),
    path('producto/', include('modules.apps.producto.urls')),
    path('stock/', include('modules.apps.stock.urls')),
    path('pedido/', include('modules.apps.pedido.urls')),
    path('inventario/', include('modules.apps.inventario.urls')),
    path('tratamiento/', include('modules.apps.tratamiento.urls')),
    #path('cita/', include('modules.apps.cita.urls')),
    #path('factura/', include('modules.apps.factura.urls')),
]
