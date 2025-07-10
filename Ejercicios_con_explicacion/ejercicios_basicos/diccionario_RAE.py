'''
Diccionarios: su estructura nos permite acceder a los valores utilizando una clave:

    · PRODUCTOS: manzanas, peras, melocotones...
    · CANTIDAD DE PRODUCTOS: 15, 25, 80
    
DICCIONARIO CREADO --> productos {'manzanas':15.00, 'peras':25.00, 'melocotones':80.00}

Si nos vamos a la realidad, la clave sería la palabra que buscamos y el valor la definición.

Sintaxis: nombreDiccionar = {clave:valor, clave:valor,... clave_n:valor_n}

# DECLARACIÓN DE VARIABLES GLOBALES ------
paises = {"España":14, "Francia":25, "Alemania":80, "Albania":11}

# FUNCTIONS ------------------------------
def imprimir(paises):
    for pais in paises:
        print(f"País: {pais} - Nº habitantes: {paises[pais]}")

# MAIN -----------------------------------
imprimir(paises)
'''

'''
Tenemos que desarrollar una aplicación que nos permita crear un diccionario inglés/español.
La CLAVE será la palabra en inglés, por lo que si existe, mostraremos la traducción.
Necesitamos:
    · 1) cargar el diccionario
    · 2) listar el diccionario completo
    · 3) introducir por teclado una palabra en inglés y mostrar su traducción (si existe)
'''
# DECLARACIÓN DE VARIABLES GLOBALES ------
# diccionario = {} de esta forma, creamos el diccionario antes de todo... ¿Mejor o Peor? Para gustos...

# FUNCTIONS ------------------------------
def cargar():
    # 1.- Creamos e inicializamos el diccionario - está en vacío
    precargar_diccionario = {} # Ahora mismo, esta variable de tipo diccionario es LOCAL a esta función

    # 2.- Cargamos el diccionario con los datos que queramos (bucle)
    continuar = 's'

    while (continuar == 's') or (continuar == 'S'):
        # Pedimos los datos por teclado
        ingles= input("Introduce la palabra en inglés: ")
        castellano = input(f"Introduce la traducción de la palabra {ingles}: ")

        # Cargamos los datos al diccionario
        precargar_diccionario[ingles] = castellano # La palabra en INGLÉS que tendrá su traducción al CASTELLANO

        # Comprobamos si se sigue la carga o no
        continuar = input("\n¿Quieres continuar introduciendo palabrotas (S/N)?")
    # "sacamos" de la función el diccionario que hemos cargado, por lo que ya tenemos una variable GLOBAL
    return precargar_diccionario

def imprimir(diccionario):
    print("############ DICCIONARIO BILINGÜIS ############")
    for palabras in diccionario:
        print(f"Palabra: {palabras} -- Traducción: {diccionario[palabras]}")

def consultar_palabra(diccionario):
    palabra_consultar = input("Introduce la palabra a consultar: ")
    if palabra_consultar in diccionario:
        print(f"Palabra consultada: {palabra_consultar}, tiene la traducción: \n '{diccionario[palabra_consultar]}'")
    else:
        print("¡¡La palabra buscada no existe en nuestro diccionario")

# MAIN -----------------------------------
diccionario = cargar() # es una forma de crear e inicializar
imprimir(diccionario) # el parámetro que enviamos es el diccionario completo
consultar_palabra(diccionario) # aquí, la misma jugada... 