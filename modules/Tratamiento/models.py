from django.db import models

class Maquina(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipomaquina = models.ForeignKey('TipoMaquina', models.DO_NOTHING, db_column='tipoMaquina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maquina'
        unique_together = (('tipomaquina'),)

class TipoMaquina(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoMaquina'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='tipoProducto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
        unique_together = (('id', 'codigo', 'tipoproducto'),)


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoProducto'



class Tratamiento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='Maquina_id')  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')

    class Meta:
        managed = False
        db_table = 'Tratamiento'
        unique_together = (('id', 'nombre','maquina','producto'),)


