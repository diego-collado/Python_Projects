'''
Geolocalización IP: normalmente la geolocalización IP se basa en situar el host al que accedemos
en un mapa, tipo Google Maps.
Se utilizará: https://ipinfo.io/

Desde shell: python simplegeo.py urlquequiero.es

'''
#IMPORTS
import sys
import requests
import socket
import json
# toma los datos de geoloc a partir de un "diccionario" que en programación tiene la extensión .JSON

# Introducción de datos a partir de sistema (llamada al py con la url)
if (len(sys.argv) < 2):
    print("A escanear: " + sys.argv[0] + "<url>")
    # argv[0] es el nombre del script
    sys.exit(1)# terminación del programa, algo parecido a break, pero sin error en sistema
    #https://docs.python.org/es/3.10/library/sys.html

# "Montamos el circo" para poder poner http/https
req = requests.get("https://" + sys.argv[1])# sys.argv[1] tiene el valor de la url
print("\n" + str(req.headers))

# Recibimos la ip del host pedido
gethostby_ = socket.gethostbyname(sys.argv[1])
print("\n Ip de " + sys.argv[1] + " es: " + gethostby_ + "\n")

# Geolocalizando con ipinfo.io
req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_two.text)# transformación de los datos recibido en JSON a texto

# Impresión de datos en pantalla
print(f"Localización: {resp_['loc']}")
print(f"País: {resp_['country']}")
print(f"Provincia/Región: {resp_['region']}")
print(f"Ciudad: {resp_['city']}")