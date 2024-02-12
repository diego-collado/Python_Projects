'''
1.- Crear un programa con la siguiente información:

    - Las edades de 5 estudiantes del turno mañana.
    - Las edades de 6 estudiantes del turno tarde.
    - Las edades de 11 estudiantes del turno noche.
    - Las edades de cada estudiante deben ingresarse por teclado.

¿Qué tenemos que hacer?
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
'''

#DECLARACIÓN/INICIALIZACIÓN DE VARIABLES ---------------------------------------------------
sumManana = 0
sumTarde = 0
sumNoche = 0

promManana = 0
promTarde = 0
promNoche = 0


#MAIN ---------------------------------------------------
''' 
for repite N veces la operación que le indiquemos, es decir, tiene comienzo y fin de bucle repetitivo
Sintaxis: for iterador in range(N_veces) --> iterador es un contador simple... va desde 0 hasta N_veces

int(....) --> PARSEO: obligamos a tener un tipo determinado de dato

Built in Functions--> FUNCIONES PRECOCINADAS
round(numero_a_redondear) --> redondea un real (float) quitando los decimales:
     < 5: redondea hacia abajo
     >=5: redondea hacia arriba
'''

#Las edades de 5 estudiantes del turno mañana
for i in range(5):
    edadM = int(input("Introduce edad (MAÑANAS): "))
    sumManana += edadM#sumamos a nuestro acumulador la edad que vamos introduciendo por teclado

#Las edades de 6 estudiantes del turno tarde
for i in range(6):
    edadT = int(input("Introduce edad (TARDE): "))
    sumTarde += edadT

#Las edades de 11 estudiantes del turno noche
for i in range(11):
    edadN = int(input("Introduce edad (NOCHES): "))
    sumNoche += edadN

#a) Obtener el promedio de las edades de cada turno (tres promedios)
'''Promedio = suma de todas las edades / número de edades introducidas'''
promManana = sumManana / 5
promTarde = sumTarde / 6
promNoche = sumNoche / 11

#b) Imprimir dichos promedios (promedio de cada turno)
print("Promedio edad turno de mañana: {} años".format(round(promManana)))
print("Promedio edad turno de tarde: {} años".format(round(promTarde)))
print("Promedio edad turno de noche: {} años".format(round(promNoche)))

#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor
'''
if (condición_a_evaluar): condicional simple --> Si ..... :
elif (condición_a_evaluar): condicional anidado --> Sino Si... :
else --> Sino...
'''
if (promManana > promTarde) and (promManana > promNoche):
    print("El promedio de edad de la mañana (con {} años), "
          "es el mayor de todos los promedios. ".format(round(promManana)))

elif (promTarde > promManana) and (promTarde > promNoche):
    print("El promedio de edad de la tarde (con {} años), "
          "es el mayor de todos los promedios. ".format(round(promTarde)))

elif (promNoche > promManana) and (promNoche > promTarde):
    print("El promedio de edad de la noche (con {} años), "
          "es el mayor de todos los promedios. ".format(round(promNoche)))
else:
    print("El promedio de edad (con {} años) es idéntico en los 3 turnos:\nP. Mañana: {}\nP. Tarde: {}"
          "\nP. Noche: {}".format(round(promManana, promManana, promTarde, promNoche)))

