from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..Empleado.views import comprobarSesion
from .forms import *
from .models import *
from ..Maquina.models import *
from django.contrib import messages

# Create your views here.
def nuevo(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormTratamientoInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         nomTra = datos.get("nombre")
         fecha = datos.get("descripcion")
         tipo = datos.get("maquina")

         if not Tratamiento.objects.filter(nombre=nomTra):  # todavia se puede guardar una maquina mas
            instMaquina = Maquina.objects.get(id=tipo)
            t = Tratamiento(nombre=nomTra, descripcion=fecha, maquina=instMaquina);
            t.save()

            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, 'El tratamiento ya existe.')
            messages.error(request, '')
   else:
      form = FormTratamientoInsert()

   return render(request, 'alta.html', {'form': form, 'elem': "tratamiento", 'cliente': False,
          'encargado': encargado, 'Basico': basico})

def modificar(request):
   encargado, basico = comprobarSesion(request)

   # si es una peticion post
   if request.method == "POST":
      form = FormTratamientoUpdate(request.POST)
      nomTra = request.GET.get("nombre")  # obtenemos el dni que hemos buscado
      print("*************",nomTra)
      print("*************", form)
      if form.is_valid():
         datos = form.cleaned_data
         print("****************")
         des = datos.get("descripcion")
         maq = datos.get("maquina")

         antiTra = Tratamiento.objects.get(nombre=nomTra)
         instMaquina = Maquina.objects.get(nombre=maq)

         # actualizamos datos
         antiTra.descripcion = des
         antiTra.maquina = instMaquina
         antiTra.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   # peticion GET
   formId = FormTratamientoDelete()
   if 'nombre' in request.GET:
      query = request.GET['nombre']  # query tiene le valor del dni

      nombre = str(query)

      if Tratamiento.objects.filter(nombre=nombre):
         tra = Tratamiento.objects.get(nombre=nombre)

         data = {
            "nombre": tra.nombre,
            "nomMaqEle": str(tra.maquina.nombre).title(),
            "des": tra.descripcion,
         }

         datosMaq = listaMaquinas(data["nomMaqEle"])

         return render(request, 'modTra.html', {"formId": formId, "buscado": True, "datos": data,
                 "datosMaq": datosMaq, 'cliente': False,'encargado': encargado, 'Basico': basico})
      else:
         messages.error(request, "El tratamiento no existe.")
         return HttpResponseRedirect("/tratamiento/modificarTratamiento")

   # primera vista
   formId = FormTratamientoDelete()
   return render(request, 'modTra.html', {"formId": formId, "buscado": False,
         'cliente': False, 'encargado': encargado, 'Basico': basico})

def borrar(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormTratamientoDelete(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         nombre = datos.get("nombre")

         if Tratamiento.objects.filter(nombre=nombre):
            Tratamiento.objects.get(nombre=nombre).delete()
            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, "El tratamiento no existe.")
   else:
      form = FormTratamientoDelete()
   return render(request, 'borrar.html', {'form': form, 'elem': "maquina", 'cliente': False,
         'encargado': encargado, 'Basico': basico})

def listar(request):
   datosFinales = datosTratamientos()
   encargado, basico = comprobarSesion(request)
   return render(request, 'listarTratamientos.html', {"datos": datosFinales, 'cliente': False,
         'encargado': encargado, 'Basico': basico})


"""
        METODOS AUXILIARES
"""
def datosTratamientos():

    datos = Tratamiento.objects.all();
    datosFinales = []

    for maq in datos:

        instMaquina = Maquina.objects.get(id=maq.maquina.id)

        data = {
            "nom": maq.nombre,
            "des": maq.descripcion,
            "maq": instMaquina.nombre.title(),
        }

        datosFinales.append(data)

    return datosFinales


def listaMaquinas(nombre):
   tipos = Maquina.objects.all();
   lista = []

   for tipo in tipos:
      nom = str(tipo.nombre).title();
      if nom != nombre:
         lista.append(nom)

   return lista
