from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50, default="");
    apellido = models.CharField(max_length=50, default="");
    edad =  models.IntegerField();
    def __str__(self):
        return str(self.nombre + " " + self.apellido)

    def get_age(self):
        edad = self.edad
        return edad
        
    #Para diferenciar entre adultos y menores
    def mayor(self):
        if self.edad > 18:
            return True
        else:
            False
    mayor.boolean = True
    mayor.short_description = 'Es adulto'
    

class Libro(models.Model):
    titulo = models.CharField(max_length=50, default="");
    editorial = models.CharField(max_length=50, default="");
    paginas =  models.IntegerField();
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE);
    def __str__(self):
        return str(self.titulo)
    
class Ejemplar(models.Model):
    localizacion = models.CharField(max_length=50, default="");
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE);
    #Esto es para que funcione el filter_horizontal
    #libro = models.ManyToManyField('Libro',);
    def __str__(self):
        return str(self.libro)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, default="");
    apellido = models.CharField(max_length=50, default="");
    edad =  models.IntegerField();
    direccion = models.CharField(max_length=100, default="");
    telefono = models.CharField(max_length=20, default="");
    ejemplar = models.ManyToManyField('Ejemplar');
    
    def __str__(self):
        return str(self.nombre + " " + self.apellido)
    
    def get_age(self):
        edad = self.edad
        return edad
    
    #Para diferenciar entre adultos y menores
    def mayor(self):
        if self.edad > 18:
            return True
        else:
            False
    mayor.boolean = True
    mayor.short_description = 'Es adulto'




