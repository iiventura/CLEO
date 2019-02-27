# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Sala
from SILVIA.Revisar.Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages


# Create your views here.
def nueva(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormSalaInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomSala = datos.get("nombre")


            if not Sala.objects.filter(nombre=nomSala): #todavia se puede guardar una maquina mas

                s = Sala(nombre=nomSala)
                s.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
            else:
                messages.error(request, 'La sala ya existe.')
                messages.error(request, '')
    else:
        form = FormSalaInsert()

    return render(request, 'alta.html', {'form': form, 'elem':"sala",'cliente': False,
        'encargado': encargado, 'Basico': basico})

def borrar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormSalaDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nombre = datos.get("nombre")

            if Sala.objects.filter(nombre=nombre):
                Sala.objects.get(nombre=nombre).delete()
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
            else:
                messages.error(request, "La sala no existe.")
    else:
        form = FormSalaDelete()
    return render(request, 'borrar.html', {'form': form, 'elem': "maquina",'cliente': False,
        'encargado': encargado, 'Basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormSalaUpdate(request.POST)
        nombreAnt = request.GET.get("nombre")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomSala = datos.get("nombre")


            if nombreAnt != nomSala: #no se modifica el nombre

                antiSala = Sala.objects.get(nombre=nombreAnt)


                # actualizamos datos
                antiSala.nombre = nomSala
                antiSala.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

    # peticion GET
    formId = FormSalaDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Sala.objects.filter(nombre=nombre):
            sala = Sala.objects.get(nombre=nombre)

            data = {
                "nombre": sala.nombre,
            }


            return render(request, 'modSala.html', {"formId": formId, "buscado": True, "datos": data,
                                                   'cliente': False,'encargado': encargado, 'Basico': basico})
        else:
            messages.error(request, "La sala no existe.")
            return HttpResponseRedirect("/sala/modificarSala")

    # primera vista
    formId = FormSalaDelete()
    return render(request, 'modSala.html', {"formId": formId, "buscado": False,
        'cliente': False,'encargado': encargado, 'Basico': basico})

def datos(request):
    encargado, basico = comprobarSesion(request)
    formId = FormSalaDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Sala.objects.filter(nombre=nombre):
            sala = Sala.objects.get(nombre=nombre)

            data = {
                "nombre": sala.nombre,
            }


            return render(request, 'datosSala.html', {"formId": formId, "buscado": True, "datos": data,
                'cliente': False,'encargado': encargado, 'Basico': basico})
        else:
            messages.error(request, "La sala no existe.")
            return HttpResponseRedirect("/sala/datosSala")

    # primera vista
    formId = FormSalaDelete()
    return render(request, 'datosSala.html', {"formId": formId, "buscado": False,'cliente': False,
            'encargado': encargado, 'Basico': basico})

def listar(request):

    datosFinales = datosSala()
    encargado, basico = comprobarSesion(request)
    return render(request, 'listarSala.html', {"datos": datosFinales,'cliente': False,
        'encargado': encargado, 'Basico': basico})

"""
        METODOS AUXILIARES
"""
def datosSala():

    datos = Sala.objects.all();
    datosFinales = []

    for sal in datos:

        data = {
            "nom": sal.nombre,
        }

        datosFinales.append(data)

    return datosFinales
