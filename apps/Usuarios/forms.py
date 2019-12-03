
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class FormularioRegistroEmpleados(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = Empleados
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'cedula', 'roles', 'foto_perfil')

class FormularioRegistroClientes(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = Clientes
        fields = ('nombre', 'apellido', 'cedula','direccion', 'correo', 'telefono','roles')