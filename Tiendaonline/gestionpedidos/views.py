from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):

    return render(request,"busqueda_productos.html" )

def buscar(request):
    if request.GET["product"]:

        #mensaje="Articulo buscado %r"%request.GET["product"]
        producto=request.GET["product"]

        if len (producto)>20:
            mensaje="Texto de busqueda demaciado largo"
        else:
            artic=articulos.objects.filter(nombre__icontains=producto)

            return render(request,"resultados_busqueda.html",{"articulos":artic,"query":producto})
    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":

        subject=request.POST["asunto"]#almacena el asunto
        
        message=request.POST["mensaje"] +" "+ request.POST["email"]#almacena el mensaje y email
        
        email_from=settings.EMAIL_HOST_USER #de donde viene el email que se envia

        recipient_list=["gian.f-neira@live.com"]#donde quiero que lleguen los msjs

        send_mail(subject, message, email_from, recipient_list)#recordar separar las listas con espacio

        return render(request,"gracias.html")

    return render(request,"contacto.html")