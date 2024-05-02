from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    query = models.Eventos.objects.all()
    context = {"eventos" : query}
    return render(request, "eventos/index.html", context)