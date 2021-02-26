# Generated by Django 3.1.7 on 2021-02-26 10:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_auto_20210226_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='equipo',
            field=models.ManyToManyField(through='app.Asignacion', to=settings.AUTH_USER_MODEL, verbose_name='equipo'),
        ),
    ]
