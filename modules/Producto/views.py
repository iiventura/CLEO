from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from modules.Producto.models import Producto, Tipoproducto
from .forms import FormProductoInsert, FormProductoUpdate


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

def modificar(request,pk):
    try:
        prod = Producto.objects.get(id=pk)

        if request.method == "POST":
            form = FormProductoUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                nomProd = datos.get("nombre")
                tipo = datos.get("Tipo")

                # se ha modificado el nombre
                antiProd = Producto.objects.get(id=pk)
                instTipoProducto = Tipoproducto.objects.get(id=tipo)

                # actualizamos datos
                antiProd.nombre = nomProd
                antiProd.tipoproducto = instTipoProducto
                antiProd.save()

                return HttpResponseRedirect('/producto/'+str(pk)+'/detalle')

            # peticion GET
        elif request.method == "GET":

            data = {
                "id": prod.id,
                #"codigo": prod.codigo,
                "nombre": prod.nombre,
                "nomTipoEle": str(prod.tipoproducto.nombre).title(),
                "idTipoEle": prod.tipoproducto.id,
            }

            datosTipos = listaTiposProductos(data["nomTipoEle"])
            print(data, datosTipos)
            return render(request, 'pmodificar.html', {"datos": data, "datosTipo":datosTipos})

    except Producto.DoesNotExist:
        raise Http404("Producto no existe")

    return render(request, 'pmodificar.html', {"datos": {},"datosTipo": {}})








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



def listaTiposProductos(nombre):

    tipos = Tipoproducto.objects.all();
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