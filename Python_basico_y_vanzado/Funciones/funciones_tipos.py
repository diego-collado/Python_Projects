'''
FUNCIÓN:
    cuadrado --> se repite 50 veces.... ¿LO CODIFICARÍAS LAS 50 VECES?
    Qué tengo que hacer: codifico 1 vez, "copio" muchas veces...

¿Qué hace una función?
    - nos ayuda a organizar todo el código
    - nos permite utilizar la función donde quiera, cuando quiera y de una manera determinada
    - podemos utilizar funciones para ciertas cosas que hacemos siempre
'''

'''
Programa que muestre 2 valores cargados por teclado y su suma, además de un mensaje de despedida.

#Función sin parámetros 
# FUNCTIONS
def presentacion():
    print("###################################################")
    print("############ PROGRAMA QUE SUMA VALORES ############")
    print("###################################################")


def cargarSuma():
    valor1 = int(input("Introduce el primer valor:"))
    valor2 = int(input("Introduce el segundo valor:"))

    suma = valor1 + valor2
    print("La suma es: ",suma)

    print("(v2) La suma es: ", valor1 + valor2)

def finalizacion():
    print("###################################################")
    print("################# BYE BYE, COMPI ##################")
    print("###################################################")


# MAIN
presentacion()
cargarSuma()
finalizacion()

#EJEMPLO DE UNA CALCULADORA
#FUNCTIONS
def presentacion():
    print("###################################################")
    print("############## SUPERMEGACALCULADORA ###############")
    print("###################################################")

def calculadora():
    valor1 = int(input("Introduce el primer valor:"))
    valor2 = int(input("Introduce el segundo valor:"))

    suma = valor1 + valor2
    resta = valor1 - valor2
    multiplicacion = valor1 * valor2
    division = valor1 / valor2

    print("Suma del valor {} y el valor {}: {}".format(valor1, valor2, suma))
    print("Resta del valor {} y el valor {}: {}".format(valor1, valor2, resta))
    print("Multiplicación del valor {} y el valor {}: {}".format(valor1, valor2, multiplicacion))
    print("División del valor {} y el valor {}: {}".format(valor1, valor2, division))

def finalizacion():
    print("###################################################")
    print("################# BYE BYE, COMPI ##################")
    print("###################################################")

#MAIN
presentacion()
calculadora() #llamada a función, sin parámetros, la conocidas como VOID en otros lenguajes
finalizacion()'''

'''
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

- condicionales: 
if (condición a evaluar):
    código el que sea
elif (condición a evaluar):
    código el que sea
else:
    código el que sea

- estructuras de repetición (empiezan en 0):
for i in frase(total longitud de una frase):
    código el que sea
    
for i in range(5):
    código el que sea
    
while (condición a evaluar):
    código el que sea

'''
'''#FUNCTIONS
listaValores = [] #inicializamos una lista. Se comienza siempre a contar por 0
def cargarValores():
    for i in range(3):
        valor = int(input("Introduce valor: "))
        listaValores.append(valor)#añadimos el valor a lista, desde la posición/elemento 0

def cualMenor():
    for i in listaValores:
        if listaValores[i] > listaValores[i+1]:
            menor = listaValores[i+1]

        else:
            menor = listaValores[i]
#MAIN
cargarValores()
cualMenor()

#FUNCTIONS
def menorValor():
    valor1 = int(input("Introduce valor 1: "))
    valor2 = int(input("Introduce valor 2: "))
    valor3 = int(input("Introduce valor 3: "))

    if (valor1 < valor2) and (valor1 < valor3):
        print("El menor es: ", valor1)
    elif (valor2 < valor1) and (valor2 < valor3):
        print("El menor es: ", valor2)
    elif (valor3 < valor1) and (valor3 < valor2):
        print("El menor es: ", valor3)
    else:
        print("Valores idénticos")
#MAIN
menorValor()
menorValor()'''


'''
Docstrings: descripciones de qué se está codificando, cómo, qué utiliza, qué devuelve...


def hola (nombre):
    """ Este es un DocString de la función o elemento que quiero explicar """
    print("Hola, ",nombre, "!!")

hola("Diego")

help(hola)

class Clase:
    """ Este es el docstring de la clase"""
    def __init__(self):
        """Este es el docstring del inicializador de clase"""
    def metodo(self):
        """Este es el docstring del metodo de clase"""

o = Clase()
help(o)'''

#Función con parámetros --> a la función le pasamos "datos" con los que puede trabajar
#Paso por valor: creamos una copia local de la variable, por lo que la original no se "toca" y no se sobreescribe
x = 10
def funcion (entrada):
    entrada = 5

funcion(x)
print(x)

#Paso por referencia: actúamos sobre la variable original, es decir, la modificamos
x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)
funcion(x)
print(x)


#FUNCTIONS
def mostrarMayor(v1, v2, v3): #en la función, recibimos los ARGUMENTOS, datos que necesitamos para trabajar
    print("El mayor valor de todos es: ")
    if (v1 > v2) and (v1 > v3):
        print(v1)
    elif (v2 > v1) and (v2 > v3):
        print(v2)
    elif (v3 > v1) and (v3 > v2):
        print(v3)
    else:
        print("ninguno, son todos los números iguales...")
def cargarDatos():
    valor1 = int(input("Introduce número 1º: "))
    valor2 = int(input("Introduce número 2º: "))
    valor3 = int(input("Introduce número 3º: "))

    mostrarMayor(valor1, valor2, valor3)#llamo a la función y la envío con los datos (PARÁMETROS) que necesita

#MAIN
cargarDatos()

#función con parámetros indeterminados: *args
def suma(*args):
    suma = 0
    for arg in args:
        suma += arg
    return suma

print(suma(1,2,3,5,4,9,87))
print(suma(1,5))
print(suma(20,25,35,1525,25,58,25,477,58))

#función con parámetros por defecto: en el caso de operaciones, mínimo debemos tener 2 valores
def subrayado(titulo,caracter='*'):
    print(titulo)
    print(caracter*len(titulo))

subrayado("Sistema de asistencia al Hacker")
subrayado("Evaluación de hacking", '·')

#retorno de parámetros: return
#FUNCTIONS
def retornarSuperficie(lado):
    superficie = lado * lado
    return superficie

#MAIN
valor = int(input("Introduce el valor del lado del cuadrado: "))
superficie = retornarSuperficie(valor)
print("Superficie = ",superficie)

def cantidad_vocal_a(pal):
    cant = 0
    for x in range(len(pal)):
        if (pal[x] == 'a') or (pal[x] == 'A'):
            cant += 1
    return cant

palabra=input("Ingrese una palabra:")
print("La palabra",palabra,"tiene",cantidad_vocal_a(palabra),"a")

#Funciones con parámetros de tipo lista
#FUNCTIONS
def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

def mayor(lista):
    mayor = lista[0]#siempre se considera como el primero de la lista
    for i in range(1,len(lista)):#desde la posición 1 hasta el final de la lista
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def menor(lista):
    menor = lista[0]#siempre se considera como el primero de la lista
    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

#MAIN
listaValores = [10, 20, 30, 40, 50, 60]#una única variable con todos los elementos del interior: OBJETO
print("Lista completa: ", listaValores)
print("Suma: ", sumar(listaValores))
print("Mayor: ", mayor(listaValores))
print("Menor: ", menor(listaValores))