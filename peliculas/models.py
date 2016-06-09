from django.db import models
from django.utils import timezone

class Paises(models.Model):
    nombre = models.CharField(max_length=100)
    bandera = models.ImageField(upload_to='static/img/banderas')

    def __str__(self):
        return self.nombre

class Directores(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Paises)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='static/img/directores')

    def __str__(self):
        return self.nombre

class Actores(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Paises)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='static/img/actores')

    def __str__(self):
        return self.nombre

class Generos(models.Model):
    genero = models.CharField(max_length=50)

    def __str__(self):
            return self.genero

class Productoras(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='static/img/productoras')

    def __str__(self):
            return self.nombre


class Peliculas(models.Model):
    caratula = models.ImageField(upload_to='static/img/caratulas')
    titulo = models.CharField(max_length=100)
    director = models.ForeignKey(Directores)
    anio = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.ManyToManyField(Generos)
    actores = models.ManyToManyField(Actores)
    pais = models.ForeignKey(Paises)
    productora = models.ForeignKey(Productoras)
    fecha_entrada = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.titulo
# Create your models here.
