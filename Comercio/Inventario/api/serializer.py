from rest_framework import serializers
from Inventario.models import Productos,Tienda,Persona

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productos 
        fields='__all__'

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tienda
        fields='__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'