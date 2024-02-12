'''
Crea una matriz de enteros 5X2 de un rango entre 100 y 200 tal que la diferencia entre cada elemento sea 10
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
array = np.arange(100, 200, 10) # Creación de matriz
print(array)

array = array.reshape(5,2) # Reconstrucción de matriz en 2 dimensiones
print(array)