from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    query = models.Cliente.objects.all()
    context = {"clientes" : query}
    return render(request, "cliente/index.html", context)


    
