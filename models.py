
from django.db import models




class Cita(models.Model):
    id = models.AutoField()
    fecha = models.DateField(blank=True, null=True)
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
        unique_together = (('id', 'estadocita', 'sala', 'cliente', 'empleado', 'horarioentrada', 'horariosalida', 'tratamiento'),)


class Estadocita(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadocita'


class Estadofactura(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadofactura'


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


class Factura(models.Model):
    id = models.AutoField()
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estadofactura = models.ForeignKey(Estadofactura, models.DO_NOTHING, db_column='estadoFactura_id')  # Field name made lowercase.
    cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='Cita_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'factura'
        unique_together = (('id', 'estadofactura', 'cita'),)


class Horario(models.Model):
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Horarioempleado(models.Model):
    id = models.AutoField()
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    tipohorarioempleado = models.ForeignKey('Tipohorarioempleado', models.DO_NOTHING, db_column='tipoHorarioEmpleado_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'horarioempleado'
        unique_together = (('id', 'empleado', 'tipohorarioempleado'),)


class Inventario(models.Model):
    id = models.AutoField()
    coste = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaentrada = models.DateField(db_column='fechaEntrada', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='Pedido_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('id', 'pedido'),)


class Maquina(models.Model):
    id = models.AutoField()
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    tipozona = models.ForeignKey('Tipozona', models.DO_NOTHING, db_column='tipoZona_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maquina'
        unique_together = (('id', 'tipozona'),)


class Notificacion(models.Model):
    id = models.AutoField()
    estadomensaje = models.ForeignKey(Estadomensaje, models.DO_NOTHING, db_column='estadoMensaje_id')  # Field name made lowercase.
    tipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='tipoUsuario_id')  # Field name made lowercase.
    mensaje = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'
        unique_together = (('id', 'estadomensaje', 'tipousuario'),)


class Pedido(models.Model):
    id = models.AutoField()
    cantidad = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estadopedido = models.ForeignKey(Estadopedido, models.DO_NOTHING, db_column='estadoPedido_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido'
        unique_together = (('id', 'estadopedido', 'producto'),)


class Producto(models.Model):
    id = models.AutoField()
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipoProducto_id')  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    borrado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto'
        unique_together = (('id', 'codigo', 'tipoproducto', 'proveedor'),)


class Promocion(models.Model):
    codigo = models.CharField(unique=True, max_length=45, blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocion'


class Proveedor(models.Model):
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    borrado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Publicidad(models.Model):
    id = models.AutoField()
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    promocion = models.ForeignKey(Promocion, models.DO_NOTHING, db_column='Promocion_id')  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publicidad'
        unique_together = (('id', 'cliente', 'promocion'),)


class Sala(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Stock(models.Model):
    id = models.AutoField()
    cantprov = models.IntegerField(db_column='cantProv', blank=True, null=True)  # Field name made lowercase.
    canttotal = models.IntegerField(db_column='cantTotal', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('id', 'proveedor', 'producto'),)


class Tipoempleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoempleado'


class Tipohorarioempleado(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipohorarioempleado'


class Tipoproducto(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoproducto'


class Tipousuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Tipozona(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipozona'


class Tratamiento(models.Model):
    id = models.AutoField()
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='Maquina_id')  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tratamiento'
        unique_together = (('id', 'maquina', 'producto'),)
