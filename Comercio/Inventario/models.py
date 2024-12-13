from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Productos(models.Model):
    name=models.CharField(max_length=30)
    descripcion=models.TextField()
    marca=models.CharField(max_length=20)
    canMaxima = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    canMin = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(998)])
    precio=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.canMin >= self.canMaxima:
            raise ValidationError("La cantidad Minima debe ser menor que la Maxima")
        

    


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


        
