# Este es un comentario de una única línea

'''
Este es un comentario multilínea que, principalmente, nos sirve para poder describir documentación
'''

'''
The Zen of Python

1.- Bello es mejor que feo.
2.- Explícito es mejor que implícito.
3.- Simple es mejor que complejo.
4.- Complejo es mejor que complicado.
5.- Plano es mejor que anidado.
6.- Espaciado es mejor que denso.
7.- La legibilidad es importante.
8.- Los casos especiales no son lo suficientemente especiales como para romper las reglas.
9.- Sin embargo la practicidad gana a la pureza.
10.- Los errores nunca deben pasar silenciosamente.
** Los errores se pueden segmentar, es decir, apagamos el código para ver porqué y dónde está el error  **
11.- A menos que se silencien explícitamente.
12.- Frente a la ambigüedad, evitar la tentación de adivinar.
13.- Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
14.- A pesar de que esa manera no sea obvia a menos que seas Holandés (el creador lo era)
15.- Ahora es mejor que nunca.
16.- A pesar de que nunca es muchas veces mejor que ahora mismo.
17.- Si la implementación es difícil de explicar, es una mala idea.
18.- Si la implementación es fácil de explicar, puede que sea una buena idea.
20.- Los namespaces son una gran idea, ¡tengamos más de esos!
'''

#########################################COMENZANDO A CURRAR CON PYTHON#########################################
'''
Tipado de datos: exijo que una variable o constante, sea de un tipo determinado de dato:

    ** TIPOS DE DATOS SIMPLES **

    - números enteros (int): -1   5   1250    binarios:0b1010     hexadecimales: 0xa
    - números flotantes (float)/ números reales: 1.1    2.58498864654   3.141592
    - booleanos: True   False
    - cadena de caracteres (string): 'a' "hola" 'hola olita'  "432423234243"  "hola mundillo"

    ** TIPOS DE DATOS COMPUESTOS **
    - listas: secuencias de valores que pueden mutar (mutables)
    - tuplas: secuencias de valores que NO pueden mutar (inmutables)
    - conjuntos: representan conjuntos únicos de elementos, es decir, no hay cabida para elementos repetidos
    - diccionarios: son contenedores especiales de datos en que podamos trabajar cómodamente si accedemos a través de una clave
    (es el concepto más parecido a JSON)

Palabras reservadas en Python: palabras clave que NO PODEMOS NI DEBEMOS utilizar bajo ningún concepto ya que
son del propio Python. Su uso, genera errores de muchos tipos, a veces muy dificiles de localizar y remediar

False	await	else	import	pass
None	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	nonlocal	while
assert	del	global	not	with
async	elif	if	or	yield

Cualquier variable creada "fuera de cualquier estructura" tiene un SCOPE global. 
En casos como las funciones, tienes un SCOPE local.
SCOPE = alcance
'''
#Se puede crear una variable de cualquier tipo en cualquier momento sin necesidad de tiparla
a = 5
b = 17.8
x = 5; y = 17.8
#Si tenemos una línea que exceda 79 caracteres, podemos utilizar \ para que se ponga en la siguiente línea
c = 1 + 2 + 3 + 4 + 5 +\
    6 + 7 + 8 + 9 + 10
d = (1 + 2 + 3 + 4 + 5 +
    6 + 7 + 8 + 9 + 10)
z = True
t = 'hola mundo'

#Creamos e inicializamos variables
u = w = h = 10 #u=10   w=10   h=10
r, s = 4, 5 #r=4   s=5

#Nombrando variables: no puede comenzar por número, ni guiones y no se permite el uso de espacios
# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

# No válido
'''2variable = 10
var-iable = 10
var iable = 10'''

#Uso de paréntesis
y = ((x*3)-3)**((10-2)+3)
# + suma  - resta  * multiplicación  ** elevado a... (potenciación)  / división

'''
###### CASTING ######
cast/casting: convertir un tipo de dato en otro:
    - conversión implícita: método automático
        
    - conversión explícita: convierte a tipo de dato con funciones de Python
'''
#CONVERSIÓN IMPLÍCITA:
a = 1
b = 3.5

a = a + b
print(a)
print(type(a))

a = 1
b = "3.5"

a = a + b#No se puede hacer, da un error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a)
print(type(a))


#CONVERSIÓN EXPLÍCITA:
#float - int
a = 3.5
a = int(a)
print(a)

#float - string
a = 3.5
print(type(a))
a = str(a)
print(type(a))

#string - float
a = "35.5"
print(float(a))

#string - int
a = "3"
print(type(a))
a = int(a)
print(type(a))

#int - string
a = 10
print(type(a))
a = str(a)
print(type(a))

'''
ELEMENTOS DE UN PROGRAMA DE PYTHON:

    - palabras reservadas (keywords):if, elif, def, round...
    - funciones integradas (precocinadas --> built-in)
    - operadores: aritméticos, relacionales...
    - identificadores: son palabras de elementos creados por los usuarios --> Variables y Constantes
        · letras mayúsculas/minúsculas
        · número y _
        · caracteres UNICODE
        · caracteres ASCII
        NO SE PERMITEN: signos de puntuación como @, $ y %, excepto el guión bajo (_) --> se considera privado
        _mivariable
        
    - literales: son datos simples (puros / primitivos) en Python:
        · números--> valores lógicos, enteros, decimales, complejos, notación decimal/octal/hexadecimal
        · cadenas de texto --> string
    - delimitadores: 
        '       "       #       \
        (       )       [       ]       {       }
        ,       :       .       ;       @       =       ->
        +=      -=      *=      /=      //=     %=      @=
        &=      |=      ^=      >>=     <<=     **=
'''
'''
Tupla (tuple): algo parecido a una lista, con la salvedad que sus elementos son INMUTABLES:
    - creamos una tupla y después NO se pueden variar sus elementos (NO SE MODIFICAN)
    - se iniciliza con (  )
'''
tupla = (1, 2, 3)
tupla2 = 1, 2, 3
tupla[2] = 5 #NO SE PERMITE, DA ERROR, produce un TypeError

tupla = 1, 2, ('a', 'b'), 3 #tuplas anidadas

#Conversión de lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)

#Iteración
tupla = 1, 2, 3
for t in tupla:
    print(t)
#MÉTODOS UTILIZADOS EN TUPLAS
l = [1, 1, 1, 3, 5]
print(l.count(1)) #count(1) --> cuenta los elementos que son como el ejemplo que pasamos, es decir, 3 unos en la lista

l = [7, 7, 7, 3, 5]
print(l.index(5))#busco el elemento que me pasas y devuelvo su posición
#devuelve un ValueError

print(l.index(7, 2))#busco el elemento que me pasas y devuelvo su posición, comenzando por la posición 2

'''
Confeccionar un programa con las siguientes funciones:
    1)Cargar una lista de 5 enteros.
    2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
'''
#se carga como siempre hemos hecho en las listas: con for .....
lista = []
tupla = ()

