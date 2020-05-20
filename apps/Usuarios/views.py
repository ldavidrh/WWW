from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required
from .forms import FormularioRegistroEmpleados, FormularioEditarEmpleado
from django.contrib.auth import login
import requests, json
from .models import Empleados, Clientes, Contrato, Persona
from apps.api.models import Contador, Consumo



def home(request):

    return render(request, 'base.html', {})

def landing(request):
    return render(request, 'landing.html', {})

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
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

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def ListaEmpleado(request):
    usuarios = Empleados.objects.all()
    return render(request, 'Usuarios/ListaEmpleados.html', {'usuarios': usuarios})

@login_required
def EditarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    if request.method == 'POST':
        form = FormularioEditarEmpleado(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            a = form.save(commit=False)
            rol = form.cleaned_data.get('roles')
            if rol == 'gerente' or rol == 'administrador':
                a.is_superuser = True
            else:
                a.is_superuser = False
            a.save()
            messages.success(request, 'Cuenta actualizada!')
            return redirect('usuarios:ListaEmpleado')

    else:
        form = FormularioEditarEmpleado(instance=usuario)

    return render(request, 'Usuarios/EditarEmpleado.html', {'form': form})

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def EliminarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    usuario.is_active = False
    usuario.save()

    return redirect('usuarios:ListaEmpleado')

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def ActivarEmpleado(request, pk):
    usuario = Empleados.objects.get(username=pk)
    usuario.is_active = True
    usuario.save()

    return redirect('usuarios:ListaEmpleado')
    
@login_required
def Perfil(request):
    usuario = request.user 

    return render(request, 'Usuarios/Perfil.html', {'usuario': usuario})

def OpcionesCliente(request):

    return render(request, 'Usuarios/opciones.html', {})


def CrearCliente(request):
    if request.method == 'POST':
        
        datos = request.POST
        direccion = datos['direccion']
        nombre = datos['nombre']
        apellido = datos['apellido']
        correo = datos['correo']
        telefono = datos['telefono']
        rol= datos['tipo']
        estrato= datos['estrato']
        cedula = datos['cedula']

        #reCAPTCHA
        clientkey = request.POST['g-recaptcha-response']
        secretkey = '6Lf_6_QUAAAAAB8T3OWQWpsUUIGAJEEXzRYVGA1e'
        captchaData = {
            'secret' : secretkey,
            'response' : clientkey
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)
        response = json.loads(r.text)
        verify = response['success']

        if verify:
            messages.success(request, 'Solicitud creada exitosamente, le notificaremos cuando se haya aprobado')
            a = Clientes(first_name=nombre, last_name=apellido, tipo=rol, email=correo, cedula=cedula, telefono=telefono, username=cedula)
            a.save()
            contrato = Contrato(cliente=a, direccion=direccion, estrato=estrato)
            contrato.save()
            return redirect('landing')
        else:
            messages.warning(request, 'Por favor verifique el CAPTCHA')
            return render(request, 'Usuarios/CrearCliente2.html', {})

    return render(request, 'Usuarios/CrearCliente2.html', {})

def ClienteAntiguo(request):
    if request.method == 'POST':
        
        datos = request.POST
        direccion = datos['direccion']
        cedula = datos['cedula']

        cliente = Clientes.objects.get(cedula=cedula)

        contrato = Contrato(cliente=cliente, direccion=direccion, en_servicio=False)
        contrato.save()

        messages.success(request, 'Solicitud creada exitosamente, le notificaremos cuando se haya aprobado')
        return redirect('usuarios:home')

def ListaSolicitudCliente(request):
    #clientes = Clientes.objects.filter(aprobado=False).select_related('contrato')
    clientes = Contrato.objects.filter(cliente__aprobado=False)
    return render(request, 'Usuarios/ListaAprobar.html', {'clientes': clientes})

def ListaSolicitudClienteA(request):
    
    clientes = Contrato.objects.filter(en_servicio=False)
    return render(request, 'Usuarios/ListaAprobarA.html', {'clientes': clientes})

def ListaCliente(request):
    #clientes = Clientes.objects.filter(aprobado=False).select_related('contrato')
    clientes = Contrato.objects.filter(cliente__aprobado=True)
    return render(request, 'Usuarios/ListaClientes.html', {'clientes': clientes})

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def AceptarCliente(request,pk):
    usuario = Clientes.objects.get(cedula=pk)
    contrato = Contrato.objects.get(cliente=usuario)
    usuario.aprobado = True
    usuario.save()
    contador = Contador(contrato=contrato, modelo="uno x ahi", fecha_vencimiento='2040-03-03')
    contador.save()

    messages.success(request, 'Cliente aprobado!')
    return redirect('usuarios:ListaSolicitudCliente')

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def AceptarClienteA(request,pk):
    contrato = Contrato.objects.get(id=pk)
    contrato.en_servicio=True
    contrato.save()

    contador = Contador(contrato=contrato, modelo="uno x ahi", fecha_vencimiento='2040-03-03')
    contador.save()

    messages.success(request, 'Cliente aprobado!')
    return redirect('usuarios:ListaSolicitudClienteA')

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def RechazarCliente(request, pk):
    usuario = Clientes.objects.get(cedula=pk)
    contrato = Contrato.objects.get(cliente=usuario)
    contrato.delete()
    usuario.delete()

    messages.success(request, 'Cliente rechazado!')
    return redirect('usuarios:ListaSolicitudCliente')

@permission_required('usuarios.view_usuario', login_url=None, raise_exception=True)
def RechazarClienteA(request, pk):
    contrato = Contrato.objects.get(id=pk)
    contrato.delete()

    messages.success(request, 'Cliente aprobado!')
    return redirect('usuarios:ListaSolicitudClienteA')
