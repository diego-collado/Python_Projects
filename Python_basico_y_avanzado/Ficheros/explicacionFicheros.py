'''
FICHEROS (FILE):
    . información diversa contenida en un elemento común, es decir, en un archivo físico como tal
    · acción que puedo hacer sobre ellos:
        - LEER (acceder al contenido del archivo en cuestión)
        - ESCRIBIR (incluir información en el archivo o generar un archivo si no existe)
        - BORRAR/CERRAR/MODIFICAR (sub-acciones a la hora de trabajar con ellos)

Pasos a seguir en cualquiera de las acciones:

1º. abrir archivo: fichero = open("fichero.loquesea","modo_apertura")
2º. el modo de apertura debemos elegirlo SIEMPRE antes de abrir nuestro archivo:
    · W: Borra el fichero si ya existiese y crea uno nuevo con el nombre indicado
    · A: Añadirá el contenido al final del fichero si ya existiese (A = APPEND)
        fichero = open("datos_ejemplo.txt",'a')#abre nuevo fichero y añade contenido al final
    · X: Si ya existe el fichero se devuelve un error
3º. escribimos en el archivo:
    · fichero.write("Contenido a escribir")
    · fichero.writelines(lista) --> necesitamos una lista
4º. cerrar el fichero: fichero.close()

Tipos de archivo a manejar:
    · HTML      · CSS       · XML
    · TXT       · CSV       · JSON
    · PY --> Script puro y duro de Python
'''
'''#ESCRIBIENDO ARCHIVOS
fichero = open("datos_ejemplo.txt",'w')#abre nuevo fichero

fichero.write("El contenido es nuevo, así que ahí queda eso, ¡¡CALMANAR!!")
fichero.close()

#ESCRIBIENDO "A LO BANZAI"
fichero = open("datos_guardados.txt", 'w')
lista = ["Manzana", "Pera", "Plátano"]

for linea in lista:
    fichero.write(linea + "\n")
fichero.close()
#Error al grabar el contenido, no se guarda bien
fichero = open("datos_guardados2.txt", 'w')
lista = ["Manzana", "Pera", "Plátano"]

fichero.writelines(lista)
fichero.close()

fichero = open("datos_guardados3.txt", 'w')
lista = ["Manzana\n", "Pera\n", "Plátano\n"]

fichero.writelines(lista)
fichero.close()
#AHORRANDO CÓDIGO: ABRIR Y CERRAR EN EL MISMO PAQUETE
lista = ["Manzana\n", "Pera\n", "Plátano\n"]

with open("sorpresita.txt",'w') as fichero:
    fichero.writelines(lista)

#UN POCO MÁS DE CAÑA: APERTURA, ESCRITURA Y LECTURA
# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    # Borra el contenido del fichero para dejarlo vacío
    f = open('fichero_comunicacion.txt', 'w')
    f.close()
    return mensaje

escribe_fichero("Esto es un mensaje")
print(lee_fichero())'''

'''
A la hora de abrir, podemos tener los siguientes modos de apertura:
    · r: Por defecto, para leer el fichero
    · w: Para escribir en el fichero
    · x: Para la creación, fallando si ya existe
    · a: Para añadir contenido a un fichero existente
    · b: Para abrir en modo binario

fichero = open('ejemplo.txt')
try:
    # Usar el fichero
    pass
finally:
    # Esta sección es siempre ejecutada
    fichero.close()'''

#lectura línea a línea hasta el final:
with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()

with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')
#Simplicando lo anterior ---------------------------------
with open('ejemplo.txt', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')