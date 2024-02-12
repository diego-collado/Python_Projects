'''
Un archivo de texto llamado "materia.txt" contiene algún texto que necesita ser mostrado de manera que
cada carácter siguietnes está separado por un símbolo "#".
Escriba una definición de función para hash_display() en Python que muestre todo el contenido del
archivo "matter.txt" en el formato deseado.
Ejemplo: Si el archivo materia.txt tiene el siguiente contenido almacenado:
    EL MUNDO ES REDONDO
La función hash_display() debería mostrar el siguiente contenido:
    #E#L# #M#U#N#D#O# #E#S# #R#E#D#O#N#D#O#
'''
#FUNCTIONS
def hash_display():
    with open("matter.txt",'r') as fichero:
        contador = 0
        for linea in fichero:
            palabras = linea.split()#separación de palabras por espacio en blanco
            for palabra in palabras:
                palabra.split()
                for caracter in palabra:
                    print(caracter,end="#")
#MAIN
hash_display()