from django.urls import path
from .views import *
app_name='subestaciones'

urlpatterns=[
    path('registrar/', registrar_view, name='registrar'),
]