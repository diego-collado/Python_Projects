'''
Rastreador de precios en Amazon: se rastrea la URL:
https://www.amazon.com/-/es/Samsung-DS-Dynamic-Unlocked-Smartphone/dp/B07WV6BY5S/ref=sr_1_9?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=JYU71JQXJVWI&dchild=1&keywords=xiaomi+mi+10+pro&qid=1609348165&sprefix=xiaomi%2Caps%2C381&sr=8-9

Comandos SMTP:
    - HELO: para abrir una sesión con el servidor.
    - EHLO: para abrir una sesión, en el caso de que el servidor soporte extensiones definidas en el RFC 1651.
    - MAIL FROM: para indicar quien envía el mensaje.
    - RCPT TO: para indicar el destinatario del mensaje.
    - DATA: para indicar el comienzo del mensaje, este finalizará cuando haya una línea únicamente con un punto.
    - QUIT: para cerrar la sesión.

    - RSET: para abortar la transacción en curso y borra todos los registros.
    - SEND: para iniciar una transacción en la cual el mensaje se entrega a una terminal.
    - VRFY: para solicitar al servidor la verificación de un argumento.
    - EXPN: para solicitar al servidor la confirmación del argumento.
    - HELP: para solicitar información sobre un comando.
'''
#IMPORT
import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/-/es/Samsung-DS-Dynamic-Unlocked-Smartphone/dp/B07WV6BY5S/ref=sr_1_9?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=JYU71JQXJVWI&dchild=1&keywords=xiaomi+mi+10+pro&qid=1609348165&sprefix=xiaomi%2Caps%2C381&sr=8-9'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


def rastrear_precio():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    producto = soup.find(id="productTitle").get_text().strip()
    precio = soup.find(id="priceblock_ourprice").get_text().strip()
    precio_convertido = float(precio[4:])

    if (precio_convertido < 800):
        enviar_correo(producto, precio)
def enviar_correo(producto, precio):
    fromaddr = 'tucorreo@gmail.com' # desde qué correo se hace el aviso
    toaddrs = 'destino@gmail.com' # a qué correo le llegará el aviso

    # Datos de GMAIL, para acceder al envío de emails
    username = 'tucorreo@gmail.com'
    password = 'password'

    # Enviando el correo en base a GMAIL: abrir sesión, comenzar conexión cifrada...
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password) # se realiza el login en gmail

    subject = 'El precio bajo del producto solicitado'
    body = 'Revisar el siguiente link de amazon: ' + URL

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        fromaddr,
        toaddrs,
        msg
    )
    print("HEEEEEY, el producto bajó su precio")
    server.quit()


while True:
    rastrear_precio()
    time.sleep(20)