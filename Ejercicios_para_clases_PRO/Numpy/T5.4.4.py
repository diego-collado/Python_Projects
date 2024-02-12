'''
Devuelve un array de filas impares y columnas pares dado el siguiente array:
    sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36],
    [39 ,42, 45, 48], [51 ,54, 57, 60]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print(sampleArray)

# Fórmulas separadas
print(sampleArray[::2]) # Impares --> ::,2
print(sampleArray[1::2]) # Pares --> 1::2

print(sampleArray[::2, 1::2]) # Fórmula par-impar conjunta