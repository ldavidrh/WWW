
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class FormularioRegistroEmpleados(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        #self.fields["roles"].help_text = "Rol"
    
    class Meta(UserCreationForm.Meta):
        model = Empleados
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'cedula', 'roles', 'foto_perfil')

    
class FormularioEditarEmpleado(forms.ModelForm):

    class Meta:
        model = Empleados
        fields = ('foto_perfil', 'first_name', 'last_name', 'email', 'roles')
        widgets = {
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'bootstrap4-multi-input', 'required': False})
        }
        
          
