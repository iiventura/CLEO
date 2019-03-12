from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, unique=True, blank=True, null=False)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    puntuacion = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'Cliente'