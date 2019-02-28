from django import forms
from django.utils import timezone
from .models import Pedido,Estadopedido
from SILVIA.Proveedor.models import Proveedor
from ..Producto.models import Producto

def estadoChoice():

    tipos = Estadopedido.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def idChoice():

    tipos = Pedido.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.id)))

    return tuple(resultado)

def proveedorChoice():

    tipos = Proveedor.objects.all();

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


class FormPedidoInsert(forms.Form):
    cantidad = forms.IntegerField(label="Cantidad",
        widget=(forms.TextInput(attrs={"id": "cantidad"})))

    fecha = forms.DateField(label=("Fecha"),
       initial=timezone.now().date(),
       input_formats=['%Y-%m-%d'],
       widget=forms.DateInput(format='%Y-%m-%d'),
       disabled=True)

    Estado = forms.ChoiceField(choices=estadoChoice())

    producto = forms.ChoiceField(choices=productoChoice())

    proveedor = forms.ChoiceField(choices=proveedorChoice())

class FormPedidoUpdate(forms.Form):

    cantidad = forms.IntegerField(label="Cantidad",
        widget=(forms.TextInput(attrs={"id": "cantidad"})))

    fecha = forms.DateField(label=("Fecha"),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'),
        disabled=True)

    Estado = forms.ChoiceField(choices=estadoChoice())

    producto = forms.ChoiceField(choices=productoChoice())

    proveedor = forms.ChoiceField(choices=proveedorChoice())

class FormPedidoDelete(forms.Form):
    id = forms.CharField(max_length=45, label="Id ",
       widget=(forms.TextInput(attrs={"id": "id"})))


