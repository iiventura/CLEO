from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.Maquina.models import Maquina, Tipomaquina
from apps.Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages
from datetime import datetime
import MySQLdb
import re

# Create your views here.
def nueva(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormMaquinaInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomMaq = datos.get("nombre")
            fecha = datos.get("fechaingreso")
            tipo = datos.get("Tipo")

            if not Maquina.objects.filter(nombre=nomMaq): #todavia se puede guardar una maquina mas
                instTipoMaquina = Tipomaquina.objects.get(nombre=tipo)
                m = Maquina(nombre=nomMaq,fechaingreso=fecha,tipomaquina=instTipoMaquina);
                m.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
            else:
                messages.error(request, 'La maquina ya existe.')
                messages.error(request, '')
    else:
        form = FormMaquinaInsert()

    return render(request, 'alta.html', {'form': form, 'elem':"maquina",'cliente': False,
        'encargado': encargado, 'Basico': basico})

def borrar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormMaquinaDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nombre = datos.get("nombre")

            if Maquina.objects.filter(nombre=nombre):
                Maquina.objects.get(nombre=nombre).delete()
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
            else:
                messages.error(request, "La maquina no existe.")
    else:
        form = FormMaquinaDelete()
    return render(request, 'borrar.html', {'form': form, 'elem': "maquina",'cliente': False,
        'encargado': encargado, 'Basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormMaquinaUpdate(request.POST)
        nombreAnt = request.GET.get("nombre")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomMaq = datos.get("nombre")
            fecha = datos.get("fechaingreso")
            tipo = datos.get("Tipo")

            if nombreAnt == nomMaq: #no se modifica el nombre

                antiMaq = Maquina.objects.get(nombre=nomMaq)
                instTipoMaquina = Tipomaquina.objects.get(nombre=tipo)

                # actualizamos datos
                antiMaq.tipomaquina = instTipoMaquina
                antiMaq.fechaingreso = fecha
                antiMaq.save()

            else: #se ha modificado el nombre
                antiMaq = Maquina.objects.get(nombre=nombreAnt)
                instTipoMaquina = Tipomaquina.objects.get(nombre=tipo)

                # actualizamos datos
                antiMaq.nombre = nomMaq
                antiMaq.tipomaquina = instTipoMaquina
                antiMaq.fechaingreso = fecha
                antiMaq.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

    # peticion GET
    formId = FormMaquinaDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Maquina.objects.filter(nombre=nombre):
            maq = Maquina.objects.get(nombre=nombre)

            data = {
                "nombre": maq.nombre,
                "nomTipoEle": str(maq.tipomaquina.nombre).title(),
                "fecha": maq.fechaingreso,
            }

            datosTipos = listaTiposMaquina(data["nomTipoEle"])

            return render(request, 'modMaq.html', {"formId": formId, "buscado": True, "datos": data,
                        "datosTipo":datosTipos, "nomAnt": data["nombre"],'cliente': False,
                        'encargado': encargado, 'Basico': basico})
        else:
            messages.error(request, "La maquina no existe.")
            return HttpResponseRedirect("/apps/modificarMaquina")

    # primera vista
    formId = FormMaquinaDelete()
    return render(request, 'modMaq.html', {"formId": formId, "buscado": False,
        'cliente': False,'encargado': encargado, 'Basico': basico})

def listar(request):

    datosFinales = datosMaquinas()
    encargado, basico = comprobarSesion(request)
    return render(request, 'listarMaquinas.html', {"datos": datosFinales,'cliente': False,
        'encargado': encargado, 'Basico': basico})

"""
        METODOS AUXILIARES
"""
def datosMaquinas():

    datos = Maquina.objects.all();
    datosFinales = []

    for maq in datos:

        instTipoMaquina = Tipomaquina.objects.get(id=maq.tipomaquina.id)

        data = {
            "nom": maq.nombre,
            "fec": maq.fechaingreso,
            "tipo": instTipoMaquina.nombre.title(),
        }

        datosFinales.append(data)

    return datosFinales

def listaTiposMaquina(nombre):

    tipos = Tipomaquina.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        if nom != nombre:
            lista.append(nom)

    return lista