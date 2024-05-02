from django.urls import path 
from . import views
app_name = "servicios"

urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/create', views.servicios_create, name='servicios_create'),    
]
