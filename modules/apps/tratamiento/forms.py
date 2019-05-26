from django import forms
from ..producto.models import Producto
from ..maquina.models import Maquina

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

    nombre = forms.CharField(max_length=45, label="Nombre",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    maquina = forms.ChoiceField(choices=maquinaChoice())

    producto = forms.ChoiceField(choices=productoChoice())

    duracion = forms.IntegerField(label="Duracion",
        widget=(forms.TextInput(attrs={"id": "duracion"})))

    precio = forms.FloatField(label="Precio",
        widget=(forms.TextInput(attrs={"id": "precio"})))

    espera = forms.IntegerField(label="Espera",
        widget=(forms.TextInput(attrs={"id": "espera"})))


class FormTratamientoUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    maquina = forms.ChoiceField(choices=maquinaChoice())

    producto = forms.ChoiceField(choices=productoChoice())

    duracion = forms.IntegerField(label="Duracion",
        widget=(forms.TextInput(attrs={"id": "duracion"})))

    precio = forms.FloatField(label="Precio",
        widget=(forms.TextInput(attrs={"id": "precio"})))

    espera = forms.IntegerField(label="Espera",
        widget=(forms.TextInput(attrs={"id": "espera"})))
