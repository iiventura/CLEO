from django import forms
from .models import Maquina, Producto

def maquinaChoice():

    tipos = Maquina.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def productoChoice():

    tipos = Producto.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)


class FormTratamientoInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    maquina = forms.ChoiceField(choices=maquinaChoice())

    producto = forms.ChoiceField(choices=productoChoice())


class FormTratamientoUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    maquina = forms.ChoiceField(choices=maquinaChoice())

    producto = forms.ChoiceField(choices=productoChoice())

