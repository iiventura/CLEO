from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from apps.Cliente.models import Cliente
from apps.Empleado.views import comprobarSesion
from .forms import *
from django.contrib import messages
from django.utils import timezone

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

            elif not Cliente.objects.filter(dni=dni).exists():
                if not Cliente.objects.filter(email=email).exists():
                    # insertamos cliente
                    c = Cliente(dni=dni, nombre=nom, apellidos=ape, direccion=dir, telefono=tlf, email=email,
                                puntuacion=0, password=password)
                    c.save()

                    return HttpResponseRedirect("/apps/loginCliente")
                else:
                    messages.error(request, 'El cliente ya existe.')
            else:
                messages.error(request, 'El cliente ya existe.')

    else:
        form = FormClienteInsert()

    #lo que lanza si no hemso dado al boton y crea el evento post
    return render(request, 'registro.html', {'form': form})

def modificarMisDatosCliente(request):

    email = request.session["session_key"]
    cli = Cliente.objects.get(email=email)

    # si es una peticion post
    if request.method == "POST":
        form = FormClienteUpdate(request.POST)
        dni = request.GET.get("dni")  # obtenemos el dni que hemos buscado

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")
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

                antiClie = Cliente.objects.get(email=email)

                # actualizamos datos
                antiClie.nombre = nom
                antiClie.apellidos = ape
                antiClie.email = email
                antiClie.direccion = dir
                antiClie.telefono = tlf
                antiClie.password = password
                antiClie.save()

                # si el evento post ha sido correcot
                return render(request, 'index.html', {'cliente': True, 'encargado': False, 'basico': False})

    # peticion GET
    else:

        data = {
            "dni": cli.dni,
            "nom": cli.nombre,
            "ape": cli.apellidos,
            "dir": cli.direccion,
            "tlf": cli.telefono,
            "email": cli.email,
            "cnt": cli.password,
        }

    return render(request, 'modDatoCli.html', {"datos": data, 'cliente': True, 'encargado': False, 'basico': False})


def alta(request):

    encargado, basico = comprobarSesion(request)
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

            elif not Cliente.objects.filter(dni=dni).exists():
                if not Cliente.objects.filter(email=email).exists():
                    # insertamso cliente
                    c = Cliente(dni=dni, nombre=nom, apellidos=ape, direccion=dir, telefono=tlf, email=email,
                                puntuacion=0, password=password)
                    c.save()

                    return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
                else:
                    messages.error(request, 'El cliente ya existe.')
            else:
                messages.error(request, 'El cliente ya existe.')

    else:
        form = FormClienteInsert()

    #lo que lanza si no hemso dado al boton y crea el evento post
    return render(request, 'alta.html', {'form': form, 'elem':"cliente",'cliente': False,
        'encargado': encargado, 'basico': basico})

def login(request):

    # si es una peticion post
    if request.method == "POST":
        form = FormClienteLogin(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            #recogemos los datos
            email = datos.get("email")
            password = datos.get("password")

        if Cliente.objects.filter(email=email):
            cli = Cliente.objects.get(email=email)
            if cli.password == password:
                request.session["session_key"] = email
                f = timezone.now().date()
                request.session["expire_date"] = str(f)

                #session_key = request.session["session_key"] #me da el email, lo que hemos guardado en la sesion

                return render(request,'index.html',{'cliente':True, 'encargado':False, 'basico':False})
            else:
                messages.error(request, "Usuario y contraseña no coinciden.")
        else:
            messages.error(request, "Usuario no coincide.")
    else:
        form = FormClienteLogin()

    #lo que lanza si no hemos dado al boton y crea el evento post
    return render(request, 'loginCli.html', {'form': form})

def baja(request):
    encargado, basico = comprobarSesion(request)
    if request.method == "POST":
        form = FormClienteDelete(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            dni = datos.get("dni")

            if Cliente.objects.filter(dni=dni).exists():
                Cliente.objects.filter(dni=dni).delete()

                #print("*********",Session.objects.all())
                #print("*********", Session.objects.all())

                #del request.session['session_key']
                #request.session.modified = True

                return render(request, 'index.html', {'cliente': False, 'encargado': encargado, 'basico': basico})
            else:
                messages.error(request, "El cliente no existe.")
    else:
        form = FormClienteDelete()

    return render(request, 'borrar.html', {'form': form, 'elem':"cliente",'cliente': False,
            'encargado': encargado, 'basico': basico})

def modificar(request):
    encargado, basico = comprobarSesion(request)
    # si es una peticion post
    if request.method == "POST":
        form = FormClienteUpdate(request.POST)
        dni = request.GET.get("dni") #obtenemos el dni que hemos buscado

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

                antiClie = Cliente.objects.get(email=email)

                # actualizamos datos
                antiClie.nombre = nom
                antiClie.apellidos = ape
                antiClie.email = email
                antiClie.direccion = dir
                antiClie.telefono = tlf
                antiClie.password = password
                antiClie.save()

                # si el evento post ha sido correcot
                return render(request, 'index.html', {'cliente': False,'encargado': encargado, 'basico': basico})

    #peticion GET
    formDni = FormClienteDelete()
    if 'dni' in request.GET:
        query = request.GET['dni'] #query tiene le valor del dni
        dni = str(query)

        if Cliente.objects.filter(dni=dni):

            cli = Cliente.objects.get(dni=dni)
            data = {
                "nom": cli.nombre,
                "ape": cli.apellidos,
                "dir": cli.direccion,
                "tlf": cli.telefono,
                "email": cli.email,
                "cnt": cli.password,
            }

            return render(request, 'modCli.html', {"formDni": formDni, "buscado": True, "datos": data,
                        'cliente': False,'encargado': encargado, 'basico': basico})

        else: #si es error vuelve a lanzar la pagina
            messages.error(request, "El cliente no existe.")
            return HttpResponseRedirect("/apps/modificarCliente")

    # primera vista
    formDni = FormClienteDelete()

    return render(request, 'modCli.html', {"formDni": formDni, "buscado": False,
            'cliente': False,'encargado': encargado, 'basico': basico})


def datosClienteEmp(request):
    encargado, basico = comprobarSesion(request)

    #peticion GET
    formDni = FormClienteDelete()
    if 'dni' in request.GET:
        query = request.GET['dni'] #query tiene le valor del dni
        dni = str(query)

        if Cliente.objects.filter(dni=dni):

            cli = Cliente.objects.get(dni=dni)
            data = {
                "nom": cli.nombre,
                "ape": cli.apellidos,
                "dir": cli.direccion,
                "tlf": cli.telefono,
                "email": cli.email,
            }

            return render(request, 'inforCliEmp.html', {"formDni": formDni, "buscado": True, "datos": data,
                        'cliente': False,'encargado': encargado, 'basico': basico})

        else: #si es error vuelve a lanzar la pagina
            messages.error(request, "El cliente no existe.")
            return HttpResponseRedirect("/apps/datosClienteEmp")

    # primera vista
    formDni = FormClienteDelete()

    return render(request, 'inforCliEmp.html', {"formDni": formDni, "buscado": False,
            'cliente': False,'encargado': encargado, 'basico': basico})

def listar(request):

  datosFinales = datosClientes()
  encargado, basico = comprobarSesion(request)

  return render(request, 'listarClientes.html',{"datos":datosFinales,
        'cliente': False,'encargado': encargado, 'basico': basico})

def datosCliente(request):

    email = request.session["session_key"]  # me da el email, lo que hemos guardado en la sesion

    cli = Cliente.objects.get(email=email)

    data = {
        "dni": cli.dni,
        "nom": cli.nombre,
        "ape": cli.apellidos,
        "dir": cli.direccion,
        "tlf": cli.telefono,
        "email": cli.email,
        "cnt": cli.password,
    }

    #lo que lanza si no hemos dado al boton y crea el evento post
    return render(request, 'inforCli.html', {"datos": data,'cliente': True, 'encargado': False, 'basico': False})


def citasCliente(request):
    return render(request, 'index.html', {'cliente': True, 'encargado': False, 'basico': False})

"""
    METODOS AUXILIARES
"""

def datosClientes():

    datos = Cliente.objects.all();
    datosFinales = []

    for cli in datos:

        data = {
            "dni": cli.dni,
            "nom": cli.nombre,
            "ape": cli.apellidos,
            "email": cli.email,
            "dir": cli.direccion,
            "tlf": cli.telefono,
        }

        datosFinales.append(data)

    return datosFinales

