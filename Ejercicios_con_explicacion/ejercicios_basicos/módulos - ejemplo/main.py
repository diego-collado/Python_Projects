# main.py -- módulos

# IMPORTS ----------------------------------
import saludos # importación del módulo completo de saludos (en este caso)
import os #https://docs.python.org/es/3.13/library/os.html
import time #https://docs.python.org/3/library/time.html

# FUNCTIONS ----------------------------------
def borrar_pantalla():
    # Windows: CLS  //  Linux/MacOS: CLEAR --> borrar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    #ejecuta CLS en el sistema si es Windows (núcleo NT), sino, ejecuta CLEAR

# MAIN ----------------------------------
borrar_pantalla() # llamada a la función borrar pantalla
time.sleep(5) # tiempo que se va a esperar la consola para ejecutar el resto de órdenes
print(saludos.saludar("Don Pepito"))
print(saludos.despedir("Don José"))