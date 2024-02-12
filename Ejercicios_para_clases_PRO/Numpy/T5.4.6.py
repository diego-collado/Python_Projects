'''
Divide la matriz en cuatro submatrices de igual tamaño.
Nota: Crea una matriz de enteros 8X3 de un rango entre 10 y 34 de tal manera que la diferencia entre cada elemento
sea 1 y luego divide la matriz en cuatro submatrices de igual tamaño.
'''

import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
array = np.arange(10, 34, 1) # Creación de matriz
print(array)

array = array.reshape(8,3) # Reconstrucción de matriz en 2 dimensiones
print(array)
subMatriz = np.split(array, 4) # Subdivisión de la matriz en 4 matrices iguales