from django.db import models

class Maquina(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipomaquina = models.ForeignKey('Tipomaquina', models.DO_NOTHING, db_column='tipoMaquina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maquina'
        unique_together = (('tipomaquina'),)

class Tipomaquina(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoMaquina'