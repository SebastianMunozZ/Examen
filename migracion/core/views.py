from email import message
from django.shortcuts import redirect, render
import requests,json
from .models import Donacion ,Producto
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

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

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redirigir al Home
            return redirect(to='home')
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)