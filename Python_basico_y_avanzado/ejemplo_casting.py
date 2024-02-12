'''
CONVERSIONES O CASTING EN PYTHON
    - CONVERSIÓN IMPLÍCITA: la que realiza automáticamente Python. Sucede cuando se realizan operaciones
    con 2 tipos de dato distintos
    - CONVERSIÓN EXPLÍCITA: la realizamos nosotros. Sucede cuando convertimos "a capón" un int en str
'''
#CONVERSIONES IMPLÍCITAS ----------------------------------------------------------
a = 1       #int
b = 2.5     #float
c = a + b   #c se convierte a float
print(c)
print(type(c))

d = "Hola, olita"
e = c + d # un float no se puede convertir en str sin utilizar ningún "cambiador de tipos (parseo)"
print(e)
print(type(e))

#CONVERSIONES EXPLÍCITAS ----------------------------------------------------------

#FLOAT - INT
a = 3.5
a = int(a) # casting a entero
print(a)
print(type(a))

#FLOAT - STRING
a = 3.5
a = str(a) # casting a string
print(a)
print(type(a))

#STRING - FLOAT
a = "3.5"
b = "Python"
a = float(a)  # casting a flotante
b = float(b)  # casting a flotante, pero da error, es una palabra y no un número... No se puede convertir
print(a)
print(type(a))
print(b)
print(type(b))

#STRING - INT
a = "3"
a = int(a)  # casting a entero
print(a)
print(type(a))

#INT - STRING
a = 35
a = str(a) # casting a string
print(a)
print(type(a))

#A LISTA
a = {1,2,3}
b = list(a) # casting a lista
print(type(a))
print(type(b))

'''
********************************************************************************************
*********** CUIDADO CON LOS TIPOS DE DATOS QUE ESTEMOS UTILIZANDO EN EL SOFTWARE ***********
********************************************************************************************
TIPOS DE DATOS INMUTABLES: INT     FLOAT       STRING      TUPLAS
Este tipo de datos son pasados por valor, es decir, dentro de las funciones (por ejemplo) se accede a una
copia y nunca a su valor original (estamos hablando a nivel de la máquina, en este caso, memoria)

TIPOS DE DATOS MUTABLES: LISTAS     DICCIONARIOS
Este tipo de datos se pasan por referencia, es decir, son algo parecido a los punteros en lenguaje C, accediendo
al dato original.
'''
#FUNCTIONS
def cargarContactos():
    contactos = {}
    continuar = 's'

    while continuar == 's':
        nombre = input("Introduce nombre del contacto: ")
        telefono = input("Introduce teléfono del contacto: ")
        contactos[nombre] = telefono
        continuar = input("¿Introducimos otro contacto más [s/n]?")
    return contactos
def modificarTlf(contactos):
    nombre = input("Introduce el nombre del contacto a modificar: ")
    if nombre in contactos:
        telefono = input("Introduce el nuevo número: ")
        contactos[nombre] = telefono
def imprimirContactos(contactos):
    print("*** LISTADO DE CONTACTOS ***")
    for nombre in contactos:
        print(nombre,contactos[nombre])
#MAIN
contactos = cargarContactos()
modificarTlf(contactos)
imprimirContactos(contactos)