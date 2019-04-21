from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import CustomUser, Cliente

class ClienteRegistrationForm(UserCreationForm):
    nombre = forms.CharField(max_length=45, label="Nombre ",
                             widget=(forms.TextInput(attrs={"id": "nombre"})))

    apellidos = forms.CharField(max_length=45, label="Apellidos ",
                                widget=(forms.TextInput(attrs={"id": "apellidos"})))

    dni = forms.CharField(max_length=9, label="Dni ",
                          widget=(forms.TextInput(attrs={"id": "dni"})))

    email = forms.EmailField(max_length=45, label="Email ",
                             widget=(forms.TextInput(attrs={"id": "email"})))

    direccion = forms.CharField(max_length=45, label="Direccion",
                                widget=(forms.TextInput(attrs={"id": "direccion"})))

    telefono = forms.CharField(max_length=45, label="Telefono ",
                               widget=(forms.TextInput(attrs={"id": "telefono"})))

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("nombre")
        user.last_name = self.cleaned_data.get("apellidos")
        user.is_client = True
        user.save()

        cliente = Cliente.objects.create(user=user)
        cliente.dni = self.cleaned_data.get('dni')
        cliente.direccion = self.cleaned_data.get('direccion')
        cliente.telefono = self.cleaned_data.get('telefono')
        cliente.puntuacion = 0
        cliente.save()

        return user