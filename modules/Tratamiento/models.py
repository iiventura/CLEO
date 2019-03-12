from django.db import models
from ..Maquina.models import Maquina
from ..Producto.models import Producto

# Create your models here.
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