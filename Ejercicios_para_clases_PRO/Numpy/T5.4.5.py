'''
Crea una matriz de resultados sumando las siguientes dos matrices de NumPy.
A continuación, modifica la matriz de resultados calculando el cuadrado de cada elemento.

    - arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
    - arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

print(arrayOne)
print(arrayTwo)

# Se crea un array conjunto y se imprime resultado
arrayResultado = arrayOne + arrayTwo
print(arrayResultado)

# Cálculo del cuadrado de cada elemento
for i in np.nditer(arrayResultado, op_flags=['readwrite']): #  np.nditer iterador multidimensional
    #op_flags=['readwrite'] permite leer y escribir el operando
    i[...] = i * i
print(arrayResultado)



