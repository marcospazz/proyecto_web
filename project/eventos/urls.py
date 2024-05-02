from django.urls import path
from . import views

app_name = "eventos"

urlpatterns = [
    path('', views.home, name='home'),
    
]
