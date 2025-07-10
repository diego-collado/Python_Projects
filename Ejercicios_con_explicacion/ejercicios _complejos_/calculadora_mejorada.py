'''
Ejercicio calculadora mejorada: Crearemos una calculadora que va a permitirnos:
    - sumar     - dividir
    - restar    - multiplicar

** Se contempla la división entre 0 con error **
** Se contempla la repetición del menú si la opción no es correcta **

EXPLICACIÓN PARA QUE TE SIRVA DE AYUDA...
while (condición):
    haz_lo_que_te_de_la_gana
'''

while True:
    # Impresión del menú en pantalla -----------------------------
    print("- - - - - - - - -  MEGACALCULADORA - - - - - - - - -\n\n\n")
    print("Bienvenid@s a nuestra aplicación... Elige la opción\n")

    print("1.- SUMAR")
    print("2.- RESTAR")
    print("3.- MULTIPLICAR")
    print("4.- DIVIDIR")
    print("5.- SALIR")

    try:
        opcion = int(input("Elige la opción que necesitas (1-5):  "))

        if (opcion == 5):
            print("Bye, byeeeeee!!!")
            break # sale del programa, es decir, lo rompe

        if (opcion < 1 or opcion > 5):
        # la opción no puede ser un número menor que 1 o mayor que 5
            print("Lo más lógico es que la opción esté entre 1 y 5")
            continue #continua en el programa si te equivocas

        #Pedimos los número por teclado
        numero1 = int(input("Introduce un número: "))
        numero2 = int(input("Introduce otro número: "))

        # Ahora, al atún... Lógica del negocio ----------------------
        if (opcion == 1):
            print("La suma es: ", numero1 + numero2)
        elif (opcion == 2):
            print("La resta es: ", numero1 - numero2)
        elif (opcion == 3):
            print("La multiplicación es: ", numero1 * numero2)
        elif (opcion == 4):
            if(numero2 == 0):
                print("Error, no podemos con esto...")
            else:
                print("La división es: ", numero1 / numero2)

    except ValueError: #ValueError es un error de valor, algo mal hecho...
        print("Entrada no válida, introduce un número, melón...")