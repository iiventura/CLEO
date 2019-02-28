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
        db_table = 'Cita'
        unique_together = (('id', 'estadocita', 'sala', 'cliente', 'empleado', 'tratamiento', 'horarioentrada', 'horariosalida'),)
False
False
False
False


class Cliente(models.Model):
    dni = models.CharField(unique=True, max_length=9)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    puntuacion = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Cliente'
False
False
False
False


class Empleado(models.Model):
    id = models.AutoField()
    dni = models.CharField(unique=True, max_length=9)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    tipoempleado = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='tipoEmpleado_id')  # Field name made lowercase.
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Empleado'
        unique_together = (('id', 'tipoempleado'),)
False
False
False
False


class Factura(models.Model):
    id = models.AutoField()
    costeporcobrar = models.FloatField(db_column='costePorCobrar', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
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
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Horario'
False
False
False
False


class Horarioempleado(models.Model):
    id = models.AutoField()
    fecha = models.DateField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_id')  # Field name made lowercase.
    horarioentrada = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioEntrada_id')  # Field name made lowercase.
    horariosalida = models.ForeignKey(Horario, models.DO_NOTHING, db_column='HorarioSalida_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HorarioEmpleado'
        unique_together = (('id', 'empleado', 'horarioentrada', 'horariosalida'),)
False
False
False
False


class Inventario(models.Model):
    id = models.AutoField()
    coste = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fechaentrada = models.DateField(db_column='fechaEntrada', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='Pedido_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventario'
        unique_together = (('id', 'proveedor', 'producto', 'pedido'),)
False
False
False
False


class Maquina(models.Model):
    id = models.AutoField()
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    tipomaquina = models.ForeignKey('Tipomaquina', models.DO_NOTHING, db_column='tipoMaquina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maquina'
        unique_together = (('id', 'tipomaquina'),)
False
False
False
False


class Notificacion(models.Model):
    id = models.AutoField()
    estadomensaje = models.ForeignKey('Estadomensaje', models.DO_NOTHING, db_column='estadoMensaje_id')  # Field name made lowercase.
    tipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='tipoUsuario_id')  # Field name made lowercase.
    mensaje = models.TextField(blank=True, null=True)

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
    fecha = models.DateField(blank=True, null=True)
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
    codigo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipoproducto = models.ForeignKey('Tipoproducto', models.DO_NOTHING, db_column='tipoProducto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Producto'
        unique_together = (('id', 'codigo', 'tipoproducto'),)
False
False
False
False


class Promocion(models.Model):
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    observaciones = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Promocion'
False
False
False
False


class Proveedor(models.Model):
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
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
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
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


class Sala(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sala'
False
False
False
False


class Tratamiento(models.Model):
    id = models.AutoField()
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    maquina = models.ForeignKey(Maquina, models.DO_NOTHING, db_column='Maquina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tratamiento'
        unique_together = (('id', 'maquina'),)
False
False
False
False


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'
False
False
False
False


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
False
False
False
False


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
False
False
False
False


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
False
False
False
False


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
False
False
False
False


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
False
False
False
False


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'
False
False
False
False


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
False
False
False
False


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
False
False
False
False


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
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
False
False
False
False


class Tipomaquina(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoMaquina'
False
False
False
False


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
