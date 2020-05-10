from django.db import models

# Create your models here.
class Transformador(models.Model):
    serial = models.CharField(max_length=10, primary_key=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    marca = models.CharField(max_length=30, null=False)
    activo = models.BooleanField(default=True)


    #TIPO DEVANADO
    ELEVADOR = "elevador"
    REDUCTOR = "reductor"
    DEVANADO_CHOICES=[
        (ELEVADOR, 'Elevador'),
        (REDUCTOR, 'Reductor')
    ]


    devanado = models.CharField(
        max_length = 10,
        choices = DEVANADO_CHOICES,
        default = ELEVADOR
    )

    subestacion = models.ForeignKey('subestaciones.Subestacion', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.marca