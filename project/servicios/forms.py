from django import forms
from . import models

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = models.Servicios
        fields = "__all__"
        # widgets = {
        #     "nombre": forms.TextInput(attrs={"class": "form-control"}),
        # #    "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        # }
