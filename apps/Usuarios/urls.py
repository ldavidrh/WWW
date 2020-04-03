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
    path('perfil/', views.Perfil, name='Perfil'),
    path('opciones/', views.OpcionesCliente, name='Opciones'),
    path('crear_cliente/', views.CrearCliente, name='CrearCliente'),
    path('cliente_antiguo/', views.ClienteAntiguo, name='ClienteAntiguo'),
    path('lista_cliente/', views.ListaSolicitudCliente, name='ListaSolicitudCliente'),
    path('lista_clienteA/', views.ListaSolicitudClienteA, name='ListaSolicitudClienteA'),
    path('aceptar_cliente/<int:pk>/', views.AceptarCliente, name='AceptarCliente'),
    path('aceptar_clienteA/<int:pk>/', views.AceptarClienteA, name='AceptarClienteA'),
    path('rechazar_cliente/<int:pk>/', views.RechazarCliente, name='RechazarCliente'),
    path('rechazar_clienteA/<int:pk>/', views.RechazarClienteA, name='RechazarClienteA'),
    path('lista_clintes/', views.ListaCliente, name='ListaCliente'),
    path('login/', auth_views.LoginView.as_view(template_name='Usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Usuarios/logout.html'), name='logout'),
]