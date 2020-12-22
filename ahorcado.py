import random

IMAGENES_AHORCADO=['''

  +---+
  |   |
      |
      |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
      |
      |
      |
 =========''','''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|   |
     |
     |
 =========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
 =========''','''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
 =========''','''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
 =========''']


palabras = '''hormiga babuino tejon murcielago oso castor camello gato
almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro
rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra
nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte
salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre
sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'''.split()

def obtenerPalabrasAlAzar(listaDePalabras):
    #esa funcion devuelve una cadena al azar de la lista de palabras pasada
    indiceDePalabras=random.randint(0,len(listaDePalabras)-1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO,letrasIncorrectas,letrasCorrectas,palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print("Letras Incorrectas:", end='')
    for letra in letrasIncorrectas:
        print(letra,end='')
    print()

    espaciosVacios='_'*len(palabraSecreta)

    for i in range(len(palabraSecreta)):#completar los espacios vacos con letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios=espaciosVacios[:i]+palabraSecreta[i]+espaciosVacios[i+1:]
    for letra in espaciosVacios:#mostrar la palabra secreta conespacios enre cada letra
        print(letra,end='')
        print()
def obtenerIntento(letrasProbadas):
    #devuelve la letra ingresada por el jugador,verifica que el jugador a ingresado solo una lera y no otra cosa
    while True:
        print("Adivina una letra.")
        intento=input()
        intento=intento.lower()
        if len(intento) !=1:
            print("por favor inroduce una letra.")
        elif intento in letrasProbadas:
            print("ya has elegido esta letra , elige otra.")
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print("por favor ingrese una LETRA")
        else:
            return intento