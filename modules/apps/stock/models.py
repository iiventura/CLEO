from django.db import models
from ..producto.models import Producto
from ..proveedor.models import Proveedor

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    cantprov = models.IntegerField(db_column='cantProv', blank=True, null=True)  # Field name made lowercase.
    canttotal = models.IntegerField(db_column='cantTotal', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.

    def str(self):
        return f'{ self.producto } {self.canttotal } stock '

    class Meta:
        db_table = 'Stock'
        unique_together = (('id', 'proveedor', 'producto'),)

