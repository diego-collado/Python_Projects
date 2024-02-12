'''
ESTRUCTURAS DE CONTROL EN PYTHON

    - Condicional if:
        Si (condición a evaluar) entonces:
            bloque de sentencias a ejecutar
        Finsi

        True: se ejecuta el bloque de sentencias
        False: se sale del if, no ejecuta el bloque de sentencias

        Operadores relacionales:
        <   <=  == (igual)
        >   >=  != (distinto)


    - Bucle for
    - Range
    - Bucle while
    - Switch
    - Break/Continue
'''
#Ejemplo de uso de IF
#asignamos valores e inicializamos las variables
a = 4 #= es operador de asignación
b = 7
#creamos el condicional
if (b != 0):
    print(a/b)#bloque de sentencias. print(nombreVariable) imprime el valor que tenga contenido la variable

a += 5#a += 5 es equivalente a a = a + 5
print(a)
print(b)
c = 4
if c > 6 and c < 25:
    print(a)
else:#cuando no se cumple la condición principal evaluada... Siempre debemos considerar esta salida
    print("Lo siento, no está el valor correctamente insertado")

x = 5

if x == 5:
    print("El número es 5")
else:
    print("El número no es 5")

#Uso ELIF
y = 6
if y == 5:
    print("El número es 5")
elif y == 6:
    print("El número es 6")
elif y == 7:
    print("El número es 7")
else:
    print("Esto no es un número")


if y == 5:print("El número es 5")
elif y == 6: print("El número es 6") #elif es else if, sino, si (condición) entonces...
elif y == 7: print("El número es 7")
else: print("Esto no es un número")