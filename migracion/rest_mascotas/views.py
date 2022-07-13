from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto, TipoMascota, Donacion
from .serializers import Formulario_serializer, Productoserializer, Tipo_mascota_serializer, Donacion_serializer,Venta_serializer,Detalle_venta,Venta_detalle_serializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_producto(request):
    """
    GET = Lista todos los productos
    POST = Agrega Registro
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = Productoserializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Productoserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def lista_gato(request):
    """
    GET = Lista todos los productos
    """
    if request.method == 'GET':
        producto = Producto.objects.filter(tipo_prod = "Gato")
        serializer = Productoserializer(producto, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST'])
def modificar_producto(request, id):
    """
    GET = Elimina un producto
    POST = Agrega Registro
    """
    if request.method == 'GET':
        producto = Producto.objects.get(id_prod = id)
        producto.delete()
        return Response('Eliminado', status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        producto = Producto.objects.get(id_prod = id)
        data = JSONParser().parse(request)
        serializer = Productoserializer(producto,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'POST'])
def agregar_tipo_mascota(request):
    """
    GET = Lista todas las mascotas
    POST = Agrega Registro
    """
    if request.method == 'GET':
        mascota = TipoMascota.objects.all()
        serializer = Tipo_mascota_serializer(mascota, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Tipo_mascota_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def agregar_form(request):
    data = JSONParser().parse(request)
    serializer = Formulario_serializer(data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_donacion(request):
    if request.method == 'GET':
        donacion = Donacion.objects.all()
        serializer = Donacion_serializer(donacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Donacion_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def modificar_donacion(request,id):
    if request.method == 'GET':
        dona = Donacion.objects.get(id_don = id)
        dona.delete()
        return Response('Eliminado', status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        dona = Donacion.objects.get(id_don = id)
        serializer = Donacion_serializer(dona,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def registrarventa(request):
    data = JSONParser().parse(request)
    print(data)
    venta = data.venta
    serializerVenta = Venta_detalle_serializer(venta)
    serializer = Venta_serializer(data.productos, many=True)
    if serializer.is_valid():
        serializer.save()
        print(serializer.id)
        detalleventa_ser = Detalle_venta()
        if serializerVenta.is_valid():
            serializerVenta.save()
            stock = Producto.objects.get(id_prod)
        