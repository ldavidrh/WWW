from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'
urlpatterns = [
    path('crear_consumo/<int:pk>/', views.CrearConsumo.as_view(), name='crear_consumo'),
    path('consumos/', views.ListaConsumo.as_view(), name='consumos'),
    path('consumos/<int:pk>/', views.ListaConsumoCliente.as_view(), name='consumosCliente'),
]