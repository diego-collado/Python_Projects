# Resumen POO - Clases

## INICIO DE LAS CLASES ##
class Persona: # CLASE BASE O CLASE PADRE
    
    # método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # métodos de la clase
    def presentarse(self):
        print(f"Hola a tod@s, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante (Persona): # CLASE DERIVADA O CLASE HIJA
    # método constructor
    def __init__(self, nombre, edad, estudios):
        super().__init__(nombre,edad) # coges estos "atributos" de la clase padre o base
        self.estudios = estudios

    # métodos de la clase
    def mostrar_info(self):
        super().presentarse()
        print(f"Mis estudios son {self.estudios}")


# MAIN ------------------------
persona1 = Persona("Diego",48) # creamos un objeto de tipo Persona
persona1.presentarse() # llamamos directamente al método de la clase

estudiante1 = Estudiante("Marta",48,"Periodismo digital y de guerra") # creamos un objeto de tipo Persona
estudiante1.mostrar_info() # llamamos directamente al método de la clase
estudiante2 = Estudiante(persona1.nombre,persona1.edad,"Ciberseguridad e IA")
estudiante2.mostrar_info()