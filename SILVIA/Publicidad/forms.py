from django import forms
from django.utils import timezone
from ..Promocion.models import Promocion
from ..Cliente.models import Cliente

def promocionChoice():

    tipos = Promocion.objects.all();
    lista = []


    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

def clienteChoice():

    tipos = Cliente.objects.all();
    lista = []


    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.dni), str(tipo.nombre)))

    return tuple(resultado)


class FormPublicidadInsert(forms.Form):

    fechainicio = forms.DateField(label=("Inicio"),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'))

    fechafin = forms.DateField(label=("Fin"),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d'))

    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())


class FormPublicidadUpdate(forms.Form):

    fechainicio = forms.DateField(label=("Inicio"),
      initial=timezone.now().date(),
      input_formats=['%Y-%m-%d'],
      widget=forms.DateInput(format='%Y-%m-%d'))

    fechafin = forms.DateField(label=("Fin"),
       initial=timezone.now().date(),
       input_formats=['%Y-%m-%d'],
       widget=forms.DateInput(format='%Y-%m-%d'))

    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())

class FormPublicidadDelete(forms.Form):

    id = forms.CharField(max_length=45, label="Id ",
        widget=(forms.TextInput(attrs={"id": "id"})))


