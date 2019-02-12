from django import forms

class FormClienteInsert(forms.Form):
    dni = forms.CharField(max_length=9,label="Dni ", required=False,
        widget = (forms.TextInput(attrs = {"id" : "dni"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",required=False,
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    apellidos = forms.CharField(max_length=45,label="Apellidos ",required=False,
        widget = (forms.TextInput(attrs = {"id" : "apellidos"})))

    email = forms.EmailField(max_length=45, label="Email ",required=False,
        widget=(forms.TextInput(attrs={"id": "email"})))

    direccion = forms.CharField(max_length=45, label="Direccion",required=False,
        widget = (forms.TextInput(attrs = {"id" : "direccion"})))

    telefono = forms.CharField(max_length=45, label="Telefono ",required=False,
        widget=(forms.TextInput(attrs={"id": "telefono"})))

    password = forms.CharField(max_length=45, label="Contraseña",required=False,
        widget=(forms.TextInput(attrs={"id": "password"})))

class FormClienteLogin(forms.Form):
    email = forms.EmailField(max_length=45, label="email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.PasswordInput(attrs={"id": "password"})))

class FormClienteDelete(forms.Form):
    dni = forms.CharField(max_length=9, label="Dni ",
        widget=(forms.TextInput(attrs={"id": "dni"})))

class FormClienteUpdate(forms.Form):
    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    apellidos = forms.CharField(max_length=45, label="Apellidos ",
        widget=(forms.TextInput(attrs={"id": "apellidos"})))

    email = forms.EmailField(max_length=45, label="Email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    direccion = forms.CharField(max_length=45, label="Direccion",
        widget=(forms.TextInput(attrs={"id": "direccion"})))

    telefono = forms.CharField(max_length=45, label="Telefono ",
        widget=(forms.TextInput(attrs={"id": "telefono"})))

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.TextInput(attrs={"id": "password"})))
