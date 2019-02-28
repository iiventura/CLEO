from django import forms
from modules.Maquina.models import Maquina

def tipoChoice():

    tipos = Maquina.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))
    return tuple(resultado)


class FormTratamientoInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(max_length=45, label="Descripcion ",
        widget=(forms.TextInput(attrs={"id": "descripcion"})))

    maquina = forms.ChoiceField(choices=tipoChoice())


class FormTratamientoUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(max_length=45, label="Descripcion ",
        widget=(forms.TextInput(attrs={"id": "descripcion"})))

    maquina = forms.ChoiceField(choices=tipoChoice())

