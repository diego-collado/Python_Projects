'''
ARCHIVO OPERACIONES
Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo.
Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la
clase Cuenta.
Una caja de ahorros y un plazo fijo tienen un nombre de titular y un montante.
Un plazo fijo añade un plazo de imposición en días y una tasa de interés.
Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
'''
#CLASS
# Padre
class Cuenta:
    def __init__(self, titular, montante):
        self.titular = titular
        self.montante = montante

    def imprimir(self):
        print(f"Titular: {self.titular}, con un montante de {self.montante} €")
        #se puede utilizar el método especial __str__

# Hijas
class CajaAhorro(Cuenta):
    def __init__(self, titular, montante):
        super().__init__(titular, montante)
    #Se podría anular porque utilizamos el constructor del padre realmente... Por precaución, mejor ponerlas
    
    def imprimir(self):
        print("- _ - Cuenta de Caja de Ahorros - _ -")
        super().imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, montante, plazo, interes):
        super().__init__(titular, montante)
        self.plazo = plazo
        self.interes = interes

    def imprimir(self):
        print("- _ - Cuenta de Plazo Fijo - _ -")
        super().imprimir()
        print(f"Plazo en día: {self.plazo} -- Interés: {self.interes}")
        self.gananciaInteres()#llamada a otro método de esta clase hija

    def gananciaInteres(self):
        print(f"Importe del interés: {self.montante * self.interes / 100} €")