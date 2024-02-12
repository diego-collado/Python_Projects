'''
ARCHIVO MAIN (EJECUTABLE)------------------------------------------------------
Crear una clase que administre una agenda personal. Se debe almacenar el nombre, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
    1.- Carga de un contacto en la agenda.
    2.- Listado completo de la agenda.
    3.- Consulta ingresando el nombre de la persona.
    4.- Modificación de su teléfono y mail.
    5.- Finalizar programa.
'''
#IMPORTS
import objectos23
'''
---------------------------------------- MÓDULOS ----------------------------------------
import nombrearchivo --> importa todo el archivo completo y total. En el caso de la bibliotecas, se importa
absolutamente todo, es decir, tenemos disponible todo el contenido, con el correspondiente peso en la carga
de nuestra aplicación

from nombrearchivo import función_determinada --> de forma única, carga la parte que yo quiero que se cargue,
lo cual me permite mejorar tiempos de carga, efectividad de mi programa...

from nombrearchivo import función_determinada1, función_determinada2, función_determinadaN

import math --> importamos todo el módulo de matemáticas
from math import sqrt, pow --> importamos las funciones/métodos raíz cuadrada y potencia del módulo de matemáticas

---------------------------------------- PAQUETES ----------------------------------------
Es un simple directorio donde se almacenan diferentes módulos bajo un mismo concepto.

...Unidad/Carpeta/Proyecto/...
    ├── main.py
    ├── loquesea1.py
    ├── loquesea2.py
    ├── loquesea3.py
    ├── matematicas/
    │   ├── __init__.py #nos obligan a tener un archivo __init__.py
    │   └── aritmetica.py
    │   └── geometria2D.py
    │   └── geometria3D.py

__init__.py --> nos sirve porque es de utilidad para instanciar objetos necesarios en nuestro proyecto, 
o lo que es lo mismo, tenemos un "nombre propio" de cada módulo, de cada función...

VENTAJAS DE MODULAR LOS PROGRAMAS -----------------------------------------------------------------
    · podemos trabajar varios programadores en el mismo proyecto sin interferir en cada uno de los sprints
    que tengamos que hacer
    · el tiempo de carga: "afinando" lo que quiero, carga más rápido y de forma más efectiva
    · evitamos fases de testing largas, es decir, nos podemos encargar de testear el programa "por partes"
    · evitas repetir el código, ya que tienes la mayor parte del trabajo "precocinado"
    · se puede reutilizar el módulo para otros proyectos que tengan la misma versión de Python
    · podemos utilizar los ALIAS:
        import modulolargodenaricesporquesemehaocurridoasi as m1
        ...
        m1.funcion1()
        Ejemplo: from math import sqrt as raiz, pow as elevar


DESVENTAJAS DE MODULAR LOS PROGRAMAS -----------------------------------------------------------------
    · ¿dónde colocamos cada módulo? Problema es la ruta, debe ser absoluta
    
    ...Unidad/Carpeta/Proyecto/...
    ├── main.py
    ├── loquesea1.py
    ├── loquesea2.py
    ├── loquesea3.py
    ├── carpetaProyectoX
    │   └── moduloA.py
    │   └── moduloB.py
    │   └── moduloC.py
    
    from carpetaProyectoX.moduloA import * 
    
    · ¿mis módulos son los mismos que los que vienen en Python instalados? NO, NO, NO y NO
    · ¿cada cosa necesita un módulo? Depende del proyecto... Ahí lo dejo...
    · Si el módulo está en una versión de Python diferente del main, puede que no funcione correctamente 
    · aunque llamemos 300K veces a un módulo, solo se carga 1 única vez:
    
    Esto es CACA:
        import mimodulo
        ....
        import mimodulo
        ....
        import mimodulo
        ....
    
    Código correcto:
        import mimodulo
        import importlib #Bibliteca de recargas e importanciones, viene preinstalada en Python
        ....
        importlib.reload(mimodulo)#recarga el módulo en cuestión
        ....
'''

#MAIN
agenda = objectos23.Agenda()
agenda.menu()