from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Producto, Tipoproducto
from ..Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages

# Create your views here.
def nueva(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormProductoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            id = datos.get("id")
            nombre = datos.get("nombre")
            tipo = datos.get("Tipo")

            if not Producto.objects.filter(id=id): #todavia se puede guardar una maquina mas
                instTipoProducto = Tipoproducto.objects.get(nombre=tipo)
                p = Producto(id=id,nombre=nombre,tipoproducto=instTipoProducto);
                p.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, 'El producto ya existe.')
                messages.error(request, '')
    else:
        form = FormProductoInsert()

    return render(request, 'alta.html', {'form': form, 'elem':"producto",'cliente': False,
        'encargado': encargado, 'basico': basico})

def borrar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormProductoDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            id = datos.get("Id")

            if Producto.objects.filter(id=id):
                Producto.objects.get(id=id).delete()
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, "El producto no existe.")
    else:
        form = FormProductoDelete()
    return render(request, 'borrar.html', {'form': form, 'elem': "producto",'cliente': False,
        'encargado': encargado, 'basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormProductoUpdate(request.POST)
        id = request.GET.get("Id")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomProd = datos.get("nombre")
            tipo = datos.get("Tipo")

            #se ha modificado el nombre
            antiProd = Producto.objects.get(id=id)
            instTipoProducto = Tipoproducto.objects.get(nombre=tipo)

            # actualizamos datos
            antiProd.nombre = nomProd
            antiProd.tipoproducto = instTipoProducto
            antiProd.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})

    # peticion GET
    formId = FormProductoDelete()
    if 'Id' in request.GET:
        query = request.GET['Id']  # query tiene le valor del dni

        id = str(query)

        if Producto.objects.filter(id=id):
            prod = Producto.objects.get(id=id)

            data = {
                "id": prod.id,
                "nombre": prod.nombre,
                "nomTipoEle": str(prod.tipoproducto.nombre).title(),
            }

            datosTipos = listaTiposProductos(data["nomTipoEle"])

            return render(request, 'modProd.html', {"formId": formId, "buscado": True, "datos": data,
                        "datosTipo":datosTipos, "nomAnt": data["nombre"],'cliente': False,
                        'encargado': encargado, 'basico': basico})
        else:
            messages.error(request, "La maquina no existe.")
            return HttpResponseRedirect("/producto/modificarProducto")

    # primera vista
    formId = FormProductoDelete()
    return render(request, 'modProd.html', {"formId": formId, "buscado": False,
        'cliente': False,'encargado': encargado, 'basico': basico})

def listar(request):

    datosFinales = datosProductos()
    encargado, basico = comprobarSesion(request)
    return render(request, 'listarProductos.html', {"datos": datosFinales,'cliente': False,
        'encargado': encargado, 'basico': basico})

"""
        METODOS AUXILIARES
"""
def datosProductos():

    datos = Producto.objects.all();
    datosFinales = []

    for prod in datos:

        instTipoProducto = Tipoproducto.objects.get(id=prod.tipoproducto.id)

        data = {
            "id": prod.id,
            "nom": prod.nombre,
            "tipo": instTipoProducto.nombre.title(),
        }

        datosFinales.append(data)

    return datosFinales

def listaTiposProductos(nombre):

    tipos = Tipoproducto.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        if nom != nombre:
            lista.append(nom)

    return lista

