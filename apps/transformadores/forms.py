from django import forms
from .models import Transformador

class FormularioRegistroTransformador(forms.ModelForm):
    class Meta:
        model=Transformador
        fields=('serial', 'latitud', 'longitud', 'marca', 'activo', 'subestacion')
