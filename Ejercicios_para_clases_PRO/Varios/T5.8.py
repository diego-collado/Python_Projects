'''
Escribe un programa en Python para añadir texto a un archivo y mostrar el texto en python.txt
'''
def readFiles(archivo):
    with open(archivo, 'a') as archivoNuevo:
        #Se abre el fichero en modo escritura para añadir el contenido nuevo
        archivoNuevo.write("\nPython es el mejor lenguaje de programación del mundo\n")
        archivoNuevo.write("Python se utiliza para muchísimas cosas\n")
        archivoNuevo.write("Python es muy fácil de aprender")

    with open(archivo, 'r') as archivoMostrado:
        contenidoArchivo = archivoMostrado.read()
        print(f"Contenido del archivo:\n {contenidoArchivo}")

readFiles("python.txt")