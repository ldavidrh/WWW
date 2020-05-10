from django.core.mail import EmailMessage
from apps.Usuarios.models import Clientes

clientes = Clientes.objects.all()



def send_email():
    for cliente in clientes:
        print(email)