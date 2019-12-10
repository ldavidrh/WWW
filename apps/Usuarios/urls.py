from django.urls import path
from . import views

app_name = 'usuarios'
urlpatterns = [
    path('', views.home, name='home'),
    path('crear_empleado/', views.CrearEmpleado, name='CrearEmpleado'),
    path('login/', views.login_view, name='login'),
]