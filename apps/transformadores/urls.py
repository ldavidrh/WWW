from django.urls import path
from .views import *

app_name = 'transformadores'

urlpatterns = [
    path('registrar/', registrar_view, name='registrar'),
    path('consultar/', consultar_view, name='consultar'),
    path('eliminar/<str:serial>', eliminar_view, name='eliminar'),
    path('actualizar/<str:serial>', actualizar_view, name='actualizar')
]
