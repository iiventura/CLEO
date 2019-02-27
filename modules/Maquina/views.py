from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
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



def listar(request):
    datos = Maquina.objects.all()
    lista = []

    for maquina in datos:
        print(maquina.fechaingreso)
        tipoMaquina = Tipomaquina.objects.get(id=maquina.tipomaquina.id)
        data = {
            "id": maquina.id,
            "nom": maquina.nombre,
            "date": maquina.fechaingreso,
            "tipo": tipoMaquina.nombre.title(),
        }
        lista.append(data)

    return render(request, 'mlista.html', {"lista": lista})



def eliminar(request,pk ):
    try:
        maq = Maquina.objects.get(id=pk)
        maq.delete()
    except Maquina.DoesNotExist:
        raise Http404("Sala no existe")

    return HttpResponseRedirect("/maquina/lista")