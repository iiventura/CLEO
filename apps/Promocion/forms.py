from django import forms


class FormPromocionInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(max_length=45, label="Observacion ",
        widget=(forms.TextInput(attrs={"id": "observaciones"})))



class FormPromocionUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(max_length=45, label="Observacion",
         widget=(forms.TextInput(attrs={"id": "observaciones"})))

class FormPromocionDelete(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
       widget=(forms.TextInput(attrs={"id": "nombre"})))


