'''
P.O.O. : PROGRAMACIÓN ORIENTADA A OBJETOS

- Tipos de dato (primitivos) que se comportan como objetos en Python:

    - listas:           lista1=[10, 5, 3]
    - strings:          "Estoy dormido porque tengo sueño"
    - tuplas:           fecha=(25, "Diciembre", 2016)
    - diccionarios:     productos = {"manzanas":39, "peras":32, "lechuga":17}

        diccionario = {clave: valor, clave: valor, ...clave_N: valor_N}

    Qué podemos hacer con los diccionarios:

Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor
el precio del mismo. Desarrollar además las funciones de:
    1) Imprimir en forma completa el diccionario
    2) Imprimir solo los artículos con precio superior a 100.


#FUNCTIONS

def cargar():
    for i in range(5):
        nombre = input("Introduce nombre de producto: ")
        precio = float(input("Introduce precio del producto: "))

        #nombre_diccionario[clave]=valor
        productos[nombre] = precio

def imprimir():
    print("Listado de productos\n")
    #dame las claves (todas) que estén en el diccionario
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimirMayor100():
    print("Listado de productos precio superior a 100€\n")
    # dame las claves (todas) que estén en el diccionario
    for nombre in productos:
        if productos[nombre] > 100:
            print(nombre)

#MAIN
productos = {}#inicialización del diccionario, scope global
cargar()
imprimir()
imprimirMayor100()'''

'''
CLASE es un conjunto de objetos del mismo "tipo", cada uno de los cuales, puede tener los mismos atributos o,
incluso, añadir más atributos nuevos. Lo que "pueden hacer o no" se denomina MÉTODOS.

class Nombreclase:
    atributos de clase
    
    def __init__():
        atributos de instancia

class Perro:
    pass

#MAIN
mi_perro = Perro()
tu_perro = Perro()
'''
'''
class Coche:
    #CREACIÓN/INSTANCIACIÓN DE OBJETOS DE TIPO "X"
    # Atributo de clase: son atributos que pertenecen a esa clase, comunes a todos los objetos
    ruedas = 4

    # Atributos de instancia: atributos que pertenecen a la instancia del objeto/clase, es decir,
    # particulares de cada instancia (cada uno de los coches que se hayan creado)

    def __init__(self, color, aceleracion):#método constructor
        self.color = color #self: hace referencia al objeto que se está manipulado
        self.aceleracion = aceleracion
        self.velocidad = 0#inicialización
        
        método especial __init__: constructor de la clase y se invoca cada vez que se instancia un nuevo objeto
        

    #MÉTODOS QUE PUEDE REALIZAR LA CLASE
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

#MAIN
coche1 = Coche ('rojo', 20)#Es la orden de fabricación
print(coche1.color)#resultado: rojo
print(coche1.ruedas)#resultado: 4
print(coche1.velocidad)'''


'''
class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)


usuario001 = Usuario('Enrique', 'Barros Fernández')
usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto'
usuario002.imprime_datos()
'''

'''
Método __init__: inicialización de los atributos del objeto:
    1.- El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
    2.- El método __init__ se llama automáticamente. 
    Es imposible de olvidarse de llamarlo ya que se llamará automáticamente.

Características:
    - no puede retornar dato
    - puede recibir parámetros que se utilizan normalmente para inicializar atributo
    - es un método OPCIONAL, de todos modos es muy común declararlo

Sintaxis:
def __init__([parámetros]):
    código en cuestión
    
EJEMPLO CON CLASE OPERACIONES VARIANTE 1

#CLASS
class Operaciones:
    def __init__(self):#CONSTRUCTOR DEL OBJETO DE LA CLASE QUE QUEREMOS DEFINIR
        self.valor1 = int(input("Introduce valor 1: "))#ATRIBUTO --> inicialización o carga
        self.valor2 = int(input("Introduce valor 2: "))#ATRIBUTO --> inicialización o carga

    def sumar(self):
        suma = self.valor1 + self.valor2
        print(f"La suma de los valores {self.valor1} y {self.valor2} es de {suma}")
    def restar(self):
        resta = self.valor1 - self.valor2
        print(f"La resta de los valores {self.valor1} y {self.valor2} es de {resta}")
    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print(f"La multiplicación de los valores {self.valor1} y {self.valor2} es de {multi}")
    def dividir(self):
        divi = self.valor1 / self.valor2
        print(f"La división de los valores {self.valor1} y {self.valor2} es de {divi}")

#MAIN
operacion1 = Operaciones()

operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.dividir()'''

'''EJEMPLO CON CLASE OPERACIONES VARIANTE 2
#CLASS
class Operaciones:
    def __init__(self):#CONSTRUCTOR DEL OBJETO DE LA CLASE QUE QUEREMOS DEFINIR
        self.valor1 = int(input("Introduce valor 1: "))#ATRIBUTO --> inicialización o carga
        self.valor2 = int(input("Introduce valor 2: "))#ATRIBUTO --> inicialización o carga

        #Métodos dentro del método Constructor
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        suma = self.valor1 + self.valor2
        print(f"La suma de los valores {self.valor1} y {self.valor2} es de {suma}")
    def restar(self):
        resta = self.valor1 - self.valor2
        print(f"La resta de los valores {self.valor1} y {self.valor2} es de {resta}")
    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print(f"La multiplicación de los valores {self.valor1} y {self.valor2} es de {multi}")
    def dividir(self):
        divi = self.valor1 / self.valor2
        print(f"La división de los valores {self.valor1} y {self.valor2} es de {divi}")

#MAIN
operacion1 = Operaciones()'''


'''
Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
Mostrar un menú de opciones que permita:
    1- Cargar alumnos.
    2- Listar alumnos.
    3- Mostrar alumnos con notas mayores o iguales a 7.
    4- Finalizar programa.
'''
#CLASS
class Alumnos:
    #Instanciamos el objeto, es decir, creamos todo y preparamos todo para ese objeto
    def __init__(self):
        self.nombres = []
        self.notas = []

        #llamamos directamente a un "gestor" de métodos, porque en este caso, disponemos de menú
        self.menu()
    #Creamos el menú con su propia descripción y llamadas a métodos de la clase
    def menu(self):
        opcion = 0

        while opcion != 4:
            print("1.- Cargar alumnos\n")
            print("2.- Listado de todos los alumnos\n")
            print("3.- Listado de alumnos con notas superiores a 7\n")
            print("4.- Salir del programa\n")

            opcion = int(input("Introduce tu opción: "))

            if (opcion == 1):
                self.cargar()
            elif (opcion == 2):
                self.listar()
            elif (opcion == 3):
                self.notas_altas()
            elif (opcion == 4):
                print("¡¡Hasta luego, MariCarmen!!")
                break
    def cargar(self):
        for i in range(5):
            nombre = input("Introduce el nombre del alumno: ")
            nota = int(input("Introduce la nota media del alumno: "))

            #carga de los datos con la sintaxis: objeto.lista.append(valor)
            self.nombres.append(nombre)
            self.notas.append(nota)
    def listar(self):
        print("Listado completo de alumnado de HaCKiNG iNSTiTuTe\n\n")#\n salto de línea, para una línea nueva
        for i in range(5):
            print(self.nombres[i], self.notas[i])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    def notas_altas(self):
        print("Alumnos con notas superiores a 7: \n")
        for i in range(5):
            if (self.notas[i] > 7):
                print(self.nombres[i], self.notas[i])
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

#MAIN
alumnos = Alumnos()
#alumnos.menu()