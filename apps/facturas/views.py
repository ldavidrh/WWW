from django.shortcuts import render, redirect
from django.contrib import messages
from apps.Usuarios.models import * 
from apps.api.models import * 
from .models import *
from random import randint, uniform,random

def Menu(request):

    return render(request, 'facturas/GenerarFacturas.html', {})


def GenerarFacturas(request):

    contratos = Contrato.objects.filter(en_servicio=True)

    for contrato in contratos:
        
        #Creamos el consumo

        lectura_anterior = Consumo.objects.filter(contador=contrato.contador).last()
        ran = randint(200,300)

        if lectura_anterior != None:

            lectura_actual = ran + lectura_anterior.lectura_actual
            consumo = Consumo(contador=contrato.contador, lectura_actual=lectura_actual, lectura_anterior=lectura_anterior.lectura_actual)
            consumo.save()

        else:
            consumo = Consumo(contador=contrato.contador, lectura_actual=ran, lectura_anterior=0)
            consumo.save()

        #Creamos la diferencia

        diferencia = consumo.lectura_actual - consumo.lectura_anterior

        #Dias de mora

        morosos = Mora.objects.all()

        cargo = 0

        if morosos != None:
            for m in morosos:
                if m.factura.contrato == contrato:
                    cargo = m.dias_retraso/100 * m.factura.total


        #Total

        total = diferencia*550 + cargo

        #Creamos la factura

        factura = Factura(contrato=contrato, consumo=consumo, diferencia=diferencia, cargo_mora=cargo, total=total, pagada=False)
        factura.save()

    messages.success(request, 'Facturas creadas exitosamente')
    return redirect('usuarios:home')

        
