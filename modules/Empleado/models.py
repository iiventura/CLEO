from django.db import models

class TipoEmpleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoEmpleado'

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(unique=True, max_length=9)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, unique=True, blank=True, null=False)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    tipoempleado = models.ForeignKey(TipoEmpleado, models.DO_NOTHING, db_column='tipoEmpleado_id')  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'Empleado'
        unique_together = (('dni','tipoempleado'),)
