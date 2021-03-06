from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from usuarios.models import Cliente, CustomUser


@login_required()
def listar(request):
    datos = Cliente.objects.all()
    lista = []

    for cliente in datos:
        user = CustomUser.objects.get(cliente=cliente)

        data={
            "id": user.id,
            "nom": user.first_name,
            "ape": user.last_name,
            "email": user.email,
        }

        lista.append(data)
    lista=sorted(lista, key=lambda i: (i['nom'], i['ape']))
    return render(request,'cliente/lista.html',{"lista":lista})

@login_required()
def eliminar(request, pk):
    try:
        Cliente.objects.filter(user_id=pk).delete()
        CustomUser.objects.filter(id=pk).delete()

    except Cliente.DoesNotExist or CustomUser.DoesNotExist:
        raise Http404("Cliente no existe")

    return HttpResponseRedirect("/cliente/lista")

@login_required()
def modificar(request):
    pass