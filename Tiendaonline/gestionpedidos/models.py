from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)#verbose_name= cambia el nombre en el server
    email=models.EmailField(blank=True,null=True)#blank=True,null=True opcional
    tlfno=models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class articulos(models.Model):
    nombre=models.CharField(max_length=50)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s el precio es %s'%(self.nombre,self.seccion,self.precio)

class pedidos(models.Model):
    numeros=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    
