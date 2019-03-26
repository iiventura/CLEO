from django.db import models

# Create your models here.

class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45, blank=True, null=True)
    nombre = models.CharField(unique=True,max_length=45, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Promocion'
        unique_together = (('codigo','nombre'),)