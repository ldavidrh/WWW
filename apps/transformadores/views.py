from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioRegistroTransformador

# Create your views here.
def registrar_view(request):
    if request.method == 'POST':
        form = FormularioRegistroTransformador(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transformador registrado exitosamente')
            return redirect('transformadores:registrar')
        else:
            messages.error(request, 'Error al registrar el transformador')

    else:
        form = FormularioRegistroTransformador()

    return render(request, 'transformadores/registrar.html', {'form':form})

        