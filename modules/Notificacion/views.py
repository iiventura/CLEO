from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..Empleado.views import comprobarSesion
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def nueva(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormNotificacionInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         estado = datos.get("Estado")
         usuario = datos.get("Usuario")
         mensaje = datos.get("mensaje")

         instEstado = Estadomensaje.objects.get(id=estado)
         instUsuario = Tipousuario.objects.get(id=usuario)

         n = Notificacion(estadomensaje=instEstado, tipousuario=instUsuario, mensaje=mensaje);
         n.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   else:
      form = FormNotificacionInsert()

   return render(request, 'alta.html', {'form': form, 'elem': "notificacion", 'cliente': False,
         'encargado': encargado, 'Basico': basico})

def modificar(request):
   encargado, basico = comprobarSesion(request)
   # si es una peticion post
   if request.method == "POST":
      form = FormNotificacionUpdate(request.POST)
      id = request.GET.get("id")  # obtenemos el dni que hemos buscado

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         estado = datos.get("Estado")
         usuario = datos.get("Usuario")
         mensaje = datos.get("mensaje")


         antiNoti= Notificacion.objects.get(id=id)
         instEstado = Estadomensaje.objects.get(id=estado)
         instUsuario = Tipousuario.objects.get(id=usuario)

         # actualizamos datos
         antiNoti.estadomensaje = instEstado
         antiNoti.tipousuario = instUsuario
         antiNoti.mensaje = mensaje
         antiNoti.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   # peticion GET
   formId = FormNotificacionDelete()
   if 'id' in request.GET:
      query = request.GET['id']  # query tiene le valor del dni

      id = str(query)

      if Notificacion.objects.filter(id=id):
         noti = Notificacion.objects.get(id=id)

         data = {
            "nomEstEle": noti.estadomensaje.nombre,
            "idEstEle": noti.estadomensaje.id,
            "nomUsuEle": noti.tipousuario.nombre,
            "idUsuEle": noti.tipousuario.id,
            "sms": noti.mensaje,
         }

         datosEstado = listaEstados(data["nomEstEle"])
         datosUsuario = listaUsuarios(data["nomUsuEle"])

         return render(request, 'modNot.html', {"formId": formId, "buscado": True, "datos": data,
               "datosEstado": datosEstado, 'datosUsuario':datosUsuario, 'cliente': False,
               'encargado': encargado, 'Basico': basico})
      else:
         messages.error(request, "La notificacion no existe.")
         return HttpResponseRedirect("/notificacion/modificarNotificacion")

   # primera vista
   formId = FormNotificacionDelete()
   return render(request, 'modNot.html', {"formId": formId, "buscado": False,
          'cliente': False, 'encargado': encargado, 'Basico': basico})

def borrar(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormNotificacionDelete(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         nombre = datos.get("nombre")

         if Notificacion.objects.filter(id=id):
            Notificacion.objects.get(id=id).delete()
            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, "La notificacion no existe.")
   else:
      form = FormNotificacionDelete()
   return render(request, 'borrar.html', {'form': form, 'elem': "notificacion", 'cliente': False,
      'encargado': encargado, 'Basico': basico})

def listar(request):
   datosFinales = datosNotificaciones()
   encargado, basico = comprobarSesion(request)
   return render(request, 'listarNotificaciones.html', {"datos": datosFinales, 'cliente': False,
        'encargado': encargado, 'Basico': basico})


"""
        METODOS AUXILIARES
"""


def datosNotificaciones():
   datos = Notificacion.objects.all();
   datosFinales = []

   for noti in datos:
      instEstado = Estadomensaje.objects.get(id=noti.estadomensaje.id)
      instUsuario = Tipousuario.objects.get(id=noti.tipousuario.id)

      data = {
         "id": noti.id,
         "est": instEstado.nombre,
         "usu": instUsuario.nombre,
         "sms": noti.mensaje,
      }

      datosFinales.append(data)

   return datosFinales


def listaEstados(nombre):
   tipos = Estadomensaje.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": str(tipo.nombre),
         }
         lista.append(data)

   return lista


def listaUsuarios(nombre):
   tipos = Tipousuario.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": str(tipo.nombre),
         }
         lista.append(data)

   return lista
