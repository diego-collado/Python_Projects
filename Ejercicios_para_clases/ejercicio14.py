'''
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
'''

#FUNCTIONS
def cantidadAes(frase):
    contadorA = 0
    for i in range(len(frase)):
        if (frase[i] == 'a') or (frase[i] == 'A'):
            contadorA += 1
    return contadorA


#MAIN
frase = input("Introduce una frase: ")
cantidad = cantidadAes(frase)#llamada, pasando una variable con la que trabajará la función
print(f"El número de A en la frase es de {cantidad} aes.")