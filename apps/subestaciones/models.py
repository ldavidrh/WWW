from django.db import models

# Create your models here.
class Subestacion(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True)
    latitud = models.FloatField(null = False)
    longitud = models.FloatField(null = False)
    activo = models.BooleanField(default=True)

    def __str__(self):
       return self.nombre
    