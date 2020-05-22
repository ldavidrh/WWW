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

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def reporte2Menu(request):
    contratos = Contrato.objects.all()
    return render(request, 'reporte2Menu.html', {'contratos': contratos})

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def reporte2(request, pk):

    contador = Contador.objects.get(contrato__id=pk)
    contrato = Contrato.objects.get(id=pk)

    mes0 = datetime.now().month
    mes1 = (datetime.now()+relativedelta(months=-1)).month
    mes2 = (datetime.now()+relativedelta(months=-2)).month
    mes3 = (datetime.now()+relativedelta(months=-3)).month
    mes4 = (datetime.now()+relativedelta(months=-4)).month
    
    consumo_mes0 = Consumo.objects.filter(contador=contador, fecha_lectura__month=mes0).last()
    consumo_mes1 = Consumo.objects.filter(contador=contador, fecha_lectura__month=mes1).last()
    consumo_mes2 = Consumo.objects.filter(contador=contador, fecha_lectura__month=mes2).last()
    consumo_mes3 = Consumo.objects.filter(contador=contador, fecha_lectura__month=mes3).last()
    consumo_mes4 = Consumo.objects.filter(contador=contador, fecha_lectura__month=mes4).last()
    

    consumos = [consumo_mes0, consumo_mes1, consumo_mes2, consumo_mes3, consumo_mes4]
    diferencias = []

    for c in consumos:
        if c:
            diferencias.append(float(c.lectura_actual - c.lectura_anterior))
        else:
            diferencias.append(0)

    diferencias.reverse()
    meses = [switch_mes(mes4), switch_mes(mes3), switch_mes(mes2), switch_mes(mes1), switch_mes(mes0)]

    print(meses)
    print(diferencias)

    return render(request, 'reporte2.html', {'contrato': contrato, 'consumos': diferencias, 'meses': meses})

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def reporte3(request):
    clientes_activo = Clientes.objects.filter(aprobado = 'True').count()
    clientes_inactivo = Clientes.objects.filter(aprobado = 'False').count()

    clientes = [clientes_activo, clientes_inactivo]
    base = ['Clientes_Activos', 'Clientes_Inactivos']

    return render(request, 'reporte3.html', {'clientes': clientes, 'base': base})


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
