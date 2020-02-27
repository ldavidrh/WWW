import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _

def validar_string(value):
    d = value.split(" ")
    bandera = True
    for palabra in d:
        if palabra.isalpha():
            pass
        else:
            bandera = False
    if bandera:
        pass
    else:
        raise ValidationError(
            _('%(value)s no es válido'),
            params={'value': value},
        )

def validar_entero(value):
    
    if len(str(abs(value))) > 16:
        raise ValidationError(
            _('%(value)s es muy largo'),
            params={'value': value},
        )


class Persona(AbstractUser):
    id = models.UUIDField(primary_key=True, max_length=10, editable=False, default=uuid.uuid4)
    cedula = models.BigIntegerField(validators=[validar_entero], verbose_name='Cédula')
    email = models.EmailField(('Correo'), unique=True)
    first_name = models.CharField(validators=[validar_string], blank=True, max_length=30, verbose_name='Nombre')
    last_name = models.CharField(validators=[validar_string], blank=True, max_length=150, verbose_name='Apellido')

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name()

    
roles=(('operador','Operador'),('administrador','Administrador'),('gerente','Gerente'))

class Empleados(Persona):

    roles = models.CharField(('Rol'), choices = roles, max_length = 20)
    foto_perfil = models.ImageField(default="default.png", upload_to='fotos_perfil')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.foto_perfil.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto_perfil.path)

tipo_persona=(('persona_natural','Persona natural'),('persona_juridica','Persona juridica'))

class Clientes(Persona):

    tipo = models.CharField(('Tipo de persona'), choices = tipo_persona, max_length = 16)
    telefono = models.BigIntegerField(validators=[validar_entero], null=False)
    aprobado = models.BooleanField(default=False)

    
 

class Contrato(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=20, null=False, unique=True)
    fecha_inicio = models.DateField(auto_now=True)
    en_servicio = models.BooleanField(default=True)















