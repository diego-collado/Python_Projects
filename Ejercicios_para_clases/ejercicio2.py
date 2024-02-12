'''
2.- Crear un programa en el que pida una oración por teclado, la cual puede tener letras tanto en mayúsculas
como minúsculas.
Contar la cantidad de vocales.
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica
que es una vocal.

EXPLICACIÓN:
Para saber qué tipo de variable está trabajando el código, se utiliza type(variable)

frase.lower() --> convierte la frase a minúsculas
frase.upper() --> convierte la frase a mayúsculas

'''

#DECLARACIÓN/INICIALIZACIÓN DE VARIABLES ---------------------------------------------------
frase = ""
contarVocales = 0

#MAIN ---------------------------------------------------
frase = str(input("Introduce una frase: "))#str(...) --> parseamos para que lo que se introduzca sea sí o sí string
fraseMinus = frase.lower()

for i in range(len(frase)):
    if (fraseMinus[i] == 'a') or (fraseMinus[i] == 'e') or (fraseMinus[i] == 'i') or (fraseMinus[i] == 'o') or (fraseMinus[i] == 'u'):
        contarVocales += 1

print("Frase original: {}\nFrase minúsculas: {}\nNúmero Vocales: {}".format(frase,fraseMinus,contarVocales))