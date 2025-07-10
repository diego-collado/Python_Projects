'''
Conversor de criptomonedas: se han utilizado funciones, diccionarios y estructuras básicas
¿Qué debería hacer el conversor?
    · disponer de los valores reales de cada criptomoneda
    · mostrar y convertir el valor que introducimos en base al valor real
    · los valores se van a expresar en €
    · monedas disponibles para la conversión
-------------------------------------------------------------------------------
NOTAS:DocStrings
Básicamente, es la ayuda de nuestro programa... ¡¡Hay que explicar fielmente qué hace o 
cómo lo deberíamos manejar!!

Ejemplo: 


def hola():
    """
Conversor de Criptomonedas (Bitcoin, Ethereum, DodgeCoin, LiteCoin) en el que debemos
introducir el valor a convertir para que el conversor nos de bien el total en € o transformado
en la cripto que deseemos.
"""
    print("Hola")

help(hola)
---------------------------------------------------------------------
LOQUESEAEN_MAYUSCULAS --> significa que es una constante, aunque no se trate como tal...
Python puede hacer lo mismo que con una variable... En otros lenguajes de programación,
si es constante, el propio lenguaje impide hacer ciertas acciones.
---------------------------------------------------------------------
Diccionarios: es un OBJETO, es decir, 1 elemento que contiene múltiples elementos.

Contactos = {
    "Nombre":"Diego",
    "Edad":48,
    "Tlf":"(+34) 645.154.916"
}
print(Contactos)
---------------------------------------------------------------------
def obtener_tasa(moneda:str) -> float | None:
def nombre_funcion (variable:tipo_esperado) -> tipo_retorno | tipo_si_no_lo_encuentra:
'''

# GLOBAL VARS ----------------------------------------------------
TASAS_EUR = {
    # Valores de las criptos expresados en €
    'EURO': 1.0,
    'BTC': 81240.93,
    'ETH': 2023.94,
    'DOGE': 0.142705,
    'LTC':73.07
}

# FUNCTIONS ------------------------------------------------------

# Monedas disponibles para conversión #
def mostrar_monedas():
    """
    Muestra las monedas disponibles para la conversión
    """
    print("\n\nMonedas disponibles a día de hoy \n\n")

    for moneda in TASAS_EUR:
        print (f"- {moneda}")

# Tasa de conversión #
def obtener_tasa(moneda:str) -> float | None:
    """
    Se obtiene la tasa de conversión de una cripto al €.
    Parámetros que vamos a pasar:
        - moneda (string): debemos ingresar el nombre de la moneda
    Qué nos va a retornar:
        - float (decimal), si la moneda existe y se puede convertir
        - None (nada de nada), si la moneda NO existe en nuestro diccionario
    """
    return TASAS_EUR.get(moneda.upper())# del diccionario, dame el valor de la moneda en mayúsculas

# Conversión entre monedas #
def convertir(origen:str,destino:str,cantidad:float) -> float | None:
    """
    Convierte una cantidad X de una moneda a otra.
    Parámetros que vamos a pasar:
        - moneda_origen, string de la moneda de origen, la que tenemos
        - moneda_destino, string de la moneda destino, a la que cambiamos
        - cantidad, float de la cantidad que queremos convertir
    Qué nos va a retornar:
        - float (decimal), si la moneda existe y se puede convertir
        - None (nada de nada), si la moneda NO existe en nuestro diccionario
    """
    # Obtenemos los valores para poder convertir, es decir, qué precio tiene cada moneda
    tasa_origen = obtener_tasa(origen) #obtenemos el valor para la moneda de origen
    tasa_destino = obtener_tasa(destino) #obtenemos el valor para la moneda de destino

    # Puede que tengamos algún valor en None
    if(tasa_origen is None) or (tasa_destino is None):
        print("Error, moneda no reconocida...")
        return None

    # Empezamos a convertir realmente
    cantidad_euros = cantidad * tasa_origen # 1 LTC es 73.07€
    resultado = cantidad_euros / tasa_destino # 730.70€ en LTC, son 10 LTC
    
    return resultado # retorno real de esta función

# Función Principal - lógica del programa
def main():
    print("============ CONVERSOR CRYPTOS -> € ============")

    #1.- Mostrar qué monedas tenemos disponibles para conversión
    mostrar_monedas()

    #2.- Recoger qué queremos convertir y a qué queremos convertirlo
    
    #.strip() quitar espacios en blanco y .upper() convierte en mayúsculas. En minúsculas, .lower()
    origen = input("Introduce la moneda de origen: ").strip().upper()
    destino = input("Introduce la moneda de destino: ").strip().upper()

    #3.- Necesitamos saber la cantidad de monedas a convertir
    try:
        cantidad = float(input(f"Introduce la cantidad de {origen}:  "))
    except ValueError:
        print("Por favor, introduce un valor correcto")
        return # se saldría de la parte try-except

    # convertimos
    resultado = convertir(origen, destino, cantidad)

    # comprobamos que no haya errores
    if (resultado is not None): # si el resultado no es None, hacemos lo que sea
        print(f"\n\n{cantidad} de {origen}, son {resultado:.6f} {destino}\n")
        # resultado:.6f quiere decir que tendrá 6 decimales

# MAIN -----------------------------------------------------------
if __name__ == "__main__":
    main()