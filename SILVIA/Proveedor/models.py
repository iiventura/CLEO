from django.db import models

# Create your models here.

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
        unique_together = (('nombre'),)
