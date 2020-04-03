from django.shortcuts import render, redirect
from django.contrib import messages
from .form import FormularioRegistroSubestacion
from .models import Subestacion
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import json


class SubestacionSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    latitud = serializers.DecimalField(max_digits=18, decimal_places=15)
    longitud = serializers.DecimalField(max_digits=18, decimal_places=15)
    activo = serializers.BooleanField()
    
# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroSubestacion(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request, 'Subestacion registrada exitosamente')
            return redirect('subestaciones:registrar')
        else:
            messages.error(request, 'Error al agregar subestación')
    else:
        form = FormularioRegistroSubestacion()

    return render(request, 'subestaciones/registrar.html', {'form':form})

def consultar_view(request):
    subestaciones = Subestacion.objects.all()
    serializer = SubestacionSerializer(subestaciones, many=True)
    return render(request, 'subestaciones/consultar.html', {'subestaciones':subestaciones, "jsonsubestaciones":serializer.data})

def eliminar_view(request, id):
    try:
        subestacion = Subestacion.objects.get(pk=id)
        subestacion.activo = False
        subestacion.save()
        messages.success(request, 'La subestacion se ha desactivado exitosamente')
        
    except:
        messages.error(request, 'Error al desactivar la subestacion')

    return redirect('subestaciones:consultar')
    
def actualizar_view(request, id):
    subestacion = Subestacion.objects.get(pk=id)
    if request.method == 'POST':
        form = FormularioRegistroSubestacion(request.POST, instance=subestacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Subestacion actualizada exitosamente")
            return redirect('subestaciones:consultar')
        else:
            messages.error(request, "Error al actualizar subestacion")
    else:
        form = FormularioRegistroSubestacion()
    serializer = SubestacionSerializer(subestacion)
    print(serializer.data)
    return render(request, 'subestaciones/actualizar.html', {'form':form, 'subestacion':serializer.data})



