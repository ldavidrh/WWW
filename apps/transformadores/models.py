from django.db import models

# Create your models here.
class transformador(models.Model):
    num_serie = models.CharField(max_length=10, primary_key=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    marca = models.CharField(max_length=30, null=False)
    activo = models.BooleanField(default=True)

    subestacion = models.ForeignKey('subestaciones.Subestacion', null=True, on_delete=models.SET_NULL)