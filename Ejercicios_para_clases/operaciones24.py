'''
MÓDULO DE OPERACIONES
Calculadora con sumas, restas, multiplicaciones, divisiones, raíz cuadrada y raíz cúbica
'''

class Calculadora:

    def __init__(self):
        pass#no hacemos nada, ejecuta el constructor (en este caso) y "pasa de él"

    def menu(self):
        opcion = 0

        while opcion != 7:
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Raíz cuadrada")
            print("6. Raíz cúbica")
            print("7. Finalizar este maravilloso Pograma")

            opcion = int(input("Introduce tu elección: "))

            if (opcion == 1):
                self.sumar()
            elif (opcion == 2):
                self.restar()
            elif (opcion == 3):
                self.multiplicar()
            elif (opcion == 4):
                self.dividir()
            elif (opcion == 5):
                self.r_cuadrada()
            elif (opcion == 6):
                self.r_cubica()
            elif (opcion == 7):
                print("Bye, Bye, BaBy!!")
                break;
            else:
                print("¡¡eRRoR, eSTa oPCióN No eXiSTe!!")

    def sumar(self):
        valor1 = int(input("Introduce el primer valor: "))
        valor2 = int(input("Introduce el segundo valor: "))
        #resultado = valor1 + valor2
        print(f"La suma de {valor1} y {valor2} es de {valor1 + valor2}")
        print("___________________________________________________")
    def restar(self):
        valor1 = int(input("Introduce el primer valor: "))
        valor2 = int(input("Introduce el segundo valor: "))
        print(f"La resta de {valor1} y {valor2} es de {valor1 - valor2}")
        print("___________________________________________________")
    def multiplicar(self):
        valor1 = int(input("Introduce el primer valor: "))
        valor2 = int(input("Introduce el segundo valor: "))
        print(f"La multiplicación de {valor1} y {valor2} es de {valor1 * valor2}")
        print("___________________________________________________")
    def dividir(self):
        valor1 = int(input("Introduce el primer valor: "))
        valor2 = int(input("Introduce el segundo valor: "))
        print(f"La división de {valor1} y {valor2} es de {valor1 / valor2}")
        print("___________________________________________________")
    def r_cuadrada(self):
        valor = int(input("Introduce el valor para la raíz: "))
        print(f"La raíz cuadrada de {valor} es de {valor ** 0.5}")
        #se puede importar: from math import sqrt
        print("___________________________________________________")
    def r_cubica(self):
        valor = int(input("Introduce el valor para la raíz: "))
        print(f"La raíz cúbica de {valor} es de {valor ** (1 / 3)}")
        #se puede importar: from math import cbrt
        print("___________________________________________________")
