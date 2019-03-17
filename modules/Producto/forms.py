from django import forms
from .models import Tipoproducto

def tipoChoice():

    tipos = Tipoproducto.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)


class FormProductoInsert(forms.Form):
    codigo = forms.CharField(max_length=45, label="Codigo ",
            widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

class FormProductoUpdate(forms.Form):
    codigo = forms.CharField(max_length=45, label="Codigo ",
        widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())




