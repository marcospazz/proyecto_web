from django import forms
from . import models

class EventosForm(forms.ModelForm):
    class Meta:
        model = models.Eventos
        fields = "__all__"       