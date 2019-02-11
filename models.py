# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
True
False
False
False


class Cita(models.Model):
    id = models.AutoField()
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
        db_table = 'Cita'
        unique_together = (('id', 'estadocita', 'sala', 'cliente', 'empleado', 'tratamiento', 'horarioentrada', 'horariosalida'),)



class Factura(models.Model):
    id = models.AutoField()
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estadofactura = models.ForeignKey('Estadofactura', models.DO_NOTHING, db_column='estadoFactura_id')  # Field name made lowercase.
    cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factura'
        unique_together = (('id', 'estadofactura', 'cita'),)
False
False
False
False


class Horario(models.Model):
    hora = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Horario'
False
False
False
False


class Horarioempleado(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    horarioentrada = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioEntrada_id')  # Field name made lowercase.
    horariosalida = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioSalida_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HorarioEmpleado'
        unique_together = (('empleado', 'horarioentrada', 'horariosalida'),)
False
False
False
False


class Inventario(models.Model):
    id = models.AutoField()
    coste = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaentrada = models.DateTimeField(db_column='fechaEntrada', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='Pedido_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventario'
        unique_together = (('id', 'proveedor', 'producto', 'pedido'),)



class Notificacion(models.Model):
    id = models.AutoField()
    estadomensaje = models.ForeignKey('Estadomensaje', models.DO_NOTHING, db_column='estadoMensaje_id')  # Field name made lowercase.
    tipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='tipoUsuario_id')  # Field name made lowercase.
    mensaje = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Notificacion'
        unique_together = (('id', 'estadomensaje', 'tipousuario'),)
False
False
False
False


class Pedido(models.Model):
    id = models.AutoField()
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estadopedido = models.ForeignKey('Estadopedido', models.DO_NOTHING, db_column='estadoPedido_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pedido'
        unique_together = (('id', 'estadopedido', 'producto', 'proveedor'),)
False
False
False
False


class Producto(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipoProducto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
        unique_together = (('id', 'tipoproducto'),)
False
False
False
False


class Promocion(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    observaciones = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Promocion'
False
False
False
False


class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Proveedor'
False
False
False
False


class Publicidad(models.Model):
    id = models.AutoField()
    fechainicio = models.DateTimeField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    promocion = models.ForeignKey(Promocion, models.DO_NOTHING, db_column='Promocion_id')  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Publicidad'
        unique_together = (('id', 'promocion', 'cliente'),)
False
False
False
False



False
False
False
False


class Tratamiento(models.Model):
    id = models.AutoField()
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='Maquina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tratamiento'
        unique_together = (('id', 'maquina'),)
False
False
False
False


class Estadocita(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadoCita'
False
False
False
False


class Estadofactura(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadoFactura'
False
False
False
False


class Estadomensaje(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadoMensaje'
False
False
False
False


class Estadopedido(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadoPedido'
False
False
False
False


class Tipoempleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoEmpleado'



class Tipoproducto(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoProducto'
False
False
False
False


class Tipousuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoUsuario'
