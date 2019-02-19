from django import forms
from .models import Tipoempleado

def tipoChoice():

    tipos = Tipoempleado.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        lista.append(nom)

    resultado = []
    resultado.append(('', 'Selecciona'))
    for i in lista:
        resultado.append((str(i), str(i)))

    return tuple(resultado)



class FormEmpleadoLogin(forms.Form):
    email = forms.EmailField(max_length=45, label="email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.PasswordInput(attrs={"id": "password"})))


