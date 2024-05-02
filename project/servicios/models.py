from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Servicios"