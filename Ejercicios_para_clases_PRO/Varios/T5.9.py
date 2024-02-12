'''
Escribe un programa en Python para calcular la frecuencia de todas las palabras de un archivo txt.
'''
#IMPORTS
from collections import Counter
#más info: https://docs.python.org/es/3/library/collections.html#collections.Counter

#FUNCTIONS
def frecuenciaPalabras(archivo):
    with open(archivo, 'r') as archivoAnalizado:
        contenidoArchivo = archivoAnalizado.read()#lectura de archivo
        contenidoArchivo = contenidoArchivo.lower()#texto pasado a minúscula
        contenidoArchivo = contenidoArchivo.strip()#elimina los espacios en blanco (innecesarios)

        palabras = contenidoArchivo.split()#contamos la frecuencia de las palabras nuestro archivo
        frecuencia = Counter(palabras)

        #Mostramos los resultados
        for palabra, frec in frecuencia.items():
            print(palabra, frec)

#MAIN
frecuenciaPalabras("story.txt")