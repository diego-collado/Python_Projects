'''
Desarrollar un programa en el que carguemos los lados de un triángulo
y podamos disponer de la siguiente información:
    · ininialización de atributos
    · impresión del valor del lado mayor 
    · clasificación del triángulo según sus lados:
        - equilátero --> 3 lados iguales
        - isósceles --> 2 lados iguales
        - escaleno --> todos los lados distintos
'''

# CLASS -------------------------------------------
class Triangulo: 
    # inicialización de atributo/s:
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0
    
    # Lo que puede hacer: los métodos

    def cargar_lados(self):
        print("Introduce los 3 lados del triángulo:\n")
        self.lado1 = float(input("Lado 1: "))
        self.lado2 = float(input("Lado 2: "))
        self.lado3 = float(input("Lado 3: "))

    def lado_mayor(self):
        mayor = max(self.lado1,self.lado2,self.lado3) 
        # max() nos permite saber qué valor es el mayor de todos
        print(f"El lado mayor es: {mayor}")
    
    def es_equilatero(self):
        if (self.lado1 == self.lado2 == self.lado3):
            print("Felicidades, es un triángulo equilátero...")
        else:
            print("¡¡Qué chasco!! No es un triángulo equilátero...")

    def clasificar_por_lado(self):
        self.es_equilatero()
        
        if(self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3):
            print("Felicidades, es un triángulo isósceles...")
        
        else:
            print("Felicidades, es un triángulo escaleno...")

# MAIN -------------------------------------------
triangulo1 = Triangulo() # 1.- Creo un objeto de tipo Triángulo
triangulo1.cargar_lados() # 2.- Comienzo a "jugar" con los métodos
triangulo1.lado_mayor()
triangulo1.clasificar_por_lado()