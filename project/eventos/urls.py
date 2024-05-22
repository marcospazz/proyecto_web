from django.urls import path
from . import views

app_name = "eventos"

urlpatterns = [
    path('', views.home, name='home'),
    path("eventos/list/", views.EventosList.as_view(), name="eventos_list"),
    path("eventos/form/", views.EventoCreate.as_view(), name="eventos_form"),
    path("eventos/delete/<int:pk>", views.EventoDelete.as_view(), name="eventos_delete"),
    path("eventos/update/<int:pk>", views.EventoUpdate.as_view(), name="eventos_update"),
    # path("eventos/update/<int:pk>", views.eventos_update, name="eventos_update"),
    path("eventos/detail/<int:pk>", views.EventoDetail.as_view(), name="eventos_detail"),
]
