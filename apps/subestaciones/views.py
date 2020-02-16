from django.shortcuts import render, redirect
from django.contrib import messages
from .form import FormularioRegistroSubestacion

# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroSubestacion(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request, 'Subestacion registrada exitosamente')
            return redirect('subestaciones:registrar')
        else:
            messages.error(request, 'Error al agregar subestacion')
    else:
        form = FormularioRegistroSubestacion()

    return render(request, 'subestaciones/registrar.html', {'form':form})