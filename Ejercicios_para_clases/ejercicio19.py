'''
Almacenar en una lista 5 empleados, cada elemento de la lista es una sublista con el nombre del empleado
junto a sus últimos tres sueldos (estos tres valores en una tupla).
El programa debe tener las siguientes funciones:

       1)Carga de los nombres de empleados y sus últimos tres sueldos.
       2)Imprimir el monto total cobrado por cada empleado.
       3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos 3 meses.

Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]
'''
#FUNCTIONS
def cargar_empleados():
    empleados = []

    for i in range(3):
        nombre = input("Introduce el nombre del empleado: ")
        sueldo1 = int(input("Introduce el sueldo del 1T: "))
        sueldo2 = int(input("Introduce el sueldo del 2T: "))
        sueldo3 = int(input("Introduce el sueldo del 3T: "))

        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])
        #empleados([nombre]([sueldo][sueldo][sueldo]))

    return empleados

def ganancia_empleado(empleados):
    print("Monto total ganado por empleado en los últimos 3 trimestres: \n")

    total = 0
    for i in range(3):
        #i es el elemento de la lista
        #[1] es el nombre
        #[...] es el sueldo en cuestión
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]
        print(f"Empleado: {empleados[i][0]} - Monto total: {total}")


def superior10k(empleados):
    print("Empleados que han superado 10K de ingreso en los últimos trimestres")

    total = 0
    for i in range(3):
        total = empleados[i][1][0] + empleados[i][1][1] + empleados[i][1][2]
        if (total > 10000):
            print(empleados[i][0], total)

#MAIN
empleados = cargar_empleados()#empleados es una variable de scope global, se conoce en todo el código
ganancia_empleado(empleados)
superior10k(empleados)