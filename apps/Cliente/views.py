from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from apps.Cliente.models import Cliente
from .forms import *
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.utils import timezone
from datetime import datetime
import MySQLdb
import re
from django.db import connection

# Create your views here.

def registro(request):

    # si es una peticion post
    if request.method == "POST":
        form = FormClienteInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            #recogemos los datos
            dni = datos.get("dni")
            nom = datos.get("nombre")
            ape = datos.get("apellidos")
            dir = datos.get("direccion")
            tlf = datos.get("telefono")
            email = datos.get("email")
            password = datos.get("password")

            #comprobamos dni
            if len(dni) == 9:
                numeros = dni[0:8]
                letra = dni[8:9]

                if not numeros.isdigit() and letra.isalpha():
                    messages.error(request, 'El Dni no es correcto.')
            else:
                messages.error(request, 'El Dni no es correcto.')

            #comprobamos el telefono
            if not (len(tlf) == 9 and tlf.isdigit()):
                messages.error(request, 'El telefono no es correcto.')

            elif not existClienteDni(dni):
                if not clienteRegistradoEmail(email):  # comprobamos si ya existe ese empleado

                    # insertamso cliente
                    c = Cliente(dni=dni, nombre=nom, apellidos=ape, direccion=dir, telefono=tlf, email=email,
                                puntuacion=0, password=password)
                    c.save()

                    # si el evento post ha sido correcot
                    return HttpResponseRedirect("/apps/index")
                else:
                    messages.error(request, 'El cliente ya existe.')
            else:
                messages.error(request, 'El cliente ya existe.')

    else:
        form = FormClienteInsert()

    #lo que lanza si no hemso dado al boton y crea el evento post
    return render(request, 'alta.html', {'form': form, 'elem':"cliente"})

def login(request):
    # si es una peticion post
    if request.method == "POST":
        form = FormClienteLogin(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            #recogemos los datos
            email = datos.get("email")
            password = datos.get("password")

        if clienteRegistradoEmail(email):
            if emailContraseña(email, password):
                request.session["session_key"] = email
                f = timezone.now().date()
                #request.session["expire_date"] = str(f)
                return HttpResponseRedirect("/apps/index")
            else:
                messages.error(request, "Usuario y contraseña no coinciden.")
        else:
            messages.error(request, "Usuario y contraseña no coinciden.")
    else:
        form = FormClienteLogin()

    #lo que lanza si no hemos dado al boton y crea el evento post
    return render(request, 'loginCli.html', {'form': form})

def baja(request):
    if request.method == "POST":
        form = FormClienteDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")

            if existClienteDni(dni):

                #print("*********",Session.objects.all())
                #print("*********", Session.objects.all())

                #del request.session['session_key']
                #request.session.modified = True

                id = idPorDni(dni)
                Cliente.objects.filter(id=id).delete()
                return HttpResponseRedirect("/apps/index")
            else:
                messages.error(request, "El cliente no existe.")
    else:
        form = FormClienteDelete()

    return render(request, 'borrar.html', {'form': form, 'elem':"cliente"})

def modificar(request):

    # si es una peticion post
    if request.method == "POST":
        form = FormClienteUpdate(request.POST)
        dni = request.GET.get("dni") #obtenemos el dni que hemos buscado

        print("*****",form)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
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
                antiClie = Cliente.objects.get(id=id)

                # actualizamos datos
                antiClie.nombre = nom
                antiClie.apellidos = ape
                antiClie.email = email
                antiClie.direccion = dir
                antiClie.telefono = tlf
                antiClie.password = password
                antiClie.save()

                #session_key = request.session["session_key"]
                #print("**********",session_key)#me da el email, lo que hemos guardado en la sesion

                # si el evento post ha sido correcot
                return HttpResponseRedirect("/apps/index")

    #peticion GET
    formDni = FormClienteDelete()
    if 'dni' in request.GET:
        query = request.GET['dni'] #query tiene le valor del dni
        dni = str(query)

        if existClienteDni(dni):

            id = idPorDni(dni)
            datos = Cliente.objects.get(id=id)

            data = {
                "nom": datos.nombre,
                "ape": datos.apellidos,
                "dir": datos.direccion,
                "tlf": datos.telefono,
                "email": datos.email,
                "cnt": datos.password,
            }

            #lo que lanza si no hemos dado al boton y crea el evento post
            return render(request, 'modCli.html', {"formDni": formDni, "buscado": True, "datos": data})

        else: #si es error vuelve a lanzar la pagina
            messages.error(request, "El cliente no existe.")
            return HttpResponseRedirect("/apps/modificarCliente")

    # primera vista
    formDni = FormClienteDelete()
    return render(request, 'modCli.html', {"formDni": formDni, "buscado": False})

def listar(request):

  datosFinales = datosClientes()
  return render(request, 'listarClientes.html',{"datos":datosFinales})

def logout(request):
    #print("*********",Session.objects.all())
    #Session.objects.get(session_key='dsvlkup0w8w7ws7o1q35njxtfvhh6elg').delete()

    try:
        del request.session['session_key']
        #diferencias con la sesion si es cliente o empleado y lanzar loginCliente o loginEmpeado
        return HttpResponseRedirect("/apps/loginCliente")
    except KeyError:
        return HttpResponse("Error, no estás logeado.")

"""
    METODOS AUXILIARES
"""
def emailContraseña(email,password):
    cursor = connection.cursor()
    query = "SELECT * FROM Cliente WHERE email =  %(email)s and password = %(password)s"
    cursor.execute(query, {'email': email, 'password': password})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def clienteRegistradoEmail(email):
    cursor = connection.cursor()
    query = "SELECT * FROM cliente WHERE email =  %(email)s"
    cursor.execute(query, {'email': email})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def existClienteDni(dni):
    cursor = connection.cursor()
    query = "SELECT * FROM Cliente WHERE dni =  %(dni)s"
    cursor.execute(query, {'dni': dni})
    datosEmpleado = cursor.fetchall()

    return datosEmpleado

def idPorDni(dni):
    cursor = connection.cursor()
    query = "SELECT id FROM Cliente WHERE dni =  %(dni)s"
    cursor.execute(query, {'dni': dni})
    empleado = cursor.fetchall()

    cad = str(empleado[0])
    cad = cad[1:len(cad) - 2]

    return cad

def datosClientes():
    cursor = connection.cursor()
    query = "select * from Cliente"
    cursor.execute(query)
    datosClientes = cursor.fetchall()

    datosFinales = []

    if datosClientes:

        for cli in datosClientes:

            data = {
                "dni": cli[1],
                "nom": cli[2],
                "ape": cli[3],
                "email": cli[4],
                "dir": cli[5],
                "tlf": cli[6],
            }

            datosFinales.append(data)

    return datosFinales

def existClienteDni(dni):
    cursor = connection.cursor()
    query = "SELECT * FROM Cliente WHERE dni =  %(dni)s"
    cursor.execute(query, {'dni': dni})
    datosCliente = cursor.fetchall()

    return datosCliente
