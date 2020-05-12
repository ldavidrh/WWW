from django import forms
from .models import Transformador

class FormularioRegistroTransformador(forms.ModelForm):
    class Meta:
        model=Transformador
        fields = '__all__'

class FormularioActualizacionTransformador(forms.ModelForm):
    class Meta:
        model=Transformador
        exclude = ('serial', 'devanado')