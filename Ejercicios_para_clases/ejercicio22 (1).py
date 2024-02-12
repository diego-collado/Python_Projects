kjhjuhiuhiuhiñ'''
Crear un menú en el que realicemos las tareas más típicas con las listas:
    - crear --> lista = []
    - añadir elemento/s --> lista.append(valor) // lista.extend(valor)
    - borrar elemento/s --> lista.remove(valor) // lista.pop para el último valor de la lista //
    del lista(posición)
    - borrar lista --> (todos los elementos) lista.clear()
    - ordenar elementos de mayor a menor y menor a mayor --> lista.sort(reverse=True) // lista.sort()
'''

#FUNCTIONS
lista = []
def crear(lista):
    elemento = input("Introduce al menos 1 elemento para la lista: ")
    lista.append(elemento)
def annadir(lista):
    elemento = input("Introduce nuevo elemento:")
    lista.append(elemento)

def annadir_posicion(lista):
    pos = int(input("Determina la posición del nuevo elemento: "))
    elemento = input("Introduce el nuevo elemento: ")
    lista.insert(pos, elemento)

def borrar_posicion(lista):
    pos = int(input("Determina la posición del nuevo elemento: "))
    lista.pop(index=pos)
def borrar_lista(lista):
    lista.clear()

def borraLista(lista):
    del lista

def ord_mayor(lista):
    lista.sort(reverse=True)
def ord_menor(lista):
    lista.sort()
#MAIN

print("Elige tu propia aventura y pulsa el número correspondiente\n ")
print("1.- Crear lista")
print("2.- Añadir elemento al final")
print("3.- Añadir elemento en posición determinada")
print("4.- Borrar elemento en posición determinada")
print("5.- Borrar toda la lista de elementos")
print("6.- Borrar la lista como tal")
print("7.- Ordenar la lista de mayor a menor")
print("8.- Ordenar la lista de menor a mayor")
print("9.- Salir de este Pedazo de Programa pulsando 'N'")

opcion = int(input("Introduce tu opción: "))

while opcion != 9:
    if (opcion == 1):
        lista = crear(lista)
        print(lista)

    elif (opcion == 2):
        annadir(lista)
        print(lista)

    elif (opcion == 3):
        annadir_posicion(lista)
        print(lista)

    elif (opcion == 4):
        borrar_posicion(lista)
        print(lista)

    elif (opcion == 5):
        borrar_lista(lista)
        print(lista)

    elif (opcion == 6):
        borraLista(lista)
        print(lista)

    elif (opcion == 7):
        ord_mayor(lista)
        print(lista)

    elif (opcion == 8):
        ord_menor(lista)
        print(lista)

    elif (opcion == 9):
        print("Chao chao, salao!!")
        break

    else:
        print("¡¡eRRoR eN Tu eLeCCióN!!")



