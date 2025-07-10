'''
Creación de calculadora básica:
    - sumar         - multiplicar
    - restar        - dividir

Condiciones a cumplir: 
    · necesitamos un menú con todas las posibilidades
    · dividir tiene que contemplar como error la división entre 0
    · el menú se ha de repetir hasta que se pulse salir
    · se piden 2 números para poder realizar la función matemática
    · los resultados se mostrarán en pantalla

Si la opción es 1, entonces...          --> if
Sino, si la opción es 2, entonces...    --> elif
Sino, si la opción es 3, entonces...    --> elif
Sino, si la opción es 4, entonces...    --> elif
Sino, error al canto                    --> else
'''

print("##### Calculadora básica ####\n\n")

print("1.- Sumar")
print("2.- Restar")
print("3.- Multiplicar")
print("4.- Dividir")

opcion = int(input("Introduzca la opción deseada (1-4): "))

if (opcion == 1):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print(f"El resultado de la suma de {num1} + {num2} es {int(num1 + num2)}")
    #print("El resultado de la suma de ",num1," + "," ",num2," es ",num1+num2)

elif (opcion == 2):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print(f"El resultado de la resta de {num1} - {num2} es {int(num1 - num2)}")

elif (opcion == 3):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    print(f"El resultado de la multiplicación de {num1} x {num2} es {int(num1 * num2)}")

elif (opcion == 4):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if num2 != 0: #!=  distinto de...
        print(f"El resultado de la división de {num1} / {num2} es {num1 / num2}")
    else:
        print("Error, no se puede dividir entre 0")

else:
    print("¡¡Deja de jugar con el teclado, melón!!")