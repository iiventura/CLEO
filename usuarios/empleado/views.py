from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from usuarios.models import CustomUser,Empleado, TipoEmpleado

@login_required()
def listar(request):
    datos = Empleado.objects.all()
    lista = []
    #lunes = fechaLunes()


    for empleado in datos:
        user = CustomUser.objects.get(empleado=empleado)
        #turno = turnoEmpleado(lunes,empleado.id)

        data={
            "id": user.id,
            "nom": user.first_name,
            "ape": user.last_name,
            "email": user.email,
            "tipo": empleado.tipoempleado.nombre,
            #"turno": turno,
        }

        lista.append(data)

    return render(request,'empleado/lista.html',{"lista":lista})

@login_required()
def eliminar(request):
    pass

@login_required()
def modificar(request):
    pass
