from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import *
from .models import *
from django.contrib import messages
from django.utils.dateparse import parse_date
from datetime import datetime


def nueva(request):
    if request.method == "POST":
        form = FormPublicidadInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            inicio = datos.get("fechainicio")
            fin = datos.get("fechafin")
            promocion = datos.get("promocion")
            cliente = datos.get("cliente")

            if inicio > fin:
                messages.error(request, "Las fechas no son correctas.")

            else:
                instPromocion = Promocion.objects.get(id=promocion)
                instCliente = Cliente.objects.get(dni=cliente)

                p = Publicidad(fechainicio=inicio, fechafin=fin, promocion=instPromocion, cliente=instCliente);
                p.save()

                return HttpResponseRedirect("/publicidad/lista")
    else:
        form = FormPublicidadInsert()

        return render(request, 'punuevo.html', {'form': form})

def listar(request):
   datos = Publicidad.objects.all()
   lista = []

   for publicidad in datos:

      data = {
         "id": publicidad.id,
         "ini": str(publicidad.fechainicio),
         "fin": str(publicidad.fechafin),
         "prom": publicidad.promocion.codigo,
         "cli": publicidad.cliente.nombre,
      }

      lista.append(data)

   return render(request, './pulista.html', {"lista": lista})

def eliminar(request, pk):
   try:
      promo = Publicidad.objects.get(id=pk)
      promo.delete()
   except Promocion.DoesNotExist:
      raise Http404("Publicidad no existe")

   return HttpResponseRedirect("/publicidad/lista")

def detalle(request, pk):
   try:
       publicidad = Publicidad.objects.get(id=pk)

       data = {
           "id": publicidad.id,
           "ini": str(publicidad.fechainicio),
           "fin": str(publicidad.fechafin),
           "prom": publicidad.promocion.codigo,
           "cli": publicidad.cliente.nombre,
       }

   except Promocion.DoesNotExist:
      raise Http404("Publicidad no existe")

   return render(request, 'pudetalle.html', {"datos": data})

def modificar(request,pk):

    try:
        publicidad = Publicidad.objects.get(id=pk)

        if request.method == "POST":
            form = FormPublicidadUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                inicio = datos.get("fechainicio")
                fin = datos.get("fechafin")
                promocion = datos.get("promocion")
                cliente = datos.get("cliente")

                if inicio > fin:
                    messages.error(request, "Las fechas no son correctas.")

                antiPub = Publicidad.objects.get(id=pk)
                instPromocion = Promocion.objects.get(id=promocion)
                instCliente = Cliente.objects.get(dni=cliente)

                # actualizamos datos
                antiPub.fechainicio = inicio
                antiPub.fechafin = fin
                antiPub.promocion = instPromocion
                antiPub.cliente = instCliente
                antiPub.save()

                return HttpResponseRedirect('/publicidad/' + str(pk) + '/detalle')

            else:
                messages.error(request, "La fechas no son validas.")

        elif request.method == "GET":

            data = {
                "id": publicidad.id,
                "ini": str(publicidad.fechainicio),
                "fin": str(publicidad.fechafin),
                "nomProEle": publicidad.promocion.nombre,
                "idProEle": publicidad.promocion.id,
                "nomCliEle": publicidad.cliente.nombre,
                "idCliEle": publicidad.cliente.id,
            }

            datosPromocion = listaPromociones(data["nomProEle"])
            datosCliente = listaClientes(data["nomCliEle"])

            return render(request, 'pumodificar.html', {"datos": data,"datosPromocion": datosPromocion,
                'datosCliente': datosCliente})

    except Promocion.DoesNotExist:
        raise Http404("Publicidad no existe")

    return HttpResponseRedirect('/publicidad/' + str(pk) + '/modificar')

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