'''
Escribe una función en Python para contar y mostrar el número total de palabras de un archivo de texto.
'''

def cuentapalabras():
    with open("story.txt",'r') as fichero:
        contador = 0
        for linea in fichero:
            palabras = linea.split()#separación de palabras por espacio en blanco
            for palabra in palabras:
                contador += 1
        print(f"Total palabras del archivo: {contador}")

cuentapalabras()