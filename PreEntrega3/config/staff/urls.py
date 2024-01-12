from django.urls import path
from django.contrib import admin
from .views import staff,formulario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",staff,name="StaffName"),
    path("formulario/",formulario,name="Formulario Name"),
    
    
     
]
