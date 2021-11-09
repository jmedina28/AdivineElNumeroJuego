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
        print("Usted ha seleccionado el nivel de dificultad simple")

elegirnivel()
