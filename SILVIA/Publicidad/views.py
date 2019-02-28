from django.shortcuts import render
from django.http import HttpResponseRedirect
from modules.Empleado.views import comprobarSesion
from .forms import *
from .models import *
from django.contrib import messages
from django.utils.dateparse import parse_date
from datetime import datetime

# Create your views here.
def nueva(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormPublicidadInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         inicio = datos.get("fechainicio")
         fin = datos.get("fechafin")
         promocion = datos.get("promocion")
         cliente = datos.get("cliente")

         if(inicio > fin):
            messages.error(request, "Las fechas no son correctas.")

         else:
            instPromocion = Promocion.objects.get(id=promocion)
            instCliente = Cliente.objects.get(dni=cliente)

            p = Publicidad(fechainicio=inicio, fechafin=fin, promocion=instPromocion, cliente=instCliente );
            #p.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   else:
      form = FormPublicidadInsert()

   return render(request, 'alta.html', {'form': form, 'elem': "publicidad", 'cliente': False,
         'encargado': encargado, 'Basico': basico})

def modificar(request):
   encargado, basico = comprobarSesion(request)
   # si es una peticion post
   if request.method == "POST":
      form = FormPublicidadUpdate(request.POST)
      id = request.GET.get("id")  # obtenemos el dni que hemos buscado

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         inicio = datos.get("fechainicio")
         fin = datos.get("fechafin")
         promocion = datos.get("promocion")
         cliente = datos.get("cliente")

         if (inicio > fin):
            messages.error(request, "Las fechas no son correctas.")
         else:
            antiPub = Publicidad.objects.get(id=id)
            instPromocion = Promocion.objects.get(id=promocion)
            instCliente = Cliente.objects.get(dni=cliente)



            # actualizamos datos
            antiPub.fechainicio = inicio
            antiPub.fechafin = fin
            antiPub.promocion = instPromocion
            antiPub.cliente = instCliente
            antiPub.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   # peticion GET
   formId = FormPublicidadDelete()
   if 'id' in request.GET:
      query = request.GET['id']  #query tiene le valor del dni

      id = str(query)

      if Publicidad.objects.filter(id=id):
         pub = Publicidad.objects.get(id=id)

         data = {
            "ini": str(pub.fechainicio),
            "fin": str(pub.fechafin),
            "nomProEle": pub.promocion.nombre,
            "idProEle": pub.promocion.id,
            "nomCliEle": pub.cliente.nombre,
            "dniCliEle": pub.cliente.dni,
         }

         datosPromocion = listaPromociones(data["nomProEle"])
         datosCliente = listaClientes(data["nomCliEle"])

         return render(request, 'modPub.html', {"formId": formId, "buscado": True, "datos": data,
               "datosPromocion": datosPromocion, 'datosCliente': datosCliente,'cliente': False,
               'encargado': encargado, 'Basico': basico})
      else:
         messages.error(request, "La publicidad no existe.")
         return HttpResponseRedirect("/publicidad/modificarPublicidad")

   # primera vista
   formId = FormPublicidadDelete()
   return render(request, 'modPub.html', {"formId": formId, "buscado": False,
         'cliente': False, 'encargado': encargado, 'Basico': basico})

def borrar(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormPublicidadDelete(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         id = datos.get("id")

         if Publicidad.objects.filter(id=id):
            Publicidad.objects.get(id=id).delete()
            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, "La publicidad no existe.")
   else:
      form = FormPublicidadDelete()
   return render(request, 'borrar.html', {'form': form, 'elem': "publicidad", 'cliente': False,
         'encargado': encargado, 'Basico': basico})

def listar(request):
   datosFinales = datosPublicidad()
   encargado, basico = comprobarSesion(request)
   return render(request, 'listarPublicidad.html', {"datos": datosFinales, 'cliente': False,
         'encargado': encargado, 'Basico': basico})


"""
        METODOS AUXILIARES
"""
def datosPublicidad():
   datos = Publicidad.objects.all();
   datosFinales = []

   for pub in datos:
      instPromocion = Promocion.objects.get(id=pub.promocion.id)
      instCliente = Cliente.objects.get(dni=pub.cliente.dni)

      data = {
         "id": pub.id,
         "ini": str(pub.fechainicio),
         "fin": str(pub.fechafin),
         "pro": instPromocion.nombre,
         "cli": instCliente.nombre,
      }

      datosFinales.append(data)

   return datosFinales


def listaPromociones(nombre):
   tipos = Promocion.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista


def listaClientes(nombre):
   tipos = Cliente.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "dni": tipo.dni,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista