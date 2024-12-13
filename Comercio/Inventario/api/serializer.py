from rest_framework import serializers
from Inventario.models import Productos,Tienda,Persona,Cargo

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos 
        fields = ['name', 'descripcion', 'marca', 'canMaxima', 'canMin', 'precio']   

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tienda
        fields='__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cargo
        fields='__all__'