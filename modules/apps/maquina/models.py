from django.db import models

class TipoZona(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre  } '

    class Meta:
        db_table = 'tipozona'


class Maquina(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fechaingreso = models.DateField(db_column='fechaIngreso', blank=True, null=True)  # Field name made lowercase.
    tipozona = models.ForeignKey('TipoZona', models.DO_NOTHING, db_column='tipoZona_id')  # Field name made lowercase.

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        db_table = 'maquina'
        unique_together = (('id', 'tipozona'),)



def cargar_TipoZona():
    if TipoZona.objects.count()==0:
        TipoZona(nombre='Corporal').save()
        TipoZona(nombre='Facial').save()



cargar_TipoZona()