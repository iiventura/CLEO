import datetime
import random
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from ..horarioEmpleado.views import formatoDateString
from ..horarioEmpleado.models import Horario
from  usuarios.models import Empleado,TipoEmpleado
from ..stock.models import Stock
from django.contrib.auth.decorators import login_required

@login_required()
def nuevo (request):

    if request.method == "GET":
        form = FormCitaClienteInsert2(request.GET)

        if form.is_valid():
            datos = form.cleaned_data
            cliente = datos.get("cliente")
            fecha = datos.get("fecha")
            tratamiento = datos.get("tratamiento")
            hora = datos.get("hora")

            instTratamiento = Tratamiento.objects.get(id=tratamiento)
            instCliente = Cliente.objects.get(dni=cliente)

            #vemos is es posible hacer ese tratamiento en esa fecha y hora (NO PUEDE HABER OTRO IGUAL)
            instHorarioEntrada = Horario.objects.get(hora=str(hora))
            posible = Cita.objects.filter(tratamiento=instTratamiento, fecha=fecha, horarioentrada=instHorarioEntrada)

            if not posible:

                # comprobamos que los dias de peseran han pasado
                # la fecha mas reciente ocupa le ultimo lugar
                posible = Cita.objects.filter(tratamiento=instTratamiento, cliente=instCliente).order_by("fecha")

                if posible: #si ya tenia cita con ese tratamiento
                    fin = posible.count() - 1
                    fechaBBDD = posible[fin].fecha
                    dif = (fecha - fechaBBDD).days
                else: #primera cita
                    dif = 10000

                if dif >= instTratamiento.espera:

                    data = {
                        "dni": cliente,
                        "fecha": formatoDateString(str(fecha)),
                        "idTraEle": instTratamiento.id,
                        "nomTraEle": instTratamiento.nombre,
                        "idHorEle": hora,
                        "nomHorEle": hora,
                    }

                    fechaHoy = timezone.now().date()

                    if fecha > fechaHoy:#fecha valida
                        fecha = formatoDateString(str(fecha))
                        lista = empleadosValidosNuevo(fecha, hora,instTratamiento.duracion)

                        if len(lista) > 0: #no hay disponibles
                            return render(request, 'ciclnuevo3.html', {"datos": data, 'datosEmpleado': lista})

                        else:
                            messages.error(request, 'No tenemos empleados disponibles.')
                    else:
                        messages.error(request, 'La fecha no es válida.')
                else:
                    mes = "Tienen que pasar "+ str(instTratamiento.espera) +" dias \n para hacer el tratamiento y solo han pasado"+ str(dif)
                    messages.error(request,mes)
            else:
                messages.error(request, 'No es posible realizar el tratamietno es esa fecha')

    if request.method == "GET":
        form = FormCitaClienteInsert(request.GET)

        if form.is_valid():
            datos = form.cleaned_data
            cliente = datos.get("cliente")
            tratamiento = datos.get("tratamiento")

            instTratamiento = Tratamiento.objects.get(id=tratamiento)
            instCliente = Cliente.objects.get(dni=cliente)


            if instCliente:

                data = {
                    "dni": cliente,
                    "idTraEle": instTratamiento.id,
                    "nomTraEle": instTratamiento.nombre,
                    "duracion": instTratamiento.duracion,
                }

                return render(request, 'ciclnuevo2.html', {"datos": data,'datosHora':listaHoras(data["duracion"])})
            else:
                messages.error(request, 'El cliente no se encuentra.')

    if request.method == "POST":
        form = FormCitaClienteInsert3(request.POST)

        if form.is_valid():

            datos = form.cleaned_data
            cliente = datos.get("cliente")
            fecha = datos.get("fecha") #ya esta en formato string
            tratamiento = datos.get("tratamiento")
            hora = datos.get("hora")
            empleado = datos.get("empleado")

            instCliente = Cliente.objects.get(dni=cliente)
            instTratamiento = Tratamiento.objects.get(id=tratamiento)

            if empleado != "0":
                instEmpleado = Empleado.objects.get(id=empleado)
            else:
                lista = empleadosValidosNuevo(fecha, hora) #obtenemso los empleados disponibles
                x = random.randint(-1, len(lista) - 1) #elegimos uno al azar
                idAzar =int(lista[0][x]["id"])
                instEmpleado = Empleado.objects.get(id=idAzar)

            newHora = finHora(hora, instTratamiento.duracion)
            instHorarioSalida = Horario.objects.get(hora=str(newHora))
            instHorarioEntrada = Horario.objects.get(hora=str(hora))
            instEstadoCita = Estadocita.objects.get(id=2)
            fecha = formatoDate(fecha) #lo pasamos  a date par insertarlo

            # insertamos la cita
            c = Cita(fecha=fecha, estadocita=instEstadoCita, cliente=instCliente,
                     empleado=instEmpleado, tratamiento=instTratamiento,
                     horarioentrada=instHorarioEntrada, horariosalida=instHorarioSalida)
            c.save()

            return HttpResponseRedirect("/cita/lista")

    return render(request, 'ciclnuevo.html', {'datosTratamiento':listaTratamiento()})

@login_required()
def listar (request):

    datos = Cita.objects.all()
    lista = []

    for cita in datos:
        data = {
            "id": cita.id,
            "estado": cita.estadocita.nombre.title(),
            "fecha": formatoDateString(str(cita.fecha)),
            "cliente": cita.cliente.nombre,
            "empleado": cita.empleado.nombre,
            "trat": cita.tratamiento.nombre,
            "entrada": cita.horarioentrada.hora,
            "salida": cita.horariosalida.hora,
        }

        lista.append(data)

    return render(request, 'cilista.html', {"lista": lista})

@login_required()
def misCitas (request):

    instEmpleado = Empleado.objects.get(dni="12345678A")
    datos = Cita.objects.filter(empleado=instEmpleado)
    lista = []

    for cita in datos:
        data = {
            "id": cita.id,
            "estado": cita.estadocita.nombre.title(),
            "fecha": formatoDateString(str(cita.fecha)),
            "cliente": cita.cliente.nombre,
            "empleado": cita.empleado.nombre,
            "trat": cita.tratamiento.nombre,
            "entrada": cita.horarioentrada.hora,
            "salida": cita.horariosalida.hora,
        }

        lista.append(data)

    return render(request, 'cilista.html', {"lista": lista})

@login_required()
def detalle (request,pk):
    try:
        cita = Cita.objects.get(id=pk)

        data = {
            "id": cita.id,
            "estado": cita.estadocita.nombre.title(),
            "fecha": formatoDateString(str(cita.fecha)),
            "cliente": cita.cliente.nombre,
            "empleado": cita.empleado.nombre,
            "trat": cita.tratamiento.nombre,
            "entrada": cita.horarioentrada.hora,
            "salida": cita.horariosalida.hora,
        }

    except Cita.DoesNotExist:
        raise Http404("Cita no existe")

    return render(request, 'cidetalle.html', {"datos": data})

@login_required()
def eliminar (request,pk):
    try:
        cita = Cita.objects.get(id=pk)
        enviarEmailCancelada(cita)

        cita.delete()

    except Cita.DoesNotExist:
        raise Http404("Cita no existe")

    return HttpResponseRedirect("/cita/lista")

@login_required()
def modificar (request,pk):
    #el empleado y el estado

    try:
        cita = Cita.objects.get(id=pk)

        if request.method == "POST":
            form = FormCitaUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                estado = datos.get("estado")
                empleado = datos.get("empleado")

                antiCita = Cita.objects.get(id=pk)
                instEstadoCita = Estadocita.objects.get(id=estado)
                instEmpleado = Empleado.objects.get(id=empleado)

                # actualizamos datos
                antiCita.estadocita = instEstadoCita
                antiCita.empleado = instEmpleado
                antiCita.save()

                if instEstadoCita.id == 1:
                    enviarEmailConfirmacion(antiCita)

                #decrementamos en los productos temporales
                actualizarStockProducto(antiCita.tratamiento.producto)

                return HttpResponseRedirect("/cita/lista")

            # peticion GET
        elif request.method == "GET":

            data = {
                "dni": cita.cliente.dni,
                "fecha": formatoDateString(str(cita.fecha)),
                "idTraEle": cita.tratamiento.id,
                "nomTraEle": cita.tratamiento.nombre.title(),
                "idHorEle": cita.horarioentrada.hora,
                "nomHorEle": cita.horarioentrada.hora,
                "idEmpEle": cita.empleado.id,
                "nomEmpEle": cita.empleado.nombre,
                "idEstEle": cita.estadocita.id,
                "nomEstEle": cita.estadocita.nombre.title(),
            }

            lista = empleadosValidosModificar(data['fecha'],data['nomHorEle'],cita.tratamiento.duracion,data["idEmpEle"])

            return render(request,'cimodificar.html', {"datos": data, "datosEstado": listaEstados(data['idEstEle']),
                            'datosEmpleado': lista})

    except Cita.DoesNotExist:
        raise Http404("Cita no existe")

    return render(request, 'cimodificar.html', {"datos": "", "datosEstado": "",'datosEmpleado': ""})

"""
    METODOS AUXILIARES
"""
def actualizarStockProducto(producto):

    stock = Stock.objects.filter(producto=producto.id, proveedor=producto.proveedor.id)
    print("***",stock)
    if stock:#confirmamos que este
        for s in stock:
            instStock = Stock.objects.get(id=s.id)
            print("***", instStock.id,instStock.cantprov)

        prov = instStock.cantprov - 1
        instStock.cantprov = prov
        instStock.save()

        print("***", instStock.cantprov)
        """
        if prov < 5:
            enviarCorreo(producto,prov)
        """

def empleadosValidosNuevo(fecha,hora,duracion):

    emp = []
    queryCita = Cita.objects.filter(fecha=formatoDate(fecha))  # obtenemos las citas de ese dia

    if not queryCita:  # no hay citas ese dia => todos los empleados libres
        lista,ids = listaEmpleado("")
    else:

        aux = formatoTime(hora)
        auxHoraEntradaCita = aux.hour
        auxHoraSalidaCita = aux.hour + duracion

        for fila in queryCita:
            auxHoraEntradaEmp = formatoTime(fila.horarioentrada.hora).hour
            auxHoraSalidaEmp = formatoTime(fila.horariosalida.hora).hour

            #comprobamos si tiene mas tratamientos asociados  el empleado en ese dia
            queryEmpleado = Cita.objects.filter(fecha=formatoDate(fecha), empleado=fila.empleado)
            masCitas = False
            valido = True

            if queryEmpleado.count() > 1:
                valido = disponibilidad(queryEmpleado,auxHoraEntradaCita,auxHoraSalidaCita)
                masCitas = True

            if not masCitas:
                valido = esValidaCita(auxHoraEntradaCita,auxHoraSalidaCita,auxHoraEntradaEmp,auxHoraSalidaEmp)

            if not valido:
                emp.append(fila.empleado)

    return filtrarEmpleados(emp)

def empleadosValidosModificar(fecha,hora,duracion,emplSel):

    queryCita = Cita.objects.filter(fecha=formatoDate(fecha)) #obtenemos las citas de ese dia
    empleados = Empleado.objects.all()

    listaEmp = []

    aux = formatoTime(hora)
    auxHoraEntradaCita = aux.hour
    auxHoraSalidaCita = aux.hour + duracion

    for emp in empleados:

        enc = False

        for fila in queryCita:

            if emp.id == fila.empleado.id: #si no es el seleccionado y tiene cita

                enc = True
                auxHoraEntradaEmp = formatoTime(fila.horarioentrada.hora).hour
                auxHoraSalidaEmp = formatoTime(fila.horariosalida.hora).hour

                # comprobamos si tiene mas tratamientos asociados en ese dia
                queryEmpleado = Cita.objects.filter(fecha=formatoDate(fecha), empleado=fila.empleado)
                masCitas = False
                valido = True

                if queryEmpleado.count() > 1 and fila.empleado.id != emplSel:
                    valido = disponibilidad(queryEmpleado, auxHoraEntradaCita, auxHoraSalidaCita)
                    masCitas = True

                if not masCitas:
                    valido = esValidaCita(auxHoraEntradaCita, auxHoraSalidaCita, auxHoraEntradaEmp, auxHoraSalidaEmp)

                if valido and fila.empleado.id != emplSel:
                    data = {
                        "id": fila.empleado.id,
                        "nom": fila.empleado.nombre,
                    }
                    listaEmp.append(data)

        if not enc: #el empleado no tenia cita
            data = {
                "id": emp.id,
                "nom": emp.nombre,
            }
            listaEmp.append(data)

    return listaEmp

def esValidaCita(auxHoraEntradaCita,auxHoraSalidaCita,auxHoraEntradaEmp,auxHoraSalidaEmp):

    if auxHoraSalidaCita == auxHoraSalidaEmp and auxHoraEntradaCita == auxHoraEntradaEmp:
        return False
            #antes de la cita                     despues de la cita
    return auxHoraSalidaCita <= auxHoraEntradaEmp or auxHoraEntradaCita >= auxHoraSalidaEmp

def disponibilidad(queryEmpleado,auxHoraEntradaCita,auxHoraSalidaCita):

    cnt = 0
    valido = True

    for dato in queryEmpleado:
        auxHoraEntradaEmp = formatoTime(dato.horarioentrada.hora).hour
        auxHoraSalidaEmp = formatoTime(dato.horariosalida.hora).hour

        if not esValidaCita(auxHoraEntradaCita, auxHoraSalidaCita, auxHoraEntradaEmp, auxHoraSalidaEmp):
            cnt += 1

    if cnt > 0:
        valido = False

    return valido

def formatoTime(cadena):

    cad = cadena.split(':')
    h=int(cad[0])
    m=int(cad[1])
    s=int(cad[2])

    h = time(h, m, s)

    return h

def finHora(hora,duracion):

    hora = formatoTime(hora)
    auxHora = hora.hour + duracion
    newHora = time(auxHora, 0, 0)

    return newHora

def filtrarEmpleados(empleados):

    tipos = Empleado.objects.all()
    lista = []
    enc = False

    for tipo in tipos:
        for e in empleados:

            if tipo.id == e.id:
                enc = True

        if not enc:#no esta ocupado
            data = {
                "id": tipo.id,
                "nom": tipo.nombre,
            }
            lista.append(data)

        enc = False

    return lista

def formatoDate(fecha):

    d = datetime.datetime.strptime(fecha, '%d-%m-%Y').day
    m = datetime.datetime.strptime(fecha, '%d-%m-%Y').month
    y = datetime.datetime.strptime(fecha, '%d-%m-%Y').year

    return datetime.datetime(y, m, d).date()

def listaTratamiento():
   tipos = Tratamiento.objects.all();
   lista = []

   for tipo in tipos:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre.title(),
         }
         lista.append(data)

   return lista

def listaEmpleado(empleado):

   tipos = Empleado.objects.all();
   lista = []

   ids = []
   for tipo in tipos:
       if tipo.id != empleado:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)
         ids.append(tipo.id)

   return lista,ids

def listaHoras(duracion):

    lista=[]

    h = 9
    limite = 14 - duracion

    for i in range(0,limite):
        hora = time(h, 0, 0)
        h += 1
        data = {
            "id": str(hora),
            "nom": str(hora),
        }
        lista.append(data)

    return lista

def listaEstados(estado):

    tipos = Estadocita.objects.all();
    lista=[]

    for i in tipos:
        if i.id != estado:
            data = {
                "id": i.id,
                "nom": i.nombre.title(),
            }
            lista.append(data)

    return lista

def enviarEmailConfirmacion(cita):

    lista = []

    message = 'Estimado cliente, \n le recordamos que tiene una cita en la fecha ' + str(cita.fecha) + \
              ' a las ' + cita.horarioentrada.hora + ". \n Un saludo."

    email = EmailMessage('Recordatorio cita', message, to=[cita.cliente.email])
    email.send()

def enviarEmailCancelada(cita):
    lista = []

    message = 'Estimado cliente, \n le informamos de que la cita que tenia en la fecha ' + str(cita.fecha) + \
              ' a las ' + cita.horarioentrada.hora + " ha sido cancelada. \n Un saludo."

    email = EmailMessage('Recordatorio cita', message, to=[cita.cliente.email])
    email.send()
