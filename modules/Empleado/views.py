from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Empleado
from .forms import *
from django.contrib import messages


def main(request):
    return render(request, 'eindex.html')


def nuevo(request):

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

                    instTipoEmpleado = TipoEmpleado.objects.get(id=tipo)

                    e = Empleado(dni=dni, codigo=cod, nombre=nom, apellidos=ape,email=email,
                                 direccion=dir,telefono=tlf,tipoempleado=instTipoEmpleado, password=password)
                    e.save()

                    return HttpResponseRedirect("/empleado/lista")
                else:
                    messages.error(request, 'El empleado ya existe.')
            else:
                messages.error(request, 'El empleado ya existe.')

    else:
        form = FormEmpleadoInsert()

    return render(request, 'enuevo.html', {'form': form,'elem': 'Alta','titulo':'Alta Empleado'})


def listar(request):
    datos = Empleado.objects.all()
    lista = []

    for empleado in datos:
        tipoEmpleado = TipoEmpleado.objects.get(id=empleado.tipoempleado.id)
        data={
           "id": empleado.id,
            "nom": empleado.nombre,
            "ape": empleado.apellidos,
            "email": empleado.email,
            "tipo": tipoEmpleado.nombre.title(),
        }
        lista.append(data)
    return render(request,'elista.html',{"lista":lista})


def perfil(request,pk ):
    try:
        empleado = Empleado.objects.get(id=pk)
        tipo = TipoEmpleado.objects.get(id=empleado.tipoempleado.id)
        data = {
            "id": empleado.id,
            "dni": empleado.dni,
            "cod": empleado.codigo,
            "tipo": tipo.nombre.title(),
            "nom": empleado.nombre,
            "ape": empleado.apellidos,
            "email": empleado.email,
            "dir": empleado.direccion,
            "tlf": empleado.telefono,
        }

    except Empleado.DoesNotExist:
        raise Http404("Empleado no existe")

    return render(request, 'eperfil.html', {"datos": data})


def eliminar(request,pk ):
    try:
        empleado = Empleado.objects.get(id=pk)
        Empleado.objects.filter(id=empleado.id).delete()

    except Empleado.DoesNotExist:
        raise Http404("Empleado no existe")

    return HttpResponseRedirect("/empleado/lista")


def modificar(request,pk ):
    try:
        empleado = Empleado.objects.get(id=pk)

        if request.method == "POST":
            form = FormEmpleadoUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                nom = datos.get("nombre")
                ape = datos.get("apellidos")
                email = datos.get("email")
                dir = datos.get("direccion")
                tlf = datos.get("telefono")
                tipo = datos.get("Tipo")

                antiEmp = Empleado.objects.get(id=pk)
                instTipoEmpleado = TipoEmpleado.objects.get(id=tipo)

                # actualizamos datos
                antiEmp.codigo = empleado.codigo
                antiEmp.nombre = nom
                antiEmp.apellidos = ape
                antiEmp.email = email
                antiEmp.direccion = dir
                antiEmp.telefono = tlf
                antiEmp.tipoempleado = instTipoEmpleado
                antiEmp.save()

                return HttpResponseRedirect("/empleado/"+str(empleado.id))

        elif request.method == "GET":

            data = {
                "cod": empleado.codigo,
                "nomTipoEle": empleado.tipoempleado.nombre,
                "idTipoEle": empleado.tipoempleado.id,
                "nom": empleado.nombre,
                "ape": empleado.apellidos,
                "email": empleado.email,
                "dir": empleado.direccion,
                "tlf": empleado.telefono,
            }

            datosTipo= listaTipos(data["nomTipoEle"])

            return render(request, 'emodificar.html', {"datos": data, "datosTipo": datosTipo})

    except Empleado.DoesNotExist:
        raise Http404("Empleado no existe")

    return HttpResponseRedirect('/empleado/' + str(pk) + '/modificar')


def listaTipos(nombre):
   tipos = TipoEmpleado.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista
