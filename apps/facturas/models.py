from django.db import models
from apps.Usuarios.models import * 
from apps.api.models import * 

class Factura(models.Model):

    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT)
    consumo = models.ForeignKey(Consumo, on_delete=models.PROTECT) 
    diferencia = models.BigIntegerField()
    cargo_mora = models.DecimalField(decimal_places=1, max_digits=300)
    total = models.DecimalField(decimal_places=1, max_digits=300)
    pagada = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)


class Mora(models.Model):

    factura = models.ForeignKey(Factura, on_delete=models.PROTECT)
    dias_retraso = models.BigIntegerField()