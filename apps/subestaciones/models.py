from django.db import models

# Create your models here.
class Subestacion(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True)
    latitud = models.DecimalField(max_digits=18, decimal_places=15)
    longitud = models.DecimalField(max_digits=18, decimal_places=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
       return self.nombre
    