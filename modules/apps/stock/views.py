from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import *
from django.contrib.auth.decorators import login_required

@login_required()
def listar(request):

    stock = Stock.objects.all()
    lista = []

    for fila in stock:
        data = {
            "id": fila.id,
            "total": fila.canttotal,
            "provisional": fila.cantprov,
            "prod": fila.producto.nombre,
            "prov": fila.producto.proveedor.nombre,
        }

        lista.append(data)

    return render(request, 'stlista.html', {"lista": lista})

@login_required()
def detalle(request,pk):

    try:
        stock = Stock.objects.get(id=pk)

        data = {
            "total": stock.canttotal,
            "provisional": stock.cantprov,
            "prod": stock.producto.nombre,
            "prov": stock.producto.proveedor.nombre,
        }

    except Stock.DoesNotExist:
        raise Http404("Error")

    return render(request, 'stdetalle.html', {"datos": data})
