from django.core.mail import EmailMessage
from apps.Usuarios.models import Clientes
from django.conf import settings

email = None


def setemail(recipients=[]):
    """Recibe un array de Strings con los correos de los destinatarios y crea una instancia de correo electronico"""
    if len(recipients) != 0:
        email = EmailMessage(
            subject="Tu factura electronica",
            body="",
            from_email=settings.EMAIL_HOST_USER,
            to=recipient
        )
    else:
        print("El array de destinatarios no puede ser vacio")


def attach(pathtofile=''):
    """Recibe la ruta relativa del archivo a ser adjuntado"""
    if email == None:
        print("Es necesario crear el Email con el metodo setmail() primero")
    else:
        if pathtofile == '':
            print("Especifique la ruta del archivo a adjuntar")
        else:
            email.attach_file(pathtofile)


def send_email():
    """Envia el correo electronico, tome en cuenta que el envio puede demorar hasta 10 segundos"""
    if email == None:
        print("Es necesario crear el Email con el metodo setmail() primero")
    else:
        email.send(fail_silently=False)
