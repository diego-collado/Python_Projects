'''
Extracción de datos y volcado a archivo CSV
'''

import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # recuperando elementos HTML de tipo quote en los <div> de la página
    quote_elements = soup.find_all('div', class_='quote')

    # iterando sobre la lista de elementos quote para extraer los datos de interés y almacenarlos entre comillas
    for quote_element in quote_elements:
        # extrayendo el texto de la quote
        text = quote_element.find('span', class_='text').text
        # extrayendo el autor de la quote
        author = quote_element.find('small', class_='author').text

        # extrayendo la etiqueta <a> elementos HTML relacionados con la cita (quote)
        tag_elements = quote_element.find('div', class_='tags').find_all('a', class_='tag')

        # almacenando la lista de cadenas de etiquetas en una lista
        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.text)

        # añadiendo un diccionario que contiene los datos de las citas en un nuevo formato en la lista de citas
        quotes.append(
            {
                'text': text,
                'author': author,
                'tags': ', '.join(tags)  # fusión de las etiquetas en una cadena "A, B, ..., Z"
            }
        )

# URL de la página de inicio del sitio web de destino
base_url = 'https://quotes.toscrape.com'

# Definiendo el encabezado User-Agent para usar en la solicitud GET
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# Recuperando la página web de destino
page = requests.get(base_url, headers=headers)

# Analizando la página web de destino con Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# Inicializando la variable que contendrá la lista de todos los datos de las citas
quotes = []

# scraping de la página principal
scrape_page(soup, quotes)

# Obteniendo el elemento HTML "Siguiente →"
next_li_element = soup.find('li', class_='next')

# Si hay una página siguiente para hacer scrapping
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # Obteniendo la nueva pagina
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # Analizando la nueva página
    soup = BeautifulSoup(page.text, 'html.parser')

    # Haciendo scrapping a la nueva página
    scrape_page(soup, quotes)

    # Buscando el elemento HTML "Siguiente →" en la nueva página
    next_li_element = soup.find('li', class_='next')

# Lectura del archivo "quotes.csv" y crearlo si no está
csv_file = open('quotes.csv', 'w', encoding='utf-8', newline='')

# inicializando el objeto escritor para insertar datos en el archivo CSV
writer = csv.writer(csv_file)

# Escribiendo el encabezado del archivo CSV
writer.writerow(['Text', 'Author', 'Tags'])

# Escribir cada fila del CSV
for quote in quotes:
    writer.writerow(quote.values())

# Cierre del CSV, liberando recursos del sistema
csv_file.close()