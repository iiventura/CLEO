from django.core.checks import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import Promocion


def nueva(request):
    if request.method == "POST":
        form = FormPromocionInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            codigo = datos.get("codigo")
            nomPro = datos.get("nombre")
            obs = datos.get("observaciones")

            if not Promocion.objects.filter(nombre=nomPro):  # todavia se puede guardar una maquina mas

                s = Promocion(codigo=codigo, nombre=nomPro, observaciones=obs)
                s.save()
                return HttpResponseRedirect("/promocion/lista")
            else:
                messages.error(request, 'La Promocion ya existe.')
                messages.error(request, '')
    else:
        form = FormPromocionInsert()

    return render(request, 'nuevoGeneral.html', {'form': form, 'elem': 'Añadir', 'titulo':'Añadir Promocion'})

def listar(request):
   datos = Promocion.objects.all()
   lista = []

   for promocion in datos:

      data = {
         "id": promocion.id,
         "cod": promocion.codigo,
         "nom": promocion.nombre,
         "obs": promocion.observaciones,
      }

      lista.append(data)

   return render(request, './prmlista.html', {"lista": lista})

def eliminar(request, pk):
   try:
      promo = Promocion.objects.get(id=pk)
      promo.delete()
   except Promocion.DoesNotExist:
      raise Http404("Promocion no existe")

   return HttpResponseRedirect("/promocion/lista")

def detalle(request, pk):
   try:
       promocion = Promocion.objects.get(id=pk)

       data = {
          "id": promocion.id,
          "cod": promocion.codigo,
          "nom": promocion.nombre,
          "obs": promocion.observaciones,
       }

   except Promocion.DoesNotExist:
      raise Http404("Promocion no existe")

   return render(request, 'prmdetalle.html', {"datos": data})

def modificar(request,pk):

    try:
        prom = Promocion.objects.get(id=pk)

        if request.method == "POST":
            form = FormPromocionUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                nom = datos.get("nombre")
                obs = datos.get("observaciones")

                antiPromo = Promocion.objects.get(id=pk)
                antiPromo.nombre = nom
                antiPromo.observaciones = obs
                antiPromo.save()

                return HttpResponseRedirect("/promocion/lista")

        elif request.method == "GET":

            data = {
                "cod": prom.codigo,
                "nom": prom.nombre,
                "obs": prom.observaciones,
            }

            return render(request, 'prmmodificar.html', {"datos": data})

    except Promocion.DoesNotExist:
        raise Http404("Promocion no existe")

    return HttpResponseRedirect('/promocion/' + str(pk) + '/modificar')
