from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from . import models, forms

def home(request):
    # query = models.Eventos.objects.all()
    # context = {"eventos" : query}
    # return render(request, "eventos/index.html", context)
    return render(request, "eventos/index.html")

# Listar eventos y filtar por busqueda de fecha 
class EventosList(ListView):
    model = models.Eventos

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Eventos.objects.filter(fecha_evento=consulta)
        else:
            object_list = models.Eventos.objects.all()
        return object_list

# Crear nuevo evento
class EventoCreate(CreateView):
    model = models.Eventos
    form_class = forms.EventosForm
    success_url = reverse_lazy("eventos:home")


# UPDATE
# def eventos_update(request, pk: int):
#     query = models.Eventos.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.EventosForm(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("eventos:eventos_list")
#     else:  # request.method == "GET"
#         form = forms.EventosForm(instance=query)
#     return render(request, "eventos/eventos_update.html", context={"form": form})

class EventoUpdate(UpdateView):
    model = models.Eventos
    form_class = forms.EventosForm
    template_name = "eventos/eventos_update.html"
    success_url = reverse_lazy("eventos:eventos_list")


class EventoDetail(DetailView):
    model = models.Eventos


# class EventoDelete(LoginRequiredMixin, DeleteView):
class EventoDelete(DeleteView):
    model = models.Eventos
    success_url = reverse_lazy("eventos:eventos_list")