from django.shortcuts import render
from apps.api.models import *
from apps.facturas.models import *
from apps.subestaciones.models import *
from apps.transformadores.models import *
from apps.Usuarios.models import *
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.decorators import login_required, permission_required
from datetime import *; from dateutil.relativedelta import *
import calendar

# Create your views here.

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def reporte1(request):
    mes1 = (datetime.now()).month
    mes2 = (datetime.now()+relativedelta(months=-1)).month
    mes3 = (datetime.now()+relativedelta(months=-2)).month
    mes4 = (datetime.now()+relativedelta(months=-3)).month
    mes5 = (datetime.now()+relativedelta(months=-4)).month

    consumo_mes1 = Consumo.objects.filter(fecha_lectura__month=mes1)
    consumo_mes2 = Consumo.objects.filter(fecha_lectura__month=mes2)
    consumo_mes3 = Consumo.objects.filter(fecha_lectura__month=mes3)
    consumo_mes4 = Consumo.objects.filter(fecha_lectura__month=mes4)
    consumo_mes5 = Consumo.objects.filter(fecha_lectura__month=mes5)


    pr = [consumo_mes1, consumo_mes2, consumo_mes3, consumo_mes4, consumo_mes5]
    valores = []    
    

    for m in pr:
        suma = 0
        if m:
            for n in m:
                a = n.lectura_actual - n.lectura_anterior
                suma = suma+a
            valores.append(float(suma))
        else:
            valores.append(0)    

    valores.reverse()            
    meses = [switch_mes(mes5), switch_mes(mes4), switch_mes(mes3), switch_mes(mes2), switch_mes(mes1)]

    return render(request, 'reporte1.html', {'cantidad': valores, 'meses': meses})

def switch_mes(argument):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octobre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return switcher.get(argument, "Invalid month")

