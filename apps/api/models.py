from django.db import models
from apps.Usuarios.models import * 


class Contador(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()

class Consumo(models.Model):
    contador = models.ForeignKey(Contador, on_delete=models.CASCADE)
    lectura_actual = models.DecimalField(decimal_places=1, max_digits=300)
    lectura_anterior = models.DecimalField(decimal_places=1, max_digits=300)
    fecha_lectura = models.DateField(auto_now=True)




