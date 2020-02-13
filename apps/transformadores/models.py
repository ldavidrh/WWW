from django.db import models

# Create your models here.
class transformador(models.Model):
    num_serie = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=30, null=False)
    activo = models.BooleanField(default=True)

    estacion = models.ForeignKey('subestaciones.Subestacion', null=True, on_delete=models.SET_NULL)