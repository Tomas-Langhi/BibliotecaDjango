from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50);
    codigo = models.IntegerField(primary_key=True);


class Libro(models.Model):
    titulo = models.CharField(max_length=50);
    editorial = models.CharField(max_length=50);
    paginas =  models.IntegerField();
    codigo = models.IntegerField(primary_key=True);
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE);
    
class Ejemplar(models.Model):
    localizacion = models.CharField(max_length=50);
    codigo = models.IntegerField(primary_key=True);
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE);

class Usuario(models.Model):
    nombre = models.CharField(max_length=50);
    direccion = models.CharField(max_length=100);
    telefono = models.CharField(max_length=20);
    codigo = models.IntegerField(primary_key=True);
    ejemplar = models.ManyToManyField('Ejemplar');

