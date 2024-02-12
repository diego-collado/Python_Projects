'''
EXCEPCIONES: en Python son una herramienta que controlar el comportamiento de un programa
cuando se produce un error. Realmente, lo que hace es parar "en seco" la ejecución del programa.

Tipos de Excepciones:
    · SyntaxError: invalid syntax --> error de sintaxis/interpretación
    · ZeroDivisionError: division by zero --> no permite dividir entre 0
    · NameError: name 'XX' is not defined --> falta definir algo en el código
    · TypeError: can only concatenate str (not "int") to str --> error de tipo en operaciones
    · ValueError: ocurre cuando introduces un valor de tipo que no es el que hemos definido
    · IndexError: se intenta acceder a una secuencia con un índice que no existe
    · KeyError: ocurre cuando se intenta acceder a un diccionario con una clave que no existe
    · ImportError: ocurre cuando falla la importación de un módulo
    · FileNotFoundError: ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada
    · OverflowError: ocurre cuando un cálculo excede el límite para un tipo de dato numérico
    · ModuleNotFoundError: cuando el import tiene problemas de carga

    · ArithmeticError, BufferError, LookupError, AssertionError --> Consultar:
**** https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions ****

A la hora de controlar los posibles errores generados por los usuarios, podemos utilizar los bloques
try-except:

try:
    ...código a ejecutar...
except tipo_excepción:
    ...código a ejecutar si hay excepción...

'''
'''try:
    dividendo = int(input("Introduce dividendo: "))
    divisor = int(input("Introduce divisor: "))
    print(f"El resultado de la división {dividendo} / {divisor} es {dividendo/divisor}")
except ZeroDivisionError:
    print("¡¡Calamar, no podemos dividir entre 0!!")
################################################################################
meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    num_mes = int(input("Introduce el número del mes [1-12]: "))
    print(meses[num_mes-1])
except IndexError:
    print("El número del mes debe estar entre 1 y 12... Ahí te lo dejo, Calamar...")
################################################################################
try:
    dividendo = int(input("Introduce dividendo: "))
    divisor = int(input("Introduce divisor: "))
    print(f"El resultado de la división {dividendo} / {divisor} es {dividendo / divisor}")
except ZeroDivisionError:
    print("¡¡Calamar, no podemos dividir entre 0!!")
except ValueError:
    print("¡¡Los valores, Calamar, son enteros!!")
################################################################################

try:
    dividendo = int(input("Introduce dividendo: "))
    divisor = int(input("Introduce divisor: "))
    print(f"El resultado de la división {dividendo} / {divisor} es {dividendo / divisor}")
except (ZeroDivisionError, TypeError, ValueError):#Modo VaGo ON, no distinguimos excepciones
    print("Error, comunique con el administrador del sistema")

try:
    dividendo = int(input("Introduce dividendo: "))
    divisor = int(input("Introduce divisor: "))
    print(f"El resultado de la división {dividendo} / {divisor} es {dividendo / divisor}")
except Exception as exc:
    print(f"*** Excepción ocurrida: {type(exc)}")#Imprimimos el tipo de excepción con type()
################################################################################
try:
    # La división puede realizarse sin problema
    x = 2/6
except:
    print("Entra en except, ha ocurrido una excepción")
finally:#este bloque se ejecuta siempre, haya o no haya habido excepción
    print("Entra en finally")
################################################################################
def solicitar_edad():
    try:
        return int(input("Escribe tu edad: "))
    except ValueError:
        return solicitar_edad()

edad = solicitar_edad()
################################################################################'''
edad = "Diego"
if not type(edad) is int:
    raise TypeError("Sólo permitimos números enteros")
#enerar excepciones cuando se produce algún error en el código, también puedes forzar
#a que se lance una excepción cuando tú consideres

x = 5
if type(x) == int:
    print("x es un entero")
'''
La función type(objeto, base, dict) tiene:
    · objeto: Es el objeto del cual se desea conocer su tipo
    · bases: Opcional. Especifica las clases base (padre)
    · dict: Opcional. Especifica el espacio de nombres con la definición de la clase
'''
#Generando una clase específica para las excepciones
class NuevaExcepcion(Exception):
    pass