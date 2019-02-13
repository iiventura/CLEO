from django import forms

from .models import Tipoempleado

def tipoChoice():

    tipos = Tipoempleado.objects.all();
    lista = []

    for tipo in tipos:
        nom = str(tipo.nombre).title();
        lista.append(nom)

    resultado = []
    resultado.append(('', 'Selecciona'))
    for i in lista:
        resultado.append((str(i), str(i)))

    return tuple(resultado)

def estadoChoice():
    #db = MySQLdb.connect(user='root', db='tfg1', passwd='root2018', host='localhost')
    cursor = db.cursor()
    query = "SHOW COLUMNS FROM Empleado LIKE 'estado'"
    cursor.execute(query)
    datos = cursor.fetchall()

    nueva = str(datos)
    d1 = nueva.split("enum")
    d2 = d1[1].split("(")
    d3 = d2[1].split(")")
    d4 = d3[0].split(",")#tiene todas las opciones
    db.close()

    lista = []
    #cogemos todas las opciones y las guardamos en una lista
    for op in d4:
        t = op[1:len(op) - 1]
        lista.append(t)

    resultado = []
    resultado.append(('', 'Selecciona'))
    for i in lista:
        resultado.append((str(i), str(i)))

    return tuple(resultado)

class FormEmpleadoInsert(forms.Form):
    dni = forms.CharField(max_length=9,label="Dni ",
        widget = (forms.TextInput(attrs = {"id" : "dni"})))

    codigo = forms.CharField(max_length=9, label="Codigo ",
        widget=(forms.TextInput(attrs={"id": "codigo"})))

    nombre = forms.CharField(max_length=45, label="Nombre ",
        widget=(forms.TextInput(attrs={"id": "nombre"})))

    apellidos = forms.CharField(max_length=45,label="Apellidos ",
        widget = (forms.TextInput(attrs = {"id" : "apellidos"})))

    email = forms.EmailField(max_length=45, label="Email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    direccion = forms.CharField(max_length=45, label="Direccion",
        widget = (forms.TextInput(attrs = {"id" : "direccion"})))

    telefono = forms.CharField(max_length=45, label="Telefono ",
        widget=(forms.TextInput(attrs={"id": "telefono"})))

    Tipo = forms.ChoiceField(choices=tipoChoice())

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.TextInput(attrs={"id": "password"})))

class FormEmpleadoLogin(forms.Form):
    email = forms.EmailField(max_length=45, label="email ",
        widget=(forms.TextInput(attrs={"id": "email"})))

    password = forms.CharField(max_length=45, label="Contraseña",
        widget=(forms.PasswordInput(attrs={"id": "password"})))

class FormEmpleadoDelete(forms.Form):
    dni = forms.CharField(max_length=9, label="Dni ",
        required=False, #lo ponemos para que no nos salga que es requerido al mostrarlo
        widget=(forms.TextInput(attrs={"id": "dni"})))

class FormEmpleadoUpdate(forms.Form):

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

    Tipo = forms.ChoiceField(choices=tipoChoice())

    password = forms.CharField(max_length=45, label="Contraseña",
            widget=(forms.TextInput(attrs={"id": "password"})))
