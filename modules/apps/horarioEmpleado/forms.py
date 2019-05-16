import datetime

from django import forms
from django.utils import timezone
from .models import Tipohorarioempleado
from usuarios.models import Empleado, CustomUser


def empleadoChoice():
    tipos = CustomUser.objects.filter(is_staff=True, is_superuser=False)

    resultado = []
    resultado.append(('', 'Selecciona'))

    for t in tipos:
        resultado.append((str(t.id), str(t.first_name)))

    return tuple(resultado)


def horarioChoice():
    tipos = Tipohorarioempleado.objects.all();

    resultado = []
    resultado.append(('', 'Selecciona'))
    for t in tipos:
        if not (str(t.nombre).title() == "Dobla" or str(t.nombre).title() == "Libra"):
            resultado.append((str(t.id), str(t.nombre)))

    return tuple(resultado)


def fechaLunes():
    # devuleve un numero 0 unes 6 domingo
    pos = datetime.datetime.today().weekday()
    dia = datetime.timedelta(days=pos)
    f = timezone.now().date()

    return f - dia


def fechaDomingo(fecha):
    dia = datetime.timedelta(days=6)
    f = fecha + dia

    return f


def fechasChoice():
    resultado = []
    f1 = fechaLunes()
    resultado.append((str(0), str("---")))

    for i in range(0, 15):
        fec = str(f1)
        idFec = fec
        cad = fec.split('-')
        fec = cad[2] + '-' + cad[1] + '-' + cad[0]

        resultado.append((str(idFec), str(fec)))

        dia = datetime.timedelta(days=1)
        f1 = f1 + dia

    return tuple(resultado)


class FormHorarioInsert(forms.Form):
    empleado = forms.ChoiceField(choices=empleadoChoice())
    horario = forms.ChoiceField(choices=horarioChoice())

    ini = fechaLunes()
    fn = fechaDomingo(ini)

    inicio = forms.DateField(label=("Inicio"),
         initial=ini,
         input_formats=['%m-%d-%Y'],
         widget=forms.DateInput(format='%m-%d-%Y'),
         disabled=True)

    fin = forms.DateField(label=("Fin"),
          initial=fn,
          input_formats=['%m-%d-%Y'],
          widget=forms.DateInput(format='%m-%d-%Y'),
          disabled=True)


class FormHorarioInsert2(forms.Form):
    empleado = forms.ChoiceField(choices=empleadoChoice())

    horario = forms.ChoiceField(choices=horarioChoice())

    ini = fechaLunes()
    fn = fechaDomingo(ini)

    inicio = forms.DateField(label=("Inicio"),
                             initial=ini,input_formats=['%m-%d-%Y'],
                             widget=forms.DateInput(format='%m-%d-%Y'),
                             disabled=True)

    fin = forms.DateField(label=("Fin"),
                          initial=fn, input_formats=['%m-%d-%Y'],
                          widget=forms.DateInput(format='%m-%d-%Y'),
                          disabled=True)

    libra = forms.ChoiceField(choices=fechasChoice())

    dobla = forms.ChoiceField(choices=fechasChoice())


class FormHorarioUpdate(forms.Form):
    empleado = forms.ChoiceField(choices=empleadoChoice())

    horario = forms.ChoiceField(choices=horarioChoice())

    inicio = forms.DateField(label=("Inicio"),
         initial=timezone.now().date(),
         input_formats=['%Y-%m-%d'],
         widget=forms.DateInput(format='%Y-%m-%d'))

    fin = forms.DateField(label=("Fin"),
          initial=timezone.now().date(),
          input_formats=['%Y-%m-%d'],
          widget=forms.DateInput(format='%Y-%m-%d'))
