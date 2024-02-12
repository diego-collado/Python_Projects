import os
import sys
import platform
import threading, subprocess # utilización hilos en Python
'''
Hilos: se crean instanciando la clase Thread. 
    - Se inicia su ejecución con el método start. 
    - Para esperar por otro hilo se invoca a su método join. 
    - Se pueden sincronizar hilos mediante exclusión mutua, semáforos o barreras 
    (clases Lock, Semaphore y Barrier)
    - La clase Timer permite establecer temporizadores para acciones a ejecutar en 
    un tiempo determinado
'''
from datetime import datetime

IPXHILOS = 4 # Cantidad de IPs a comprobar por hilo
ip = input("Introduce la IP: ")
ipDividida = ip.split('.')

try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    comienzo = int(input("Introduce el número de comienzo de la subred: "))
    fin = int(input("Introduce el número en el que deseas acabar el escaneo: "))
except:
    print("[!] Error")
    sys.exit(1)

if (platform.system() == "Windows"):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

'''Creación de una clase Hilo que extiende de threading
Thread recibe como parámetros inicio y fin de las direcciones con las que tendrá 
que trabajar cada hilo,
La función run es necesaria y se utiliza para realizar el trabajo
'''
class Hilo(threading.Thread):
    def __init__(self, inicio, fin):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fin = fin

    def run(self):
        for subred in range(self.inicio, self.fin):
            direccion = red + str(subred)
            response = os.popen(ping + " " + direccion)
            for line in response.readlines():
                if ("ttl" in line.lower()):
                    print(direccion, "está activo")
                    break


tiempoInicio = datetime.now()
print("[*] El escaneo se está realizando desde", red + str(comienzo), "hasta", red + str(fin))
NumeroIPs = fin - comienzo
numeroHilos = int((NumeroIPs / IPXHILOS))
hilos = [] # lista donde almacenar cada hilo, para después hacer que el hilo principal
# espere a que el resto termine el trabajo

try:
    for i in range(numeroHilos):
        finAux = comienzo + IPXHILOS
        if (finAux > fin):
            finAux = fin
        hilo = Hilo(comienzo, finAux)
        hilo.start()
        hilos.append(hilo)
        comienzo = finAux
except Exception as e:
    print("[!] Error creando hilos:", e)
    sys.exit(2)

for hilo in hilos:
    hilo.join()

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print("[*] El escaneo ha durado %s" % tiempo)