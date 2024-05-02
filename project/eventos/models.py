from django.db import models
from cliente.models import Cliente
from servicios.models import Servicios
# Create your models here.

class Eventos(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Cliente"
        )
    servicio = models.ForeignKey(
        Servicios, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Servicio a realizar"
        )
    fecha_evento = models.DateField(verbose_name= "Fecha evento", blank=False)

    def __str__(self):
        return f"Fecha evento: {self.fecha_evento} Servicio: {self.servicio} Cliente: {self.cliente}"
    
    class Meta:
        verbose_name_plural = "Eventos"