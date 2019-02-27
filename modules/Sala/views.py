from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms import FormSalaInsert
from .models import Sala
from django.contrib import messages


def nuevo(request):
    if request.method == "POST":
        form = FormSalaInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomSala = datos.get("nombre")

            if not Sala.objects.filter(nombre=nomSala):  # todavia se puede guardar una maquina mas

                s = Sala(nombre=nomSala)
                s.save()

                return render(request, 'snuevo.html', {'form': form})
            else:
                messages.error(request, 'La sala ya existe.')
                messages.error(request, '')
    else:
        form = FormSalaInsert()

    return render(request, 'snuevo.html', {'form': form})



def listar(request):
    datos = Sala.objects.all()
    lista = []

    for sala in datos:
        data={
           "id": sala.id,
            "nom": sala.nombre,
        }
        lista.append(data)
    return render(request,'./slista.html',{"lista":lista})



def eliminar(request,pk ):
    try:
        sala = Sala.objects.get(id=pk)
        sala.delete()
    except Sala.DoesNotExist:
        raise Http404("Sala no existe")

    return HttpResponseRedirect("/sala/lista")
