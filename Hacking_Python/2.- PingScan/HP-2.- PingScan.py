'''
PingScan: encontrar máquinas activas en un segmento de red que utiliza un protocolo simple
para el intercambio de mensajes entre máquinas, el cual es conocido como ICMP. Este protocolo
permite sabes si una máquina determinada responde o no.
ICMP es de la capa de enlace, aunque aquí se utiliza en la capa de aplicación, como TRACEROUTE.

Se utiliza de forma indistinta en Windows, Linux o MacOS.


'''
# módulo subprocess permite lanzar nuevos procesos y gestionar los resultados
# (https://docs.python.org/es/3/library/subprocess.html)
from subprocess import Popen, PIPE

for ip in range(1,254):# para introducir el último octeto a la IP
	ipAddress = '192.168.1.'+str(ip)
	print("Escaneando... %s " %(ipAddress))
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	#creación de instancia de Popen en la que se indica que se va a ejecutar el comando ping
	# con los argumentos '-c 1 ', ipAddress
	stdout, stderr= subprocess.communicate(input=None)
	# captura el flujo de salida con el módulo .communicate

	if "bytes from " in stdout: #se busca la cadena bytes from
		print("La IP %s ha respondido con un ECHO_REPLY!" %(stdout.split()[1]))
		with open("ips.txt", "a") as myfile:
			myfile.write(stdout.split()[1]+'\n')