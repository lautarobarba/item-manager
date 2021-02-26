from django.db import models
from django.urls import reverse

class EstadoItem(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=255, unique=True)
    detalle = models.CharField(verbose_name='detalle', max_length=255)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        #return reverse('estadoitem-detail', kwargs={'pk':self.id})
        return reverse('home')