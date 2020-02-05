from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'
urlpatterns = [
    path('', views.home, name='home'),
    path('crear_empleado/', views.CrearEmpleado, name='CrearEmpleado'),
    path('lista_empleado/', views.ListaEmpleado, name='ListaEmpleado'),
    path('editar_empleado/<int:pk>/', views.EditarEmpleado, name='EditarEmpleado'),
    path('eliminar_empleado/<int:pk>/', views.EliminarEmpleado, name='EliminarEmpleado'),
    path('activar_empleado/<int:pk>/', views.ActivarEmpleado, name='ActivarEmpleado'),
    path('login/', auth_views.LoginView.as_view(template_name='Usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Usuarios/logout.html'), name='logout'),
]