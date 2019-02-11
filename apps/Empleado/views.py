from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from apps.Empleado.models import Empleado,Tipoempleado
from .forms import *
from django.contrib import messages
import MySQLdb
import re
from django.db import connection
from django.utils import timezone

# Create your views here.

def login(request):

    if request.method == "POST":
        form = FormEmpleadoLogin(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            email = datos.get("email")
            password = datos.get("password")

        if Empleado.objects.filter(email=email):
            emp = Empleado.objects.get(email=email)
            if emp.password == password:
                request.session["session_key"] = email
                f = timezone.now().date()
                request.session["expire_date"] = str(f)

                encargado, basico = comprobarSesion(request)
                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
            else:
                messages.error(request, "Usuario y contraseña no coinciden.")
        else:
            messages.error(request, "Usuario no coincide")

    else:
        form = FormEmpleadoLogin()

    #lo que lanza si no hemso dado al boton y crea el evento post
    return render(request, 'loginEmpleado.html', {'form': form})

def alta(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormEmpleadoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")
            cod = datos.get("codigo")
            nom = datos.get("nombre")
            ape = datos.get("apellidos")
            email = datos.get("email")
            dir = datos.get("direccion")
            tlf = datos.get("telefono")
            tipo = datos.get("Tipo")
            password = datos.get("password")

            # comprobamos dni
            if len(dni) == 9:
                numeros = dni[0:8]
                letra = dni[8:9]

                if not numeros.isdigit() and letra.isalpha():
                    messages.error(request, 'El Dni no es correcto.')
            else:
                messages.error(request, 'El Dni no es correcto.')

            #comprobamso telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')
                messages.error(request, '')

            elif not Empleado.objects.filter(dni=dni).exists():
                if not Empleado.objects.filter(email=email).exists():  # comprobamos si ya existe ese empleado

                    instTipoEmpleado = Tipoempleado.objects.get(nombre=tipo)

                    e = Empleado(dni=dni, codigo=cod, nombre=nom, apellidos=ape,email=email,
                                 direccion=dir,telefono=tlf,tipoempleado=instTipoEmpleado, password=password)
                    e.save()


                    return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})
                else:
                    messages.error(request, 'El empleado ya existe.')
            else:
                messages.error(request, 'El empleado ya existe.')

    else:
        form = FormEmpleadoInsert()

    return render(request, 'alta.html', {'form': form, 'elem': "empleado", 'cliente': False,
                'encargado': encargado, 'Basico': basico})

def baja(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormEmpleadoDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")

            if Empleado.objects.filter(dni=dni).exists():
                Empleado.objects.filter(dni=dni).delete()
                return HttpResponseRedirect("/apps/index")
            else:
                messages.error(request, "El empleado no existe.")
        else:
            form = FormEmpleadoDelete()
    else:
        form = FormEmpleadoDelete()

    return render(request, 'borrar.html', {'form': form, 'elem':"empleado", 'cliente': False,
                'encargado': encargado, 'Basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormEmpleadoUpdate(request.POST)
        dni = request.GET.get("dni") #obtenemos el dni que hemos buscado

        if form.is_valid():
            emp = form.cleaned_data

            # recogemos los datos
            tipo = emp.get("Tipo")
            nom = emp.get("nombre")
            ape = emp.get("apellidos")
            email = emp.get("email")
            dir = emp.get("direccion")
            tlf = emp.get("telefono")
            password = emp.get("password")

            # comprobamos el telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')
            else:

                antiEmple = Empleado.objects.get(email=email)
                instTipoEmpleado = Tipoempleado.objects.get(nombre=tipo)

                #actualizamos datos
                antiEmple.nombre = nom
                antiEmple.apellidos = ape
                antiEmple.email = email
                antiEmple.direccion = dir
                antiEmple.telefono = tlf
                antiEmple.tipoempleado = instTipoEmpleado
                antiEmple.password = password
                antiEmple.save()

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'Basico': basico})

    # peticion GET
    formId = FormEmpleadoDelete()
    if 'dni' in request.GET:
        query = request.GET['dni']  # query tiene le valor del dni

        dni = str(query)

        if Empleado.objects.filter(dni=dni):

            emp = Empleado.objects.get(dni=dni)

            data = {
                "nom": emp.nombre,
                "ape": emp.apellidos,
                "email": emp.email,
                "dir": emp.direccion,
                "tlf": emp.telefono,
                "nomTipoEle": str(emp.tipoempleado.nombre).title(),#tipoEmpleadoId(datos.tipoempleado),
                "pass": emp.password,
            }

            datosTipos = listaTiposEmpleado(data["nomTipoEle"])

            return render(request, 'modEmp.html', {"formId": formId, "buscado": True,"datos": data,
                    "datosTipos": datosTipos,'cliente': False,'encargado': encargado, 'Basico': basico})

        else: #si es error vuelve a lanzar la pagina
            messages.error(request, "El empleado no existe.")
            return HttpResponseRedirect("/apps/modificarEmpleado")

    # primera vista
    formDni = FormEmpleadoDelete()

    return render(request, 'modEmp.html', {"formDni": formDni, "buscado": False,'cliente': False,
                'encargado': encargado, 'Basico': basico})

def listar(request):

  datosFinales = datosEmpleados()
  encargado, basico = comprobarSesion(request)

  return render(request, 'listarEmpleados.html',{"datos":datosFinales, 'cliente': False,
        'encargado': encargado, 'Basico': basico})

def datosEmpleado(request):

    email = request.session["session_key"]  # me da el email, lo que hemos guardado en la sesion
    emp = Empleado.objects.get(email=email)

    data = {
        "dni": emp.dni,
        "cod": emp.codigo,
        "tipo": emp.tipoempleado.nombre,
        "nom": emp.nombre,
        "ape": emp.apellidos,
        "email": emp.email,
        "dir": emp.direccion,
        "tlf": emp.telefono,
        "cnt": emp.password,
    }

    encargado,basico = comprobarSesion(request)

    return render(request, 'inforEmp.html', {"datos": data,'cliente': False,
        'encargado': encargado, 'Basico': basico})


def logout(request):

    # print("*********",Session.objects.all())
    # Session.objects.get(session_key='dsvlkup0w8w7ws7o1q35njxtfvhh6elg').delete()

    try:

        email = request.session["session_key"]
        del request.session['session_key']

        if not Empleado.objects.filter(email=email):
            return HttpResponseRedirect("/apps/loginCliente")
        else:
            return HttpResponseRedirect("/apps/loginEmpleado")

        # diferencias con la sesion si es cliente o empleado y lanzar loginCliente o loginEmpeado

    except KeyError:
        return HttpResponse("Error, no estás logeado.")

"""
    METODOS AUXILIARES
"""

def comprobarSesion(request):
    email = request.session["session_key"]
    emp = Empleado.objects.get(email=email)

    if emp.tipoempleado.nombre == 'encargado':
        encargado = True
        basico = False
    else:
        encargado = False
        basico = True

    return encargado, basico;

def datosEmpleados():

    datos = Empleado.objects.all();
    datosFinales = []

    for emp in datos:

        instTipoEmpleado = Tipoempleado.objects.get(id=emp.tipoempleado.id)

        data = {
            "dni": emp.dni,
            "cod": emp.codigo,
            "nom": emp.nombre,
            "ape": emp.apellidos,
            "email": emp.email,
            "dir": emp.direccion,
            "tlf": emp.telefono,
            "tipo": instTipoEmpleado.nombre.title(),
        }

        datosFinales.append(data)

    return datosFinales

def listaTiposEmpleado(nombre):

    tipos = Tipoempleado.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        if nom != nombre:
            lista.append(nom)

    return lista



