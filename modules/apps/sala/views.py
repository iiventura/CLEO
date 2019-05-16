from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms import FormSalaInsert, FormSalaUpdate
from .models import Sala
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
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

                return HttpResponseRedirect("/sala/lista")
            else:
                messages.error(request, 'La sala ya existe.')
                messages.error(request, '')
    else:
        form = FormSalaInsert()

    return render(request, 'snuevo.html', {'form': form})

@login_required()
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

@login_required()
def eliminar(request,pk ):
    try:
        sala = Sala.objects.get(id=pk)
        sala.delete()
    except Sala.DoesNotExist:
        raise Http404("Sala no existe")

    return HttpResponseRedirect("/sala/lista")

@login_required()
def modificar(request,pk ):
    try:
        sala = Sala.objects.get(id=pk)

        if request.method == "POST":
            form = FormSalaUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                nom = datos.get("nombre")

                # actualizamos datos
                sala.nombre = nom
                sala.save()

                return HttpResponseRedirect("/sala/lista")

        elif request.method == "GET":

            data = {
                "nom": sala.nombre,
            }

            return render(request, 'smodificar.html', {"datos": data,})

    except Sala.DoesNotExist:
        raise Http404("Empleado no existe")

    return HttpResponseRedirect('/sala/' + str(pk) + '/modificar')