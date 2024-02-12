import requests
from bs4 import BeautifulSoup
import texttable as tt

# URL para extraer datos
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# Extracción del HTML de una URL
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') realiza un scrapping de cada elemento en la tabla de la URL
data_iterator = iter(soup.find_all('td'))

# data_iterator es el iterador de la tabla, cuyo ciclo seguirá repitiéndose hasta que haya datos disponibles
# en el iterador
while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text

        data.append((
            country,
            int(confirmed.replace(',', '')),
            int(deaths.replace(',', '')),
            continent
        ))

    # El error StopIteration se genera cuando no quedan más elementos para iterar
    except StopIteration:
        break

# Ordenación de los datos por el número de casos confirmados
data.sort(key=lambda row: row[1], reverse=True)

# crea texttable object, algo parecido a las tablas ASCII (sencillas, tipo impresora matricial)
table = tt.Texttable()

# Se agrega una fila vacía al principio para los encabezados
table.add_rows([(None, None, None, None)] + data)

# 'l' para izquierda, 'c' para centro y 'r' para derecha
table.set_cols_align(('c', 'c', 'c', 'c'))
table.header((' País ', ' Número de Casos ', ' Muertes ', ' Continente '))

print(table.draw())