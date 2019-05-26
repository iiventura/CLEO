from django.db import models
from ..cita.models import Cita

# Create your models here.
class Estadofactura(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'estadoFactura'

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estadofactura = models.ForeignKey('Estadofactura', models.DO_NOTHING, db_column='estadoFactura_id')  # Field name made lowercase.
    cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_id')  # Field name made lowercase.

    def str(self):
        return f'{ self.cita.cliente } {self.fecha } factura '

    class Meta:
        db_table = 'Factura'
        unique_together = (('id', 'estadofactura', 'cita'),)


def cargar_Estadofactura():
    if Estadofactura.objects.count()==0:
        Estadofactura(nombre='Pagado').save()
        Estadofactura(nombre='Pendiente').save()

cargar_Estadofactura()