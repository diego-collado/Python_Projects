'''
3.- Solicitar por teclado el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario
mostrar un mensaje de error.
'''

clave = ""

while (len(clave) <= 10) or (len(clave) >= 20):
    clave = str(input("Introduce la clave nueva (entre 10 y 20 caracteres): "))
    if (len(clave) >= 10) and (len(clave) <= 20):
        print("Clave correcta, guardando...")
        #break --> me asegura que se sale del bucle
    else:
        print("Clave incorrecta, introduzca una nueva")