'''
Programa que me controla si la contraseña que se introduce, tiene como
mínimo 20 caracteres y como máximo 30.
'''

# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ------------
password = input("Introduce la contraseña que quieres controlar: ")

contador = 0

# MAIN -------------------------------------------------
for i in password:
    print(f"Comprobación nº: {i}")
    contador += 1 #cuenta cada vuelta

# Otra forma de verlo
longitud = len(password) # nos ahorraríamos el for

print(contador)
if contador < 20 or contador > 30:
    print("Contraseña KO")
else:
    print("Contraseña OK")

#Saquemos conclusiones: forma 2 de verlo
print(longitud)
if longitud < 20 or longitud > 30:
# Otra solución para el if: if 20 <= longitud <= 30:
    print("Contraseña mala")
else:
    print("Contraseña guay")