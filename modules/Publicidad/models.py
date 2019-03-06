from django.db import models
from ..Promocion.models import Promocion
from  ..Cliente.models import Cliente

# Create your models here.
class Publicidad(models.Model):
    id = models.AutoField(primary_key=True)
    #fechainicio = models.CharField(unique=True, max_length=10, blank=True,null=True)
    #fechafin = models.CharField(unique=True, max_length=10, blank=True, null=True)
    fechainicio = models.DateField(db_column='fechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    promocion = models.ForeignKey(Promocion, models.DO_NOTHING, db_column='Promocion_id')  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publicidad'
        unique_together = (('id', 'promocion', 'cliente'),)