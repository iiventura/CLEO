from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from modules.Maquina.models import Maquina
from .models import Tratamiento
from .forms import FormTratamientoInsert


def nuevo(request):
   if request.method == "POST":
      form = FormTratamientoInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         nomTra = datos.get("nombre")
         fecha = datos.get("descripcion")
         tipo = datos.get("maquina")

         if not Tratamiento.objects.filter(nombre=nomTra):  # todavia se puede guardar una maquina mas
            instMaquina = Maquina.objects.get(id=tipo)
            t = Tratamiento(nombre=nomTra, descripcion=fecha, maquina=instMaquina);
            t.save()
            return HttpResponseRedirect("/tratamiento/lista")

         else:
            messages.error(request, 'El tratamiento ya existe.')
            messages.error(request, '')
   else:
      form = FormTratamientoInsert()

   return render(request, 'tnuevo.html', {'form': form})


def listar(request):
   datos = Tratamiento.objects.all()
   lista = []
   data ={}
   for tratamiento in datos:
      instMaquina = Maquina.objects.get(id=tratamiento.maquina.id)
      data = {
         "id": tratamiento.id,
         "nom": tratamiento.nombre,
         "des": tratamiento.descripcion,
         "maq": instMaquina.nombre.title(),
      }
      lista.append(data)
   return render(request, './tlista.html', {"lista": lista})


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
      tipo = Maquina.objects.get(id=tratamiento.maquina.id)
      data = {
         "id": tratamiento.id,
         "nom": tratamiento.nombre,
         "des": tratamiento.descripcion,
         "maq": tipo.nombre.title(),
      }
   except Tratamiento.DoesNotExist:
      raise Http404("Tratamiento no existe")

   return render(request, 'tdetalle.html', {"datos": data})

