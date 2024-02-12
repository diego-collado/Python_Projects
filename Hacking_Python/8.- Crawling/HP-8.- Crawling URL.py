'''
DIFERENCIAS:
    - Scraping: raspado web, sistema de extracción de datos de una o varias páginas web. Posee módulos:
        · downloader o descargador
        · Scrapy Engine o motor
        · requests o solicitudes
        · answers o respuestas
        · crawlers o arañas web.

    - Crawling: método de extracción que, principalmente, se basa en el envío de spiders a la recolección
    de páginas web existentes relacionadas con el comando de búsqueda

_-_-_-_-_-_ Principales diferencias del Scraping vs Crawling _-_-_-_-_-_
    --> discrepancia principal: radica en el enfoque:
        · scraping responde a cualquier tipo de datos encontrado en las páginas web
        · crawling recolecta, únicamente, los hipervínculos de un sitio web
    --> CRAWLER <--
        · indexa, descubre y genera fuentes de datos
        · hace clic en los datos por ti
        · va de la mano con la parte web

    --> SCRAPER <--
        · procesa datos con reglas lógicas y extrae los datos estructurados
        · extraer datos de esos sitios en los que has clicado
        · se podrá scrapear una BBDD, incluso, podrás llegar a scrapear una API.

---- Arañas web o crawlers ----
Son programas (normalmente son robots) que inspeccionan páginas de la web de una forma metódica y automatizada.
Su uso más frecuente se centra en:
    - Crear una copia de todas las webs visitadas.
    - Procesarlas posteriormente para un motor de búsqueda que indexe esas páginas.
    - Crear un sistema de búsquedas rápidas.

Funcionamiento:
    - Visitan una serie URLs
    - Se descarga el contenido de esas páginas, para lo cual hay que realizar un web scraping
    - Identifican los hiperenlaces
    - La araña web va a visitar recursivamente estos hiperenlaces.
    - Descarga las nuevas páginas.
    - Analiza los nuevos enlaces.
'''
#IMPORTS
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Fallo al realizar crawling: {url}')
            finally:
                self.visited_urls.append(url)

if __name__ == '__main__':
    Crawler(urls=['https://kobalto.es/']).run()