from django import forms
from .models import TipoEmpleado


def tipoChoice():
    tipos = TipoEmpleado.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

class FormEmpleadoInsert(forms.Form):
    dni = forms.CharField(max_length=9,label="Dni ",
        widget = (forms.TextInput(attrs = {"id" : "dni"})))

    codigo = forms.CharField(max_length=9, label="Codigo ",
        widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    apellidos = forms.CharField(max_length=45,label="Apellidos ",
        widget = (forms.TextInput(attrs = {"id" : "apellidos"})))

    email = forms.EmailField(max_length=45, label="Email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    direccion = forms.CharField(max_length=45, label="Direccion",
        widget = (forms.TextInput(attrs = {"id" : "direccion"})))

    telefono = forms.CharField(max_length=45, label="Telefono ",
        widget=(forms.TextInput(attrs={"id": "telefono"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.TextInput(attrs={"id": "password"})))


class FormEmpleadoUpdate(forms.Form):
     nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

     apellidos = forms.CharField(max_length=45,label="Apellidos ",
        widget = (forms.TextInput(attrs = {"id" : "apellidos"})))

     email = forms.EmailField(max_length=45, label="Email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

     direccion = forms.CharField(max_length=45, label="Direccion",
        widget = (forms.TextInput(attrs = {"id" : "direccion"})))

     telefono = forms.CharField(max_length=45, label="Telefono ",
        widget=(forms.TextInput(attrs={"id": "telefono"})))

     Tipo = forms.ChoiceField(choices=tipoChoice())








