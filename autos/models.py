from django.db import models

# Create your models here.

class Auto(models.Model):
    titulo = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    propietario = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=14)
    problema = models.CharField(max_length=100)
    id = models.CharField(max_length=3, primary_key=True)
    fecha = models.DateTimeField()
 
    def __str__(self):
        return "Toyota " +  self.titulo + " " + self.modelo + " - " + self.propietario 

    
class Fiado(models.Model):
    persona = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    articulo = models.CharField(max_length=200)
    monto = models.CharField(max_length=10)