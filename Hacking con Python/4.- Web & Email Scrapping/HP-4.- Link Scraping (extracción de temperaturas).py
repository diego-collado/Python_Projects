#IMPORTS
from bs4 import BeautifulSoup
import requests
import time
import os

# Creamos el Bucle infinito para chequeo de temperaturas
while True:
    # Captura de la url
    url = "http://www.timeanddate.com/weather/china/beijing"

    # Captura del HTML y creación del objeto RESPONSE
    r = requests.get(url)
    data = r.text

    # Creación del objeto SOUP junto con los datos capturados con REQUEST
    soup = BeautifulSoup(data, "html.parser")

    # Búsqueda del div para extraer los grados
    temp = soup.find_all('div', class_="h2")

    # Búsqueda del div para extraer la sensación térmica
    sTerm = soup.find_all('div', class_="clear")

    # Con [0] se extrae el primer elemento y con [1] el segundo
    print ("La temperatura en Beijing: " + temp[0].text)
    print ("La sensación térmica: " + sTerm[1].text)

    # Tiempo en segundos para ejecutarse nuevamente
    time.sleep(15)

    # Borrado de datos viejos (Windows: cls - Linux/MAC: clear)
    os.system("clear")