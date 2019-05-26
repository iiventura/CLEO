import datetime

from django import forms
from ..proveedor.models import Proveedor


def meses():
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
                 'Octubre', 'Noviembre', 'Diciembre']
        i = 0

        resultado = []
        resultado.append(("", 'Selecciona'))
        resultado.append((str(i), '---'))

        for m in meses:
            i += 1
            resultado.append((str(i), str(m)))

        return tuple(resultado)

def proveedorChoice():

    tipos = Proveedor.objects.all();

    resultado = []
    resultado.append(("", 'Selecciona'))
    resultado.append(("0", '---'))

    for tipo in tipos:
        if tipo.borrado != 1:
            resultado.append((str(tipo.id), str(tipo.nombre)))

    return tuple(resultado)

class FormInventarioFiltro(forms.Form):

    mes = forms.ChoiceField(choices=meses())

    proveedor = forms.ChoiceField(choices=proveedorChoice())
