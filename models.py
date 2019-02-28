# This is an auto-generated Django model modules.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    estadocita = models.ForeignKey('Estadocita', models.DO_NOTHING, db_column='estadoCita_id')  # Field name made lowercase.
    sala = models.ForeignKey('Sala', models.DO_NOTHING, db_column='Sala_id')  # Field name made lowercase.
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='Tratamiento_id')  # Field name made lowercase.
    horarioentrada = models.ForeignKey('Horario', models.DO_NOTHING, db_column='HorarioEntrada_id')  # Field name made lowercase.
    horariosalida = models.ForeignKey('Horario', models.DO_NOTHING, db_column='HorarioSalida_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cita'
        unique_together = (('id', 'estadocita', 'sala', 'cliente', 'empleado', 'tratamiento', 'horarioentrada', 'horariosalida'),)

<<<<<<< HEAD
=======

>>>>>>> 0abc9e44661e59ce535fa70dd578c0fedace4efa
class Estadocita(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocita'


class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estadofactura = models.ForeignKey(Estadofactura, models.DO_NOTHING, db_column='estadoFactura_id')  # Field name made lowercase.
    cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'
        unique_together = (('id', 'estadofactura', 'cita'),)

class Estadofactura(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadofactura'

<<<<<<< HEAD
class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estadofactura = models.ForeignKey(Estadofactura, models.DO_NOTHING, db_column='estadoFactura_id')  # Field name made lowercase.
    cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_id')  # Field name made lowercase.
=======

class Estadomensaje(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadomensaje'


class Estadopedido(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadopedido'


>>>>>>> 0abc9e44661e59ce535fa70dd578c0fedace4efa



class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    coste = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaentrada = models.DateTimeField(db_column='fechaEntrada', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='Pedido_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('id', 'proveedor', 'producto', 'pedido'),)





