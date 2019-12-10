from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import FormularioRegistroClientes, FormularioRegistroEmpleados
from django.contrib.auth import login

def home(request):
    
    return render(request, 'base.html', {})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('usuarios:home')
    else:
        form = AuthenticationForm()
    return render(request, 'Usuarios/login.html', {'form': form})

def CrearEmpleado(request):
    if request.method == 'POST':
        form = FormularioRegistroEmpleados(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            cedula = form.cleaned_data.get('cedula')
            a.username = cedula
            a.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('usuarios:home')
    else:
        form = FormularioRegistroEmpleados()

    return render(request, 'Usuarios/CrearUsuario.html', {'form': form})
