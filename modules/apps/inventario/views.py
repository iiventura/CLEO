from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from ..horarioEmpleado.views import formatoDateString
from ..producto.views import listaProveedores
from django.contrib.auth.decorators import login_required

@login_required()
def listar(request):

    lista = []

    if request.method == "POST":

        form = FormInventarioFiltro(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            mes = datos.get("mes")
            proveedor = datos.get("proveedor")


            if mes != "0" and proveedor == "0": #solo por mes
                lista = filtroMes(mes)

            elif mes == "0" and proveedor != "0": #solo proveedor
                lista = filtroProveedor(proveedor)

            else:#los dos
                lista = filtroMesProveedor(mes,proveedor)

            return render(request, 'ilista.html', {"lista": lista, "datosMes": meses(), "datosProv": listaProveedores("")})

    else:

        lista = inventarios()

        return render(request, 'ilista.html', {"lista": lista,"datosMes":meses(),"datosProv":listaProveedores("")})

@login_required()
def detalle(request,pk):
    try:
        inve = Inventario.objects.get(id=pk)

        if not inve.fechafin:
            ent = "---"
        else:
            ent = formatoDateString(str(inve.fechafin))

        data = {
            "id": inve.id,
            "cantidad": inve.cantidad,
            "total": inve.coste,
            "fechaini": formatoDateString(str(inve.fechaentrada)),
            "fechafin": ent,
            "estado": inve.pedido.estadopedido.nombre.title(),
            "producto": inve.pedido.producto.nombre.title(),
            "proveedor": inve.pedido.producto.proveedor.nombre.title(),
            "pedido": inve.pedido.id,
        }

    except Inventario.DoesNotExist:
        raise Http404("Inventario no existe")

    return render(request, 'idetalle.html', {"datos": data})

"""
    METODOS AUXILIARES
"""
def meses():

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
             'Octubre', 'Noviembre', 'Diciembre']
    i = 0
    lista = []

    for m in meses:
        data = {
            "id": i+1,
            "nom": m,
        }

        i += 1

        lista.append(data)

    return lista


def inventarios():

    datos = Inventario.objects.all()
    lista = []

    # primer listado sin filtrar
    for inve in datos:

        if not inve.fechafin:
            ent = "---"
        else:
            ent = formatoDateString(str(inve.fechafin))

        data = {
            "id": inve.id,
            "cantidad": inve.cantidad,
            "total": inve.coste,
            "fechaini": formatoDateString(str(inve.fechaentrada)),
            "fechafin": ent,
            "estado": inve.pedido.estadopedido.nombre.title(),
            "producto": inve.pedido.producto.nombre.title(),
            "pedido": inve.pedido.id,
        }

        lista.append(data)

    return lista


def filtroMes(mes):

    datos = Inventario.objects.all()
    lista = []

    for inve in datos:

        mesEn = str(inve.fechaentrada.month)

        if not inve.fechafin:
            mesFi = "0"
            ent = "---"
        else:
            mesFi = str(inve.fechafin.month)
            ent = formatoDateString(str(inve.fechafin))

        if mesEn == mes or mesFi == mes:

            data = {
                "id": inve.id,
                "cantidad": inve.cantidad,
                "total": inve.coste,
                "fechaini": formatoDateString(str(inve.fechaentrada)),
                "fechafin": ent,
                "estado": inve.pedido.estadopedido.nombre.title(),
                "producto": inve.pedido.producto.nombre.title(),
                "pedido": inve.pedido.id,
            }

            lista.append(data)

    return lista


def filtroProveedor(prov):

    #inventario.pedido -> producto.proveedor

    datos = Inventario.objects.all()
    lista = []

    for inve in datos:

        proveedor = str(inve.pedido.producto.proveedor.id)

        if prov == proveedor:

            if not inve.fechafin:
                ent = "---"
            else:
                ent = formatoDateString(str(inve.fechafin))

            if proveedor == prov:

                data = {
                    "id": inve.id,
                    "cantidad": inve.cantidad,
                    "total": inve.coste,
                    "fechaini": formatoDateString(str(inve.fechaentrada)),
                    "fechafin": ent,
                    "estado": inve.pedido.estadopedido.nombre.title(),
                    "producto": inve.pedido.producto.nombre.title(),
                    "pedido": inve.pedido.id,
                }

                lista.append(data)

    return lista


def filtroMesProveedor(mes,prov):

    datos = Inventario.objects.all()
    lista = []

    for inve in datos:

        mesEn = str(inve.fechaentrada.month)

        if not inve.fechafin:
            mesFi = "0"
            ent = "---"
        else:
            mesFi = str(inve.fechafin.month)
            ent = formatoDateString(str(inve.fechafin))

        proveedor = str(inve.pedido.producto.proveedor.id)

        if (mesEn == mes or mesFi == mes) and prov == proveedor:

            data = {
                "id": inve.id,
                "cantidad": inve.cantidad,
                "total": inve.coste,
                "fechaini": formatoDateString(str(inve.fechaentrada)),
                "fechafin": ent,
                "estado": inve.pedido.estadopedido.nombre.title(),
                "producto": inve.pedido.producto.nombre.title(),
                "pedido": inve.pedido.id,
            }

            lista.append(data)

    return lista
