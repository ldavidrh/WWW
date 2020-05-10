from django.db import models
from apps.Usuarios.models import * 
from apps.api.models import * 

class Factura(models.Model):

    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT)
    consumo = models.ForeignKey(Consumo, on_delete=models.PROTECT) 
    diferencia = models.IntegerField
    dias_mora = models.IntegerField
    total = models.DecimalField(decimal_places=1, max_digits=300)
    pagada = models.BooleanField
    fecha = models.DateField(auto_now=True)