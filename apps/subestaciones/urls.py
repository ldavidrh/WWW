from django.urls import path
from .views import *

app_name='subestaciones'

urlpatterns=[
    path('registrar/', registrar_view, name='registrar'),
    path('consultar/', consultar_view, name='consultar'),
    path('eliminar/<int:id>', eliminar_view, name='eliminar'),
    path('actualizar/<int:id>', actualizar_view, name='actualizar'),
    path('mapa/', map_view, name='mapa')
]