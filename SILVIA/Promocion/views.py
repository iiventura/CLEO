from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Promocion
from ..Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages

# Create your views here.
def nueva(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormPromocionInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomPro = datos.get("nombre")
            obs = datos.get("observaciones")


            if not Promocion.objects.filter(nombre=nomPro): #todavia se puede guardar una maquina mas

                s = Promocion(nombre=nomPro, observaciones=obs)
                s.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, 'La Promocion ya existe.')
                messages.error(request, '')
    else:
        form = FormPromocionInsert()

    return render(request, 'alta.html', {'form': form, 'elem':"promocion",'cliente': False,
        'encargado': encargado, 'basico': basico})

def borrar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormPromocionDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nombre = datos.get("nombre")

            if Promocion.objects.filter(nombre=nombre):
                Promocion.objects.get(nombre=nombre).delete()
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, "La promocion no existe.")
    else:
        form = FormPromocionDelete()
    return render(request, 'borrar.html', {'form': form, 'elem': "promocion",'cliente': False,
        'encargado': encargado, 'basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormPromocionUpdate(request.POST)
        nombreAnt = request.GET.get("nombre")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            obs = datos.get("observaciones")

            antiPromo= Promocion.objects.get(nombre=nombreAnt)
            antiPromo.observaciones = obs
            antiPromo.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})

    # peticion GET
    formId = FormPromocionDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Promocion.objects.filter(nombre=nombre):
            promo = Promocion.objects.get(nombre=nombre)

            data = {
                "nombre": promo.nombre,
                "obs": promo.observaciones,
            }


            return render(request, 'modPromo.html', {"formId": formId, "buscado": True, "datos": data,
                        'cliente': False,'encargado': encargado, 'basico': basico})
        else:
            messages.error(request, "La promocion no existe.")
            return HttpResponseRedirect("/promocion/modificarPromocion")

    # primera vista
    formId = FormPromocionDelete()
    return render(request, 'modPromo.html', {"formId": formId, "buscado": False,
        'cliente': False,'encargado': encargado, 'basico': basico})

def datos(request):
    encargado, basico = comprobarSesion(request)
    formId = FormPromocionDelete()
    if 'nombre' in request.GET:
        query = request.GET['nombre']  # query tiene le valor del dni

        nombre = str(query)

        if Promocion.objects.filter(nombre=nombre):
            promo = Promocion.objects.get(nombre=nombre)

            data = {
                "nombre": promo.nombre,
                "obs": promo.observaciones,
            }

            return render(request, 'datosPromocion.html', {"formId": formId, "buscado": True, "datos": data,
                'cliente': False,'encargado': encargado, 'basico': basico})
        else:
            messages.error(request, "La sala no existe.")
            return HttpResponseRedirect("/promocion/datosPromocion")

    # primera vista
    formId = FormPromocionDelete()
    return render(request, 'datosPromocion.html', {"formId": formId, "buscado": False,'cliente': False,
            'encargado': encargado, 'basico': basico})

def listar(request):

    datosFinales = datosPromocion()
    encargado, basico = comprobarSesion(request)
    return render(request, 'listarPromociones.html', {"datos": datosFinales,'cliente': False,
        'encargado': encargado, 'basico': basico})

"""
        METODOS AUXILIARES
"""
def datosPromocion():

    datos = Promocion.objects.all();
    datosFinales = []

    for pro in datos:

        data = {
            "nom": pro.nombre,
            "obs": pro.observaciones,
        }

        datosFinales.append(data)

    return datosFinales
