'''
Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntuación, y los métodos __init__, imprimir y
pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el
fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
'''
#CLASS
class Jugador:
    tiempo = 30#atributo de clase, la tenemos como variable de scope global

    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def imprimir(self):
        #para acceder a una variable o atributo de clase: nombreClase.variable
        print(f"{self.nombre} tiene una puntuación de {self.puntuacion} "
              f"y un fin de juego en {Jugador.tiempo} minutos.")

    def pasaminutos(self):
        Jugador.tiempo -= 1

#MAIN
jugador1 = Jugador("Diego", 100)
jugador2 = Jugador("Marta", 405)

while Jugador.tiempo > 0:
    jugador1.imprimir()
    jugador2.imprimir()

    jugador1.pasaminutos()