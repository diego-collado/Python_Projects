'''
LINK SCRAPPING
'''
from bs4 import BeautifulSoup
import requests

URL_BASE = input("Introduce la URL a comprobar: ")
MAX_PAGES = 20 # limitación del número de página a mostrar, es decir, profundidad de búsqueda
counter = 0

for i in range(1, MAX_PAGES):

    # Construcción de la URL
    if (i > 1):
        url = "%spage/%d/" % (URL_BASE, i)
    else:
        url = URL_BASE

    req = requests.get(url) # petición a la web. Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:
        # Se pasa el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Se obtienen todos los divs donde están las entradas (por ejemplo)
        entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

        # Se recorren todas las entradas para extraer el título, autor y fecha
        for entrada in entradas:
            counter += 1
            titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
            autor = entrada.find('span', {'class': 'autor'}).getText()
            fecha = entrada.find('span', {'class': 'fecha'}).getText()

            # Impresión del Título, Autor y Fecha de las entradas en formato "tabla"
            print ("%d - %s  |  %s  |  %s" % (counter, titulo, autor, fecha))

    else:
        break # Si ya no existe la página y da error 400