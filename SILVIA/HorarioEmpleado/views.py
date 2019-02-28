from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages
import re
import datetime
import time
import MySQLdb

# Create your views here.
def nuevo(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormHorarioEmpleadoInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         fecha = datos.get("fecha")
         emp = datos.get("empleado")
         entrada = datos.get("horarioentrada")
         salida = datos.get("horariosalida")

         instEmpleado = Empleado.objects.get(dni=emp)
         instEntrada = Horario.objects.get(id=entrada)
         instSalida = Horario.objects.get(id=salida)

         he = Horarioempleado(fecha=fecha, empleado=instEmpleado, horarioentrada=instEntrada, horariosalida=instSalida);
         he.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
   else:
      form = FormHorarioEmpleadoInsert()

   return render(request, 'alta.html', {'form': form, 'elem': "horario", 'cliente': False,
      'encargado': encargado, 'Basico': basico})

def modificar(request):
   encargado, basico = comprobarSesion(request)
   # si es una peticion post
   if request.method == "POST":
      form = FormHorarioEmpleadoUpdate(request.POST)
      emp = request.GET.get("empleado")  # obtenemos el dni que hemos buscado

      if form.is_valid():
         datos = form.cleaned_data
         # recogemos los datos
         entrada = datos.get("horarioentrada")
         salida = datos.get("horariosalida")

         instEmpleado = Empleado.objects.get(dni=emp)
         antiHor = Horarioempleado.objects.get(empleado=instEmpleado)

         # actualizamos datos
         antiHor.horarioentrada = Horario.objects.get(id=entrada)
         antiHor.horariosalida = Horario.objects.get(id=salida)
         antiHor.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   # peticion GET
   formId = FormHorarioEmpleadoDelete()
   if 'empleado' in request.GET:
      query = request.GET['empleado']  # query tiene le valor del dni

      emp = str(query)

      instEmpleado = Empleado.objects.get(dni=emp)
      dato = Horarioempleado.objects.get(empleado=instEmpleado)

      data = {
         "fecha": str(dato.fecha),
         "dni": dato.empleado.dni,
         "nom": dato.empleado.nombre,
         "nomEntradaEle": str(dato.horarioentrada.hora),
         "idEntradaEle": dato.horarioentrada.id,
         "nomSalidaEle": str(dato.horariosalida.hora),
         "idSalidaEle": dato.horariosalida.id,
      }

      datosEntrada = listaHorario(data["nomEntradaEle"])
      datosSalida = listaHorario(data["nomSalidaEle"])

      return render(request, 'modHor.html', {"formId": formId, "buscado": True, "datos": data,
            'datosEntrada':datosEntrada, 'datosSalida':datosSalida,'cliente': False,
            'encargado': encargado, 'Basico': basico,"cnt":0})


   # primera vista
   formId = FormHorarioEmpleadoDelete()
   return render(request, 'modMaq.html', {"formId": formId, "buscado": False,
         'cliente': False, 'encargado': encargado, 'Basico': basico})

def borrar(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormHorarioEmpleadoDelete(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         emp = datos.get("empleado")
         instEmpleado = Empleado.objects.get(dni=emp)

         if Horarioempleado.objects.filter(empleado=instEmpleado):
            Horarioempleado.objects.get(empleado=instEmpleado).delete()
            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, "No hay horario para este empleado.")
   else:
      form = FormHorarioEmpleadoDelete()
   return render(request, 'borrar.html', {'form': form, 'elem': "maquina", 'cliente': False,
            'encargado': encargado, 'Basico': basico})

def listar(request):
   datosFinales = datosHorario()
   encargado, basico = comprobarSesion(request)
   return render(request, 'listarHorarios.html', {"datos": datosFinales, 'cliente': False,
         'encargado': encargado, 'Basico': basico})

"""
        METODOS AUXILIARES
"""
def datosHorario():

    datos = Horarioempleado.objects.all();
    datosFinales = []

    for dato in datos:
        data = {
            "fecha": str(dato.fecha),
            "emp": dato.empleado.nombre,
            "he": dato.horarioentrada.hora,
            "hs": dato.horariosalida.hora,
        }

        datosFinales.append(data)

    return datosFinales


def listaHorario(hora):
   tipos = Horario.objects.all();

   resultado = []
   for tipo in tipos:
      if hora != str(tipo.hora):

         data = {
            "id": tipo.id,
            "hora": str(tipo.hora),
         }

         resultado.append(data)

   return resultado