from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipoProducto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
        unique_together = (('id', 'codigo', 'tipoproducto'),)


class Tipoproducto(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoProducto'