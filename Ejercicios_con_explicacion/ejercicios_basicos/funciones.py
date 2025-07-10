'''
Crea un cuadrado 25000 veces... ¿Lo codificarías?
Yo NO... Para esto utilizamos las funciones: se programa una vez y se llama X veces

¿Para qué necesito una función?
    · ayuda a organizar el código
    · permite que su utilización en cualquier sitio
    · tiene la forma de trabajo que queramos nosotr@s
    · las cosas que repites X veces, es mejor tenerlas en funciones

ESTRUCTURANDO (DE NUEVO) NUESTRO CÓDIGO ------------------------------------------------

# FUNCTIONS
.... aquí creamos las funciones necesarias

# MAIN
.... el resto del programa y llamadas a esas funciones

Codificando de forma básica:
    def nombre_funcion():
        lo_que_quieras_hacer

Llamando a la función:    
    nombre_funcion

Con argumentos:
    def nombre_funcion(argumentos_para_trabajar):
        lo_que_quieras_hacer

Llamando al a función:
    nombre_funcion(argumentos_con_los_que_trabajar)
'''
# FUNCTIONS---aquí es el bloque donde declaramos las funciones necesarias
def di_hola():
    print("¡¡Hola!!")

# Pasando argumentos de entrada
def diHola(nombre):
    print(f"Hola, {nombre}!!")

# Pasando argumentos por posición
def suma(num1,num2):
    print(f"Resultado: {num1 + num2}")

# Pasando argumentos por nombre
def multiplicacion(num1,num2):
    print(f"Resultado: {num1 * num2}")

# Pasando argumentos por defecto
def resta(num1,num2,num3=0):
    print(f"Resultado: {num1 - num2 - num3}")

# Pasando argumentos de longitud variable - utilizando una lista
def sumando(numeros):
    total = 0
    for num in numeros:
        total += num
    print(f"Resultado: {total}")

# Pasando argumentos de longitud variable - real
def sumatorio(*numeros): #si llamamos a type(numeros), es un tipo tupla
    total = 0
    for num in numeros:
        total += num
    print(f"Resultado: {total}")

# MAIN---aquí es el bloque donde tengo las llamadas a funciones y demás lógica del programa
di_hola() # llamando a una función sencillita
diHola("Diego") # te paso "algo" para que tú puedas trabajar
suma(4,5)
# suma(3,7,6,4,2,12) --> da error, pasamos demasiados argumentos
# multiplicacion(num1=8, num2=5, num3=44) --> da error, nombramos un argumento que no existe
resta(55,11)
resta(55,11,11)
sumando([1,2,3,4,54,56,7,7,78,86,9,789,789,789,879,7])
sumatorio(1,2,3,4,54,56,7,7,78,86,9,789,789,789,879,43427)