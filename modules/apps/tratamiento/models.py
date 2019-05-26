from django.db import models
from ..maquina.models import Maquina
from ..producto.models import Producto


class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    espera = models.IntegerField(blank=True, null=True)
    maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='Maquina_id')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')

    def str(self):
        return f'{ self.nombre } {self.precio } tratamiento '

    class Meta:
        db_table = 'Tratamiento'
        unique_together = (('id', 'nombre','maquina','producto'),)
