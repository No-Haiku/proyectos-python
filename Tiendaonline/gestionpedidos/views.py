from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos

# Create your views here.

def busqueda_productos(request):

    return render(request,"busqueda_productos.html" )

def buscar(request):
    if request.GET["product"]:

        #mensaje="Articulo buscado %r"%request.GET["product"]
        producto=request.GET["product"]
        artic=articulos.objects.filter(nombre__icontains=producto)

        return render(request,"resultados_busqueda.html",{"articulos":artic,"query":producto})
    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)