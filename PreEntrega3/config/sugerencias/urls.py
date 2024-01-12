from django.urls import path
from .views import formulario_sugerencia

app_name = 'sugerencias'

urlpatterns = [
    path('formulario/', formulario_sugerencia, name="formulario_sugerencia"),
    # Otras rutas para sugerencias
]
