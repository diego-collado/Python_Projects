'''
Diccionario: estructura es clave: valor, de modo que para acceder al valor, tengo que conocer la clave
Es mutable, es decir, sus elementos pueden ser borrados, agregados, modificados...
Conceptos:
    - diccionario tradicional: la clave sería la palabra y el valor sería la definición de dicha palabra
    - agenda personal: la fecha sería la clave y las actividades de dicha fecha sería el valor
    -  conjunto de usuarios de un sitio web: nombre de usuario sería la clave y como valor podríamos almacenar su mail,
    clave, fechas de login etc

Sintaxis:
    nombreDiccionario = {"clave":valor, "clave":valor,"N_clave":N_valor,}
    productos={"manzanas":39, "peras":32, "lechuga":17}


def imprimir(paises):
    for clave in paises:
        print(f"Clave: {clave} - Nº Habitantes (mill.): {paises[clave]}")

#MAIN
paises = {"España": 24, "Francia":25, "Alemania": 32, "Congo Belga":500}
imprimir(paises)'''

'''
Ejemplo práctico de ejercicio:
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. 
La clave es la palabra en ingles y el valor es la palabra en castellano.
Crear las siguientes funciones:
    1) Cargar el diccionario.
    2) Listado completo del diccionario.
    3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.

'''
#FUNCTIONS
def cargar():
    #crear el diccionario como tal e inicializarlo vacío
    diccionario = {}

    #cargo el diccionario hasta que me canse
    continuar = 's'
    while (continuar == 's') or (continuar == 'S'):
        castellano = input("Introduce una palabra en castellano: ")
        ingles = input("Introduce una palabra en inglés (traducción): ")

        #cargamos el diccionario con los valores, con la sintaxis: diccionario[clave] = valor
        diccionario[ingles] = castellano

        continuar = input("¿Quieres cargar más palabrotas (S/N)? ")
    return diccionario
def imprimir(diccionario):
    print("***** Nuestro diccionario de la Real Academia del Hacking *****")
    for ingles in diccionario: #mientras haya claves en el diccionario...
        print(f"Inglés: {ingles} - Castellano: {diccionario[ingles]}")
def consultar_palabra(diccionario):
    palabra = input("Introduce la palabra en inglés para consultar: ")
    if palabra in diccionario: #si la palabra está en el diccionario...
        print(f"La palabra que buscabas es {palabra}, cuya traducción al castellano es {diccionario[palabra]}.")
    else:
        print("¡¡Lo siento, ese palabro no está en nuestro hackDiccionario!!")


#MAIN
diccionario = cargar()
imprimir(diccionario)
consultar_palabra(diccionario)

