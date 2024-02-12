'''
paquete/
    __init__.py
    saludos.py
    script.py
'''
from paquete.saludos import Saludo
#de la carpeta llamada PAQUETE, importa el archivo (módulo) saludos.py

s = Saludo() #instanciamos una clase llamada Saludo.

'''
script.py
paquete/
    __init__.py
    hola/
        __init__.py
        saludos.py
    adios/
        __init__.py
        despedidas.py
'''
#paquete/hola/saludos.py ---------------------------------------
def saludar():
    print("Hola, te estoy saludando desde el método saludar(), módulo saludos")
class Saludo():
    def __init__(self):
        print("Hola, te estoy saludando desde el constructor de Saludos, módulo saludos")

#paquete/adios/despedidas.py ---------------------------------------
def despedir():
    print("Chao chao, te estoy saludando desde el método despedir(), módulo adios")
class Despedida():
    def __init__(self):
        print("Hola, te estoy saludando desde el constructor de Despedidas, módulo adios")

#script.py ---------------------------------------
from paquete.hola.saludos import saludar
from paquete.adios.despedidas import Despedida
from paquete.adios import *
from paquete.hola import *

'''
Que es y como funciona __init__.py:

Proyecto/
    main.py
    archivo1.py
    archivo2.py
    archivo3.py
    PythonPruebas/
        __init__.py
        pruebas1.py
        pruebas2.py

**** El archivo __init__.py se utiliza para realizar configuraciones de importación ****
En este archivo, podemos hacer disponibles:
    · clases
    · funciones
    · ...
Hacemos que el paquete tenga scope GLOBAL, es decir, qué todo el mundo conozca lo que tengo 
'''
#main.py
from PythonPruebas import * #importaría el paquete o lo que se defina en __init.py__

import PythonPruebas #cuando tenemos el archivo __init__.py vacío. No es obligatorio tenerlo con contenido

'''****
Lo que hace __init__.py es "convertir" un directorio en un modulo (paquete) que contiene otros módulos, 
y esto lo hace para poder importarlos
****'''


