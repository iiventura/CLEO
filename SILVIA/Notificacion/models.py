from django.db import models

# Create your models here.
class Estadomensaje(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadomensaje'

class Tipousuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipousuario'

class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    estadomensaje = models.ForeignKey(Estadomensaje, models.DO_NOTHING, db_column='estadoMensaje_id')  # Field name made lowercase.
    tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='tipoUsuario_id')  # Field name made lowercase.
    mensaje = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'
        unique_together = (('id', 'estadomensaje', 'tipousuario'),)