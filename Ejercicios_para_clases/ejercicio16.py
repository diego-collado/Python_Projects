'''
Confeccionar una función que reciba entre 2 y 5 enteros.
La misma nos debe retornar la suma de dichos valores.
Debe tener tres parámetros por defecto.
'''
#FUNCTIONS
def suma(num1, num2, num3 = 0, num4 = 0, num5 = 0):
    suma = num1 + num2 + num3 +num4 + num5
    return suma

#MAIN
print("Suma de 5 + 6: ",suma(5,6))
print("Suma de 5 + 6 + 8: ",suma(5,6, 8))
print("Suma de 5 + 6 + 8 + 30: ",suma(5,6, 8, 30))
print("Suma de 5 + 6 + 8 + 30 + 100: ",suma(5,6, 8, 30, 100))