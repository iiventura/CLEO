from django.db import models
from ..producto.models import Producto

# Create your models here.

class EstadoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    def str(self):
        return f'{ self.nombre } estadopedido '

    class Meta:
        db_table = 'estadopedido'

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estadopedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='estadoPedido_id')  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.

    def str(self):
        return f'{ self.fecha } pedido '

    class Meta:
        db_table = 'Pedido'
        unique_together = (('id','estadopedido','producto'),)

def cargar_EstadoPedido():
    if EstadoPedido.objects.count()==0:
        EstadoPedido(nombre='Entregado').save()
        EstadoPedido(nombre='En proceso').save()
        EstadoPedido(nombre='Cancelado').save()

#cargar_EstadoPedido()