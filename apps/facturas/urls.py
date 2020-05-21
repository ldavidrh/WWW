from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'facturas'
urlpatterns = [
    path('menu/', views.Menu, name = 'menu'),
    path('generar/', views.GenerarFacturas, name = 'generar'),
    path('consultarFactura/', views.ConsultarFactura, name = 'consultarFactura')
]