from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50);
    codigo = models.IntegerField(primary_key=True);

