'''
Ordena el siguiente array de NumPy:
    - Caso 1: Ordenar el array por la segunda fila
    - Caso 2: Ordenar el array por la segunda columna

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

arrayFila = sampleArray[:,sampleArray[1,:].argsort()] # ordenación array por 2ª fila (1 en el array)
print(arrayFila)

arrayColumna = sampleArray[:,sampleArray[:,1].argsort()] # ordenación array por 2ª columna (1 en el array)
print(arrayColumna)
