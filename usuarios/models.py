from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)


class TipoEmpleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tipoempleado'


class Empleado(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    tipoempleado = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='tipoEmpleado_id')



    class Meta:
        db_table = 'empleado'
        unique_together = (('tipoempleado', 'dni'),)


class Cliente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    puntuacion = models.IntegerField(blank=True, null=True)


    class Meta:
       db_table = 'cliente'



def cargar():
    if TipoEmpleado.objects.count()==0:
        TipoEmpleado(nombre='Encargado').save()
        TipoEmpleado(nombre='Basico').save()



cargar()