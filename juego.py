#Voy a volver a hacer el código sobre la marcha
#con otro enfoque para que sea más facil introducir los nuevos cambios

#importamos la librería que necesitamos
import random

#creamos una función 
#para elegir el nivel en el futuro una vez vayamos a jugar
def elegirnivel():
    print("Seleccione un nivel de dificultad: ")
    print("1 = Simple")
    print("2 = Intermedio")
    print("3 = Avanzado")
    print("4 = Experto")
    nivelelegido = int(input("¿En qué nivel de dificultad desea jugar?: "))
    global eleccionnivel
    eleccionnivel = nivelelegido
    if eleccionnivel == 1 :
        print("Usted ha seleccionado el nivel de dificultad simple.")
    if eleccionnivel == 2 :
        print("Usted ha seleccionado el nivel de dificultad intermedio.")
    if eleccionnivel == 3 :
        print("Usted ha seleccionado el nivel de dificultad avanzado.")
    if eleccionnivel == 4 :
        print("Usted ha seleccionado el nivel de dificultad experto.")

elegirnivel()

#Ahora vamos a trabajar el nivel simple y en base a eso realizamos el resto de dificultades.
if eleccionnivel == 1 :
    nintentos = 0
    numero = random.randint(0,100)
    print("A continuación se le va a pedir que adivine un número generado del 0 al 100.")

    while nintentos < 20 :
        print("Intente adivinar el número: ")
        intento = int(input())
        nintentos += 1

        if intento < numero :
            print("Te has quedado por debajo del número generado.")
        if intento > numero :
            print("Te has quedado por encima del número generado.")
        if intento == numero :
            break
    
    if intento == numero :
        print("Has logrado acertar el número con " + str(nintentos) + " intentos.")
    if intento != numero :
        print("Lo sentimos, no has logrado acertar el número en los 20 intentos que tenías.")
