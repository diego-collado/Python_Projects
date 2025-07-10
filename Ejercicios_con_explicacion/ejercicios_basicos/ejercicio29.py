'''
Crea una función que nos permita contar y mostrar el número total de 
palabras de un archivo de texto.

La funcionalidad de try-except es mágica... Nos permite controlar todo...
EL control es necesario, sobre todo, en los errores

método split():
    busca que esté un espacio o símbolo entre los datos que me interesan
grocery = 'Milk#Chicken#Bread#Butter'
print(grocery.split('#', 1))  # Output: ['Milk', 'Chicken#Bread#Butter']
print(grocery.split('#', 2))  # Output: ['Milk', 'Chicken', 'Bread#Butter']
print(grocery.split('#', 5))  # Output: ['Milk', 'Chicken', 'Bread', 'Butter']
print(grocery.split('#', 0))  # Output: ['Milk#Chicken#Bread#Butter']

RUTAS:
    - absoluta: se pone dónde está el archivo, desde la unidad hasta la carpeta 
    y el nombre del archivo. Se tiene que implementar: c:\\.... siempre con doble \\
    - relativa: simplemente cargamos el archivo. Se hace .\\
    

    proyecto
        |--main.py
        |
        |---DATOS
                |--ejercicioX.txt

'''
# FUNCTIONS -----------------------------------
def contar_palabras(archivo):
    try:
        with open(archivo,'r',encoding='utf-8') as a:
            contenido = a.read() # leemos el archivo
            palabras = contenido.split() # la palabra va de espacio a espacio
            cantidad = len(palabras) # len() me permite saber la longitud

            print(f"El archivo cargado contiene {cantidad} palabras")
    except FileNotFoundError:
        print(f"Error, no existe el archivo {archivo}.")
    except Exception as e:
        print(f"Se ha producido un error en el {archivo}, el cual es:\n {e}")
    
# MAIN -----------------------------------
#contar_palabras('C:\\Users\\A4-Profesor\\Downloads\\Proyectos_Python\\Básicos\\ejercicio29.txt')
contar_palabras('.\\Básicos\\ejercicio29.txt')