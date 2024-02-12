'''
Escribe una función display_words() en Python para ller las líneas de un archivo de texto "story.txt" y
mostrar aquellas palabras que tenga menos de 4 caracteres.
'''
#FUNCTIONS
def display_words():
    with open("story.txt",'r') as fichero:
        contador = 0
        for linea in fichero:
            palabras = linea.split()#separación de palabras por espacio en blanco
            for palabra in palabras:
                if len(palabra) < 4:
                    contador += 1
        print(f"Total palabras menores de 4 caracteres en el archivo: {contador}")

#MAIN
display_words()