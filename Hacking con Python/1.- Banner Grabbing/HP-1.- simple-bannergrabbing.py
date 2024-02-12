'''
Banner Grabbing (FINGERPRINT): técnica que se utiliza para el descubrimiento de versiones de servicios
en Internet. Para obtener información de esta forma, el protocolo/servicio que se esté
ejecutando debe devolver un banner.
Ejecutar un ataque de captura de banner contra cualquier protocolo puede revelar aplicaciones
inseguras y vulnerables que podrían conducir a la explotación y el compromiso del servicio,
en el caso de coincidir con un CVE crítico.

ACTIVO --> Este es el tipo más popular de captura de banners, básicamente el acto de enviar
paquetes al host remoto y esperar su respuesta para analizar los datos.
Aquí está implicada la captura de paquetes TCP, con lo cual nos podrían llegar a detectar más fácilmente.

PASIVO --> Permite obtener la misma información mientras evita un alto nivel de exposición
de la conexión de origen. Se pueden usar diferentes plataformas y software intermedios como
puerta de enlace para evitar una conexión directa y aún así permitirte obtener los datos que
necesitas.

CÓMO REALIZAR BANNER-GRABBING ---------------------------------------------------------------
	- NetCat: nc IP PUERTO
	- Telnet: telnet IP PUERTO
	- NMAP: nmap -sV IP -p PUERTO –script=banner
			nmap -sV IP -p PUERTO
	- Whatweb: whatweb IP/DOMINIO
	- Wget: wget IP -q -S
			· -Q suprimirá la salida normal
			· -S imprimirá los encabezados enviados por el servidor HTTP Y FTP
	- cURL:  curl -s -I IP | grep -e «Server:»
			· -s se usa para evitar mostrar el progreso o mensajes de error
			· -I mostrará el encabezado de todas las páginas solicitadas

	- DMitry: dmitry -bp IP
			· -p para el escaneo de puertos
			· -b para permitirte realizar el descubrimiento de banners

CÓMO PREVENIR -------------------------------------------------------------------------------
1. Eliminar o cambiar la información de banner
2. Filtrado de paquetes con un firewall
3. Enmascaramiento de versiones
4. Mantener actualizado el software instalado
5. Utilizar herramientas de seguridad
6. Restringir el acceso a los servicios en la red
7. Apagar los servicios no utilizados o innecesarios que se ejecutan en hosts de red
8. Anular el comportamiento de banner predeterminado del servidor para ocultar información de la versión
9. Mantener el servidor y sistemas actualizados para protegernos contra las vulnerabilidades

EJECUCIÓN EN LINUX ----------------------------------------------------------------------
python simple-bannergrabbing.py 192.168.1
-- necesitamos listado de puertos (port.txt) y de banners (vulnbanners.txt)

MÁS INFORMACIÓN ADICIONAL:
	- https://developer.mozilla.org/es/docs/Web/HTTP/Messages
	- https://developer.mozilla.org/es/docs/Web/HTTP/Status
'''
#módulo comunicación en red, manejo de datos (https://docs.python.org/es/3.10/library/socket.html)
import socket
#módulo variables/funciones interacción con sistema operativo (https://docs.python.org/es/3/library/sys.html)
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Creación de un sockect IPv4 con protocolo TCP/IP
for host in range(0, 80): #número de las máquinas a recorrer (IP)
	ports = open('ports.txt', 'r') #txt con los puertos a revisar (21, 22, ...)
	vulnbanners = open('vulnbanners.txt', 'r') #txt con los banners que corresponden a servicios vulnerables
	for port in ports:
		try:
			socket.connect((str(sys.argv[1]+'.'+str(host)), int(port) ))# apertura conexión
			print('Conectando a '+str(sys.argv[1]+'.'+str(host))+' en el puerto: '+str(port))
			socket.settimeout(1)#espera de 1 seg
			banner = socket.recv(1024)# recuperación de banner
			for vulnbanner in vulnbanners:
				if banner.strip() in vulnbanner.strip():# comparación banner encontrado con lista
					print('¡Hay un banner vulnerable! '+banner)
					print('Host: '+str(sys.argv[1]+'.'+str(host)))
					print('Puerto: '+str(port))
		except :
			print('No se ha encontrado Banner en: '+str(sys.argv[1]+'.'+str(host)) +':'+ str(port))
			pass
'''
## Protocolo TCP: protocolo de navegación (uno de los más utilizados)
Tranfer Control Protocol y está muy orientado a la conexión entre cliente-servidor, lo que implica:
	- transmitir una determinada información entre un dispositivo y otro
	- verificar la correcta recepción de la información transmitida entre un dispositivo y otro
Realmente, controlar la conexión de extremo a extremo, como complemente al protocolo IP. Sigue estos pasos:

	1.- establece una conexión entre el dispositivo emisor y el dispositivo receptor (negociación)
		- se autoriza la conexión entre ambos dispositivos gracias a la negociación
	2.- verifica de forma continua la emisión y recepción de la información entre ambos:
		- divide la información en segmentos ordenados antes de transmitirlos por el protocolo IP
	3.- el número de secuencia es verificado por el dispositivo receptor, por lo que si faltase algo de info,
	el protocolo TCP solicita el envío de esta información "perdida" (segmentos) por medio del protocolo IP.ç
	4.- se hace hasta que la información llega de forma completa al dispositivo receptor
	5.- se cierra la conexión para evitar problemas

Al ser un protocolo FIABLE, soporta protocolos de otras características como HTTP, SMTP, SSH, FTP y otros.
En el protocolo TCP los datos se entregan en el mismo orden en el que se enviaron, aunque el envío esté realizado
por "trozos" de información, los cuales van a viajar siempre por la ruta más rápida, independientemente de la 
distancia real que tengamos entre redes o servidores.

## Protocolo IP: enruta y direcciona paquetes de información para que viajen a través de la red de modo que,
una vez enviamos los paquetes a Internet, estos se "trocean" en paquetes más pequeños y se envían. 
Además del paquete de información como tal, tenemos una info añadida que ayuda a los enrutadores (routers/switch) a
poder dirigir correctamente cada paquete.
A cada dispositivo o dominio que se conecta a Internet se le asigna una dirección IP y a medida que los paquetes se 
dirigen a la dirección IP, los datos llegan a donde se necesitan.
Por desgracia, por sí solo, tiene muchos fallos de seguridad (pérdida de datos durante la transferencia), con lo que 
deberíamos conbinarlo con otros protocolos más seguros, como por ejemplo el protocolo TCP.

## Paquete IP: Los paquetes IP se crean al añadir un encabezado IP a cada paquete de datos antes de enviarlo.
## Encabezado IP: una serie de bits (unos y ceros), y registra varios datos sobre el paquete, como la dirección IP 
de envío y de recepción. Estos encabezados nos informan, además, de:
	- longitud de encabezado												- longitud del paquete
	- tiempo de vida (TTL, saltos de red antes de descartar el paquete)		- protocolo que lo transporta (TCP, UDP..)

En total, hay 14 campos de información en los encabezados IPv4, aunque uno de ellos es opcional.

#Datagrama IP: unidad básica de transferencia en una red IP, el cual consiste en una cabecera IP y un campo de datos.
Tiene una longitud máxima de 1.500 bytes (ethernet).
IP puede llevar a cabo la fragmentación y re-ensamblaje de sus datagramas, cuya longitud máxima por datagrama suele
ser de 65.535 bytes.

IPv4 --> tiene una cabecera de (máximo) 32 bits, cuyos campos son:
	Versión: lleva el registro de la versión del protocolo al que pertenece el datagrama
	IHL: indica la longitud completa de la cabecera IP
	Tipo de servicio (TOS): permite al host indicar la calidad del servicio (RFC 791):
		Preferencia: naturaleza y prioridad del datagrama
		TOS: especifica el valor del tipo de servicio:
		 	1000 - el paquete solicita minimizar la demora
		 	0100 - el paquete solicita maximizar la transferencia
		 	0010 - el paquete solicita maximizar la fiabilidad
		 	0000 - servicio normal
		Bit de comprobación (MBZ)
	Longitud total: longitud total del datagrama, cabecera y datos (máximo 65.535 bytes)
	Identificación: valor único asignado al datagrama por el emisor que permite identificar a que datagrama pertenece
	el fragmento
	Desplazamiento del fragmento: indica en qué parte del datagrama actual va este fragmento
	Indicadores:
		Flag DF: significa no fragmentar
		Flag MF: significa más fragmentos
	Tiempo de vida: contador que sirve para limitar la vida del paquete
	Protocolo: indica la capa de transporte a la que debe entregarse (TCP o UDP o algún otro)
	Direcciones IP origen y destino: Direcciones origen y destino del datagrama
	Suma de comprobación de la cabecera (CHECKSUM): verifica solamente a la cabecera
	Opciones: 
		- Seguridad
		- Enrutamiento estricto desde el origen
		- Enrutamiento libre desde el origen
		- Registrar ruta
		- Marca de tiempo

MÁS INFORMACIÓN: https://www.youtube.com/watch?app=desktop&v=AGVLFjdOU5I
################################################################################################################
##TCP/IP: seguimos los pasos de TCP, garantizando que la información llegue a su destino, con acuse de recibo por parte
del dispositivo receptor. No se envían más paquetes si el receptor no emite el acuse de recibo.
TCP e IP se diseñaron originalmente para ser utilizados juntos, y a menudo se les conoce como el conjunto TCP/IP. 
'''