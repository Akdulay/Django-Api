from django.db import models

# Create your models here.

class Productos(models.Model):
    name=models.CharField(max_length=30)
    descripcion=models.TextField()
    marca=models.CharField(max_length=20)
    canMaxima=models.IntegerField()
    canMin=models.IntegerField()
    precio=models.DecimalField(max_digits=5, decimal_places=2)


class Tienda(models.Model):
    name=models.CharField(max_length=20)
    descripcion=models.TextField()



class Persona(models.Model):
    name=models.CharField(max_length=20)
    ocupacion=models.CharField(max_length=100)
    descripcion_ocupa=models.TextField()
    tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)    


        
