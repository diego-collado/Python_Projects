'''
ARCHIVO OBJETOS/CLASES ----------------------------------------------------
Plantear una clase Persona que contenga dos atributos: nombre y edad.
Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal (main) del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo
y muestre si debe pagar impuestos (sueldo superior a 3.000€)

También en el bloque principal del programa crear un objeto de la clase Empleado.
'''
#CLASS
#CLASE PADRE
class Persona:
    def __init__(self):
        self.nombre = input("Introduce nombre: ")
        self.edad = int(input("Introduce edad: "))

    def imprimir(self):
        print(f"{self.nombre} tiene {self.edad} años.")

#CLASE HIJA
class Empleado(Persona):
    def __init__(self):
        super().__init__()#cargas los atributos de papá
        self.sueldo = float(input("Introduce el sueldo de este empleado: "))

    def imprimir(self):
        super().imprimir()#utiliza el método de papá, de modo que no repito lo codificado
        print(f"Cobra {self.sueldo} €, ¡¡qué pajar@!! ")

    def pagaonoimpuestos(self):
        if self.sueldo > 3000:
            print(f"Nuestro empleado {self.nombre}, debería pagar impuestos, como todos")
        else:
            print("Corazón... Cobras tan poco que no te dejamos pagar impuestos (caso IRREAL)")