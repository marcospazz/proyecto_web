from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.

def home(request):
    query = models.Servicios.objects.all()
    context = {"servicios" : query}
    return render(request, "servicios/index.html", context)

def servicios_create(request):
    if request.method == "POST":
        form = forms.ServiciosForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("servicios:home")
    else:  # request.method == "GET"
        form = forms.ServiciosForm()
    return render(request, "servicios/servicios_create.html", context={"form": form})


