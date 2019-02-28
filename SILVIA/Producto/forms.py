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
    id = forms.IntegerField(label="Id ",
            widget=(forms.TextInput(attrs={"id": "id"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

class FormProductoUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

class FormProductoDelete(forms.Form):

    Id = forms.CharField(max_length=45, label="Id ",
        widget=(forms.TextInput(attrs={"id": "id"})))


