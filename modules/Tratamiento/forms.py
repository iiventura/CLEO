from django import forms
from modules.Maquina.models import Maquina

def tipoChoice():

    tipos = Maquina.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        lista.append(nom)

    resultado = []
    resultado.append(('', 'Selecciona'))
    for i in lista:
        resultado.append((str(i), str(i)))

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




