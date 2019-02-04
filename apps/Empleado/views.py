from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from apps.Empleado.models import Empleado,Tipoempleado
from .forms import *
from django.contrib import messages
import MySQLdb
import re
from django.db import connection

# Create your views here.

def login(request):
 # si es una peticion post
    if request.method == "POST":
        form = FormEmpleadoLogin(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            #recogemos los datos
            email = datos.get("email")
            password = datos.get("password")

            if empleadoRegistradoEmail(email):
                if emailContraseña(email,password):
                    request.session["session_key"] = email
                    return HttpResponseRedirect("/apps/index")
                else:
                    messages.error(request, "Usuario y contraseña no coinciden.")
            else:
                messages.error(request, "Usuario y contraseña no coinciden.")

    else:
        form = FormEmpleadoLogin()

    #lo que lanza si no hemso dado al boton y crea el evento post
    return render(request, 'loginEmpleado.html', {'form': form})

def alta(request):

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

            elif not existEmpleadoDni(dni):
                if not empleadoRegistradoEmail(email):  # comprobamos si ya existe ese empleado

                    id = idTipoEmpleadoPorNom(tipo)
                    instTipoEmpleado = Tipoempleado.objects.get(id=id)

                    e = Empleado(dni=dni, codigo=cod, nombre=nom, apellidos=ape,email=email,
                                 direccion=dir,telefono=tlf,tipoempleado=instTipoEmpleado, password=password)
                    e.save()
                    return HttpResponseRedirect("/apps/index")
                else:
                    messages.error(request, 'El empleado ya existe.')
            else:
                messages.error(request, 'El empleado ya existe.')

    else:
        form = FormEmpleadoInsert()

    return render(request, 'alta.html', {'form': form, 'elem': "empleado"})

def baja(request):

    if request.method == "POST":
        form = FormEmpleadoDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")

            if existEmpleadoDni(dni):
                Empleado.objects.filter(dni=dni).delete()
                return HttpResponseRedirect("/apps/index")
            else:
                messages.error(request, "El empleado no existe.")
        else:
            form = FormEmpleadoDelete()
    else:
        form = FormEmpleadoDelete()

    return render(request, 'borrar.html', {'form': form, 'elem':"empleado"})

def modificar(request):

    if request.method == "POST":
        form = FormEmpleadoUpdate(request.POST)
        dni = request.GET.get("dni") #obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            tipo = datos.get("Tipo")
            nom = datos.get("nombre")
            ape = datos.get("apellidos")
            email = datos.get("email")
            dir = datos.get("direccion")
            tlf = datos.get("telefono")
            password = datos.get("password")

            # comprobamos el telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')
            else:

                id = idPorDni(dni)
                antiEmple = Empleado.objects.get(id=id)

                id = idTipoEmpleadoPorNom(tipo)
                instTipoEmpleado = Tipoempleado.objects.get(id=id)

                #actualizamos datos
                antiEmple.nombre = nom
                antiEmple.apellidos = ape
                antiEmple.email = email
                antiEmple.direccion = dir
                antiEmple.telefono = tlf
                antiEmple.tipoempleado = instTipoEmpleado
                antiEmple.password = password
                antiEmple.save()

                return HttpResponseRedirect("/apps/index")

    # peticion GET
    formId = FormEmpleadoDelete()
    if 'dni' in request.GET:
        query = request.GET['dni']  # query tiene le valor del dni

        dni = str(query)

        if existEmpleadoDni(dni):

            id = idPorDni(dni)
            datos = Empleado.objects.get(id=id)

            data = {
                "nom": datos.nombre,
                "ape": datos.apellidos,
                "email": datos.email,
                "dir": datos.direccion,
                "tlf": datos.telefono,
                "nomTipoEle": str(datos.tipoempleado.nombre).title(),#tipoEmpleadoId(datos.tipoempleado),
                "pass": datos.password,
            }

            datosTipos = listaTiposEmpleado(data["nomTipoEle"])

            # lo que lanza si no hemos dado al boton y crea el evento post
            return render(request, 'modEmp.html', {"formId": formId, "buscado": True,
                        "datos": data, "datosTipos": datosTipos})

        else: #si es error vuelve a lanzar la pagina
            messages.error(request, "El empleado no existe.")
            return HttpResponseRedirect("/apps/modificarEmpleado")

    # primera vista
    formDni = FormEmpleadoDelete()
    return render(request, 'modEmp.html', {"formDni": formDni, "buscado": False})

def listar(request):

  datosFinales = datosEmpleados()
  return render(request, 'listarEmpleados.html',{"datos":datosFinales})

def logout(request):
    #print("*********",Session.objects.all())
    #Session.objects.get(session_key='dsvlkup0w8w7ws7o1q35njxtfvhh6elg').delete()

    try:
        del request.session['session_key']
        return HttpResponseRedirect("/apps/loginEmpleado")
    except KeyError:
        return HttpResponse("Error, no estás logeado.")

"""
    METODOS AUXILIARES
"""

def empleadoRegistradoEmail(email):
    cursor = connection.cursor()
    query = "SELECT * FROM Empleado WHERE email =  %(email)s"
    cursor.execute(query, {'email': email})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def emailContraseña(email,password):
    cursor = connection.cursor()
    query = "SELECT * FROM Empleado WHERE email =  %(email)s and password = %(password)s"
    cursor.execute(query, {'email': email, 'password': password})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def existEmpleadoDni(dni):
    cursor = connection.cursor()
    query = "SELECT * FROM Empleado WHERE dni =  %(dni)s"
    cursor.execute(query, {'dni': dni})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def idTipoEmpleadoPorNom(nombre):
    cursor = connection.cursor()
    query = "SELECT id FROM tipoEmpleado WHERE nombre =  %(nombre)s"
    cursor.execute(query, {'nombre': nombre})
    tipo = cursor.fetchall()

    cad = str(tipo)
    cad = cad[2:len(cad)-3]

    return cad

def datosEmpleados():
    cursor = connection.cursor()
    query = "select * from Empleado"
    cursor.execute(query)
    datosEmpleados = cursor.fetchall()

    datosFinales = []

    if datosEmpleados:

        for emp in datosEmpleados:

            instTipoEmpleado = Tipoempleado.objects.get(id=emp[8])

            data = {
                "dni": emp[1],
                "cod": emp[2],
                "nom": emp[3],
                "ape": emp[4],
                "email": emp[5],
                "dir": emp[6],
                "tlf": emp[7],
                "tipo": instTipoEmpleado.nombre.title(),
            }

            datosFinales.append(data)

    return datosFinales

def dniPorEmail(email):
    cursor = connection.cursor()
    query = "SELECT * FROM Empleado WHERE email =  %(email)s"
    cursor.execute(query, {'email': email})
    empleado = cursor.fetchall()

    cad = str(empleado[0])
    cad = cad[1:len(cad) - 1]  # paraentesis del principio y final
    cad = cad.split(",")

    return cad[0][1:len(cad)]

def idPorDni(dni):
    cursor = connection.cursor()
    query = "SELECT id FROM Empleado WHERE dni =  %(dni)s"
    cursor.execute(query, {'dni': dni})
    empleado = cursor.fetchall()

    cad = str(empleado[0])
    cad = cad[1:len(cad) - 2]

    return cad

def listaTiposEmpleado(nombre):

    cursor = connection.cursor()
    query = "select * from tipoEmpleado"
    cursor.execute(query)
    datos = cursor.fetchall()

    #quitamos los []
    campos = str(datos)
    campos = campos[1:len(campos)-1]

    id = 1;
    cadSplit = campos.split(",")
    lista = []

    for x in cadSplit:
        if id == 0:
            cad = x[2:len(x)-2] #obtenemos el nombre
            nom = str(cad).title()
            if nom != nombre:
                lista.append(nom) #lo guardamos
            id += 1
        else:
            id -= 1

    return lista



