from django.db import models

# Create your models here.
class Subestacion(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    latitud = models.FloatField()
    longitud = models.FloatField()
    activo = models.BooleanField(default=True)