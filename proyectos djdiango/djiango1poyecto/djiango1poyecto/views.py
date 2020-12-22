from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

#OBJETO
class persona(object):

    def __init__(self,nombre,apellido):

        self.nombre=nombre
        self.apellido=apellido 


def saludo(request):#primera vista

    #LLAMADO AL OBJETO
    p1=persona("Gianfranco","Neira")

    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"] 

    #nombre="Juan "
    #apellido="Diaz"
    hora_actual=datetime.datetime.now()
    #doc_externo=open("C:/Users/gianf/OneDrive/Escritorio/PYTHON/proyectos djdiango/misplantillas/plantillas1.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo=get_template('plantillas1.html')

    #DICCIONARIO
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"hora_actual":hora_actual,"temas":temas})

    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"hora_actual":hora_actual,"temas":temas})
    return render(request,"plantillas1.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"hora_actual":hora_actual,"temas":temas})

def cursoC(request):

    hora_actual=datetime.datetime.now()

    return render(request,"cursoC.html",{"hora_actual":hora_actual})

def cursoCss(request):

    hora_actual=datetime.datetime.now()

    return render(request,"cursoCss.html",{"hora_actual":hora_actual})

def despedida(request):

    return HttpResponse('adios mundo')

def dameFecha(request):

    fechaActual= datetime.datetime.now()

    documento="<html><body><h1> Fecha y hora actuales %s </html></body></h1>" % fechaActual

    return HttpResponse(documento)

def calcularEdad (request,edad,anio):

    #edadActual=18
    periodo=anio-2020
    edadFutura=edad+periodo
    documento="<html><body><h1> En el año %s tendras %s años </html></body></h1>"%(anio,edadFutura)
    return HttpResponse(documento)