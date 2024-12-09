from django.db import models

# Create your models here.

class Productos(models.Model):
    name=models.CharField(max_length=30)
    descripcion=models.TextField()
    marca=models.CharField(max_length=20)
    canMaxima=models.IntegerField()
    canMin=models.IntegerField()
    precio=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Tienda(models.Model):
    name=models.CharField(max_length=20)
    descripcion=models.TextField()


    def __str__(self):
        return self.name 
    

class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    name=models.CharField(max_length=20)
    ocupacion=models.CharField(max_length=100)
    descripcion_ocupa=models.TextField()
    tienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)
    cargo=models.OneToOneField(Cargo,on_delete=models.SET_NULL,blank=True, null=True)
    
    def __str__(self):
        return self.name    


        
