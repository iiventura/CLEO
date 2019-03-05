from django import forms


class FormPromocionInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))



class FormPromocionUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    observaciones = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))

class FormPromocionDelete(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
       widget=(forms.TextInput(attrs={"id": "nombre"})))


