'''
Banner Grabbing, con introducción de la IP/dominio por parte del usuario
'''

#IMPORTS
import socket
import os, sys
import threading

# Petición de datos
ip = str(input("Introduzca dirección IP, separando octetos con . :"))

# Captura de banner de server
def get_banner(ip, puerto):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# conexión como tal
        sock.connect((ip, puerto))
        banner = sock.recv(1024)
        return banner
    except:
        return # se hace un return vacío porque no hay datos que analizar

# Comprobar que el banner es o no vulnerable
def vulncheck(banner, archivo):
    a = open(archivo, 'r')

    for linea in a.readlines():
        if linea.strip("\n").encode() in banner: # si encuentro un salto de línea (el archivo es texto codificado)
            print("Vulnerabilidad: {}".format(banner.strip(b"\n\r")))

# comprobamos errores: si hay archivo de vulnerabilidades, etc
def main():
    # ¿Qué errores puedo tener con los archivos en el sistema?
    if (len(sys.argv) == 2):
        archivo = sys.argv[1]

        if not os.path.isfile(archivo): # no hay archivo
            print("El archivo no se encuentra")

        if not os.access(archivo, os.R_OK): # existe, pero no es accesible
            print("Acceso denegado")

    else:
        print("Uso: " + str(sys.argv[0] + " vulnbanners.txt"))

    # iteracción para que revise X puertos
    for puerto in range(1,80):
        banner = get_banner(ip, puerto)

        if (banner):
            print("{}/{} : {}".format(ip, puerto, banner))
            vulncheck(banner, archivo)

    t = threading.Thread(target=get_banner, args=(ip, puerto))
    t.start()



#MAIN
main()