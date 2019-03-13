from django import forms

class FormSalaInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))



class FormSalaUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))