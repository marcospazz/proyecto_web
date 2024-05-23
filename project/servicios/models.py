from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500, null = True, blank = True)
    avatar = models.ImageField(upload_to="avatares", null = True, blank = True)
    
    def __str__(self) -> str:
        return f"Servicio: {self.nombre} Descripción: {self.descripcion}"
    
    class Meta:
        verbose_name_plural = "Servicios"