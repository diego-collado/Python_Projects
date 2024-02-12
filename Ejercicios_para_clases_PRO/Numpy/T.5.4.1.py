'''
Crea un array de enteros 4X2 e imprime sus atributos.
Nota: El elemento debe ser de tipo unsigned int16. Imprime los siguientes atributos:
    - La shape del array.
    - Las dimensiones del array.
    - El tamaño de cada elemento del array en bytes.
'''

import numpy as np # Import módulo Numpy

# Creación del array e impresión del resultado
array = np.empty([4,2], dtype=np.uint16)
print(array)

# Atributos
print ("Shape:", array.shape) # forma del array
print ("Dimensiones: ", array.ndim) # dimensiones del array
print("Tamaño en bytes: ", array.itemsize) # tamaño por item