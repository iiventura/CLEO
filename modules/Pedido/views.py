from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..Empleado.views import comprobarSesion
from .forms import *
from .models import Pedido,Estadopedido
from ..Proveedor.models import Proveedor
from ..Producto.models import Producto
from django.contrib import messages

# Create your views here.
def nuevo(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormPedidoInsert(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         cantidad = datos.get("cantidad")
         fecha = datos.get("fecha")
         estado = datos.get("Estado")
         producto = datos.get("producto")
         proveedor = datos.get("proveedor")

         instEstadoPedido = Estadopedido.objects.get(id=estado)
         instProducto = Producto.objects.get(id=producto)
         instProveedor = Proveedor.objects.get(id=proveedor)
         p = Pedido(cantidad=cantidad, fecha=fecha, estadopedido=instEstadoPedido, producto=instProducto, proveedor=instProveedor)
         p.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   else:
      form = FormPedidoInsert()

   return render(request, 'alta.html', {'form': form, 'elem': "pedido", 'cliente': False,
          'encargado': encargado, 'Basico': basico})

def modificar(request):
   encargado, basico = comprobarSesion(request)
   # si es una peticion post
   if request.method == "POST":
      form = FormPedidoUpdate(request.POST)
      id = request.GET.get("id")  # obtenemos el dni que hemos buscado

      if form.is_valid():
         datos = form.cleaned_data

         # recogemos los datos
         cantidad = datos.get("cantidad")
         fecha = datos.get("fecha")
         estado = datos.get("Estado")
         prod = datos.get("producto")
         prov = datos.get("proveedor")

         # se ha modificado el nombre
         antiPed = Pedido.objects.get(id=id)
         instEstadoPedido = Estadopedido.objects.get(id=estado)
         instProducto = Producto.objects.get(id=prod)
         instProveedor = Proveedor.objects.get(id=prov)
         
         # actualizamos datos
         antiPed.cantidad = cantidad
         antiPed.fecha = fecha
         antiPed.estado = instEstadoPedido
         antiPed.producto = instProducto
         antiPed.proveedor = instProveedor
         antiPed.save()

         return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

   # peticion GET
   formId = FormPedidoDelete()
   if 'id' in request.GET:
      query = request.GET['id']  # query tiene le valor del dni

      id = str(query)

      if Pedido.objects.filter(id=id):
         ped = Pedido.objects.get(id=id)

         data = {
            "can": ped.cantidad,
            "fec": str(ped.fecha),
            "nomEstadoEle": str(ped.estadopedido.nombre).title(),
            "idEstadoEle": ped.estadopedido.id,
            "nomProdEle": ped.producto.nombre,
            "idProdEle": ped.producto.id,
            "nomProvEle": ped.proveedor.nombre,
            "idProvEle": ped.proveedor.id,
         }

         datosEstado = listaEstadosPedido(data["nomEstadoEle"])
         datosProd = listaProducto(data["nomProdEle"])
         datosProv = listaProveedor(data["nomProvEle"])

         return render(request, 'modPed.html', {"formId": formId, "buscado": True, "datos": data,
               "datosEstado": datosEstado, "datosProd": datosProd, "datosProv": datosProv,
               'cliente': False,'encargado': encargado, 'Basico': basico})
      else:
         messages.error(request, "El pedido no existe.")
         return HttpResponseRedirect("/pedido/modificarPedido")

   # primera vista
   formId = FormPedidoDelete()
   return render(request, 'modPed.html', {"formId": formId, "buscado": False,
         'cliente': False, 'encargado': encargado, 'Basico': basico})

def borrar(request):
   encargado, basico = comprobarSesion(request)
   if request.method == "POST":
      form = FormPedidoDelete(request.POST)

      if form.is_valid():
         datos = form.cleaned_data

         ped = datos.get("id")

         if Pedido.objects.filter(id=ped):
            Pedido.objects.get(id=ped).delete()
            return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
         else:
            messages.error(request, "No existe este pedido.")

   else:
      form = FormPedidoDelete()
   return render(request, 'borrar.html', {'form': form, 'elem': "maquina", 'cliente': False,
                                          'encargado': encargado, 'Basico': basico})

def listar(request):
   datosFinales = datosPedidos()
   encargado, basico = comprobarSesion(request)
   return render(request, 'listarPedidos.html', {"datos": datosFinales, 'cliente': False,
         'encargado': encargado, 'Basico': basico})

"""
        METODOS AUXILIARES
"""
def datosPedidos():

    datos = Pedido.objects.all();
    datosFinales = []

    for ped in datos:

        data = {
            "id": ped.id,
            "can": ped.cantidad,
            "fec": str(ped.fecha),
            "estado": ped.estadopedido.nombre.title(),
            "prod": ped.producto.nombre,
            "prov": ped.proveedor.nombre,
        }

        datosFinales.append(data)

    return datosFinales


def listaEstadosPedido(nombre):
   tipos = Estadopedido.objects.all();
   lista = []

   for tipo in tipos:
      nom = str(tipo.nombre).title();
      if nom != nombre:
         data = {
            "id": tipo.id,
            "nom": str(tipo.nombre),
         }
         lista.append(data)

   return lista

def listaProducto(nombre):
   tipos = Producto.objects.all();
   lista = []

   for tipo in tipos:
      nom = str(tipo.nombre).title();
      if nom != nombre:
         data = {
            "id": tipo.id,
            "nom": str(tipo.nombre),
         }
         lista.append(data)

   return lista

def listaProveedor(nombre):
   tipos = Proveedor.objects.all();
   lista = []

   for tipo in tipos:
      nom = str(tipo.nombre).title();
      if nom != nombre:
         data = {
            "id": tipo.id,
            "nom": str(tipo.nombre),
         }
         lista.append(data)

   return lista
