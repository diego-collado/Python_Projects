'''
Link extractor: aunque se parece a una herramienta SEO, este script es útil para enumerar
directorios de un sitio web.
Como es evidente, se debe tener cuidado en sitios web grandes, aunque se puede pasar un
parámetro de profundidad al script, si el sitio web tiene muchos enlaces los comprobará todos
de forma recursiva.
También puede enviar el resultado a un archivo con el parámetro -o opcional.

Ejecución en shell: sudo python3 linkextractor.py -u [URL] -d [depth] -o [filename]
Ejemplo: sudo python3 linkextractor.py -u https://loquesea.com -d 1 -o directorios.txt
'''

import requests, argparse, sys # módulos de sistema, petición de info a web y analizador automático (parse)
from urllib.parse import urlparse, urljoin # análisis de una URL en componentes
from bs4 import BeautifulSoup # análisis de documentos HTML - Python

internal_urls = set()
external_urls = set()

# Se determina que la URL que se envía sea válida. Se tiene en cuenta que sean resultados en 200 (conexión OK)
def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Se extrae la información de las URLs que estén disponibles
def get_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for tag in soup.findAll("a"):
        href = tag.attrs.get("href")
        if href == "" or href is None:
            continue

        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        # href = https + "://" + kobalto + formacion.es
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                print(f"[!] URL EXTERNA ···>  {href}")
                external_urls.add(href)
            continue
        print(f"[+] URL INTERNA ···>  {href}")
        urls.add(href)
        internal_urls.add(href)
    return urls

#  Se comienza a hacer crawling de links
def crawl(url, max_urls):
    total_urls_visited = 0
    total_urls_visited += 1

    print(f"[*] CRAWLING ···>  {url}")
    links = get_links(url)
    for link in links:
        if total_urls_visited > int(max_urls):
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url", help="URL para realizar crawl: ")
        parser.add_argument("-m", "--max", help="Máximo de URLs a extraer: ")
        parser.add_argument("-o", "--output", nargs="?")

        args = parser.parse_args()

        url = args.url
        max_urls = args.max
        output_file = args.output

        crawl(url, max_urls)

        if output_file:
            with open(output_file, "w") as f:
                for url in internal_urls:
                    if "http" in url:
                        print(url, file=f)
                    else:
                        pass

        print("\n" + "-" * 45)
        print("[*] TOTAL LINKS INTERNOS: ", len(internal_urls))
        print("[*] TOTAL LINKS EXTERNOS: ", len(external_urls))
        print("[*] TOTAL URLs: ", len(external_urls) + len(internal_urls))
        print("[*] TOTAL URLs CRAWLED: ", len(max_urls))
        print("-" * 45)

    except KeyboardInterrupt:
        if output_file:
            with open(output_file, "w") as f:
                for url in internal_urls:
                    if "http" in url:
                        print(url, file=f)
                    else:
                        pass

        print("\naBoRTaNDo eXTRaCCióN De LiNKS...")