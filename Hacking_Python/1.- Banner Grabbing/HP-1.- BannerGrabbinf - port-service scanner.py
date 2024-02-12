# Utilización: script.py direcciónIP puerto_inicial puerto_final

import sys
from datetime import datetime
import socket

if len(sys.argv) != 4:
    print ('El script utiliza 4 parámetros, dados: ', len(sys.argv))
    sys.exit(0)
else:
    pass

# guardado de argumentos envíados desde el sistema y realización del casting
addr = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

def scanport(addr, port):
    '''Chequeando si el puerto está abierto en el host'''
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = socket_obj.connect_ex((addr,port))
    socket_obj.close()

    if result == 0:
        machine_hostname = socket.gethostbyaddr(addr)[0]
        service = socket.getservbyport(port)
        print (" --> puerto detectado: " + str(addr) + " \t-- Puerto: " + str(port) + " \t-- Servicio: " + str(service) + " \t-- Hostname: " + str(machine_hostname))
        return port
    else:
        return None


def bannergrabbing(addr, port):
    '''Connect to process and return application banner'''
    print ("Gettig service information for port: ", port)
    bannergrabber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    try:
        bannergrabber.connect((addr, port))
        bannergrabber.send('WhoAreYou\r\n')
        banner = bannergrabber.recv(100)
        bannergrabber.close()
        print (banner, "\n")
    except:
        print ("Cannot connect to port ", port)

    
def portscanner(address, start, end):
    open_ports = []
    # scan port range for host
    for port in range(start_port, end_port):
        open_port = scanport(addr, port)
        if open_port is None:
            continue
        else:
            open_ports.append(open_port)
    return open_ports

def get_service_banners_for_host(address, portlist):
    for port in portlist:
        bannergrabbing(addr, port)



if __name__=='__main__':
    open_ports = portscanner(addr, start_port, end_port)

    get_service_banners_for_host(addr, open_ports)
