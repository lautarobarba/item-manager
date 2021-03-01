from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .proyecto import Proyecto
from .tipo_item import TipoItem
from .estado_item import EstadoItem

class Item(models.Model):
    proyecto = models.ForeignKey(Proyecto, verbose_name='proyecto', on_delete=models.PROTECT)
    nombre = models.CharField(verbose_name='nombre', max_length=255, unique=True)
    detalle = models.CharField(verbose_name='detalle', max_length=255)
    creacion = models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True, max_length=255)
    tipo = models.ForeignKey(TipoItem, verbose_name='tipo', on_delete=models.PROTECT)
    estado = models.ForeignKey(EstadoItem, verbose_name='estado', default=1, on_delete=models.PROTECT)
    responsable = models.ForeignKey(User, verbose_name='responsable',  related_name="responsables", on_delete=models.PROTECT)
    equipo = models.ManyToManyField(User, verbose_name='equipo')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk':self.pk})