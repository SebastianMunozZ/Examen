from django.urls import path
from .views import lista_donacion, lista_producto, modificar_producto, agregar_tipo_mascota,agregar_form,modificar_donacion,lista_gato,registrarventa

urlpatterns = [
    path('lista-productos', lista_producto, name='lista_producto'),
    path('tipo-mascota', agregar_tipo_mascota, name='tipo_mascota'),
    path('modificar-producto/<int:id>',modificar_producto,name='modificar_producto'),
    path('add-form',agregar_form,name='agregar form'),
    path('lista-donacion',lista_donacion,name='lista_donacion'),
    path('modi-donacion/<int:id>/',modificar_donacion,name='modi_donacion'),  
    path('lista-gato',lista_gato,name='lista_gato'),
    path('reg-venta',registrarventa,name='reg_venta'),
]   

