from django.contrib import messages
from django.shortcuts import render

from .forms import FormMaquinaInsert
from .models import Maquina, Tipomaquina


def nuevo(request):
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

                return render(request, 'mnuevo.html', {'form': form})
            else:
                messages.error(request, 'La maquina ya existe.')
                messages.error(request, '')
    else:
        form = FormMaquinaInsert()

    return render(request, 'mnuevo.html', {'form': form})