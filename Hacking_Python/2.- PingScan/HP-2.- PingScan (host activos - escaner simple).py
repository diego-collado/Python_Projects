'''
    - os: necesaria para realizar el ping a través del sistema operativo
    - sys: se utiliza para terminar el programa ante un error en la introducción de datos
    - platform: permite saber el sistema operativo donde corremos el programa,
    - datetime: usado para saber el tiempo que tarda en realizar el escaneo
'''
import os
import sys
import platform
from datetime import datetime

ip = input("Introduce IP: ")
ipDividida = ip.split('.')

try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    comienzo = int(input("Introduce el número de comienzo de la subred: "))
    fin = int(input("Introduce el número en el que deseas acabar el escaneo: "))
except:
    print("[!] Error")
    sys.exit(1)

# comprobación del sistema operativo
if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

tiempoInicio = datetime.now() # hora de comienzo del scan

print("[*] El escaneo se está realizando desde", red + str(comienzo), "hasta", red + str(fin))

for subred in range(comienzo, fin + 1):
    direccion = red + str(subred)
    response = os.popen(ping + " " + direccion)
    for line in response.readlines():
        if ("ttl" in line.lower()):
            print(direccion, "está activo")
            break

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)