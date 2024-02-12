'''
9.- En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a lo siguiente:
    a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
    b) Realizar un listado que muestre los nombres, notas y condición del alumno.
    En la condición colocar:
        · "Muy Bueno" si la nota es mayor o igual a 8
        · "Bueno" si la nota está entre 4 y 7
        · "Insuficiente" si la nota es inferior a 4
    c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.
'''
nombres = []
notas = []

for i in range(4):
    nombre = input("Introduce el nombre: ")
    nombres.append(nombre)

    nota = int(input("Introduce la nota: "))
    notas.append(nota)

cant = 0

for x in range(4):
    print(nombres[x])
    print(notas[x])

    if notas[x] >= 8:
        print("Muy bueno")
        cant += 1
    elif (notas[x] >= 4) and (notas[x] <= 7):
        print("Bueno")
    elif notas[x] < 4:
        print("Insuficiente")
print("Cantidad de alumnos sobresalientes de la clase: {}".format(cant))



'''#DECLARATIONS
notas_examen = []
nombres_alumnos = []

#FUNCTIONS
def registrar():
    numero = int(input("Introduce el número de alumnos que vamos a registrar: "))
    for i in range(numero):
        nombre = str(input("Introduce el nombre del alumno: "))
        nota = int(input("Introduce la nota del alumno: "))

        if (nota >= 0) and (nota <= 10):
            nombres_alumnos.append(nombre)
            notas_examen.append(nota)
        else:
            print("Nota no válida, repitamos el proceso...")
            registrar()

def condicion():
    condiciones = ["Muy Bueno", "Bueno", "Insuficiente"]
    contador = 0
    for i in nombres_alumnos:
        for x in notas_examen:
            if (notas_examen[x] < 4):
                print("{} tiene {}".format(nombres_alumnos[i], condiciones[2]))
            elif (notas_examen[x] >= 4) and (notas_examen[x] <= 7):
                print("{} tiene {}".format(nombres_alumnos[i], condiciones[1]))
            elif (notas_examen[x] > 7):
                print("{} tiene {}".format(nombres_alumnos[i], condiciones[0]))
                contador += 1
    print("{} han sacado la nota de {}".format(contador, condiciones[0]))


#MAIN
registrar()
condicion()'''