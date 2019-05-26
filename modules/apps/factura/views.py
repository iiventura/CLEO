from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.utils import timezone
from .forms import *
from .models import Factura, Estadofactura
from ..cita.models import Cita
from ..horarioEmpleado.views import formatoDateString
from ..stock.models import Stock
from ..pedido.views import enviarCorreo
from django.contrib.auth.decorators import login_required

@login_required()
def nuevo (request):

    if request.method == "GET":
        form = FormFacturaInsert1(request.GET)

        if form.is_valid():
            datos = form.cleaned_data
            cita = datos.get("cita")

            instCita = Cita.objects.get(id=cita)
            fecha = today()

            data = {
                "idCitaEle": instCita.id,
                "dniCliEle": instCita.cliente.dni,
                "dniEmpEle": instCita.empleado.dni,
                "total": instCita.tratamiento.precio,
                "fecha": fecha
            }

            # vemos si ya habia una factura para esta cita => esta francionada
            # pondremos la diferencia
            facturas = Factura.objects.filter(cita=instCita)
            fracc = False
            resto = 0

            if facturas: #esta fraccionada
                fracc = True
                resto = totalPorPagar(instCita, facturas)

            if fracc:
                data["total"] = resto

            return render(request, 'fnuevo2.html', {"datos": data, "datosEstado": listaEstado("")})

    if request.method == "POST":
        form = FormFacturaInsert2(request.POST)

        if form.is_valid():

            datos = form.cleaned_data
            cita = datos.get("cita")
            estado = datos.get("estado")
            fecha = datos.get("fecha")
            paga = datos.get("paga")

            instCita = Cita.objects.get(id=cita)
            instEstado = Estadofactura.objects.get(id=estado)

            #cantidad
            total = instCita.tratamiento.precio

            #actualizar stock si es la primera factura de la cita
            instFacura = Factura.objects.filter(cita=instCita)

            if instFacura or instEstado.id == 2: #esta fraccionada o no se paga entera
                total = totalPorPagar(instCita, instFacura)

            if not instFacura and (not instFacura and paga >= total): #primera vez, y la 1º vez y ademas se apga entera
                actualizarStock(instCita)

            if paga >= total: #se paga entera
                instEstado = Estadofactura.objects.get(id=1) #nos aseguramos que el estado pase a pagado si se ha pagado completametne
            else:
                instEstado = Estadofactura.objects.get(id=2)

            f = Factura(costeporcobrar=paga, total=total, fecha=formatoDate(fecha), estadofactura=instEstado,
                        cita=instCita)
            f.save()

            return HttpResponseRedirect("/factura/lista")

    #metemos solo las citas con pagos pendientes
    return render(request, 'fnuevo.html', {'datosCita': listaCitas()})

@login_required()
def listar (request):

    datos = Factura.objects.all()
    lista = []

    for factura in datos:

        data = {
            "id": factura.id,
            "cita": factura.cita.id,
            "cliente": factura.cita.cliente.dni,
            "empleado": factura.cita.empleado.dni,
            "total": factura.total,
            "estado": factura.estadofactura.nombre.title(),
            "paga": factura.costeporcobrar,
            "fecha": formatoDateString(str(factura.fecha)),
        }

        lista.append(data)

    return render(request, 'flista.html', {"lista": lista})

@login_required()
def detalle (request,pk):

    try:
        factura = Factura.objects.get(id=pk)

        data = {
            "id": factura.id,
            "cita": factura.cita.id,
            "cliente": factura.cita.cliente.dni,
            "empleado": factura.cita.empleado.dni,
            "total": factura.cita.tratamiento.precio,
            "estado": factura.estadofactura.nombre.title(),
            "paga": factura.costeporcobrar,
            "fecha": factura.fecha,
        }

    except Factura.DoesNotExist:
        raise Http404("Factura no existe")

    return render(request, 'fdetalle.html', {"datos": data})

@login_required()
def modificar (request,pk):

    try:
        factura = Factura.objects.get(id=pk)

        if request.method == "POST":
            form = FormFacturaUpdate(request.POST)

            if form.is_valid():
                print("****")
                datos = form.cleaned_data
                estado = datos.get("estado")
                paga = datos.get("paga")

                # se ha modificado el nombre
                antiFac = Factura.objects.get(id=pk)
                instEstado = Estadofactura.objects.get(id=estado)
                instCita = antiFac.cita

                total = totalPorPagar(instCita, antiFac)

                # actualizamos datos
                antiFac.total = total
                antiFac.costeporcobrar = paga
                antiFac.estadofactura = instEstado
                antiFac.save()

                return HttpResponseRedirect("/factura/lista")

            # peticion GET
        elif request.method == "GET":

            if factura.estadofactura.id == 2:
                mod = True
            else:
                mod = False

            data = {
                "id": factura.id,
                "cita": factura.cita.id,
                "cliente": factura.cita.cliente.dni,
                "empleado": factura.cita.empleado.dni,
                "total": factura.cita.tratamiento.precio,
                "idEstEle": factura.estadofactura.id,
                "nomEstEle": factura.estadofactura.nombre.title(),
                "paga": factura.costeporcobrar,
                "fecha": formatoDateString(str(factura.fecha)),
                "modificar": mod,
            }

            return render(request,'fmodificar.html', {"datos": data,"datosEstado": listaEstado(data["nomEstEle"])})

    except Factura.DoesNotExist:
        raise Http404("Factura no existe")

    return render(request, 'fmodificar.html', {"datos": {},"datosTipo": {}})

"""
    METODOS AUXILIARES
"""

def listaEstado(nombre):
    estados = Estadofactura.objects.all()

    lista = []

    for tipo in estados:
        if nombre != tipo.nombre.title():
            data = {
                "id": tipo.id,
                "nom": str(tipo.nombre).title(),
            }
            lista.append(data)
    return lista

def listaCitas():

    #ponemos solo las citas que no tienen factura o que se NO ha pagado completamente

    estados = Cita.objects.all()

    lista = []

    for tipo in estados:

        facturas = Factura.objects.filter(cita=tipo)
        resto = 1 # por si no hubiese factura que tenga pendiente

        if facturas:  # esta fraccionada
            resto = totalPorPagar(tipo,facturas)

        if resto > 0: #tiene pagos pendientes
            data = {
                "id": tipo.id,
                "nom": tipo.id,
            }
            lista.append(data)
    return lista

def totalPorPagar(cita, facturas):

    totalFactura = cita.tratamiento.precio
    totalPagado = 0

    for fac in facturas:
        totalPagado += fac.costeporcobrar

    return totalFactura - totalPagado

def today():
    fecha = timezone.now().date()
    fecha = str(fecha)
    # en la bbdd se guarda yyyy-mm-dd cambiamso para que sea dd-mm-yyy
    cad = fecha.split('-')
    cad = cad[2] + '-' + cad[1] + '-' + cad[0]

    return cad

def formatoDate(fecha):

    d = datetime.datetime.strptime(fecha, '%d-%m-%Y').day
    m = datetime.datetime.strptime(fecha, '%d-%m-%Y').month
    y = datetime.datetime.strptime(fecha, '%d-%m-%Y').year

    return datetime.datetime(y, m, d).date()

def actualizarStock(cita):

    stock = Stock.objects.filter(producto=cita.tratamiento.producto.id, proveedor=cita.tratamiento.producto.proveedor.id,)

    if stock:  # actualizamos comprobamos con filter por si hubiesemos borardo el producto

        for s in stock:
            instStock = Stock.objects.get(id=s.id)

        total = instStock.canttotal - 1

        instStock.canttotal = total
        instStock.save()

        if instStock.canttotal < 11:
            enviarCorreo(instStock, instStock.canttotal)
