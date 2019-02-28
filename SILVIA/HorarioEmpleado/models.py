from django.db import models
from modules.Empleado.models import Empleado

# Create your models here.
class Horario(models.Model):
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Horario'

class Horarioempleado(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    horarioentrada = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioEntrada_id',related_name='horarioentrada')  # Field name made lowercase.
    horariosalida = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioSalida_id',related_name='horariosalida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HorarioEmpleado'
        unique_together = (('empleado', 'horarioentrada', 'horariosalida'),)