from django import forms
from .models import TipoProducto
from ..proveedor.models import Proveedor

def tipoChoice():

    tipos = TipoProducto.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def proveedorChoice():

    tipos = Proveedor.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        if tipo.borrado != 1:
            resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

class FormProductoInsert(forms.Form):
    codigo = forms.CharField(max_length=45, label="Codigo ",
            widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    precio = forms.FloatField(label="Precio ",
        widget=(forms.TextInput(attrs={"id": "precio"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

    proveedor = forms.ChoiceField(choices=proveedorChoice())

class FormProductoUpdate(forms.Form):
    codigo = forms.CharField(max_length=45, label="Codigo ",
        widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    precio = forms.FloatField(label="Precio ",
         widget=(forms.TextInput(attrs={"id": "precio"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

    proveedor = forms.ChoiceField(choices=proveedorChoice())




