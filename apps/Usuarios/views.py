from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import FormularioRegistroClientes, FormularioRegistroEmpleados, FormularioEditarEmpleado
from django.contrib.auth import login
from .models import Empleados, Clientes, Contrato

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


def CrearCliente(request):
    if request.method == 'POST':
        
        datos = request.POST
        direccion = datos['direccion']
        nombre = datos['nombre']
        apellido = datos['apellido']
        correo = datos['correo']
        telefono = datos['telefono']
        rol= datos['tipo']
        cedula = datos['cedula']
   
        a = Clientes(first_name=nombre, last_name=apellido, tipo=rol, email=correo, cedula=cedula, telefono=telefono, username=cedula)
        a.save()
        contrato = Contrato(cliente=a, direccion=direccion)
        contrato.save()
        
        messages.success(request, 'Solicitud creada exitosamente, le notificaremos cuando se haya aprobado')
        return redirect('usuarios:home')
    
    return render(request, 'Usuarios/CrearCliente.html', {})

def ListaSolicitudCliente(request):
    #clientes = Clientes.objects.filter(aprobado=False).select_related('contrato')
    clientes = Contrato.objects.filter(cliente__aprobado=False)
    return render(request, 'Usuarios/ListaAprobar.html', {'clientes': clientes})

def ListaCliente(request):
    #clientes = Clientes.objects.filter(aprobado=False).select_related('contrato')
    clientes = Contrato.objects.filter(cliente__aprobado=True)
    return render(request, 'Usuarios/ListaClientes.html', {'clientes': clientes})

def AceptarCliente(request,pk):
    usuario = Clientes.objects.get(cedula=pk)
    usuario.aprobado = True
    usuario.save()

    messages.success(request, 'Cliente aprobado!')
    return redirect('usuarios:ListaSolicitudCliente')

def RechazarCliente(request, pk):
    usuario = Clientes.objects.get(cedula=pk)
    contrato = Contrato.objects.get(cliente=usuario)
    contrato.delete()
    usuario.delete()

    messages.success(request, 'Cliente rechazado!')
    return redirect('usuarios:ListaSolicitudCliente')