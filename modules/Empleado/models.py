from django.db import models

class Tipoempleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoempleado'

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    tipoempleado = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='tipoEmpleado_id')  # Field name made lowercase.
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'empleado'
        unique_together = (('id', 'tipoempleado'),)