from django.core.mail import EmailMessage
from apps.Usuarios.models import Clientes
from django.conf import settings

email = EmailMessage(
    "Factura de servicio",
    "Hola 'nombre_de_usuario', esta es tu factura del mes de 'fecha_factura'",
    'electrisoftwww@gmail.com',
    ["luisrestrepo1995@gmail.com"]
)

email.connection(settings.EMAIL_BACKEND)
def send_email():
    email.send(fail_silently=False)
