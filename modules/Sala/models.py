from django.db import models

class Sala(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sala'
