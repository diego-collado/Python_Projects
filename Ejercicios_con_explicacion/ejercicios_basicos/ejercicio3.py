'''Pidiendo por teclado e imprimiendo en pantalla'''

'''# 1.- Petición por teclado de los datos - input("el texto que quieras")
nombre = input("¿Cómo te llamas?  ")
#parseamos a entero
edad = int(input("¿Cuántos años tienes?  "))
# obliga a introducir un número entero
residencia = input("¿Dónde vives?  ")

# 2.- Impresión en pantalla
print(f"Hola, {nombre}... ¿Qué tal estás? Yo bien. \n \
      Parece que también vives en {residencia}, como nosotros. \n \
      ¿Tienes de verdad {edad} años? Pues no lo aparentas")'''

'''
Otra forma menos sencilla (bajo mi punto de vista)
print("Hola, ",nombre + "... ¿Qué tal estás? Yo bien. \n Parece que \
también vives en ", residencia + ", como nosotros. ¿Tienes de verdad ", edad + "años? Pues no lo aparentas")
# concatenar texto: texto1 + texto2'''

'''
CASTING: convertir un tipo de dato en otro (cast). 
Existen 2 tipos de casting:
    · CONVERSIÓN IMPLÍCITA:
        a = 1
        b = "3.5"

        a = a + b
        print(a)
        print(type(a))
        
        --> Resultado: 4.5 y además el tipo float
        --> si es un string, no se puede sumar así como así...

    · CONVERSIÓN EXPLÍCITA:

        variable = tipo(variable)
        a = str(a)
        b = int(b)
        c = float(c)

        a = b = c = 10

        Imprimir a + b + c
'''
a = b = c = 10
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

a = b = 10
c = 5.99
print(a)
print(b)
print(int(c))
print(type(a))
print(type(b))
print(type(c))

a = b = c = 10
a = str(a)
b = int(b)
c = float(c)

print("Resultado: ", str(b+c)+a)