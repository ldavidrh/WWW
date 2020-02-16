from django import forms
from .models import Subestacion
class FormularioRegistroSubestacion(forms.ModelForm):
    class Meta:
        model=Subestacion
        fields=['nombre', 'latitud', 'longitud', 'activo']
