from rest_framework import viewsets
from Inventario.models import *
from Inventario.api.serializer import *


class ProductosViewSet(viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    serializer_class=ProductosSerializer


class TiendaViewset(viewsets.ModelViewSet):
    queryset=Tienda.objects.all()
    serializer_class=TiendaSerializer

class PersonaViewset(viewsets.ModelViewSet):
    queryset=Persona.objects.all()
    serializer_class=PersonaSerializer

class TotalIngeViewset(viewsets.ModelViewSet): 
    queryset=Persona.objects.filter(tienda=1)
    serializer_class=PersonaSerializer

class CargoViewset(viewsets.ModelViewSet):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer
   

    
        
       
            
    
        
