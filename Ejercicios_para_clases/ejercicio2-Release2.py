'''
***** VERSIÓN 2 DEL EJERCICIO - UTILIZACIÓN DE LISTAS Y MÉTODOS ESPECIALES *****
2.- Crear un programa en el que pida una oración por teclado, la cual puede tener letras tanto en mayúsculas
como minúsculas.
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica
que es una vocal.
'''

#DECLARACIÓN/INICIALIZACIÓN DE VARIABLES ---------------------------------------------------
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
#Python = lista -- Otros lenguajes = array/arreglo -- Realmente es un objeto: un solo elemento, muchos más elementos dentro

contarVocales = 0

#MAIN ---------------------------------------------------

frase = str(input("Introduce una frase: "))#str(...) --> parseamos para que lo que se introduzca sea sí o sí string
frase = frase.lower()

for letra in frase:#te paso un disco duro, el cual se ve desde la carpeta 0 hasta la carpeta final
    if (letra in vocales):#in --> nos permite comparar entre una lista y otra: si X está en la lista secundaria
        contarVocales += 1
print("Frase minúsculas: {}\nNúmero Vocales: {}".format(frase,contarVocales))