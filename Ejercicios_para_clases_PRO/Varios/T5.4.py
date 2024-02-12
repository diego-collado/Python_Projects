'''
Escribe una función en Python para leer líneas de un archivo de texto "notas.txt".
Su función debe encontrar y mostrar la aparición de la palabra "el".
'''

def el_palabras():
    with open("notas.txt",'r') as fichero:
        contador = 0
        for linea in fichero:
            palabras = linea.split()#separación de palabras por espacio en blanco
            for palabra in palabras:
                if palabra.lower() == "el":
                    contador += 1
        print(f"Total palabras 'el' en el archivo: {contador}")


#MAIN
el_palabras()