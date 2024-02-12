'''
Confeccionar una función que calcule la superficie de un rectángulo y la retorne,
la función recibe como parámetros los valores de dos de sus lados:
    def retornar_superficie(lado1,lado2):
'''
'''#Versión normal, para personas de la calle
def retornar_superficie(lado1,lado2):
    superficie = lado1 * lado2

    return superficie

lado1 = int(input("Introduce lado 1, primer rectángulo: "))
lado2 = int(input("Introduce lado 2, primer rectángulo: "))
lado3 = int(input("Introduce lado 1, segundo rectángulo: "))
lado4 = int(input("Introduce lado 2, segundo rectángulo: "))


superficie1 = retornar_superficie(lado1, lado2)
superficie2 = retornar_superficie(lado3, lado4)
print(f"Superficie del rectángulo 1 con medidas {lado1} x {lado2}: {superficie1}")
print(f"Superficie del rectángulo 2 con medidas {lado3} x {lado4}: {superficie2}")

if superficie1 > superficie2:
    print("El rectángulo más grande es el número 1")
else:
    print("El rectángulo más grande es el número 2")'''








