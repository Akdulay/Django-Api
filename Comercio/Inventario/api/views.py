from rest_framework import viewsets
from Inventario.models import Productos,Tienda,Persona
from Inventario.api.serializer import ProductosSerializer,TiendaSerializer,PersonaSerializer
from rest_framework.permissions import IsAuthenticated

class ProductosViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
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
   

    
        
       
            
    
        
