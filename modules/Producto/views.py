from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from modules.Producto.models import Producto, TipoProducto
from .forms import FormProductoInsert, FormProductoUpdate


def nuevo(request):
    if request.method == "POST":
        form = FormProductoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            codigo = datos.get("codigo")
            nombre = datos.get("nombre")
            tipo = datos.get("Tipo")

            if not Producto.objects.filter(codigo=codigo):
                instTipoProducto = TipoProducto.objects.get(id=tipo)
                p = Producto(codigo=codigo, nombre=nombre, tipoproducto=instTipoProducto)
                p.save()

                return HttpResponseRedirect("/producto/lista")
            else:
                messages.error(request, 'El producto ya existe.')
                messages.error(request, '')
    else:
        form = FormProductoInsert()

    return render(request, 'prdnuevo.html', {'form': form,'elem': 'Añadir','titulo':'Añadir Producto'})


def listar(request):
    datos = Producto.objects.all()
    lista = []

    for prod in datos:
        instTipoProducto = TipoProducto.objects.get(id=prod.tipoproducto.id)

        data = {
            "id": prod.id,
            "cod": prod.codigo,
            "nom": prod.nombre,
            "tipo": instTipoProducto.nombre.title(),
        }
        lista.append(data)
    return render(request, 'prdlista.html', {"lista": lista})

def modificar(request,pk):
    try:
        prod = Producto.objects.get(id=pk)

        if request.method == "POST":
            form = FormProductoUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                codigo = datos.get("codigo")
                nomProd = datos.get("nombre")
                tipo = datos.get("Tipo")

                # se ha modificado el nombre
                antiProd = Producto.objects.get(id=pk)
                instTipoProducto = TipoProducto.objects.get(id=tipo)

                # actualizamos datos
                antiProd.nombre = nomProd
                antiProd.tipoproducto = instTipoProducto
                antiProd.save()

                return HttpResponseRedirect('/producto/'+str(pk)+'/detalle')

            # peticion GET
        elif request.method == "GET":

            data = {
                "cod": prod.codigo,
                "nom": prod.nombre,
                "nomTipoEle": str(prod.tipoproducto.nombre).title(),
                "idTipoEle": prod.tipoproducto.id,
            }

            datosTipos = listaTiposProductos(data["nomTipoEle"])
            print(data, datosTipos)
            return render(request, 'prdmodificar.html', {"datos": data, "datosTipo":datosTipos})

    except Producto.DoesNotExist:
        raise Http404("Producto no existe")

    return render(request, 'prdmodificar.html', {"datos": {},"datosTipo": {}})

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
      tipo = TipoProducto.objects.get(id=producto.tipoproducto.id)
      data = {
         "id": producto.id,
         "cod":  producto.codigo,
         "nom":  producto.nombre,
         "tipo": tipo.nombre.title(),
      }
   except Producto.DoesNotExist:
      raise Http404("Producto no existe")

   return render(request, 'prddetalle.html', {"datos": data})



def listaTiposProductos(nombre):

    tipos = TipoProducto.objects.all();
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