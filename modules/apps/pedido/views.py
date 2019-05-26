from django.core.mail import EmailMessage
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from ..stock.models import Stock
from ..proveedor.models import Proveedor
#from ..Inventario.models import Inventario
from .forms import *
from ..horarioEmpleado.views import formatoDateString
from usuarios.models import Empleado,TipoEmpleado
from django.contrib.auth.decorators import login_required

@login_required()
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

            instEstadoPedido = EstadoPedido.objects.get(id=estado)
            instProducto = Producto.objects.get(id=producto)

            precio = instProducto.precio
            total = cantidad * precio

            p = Pedido(cantidad=cantidad, total=total, fecha=fecha, estadopedido=instEstadoPedido, producto=instProducto)
            p.save()

            crearInventario(p)

            if instEstadoPedido.id == 1:
                actualizarStockInventario(p)

            return HttpResponseRedirect("/pedido/lista")

    else:
        form = FormPedidoInsert()

    return render(request, 'penuevo.html', {'form': form, "fecha": formatoDate(), "datosEstado": listaEstado(""),
                                            "datosProd": listaProdcutos()})

@login_required()
def listar(request):
    datos = Pedido.objects.all()
    lista = []

    for pedido in datos:
        data = {
            "id": pedido.id,
            "estado": pedido.estadopedido.nombre.title(),
            "cantidad": pedido.cantidad,
            "total": pedido.total,
            "fecha": formatoDateString(str(pedido.fecha)),
            "idProd": pedido.producto.id,
            "idProv": pedido.producto.proveedor.id,
            "producto": pedido.producto.nombre,
            "proveedor": pedido.producto.proveedor.nombre,
        }
        lista.append(data)
    return render(request, 'pelista.html', {"lista": lista})

@login_required()
def modificar(request,pk):
    try:
        pedido = Pedido.objects.get(id=pk)

        if request.method == "POST":
            form = FormPedidoUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                cantidad = datos.get("cantidad")
                estado = datos.get("Estado")

                # se ha modificado el nombre
                antiPed = Pedido.objects.get(id=pk)
                instEstadoPedido = EstadoPedido.objects.get(id=estado)
                precio = antiPed.producto.precio

                # actualizamos datos
                antiPed.total = precio* cantidad
                antiPed.cantidad = cantidad
                antiPed.estadopedido = instEstadoPedido
                antiPed.save()


                #modificamos el stock si le indicamos que el estado es entregado
                if instEstadoPedido.id == 1:
                    actualizarStockInventario(antiPed)

                #return HttpResponseRedirect('/pedido/'+str(pk)+'/detalle')
                return HttpResponseRedirect("/pedido/lista")

            # peticion GET
        elif request.method == "GET":

            if pedido.estadopedido.id == 2:
                mod = True
            else:
                mod = False

            data = {
                "fecha": formatoDateString(str(pedido.fecha)),
                "nomProEle": pedido.producto.nombre,
                "idProEle": pedido.producto.id,
                "cantidad": pedido.cantidad,
                "nomEstEle": pedido.estadopedido.nombre.title(),
                "idEstEle": pedido.estadopedido.id,
                "modificar":mod,
            }

            return render(request,'pedmodificar.html', {"datos": data,"datosEstado": listaEstado(data["nomEstEle"])})

    except Producto.DoesNotExist:
        raise Http404("Producto no existe")

    return render(request, 'pedmodificar.html', {"datos": {},"datosTipo": {}})

@login_required()
def eliminar(request, pk):
    try:
        pedido = Pedido.objects.get(id=pk)
        pedido.delete()
    except Pedido.DoesNotExist:
        raise Http404("Pedido no existe")

    return HttpResponseRedirect("/pedido/lista")

@login_required()
def detalle(request, pk):
    try:
        pedido = Pedido.objects.get(id=pk)
        data = {
            "id": pedido.id,
            "fecha": formatoDateString(str(pedido.fecha)),
            "producto": pedido.producto.nombre,
            "cantidad": pedido.cantidad,
            "total": pedido.total,
            "estado": pedido.estadopedido.nombre.title(),
            "proveedor": pedido.producto.proveedor.nombre
        }
        estados = listarEstados(data["id"], data["estado"])

    except Pedido.DoesNotExist:
        raise Http404("Pedido no existe")

    return render(request, 'pedetalle.html', {"datos": data, "estados": estados})

"""
    METODOS AUXILIARES
"""
def estado(request, pk, sk):

    try:
        pedido = Pedido.objects.get(id=pk)
        estado = EstadoPedido.objects.get(id=sk)
        pedido.estadopedido = estado
        pedido.save()

    except Pedido.DoesNotExist:
        raise Http404("Pedido no existe")
    except EstadoPedido.DoesNotExist:
        raise Http404("Estado no existe")

    return HttpResponseRedirect("/pedido/" + str(pk) + "/detalle")

def listarEstados(idPedido, nombre):
    estados = EstadoPedido.objects.all()

    lista = []

    for tipo in estados:
        nom = str(tipo.nombre).title().lower()
        if nom != nombre:
            data = {
                "idPedido": idPedido,
                "id": tipo.id,
                "nom": str(tipo.nombre),
            }
            lista.append(data)

    return lista

def listaEstado(nombre):
    estados = EstadoPedido.objects.all()

    lista = []

    for tipo in estados:
        if nombre != tipo.nombre.title():
            data = {
                "id": tipo.id,
                "nom": str(tipo.nombre).title(),
            }
            lista.append(data)
    return lista

def listaProdcutos():
    prd = Producto.objects.all()
    lista = []

    for pro in prd:
        if pro.borrado != 1:
            data = {
                "id": pro.id,
                "nom": str(pro.nombre).title(),
            }
            lista.append(data)

    return lista

def formatoDate():
    fecha = timezone.now().date()
    fecha = str(fecha)
    # en la bbdd se guarda yyyy-mm-dd cambiamso para que sea dd-mm-yyy
    cad = fecha.split('-')
    cad = cad[2] + '-' + cad[1] + '-' + cad[0]

    return cad

def actualizarStockInventario(pedido):

    # vemos si ya hay stock de esto
    stock = Stock.objects.filter(producto=pedido.producto.id, proveedor=pedido.producto.proveedor.id)

    if stock: #actualizamos

        for s in stock:
            instStock = Stock.objects.get(id=s.id)

        dif = instStock.canttotal - instStock.cantprov
        act = instStock.canttotal + pedido.cantidad
        prov = act - dif

        instStock.canttotal=act
        instStock.cantprov = prov
        instStock.save()

        if act < 11:
            enviarCorreo(pedido,act)

    else:#insertamos
        instProducto = Producto.objects.get(id=pedido.producto.id)
        instProveedor = Proveedor.objects.get(id=instProducto.proveedor.id)

        s = Stock(cantprov=pedido.cantidad, canttotal=pedido.cantidad, proveedor=instProveedor, producto=instProducto)
        s.save()

        if pedido.cantidad < 11:
            enviarCorreo(pedido,pedido.cantidad)
    """
    #actualizamos inventario
    inv = Inventario.objects.filter(pedido=pedido.id)
    fecha = timezone.now().date()

    if inv: #actualizamos

        for i in inv:
            instInv = Inventario.objects.get(id=i.id)

        instInv.fechafin = fecha
        instInv.save()
    """

def crearInventario(pedido):
    fecha = timezone.now().date()
    coste = pedido.cantidad * pedido.producto.precio

    #i = Inventario(coste=coste, cantidad=pedido.cantidad, fechaentrada=fecha, pedido=pedido)
    #i.save()

def enviarCorreo(datos, cant):

    lista = []
    ints = TipoEmpleado.objects.get(id=1)
    empleados = Empleado.objects.filter(tipoempleado=ints)
    message = 'Aviso sobre el producto '+ datos.producto.nombre + ' con código ' + datos.producto.codigo + \
        ' del proveedor '+ datos.producto.proveedor.nombre + ' su stock es: '+ str(cant) + '.'

    for emp in empleados:
        if emp.tipoempleado.id == 1:
            lista.append(emp.email)

    for e in lista:
        email = EmailMessage('Aviso Stock Cleo', message, to=[e])
        email.send()
