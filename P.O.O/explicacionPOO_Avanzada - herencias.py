'''
HERENCIA: La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una
clase padre, compartiendo sus métodos y atributos.
Además, una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.

VENTAJAS:
    · heredamos métodos y atributos del padre, las particularidades también se heredan
    · Principio D.R.Y. --> Don't Repeat Yourself --> ¡¡No codifiques de nuevo algo hecho, calamar!!
    · No repetimos cosas hechas, no hay inconsistencias (algo que no funciona bien), no hay duplicación
    · podemos (o no, según nos haga falta) crear más métodos y atributos según la clase



'''

#Clase Padre: de la que dependemos "tod@s"
class Animal:
    #Método constructor genérico para todas las subclases
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #Método X común a todas las subclases
    def hablar(self):
        pass

    def moverse(self):
        pass

    #Método genérico con la misma implementación para todos
    def describir(self):
        print("Soy un Animal de tipo ", type(self).__name__)#type(self).__name__ nos dice qué subclase es

#Clases "hijas"
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
class Gato(Animal):
    def hablar(self):
        print("Miau!")
    def moverse(self):
        print("Caminando con 4 patas")
class Raton(Animal):
    def hablar(self):
        print("riski, riski!")
    def moverse(self):
        print("Caminando con 4 o 2 patas")

mi_perro = Perro("mamifero", 10)
mi_perro.describir()
mi_gato = Gato("mamifero",26)

'''REDEFINIENDO LA CLASE HIJA COMPLETA, OPCIÓN MÁS PRO Y MEJOR Y MÁS EFICIENTE Y MEJOR PARA TODO'''
#OPCIÓN 1: LA MÁS NORMAL
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        self.especie = especie
        self.edad = edad
        self.dueño = dueño#atributo extra que quiero añadir al constructor

    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")
#OPCIÓN 2: ENTRANDO EN MATRIX
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)#definimos que hay que llamar al padre para este atributo
        #carga los atributos del "paaapaaa"
        self.dueño = dueño#atributo extra que quiero añadir al constructor

    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

mi_perro = Perro('mamífero', 7, 'Luis')
mi_perro.especie
mi_perro.edad
mi_perro.dueño