from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    mes = models.CharField(max_length=50)
    anio = models.IntegerField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.nombre}"
    

class Cuerpo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    jerarquia = models.CharField(max_length=50)
    email = models.EmailField()
    legajo = models.IntegerField()

    class Meta:
        verbose_name = "Cuerpo Activo"
        verbose_name_plural = "Cuerpo Activo"
        ordering = ["legajo"]


    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    jerarquia = models.CharField(max_length=50)
    cuartel = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["cuartel","nombre", "apellido"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    


class Cartelera(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    novedad = models.CharField(max_length=200, default="Escriba aquí su novedad")

    class Meta:
        verbose_name = "Cartelera"
        verbose_name_plural = "Cartelera"
    

    def __str__(self):
        return f"{self.titulo}"
    


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    

