'''
Diferencias entre peticiones CLIENTE a SERVIDOR: 
    
    · GET: agregamos datos a la petición con el par clave-valor
        --> fácil de marcar como favoritos (web browser)
        --> se puede utilizar para recuperar datos desde la barra de navegación (web browser)
        --> permite almacenar fácilmente los datos (porque puedes, por ejemplo, ver el código del producto)
        --> tiene limitación de longitud a 255 caracteres
        --> solo admite tipos de datos de cadena
        --> se puede almacenar en caché

        <-- no se puede utilizar para enviar documentos (imágenes, word...)
        <-- solo se pueden utilizar para recuperación de datos
        <-- no se puede utilizar para pasar información confidencial

    · POST: los datos se incluyen en el cuerpo del mensaje
        --> obtiene información del cuerpo del mensaje y de la propia cadena de consulta
        --> los datos de la consulta NO son visibles en la URL
        --> los parámetros no se guardan en el historial del web browser
        --> no hay restricción en el número de bytes enviado (normalmente sí)
        --> nos ayuda a pasar de forma confidencial data sensible (login, etc)
        --> admite cualquier tipo de dato (cadenas, binarios, numéricos...)
        --> difícilmente se puede almacenar en caché

        <-- no es posible guardar los datos, son invisibles en la URL
        <-- no es compatible con muchas configuraciones de Blue Team (defensa) y su hardware como firewall, etc
        <-- tarda la carga en el momento que se hace con un binario

--> Django se desencadena: MVC ---------------------------------------------------------------------------------->
A la hora de programar, sobre todo en apps y web apps, se utiliza el MVC (Modelo-Vista-Controlador). En el caso de
Django, es MVT (Modelo-Vista-Plantilla/Template).

Vayamos por partes, como dijo Jack el destripaor....

    · Model (M): datos y lógica de negocio
    · View (V): conecta la data con la presentación de usuario
    · Template (T): es la propia presentación de usuario

Que siiiiiiiiiiiiiii, ¿pero cómo funciona? El flujo de proceso
    1.- un cliente hace una petición: entrar a /productos
    2.- la VIEW, recibe la petición y le pide a MODEL, los datos del producto que estamos buscando a coger desde la BBDD
    3.- una vez recibe los datos desde la BBDD, el MODEL nos devuelve los datos directamente a la VIEW
    4.- la VIEW pasa los datos a la TEMPLATE
    5.- la TEMPLATE renderiza toda la información y se las proporciona a cliente

Renderización en web: 
    - compilar HTML y CSS para que podamos mostrar la web como tal
    - carga todo el código para que se muestre la página en cuestión, con la data solicitada
    - ¡¡CADA NAVEGADOR TIENE UN MOTOR DE RENDERIZACIÓN DIFERENTE!!
        . Google Chrome/Brave: blink buscador y su intérprete de JavaScript es V8
        . Mozilla Firefox/Tor Browser: Gecko y su intérprete de JavaScript es SpiderMonkey
        . Safari: WebKit y su intérprete de JavaScript es Nitro
        . Microsoft Edge: EdgeHTML y su intérprete de JavaScript es ChackraCore
        . Internet Explorer: Trident y su intérprete de JavaScript es Chakra

¿Cómo creamos una página web (y en nuestro caso) con Django?
    A.- PARTE CLIENTE (web browser) --> Template = FrontEnd
        · es la parte visible al usuario final
        · para su creación se utilizan las tecnologías/lenguaje de programación:
            . HTML5: es el lenguaje de marcado, el esqueleto de la web
            . CSS3: es la parte más decorativa, es decir, poner el resto de las cosas al esqueleto
            . JavaScript/framework JS: es más las acciones
        · esta parte genera el HTML que se va a recibir por parte del web browser
        · los datos vienen directamente desde la View

    B.- PARTE SERVIDOR (server) --> Model + View = BackEnd
        · View:
            . es la capa que recibe las peticiones
            · llama a Model para pedir los datos (y que se obtengan desde la BBDD)
            . es quién decide qué mostrar y cómo mostrar... o lo que es lo mismo, que Template utilizar

        · Model: 
            . se encarga de todo la lógica de cómo se manejan los datos
            . define la estructura de la información (tablas, campos y las relaciones en la BBDD que hay por detrás)
            . se encarga, también, de conectar con la BBDD, tanto en modo guardar como recuperar info
        
        · BBDD: es la fuente real de datos almacenados de forma persistente

El flujo de trabajo, paso a paso, quedaría:
    1.- el usuario realiza una petición (request) desde el navegador (web browser)
    2.- Django va a recibir esta petición en un archivo:
        --> archivo: urls.py
        --> en este archivo se definen la ruta y se decide qué View debería atender esa URL
    3.- el archivo urls.py nos dirige al nuevo archivo que contiene la View para atender la petición
        --> archivo: views.py
        --> en este archivo se da cabida a toda la lógica que tenemos que ejecutar al recibir la petición
        --> puede leer datos desde el Model (BBDD), procesar la información o también seleccionar la Template que se
        va a renderizar como resultado
    4.- se toman los datos:
        --> archivo: models.py
        --> define la estructura de datos y cómo se va a guardar o recuperar desde la BBDD
        --> se comunica directamente con la BBDD para lectura/escritura
    5.- se muestran los resultados obtenidos de la BBDD:
        --> archivo: templates/*.html
        --> es la capa de presentación: está hecha en HTML con Django Template Language
        --> recibimos los datos desde la View y los mostramos al usuario, simplemente
'''

