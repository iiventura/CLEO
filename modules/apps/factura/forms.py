from datetime import time
from django import forms
from .models import Factura, Estadofactura
from ..cita.models import Cita

"""
def clienteChoice():

    tipos = Cita.objects.all();
    emp = []

    resultado = []
    resultado.append(('', 'Selecciona'))

    for tipo in tipos:
        resultado.append((str(tipo.cliente.id), str(tipo.cliente.dni)))

    return tuple(resultado)

def empleadoChoice():

    tipos = Cita.objects.all();
    emp = []

    resultado = []
    resultado.append(('', 'Selecciona'))

    for tipo in tipos:
        resultado.append((str(tipo.empleado.id), str(tipo.empleado.dni)))

    return tuple(resultado)
"""
def estadoChoice():
    tipos = Estadofactura.objects.all();
    emp = []

    resultado = []
    resultado.append(('', 'Selecciona'))

    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre).title()))

    return tuple(resultado)

def citaChoice():

    tipos = Cita.objects.all()

    resultado = []
    resultado.append(('', 'Selecciona'))

    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.id)))

    return tuple(resultado)

class FormFacturaInsert1(forms.Form):

    cita = forms.ChoiceField(choices=citaChoice())


class FormFacturaInsert2(forms.Form):

    cita = forms.ChoiceField(choices=citaChoice())

    cliente = forms.CharField(max_length=9, label="Cliente",
        widget=(forms.TextInput(attrs={"id": "cliente"})))

    empleado = forms.CharField(max_length=9, label="Empleado",
        widget=(forms.TextInput(attrs={"id": "empleado"})))

    fecha = forms.CharField(max_length=10, label="Fecha ",
        widget=(forms.TextInput(attrs={"id": "fecha"})))

    total = forms.FloatField(label="total",
        widget=(forms.TextInput(attrs={"id": "total"})))

    estado = forms.ChoiceField(choices=estadoChoice())

    paga = forms.FloatField(label="Paga",
        widget=(forms.TextInput(attrs={"id": "paga"})))


class FormFacturaUpdate(forms.Form):
    cita = forms.ChoiceField(choices=citaChoice())

    cliente = forms.CharField(max_length=9, label="Cliente",
        widget=(forms.TextInput(attrs={"id": "cliente"})))

    empleado = forms.CharField(max_length=9, label="empleado",
        widget=(forms.TextInput(attrs={"id": "empleado"})))

    fecha = forms.CharField(max_length=10, label="Fecha ",
        widget=(forms.TextInput(attrs={"id": "fecha"})))

    total = forms.FloatField(label="total",
       widget=(forms.TextInput(attrs={"id": "total"})))

    estado = forms.ChoiceField(choices=estadoChoice())

    paga = forms.FloatField(label="Paga",
       widget=(forms.TextInput(attrs={"id": "paga"})))
