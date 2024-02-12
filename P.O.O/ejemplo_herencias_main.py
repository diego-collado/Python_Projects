'''
ARCHIVO PRINCIPAL ----------------------------------------------------
Plantear una clase Persona que contenga dos atributos: nombre y edad.
Definir como responsabilidades la carga por teclado y su impresión.
En el bloque principal (main) del programa definir un objeto de la clase persona y llamar a sus métodos.

Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo
y muestre si debe pagar impuestos (sueldo superior a 3.000€)

También en el bloque principal del programa crear un objeto de la clase Empleado.
'''
#IMPORTS
import ejemplo_herencias_objetos as herencia

#MAIN
persona1 = herencia.Persona()
persona1.imprimir()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
empleado1 = herencia.Empleado()
empleado1.imprimir()
empleado1.pagaonoimpuestos()