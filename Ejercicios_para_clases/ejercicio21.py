'''
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
    - inicializar los atributos
    - imprimir el valor del lado mayor y otro método que muestre si es equilátero o no

El nombre de la clase llamarla Triangulo.
'''
#CLASS
class Triangulo:
    def inicializar(self):#self hace referencia al objeto que estamos manipulando
        self.lado1 = int(input("Introduce valor lado 1: "))
        self.lado2 = int(input("Introduce valor lado 2: "))
        self.lado3 = int(input("Introduce valor lado 3: "))

    def imprimir(self):
        print("Valores del triángulo: \n")
        print(f"Lado 1: {self.lado1} - Lado 2: {self.lado2} - Lado 3: {self.lado3}")

    def lado_mayor(self):
        if (self.lado1 > self.lado2) and (self.lado1 > self.lado3):
            print(f"El lado mayor es {self.lado1}")
        elif (self.lado2 > self.lado3) and (self.lado2 > self.lado1):
            print(f"El lado mayor es {self.lado2}")
        else:
            print(f"El lado mayor es {self.lado3}")
    def equilatero(self):
        if (self.lado1 == self.lado2) and (self.lado1 == self.lado3):
            print("El triángulo es equilátero")
        else:
            print("El triángulo NO es equilátero")


#MAIN: solamente se llama a cada de las acciones que queramos hacer, como crear un objeto de la clase X, imprimir su contenido...
#1ª acción SIEMPRE: instanciar el objeto: crear un objeto de clase X

triangulo1 = Triangulo()#instanciación
#métodos
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.equilatero()
