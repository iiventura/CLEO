from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import EstadoPedido, Proveedor, Producto, Pedido
from .forms import FormPedidoInsert


def nuevo(request):
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

         instEstadoPedido = EstadoPedido.objects.get(id=estado)
         instProducto = Producto.objects.get(id=producto)
         instProveedor = Proveedor.objects.get(id=proveedor)
         p = Pedido(cantidad=cantidad, fecha=fecha, estadopedido=instEstadoPedido, producto=instProducto, proveedor=instProveedor)
         p.save()

         return render(request, 'penuevo.html', {'form': form})

   else:
      form = FormPedidoInsert()

   return render(request, 'penuevo.html', {'form': form})

def listar(request):
    datos = Pedido.objects.all()
    lista = []
    data={}

    for pedido in datos:
        data = {
            "id": pedido.id,
            "fecha": str(pedido.fecha),
            "idProv":pedido.proveedor.id,
            "proveedor": pedido.proveedor.nombre,
            "idProd": pedido.producto.id,
            "producto": pedido.producto.nombre,
        }
        lista.append(data)
    return render(request, 'pelista.html', {"lista": lista})

def eliminar(request, pk):
   try:
      pedido = Pedido.objects.get(id=pk)
      pedido.delete()
   except Pedido.DoesNotExist:
      raise Http404("Pedido no existe")

   return HttpResponseRedirect("/pedido/lista")


def detalle(request, pk):
   try:
      pedido = Pedido.objects.get(id=pk)
      data = {
          "id": pedido.id,
          "fecha": str(pedido.fecha),
          "proveedor": pedido.proveedor.nombre,
          "producto": pedido.producto.nombre,
          "cantidad": pedido.cantidad,
          #"estado":
      }
   except Producto.DoesNotExist:
      raise Http404("Pedido no existe")

   return render(request, 'pedetalle.html', {"datos": data})
