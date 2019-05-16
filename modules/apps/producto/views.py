from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Producto, TipoProducto
from .forms import FormProductoInsert, FormProductoUpdate
from ..proveedor.models import Proveedor
from django.contrib.auth.decorators import login_required

@login_required()
def nuevo(request):
    if request.method == "POST":
        form = FormProductoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            codigo = datos.get("codigo")
            nombre = datos.get("nombre")
            precio = datos.get("precio")
            tipo = datos.get("Tipo")
            proveedor = datos.get("proveedor")

            if not Producto.objects.filter(codigo=codigo) or Producto.objects.filter(codigo=codigo,borrado=1):

                instTipoProducto = TipoProducto.objects.get(id=tipo)
                instProveedor = Proveedor.objects.get(id=proveedor)

                p = Producto(codigo=codigo, nombre=nombre, precio=precio, uso=uso, tipoproducto=instTipoProducto,
                    proveedor=instProveedor, borrado=0)
                p.save()

                return HttpResponseRedirect("/producto/lista")
            else:
                messages.error(request, 'El producto ya existe.')
                messages.error(request, '')
    else:
        form = FormProductoInsert()

    return render(request, 'prdnuevo.html', {'datosProv': listaProveedores(""),'datosTipo':listaTiposProductos("")})

@login_required()
def listar(request):
    datos = Producto.objects.all()
    lista = []

    for prod in datos:
        instTipoProducto = TipoProducto.objects.get(id=prod.tipoproducto.id)

        if prod.proveedor.borrado != 1:
            if prod.borrado != 1:
                data = {
                    "id": prod.id,
                    "cod": prod.codigo,
                    "nom": prod.nombre,
                    "prec": prod.precio,
                    "tipo": instTipoProducto.nombre.title(),
                    "prov": prod.proveedor.nombre.title(),
                    "idPrv": prod.proveedor.id,
                }

                lista.append(data)

    return render(request, 'prdlista.html', {"lista": lista})

@login_required()
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
                precio = datos.get("precio")
                tipo = datos.get("Tipo")
                proveedor = datos.get("proveedor")

                # se ha modificado el nombre
                antiProd = Producto.objects.get(id=pk)
                instTipoProducto = TipoProducto.objects.get(id=tipo)
                instProveedor = Proveedor.objects.get(id=proveedor)

                # actualizamos datos
                antiProd.nombre = nomProd
                antiProd.precio = precio
                antiProd.tipoproducto = instTipoProducto
                antiProd.proveedor = instProveedor
                antiProd.borrado=0
                antiProd.save()

                return HttpResponseRedirect('/producto/'+str(pk)+'/detalle')

            # peticion GET
        elif request.method == "GET":

            data = {
                "cod": prod.codigo,
                "nom": prod.nombre,
                "prec": prod.precio,
                "nomTipoEle": str(prod.tipoproducto.nombre).title(),
                "idTipoEle": prod.tipoproducto.id,
                "nomPrvEle": str(prod.proveedor.nombre).title(),
                "idPrvEle": prod.proveedor.id,
            }

            datosTipos = listaTiposProductos(data["nomTipoEle"])
            datosProv = listaProveedores(data["nomPrvEle"])

            return render(request, 'prdmodificar.html', {"datos": data, "datosTipo":datosTipos,"datosProv":datosProv})

    except Producto.DoesNotExist:
        raise Http404("Producto no existe")

    return render(request, 'prdmodificar.html', {"datos": {},"datosTipo": {}})

@login_required()
def eliminar(request, pk):
   try:
      producto = Producto.objects.get(id=pk)
      #producto.delete()
      producto.borrado=1
      producto.save()
   except Producto.DoesNotExist:
      raise Http404("Producto no existe")

   return HttpResponseRedirect("/producto/lista")

@login_required()
def detalle(request, pk):
   try:
      producto = Producto.objects.get(id=pk)
      tipo = TipoProducto.objects.get(id=producto.tipoproducto.id)

      data = {
         "id": producto.id,
         "cod":  producto.codigo,
         "nom":  producto.nombre,
         "prec": producto.precio,
         "tipo": tipo.nombre.title(),
         "idPrv": producto.proveedor.id,
      }

   except Producto.DoesNotExist:
      raise Http404("Producto no existe")

   return render(request, 'prddetalle.html', {"datos": data})

"""
    METODOS AUXILIARES
"""
def listaProveedores(nombre):

   prov = Proveedor.objects.all()
   lista = []

   for pro in prov:
       if pro.borrado != 1 and pro.nombre.title() != nombre:
        data = {
           "id": pro.id,
           "nom": str(pro.nombre).title(),
        }
        lista.append(data)

   return lista

def listaTiposProductos(nombre):

    tipos = TipoProducto.objects.all()
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title()
        if nom != nombre:
            data = {
                "id": tipo.id,
                "nom": str(tipo.nombre).title(),
            }
            lista.append(data)

    return lista