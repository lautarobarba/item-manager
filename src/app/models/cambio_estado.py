from django.db import models
from django.urls import reverse
from .estado_item import EstadoItem


class CambioEstado(models.Model):
    origen = models.ForeignKey(EstadoItem, verbose_name='origen', related_name="origenes", on_delete=models.PROTECT)
    destino = models.ForeignKey(EstadoItem, verbose_name='destino', related_name="destinos", on_delete=models.PROTECT)

    class Meta:
        unique_together = [['origen', 'destino']]

    def __str__(self):
        return f'{self.origen}->{self.destino}'

    def get_absolute_url(self):
        #return reverse('estadoitem-detail', kwargs={'pk':self.id})
        return reverse('home')