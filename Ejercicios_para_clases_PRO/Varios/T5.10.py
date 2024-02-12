'''
Escribe un programa en Python para comprobar si un archivo especificado existe.
'''

def comprobandoArchivos(archivo):
    try:
        with open(archivo,'r'):
            print("El archivo ha sido encontrado...")

    except FileNotFoundError:
        print("¡¡Error, archivo proporcionado no encontrado!!")

#MAIN
nombre = input("Introduce el nombre del archivo a comprobar:")
nombre = nombre+".txt"
comprobandoArchivos(nombre)