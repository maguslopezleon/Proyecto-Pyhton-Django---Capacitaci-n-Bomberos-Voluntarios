# Generated by Django 5.0.2 on 2024-03-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartelera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('fechaPublicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CuerpoActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('jerarquia', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('legajo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('mes', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
            ],
            options={
                'ordering': ['anio'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=50)),
                ('cuartel', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['cuartel', 'nombre', 'apellido'],
            },
        ),
    ]
