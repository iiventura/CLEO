from django.contrib import admin

from .models import Producto, TipoProducto

admin.site.register(Producto)
admin.site.register(TipoProducto)

