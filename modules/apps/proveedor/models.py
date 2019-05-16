from django.db import models

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=45, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    borrado = models.IntegerField(blank=True, null=True)

    def str(self):
        return f'{ self.nombre } {self.contacto } proveedor '

    class Meta:
        db_table = 'Proveedor'
        unique_together = (('id','nombre'),)
