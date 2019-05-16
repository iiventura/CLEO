from django.db import models
from usuarios.models import Empleado

class Tipohorarioempleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tipoHorarioEmpleado'

class Horario(models.Model):
    hora = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'Horario'

class Horarioempleado(models.Model):
    id = models.AutoField(primary_key=True)
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    tipohorarioempleado = models.ForeignKey(Tipohorarioempleado, models.DO_NOTHING, db_column='tipoHorarioEmpleado_id')  # Field name made lowercase.

    def str(self):
        return f'{ self.inicio } {self.fin } horario '

    class Meta:
        db_table = 'HorarioEmpleado'
        unique_together = (('id', 'empleado', 'tipohorarioempleado'),)


def cargar_Tipohorarioempleado():
    if Tipohorarioempleado.objects.count()==0:
        Tipohorarioempleado(nombre='Mañana').save()
        Tipohorarioempleado(nombre='Tarde').save()
        Tipohorarioempleado(nombre='Libra').save()
        Tipohorarioempleado(nombre='Dobla').save()

cargar_Tipohorarioempleado()