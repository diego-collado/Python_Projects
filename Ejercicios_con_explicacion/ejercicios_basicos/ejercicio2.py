'''
TIPOS DE DATOS ---------------------------------------------------------------------------

    - DATOS SIMPLES (PRIMITIVOS):
        · números enteros (int): 1 3 5 1,234 // binarios: 011010 // hexadecimales: #FFF
        · números decimales (flotantes / con coma flotante / float): 0,1  2,5 .2
        · booleanos: True   False
        · cadenas de caracteres (string): "hola" 'a' 'opcion' "Remate" "1231243245,5"

    - DATOS COMPUESTOS (AVANZADOS / COMPLEJOS):
        · listas: secuencias de valores que pueden mutar (mutables)
        · tuplas: secuencias de valores que NO pueden mutar (inmutables)
        · conjuntos: representamos conjuntos únicos de elementos, no hay
        cabida para elementos repetidos
        · diccionarios: contenedores de datos a los que se accede mediante
        el par clave: valor, como JSON

PALABRAS RESERVADAS: ¡¡NO LAS PUEDO USAR!! ----------------------------------

En un programa, creamos "cajas" en las que metemos valores... Esas cajas
son, realmente, las variables. 
A veces, disponemos de ciertas "cajas" que no se pueden utilizar.

False   await   else    import  pass    None    break
True    except  in      raise   class   finally is
return  and     for     lambda  def     as      continue   
from    nonlocal        while   assert  del     global
async   elif    if      not     with    or      yield


UNA DE PALABROTAS: SCOPE (ÁMBITO / ALCANCE) -------------------------------------
Cuando creamos variables, estas pueden ser de 2 tipos:
    - globales: scope "completo", es decir, cualquier parte del código la conoce
    - locales: scope "loca", es decir, solo se conoce en ciertas zonas "cerradas"

'''

# EMPEZANDO A JUGAR: EL CÓMO, EL DÓNDE, EL CUÁNDO...
# 1.- Llamando a cada cosa por su nombre:

# Nombrando las variables de forma válida
_variable = 10
var_iable = 10
variable10 = 10
varIable = 10

snake_case = 10
nombre_apellidos = "Diego Collado Ramos"
camelCase = 10
nombreApellidos = "Diego Collado Ramos"

 # Si lo nombro así... ¡¡Error!!
"""2variable = 10
var-iable = 10
var iable = 10 """

# 2.- Asignando los valores:

nombre = "Diego Collado"
edad = 48

a, b, c = 10, 20, 30
# Si lo hacemos sin resumir...
a = 10
b = 20
c = 30

# límite "visual": 79 caracteres - \ a nivel visual y a nivel de ejecución
suma =  1 + 2 + 5 + 10 + 10 + 5 + 8 + 9 + 7 +\
      99 + 2 + 98 + 45869 + 469 + 48 + 498 + 4984 + 584694 + 698489

# 3.- Inicialización:
num1 = 0
num2 = 0
nombre = ""

# 4.- Una de "cosas raras"
z = h = j = d = 0 # inicialización múltiple
y = ((((z*3) + (h/7)) / j) + (8 * 2)) + d # uso de paréntesis
# Puedo hacer... + - * / ** % son las operaciones más básicas

'''
ESTRUCTURANDO UN PROGRAMA CON PYTHON:

    ELEMENTOS:
        · palabras reservadas: if, else, def... son Python como tal
        · funciones "precocinadas", llamadas BUILT-IN
        · operadores: aritméticos, relacionales...
        · identificadores:
            - variables: identificador cuyo valor varia en el ciclo de vida de un programa
            - constantes: identificador cuyo valor NO varia en el ciclo de vida de un programa

            letras mayúsculas, minúsculas, símbolos, números, _
            caracteres UNICODE y ASCII
            NO PERMITIDO: @ $ %
        · delimitadores: me ayuda a "encerrar" elementos
        ' " # \ ( ) [ ] { } , : ; += -= *= /= = == ->
        &= |=  ^= >>= <<=  **= @ <= >= !=
    
    ESTRUCTURA REAL DE UN PROGRAMA EN PYTHON

        1.- Importaciones de archivos o bibliotecas externas (módulos)
        2.- Constantes globales (si son necesarias)
        3.- Clases
        4.- Funciones
        5.- Función MAIN o PRINCIPAL: es el punto de entrada, es decir,
        se ejecuta si el archivo es el principal

        if __name__ == "__main__":
            el código...     
'''
