from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Empleados(AbstractUser):

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.get_full_name()

    cedula = models.CharField(primary_key=True, max_length=16)

    #USUARIO CHOICES
    ADMINISTRADOR = 'administrador'
    GERENTE = 'gerente'
    OPERADORES = 'operadores'

    ROLES_CHOICES={
        (ADMINISTRADOR, 'administrador'),
        (GERENTE, 'gerente'),
        (OPERADORES, 'operadores'),
    }

    roles = models.CharField(
        choices = ROLES_CHOICES,
        max_length = 15,
        default = OPERADORES
    )


    foto_perfil = models.ImageField(upload_to='fotos_perfil')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.foto_perfil.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto_perfil.path)

class Clientes(models.Model):

    #USUARIO CHOICES
    CLIENTE_NATURAL = 'persona natural'
    CLIENTE_JURIDICO = 'persona juridica'

    ROLES_CHOICES={
        (CLIENTE_NATURAL, 'persona natural'),
        (CLIENTE_JURIDICO, 'persona juridica'),
    }

    roles = models.CharField(
        ('Tipo de persona'),
        choices = ROLES_CHOICES,
        max_length = 15,
        default = CLIENTE_NATURAL
    )
        
    cedula = models.CharField(max_length = 16, null=False)
    nombre = models.CharField(max_length = 16, null=False)
    apellido = models.CharField(max_length = 16)
    correo = models.EmailField(null=False)
    telefono = models.IntegerField(null=False)
    aprobado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)


class Contrato(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    direccion = models.CharField(max_length=20, null=False)
    fecha_inicio = models.DateField(auto_now=True)
    en_servicio = models.BooleanField(default=True)















