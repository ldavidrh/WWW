from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'reportes'
urlpatterns = [
    path('reporte1/', views.reporte1, name='reporte1')
]