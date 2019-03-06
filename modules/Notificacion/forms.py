from django import forms
from .models import *

def estadoChoice():

    tipos = Estadomensaje.objects.all();
    lista = []

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def tipoUsuarioChoice():

    tipos = Tipousuario.objects.all();
    lista = []

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)


class FormNotificacionInsert(forms.Form):

    Estado = forms.ChoiceField(choices=estadoChoice())

    Usuario = forms.ChoiceField(choices=tipoUsuarioChoice())

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))


class FormNotificacionUpdate(forms.Form):
    Estado = forms.ChoiceField(choices=estadoChoice())

    Usuario = forms.ChoiceField(choices=tipoUsuarioChoice())

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

class FormNotificacionDelete(forms.Form):

    id = forms.CharField(max_length=45, label="Id ",
        widget=(forms.TextInput(attrs={"id": "id"})))


