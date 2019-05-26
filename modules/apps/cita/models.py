from django.db import models
from usuarios.models import Cliente, Empleado
from ..tratamiento.models import Tratamiento
from ..horarioEmpleado.models import Horario

# Create your models here.

class Estadocita(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'estadoCita'


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    estadocita = models.ForeignKey(Estadocita, models.DO_NOTHING, db_column='estadoCita_id')  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    tratamiento = models.ForeignKey(Tratamiento, models.DO_NOTHING, db_column='Tratamiento_id')  # Field name made lowercase.
    horarioentrada = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioEntrada_id',related_name='entrda')  # Field name made lowercase.
    horariosalida = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioSalida_id',related_name='salida')  # Field name made lowercase.

    def str(self):
        return f'{ self.cliente.nombre } {self.fecha } cita '

    class Meta:
        db_table = 'Cita'
        unique_together = (('id', 'estadocita', 'cliente', 'empleado', 'horarioentrada', 'horariosalida', 'tratamiento'),)

def cargar_Estadocita():
    if Estadocita.objects.count()==0:
        Estadocita(nombre='Confirmada').save()
        Estadocita(nombre='No confirmada').save()

cargar_Estadocita()