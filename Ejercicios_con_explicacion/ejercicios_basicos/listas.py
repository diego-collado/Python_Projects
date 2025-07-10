'''
LISTAS: es un tipo de dato complejo o avanzado, ya que nos permite guardar
o almacenar muchos tipos diferentes de datos dentro de sí mismas.
Mal comparando con otros lenguajes de programación, es un arreglo, array, matriz.
Pero... ¿qué es realmente?
    - es mutable, podemos modelarlo como queramos (agregar/quitar elementos)
    - dinámico, lo mismo de antes
    - permite cualquier tipo de dato en cualquier posición
    - se puede indexar u ordenar
    - podemos insertar listas dentro de listas (multidimensionales)

Modelando una lista:

LISTA_EJEMPLO --> [variable][variable][variable][variable][variable]
                    pos. 0    pos. 1    pos.2      pos.3    pos.4

'''

# Comenzamos a jugar: DECLARACIÓN / INICIALIZACIÓN DE LISTAS ---------

lista = [] # declaración e inicialización - lista vacía
lista2 = [1,2,3,4] # declaración e inicialización
lista3 = [1,"eoeoooeoeooeoe", True, 'a', 4.6546757] # declaración e inicialización
lista4 = [1,'Guay', True, 3.456, lista2]

# Imprimiendo contenido
print(lista4) # imprimo lista completa
print(lista4[3]) # imprimo una posición de la lista
print(lista4[-1]) # imprimo la posición X desde el final
print("lista:",lista4[0:3]) # imprimo desde la posición 0 hasta la posición 3
print(lista4[::2]) # imprimo solo posiciones pares
print(lista4[3], lista4[-1]) # imprimo la posición 
print("lista final", lista4[0::3])
print("Otra lista final", lista4[0-3]) # hacia atrás, -3


# MÉTODOS (PRECOCINADOS) PARA OPERAR CON LISTAS ---------------------
# Borrado
lista5 = [1,2,3,4,5,6] # lista original
print (lista5)
del lista5[2] # la lista se modifica, borra la posición 2
print (lista5)

# Añadiendo elementos
listita = [1,2,3,4,5]
listita += [6,7,8,9,10] # con más igual, añadimos elementos al final de la lista
print(listita)

# Asignación de elementos
listax = [1,2,3]
z, x, y = listax
print(z,x,y)
print(z)
print(x)
print(y)

# Recorremos la lista: iteración
listay = [1,2,3,4,5,6]
for elemento in listay:
    print("elemento: ", elemento)

# imprimiendo, además, el índice
lista_indice = ['a','b','c','d']
for i, l in enumerate(lista_indice):
    print(i,l)

for i in range(0, len(lista_indice)): #len = longitud de la lista
    print(f"Posición: {i} -- Contenido: {lista_indice[i]}")

# MÉTODOS (BUILT-IN) DE PYTHON---------------------------------------
final = ['Diego','Marta','Izan','Adrián']

final.append('Coco') # añadimos un elemento final
print(final)

final.extend(['Volvo','Mini','Patinetes y bicis']) # añadimos contenido a la lista original
print(final)

final2 = ['Switch','Raspberry Pi']
final.insert(1,final2)# añadimos elementos en una posición determinada
print(final)

final.remove(final2) # borramos el elemento que queramos
print(final)

final.pop() # borrado del último elemento
final.pop(5) # borrado de la posición que quiero
print(final)

final.reverse() # invertimos el orden
print(final)

final.sort() # ordenadoción mayor a menor
print(final)

final.sort(reverse=True) # ordenación de menor a mayor
print(final)

print(final.index('Diego')) # imprime la posición en la que está el elemento
print(final.index('Volvo')) # ValueError: el elemento no lo encuentra