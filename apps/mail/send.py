from django.core.mail import EmailMessage
from apps.Usuarios.models import Clientes
from django.conf import settings

email = EmailMessage(
    subject="Tu factura electronica",
    body="Prueba de email",
    from_email=settings.EMAIL_HOST_USER,
    to=["luisrestrepo1995@gmail.com"]
)

def sendnow():
    email.send(fail_silently=False)
