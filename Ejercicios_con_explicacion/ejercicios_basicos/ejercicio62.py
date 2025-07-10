'''
Crea un programa en el que se implemente:
    - una función que devuelva los divisores de un número
    - que imprima la lista de divisores en pantalla

Divisor: aquel que divide a ese número de forma exacta, 
es decir, sin dejar residuo.
'''

# FUNCTIONS -----------------------------------
def obten_divisor(numero):
    divisores = []

    for i in range(1,numero+1): 
        #no se pueden entre 0, por eso comenzamos en 1
        #numero+1, para que llegue justo al número
        print(i)
        if numero % i == 0: #% me hace la división y me da el resto
            divisores += [i]
    return divisores
# MAIN ----------------------------------------
numero = int(input("Introduce un número: "))

print(f"Divisores de {numero}:\n {obten_divisor(numero)}")