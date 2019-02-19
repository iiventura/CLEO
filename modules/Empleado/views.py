from django.shortcuts import render
from .models import Empleado, Tipoempleado
from .forms import *
from django.contrib import messages
from django.utils import timezone


def main(request):
    return render(request, 'index.html')


def nuevo(request):
    if request.method == "POST":
        form = FormEmpleadoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")
            cod = datos.get("codigo")
            nom = datos.get("nombre")
            ape = datos.get("apellidos")
            email = datos.get("email")
            dir = datos.get("direccion")
            tlf = datos.get("telefono")
            tipo = datos.get("Tipo")
            password = datos.get("password")

            # comprobamos dni
            if len(dni) == 9:
                numeros = dni[0:8]
                letra = dni[8:9]

                if not numeros.isdigit() and letra.isalpha():
                    messages.error(request, 'El Dni no es correcto.')
            else:
                messages.error(request, 'El Dni no es correcto.')

            # comprobamso telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')
                messages.error(request, '')

            elif not Empleado.objects.filter(dni=dni).exists():
                if not Empleado.objects.filter(email=email).exists():  # comprobamos si ya existe ese empleado

                    instTipoEmpleado = Tipoempleado.objects.get(nombre=tipo)

                    e = Empleado(dni=dni, codigo=cod, nombre=nom, apellidos=ape, email=email,
                                 direccion=dir, telefono=tlf, tipoempleado=instTipoEmpleado, password=password)
                    e.save()

                    return render(request, 'nuevo.html', {'form': form})
                else:
                    messages.error(request, 'El empleado ya existe.')
            else:
                messages.error(request, 'El empleado ya existe.')

    else:
        form = FormEmpleadoInsert()
        return render(request, 'nuevo.html', {'form': form})
