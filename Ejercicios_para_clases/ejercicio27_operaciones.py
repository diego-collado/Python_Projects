'''
ARCHIVO OPERACIONAL
Un banco tiene 3 clientes que pueden hacer depósitos y extracciones.
También el banco requiere que al final del día calcule la cantidad de dinero que hay depositado.

Cliente	----------------------------------------------------------------------------
    atributos: nombre y montante
    métodos
        __init__
        depositar
        extraer
        retornar_monto

Banco ----------------------------------------------------------------------------
    atributos: 3 Clientes (3 objetos de la clase Cliente)
    métodos:
        __init__
        operar
        depositos_totales

'''
#CLASS
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.montante = 0

    def depositar(self, montante):
        self.montante = self.montante + montante

    def extraer(self, montante):
        self.montante = self.montante - montante

    def retornarMontante(self):
        return self.montante

    def imprimir(self):
        print(f"{self.nombre} tiene depositado en el Banco la suma de {self.montante} €")

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Diego")
        self.cliente2 = Cliente("Sandra")
        self.cliente3 = Cliente("Sergio")

    def operar(self):
        self.cliente1.depositar(5000)
        self.cliente2.depositar(10000)
        self.cliente3.depositar(25000)
        self.cliente1.depositar(5000)
        self.cliente2.extraer(400)

    def depositosTotales(self):
        print("Lista de clientes y su respectivo montante:\n")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        print(f"El Banco dispone de un depósito total de "
              f"{self.cliente1.retornarMontante() + self.cliente2.retornarMontante() + self.cliente3.retornarMontante()} "
              f"€")