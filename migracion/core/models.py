from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING
from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    id_tipomascota = models.AutoField(primary_key=True, verbose_name='Id de tipo mascota')
    tipoMascota = models.CharField(max_length=50, verbose_name='Nombre tipo mascota')
    
    
    def __str__(self):
        return self.tipoMascota

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True, verbose_name='Id producto')
    nombre_prod = models.CharField(max_length=200, verbose_name='Nombre producto')
    descripcion_prod = models.CharField(max_length=1000, verbose_name='Descripción de Producto')
    valor_prod = models.IntegerField(verbose_name='Valor producto')
    tipo_prod = models.CharField(max_length=50, verbose_name='Tipo Mascota')
    imagen_prod = models.CharField(max_length=2000, verbose_name='Descripción de Mascota')
    stock_prod = models.IntegerField(verbose_name='cantidad disponible')
    
    def __str__(self):
        return self.nombre_prod
   
   
   #no lista 
class Donacion(models.Model):
    id_don = models.AutoField(primary_key=True, verbose_name='Id organización')
    nombre_donacion = models.CharField(max_length=100, verbose_name='nombre organización')
    description_1_donacion = models.CharField(max_length=500, verbose_name='descripción simple')
    description_2_donacion = models.CharField(max_length=550, verbose_name='descripción detallada')
    img_dir_donacion = models.CharField(max_length=2000, verbose_name='imagen fundación')
    def __str__(self):
        return self.nombre_donacion


class Formulario(models.Model):
    id_form = models.AutoField(primary_key=True, verbose_name='correlativo form')
    nombre_form = models.CharField(max_length=50, verbose_name='nombre form')
    apellidos_form = models.CharField(max_length=50, verbose_name='apellidos form')
    fono_form = models.CharField(max_length=12, verbose_name='fono form')
    email_form = models.CharField(max_length=50, verbose_name='mail form')
    region_form = models.CharField(max_length=50, verbose_name='region form')
    comuna_form = models.CharField(max_length=50, verbose_name='comuna form')
    
    def __str__(self):
        return self.nombre_form

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, verbose_name='correlativo venta')
    user = models.CharField(max_length=50, verbose_name='user comprador')
    total = models.IntegerField(verbose_name='Valor Total venta')
    def __str__(self):
        return self.id_venta

class Detalle_venta(models.Model):
    id_detalle = models.AutoField(primary_key=True, verbose_name='correlativo form')
    id_venta = models.IntegerField(verbose_name='Venta asociada')
    producto = models.IntegerField(verbose_name='Valor producto')
    cantidad = models.IntegerField(verbose_name='Cantidad comprada')
    def __str__(self):
        return self.producto