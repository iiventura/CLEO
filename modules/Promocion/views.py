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
            nomPro = datos.get("nombre")
            obs = datos.get("observaciones")

            if not Promocion.objects.filter(nombre=nomPro):  # todavia se puede guardar una maquina mas

                s = Promocion(nombre=nomPro, observaciones=obs)
                s.save()
                return render(request, 'pmnuevo.html', {'form': form})
            else:
                messages.error(request, 'La Promocion ya existe.')
                messages.error(request, '')
    else:
        form = FormPromocionInsert()

        return render(request, 'pmnuevo.html', {'form': form})

def listar(request):
   datos = Promocion.objects.all()
   lista = []

   for promocion in datos:

      data = {
         "cod": promocion.codigo,
         "nom": promocion.nombre,
         "obs": promocion.observaciones,
      }

      lista.append(data)

   return render(request, './pmlista.html', {"lista": lista})

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
          "cod": promocion.codigo,
          "nom": promocion.nombre,
          "obs": promocion.observaciones,
       }

   except Promocion.DoesNotExist:
      raise Http404("Promocion no existe")

   return render(request, 'pmdetalle.html', {"datos": data})