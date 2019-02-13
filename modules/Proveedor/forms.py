from django import forms


class FormProveedorInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    contacto = forms.CharField(max_length=45, label="Contacto ",
        widget=(forms.TextInput(attrs={"id": "contacto"})))

    descripcion = forms.CharField(max_length=45, label="Descripcion ",
        widget=(forms.TextInput(attrs={"id": "descripcion"})))


class FormProveedorUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    contacto = forms.CharField(max_length=45, label="Contacto ",
        widget=(forms.TextInput(attrs={"id": "contacto"})))

    descripcion = forms.CharField(max_length=45, label="Descripcion ",
        widget=(forms.TextInput(attrs={"id": "descripcion"})))

class FormProveedorDelete(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
       widget=(forms.TextInput(attrs={"id": "nombre"})))


