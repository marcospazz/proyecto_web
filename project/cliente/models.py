from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length= 200, unique=True, verbose_name="Nombre y Apellido")
    correo = models.EmailField(max_length= 200, verbose_name= "Email")
    contacto_telefonico = models.PositiveIntegerField(verbose_name="Teléfono movil")

    def __str__(self) -> str:
        return self.nombre

    