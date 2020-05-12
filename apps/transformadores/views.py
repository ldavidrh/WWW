from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioRegistroTransformador, FormularioActualizacionTransformador
from .models import Transformador
from .serializer import TransformadorSerializer
from django.core import serializers

# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroTransformador(request.POST)
        if form.is_valid():
            transformador = form.save(commit=False)
            subestacion = form.cleaned_data.get('subestacion')
            if subestacion is None:
                transformador.save()
            else:
                transformador.latitud = subestacion.latitud
                transformador.longitud = subestacion.longitud
                transformador.save()
            messages.success(request, 'Transformador registrado exitosamente')
            return redirect('transformadores:registrar')
        else:
            messages.error(request, 'Error al registrar el transformador')
    else:
        form = FormularioRegistroTransformador()
    
    return render(request, 'transformadores/registrar.html', {'form':form})

def consultar_view(request):
    transformadores = Transformador.objects.all()
    jsontransformadores = serializers.serialize('json', transformadores)
    return render(request, 'transformadores/consultar.html', {'transformadores':transformadores, 'jsontransformadores': jsontransformadores})

def eliminar_view(request, serial):
    try:
        transformador = Transformador.objects.get(pk=serial)
        transformador.activo = False
        transformador.subestacion = None
        transformador.latitud = None
        transformador.longitud = None
        transformador.save()
        messages.success(request, 'Transformador desactivado exitosamente')
    except:
        messages.error(request, 'Error al desactivar transformador')

    return redirect('transformadores:consultar')

def actualizar_view(request, serial):
    transformador = Transformador.objects.get(pk=serial)
    if request.method == 'POST':
        form = FormularioActualizacionTransformador(request.POST, instance = transformador)
        if form.is_valid():
            transformador = form.save(commit=False)
            subestacion = form.cleaned_data.get('subestacion')
            if subestacion is None:
                transformador.save()
            else:
                transformador.latitud = subestacion.latitud
                transformador.longitud = subestacion.longitud
                transformador.save()
            messages.success(request, 'Transformador actualizado exitosamente')
            return redirect('transformadores:consultar')
        else:
            messages.error(request, 'Error al actualizar transformador')
    else:
        form = FormularioActualizacionTransformador()
        jsontransformador = serializers.serialize('json', [transformador,])
    return render(request, 'transformadores/actualizar.html', {'form':form, 'transformador':jsontransformador})
