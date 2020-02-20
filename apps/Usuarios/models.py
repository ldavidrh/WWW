from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class Persona(AbstractUser):

    cedula = models.IntegerField(primary_key=True)
    email = models.EmailField(('Correo'), unique=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name()

    
roles=(('operador','Operador'),('administrador','Administrador'),('gerente','Gerente'))

class Empleados(Persona):

    roles = models.CharField(choices = roles, max_length = 20)

    foto_perfil = models.ImageField(upload_to='fotos_perfil')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.foto_perfil.path)

        if img.height > 160 or img.width > 160:
            output_size = (160, 160)
            img.thumbnail(output_size)
            img.save(self.foto_perfil.path)

tipo_persona=(('persona_natural','Persona natural'),('persona_juridica','Persona juridica'))

class Clientes(Persona):

    tipo = models.CharField(('Tipo de persona'), choices = tipo_persona, max_length = 16)
    telefono = models.IntegerField(null=False)
    aprobado = models.BooleanField(default=False)

    
 

class Contrato(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=20, null=False)
    fecha_inicio = models.DateField(auto_now=True)
    en_servicio = models.BooleanField(default=True)















