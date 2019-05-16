from django.db import models
from ..proveedor.models import Proveedor


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    def str(self):
        return f'{ self.nombre } tipoproducto '

    class Meta:
        db_table = 'tipoProducto'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    tipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipoProducto_id')
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='Proveedor_id')
    borrado = models.IntegerField(blank=True, null=True, default=0)

    def str(self):
        return f'{ self.nombre } {self.proveedor } producto '

    class Meta:
        db_table = 'Producto'
        unique_together = (('id', 'codigo', 'tipoproducto','proveedor'),)


def cargar_TipoProducto():
    if TipoProducto.objects.count()==0:
        TipoProducto(nombre='Uso').save()
        TipoProducto(nombre='Venta').save()

cargar_TipoProducto()