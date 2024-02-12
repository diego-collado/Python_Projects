'''
ARCHIVO MAIN
Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo.
Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la
clase Cuenta.
Una caja de ahorros y un plazo fijo tienen un nombre de titular y un montante.
Un plazo fijo añade un plazo de imposición en días y una tasa de interés.
Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.
'''
#IMPORTS
import ejercicio26_operaciones as op

cajaAhorro_Toledo = op.CajaAhorro("Diego", 59000)
cajaAhorro_Toledo.imprimir()

plazoFijo_Toledo = op.PlazoFijo("Diego", 100000, 30, 0.75)
plazoFijo_Toledo.imprimir()