from django.db import models

# Create your models here.

class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=45, blank=True, null=True)
    nombre = models.CharField(unique=True,max_length=45, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)

    def str(self):
        return f'{ self.nombre } promocion '

    class Meta:
        db_table = 'Promocion'
        unique_together = (('codigo','nombre'),)
