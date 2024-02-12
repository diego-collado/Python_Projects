'''
7.- Crear dos listas paralelas.
En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
'''

sueldos = []
nombres = []

posicion = 0


num_empleados = int(input("Introduce número de empleados: "))
for i in range(num_empleados):
    #Bloque petición de datos
    nombre = str(input("Introduce nombre de empleado: "))
    sueldo = float(input("Introduce sueldo: "))

    #Bloque inserción en lista
    nombres.append(nombre)
    sueldos.append(sueldo)
    #print("DATOS INTRODUCIDOS: \nEmpleado {}: {} --- {}".format(i, nombre, sueldo))

#Bloque de búsqueda y borrado
while (posicion < len(sueldos)):
    if sueldos[posicion] > 1000:
        sueldos.pop(posicion)
        nombres.pop(posicion)
    else:
        posicion += 1

print("Lista de empleados que cobran menos de 1.000€ al mes ------------------ ")
for i in range(len(sueldos)):
    print("Empleado: {} - Sueldo: {}".format(nombres[i], sueldos[i]))