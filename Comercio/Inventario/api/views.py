from rest_framework import viewsets
from Inventario.models import Productos,Tienda,Persona
from Inventario.api.serializer import ProductosSerializer,TiendaSerializer,PersonaSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializer_class=ProductosSerializer


class TiendaViewset(viewsets.ModelViewSet):
    queryset=Tienda.objects.all()
    serializer_class=TiendaSerializer

class PersonaViewset(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=PersonaSerializer