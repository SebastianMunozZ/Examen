from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(TipoMascota)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle_venta)