from django import forms
from django.utils import timezone
from .models import Tipomaquina

def tipoChoice():
    tipos = Tipomaquina.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

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




