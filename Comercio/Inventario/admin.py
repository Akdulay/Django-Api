from django.contrib import admin

# Register your models here.
from Inventario.models import Tienda,Persona,Productos

admin.site.register(Tienda)
admin.site.register(Productos)
admin.site.register(Persona)