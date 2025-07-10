'''
Módulos: son archivos .py que contienen código reutilizable (funciones, clases, variables...)
Podemos dividir el código en partes manejables.
Estructura básica para los módulos:
    main.py
        |- clientes.py
        |- proveedores.py
        |- productos.py
    
#saludo.py -------------------------
def saludar(nombre):
    return print(f"Hola, {nombre}")

#main.py -------------------------
import saludo
print(saludo.saludar("Diego"))

TIPOS DE MÓDULOS o también llamados LIBRERÍAS: 
    · los míos propios, construidos por nosotr@s mism@s
    · módulos estándar, preinstalado ya con Python (math, datetime, os, sys, json)
    · módulos de 3º, como numpy, pandas, requests...
        En la consola de Windows, MacOS o Linux, tenemos que instalar la librería:
            pip install nombre_librería

¿CÓMO IMPORTO LOS MÓDULOS? IMPORTANDO DE DIFERENTES FORMAS

import modulo
import modulo as alias --> 
    import math as matematicas
    import beautifulsoup4 as bt --> bt.saludo
    import saludo as s --> s.saludar("Diego")
from modulo import funcion

- ATENCIÓN - ATENCIÓN - ATENCIÓN - ATENCIÓN -
from modulo import * ---> lo mejor es no utilizar este tipo de llamadas... para eso,
podemos importar import modulo.
'''

#import math # módulo instalado con Python. import nombre te carga el archivo completo
from math import sqrt, pi # carga únicamente lo que quiero de un módulo

#print(math.pi) # llamada a una parte del módulo importado
print(sqrt(16)) # llamada a una funcionalidad de un módulo
print(pi)

###################### IMPORTACIONES, NORMALMENTE EN EL MAIN!! ######################
