'''
LINK SCRAPPING: permite extraer los datos de los links activos, como de las redirecciones de la web (301)
A utilizar (según proyecto):
    - librerías REQUESTS y BEAUTIFUL SOUP (de manera independiente o conjunta)
    - FRAMEWORK SCRAPY, el cual permite hacer scrapping (extracción de info de la web)
    y crawling (descubrimiento de enlaces y navegación entre los mismos)

BEAUTIFUL SOUP: es una librería Python que permite extraer información de contenido del formato HTML o XML.
Todos los websites están escritos en HTML + CSS o tienen contenido en XML.
Para su uso, debemos especificar un PARSER, que se encarga de transformar un documento HTML/XML a un árbol de
objetos de Python.

Para qué sirve esta librería: web scrapping, análisis de datos y vulnerabilidades, Data Science, Machine Learning...

Tipos de objetos utiliza Beautiful Soup:
    · TAG: se corresponde con una etiqueta HTML o XML, por lo que se puede acceder a cualquiera de sus atributos
    tratando al objeto accedido como si fuese un diccionario.
    · NAVIGABLESTRING: representa la cadena de texto contenida en la etiqueta en cuestión, donde también podemos
    llegar a encontrar la siguiente información:
        -- Comment: esta clase representa un comentario HTML
        -- Stylesheet: esta clase representa un código CSS embebido
        -- Script: esta clase representa un código Javascript embebido

Ejemplo de página VS Beautiful Soup:

A.- El ejemplo HTML --------------------------------------------------------------------------
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página de prueba</title>
</head>
<body>
<div id="main" class="full-width">
    <h1>El título de la página</h1>
    <p>Este es el primer párrafo</p>
    <p>Este es el segundo párrafo</p>
    <div id="innerDiv">
        <div class="links">
            <a href="https://pagina1.xyz/">Enlace 1</a>
            <a href="https://pagina2.xyz/">Enlace 2</a>
        </div>
        <div class="right">
            <div class="links">
                <a href="https://pagina3.xyz/">Enlace 3</a>
                <a href="https://pagina4.xyz/">Enlace 4</a>
            </div>
        </div>
    </div>
    <div id="footer">
        <!-- El footer -->
        <p>Este párrafo está en el footer</p>
        <div class="links footer-links">
            <a href="https://pagina5.xyz/">Enlace 5</a>
        </div>
    </div>
</div>
</body>
</html>

B.- Traduciendo a Beautiful Soup --------------------------------------------------------------------------
from bs4 import BeautifulSoup
contenido = """
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Página de prueba</title>
        </head>
        <body>
        <div id="main" class="full-width">
            <h1>El título de la página</h1>
            <p>Este es el primer párrafo</p>
            ...
        </div>
        </body>
        </html>
"""
sopa = BeautifulSoup(contenido, 'lxml')

C.- Objetos HTML - Beautiful Soup --------------------------------------------------------------------------
    - Tag:  sopa.title --> <title>Página de prueba</title>
            div_main = sopa.div --> div_main['id'] = main
            div_main.attrs --> {'id': 'main', 'class': ['full-width']}

    - NavigableString:
            primer_parrafo = sopa.p
            texto = primer_parrafo.string --> texto 'Este es el primer párrafo'
            type (texto) --> <class 'bs4.element.NavigableString'>

D.- Navegando por Beautiful Soup --------------------------------------------------------------------------
Es posible acceder a los objetos del árbol utilizando los nombres de las etiquetas como atributos, una de las
formas más simples de navegar a través del árbol.

    sopa.meta['charset'] --> 'UTF-8'
    sopa.div.div.div --><div class="links">
                            <a href="https://pagina1.xyz/">Enlace 1</a>
                            <a href="https://pagina2.xyz/">Enlace 2</a>
                        </div>


E.- Utilizando el filtrado con Beautiful Soup --------------------------------------------------------------------------
    - Filtro por clase/selector CSS:
        · links_divs = soup.find_all('div', class_="links")
        · footer_links = soup.find_all(class_="links footer-links")

    - Filtro por clase CSS que coincidan con 2 o más clases:
        · footer_links = soup.select('div.footer-links.links')

    - Filtrado para 1 único objeto (opción más optimizada)
        · soup.find('title')

    - Filtrado por localización elementos:
        · Por tipo: soup.find_all(type='text')
        · Por contenido: soup.find_all('h2', string='Formulario')
        · Mediante expresiones regulares: soup.find_all(re.compile(r'^h\d+.*'))
        · Múltiples elementos: soup.find_all(['input', 'span'])

Extracción de datos de múltiples páginas:
def extraer_datos(url):
    # Aquí va el código para extraer los datos de una página
    respuesta = requests.get(url)
    contenido = respuesta.content
    soup = BeautifulSoup(contenido, "html.parser")
    # Aquí continúa el proceso de extracción

for pagina in range(1, 6):  # Suponiendo que hay 5 páginas
    url = f"https://ejemplo.com/lista-pag-{pagina}"
    extraer_datos(url)


***************************************************************************************************
*************** MÁS INFO: https://www.crummy.com/software/BeautifulSoup/bs4/doc.es/ ***************
***************************************************************************************************

------------------- PASOS A REALIZAR EN UN BUEN SCRAPPING WEB -------------------

    1.- IDENTIFICACIÓN DE ELEMENTOS A EXTRAER: todos los websites, están creados en un tipo de documento
    jerarquizado mediante elementos, por lo que se hace imprescindible identificar correctamente el elemento
    o elementos que contienen la información deseada.
    Lo más común: abrir la web en el browser e inspeccionar elemento a elemento
    Después de "conocer" los elementos que podrían tener información asociada, tendremos que utilizarlos para
    poder extraer la info con Beautiful Soup

    2.- DESCARGA DE CONTENIDO DE LA PÁGINA: para esta acción, utilizamos la librería REQUESTS, ya que el contenido
    de la respuesta será el que procese Beautiful Soup para crear la estructura de elementos y poder realizar consultas
    a ese árbol

    3.- CREAR LA "SOPA": el contenido que habíamos chequeado en el paso 2, se utiliza para crear la "sopa", la cual
    realmente es la estructura de árbol de objetos de Python que representan el HTML completo. Se creará un objeto
    de tipo BeautifulSoup, al cual se pasa el HTML y el identificador del parser a utilizar:

        import requests                                     --> para adquirir contenido de respuesta
        from bs4 import BeautifulSoup                       --> para traducir HTML a Python
        r = requests.get('http://lapaginaquesea.loquesea')  --> recuperamos el contenido de la respuesta web
        sopa = BeautifulSoup(r.text, 'lxml')                --> utilizamos el parser (lectura-conversión)

    4.- BÚSQUEDA DE LOS ELEMENTOS DE INTERÉS Y OBTENCIÓN DE INFO DE LA "SOPA": buscar la información en el árbol
    de objetos Python, los cuales ya contendrán la información que necesitamos.
'''

#IMPORTS
import requests
from bs4 import BeautifulSoup # importación de la biblioteca BeautifulSoup

# MÉTODOS UTILIZADOS
def extract_all_links(site):
    html = requests.get(site).text # solicitud al site para convertirlo a texto
    soup = BeautifulSoup(html, "html.parser").find_all("a")
    # encuentra los enlaces en el texto que te he pasado y que re-traduces a Python
    #BeautifulSoup(web_a_scrappear, "parser_del_lenguaje").filtramos_por_atributo("atributo_a_buscar")

    links = [link.get("href") for link in soup] # buscamos realmente el link (redirección) en la "sopa"
    return links

#MAIN
if __name__ == "__main__":
    # permite manejar de una mejor forma el código:
        # se permite iniciar ciertas líneas de código
        # si se está ejecutando el programa desde el intérprete, las cuales no se pueden iniciar
        # si el código es importado
    site_link = input("Introduce la URL a comprobar: ")
    all_links = extract_all_links(site_link)
    print(all_links)