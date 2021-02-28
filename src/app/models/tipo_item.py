from django.db import models
from django.urls import reverse
from .cambio_estado import CambioEstado

class TipoItem(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=255, unique=True)
    detalle = models.CharField(verbose_name='detalle', max_length=255)
    workflow = models.ManyToManyField(CambioEstado, verbose_name='workflow')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tipoitem-detail', kwargs={'pk':self.pk})