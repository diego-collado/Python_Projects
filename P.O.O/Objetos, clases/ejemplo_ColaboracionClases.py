'''
Plantear un programa que permita jugar a los dados.
Las reglas de juego son:
    · se tiran tres dados
    · si los tres salen con el mismo valor mostrar un mensaje que "gano"
    · sino "perdió".

Pintando "la mona":
Dado -------------------------
    atributos
        valor
    métodos
        tirar
        imprimir
        retornar_valor

JuegoDeDados -------------------------
    atributos
        3 Dado (3 objetos de la clase Dado)
    métodos
        __init__
        jugar
'''
import random #importación de random para poder tirar los dados y que salgan números al azar

class Dado:
    def tirar(self):
        self.valor = random.randint(1,6)

    def imprimir(self):
        print(f"Valor del dado: {self.valor}")

    def retornarValor(self):
        return self.valor

class JuegoDeDados:
    #comenzamos a colaborar, es decir, se "anidan" los objetos
    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()

        if (self.dado1.retornarValor() == self.dado2.retornarValor()) and (self.dado1.retornarValor() == self.dado3.retornarValor()):
            print("Has Ganadoooooo!!")
        else:
            print("Perdisteeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!")
#MAIN
juegoDados = JuegoDeDados()
juegoDados.jugar()