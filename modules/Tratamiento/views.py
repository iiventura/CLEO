from django.contrib import messages
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
            instMaquina = Maquina.objects.get(nombre=tipo)
            t = Tratamiento(nombre=nomTra, descripcion=fecha, maquina=instMaquina);
            t.save()
            return render(request, 'tnuevo.html', {'form': form})

         else:
            messages.error(request, 'El tratamiento ya existe.')
            messages.error(request, '')
   else:
      form = FormTratamientoInsert()

   return render(request, 'tnuevo.html', {'form': form})
