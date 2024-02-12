'''
A continuación se muestra el array numPy proporcionado.
Devuelve un array de elementos tomando la tercera columna de todas las filas.
    sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
'''
import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print(sampleArray)

# Devolución de elementos tomando 3ª columna de todas las filas
newArray = sampleArray[...,2]
print(newArray)