from django.db import models

class Maquina(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipozona = models.ForeignKey('TipoZona', models.DO_NOTHING, db_column='TipoZona_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maquina'
        unique_together = (('tipozona'),)

class TipoZona(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoZona'