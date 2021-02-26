from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=255, unique=True)
    creacion = models.DateTimeField(verbose_name='fecha de creacion', auto_now_add=True, max_length=255)
    equipo = models.ManyToManyField(
        User,
        verbose_name='equipo',
        through='Asignacion',
        through_fields=('proyecto', 'trabajador'),
        blank=True
    )

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('proyecto-detail', kwargs={'pk':self.pk})


class Asignacion(models.Model):
    class Role(models.TextChoices):
        LIDER = 'lider'
        DESARROLLADOR = 'desarrollador'

    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    trabajador = models.ForeignKey(User, on_delete=models.PROTECT)
    rol = models.TextField(verbose_name='rol', choices=Role.choices, default=Role.DESARROLLADOR)