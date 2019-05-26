from django.db import models

# Create your models here.
class Estadomensaje(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'estadomensaje'

class Tipousuario(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'tipousuario'

class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    estadomensaje = models.ForeignKey(Estadomensaje, models.DO_NOTHING, db_column='estadoMensaje_id')  # Field name made lowercase.
    tipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='tipoUsuario_id')  # Field name made lowercase.
    mensaje = models.TextField(blank=True, null=True)

    def str(self):
        return f'{ self.tipousuario } notificacion '

    class Meta:
        db_table = 'notificacion'
        unique_together = (('id', 'estadomensaje', 'tipousuario'),)

def cargar_Estadomensaje():
    if Estadomensaje.objects.count()==0:
        Estadomensaje(nombre='Leido').save()
        Estadomensaje(nombre=' No leido').save()

def cargar_Tipousuario():
    if Tipousuario.objects.count()==0:
        Tipousuario(nombre='Cliente').save()
        Tipousuario(nombre='Encargado').save()

cargar_Estadomensaje()
cargar_Tipousuario()