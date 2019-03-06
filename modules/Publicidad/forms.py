from django import forms
from django.utils import timezone
from ..Promocion.models import Promocion
from ..Cliente.models import Cliente

def promocionChoice():

    tipos = Promocion.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)


def clienteChoice():

    tipos = Cliente.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.dni), str(tipo.nombre)))

    return tuple(resultado)


class FormPublicidadInsert(forms.Form):

    fechainicio = forms.CharField(max_length=10, label="Inicio ",
        widget=(forms.TextInput(attrs={"id": "fechainicio"})))

    fechafin = forms.CharField(max_length=10, label="Fin ",
         widget=(forms.TextInput(attrs={"id": "fechafin"})))
    """
    fechainicio = forms.DateField(label=("Inicio"),
        initial=timezone.now().date(),
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y'))

    fechafin = forms.DateField(label=("Fin"),
        initial=timezone.now().date(),
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y'))
    """
    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())


class FormPublicidadUpdate(forms.Form):

    fechainicio = forms.CharField(max_length=10, label="Inicio ",
        widget=(forms.TextInput(attrs={"id": "fechainicio"})))

    fechafin = forms.CharField(max_length=10, label="Fin ",
        widget=(forms.TextInput(attrs={"id": "fechafin"})))
    f"""
    fechainicio = forms.DateField(label=("Inicio"),
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y'))

    fechafin = forms.DateField(label=("Fin"),
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y'))
    """

    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())

class FormPublicidadDelete(forms.Form):

    id = forms.CharField(max_length=45, label="Id ",
        widget=(forms.TextInput(attrs={"id": "id"})))


