# Generated by Django 5.0.2 on 2024-03-15 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_remove_cartelera_fechapublicacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CuerpoActivo',
            new_name='Cuerpo',
        ),
    ]
