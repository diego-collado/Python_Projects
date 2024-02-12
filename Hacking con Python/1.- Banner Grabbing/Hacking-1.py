'''
BANNER GRABBING: técnica de FingerPrint utiliza para el descubrimiento de las versiones
de servicios en Internet (server).
Ejemplo visual: https://www.thesecuritybuddy.com/wordpress/bdr/uploads/2020/08/BannerGrabbing.jpg.webp
+ INFO:
    - https://developer.mozilla.org/es/docs/Web/HTTP/Headers
    - https://www.webempresa.com/blog/cabeceras-http-mas-comunes.html
    - https://developer.mozilla.org/es/docs/Web/HTTP/Status

UNA WEB SIEMPRE "ARRANCA" GRACIAS AL ARCHIVO index.html // index.php, SIEMPRE Y CUANDO
EL SERVIDOR AL QUE HAGO LA PETICIÓN SEA LINUX, ES DECIR, QUE LOS SITES QUE ESTÉN EN ESE
SERVIDOR, SE EJECUTEN BAJOS SISTEMAS OPERATIVOS TIPO OPEN SOURCE.

WINDOWS (SERVER) SE UTILIZA PARA SITES QUE TIENEN BASTANTE "CHICHA" A NIVEL DE BBDD, PARA
LO QUE SE UTILIZA UN LENGUAJE ESPECÍFICO Y PROPIETARIO DE MICROSOFT: .NET (SITES CON index.asp)
Se obtiene -------------------------------------------------------------------------------
    - servicio
    - puerto que utiliza
    - versión del servicio
    - posible sistema operativo, subversión...
    - protocolo y su versión

    - puertos - servicios - aplicaciones que son vulnerables e inseguras:
        · qué puedo comprometer
        · qué vulnerabilidad tengo disponible del sistema, servicio o protocolo --> CVE
        · exploit a medida (malware)

Cómo realizamos el Banner Grabbing (linux) -------------------------------------------------

	- NetCat: nc IP PUERTO
	- NMAP: nmap -sV IP -p PUERTO –script=banner
			nmap -sV IP -p PUERTO

    - Whatweb: whatweb IP/DOMINIO
    - Wget: wget IP -q -S
			· -q suprimirá la salida normal
			· -S imprimirá los encabezados enviados por el servidor HTTP Y FTP

    - cURL:  curl -s -I IP | grep -e «Server:»
			· -s se usa para evitar mostrar el progreso o mensajes de error
			· -I mostrará el encabezado de todas las páginas solicitadas

	- DMitry: dmitry -bp IP
			· -p para el escaneo de puertos
			· -b para permitirte realizar el descubrimiento de banners

Tipos de Banner Grabbing --------------------------------------------------------------------
    - ACTIVO --> Este es el tipo más popular de captura de banners, básicamente el acto de enviar
    paquetes al host remoto y esperar su respuesta para analizar los datos.
    - PASIVO --> Permite obtener la misma información mientras evita un alto nivel de exposición
    de la conexión de origen. Se pueden usar diferentes plataformas y software intermedios como
    puerta de enlace para evitar una conexión directa y aún así permitirte obtener los datos que
    necesitas.

Cómo prevenir un 'ataque' de este tipo -------------------------------------------------------
1. Eliminar o cambiar la información de banner
2. Filtrado de paquetes con un firewall
3. Enmascaramiento de versiones
4. Mantener actualizado el software instalado
5. Utilizar herramientas de seguridad - IPS, IDS...
6. Restringir el acceso a los servicios en la red
7. Apagar los servicios no utilizados o innecesarios que se ejecutan en hosts de red
8. Anular el comportamiento de banner predeterminado del servidor para ocultar información de la versión
9. Mantener el servidor y sistemas actualizados para protegernos contra las vulnerabilidades

Ejecutando nuestro py en Linux ---------------------------------------------------------------
Necesitamos crear 2 listados: port.txt y vulnbanners.txt

port.txt modo ejemplo:
    22
    21
    23
vulnbanners.txt modo ejemplo:
    SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1\n
    220 ProFTPD 1.3.1 Server (Debian)
    Apache/2.4.18 CVE-2016-4979
    Apache/2.3.20 CVE-2016-4438
    Apache HTTP Server 2.4.49

URLS PARA OBTENER VULNBANNERS:
    - https://github.com/richlamdev/ssh-default-banners

python Hacking-1.py 192.168.1.

192.168.1. --> es el segmento de red al cual le hago BannerGrabbing
'''

#IMPORTS -------------------------------------------------------------------------------------
import socket # módulo comunicación en red y manejo de datos
# (https://docs.python.org/es/3.10/library/socket.html)
import sys # módulo variables/funciones interacción con el sistema operativo
# (https://docs.python.org/es/3/library/sys.html)

#MAIN ----------------------------------------------------------------------------------------
# 1.- abrimos las comunicaciones creando un socket IPv4 con protocolo TCP/IP
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
SOCKET
¿de hasta? De dónde conecto y hasta dónde conecto... Cliente - Servidor (arquitectura Cliente-Servidor)
1. coger el teléfono
    crear un socket
2. marcar el número
    introducir la ip en el socket
3. llamar
    hacer la petición al servidor desde el socket
4. recibir respuesta
    recibir la respuesta en el socket
5. tomar la decisión hasta finalizar la llamada
    tomar datos... hasta cerra comunicación desde el socket
'''
#  socket es un enlace entre dos aplicaciones que pueden comunicarse entre sí (ya sea localmente en una sola máquina o a distancia entre dos máquinas en ubicaciones separadas)


# 2.- analizaremos todas las direcciones IP que queramos, comprobando el banner disponible con nuestro diccionario
for host in range(0, 254): #número de maquínas que comprobar (último octeto de la IP X.X.X.[IP])
    # lectura de diccionarios con puertos y banners vulnerables (ya hechos)
    ports = open('ports.txt', 'r') # txt con los puertos a revisar (21, 22, ...)
    vulnbanners = open('vulnbanners.txt', 'r') #txt con los banners que corresponden a servicios vulnerables

    # compara los txt con la realidad en la red
    for port in ports:
        try:
            # A.- conexión de la comunicación - apertura de comunicaciones
            socket.connect((str(sys.argv[1]+'.'+str(host)), int(port)))
            #socket.connect((lo_que_me_das + . + host (0-254), puerto
            # sys.argv[1] representa la lista de todos los posibles argumentos de sistema que podría pasarnos
            # la info del sistema es el segmento de red que le proporcionamos
            print("Conectando a "+str(sys.argv[1]+'.'+str(host))+" en el puerto: "+str(port))
            socket.settimeout(1000)# espera de 1 seg

            # B.- recuperación del banner
            banner = socket.recv(1024)
            # recv = se utiliza para recuperar datos de un socket (TCP/UDP)
            # 1024 = tamaño del paquete en bytes, tamaño aprox. 1MB
            # (cabecera TCP, tamaño mínimo 20 bytes - tamaño máximo 65.495 bytes)

            # C.- comparativa de datos recuperados contra diccionarios
            for vulnbanner in vulnbanners:
                if banner.strip() in vulnbanner.strip(): # comparación de lo obtenido con el diccionario
                    print("¡Hay vulnerabilidad! La hemos encontrado en: "+banner)
                    print("Host: "+str(sys.argv[1]+'.'+str(host)))
                    print("Puerto: "+str(port))
        except:
            print("Error en la conexión a "+str(sys.argv[1]+'.'+str(host))+':'+str(port))
            pass
            # Error en la conexión a 192.168.1.34:25