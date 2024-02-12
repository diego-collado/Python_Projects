''
4.- En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que:
    - lea los sueldos que cobra cada empleado
    - informe cuántos empleados cobran entre $100 y $300
    - informe cuántos cobran más de $300.
    - Además el programa deberá informar el importe que gasta la empresa en sueldos al personal
'''
#DECLARACIÓN DE VARIABLES
lista_sueldos = []

#FUNCTIONS
def iniciar_empresa():
    num_empleados = int(input("Introduce el número de empleados de MIEMPRESA S.A. :"))
    lista_sueldos = []
    for i in range(num_empleados):
        registrar_sueldos()
    calcular()
    #no hay return, no hacemos nada más que inicializar toda la empresa
def registrar_sueldos():
    sueldo = float(input("Introduce el sueldo: "))
    if (sueldo < 100) or (sueldo > 500):
        print("Error, debes estar dentro de los parámetros del programa")
        registrar_sueldos()
    else:
        lista_sueldos.append(sueldo)

def calcular():

    #variables locales a la función, es decir, se utilizan únicamente dentro de la misma
    contadorMas = 0
    contadorMenos = 0
    total = 0

    for i in lista_sueldos:
        if lista_sueldos[i] >= 300:
            contadorMas += 1
            total += lista_sueldos[i]
        else:
            contadorMenos += 1
            total += lista_sueldos[i]

    print("Sueldos superiores a $300: ", contadorMas)
    print("Sueldos inferiores a $300: ", contadorMenos)
    print("Total de gasto en personal: ", total)

#MAIN
iniciar_empresa()

#Al llamar a la primera función, se ejecuta absolutamente todo

