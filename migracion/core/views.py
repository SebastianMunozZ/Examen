from django.shortcuts import render
import requests,json
from .models import Donacion ,Producto

# Create your views here.

def home (request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html' )

def tienda(request):
    productos = requests.get('http://127.0.0.1:8000/api/lista-productos')
    datos = productos.json()
    data = {
        'productos':datos
   
    }

    return render(request,'tienda.html',data) 

def pring_front(request):
    if request.GET.get('mostrarTodo'):
        print('holaaaa')





def nosotros(request):
    return render(request, 'nosotros.html' )

def donaciones(request):
    # mascotas = Mascota.objects.all
    donaciones = requests.get('http://127.0.0.1:8000/api/lista-donacion')
    
    datos = donaciones.json()
    data = {
        'donaciones': datos
    } 
    return render(request, 'donaciones.html', data )

