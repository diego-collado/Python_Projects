'''
Lista =  es un dato que permite almacenar muchos datos de diferentes tipos dentro de sí misma:
    - es mutable, es decir, cambiamos el contenido cuando queremos
    - es dinámica, es decir, se introduce lo que se quiere en el momento preciso (agregar/quitar elementos)
    - permite cualquier tipo de dato en cada posición
    - podemos indexarlas y ordenarlas
    - podemos introducir una lista dentro de otra y de otra y de otra... ¡¡Cuidado con crear muchos subniveles!!
       Lista unidimensionales, bidimensionales, tridimensionales...

    LISTA_EJEMPLO --> [variable][variable][variable][variable]
    LISTA_EJEMPLO --> [variable posición 0][variable posición 1][variable posición 2][variable posición 3]
'''

#DECLARACIÓN/INICIALIZACIÓN DE VARIABLES ---------------------------------------------------
lista = []
lista2 = [1, 3, 5]
#lista = [1, 2, 3]
#lista = ['a', 1.34,"lo mío es mío y lo tuyo es mío también", 1, True]
#lista = ['a', 1.34,"lo mío es mío y lo tuyo es mío también", 1, True, lista2]

#print(lista[1]) #accedemos a la posición X, empezando desde 0
#print(lista[-1]) #accedemos a la posición X, empezando desde el final
#lista[2] = 'Pepito Colorao'

#MÉTODOS A UTILIZAR CON LAS LISTAS - OPERACIONES "NORMALES":
#borrado:
l = [1, 2, 3, 4, 5]
del l[2]#borraría el número 3, posición 2 en nuestra lista

#mostrar desde X hasta Y:
print(l[0:3])#mostramos desde el elemento posición 0 hasta el elemento posición 3

#inicializar de nuevo:
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0]
print(l)

#añadir elementos:
l = [1, 2, 3, 4, 5, 6]
l += [7, 8, 9, 10]
print(l)

#asignación de elementos:
l = [1, 2, 3]
z, x, y = l

print(x, y, z)

#iterar listas: "recorrer" la lista
lista = [5, 9, 10]

for l in lista:
    print(l)

#imprimir el índice además del contenido:
lista = [5, 9, 10]
for i, l in enumerate(lista):
    print(i, l)

for i in range(0, len(lista)):
    print("Posición: {} - Contenido: {}".format(i, lista[i]))

#MÉTODOS PARA LAS LISTAS: método es una función built-in, precocinada
l = [1, 2]

#añadir elemento al final
l.append(3)

#añadir contenido a la lista inicial
l.extend([5, 6, 7])

#añadir elemento a posición determinada
l = [1, 3]
l.insert(1,2)

#borrado de elemento
l.remove(3)
print(l)

#eliminación por defecto del último elemento
l = [1, 2, 3]
l.pop() #elimninación de un elemento en la posición X --> l.pop(x)

#invertir el orden
l.reverse()

#ordenación de menor a mayor
l.sort()
#ordenación de mayor a menor
l.sort(reverse=True)

#¿¿Dónde aparece el elemento X??
lista = ["Angular", "React", "TypeScript", "JavaScript"]
print(lista.index("TypeScript"))#Si no está en la lista, da un error de valor : ValueError: 'Typescript' is not in list
print(lista.index("TypeScript", 1))#búsqueda a comenzar por la posición X