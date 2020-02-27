from django.urls import path
from .views import *

app_name='subestaciones'

urlpatterns=[
    path('registrar/', registrar_view, name='registrar'),
    path('consultar/', consultar_view, name='consultar'),
    path('eliminar/', eliminar_view, name='eliminar')
]