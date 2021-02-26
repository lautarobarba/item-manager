# Generated by Django 3.1.7 on 2021-02-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='nombre')),
                ('detalle', models.CharField(max_length=255, verbose_name='detalle')),
            ],
        ),
    ]