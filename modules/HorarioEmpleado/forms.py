from django import forms
from django.utils import timezone
from modules.Empleado.models import *
from .models import HorarioEmpleado,Horario

def empChoice():

    tipos = Empleado.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.dni), str(tipo.nombre).title()))

    return tuple(resultado)

def empHorarioChoice():

    datos = Horarioempleado.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))

    for dato in datos:
        emp = dato.empleado
        resultado.append((str(emp.dni), str(emp.nombre).title()))

    return tuple(resultado)


def horaChoice():

    tipos = Horario.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.hora)))

    return tuple(resultado)


class FormHorarioEmpleadoInsert(forms.Form):

    fecha = forms.DateField(label=("Fecha"),
       initial=timezone.now().date(),
       input_formats=['%Y-%m-%d'],
       widget=forms.DateInput(format='%Y-%m-%d'),
       disabled=True)

    empleado = forms.ChoiceField(choices=empChoice())

    horarioentrada = forms.ChoiceField(choices=horaChoice())

    horariosalida = forms.ChoiceField(choices=horaChoice())


class FormHorarioEmpleadoUpdate(forms.Form):

    fecha = forms.DateField(label=("Fecha"),
       initial=timezone.now().date(),
       input_formats=['%Y-%m-%d'],
       widget=forms.DateInput(format='%Y-%m-%d'),
       disabled=True)

    empleado = forms.ChoiceField(choices=empChoice())

    horarioentrada = forms.ChoiceField(choices=horaChoice())

    horariosalida = forms.ChoiceField(choices=horaChoice())


