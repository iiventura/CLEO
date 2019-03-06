from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import *
from ..Empleado.models import Tipoempleado
from .forms import *
from django.contrib import messages
from django.utils import timezone


# Create your views here.

def nuevo(request):

    # si es una peticion post
    if request.method == "POST":
        form = FormClienteInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            #recogemos los datos
            dni = datos.get("dni")
            nom = datos.get("nombre")
            ape = datos.get("apellidos")
            dir = datos.get("direccion")
            tlf = datos.get("telefono")
            email = datos.get("email")
            password = datos.get("password")

            #comprobamos dni
            if len(dni) == 9:
                numeros = dni[0:8]
                letra = dni[8:9]

                if not numeros.isdigit() and letra.isalpha():
                    messages.error(request, 'El Dni no es correcto.')
            else:
                messages.error(request, 'El Dni no es correcto.')

            #comprobamos el telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')

            elif not Cliente.objects.filter(dni=dni).exists():
                if not Cliente.objects.filter(email=email).exists():
                    # insertamos cliente
                    c = Cliente(dni=dni, nombre=nom, apellidos=ape, direccion=dir, telefono=tlf, email=email,
                                puntuacion=0, password=password)
                    c.save()

                    return HttpResponseRedirect("/cliente/lista")
                else:
                    messages.error(request, 'El cliente ya existe.')
            else:
                messages.error(request, 'El cliente ya existe.')

    else:
        form = FormClienteInsert()

    #return render(request, 'cnuevo.html', {'form': form})
    return render(request, 'nuevoGeneral.html', {'form': form, 'elem': 'Cliente'})

def listar(request):
    datos = Cliente.objects.all()
    lista = []

    for cli in datos:

        data = {
            "id": cli.id,
            "dni": cli.dni,
            "nom": cli.nombre,
            "ape": cli.apellidos,
            "email": cli.email,
        }
        lista.append(data)

    return render(request,'clista.html',{"lista":lista})

def perfil(request,pk ):
    try:
        cli = Cliente.objects.get(id=pk)

        data = {
            "id": cli.id,
            "dni": cli.dni,
            "nom": cli.nombre,
            "ape": cli.apellidos,
            "dir": cli.direccion,
            "tlf": cli.telefono,
            "email": cli.email,
        }

    except Cliente.DoesNotExist:
        raise Http404("Cliente no existe")

    return render(request, 'cperfil.html', {"datos": data})

def eliminar(request,pk ):
    try:
        cli = Cliente.objects.get(id=pk)
        Cliente.objects.filter(id=cli.id).delete()

    except Cliente.DoesNotExist:
        raise Http404("Cliente no existe")

    return HttpResponseRedirect("/cliente/lista")

def modificar(request,pk ):

    try:
        cli = Cliente.objects.get(id=pk)

        if request.method == 'POST':
            form = FormClienteUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data
                print("****2****")
                #recogemos los datos
                nom = datos.get("nombre")
                ape = datos.get("apellidos")
                email = datos.get("email")
                dir = datos.get("direccion")
                tlf = datos.get("telefono")

                # comprobamos el telefono
                if not (len(tlf) == 9 and tlf.isdigit()):
                    messages.error(request, 'El telefono no es correcto.')
                else:

                    antiClie = Cliente.objects.get(email=email)

                    # actualizamos datos
                    antiClie.nombre = nom
                    antiClie.apellidos = ape
                    antiClie.email = email
                    antiClie.direccion = dir
                    antiClie.telefono = tlf
                    antiClie.save()

                    return HttpResponseRedirect('/cliente/' + str(pk))

        elif request.method == "GET":

            data = {
                "id": cli.id,
                "nom": cli.nombre,
                "ape": cli.apellidos,
                "dir": cli.direccion,
                "tlf": cli.telefono,
                "email": cli.email,
            }

            return render(request, 'cmodificar.html', {"data": data})

    except Cliente.DoesNotExist:
        raise Http404("Cliente no existe")

    return HttpResponseRedirect('/cliente/' + str(pk) + '/modificar')
