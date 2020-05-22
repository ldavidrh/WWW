from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'facturas'
urlpatterns = [
    path('menu/', views.Menu, name = 'menu'),
    path('generar/', views.GenerarFacturas, name = 'generar'),
    path('consultarFactura/<int:idcontrato>', views.ConsultarFactura, name = 'consultarFactura'),
    path('pagar1/', views.PagoFactura1, name = 'pagar1'),
    path('pagar2/', views.PagoFactura2, name = 'pagar2')
]