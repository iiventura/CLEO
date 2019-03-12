from django import forms
from django.utils import timezone
from ..Promocion.models import Promocion
from ..Cliente.models import Cliente

def promocionChoice():

    tipos = Promocion.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)


def clienteChoice():

    tipos = Cliente.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for tipo in tipos:
        resultado.append((str(tipo.dni), str(tipo.nombre)))

    return tuple(resultado)

def formatoDate():

    fecha = timezone.now().date()
    fecha = str(fecha)
    #en la bbdd se guarda yyyy-mm-dd cambiamso para que sea dd-mm-yyy
    cad = fecha.split('-')
    cad = cad[2] + '-' + cad[1] + '-' + cad[0]

    return cad

class FormPublicidadInsert(forms.Form):

    fecha = formatoDate()

    fechainicio = forms.CharField(max_length=10, label="Inicio ",
        widget=(forms.TextInput(attrs={"id": "fechainicio", "value": fecha})))

    fechafin = forms.CharField(max_length=10, label="Fin ",
         widget=(forms.TextInput(attrs={"id": "fechafin", "value": fecha})))


    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())


class FormPublicidadUpdate(forms.Form):

    fechainicio = forms.CharField(max_length=10, label="Inicio ",
        widget=(forms.TextInput(attrs={"id": "fechainicio"})))

    fechafin = forms.CharField(max_length=10, label="Fin ",
        widget=(forms.TextInput(attrs={"id": "fechafin"})))

    promocion = forms.ChoiceField(choices=promocionChoice())

    cliente = forms.ChoiceField(choices=clienteChoice())

class FormPublicidadDelete(forms.Form):

    id = forms.CharField(max_length=45, label="Id ",
        widget=(forms.TextInput(attrs={"id": "id"})))


