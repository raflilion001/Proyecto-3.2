from django.urls import path
from .views import formulario_cliente

app_name = 'clientes'

urlpatterns = [
    path('formulario/', formulario_cliente, name="formulario_cliente"),
    # Otras rutas para clientes
]
