from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Proveedor
from ..Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages

# Create your views here.
def nuevo(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormProveedorInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomPro = datos.get("nombre")
            con = datos.get("contacto")
            des = datos.get("descripcion")


            if not Proveedor.objects.filter(nombre=nomPro): #todavia se puede guardar una maquina mas

                s = Proveedor(nombre=nomPro, contacto=con, descripcion=des)
                s.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, 'El proveedor ya existe.')
                messages.error(request, '')
    else:
        form = FormProveedorInsert()

    return render(request, 'alta.html', {'form': form, 'elem':"proveedor",'cliente': False,
        'encargado': encargado, 'basico': basico})

def borrar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormProveedorDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nombre = datos.get("nombre")

            if Proveedor.objects.filter(nombre=nombre):
                Proveedor.objects.get(nombre=nombre).delete()
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, "El proveedor no existe.")
    else:
        form = FormProveedorDelete()
    return render(request, 'borrar.html', {'form': form, 'elem': "maquina",'cliente': False,
        'encargado': encargado, 'basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormProveedorUpdate(request.POST)
        nombreAnt = request.GET.get("nombre")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            con = datos.get("contacto")
            desc = datos.get("descripcion")

            antiProv= Proveedor.objects.get(nombre=nombreAnt)
            antiProv.contacto = con
            antiProv.descripcion = desc
            antiProv.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})

    # peticion GET
    formId = FormProveedorDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Proveedor.objects.filter(nombre=nombre):
            pro = Proveedor.objects.get(nombre=nombre)

            data = {
                "nombre": pro.nombre,
                "con": pro.contacto,
                "desc": pro.descripcion,
            }


            return render(request, 'modProv.html', {"formId": formId, "buscado": True, "datos": data,
                        'cliente': False,'encargado': encargado, 'basico': basico})
        else:
            messages.error(request, "La promocion no existe.")
            return HttpResponseRedirect("/proveedor/modificarProveedor")

    # primera vista
    formId = FormProveedorDelete()
    return render(request, 'modProv.html', {"formId": formId, "buscado": False,
        'cliente': False,'encargado': encargado, 'basico': basico})

def datos(request):
    encargado, basico = comprobarSesion(request)
    formId = FormProveedorDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Proveedor.objects.filter(nombre=nombre):
            promo = Proveedor.objects.get(nombre=nombre)

            data = {
                "nombre": promo.nombre,
                "contacto": promo.contacto,
                "desc": promo.descripcion,
            }

            return render(request, 'datosProveedor.html', {"formId": formId, "buscado": True, "datos": data,
                'cliente': False,'encargado': encargado, 'basico': basico})
        else:
            messages.error(request, "La sala no existe.")
            return HttpResponseRedirect("/proveedor/datosProveedor")

    # primera vista
    formId = FormProveedorDelete()
    return render(request, 'datosProveedor.html', {"formId": formId, "buscado": False,'cliente': False,
            'encargado': encargado, 'basico': basico})

def listar(request):

    datosFinales = datosProveedor()
    encargado, basico = comprobarSesion(request)
    return render(request, 'listarProveedores.html', {"datos": datosFinales,'cliente': False,
        'encargado': encargado, 'basico': basico})

"""
        METODOS AUXILIARES
"""
def datosProveedor():

    datos = Proveedor.objects.all();
    datosFinales = []

    for pro in datos:

        data = {
            "nombre": pro.nombre,
            "con": pro.contacto,
            "desc": pro.descripcion,
        }

        datosFinales.append(data)

    return datosFinales
