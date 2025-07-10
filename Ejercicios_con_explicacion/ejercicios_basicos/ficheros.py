'''
Ficheros en Python: realmente, es el manejo físico de la información.

¿Qué podemos hacer con un fichero? LEER o ESCRIBIR

    -LEER: proceso de apertura de un fichero y lectura del mismo
    -ESCRIBIR: proceso de apertura de un fichero y escritura en el 
    mismo. También se puede crear vacío o, incluso, "machacar" con 
    la escritura, reiniciando su contenido.

Tipos de ficheros que podemos utilizar sin instalar "naita":
    · extensión TXT
    · extensión CSV (se recomienda la instalación de la biblioteca
    correspondiente, mejora la experiencia y utilización)
    · extensión JSON (igualmente, lo mismo que antes)
    · extensión PDF (lo mismo)

OBLIGATORIO:
    1.- Abrir fichero (open)
    2.- Lectura o grabación (read, write)
    3.- Cierre (close)
- - - - - - - - - - - - - - - - - - - - - - -
  **1.- Abrir fichero (open con cierre automático al acabar)**
    2.- Lectura o grabación (read, write)

Modos para abrir archivo:
    · r -> se da por defecto, modo lectura
    · w --> modo escritura
    · x --> creación el archivo, da fallo si existe
    · a --> añade contenido si existe
    · b -> modo binario

¿Cómo implementamos el modo?

    fichero = open('archivo.txt','r') --> apertura SOLO LECTURA
    
    fichero = open('archivo.txt','w') --> apertura ESCRITURA: 
    ¡¡ojo, puede destruir el contenido del archivo!!
    
    fichero = open('archivo.txt','x') --> apertura creando el archivo 
    si no existe. Si está ya creado, da un error

    fichero = open('archivo.txt','a') --> apertura para añadir contenido,
    es decir, respeta el contenido que hay y lo añade al final

    *** SE TRABAJA POCO, TIENE MUCHO PESO ***
    fichero = open('archivo.txt','b') --> apertura modo binario. Se suele
    utilizar para insertar elementos de tipo BLOB, es decir, imágenes/vídeos...
    Se suele utilizar (por ejemplo) para calcular cuánto ocupa un PNG,
    copia un JPG, manejar vídeo/audio, manejar PDF...
    La cuestión es que para todas esas "acciones raras" tenemos bibliotecas
    que nos permiten manejar esos tipos de archivo.


TIPO DE DATO BLOB (Binary Large OBject): no es un tipo de dato de Python,
pero se utiliza para, por ejemplo, trabajar con bases de datos, APIs...
'''
# 1.- Abriendo el archivo
fichero = open('archivo.txt') #cargamos el contenido del archivo que abrimos a una variable llamada fichero

# 2.- Lectura del contenido: completa
#print(fichero.read()) #leer el contenido del fichero
print(fichero.readline()) #leer 1 única línea, la 1ª

# lectura multilínea
lineas = fichero.readlines()
for linea in lineas:
    print(linea)

# 3.- Cerramos el fichero
fichero.close()

## -------------------------------------------------------------- ##
# El "Truco del Almendruco": apertura con cierre automático
with open('archivo.txt','r') as fichero:
    pass
#Abre el archivo denominado archivo.txt y a partir de ahora lo metemos
# en una variable que se llama fichero. Cuando termines, cierra el archivo

with open('archivo.txt','r') as fichero:
    for linea in fichero: # leemos cada línea del archivo.txt
        print(linea, end='')# end='' significa que no me imprima el final del línea.
