# Generated by Django 3.1.7 on 2021-03-01 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210228_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cambioestado',
            options={'ordering': ['origen']},
        ),
    ]