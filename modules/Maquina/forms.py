from django import forms
from django.utils import timezone
from modules.Maquina.models import Tipomaquina

def tipoChoice():

    tipos = Tipomaquina.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        lista.append(nom)

    resultado = []
    resultado.append(('', 'Selecciona'))
    for i in lista:
        resultado.append((str(i), str(i)))

    return tuple(resultado)


class FormMaquinaInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    fechaingreso = forms.DateField(label=("Fecha"),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'),
        disabled = True)

    Tipo = forms.ChoiceField(choices=tipoChoice())

class FormMaquinaUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    fechaingreso = forms.DateField(label=("Fecha"),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'),
        disabled=True)

    Tipo = forms.ChoiceField(choices=tipoChoice())




