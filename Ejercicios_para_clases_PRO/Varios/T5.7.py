'''
Escribe un programa en Python para generar 26 archivos de texto llamados A.txt, B.txt... Y así sucesivamente
hasta la Z.txt
'''
#IMPORTS
import string, os

#MAIN
if not os.path.exists("Abecedario"):#Comprobación para creación de carpeta que contenga los archivos
    os.mkdir("Abecedario")#Creación de carpeta contenedora
    os.chdir("Abecedario")#Cambio de directorio de escritura para los futuros archivos

for letra in string.ascii_uppercase:
    with open(letra + '.txt', 'w') as fichero:
        fichero.writelines(letra)