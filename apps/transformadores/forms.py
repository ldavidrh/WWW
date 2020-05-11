from django import forms
from .models import Transformador

class FormularioRegistroTransformador(forms.ModelForm):
    class Meta:
        model=Transformador
        exclude=('id',)
