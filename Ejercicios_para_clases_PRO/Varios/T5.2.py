'''
Escribe una función para contar el número de líneas de un archivo de texto "historia.txt":
ejemplo --> si el archivo es "story.txt" contiene las siguientes líneas:
    Un niño jugando por allí
    Hay un parque infantil
    Un avión está en el cielo
    El cielo es rosa
    La contraseña puede contener números y letras
    El resultado debe ser 5
'''

def numero_lineasFichero():
    fichero = open('story.txt', 'r')
    print(len(fichero.readlines()))
    fichero.close()

numero_lineasFichero()