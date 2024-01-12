
from django.contrib import admin
from django.urls import include, path
from staff.views import staff

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("staff.urls")),
    
    path("staff/",staff),
    
    
    
]
