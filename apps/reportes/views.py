from django.shortcuts import render
from apps.api.models import *
from apps.facturas.models import *
from apps.subestaciones.models import *
from apps.transformadores.models import *
from apps.Usuarios.models import *
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def reporte1(request):
    return render(request, 'reporte1.html', {})

