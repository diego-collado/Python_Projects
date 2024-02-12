'''
Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18
(como mínimo se envía un entero a la función)
'''
#FUNCTIONS
def mayor18(edad1, *edades): #* me permite recibir la segunda o más cantidad de variables para trabajar
    # (o no recibir absolutamente nada de nada)
    cantidad = 0
    if edad1 >= 18:
        cantidad += 1

    for i in range(len(edades)):
        if edades[i] >= 18:
            cantidad += 1

    return cantidad
#MAIN
print("La cantidad de personas mayores de 18 es: ",mayor18(46,46,8,6,14,38,42,45))
print("La cantidad de personas mayores de 18 es: ",mayor18(6,14,38,42,45))