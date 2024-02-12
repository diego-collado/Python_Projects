'''
Escribe una función en Python para leer el contenido de un archivo de texto "poema.txt" línea
por línea y mostrar el mismo en pantalla
'''

def lee_fichero():
    with open('poema.txt', 'r') as fichero:
        for linea in fichero:
            print(linea, end='')

lee_fichero()