from django.contrib import admin

from .models import Empleado, Tipoempleado

admin.site.register(Empleado)
admin.site.register(Tipoempleado)