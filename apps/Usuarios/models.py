from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


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
        max_length = 16,
        default = OPERADORES
    )


    foto_perfil = models.ImageField(upload_to='fotos_perfil')

class Clientes(models.Model):

    #USUARIO CHOICES
    CLIENTE_NATURAL = 'cliente_natural'
    CLIENTE_JURIDICO = 'cliente_juridico'

    ROLES_CHOICES={
        (CLIENTE_NATURAL, 'cliente_natural'),
        (CLIENTE_JURIDICO, 'cliente_juridico'),
    }

    roles = models.CharField(
        choices = ROLES_CHOICES,
        max_length = 16,
        default = CLIENTE_NATURAL
    )
        
    cedula = models.CharField(max_length = 16, null=False)
    nombre = models.TextField(null=False)
    apellido = models.TextField()
    direccion = models.TextField(null=False)
    correo = models.EmailField(null=False)
    telefono = models.IntegerField(null=False)











