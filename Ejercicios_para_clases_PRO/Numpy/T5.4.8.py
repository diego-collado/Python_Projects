'''
Imprime el máximo del eje 0 y el mínimo del eje 1 de la siguiente matriz bidimensional:
    sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

# Cálculo del máximo del eje 0 e impresión
maxAxe = np.max(sampleArray, 0)
print(maxAxe)

# Cálculo del mínimo del eje 1 e impresión
minAxe = np.min(sampleArray, 1)
print(minAxe)