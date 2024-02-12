'''
Confeccionar una clase que permita carga el nombre y la edad de una persona.
Mostrar los datos cargados.
Imprimir un mensaje si es mayor de edad (edad>=18)
-------------------------------------------------------------------------------
Sintaxis para generar una clase:
class nommbreClase:
    declaración_atributo --> las características de cada objeto de esta clase
    declaración_constructor --> inicializar el objeto de la clase, lo que llamamos instanciar
    declaración_método/s --> las acciones que pueden hacer los objetos (funciones)
'''
#CLASS
class Persona:
    #Atributos de instancia ----------------------------------------
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Métodos de la clase ----------------------------------------
    def imprimir(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} años")

    def mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad, ya que tiene {self.edad} años.")
        else:
            print(f"{self.nombre} es menor de edad, ya que tiene {self.edad} años.")

#MAIN
persona1 = Persona()#Así se instancia una clase, es decir, la creo y la tengo disponible
persona1.inicializar("Diego", 46)#Crear una persona con X características
persona1.imprimir()
persona1.mayor_edad()
persona2 = Persona()#Así se instancia una clase, es decir, la creo y la tengo disponible
persona2.inicializar("Adrián", 8)#Crear una persona con X características
persona2.imprimir()
persona2.mayor_edad()