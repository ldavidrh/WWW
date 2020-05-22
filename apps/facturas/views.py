from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from apps.Usuarios.models import * 
from apps.api.models import * 
from .models import *
from random import randint, uniform,random
from django.db import transaction
#from datetime import datetime
from datetime import *
from dateutil.relativedelta import *
import calendar
from decimal import Decimal
#from datetime import date

def Menu(request):

    hoy =  date.today()
    dia = hoy.day

    if dia == 22:
        facturas = Factura.objects.filter(fecha=hoy)
        if len(facturas) == 0 or len(facturas) == None:
            bandera = True
        else:
            bandera = False    
    else:
        bandera = False

    return render(request, 'facturas/GenerarFacturas.html', {'hoy': hoy, 'bandera': bandera })


def GenerarFacturas(request):

    contratos = Contrato.objects.filter(en_servicio=True)
    hoy = date.today()


    for contrato in contratos:

        facturas_sin_pagar = Facturas.objects.filter(contrato=contrato, pagada=False)
        x = len(facturas_sin_pagar)
        d1 = 0
        d2 = 0
        bandera = True
        crear = True
        if x == 2:
            for f in facturas_sin_pagar:
                if bandera:
                    d1 = abs(hoy - f.fecha).days
                else:
                    d2 = abs(hoy - f.fecha).days
                bandera = False
            
            if d1 > 28 and d2 > 28:
                f.contrato.en_servicio = False
                f.save()
                crear = False

        if crear:
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

            cargo = 0
            
            #Total

            total = diferencia*550 + cargo

            #Creamos la factura

            factura = Factura(contrato=contrato, consumo=consumo, diferencia=diferencia, cargo_mora=cargo, total=total, pagada=False)
            factura.save()

    messages.success(request, 'Facturas creadas exitosamente')
    return redirect('usuarios:home')

@transaction.atomic
def PagoFactura1(request):
    if request.method == 'POST':
        datos = request.POST
        idcontrato = datos['contrato']
        
        try:
            contrato = Contrato.objects.get(id=idcontrato)

            facturas_sin_pagar = Factura.objects.filter(contrato=contrato, pagada=False)

            cantidad = len(facturas_sin_pagar)

            if cantidad == 0 or cantidad == None:
                msj = "No tienes facturas por pagar"
                
                return render(request, "facturas/pago2.html", {'msj': msj})
            
            elif cantidad == 1:
                hoy =  date.today()
                diferencia = 0

                for f in facturas_sin_pagar:
                    if hoy != f.fecha:
                        diferencia = abs(hoy - f.fecha).days

                    if diferencia > 30:
                        diferencia = 30 
                        f.cargo_mora = round(f.total*0.30)
                        f.save()
                        f.total = f.total + f.cargo_mora
                        f.save()
                    else:
                        f.cargo_mora = round(Decimal(diferencia/100) * f.total)
                        f.save()
                        f.total = f.total + f.cargo_mora
                        f.save()
                
                msj = "Su factura tiene "+str(diferencia)+" dias de retraso" 
                
                return render(request, "facturas/pago3.html", {'id': idcontrato, 'facturas': facturas_sin_pagar, 'msj': msj, 'diferencia': diferencia, 'hoy': hoy})

            elif cantidad == 2:

                hoy =  date.today()
                diferencia1 = 0
                diferencia2 = 0
                bandera = True
                total = 0

                for f in facturas_sin_pagar:
                    if bandera:
                        if hoy != f.fecha:
                            diferencia1 = abs(hoy - f.fecha).days

                        if diferencia1 > 30:
                            diferencia1 = 30 
                            f.cargo_mora = round(f.total*0.30)
                            f.save()
                            f.total = f.total + f.cargo_mora
                            f.save()
                            total = total + f.total
                        else:
                            f.cargo_mora = round(Decimal(diferencia1/100) * f.total)
                            f.save()
                            f.total = f.total + f.cargo_mora
                            f.save() 
                            total = total + f.total
                    else:
                        if hoy != f.fecha:
                            diferencia2 = abs(hoy - f.fecha).days

                        if diferencia2 > 30:
                            diferencia2 = 30 
                            f.cargo_mora = round(f.total*0.30)
                            f.save()
                            f.total = f.total + f.cargo_mora
                            f.save()
                            total = total + f.total
                        else:
                            f.cargo_mora = round(Decimal(diferencia2/100) * f.total)
                            f.save()
                            f.total = f.total + f.cargo_mora
                            f.save()
                            total = total + f.total
                    bandera = False
                
                r = False
                if diferencia1 > 30 and diferencia2 > 30:
                    total = total + 34000
                    r = "$34.000"
                    msj = "Sus facturas tienen "+str(diferencia1+diferencia2)+" dias de retraso, la reactivación del servicio cuesta $34.000"
                else:
                    msj = "Sus facturas tienen "+str(diferencia1+diferencia2)+" dias de retraso"

                return render(request, "facturas/pago3.html", {'id': idcontrato, 'facturas': facturas_sin_pagar, 'msj': msj, 'diferencia1': diferencia1, 'hoy': hoy, 'diferencia2': diferencia2, 'total': total, 'r': r})

        except:
            messages.error(request, 'Numero de contrato invalido')

    return render(request, "facturas/pago1.html", {})

@transaction.atomic
def PagoFactura2(request):

    if request.method == 'POST':
        datos = request.POST
        idcontrato = datos['contrato']

        contrato = Contrato.objects.get(id=idcontrato)

        facturas_sin_pagar = Factura.objects.filter(contrato=contrato, pagada=False)

        contrato.en_servicio = True
        contrato.save()

        for f in facturas_sin_pagar:
            f.pagada = True
            f.save()
        
        messages.success(request, 'Facturas pagadas!')
        return redirect('landing')



    return redirect('landing')

def ConsultarFactura(request, idcontrato):
    
    factura = Factura.objects.get(id=1)

    contrato = Contrato.objects.get(id = idcontrato)
    
    facturas_sin_pagar = Factura.objects.filter(contrato=contrato, pagada=False)

    cantidad = len(facturas_sin_pagar)

    if cantidad == 0 or cantidad == None:
        msj = "No tienes facturas por pagar"
        
        return render(request, "facturas/pago2.html", {'msj': msj})
        
    elif cantidad == 1:
        dif_lectura = 0
        total = 0
        r = "$0"
        for f in facturas_sin_pagar:
            hoy =  f.fecha
            dif_lectura = f.consumo.lectura_actual - f.consumo.lectura_anterior
            total = dif_lectura*550
            
            return render(request, 'facturas/invoice.html', {'contrato': contrato, 'facturas': facturas_sin_pagar, 'dif_lectura': dif_lectura, 'subtotal1': total, 'r':r, 'hoy':hoy})

    elif cantidad == 2:

        diferencia1=0
        diferencia2=0
        dif_lectura1 = 0
        dif_lectura2 = 0
        subtotal1 = 0
        subtotal2 = 0
        bandera = True
        total = 0

        for f in facturas_sin_pagar:
            hoy =  f.fecha
            if bandera:
                dif_lectura1 = f.consumo.lectura_actual - f.consumo.lectura_anterior
                subtotal1 = dif_lectura1*550
                diferencia1 = abs(hoy - f.fecha).days

                total = total + f.total
                
            else:
                dif_lectura2 = f.consumo.lectura_actual - f.consumo.lectura_anterior
                subtotal2 = dif_lectura2*550
                diferencia2 = abs(hoy - f.fecha).days
                
                total = total + f.total
            bandera = False
                    
        r = "$0"
        if diferencia1 > 30 and diferencia2 > 30:
            total = total + 34000
            r = "$34.000"

        return render(request, 'facturas/invoice.html', {'contrato': contrato, 'facturas': facturas_sin_pagar, 'subtotal1': subtotal1, 'subtotal2': subtotal2, 'total': total, 'r': r, 'hoy': hoy})
     
    #return render(request, 'facturas/invoice.html', {'contrato': contrato, 'facturas': facturas_sin_pagar})



            



            










