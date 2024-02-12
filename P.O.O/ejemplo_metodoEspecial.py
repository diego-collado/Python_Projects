'''
Definir una clase llamada Punto con dos atributos x e y.
Crearle el método especial __str__ para retornar un string con el formato (x,y).
Método especial __str__ --> convertir lo que sea a string

#CLASS
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.x) + ")"
#MAIN
punto1 = Punto(10, 4)
punto2 = Punto(60, 93)

print(type(punto1))
print(punto2)'''

'''
Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista 
con los nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de 
todos sus hijos.
'''
class Familia:
    def __init__(self, padre, madre, hijos = []):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        cadena = self.padre + " y " + self.madre
        for hijos in self.hijos:
            cadena = cadena + " han tenido a " + hijos
        return  cadena

#MAIN
familia1 = Familia("Diego", "Marta",["Adrián", "Izan"])

print(familia1)
