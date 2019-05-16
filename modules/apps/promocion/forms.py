from django import forms


class FormPromocionInsert(forms.Form):

    codigo = forms.CharField(max_length=45, label="Codigo ",
            widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    descuento = forms.FloatField( label="Descuento ",
        widget=(forms.TextInput(attrs={"id": "descuento"})))



class FormPromocionUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

    descuento = forms.FloatField( label="Descuento ",
        widget=(forms.TextInput(attrs={"id": "descuento"})))

class FormPromocionDelete(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
       widget=(forms.TextInput(attrs={"id": "nombre"})))


