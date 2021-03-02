from django.db import models
from django.urls import reverse
from .item import Item
from .estado_item import EstadoItem
from django.contrib.auth.models import User

class Snapshot(models.Model):
    item = models.ForeignKey(Item, verbose_name='item', related_name="snapshot", on_delete=models.PROTECT)
    creacion = models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True, max_length=255)
    estado = models.ForeignKey(EstadoItem, verbose_name='estado', default=1, on_delete=models.PROTECT)
    responsable = models.ForeignKey(User, verbose_name='responsable', on_delete=models.PROTECT)

    class Meta:
        ordering = ['creacion']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk':self.pk})