from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from usuarios.models import Empleado, CustomUser
from .models import Horarioempleado, Tipohorarioempleado
from .forms import FormHorarioInsert, FormHorarioInsert2, fechaLunes, fechaDomingo, FormHorarioUpdate
import datetime
from django.contrib.auth.decorators import login_required

@login_required()
def nuevo(request):

    datos={}

    if request.method == "GET":
        form = FormHorarioInsert(request.GET)
        if form.is_valid():
            datos = form.cleaned_data

            empleado = datos.get("empleado")
            horario = datos.get("horario")
            inicio = datos.get("inicio")
            fin = datos.get("fin")

            inicio = formatoDate(str(inicio))
            fin = formatoDate(str(fin))

            valido = 0

            if not Horarioempleado.objects.filter(empleado=empleado):
                valido = 1
            elif not Horarioempleado.objects.filter(empleado=empleado,inicio=inicio):
                    valido = 1
            elif not Horarioempleado.objects.filter(empleado=empleado,inicio=inicio, tipohorarioempleado=4) or not \
                    Horarioempleado.objects.filter(empleado=empleado, inicio=inicio, tipohorarioempleado=3):
                #aunque ya tenga horario para esa semana le falta pr asignar el dia libre o el doblar
                    valido = 1
            else:
                messages.error(request, 'Ya tiene un horario para esta semana.')


            if valido == 1:
                user=CustomUser.objects.get(id=empleado)
                instEmpleado = Empleado.objects.get(user=user)
                instTipoHorario = Tipohorarioempleado.objects.get(id=horario)

                data = {
                    "ini": formatoDateString(str(inicio)),
                    "fin": formatoDateString(str(fin)),
                   # "idEmpEle": instEmpleado.id,
                   # "nomEmpEle": instEmpleado.nombre,
                    "idHorEle": instTipoHorario.id,
                    "nomHorEle": instTipoHorario.nombre.title(),
                }

                return render(request, 'hnuevo2.html', {"datos": data,'fechas':franjaFechas(),'completo':True})

    elif request.method == "POST":

            form = FormHorarioInsert2(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                #ver que no sean la misma fecha y si es --- no se inserta
                #hace falta hacer form de este

                # recogemos los datos
                empleado = datos.get("empleado")
                horario = datos.get("horario")
                inicio = datos.get("inicio")
                fin = datos.get("fin")
                libra = datos.get("libra")
                dobla = datos.get("dobla")

                #primer form
                inicio = formatoDate(str(inicio))
                fin = formatoDate(str(fin))

                instEmpleado = Empleado.objects.get(id=empleado)
                instTipoHorario1 = Tipohorarioempleado.objects.get(id=horario)

                data = {
                    "ini": formatoDateString(str(inicio)),
                    "fin": formatoDateString(str(fin)),
                    "idEmpEle": instEmpleado.id,
                    "nomEmpEle": instEmpleado.nombre,
                    "idHorEle": instTipoHorario1.id,
                    "nomHorEle": instTipoHorario1.nombre.title(),
                }

                #si las fechas son = o si ya tiene un doblar o un librar
                if not libra == "0" and not dobla == "0" and libra == dobla:
                    messages.error(request, 'No puede seleccionar el mismo día.')

                # segundo form
                if libra != "0":
                    libra = formatoDate(str(libra))

                if dobla != "0":
                    dobla = formatoDate(str(dobla))

                valido = 0

                #por si no asigno dia libre o doblado pero ya tengo turno
                if libra == "0" and dobla == "0" and Horarioempleado.objects.filter(empleado=empleado,inicio=inicio,fin=fin):
                    messages.error(request, 'Ya tiene un horario para esta semana.')
                    return render(request, 'hnuevo2.html', {"datos": data, 'fechas': franjaFechas(), 'completo': True})

                #si el mepledo no tenia horario no hay problema
                if (dobla == "0" and libra == "0") or (libra != "0" or dobla != "0")and \
                        not Horarioempleado.objects.filter(empleado=empleado):
                    valido = 1
                else:
                    #si le ponemos dia libre no tiene que coincidir en la misma fecha
                    if libra != "0" and not Horarioempleado.objects.filter(empleado=empleado,inicio=libra,tipohorarioempleado=3):
                        valido = 1
                    else:
                        # si le ponemos dia dobla no tiene que coincidir en la misma fecha
                        if dobla != "0" and not Horarioempleado.objects.filter(empleado=empleado,inicio=dobla,tipohorarioempleado=4):
                            valido = 1

                #es posible insertarlo
                if valido == 1:
                    #vemos si es de nuevas o ya estaba y solo añadimos el librar-doblar
                    if not Horarioempleado.objects.filter(empleado=empleado) or not Horarioempleado.objects.filter(empleado=empleado,inicio=inicio):
                            m = Horarioempleado(inicio=inicio,fin=fin,empleado=instEmpleado,tipohorarioempleado=instTipoHorario1)
                            m.save()

                    if libra != "0":
                        instLibra = Tipohorarioempleado.objects.get(nombre="Libra")
                        m = Horarioempleado(inicio=libra,fin=libra,empleado=instEmpleado,tipohorarioempleado=instLibra)
                        m.save()

                    if dobla != "0":
                        instDobla = Tipohorarioempleado.objects.get(nombre="Dobla")
                        m = Horarioempleado(inicio=dobla,fin=dobla,empleado=instEmpleado,tipohorarioempleado=instDobla)
                        m.save()

                    return HttpResponseRedirect("/horario/lista")

                else:
                    messages.error(request, 'Los campos no son correctos.')
                    return render(request, 'hnuevo2.html', {"datos": data, 'fechas': franjaFechas(), 'completo': True})

    inicio = fechaLunes()
    fin = fechaDomingo(inicio)

    inicio = formatoDateString(str(inicio))
    fin = formatoDateString(str(fin))

    return render(request, 'hnuevo.html', {'inicio':inicio, 'fin':fin,'datosEmp': listaEmpleados(""),
                           'datosTipo':listaTipoHorario(""),'completo':False})

@login_required()
def listar(request):
    datos = Horarioempleado.objects.all()
    lista = []

    for horario in datos:

        data = {
            "id": horario.id,
            "ini": formatoDateString(str(horario.inicio)),
            "fin": formatoDateString(str(horario.fin)),
            "emp": horario.empleado.nombre.title(),
            "tipo": horario.tipohorarioempleado.nombre.title(),
        }
        lista.append(data)

    return render(request, 'hlista.html', {"lista": lista})

@login_required()
def eliminar(request,pk ):
    try:
        hor = Horarioempleado.objects.get(id=pk)
        hor.delete()
    except Horarioempleado.DoesNotExist:
        raise Http404("El horario no existe")

    return HttpResponseRedirect("/horario/lista")

@login_required()
def modificar(request,pk):
    try:
        horario = Horarioempleado.objects.get(id=pk)

        if request.method == "POST":
            form = FormHorarioUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                hor = datos.get("horario")
                inicio = datos.get("inicio")
                fin = datos.get("fin")

                instTipoHorario = Tipohorarioempleado.objects.get(id=hor)

                inicio = formatoDate(inicio)
                fin = formatoDate(fin)

                if fin > inicio:
                    messages.error(request, "Las fechas no son correctas.")
                else:
                    # actualizamos datos
                    horario.tipohorarioempleado = instTipoHorario
                    horario.inicio=inicio
                    horario.fin=fin
                    horario.save()

                    return HttpResponseRedirect("/horario/lista")

        elif request.method == "GET":

            data = {
                "id": horario.id,
                "ini": formatoDateString(str(horario.inicio)),
                "fin": formatoDateString(str(horario.fin)),
                "dniEmpEle": horario.empleado.dni,
                "nomEmpEle": horario.empleado.nombre.title(),
                "idHorEle": horario.tipohorarioempleado.id,
                "nomHorEle": horario.tipohorarioempleado.nombre.title(),
            }

            datosTipo= listaTipoHorario(data["nomHorEle"])

            return render(request, 'hmodificar.html', {"datos": data, "datosTipo": datosTipo})

    except Horarioempleado.DoesNotExist:
        raise Http404("El horario no existe")

    return HttpResponseRedirect('/horario/' + str(pk) + '/modificar')

@login_required()
def horario(request):

    lunes = fechaLunes()

    dias = []
    diaActual = lunes
    nom = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    for i in range(0, 7):

        data = {
            "dia": nom[i],
            "num": diaActual.day,
        }

        dias.append(data)

        diaSig = datetime.timedelta(days=1)
        diaActual += diaSig

    # obtenemos los turnos de esta semana
        listaMayana = Horarioempleado.objects.filter(inicio=lunes, tipohorarioempleado=1)
    turnoTarde = Horarioempleado.objects.filter(inicio=lunes, tipohorarioempleado=2)

    #lista con turnos mañana y tarde
    listaMayana=listaDeTurnos(listaMayana)
    listaTarde = listaDeTurnos(turnoTarde)

    #filtros de turnos libres
    listaMayana = listaDeTurnosLibra(listaMayana,lunes)
    listaTarde = listaDeTurnosLibra(listaTarde,lunes)

    #filtros de turnos dobles
    listaMayana = listaDeTurnosDoble(listaMayana,lunes,2)
    listaTarde = listaDeTurnosDoble(listaTarde, lunes, 1)

    inicio = lunes.day
    dia = datetime.timedelta(days=6)
    fin = (lunes + dia).day
    mes = nombreMes(lunes.month)

    return render(request, 'calendar.html', {"inicio":str(inicio),"fin":str(fin),"mes":mes,
            "dias":dias,"n":7,"mañana":listaMayana,"tarde": listaTarde ,"cnt":'0'})

"""
    AUXILIARES
"""
def nombreMes(mes):
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
             'Octubre','Noviembre','Diciembre']

    return meses[mes-1]

def listaDeTurnos(filas):

    lista = []

    for emp in filas:

        semana =[]
        for i in range(0, 7):

            data = {
                "id": emp.empleado.id,
                "nom": emp.empleado.nombre,
                "idx": i,
            }

            semana.append(data)

        lista.append(semana)

    return lista

def listaDeTurnosLibra(listaTurno,lunes):

    listaFinal = []

    #todos los empleados de mañana
    for lista in listaTurno:

        diaActual = lunes

        for data in lista:#los 7 dias de un empleado

            #obtenemos si el dia que toca (de los siete libra)
            aux = Horarioempleado.objects.filter(inicio=diaActual, empleado=data["id"],tipohorarioempleado=3)

            if aux:
                data["id"] = False
                data["nom"] = -1
                data["idx"] = -1

            dia = datetime.timedelta(days=1)
            diaActual += dia

        listaFinal.append(lista)

    return listaFinal

def listaDeTurnosDoble(listaTurno,lunes,id):

    dataNull = {
        "id": False,
        "nom": -1,
        "idx": -1,
    }

    turnoElegido = Horarioempleado.objects.filter(inicio=lunes, tipohorarioempleado=id)

    #todos los empleados de mañana
    for dobla in turnoElegido:

        diaActual = lunes
        lista = []
        i = 0
        enc = 0

        for i in range(0, 7):#comprobamos los 7 dias

            #obtenemos si el dia que toca (de los siete libra)
            aux = Horarioempleado.objects.filter(inicio=diaActual, empleado=dobla.empleado,tipohorarioempleado=4)

            if aux:
                enc = 1
                data = {
                    "id": dobla.empleado.id,
                    "nom": dobla.empleado.nombre,
                    "idx": i,
                }
                lista.append(data)
            else:
                lista.append(dataNull)

            dia = datetime.timedelta(days=1)
            diaActual += dia
            i += 1

        if enc == 1:
            listaTurno.append(lista)

    return listaTurno

def listaEmpleados(nombre):


   empleado = CustomUser.objects.filter(is_staff=True, is_superuser=False)
   lista = []

   for emp in empleado:

       data = {
           "id": emp.id,
           "nom": emp.first_name,
        }
       lista.append(data)

   return lista

def listaTipoHorario(nombre):

    tipos = Tipohorarioempleado.objects.all()
    lista = []

    for tipo in tipos:
        if not (str(tipo.nombre).title() == "Dobla" or str(tipo.nombre).title() == "Libra"):
            data = {
                "id": tipo.id,
                "nom": str(tipo.nombre).title(),
            }
            lista.append(data)

    return lista

def formatoDateString(fecha):

    #en la bbdd se guarda yyyy-mm-dd cambiamso para que sea dd-mm-yyy
    cad = fecha.split('-')
    cad = cad[2] + '-' + cad[1] + '-' + cad[0]

    return cad

def formatoDate(fecha):

    fecha =formatoDateString(fecha)
    d = datetime.datetime.strptime(fecha, '%d-%m-%Y').day
    m = datetime.datetime.strptime(fecha, '%d-%m-%Y').month
    y = datetime.datetime.strptime(fecha, '%d-%m-%Y').year

    return datetime.datetime(y, m, d).date()

def franjaFechas():

    lista=[]
    f1 = fechaLunes()

    data = {
        "id": 0,
        "nom": "---",
    }

    lista.append(data)

    for i in range(0,6):

        fec = str(f1)
        idFec = fec # para guardalo en el id con fomrato yyyy-mm-dd
        cad = fec.split('-')
        fec = cad[2] + '-' + cad[1] + '-' + cad[0]

        data = {
            "id": idFec,
            "nom": fec,
        }

        dia = datetime.timedelta(days=1)
        f1 = f1 + dia

        lista.append(data)

    return lista
