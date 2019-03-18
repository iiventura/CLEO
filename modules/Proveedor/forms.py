from django import forms


class FormProveedorInsert(forms.Form):

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    contacto = forms.CharField(max_length=45, label="Contacto ",
        widget=(forms.TextInput(attrs={"id": "contacto"})))

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 28, 'rows': 2}))


class FormProveedorUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
         widget=(forms.TextInput(attrs={"id": "nombre"})))

    contacto = forms.CharField(max_length=45, label="Contacto ",
        widget=(forms.TextInput(attrs={"id": "contacto"})))

    descripcion = forms.CharField(max_length=45, label="Descripcion ",
        widget=(forms.TextInput(attrs={"id": "descripcion"})))




