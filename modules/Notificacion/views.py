from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import *
from .models import *
from ..Cliente.models import Cliente
from ..Empleado.models import Empleado

from django.core.mail import EmailMessage

from django.contrib import messages

# Create your views here.
def nueva(request):
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

         #enviar mensajes
         if instUsuario.nombre == 'cliente':
            enviarCorreo('cliente',mensaje)
         else:
            enviarCorreo('encargado',mensaje)

         return HttpResponseRedirect("/notificacion/lista")

   else:
      form = FormNotificacionInsert()

   #return render(request, 'nnuevo.html', {'form': form})
   return render(request, 'nuevoGeneral.html', {'form': form, 'elem': 'Notificacion'})

def eliminar(request,pk):

   try:
      promo = Notificacion.objects.get(id=pk)
      promo.delete()
   except Notificacion.DoesNotExist:
      raise Http404("Notificacion no existe")

   return HttpResponseRedirect("/notificacion/lista")

def listar(request):

   datos = Notificacion.objects.all();
   lista = []

   for noti in datos:
      instEstado = Estadomensaje.objects.get(id=noti.estadomensaje.id)
      instUsuario = Tipousuario.objects.get(id=noti.tipousuario.id)

      data = {
         "id": noti.id,
         "est": instEstado.nombre,
         "usu": instUsuario.nombre,
         "sms": noti.mensaje,
      }

      lista.append(data)

   return render(request, './nlista.html', {"lista": lista})

def detalle(request, pk):
   try:
       noti = Notificacion.objects.get(id=pk)
       instEstado = Estadomensaje.objects.get(id=noti.estadomensaje.id)
       instUsuario = Tipousuario.objects.get(id=noti.tipousuario.id)

       data = {
          "id": noti.id,
          "est": instEstado.nombre,
          "usu": instUsuario.nombre,
          "sms": noti.mensaje,
       }

   except Notificacion.DoesNotExist:
      raise Http404("Notificacion no existe")

   return render(request, 'ndetalle.html', {"datos": data})

def modificar(request,pk):

   try:
      noti = Notificacion.objects.get(id=pk)

      # si es una peticion post
      if request.method == "POST":
         form = FormNotificacionUpdate(request.POST)
         if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            estado = datos.get("Estado")
            usuario = datos.get("Usuario")
            mensaje = datos.get("mensaje")


            antiNoti= Notificacion.objects.get(id=pk)
            instEstado = Estadomensaje.objects.get(id=estado)
            instUsuario = Tipousuario.objects.get(id=usuario)

            # actualizamos datos
            antiNoti.estadomensaje = instEstado
            antiNoti.tipousuario = instUsuario
            antiNoti.mensaje = mensaje
            antiNoti.save()

            return HttpResponseRedirect("/notificacion/lista")

      elif request.method == "GET":

         data = {
            "nomEstEle": noti.estadomensaje.nombre,
            "idEstEle": noti.estadomensaje.id,
            "nomUsuEle": noti.tipousuario.nombre,
            "idUsuEle": noti.tipousuario.id,
            "sms": noti.mensaje,
         }

         datosEstado = listaEstados(data["nomEstEle"])
         datosUsuario = listaUsuarios(data["nomUsuEle"])

         return render(request, 'nmodificar.html', {"datos": data,"datosEstado": datosEstado, 'datosUsuario':datosUsuario})

   except Notificacion.DoesNotExist:
      raise Http404("Notificacion no existe")

   return HttpResponseRedirect('/notificacion/' + str(pk) + '/modificar')


"""
        METODOS AUXILIARES
"""

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

def enviarCorreo(destinarario,texto):

   lista = []

   if destinarario == 'cliente':
      datos = Cliente.objects.all();

      for dato in datos:
         lista.append(dato.email)

   else:
      datos = Empleado.objects.all();

      for dato in datos:
         if dato.tipoempleado.id == 1:
            lista.append(dato.email)

   for e in lista:
      email = EmailMessage('Notificacion Cleo', texto, to=[e])
      email.send()


