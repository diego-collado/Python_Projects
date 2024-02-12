'''
Quote Spider: extraemos en un fichero los comentarios de un site.

Ejecución en shell: sudo python3 extractor.py --o [filename.ext]
Ejemplo: sudo python3 extractor.py -o quotes.json

Tamnbién se puede utilizar el siguiente script:

import scrapy
from scrapy.linkextractors import LinkExtractor


class Spider(scrapy.Spider):
    name = "Spider"
    start_urls = ["URL_que_prefieras"]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        self.link_extractor = LinkExtractor(unique=True)

    def parse(self, response):
        links = self.link_extractor.extract_links(response)

        for link in links:
            yield {"Enlaces nofollow": link.nofollow, "url": link.url, "text": link.text}

'''

import scrapy
from scrapy.linkextractors import LinkExtractor


class QuoteSpider(scrapy.Spider):
    name = "OuoteSpider"
    start_urls = ["https://www.kobalto.es/"]

    def parse(self, response):
        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)

        for link in links:
            yield {"url": link.url, "text": link.text}