'''
Ejercicio calculadora: Crearemos una calculadora que va a permitirnos:
    - sumar     - dividir
    - restar    - multiplicar

EXPLICACIÓN PARA AYUDAR...

Condicional básico de verdad

if (condición_a_evaluar):
    ejecutar_lo_que_sea-si_se_cumple
else:
    ejecutar_lo_que_sea-si_no_se_cumple


Condicional anidado (múltiple)
if (condición_a_evaluar):
    ejecutar_lo_que_sea-si_se_cumple
elif (condición_a_evaluar): --> elif significa else if, sino si...
    ejecutar_lo_que_sea-si_se_cumple
...
else:
    ejecutar_lo_que_sea-si_no_se_cumple
'''
# Impresión del menú en pantalla -----------------------------
print("- - - - - - - - -  MEGACALCULADORA - - - - - - - - -\n\n\n")
print("Bienvenid@s a nuestra aplicación... Elige la opción\n")

print("1.- SUMAR")
print("2.- RESTAR")
print("3.- MULTIPLICAR")
print("4.- DIVIDIR")

opcion = int(input("Elige la opción que necesitas:  "))

# Introducción de números para poder comenzar a trabajar
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))

# Ahora, al atún... Lógica del negocio ----------------------
if (opcion == 1):
    print("La suma es: ", numero1 + numero2)
elif (opcion == 2):
    print("La resta es: ", numero1 - numero2)
elif (opcion == 3):
    print("La multiplicación es: ", numero1 * numero2)
elif (opcion == 4):
    print("La división es: ", numero1 / numero2)
else:
    print("######## eRRoR, No TeNeMoS eSa oPCióN DiSPoNiBLe ########")
