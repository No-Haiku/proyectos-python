import random

intentosRealizados=0

print ("Hola como te llamas?")

miNombre=input ()

numero= random.randint (1,20)

print ("Bueno "+miNombre+" estoy pensando en un numero entre el 1 y 20")

while intentosRealizados < 6:
    print ("intenta adivinar")

    estimacion= input()

    estimacion= int(estimacion)

    intentosRealizados= intentosRealizados +1
    if estimacion < numero:
        print ("Muy chico intenta un numero mas grande")
        
    if estimacion > numero:
        print ("Te pasaste intenta con un numero mas chico")

    if estimacion== numero:
        break
if estimacion== numero:
    intentosRealizados= str(intentosRealizados)

    print ("En hora buena "+miNombre+" lo conseguiste en tan solo "+intentosRealizados+" intentos realizados!!!")

if estimacion != numero:
    numero=str(numero)
    print("El numero que estaba pensando era "+numero+" mejor suerte la proxima")

