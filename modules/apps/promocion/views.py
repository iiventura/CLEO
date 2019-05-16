from django.core.checks import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import Promocion
from django.contrib.auth.decorators import login_required

@login_required()
def nueva(request):
    if request.method == "POST":
        form = FormPromocionInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            codigo = datos.get("codigo")
            nomPro = datos.get("nombre")
            obs = datos.get("observaciones")
            des = datos.get("descuento")

            if not Promocion.objects.filter(nombre=nomPro):  # todavia se puede guardar una maquina mas

                s = Promocion(codigo=codigo, nombre=nomPro, observaciones=obs,descuento=des)
                s.save()
                return HttpResponseRedirect("/promocion/lista")
            else:
                messages.error(request, 'La Promocion ya existe.')
                messages.error(request, '')
    else:
        form = FormPromocionInsert()

    return render(request, 'promnueva.html', {'form': form, 'elem': 'Añadir', 'titulo':'Añadir Promocion'})

@login_required()
def listar(request):
   datos = Promocion.objects.all()
   lista = []

   for promocion in datos:

      data = {
         "id": promocion.id,
         "cod": promocion.codigo,
         "nom": promocion.nombre,
         "obs": promocion.observaciones,
         "des": promocion.descuento,
      }

      lista.append(data)

   return render(request, './prmlista.html', {"lista": lista})

@login_required()
def eliminar(request, pk):
   try:
      promo = Promocion.objects.get(id=pk)
      promo.delete()
   except Promocion.DoesNotExist:
      raise Http404("Promocion no existe")

   return HttpResponseRedirect("/promocion/lista")

@login_required()
def detalle(request, pk):
   try:
       promocion = Promocion.objects.get(id=pk)

       data = {
          "id": promocion.id,
          "cod": promocion.codigo,
          "nom": promocion.nombre,
          "obs": promocion.observaciones,
          "des": promocion.descuento,
       }

   except Promocion.DoesNotExist:
      raise Http404("Promocion no existe")

   return render(request, 'prmdetalle.html', {"datos": data})

@login_required()
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
                des = datos.get("descuento")

                antiPromo = Promocion.objects.get(id=pk)
                antiPromo.nombre = nom
                antiPromo.observaciones = obs
                antiPromo.descuento = des
                antiPromo.save()

                return HttpResponseRedirect("/promocion/lista")

        elif request.method == "GET":

            data = {
                "cod": prom.codigo,
                "nom": prom.nombre,
                "obs": prom.observaciones,
                "des": prom.descuento,
            }

            return render(request, 'prmmodificar.html', {"datos": data})

    except Promocion.DoesNotExist:
        raise Http404("Promocion no existe")

    return HttpResponseRedirect('/promocion/' + str(pk) + '/modificar')
