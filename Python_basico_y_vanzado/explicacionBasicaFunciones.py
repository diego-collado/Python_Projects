'''
FUNCIONES: son bloques de código que se repiten pero que NO CODIFICAMOS NADA MÁS QUE 1 ÚNICA VEZ:
    - Las funciones suelen ser llamadas las veces que se considere necesarias
    - Organizas el código de una forma eficiente
    - Reutilizas el código las veces que se consideren necesarias
    - Te ayudan a refactorizar (rehacer el código y mejorarlo)

Sintaxis:
    def nombreFunción(argumentos):
        bloque_código_a_realizar
        return lo_que_se_envía_al_main

nombreFunción: CUIDADO CUIDADO Y CUIDADO---- NO UTILIZAR SÍMBOLOS NI CARACTERES "RAROS"

def registro_empleados_sueldo():
    pass --> no hace efecto, simplemente ejecuta un "nada"

def registroEmpleadoPagas():
    pass

'''

#FUNCTIONS

#Función vacía (no recibe nada)
def saluda():
    print("Hola, olita!!")

#Función con argumentos de entrada (se le envía material para que trabaje)
def saludame(nombre):#nombre es la variable que se va a utilizar en esta función, es decir, tiene scope local
    print("Hola, compi, sé que eres ", nombre)

#Función con return (retorno de resultados)
def multiplicacion_2(numero):
    nuevo_num = numero * 2
    return nuevo_num

def multiplicacion_2(numero):
    return numero * 2

#Función con argumentos dados por posición/por nombre
def resta(a, b):
    return a - b

def create_product(id_product, name, color, height, width, weight, price, manufacturer):
    print('text')


#Función con argumentos por defecto
def suma(a, b, c=0):#si no enviamos C, se considera como 0
    return a + b + c

#Función con argumentos de longitud variable
#Si lo hacemos con una lista:
def sumar(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

#Si lo hacemos con una tupla
def sumarX(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

#MAIN
saluda()#llamada a función vacía
saludame("Diego")#llamada a función con argumentos de entrada
y = multiplicacion_2(4)
print(y)

x = int(input("Introduce número: ")) #pedimos el argumento por teclado
print(multiplicacion_2(x))#imprimimos directamente el resultado de la llamada a la función con el argumento
resta(9, 6)#Función con argumentos dados por posición
resta(b=18, a=25)#Función con argumentos dados por nombre
create_product(1, '', 'black', 30, 21, 45, 5.00, 'Samsung')
print(suma(25, 25, 50))#Función con argumentos por defecto, con las 3 variables dadas
print(suma(25, 25))#Función con argumentos por defecto, con solo 2 variables dadas
sumar([1, 5, 10, 25])#Función con argumentos de longitud variable, con listas
total = sumarX(4, 5,6, 8, 9, 10)#te envío estos datos, no otros, no variamos estos...
print(total)