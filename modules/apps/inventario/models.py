from django.db import models
from ..pedido.models import Pedido

class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    coste = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaentrada = models.DateField(db_column='fechaEntrada', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='Pedido_id')  # Field name made lowercase.

    def str(self):
        return f'{ self.pedido.id } { self.fechaentrada } {self.fechafin } inventario '

    class Meta:
        db_table = 'Inventario'
        unique_together = (('id', 'pedido'),)

