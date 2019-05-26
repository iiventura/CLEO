from datetime import time

from django import forms
from .models import Estadocita
from usuarios.models import Empleado
from ..tratamiento.models import Tratamiento

def empleadoChoice():

    tipos = Empleado.objects.all();
    emp = []

    resultado = []
    resultado.append(('', 'Selecciona'))
    resultado.append(("0", '---'))

    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def horarioChoice():

    resultado = []
    resultado.append(('', 'Selecciona'))
    h = 9

    for i in range(0,13):
        hora = time(h, 0, 0)
        h += 1
        resultado.append((str(hora), str(hora)))
        #resultado.append((str(k), str(hora)))

    return tuple(resultado)

def tratamientoChoice():
    tipos = Tratamiento.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))

    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def estadoChoice():
    tipos = Estadocita.objects.all();

    resultado = []

    for tipo in tipos:
        resultado.append((str(tipo.id).title(), str(tipo.nombre).title()))

    return tuple(resultado)


class FormCitaClienteInsert(forms.Form):
    cliente = forms.CharField(max_length=9,label="Dni ",
        widget=(forms.TextInput(attrs={"id": "dni"})))

    tratamiento = forms.ChoiceField(choices=tratamientoChoice())


class FormCitaClienteInsert2(forms.Form):
    cliente = forms.CharField(max_length=9,label="Dni ",
        widget=(forms.TextInput(attrs={"id": "dni"})))

    tratamiento = forms.ChoiceField(choices=tratamientoChoice())

    fecha = forms.DateField(label=("Fecha"),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'),
        disabled=False)

    hora = forms.ChoiceField(choices=horarioChoice())


class FormCitaClienteInsert3(forms.Form):
    cliente = forms.CharField(max_length=9,label="Dni ",
        widget = (forms.TextInput(attrs={"id": "dni"})))

    tratamiento = forms.ChoiceField(choices=tratamientoChoice())

    fecha = forms.CharField(max_length=10, label="Fecha ",
        widget=(forms.TextInput(attrs={"id": "fecha"})))

    hora = forms.ChoiceField(choices=horarioChoice())

    empleado = forms.ChoiceField(choices=empleadoChoice())

class FormCitaUpdate(forms.Form):
    cliente = forms.CharField(max_length=9,label="Dni ",
        widget = (forms.TextInput(attrs={"id": "dni"})))

    tratamiento = forms.ChoiceField(choices=tratamientoChoice())

    fecha = forms.CharField(max_length=10, label="Fecha ",
        widget=(forms.TextInput(attrs={"id": "fecha"})))

    hora = forms.ChoiceField(choices=horarioChoice())

    estado = forms.ChoiceField(choices=estadoChoice())

    empleado = forms.ChoiceField(choices=empleadoChoice())
