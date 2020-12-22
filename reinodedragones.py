import random
import time

def mostrarIntroduccion():
    print("Bienvendo joven guerrero! cual su nombre?")
    miNombre=input ()
    print ("Muy bien "+miNombre+" enpecemos la aventura")
    print (...)
    print ("Estas en una tierra llena de dragones frente a ti")
    print ("Hay dos cuevas, en una de ellas el dragon es generoso y")
    print ("Amigable el cual compartira su tesoro con tigo")
    print ("El otro es codicioso y esta hambriento , de devorara sin pensarlo!!!")
    print ()
def elegirCueva():
    cuevaElegida=''
    while cuevaElegida != '1' and cuevaElegida !='2':
        print ("a que cueva quieres entrar 1 o 2?")
        cuevaElegida= input()
    return cuevaElegida
def explorarCueva(cuevaElegida):
    print ("Te aproximas a la cueva...")
    time.sleep(2)
    print("es oscura y espeluznante...")
    time.sleep(2)
    print("un gran dragon aparece subitamente frente a ti !!! abre sus fauces...")
    print()
    time.sleep(2)

    cuevaAmigable= random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
        print ("Te regala su tesoro!")
    else:
        print("Te engulle de un bocado")
jugarDeNuevo='si'
while jugarDeNuevo== 'si' or jugarDeNuevo=='s':
    mostrarIntroduccion()
    numeroDecueva=elegirCueva()
    explorarCueva(numeroDecueva)

    print("quieres jugar de nuevo si o no?")

    jugarDeNuevo=input()





    