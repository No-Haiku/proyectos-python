from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def busqueda_productos(request):

    return render(request,"busqueda_productos.html" )

def buscar(request):

    mensaje="Articulo buscado %r"%request.GET["product"]

    return HttpResponse(mensaje)