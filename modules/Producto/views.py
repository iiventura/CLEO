from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from modules.Producto.models import Producto, Tipoproducto
from .forms import FormProductoInsert


def nuevo(request):
    if request.method == "POST":
        form = FormProductoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            id = datos.get("id")
            nombre = datos.get("nombre")
            tipo = datos.get("Tipo")

            if not Producto.objects.filter(id=id):  # todavia se puede guardar una maquina mas
                instTipoProducto = Tipoproducto.objects.get(id=tipo)
                p = Producto(id=id, nombre=nombre, tipoproducto=instTipoProducto);
                p.save()

                return render(request, 'pnuevo.html', {'form': form})
            else:
                messages.error(request, 'El producto ya existe.')
                messages.error(request, '')
    else:
        form = FormProductoInsert()

    return render(request, 'pnuevo.html', {'form': form})

def listar(request):
    datos = Producto.objects.all()
    lista = []
    data={}

    for prod in datos:
        instTipoProducto = Tipoproducto.objects.get(id=prod.tipoproducto.id)

        data = {
            "id": prod.id,
            "nom": prod.nombre,
            "tipo": instTipoProducto.nombre.title(),
        }
        lista.append(data)



    return render(request, 'plista.html', {"lista": lista})


def eliminar(request, pk):
   try:
      producto = Producto.objects.get(id=pk)
      producto.delete()
   except Producto.DoesNotExist:
      raise Http404("Producto no existe")

   return HttpResponseRedirect("/producto/lista")


def detalle(request, pk):
   try:
      producto = Producto.objects.get(id=pk)
      tipo = Tipoproducto.objects.get(id=producto.tipoproducto.id)
      data = {
         "id":  producto.id,
         "nom":  producto.nombre,
         "tipo": tipo.nombre.title(),
      }
   except Producto.DoesNotExist:
      raise Http404("Producto no existe")

   return render(request, 'pdetalle.html', {"datos": data})

