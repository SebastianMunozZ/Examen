from dataclasses import fields
from rest_framework import serializers
from core.models import Producto, TipoMascota,Donacion,Formulario, Venta, Detalle_venta

class Productoserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ['id_prod', 'nombre_prod', 'descripcion_prod', 'valor_prod', 'tipo_prod', 'imagen_prod', 'stock_prod']
        
class Tipo_mascota_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoMascota
        fields = ['id_tipomascota','tipoMascota']

class Donacion_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donacion
        fields = ['id_don','nombre_donacion','description_1_donacion','description_2_donacion','img_dir_donacion']
        
class Formulario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['id_form','nombre_form','apellidos_form','fono_form','email_form','region_form','comuna_form']

class Formulario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id_venta','user','total']

class Formulario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_venta
        fields = ['id_detalle','id_venta','producto','cantidad']