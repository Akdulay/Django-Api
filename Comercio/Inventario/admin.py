from django.contrib import admin

# Register your models here.
from Inventario.models import Tienda,Persona,Productos,Cargo

admin.site.register(Tienda)
admin.site.register(Productos)
admin.site.register(Persona)
admin.site.register(Cargo)