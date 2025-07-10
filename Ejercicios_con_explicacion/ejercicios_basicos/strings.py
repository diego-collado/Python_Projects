'''
Hablemos de las CADENAS DE CARACTERES... donde nos encontramos los 
famosísimos tipos de dato string. La cuestión es que este tipo de
variables es INMUTABLE y permite almacenar secuencias de caracteres.

'''

cadena = "Esto es una cadena" # string

x = 5
s = "El número es " + str(x)
print(s)

s = "El número es %f" %x
print(s)

s = "El número es %d y %d" %(5,10)
print(s)

s = "El número es {} y {}".format(8,90)
print(s)

a= 465
b = 987
s = f"El número es {a} y {b}"
print(s)

print("me mola" in "Python me mola") 
# así sabemos si está o no algo dentro de algo

print(len("En un país de cuyo nombre no quiero acordarme porque me trae malos recuerdos y ya no me acuerdo de nada más... Es viernes, también comprende cómo estoy..."))
# len(variable)  //  len(texto) nos calcula el tamaño en caracteres.