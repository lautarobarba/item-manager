from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=255, unique=True)
    creacion = models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True, max_length=255)
    lider = models.ForeignKey(User, verbose_name='lider', related_name="lidera", on_delete=models.PROTECT)
    equipo = models.ManyToManyField(User, verbose_name='equipo', related_name="participa")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proyecto-detail', kwargs={'pk':self.pk})