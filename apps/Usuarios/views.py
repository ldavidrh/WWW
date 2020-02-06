from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import FormularioRegistroClientes, FormularioRegistroEmpleados, FormularioEditarEmpleado
from django.contrib.auth import login
from .models import Empleados, Clientes 

def home(request):
    
    return render(request, 'base.html', {})


def CrearEmpleado(request):
    if request.method == 'POST':
        form = FormularioRegistroEmpleados(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            cedula = form.cleaned_data.get('cedula')
            a.username = cedula
            rol = form.cleaned_data.get('roles')
            if rol == 'gerente' or rol == 'administrador':
                a.is_superuser = True
            a.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('usuarios:home')
    else:
        form = FormularioRegistroEmpleados()

    return render(request, 'Usuarios/CrearUsuario.html', {'form': form})

def ListaEmpleado(request):
    usuarios = Empleados.objects.all()
    return render(request, 'Usuarios/ListaEmpleados.html', {'usuarios': usuarios})

def EditarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    if request.method == 'POST':
        form = FormularioEditarEmpleado(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta actualizada!')
            return redirect('usuarios:ListaEmpleado')

    else:
        form = FormularioEditarEmpleado(instance=usuario)

    return render(request, 'Usuarios/EditarEmpleado.html', {'form': form})

def EliminarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    usuario.is_active = False
    usuario.save()

    return redirect('usuarios:ListaEmpleado')

def ActivarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    usuario.is_active = True
    usuario.save()

    return redirect('usuarios:ListaEmpleado')

def Perfil(request):
    usuario = request.user 

    return render(request, 'Usuarios/Perfil.html', {'usuario': usuario})
