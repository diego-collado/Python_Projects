'''
Elimina la segunda columna de una matriz dada e inserta la siguiente columna nueva en su lugar.
    sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
    newColumn = numpy.array([[10,10,10]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

sampleArray = np.delete(sampleArray, 1, axis=1) # borrado de la 2ª columna del array sampleArray, axe 1

# Creación e impresión del nuevo array
newColumn = np.array([[10,10,10]])
print(newColumn)

# Construcción del nuevo array resultado, completo, con la nueva columna
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)
print(sampleArray)