from django.db import models

class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True,max_length=45, blank=True, null=True)

    def str(self):
        return f'{ self.nombre } sala '

    class Meta:
        db_table = 'Sala'
        unique_together = (('id', 'nombre'),)
