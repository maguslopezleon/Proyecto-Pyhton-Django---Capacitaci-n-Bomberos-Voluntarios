# Generated by Django 5.0.2 on 2024-03-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_cartelera_novedad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartelera',
            name='novedad',
            field=models.CharField(default='Escriba aquí su novedad', max_length=200),
        ),
    ]
