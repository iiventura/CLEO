from django.contrib import admin

from .models import Empleado, TipoEmpleado

admin.site.register(Empleado)
admin.site.register(TipoEmpleado)