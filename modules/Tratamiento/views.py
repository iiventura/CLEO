from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Maquina, Producto, Tratamiento
from .forms import *


def nuevo(request):
   if request.method == "POST":
      form = FormTratamientoInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         nomTra = datos.get("nombre")
         desc = datos.get("descripcion")
         tipo = datos.get("maquina")
         prod = datos.get("producto")

         if not Tratamiento.objects.filter(nombre=nomTra):  # todavia se puede guardar una maquina mas
            instMaquina = Maquina.objects.get(id=tipo)
            instProducto = Producto.objects.get(id=prod)
            t = Tratamiento(nombre=nomTra, descripcion=desc, maquina=instMaquina, producto=instProducto);
            t.save()
            return HttpResponseRedirect("/tratamiento/lista")

         else:
            messages.error(request, 'El tratamiento ya existe.')
            messages.error(request, '')
   else:
      form = FormTratamientoInsert()
      datosMaquina = listaMaquinas("Selecciona")
      datosProducto = listaProducto(" ")

   return render(request, 'tnuevo.html', {"datosMaquina": datosMaquina, 'datosProducto': datosProducto})


def listar(request):
   datos = Tratamiento.objects.all()
   lista = []

   for tratamiento in datos:
      instMaquina = Maquina.objects.get(id=tratamiento.maquina.id)
      instProducto = Producto.objects.get(id=tratamiento.producto.id)

      data = {
         "id": tratamiento.id,
         "nom": tratamiento.nombre,
         "maq": instMaquina.nombre.title(),
         "pro": instProducto.nombre.title(),
      }
      lista.append(data)

   return render(request, './tlista.html', {"lista": lista})


def modificar(request, pk):
   try:
      tratamiento = Tratamiento.objects.get(id=pk)

      if request.method == "POST":
         form = FormTratamientoUpdate(request.POST)

         if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomTra = datos.get("nombre")
            desc = datos.get("descripcion")
            tipo = datos.get("maquina")
            prod = datos.get("producto")

            antiPub = Tratamiento.objects.get(id=pk)
            instMaquina = Maquina.objects.get(id=tipo)
            instProducto = Producto.objects.get(id=prod)

            # actualizamos datos
            antiPub.nombre = nomTra
            antiPub.descripcion = desc
            antiPub.maquina = instMaquina
            antiPub.producto = instProducto
            antiPub.save()

            return HttpResponseRedirect("/tratamiento/lista")

      elif request.method == "GET":

         data = {
            "id": tratamiento.id,
            "nom": tratamiento.nombre,
            "des": tratamiento.descripcion,
            "nomMaqEle": tratamiento.maquina.nombre,
            "idMaqEle": tratamiento.maquina.id,
            "nomProEle": tratamiento.producto.nombre,
            "idProEle": tratamiento.producto.id,
         }


         datosMaquina = listaMaquinas(data["nomMaqEle"])
         datosProducto= listaProducto(data["nomProEle"])

         return render(request, 'tmodificar.html', {"datos": data, "datosMaquina": datosMaquina,
               'datosProducto': datosProducto})

   except Tratamiento.DoesNotExist:
      raise Http404("Tratamiento no existe")

   return HttpResponseRedirect('/tratamiento/' + str(pk) + '/modificar')

def eliminar(request, pk):
   try:
      sala = Tratamiento.objects.get(id=pk)
      sala.delete()
   except Tratamiento.DoesNotExist:
      raise Http404("Tratamiento no existe")

   return HttpResponseRedirect("/tratamiento/lista")


def detalle(request, pk):
   try:
      tratamiento = Tratamiento.objects.get(id=pk)
      maquina = Maquina.objects.get(id=tratamiento.maquina.id)
      producto = Producto.objects.get(id=tratamiento.producto.id)

      data = {
         "id": tratamiento.id,
         "nom": tratamiento.nombre,
         "des": tratamiento.descripcion,
         "maq": maquina.nombre.title(),
         "tipomaquina": maquina.tipomaquina.nombre,
         "pro": producto.nombre.title(),
         "tipoproducto":producto.tipoproducto.nombre
      }
   except Tratamiento.DoesNotExist:
      raise Http404("Tratamiento no existe")

   return render(request, 'tdetalle.html', {"datos": data})


def listaMaquinas(nombre):
   tipos = Maquina.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista

def listaProducto(nombre):
   tipos = Producto.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "dni": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista