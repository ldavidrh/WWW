from django.db import models

# Create your models here.


class Transformador(models.Model):
    serial = models.CharField(max_length=10, primary_key=True)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    marca = models.CharField(max_length=30, null=False)
    # TIPO DEVANADO
    ELEVADOR = "elevador"
    REDUCTOR = "reductor"
    DEVANADO_CHOICES = [
        (ELEVADOR, 'Elevador'),
        (REDUCTOR, 'Reductor')
    ]

    devanado = models.CharField(
        max_length=10,
        choices=DEVANADO_CHOICES,
        default=ELEVADOR
    )

    subestacion = models.ForeignKey('subestaciones.Subestacion', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.marca

    activo = models.BooleanField(default=True)
