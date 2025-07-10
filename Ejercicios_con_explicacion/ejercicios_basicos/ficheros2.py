'''

'''
# 1.- Creamos y escribimos en un archivo llamado ejemplo1.txt
# Con modo W lo que hace es sobreescribir el archivo
with open('ejemplo1.txt','w') as fichero:
    fichero.write("Hola, mundo mundial\n") #escribimos una línea
    fichero.write("¿Qué tal estamos?\n") #escribimos una línea
    fichero.write("Venga, no tenemos que ser ñoños\n") #escribimos una línea

# Variante, quiero que se grabe en CASTELLANO
with open('ejemplo2.txt','w',encoding="utf-8") as fichero:
    fichero.write("Hola, mundo mundial\n") #escribimos una línea
    fichero.write("¿Qué tal estamos?\n") #escribimos una línea
    fichero.write("Venga, no tenemos que ser ñoños\n") #escribimos una línea
'''
Ñ mayúscula: ALT + 0209
ñ minúscula: ALT + 0241
'''

# 2.- Lectura de un archivo completo ejemplo2.txt
with open("ejemplo2.txt",'r', encoding='utf-8') as fichero:
    contenido = fichero.read()#leemos el contenido del archivo
    print("Contenido: \n", contenido)

# 3.- Creamos un archivo nuevo y le insertamos el contenido de una lista
with open("ejemplo3.txt",'a',encoding='utf-8') as fichero:
    # lista con elementos
    coches = ['Volvo', 'BMW', 'Ferrari', 'Lamborghini']

    #Insertamos cada elemento en un línea
    for coche in coches:
        fichero.write(coche) #inserta el elemento que corresponda y le añade un salto de línea
